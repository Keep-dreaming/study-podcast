"""Make an MP3 for every episode script that does not have one yet.

Usage:
    python scripts/make_audio.py           # generate the missing MP3s
    python scripts/make_audio.py --check   # only list what is missing

What happens for each missing episode:
  1. The script is split into paragraphs and [pause] markers.
  2. Piper (offline text-to-speech) speaks each paragraph. It returns one
     audio chunk per sentence.
  3. All chunks go into one WAV file, with silence added between
     sentences and between paragraphs so it doesn't sound rushed.
  4. ffmpeg converts the WAV into a small mono MP3 and evens out the
     loudness, then the MP3 is saved as audio/<script name>.mp3.

An episode "has audio" when audio/<script name>.mp3 exists, so to
re-record one, delete its MP3 and run this again.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import time
import wave
from pathlib import Path

from common import (
    AUDIO_DIR,
    VOICES_DIR,
    Episode,
    apply_pronunciations,
    load_config,
    load_episodes,
    split_into_blocks,
)

LEAD_IN_SECONDS = 0.6   # silence at the very start (some players clip it)
TAIL_SECONDS = 1.5      # silence at the very end


def set_github_output(**values: str) -> None:
    """Pass values to later workflow steps (see the workflow YAML).

    GitHub Actions gives each step a file path in $GITHUB_OUTPUT. Lines of
    the form name=value written there become steps.<id>.outputs.<name>.
    Outside GitHub Actions the variable is not set and this does nothing.
    """
    path = os.environ.get("GITHUB_OUTPUT")
    if path:
        with open(path, "a", encoding="utf-8") as f:
            for name, value in values.items():
                f.write(f"{name}={value}\n")


def load_voice(model: str):
    from piper import PiperVoice  # imported here so --check works without Piper

    model_path = VOICES_DIR / f"{model}.onnx"
    if not model_path.exists():
        sys.exit(
            f"ERROR: voice model {model_path} not found. Download it with:\n"
            f"  python3 -m piper.download_voices --download-dir voices {model}"
        )
    return PiperVoice.load(model_path)


def synthesize_to_wav(episode: Episode, voice, config: dict, wav_path: Path) -> int:
    """Speak the episode into a WAV file. Returns the number of paragraphs."""
    from piper import SynthesisConfig

    vcfg = config["voice"]
    syn_config = SynthesisConfig(length_scale=vcfg.get("length_scale"))
    pronounce = config.get("pronounce", {})
    rate = voice.config.sample_rate

    def silence(seconds: float) -> bytes:
        return b"\x00\x00" * int(rate * seconds)  # 16-bit samples of zero

    blocks = split_into_blocks(episode.body, vcfg.get("default_marker_pause", 3.0))
    speech_blocks = [b for b in blocks if b[0] == "speech"]

    with wave.open(str(wav_path), "wb") as wav:
        wav.setnchannels(1)   # mono
        wav.setsampwidth(2)   # 16-bit
        wav.setframerate(rate)
        wav.writeframes(silence(LEAD_IN_SECONDS))

        previous = None
        done = 0
        for kind, value in blocks:
            if kind == "pause":
                wav.writeframes(silence(value))
            else:
                if previous == "speech":
                    wav.writeframes(silence(vcfg["paragraph_pause"]))
                text = apply_pronunciations(value, pronounce)
                for i, chunk in enumerate(voice.synthesize(text, syn_config)):
                    if i > 0:
                        wav.writeframes(silence(vcfg["sentence_pause"]))
                    wav.writeframes(chunk.audio_int16_bytes)
                done += 1
                if done % 10 == 0 or done == len(speech_blocks):
                    print(f"    spoke {done}/{len(speech_blocks)} paragraphs", flush=True)
            previous = kind

        wav.writeframes(silence(TAIL_SECONDS))
    return len(speech_blocks)


def wav_to_mp3(wav_path: Path, mp3_path: Path, episode: Episode, config: dict, rate: int) -> None:
    podcast, audio = config["podcast"], config["audio"]
    cmd = [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(wav_path),
        # Even out the volume to a standard podcast loudness.
        "-af", f"loudnorm=I={audio['loudness']}:TP=-1.5:LRA=11",
        "-ar", str(rate),            # keep the voice's sample rate
        "-ac", "1",                  # mono
        "-c:a", "libmp3lame",        # MP3 encoder
        "-b:a", audio["bitrate"],    # e.g. 64k
        # ID3 tags, shown by players that read the file directly:
        "-id3v2_version", "3",
        "-metadata", f"title={episode.title}",
        "-metadata", f"artist={podcast['author']}",
        "-metadata", f"album={podcast['title']}",
        "-metadata", f"date={episode.published.year}",
        "-metadata", "genre=Podcast",
        str(mp3_path),
    ]
    subprocess.run(cmd, check=True)


def generate(episode: Episode, voice, config: dict) -> None:
    started = time.monotonic()
    print(f"==> {episode.slug}: {episode.title}", flush=True)
    AUDIO_DIR.mkdir(exist_ok=True)

    # Work in a temporary folder and move the MP3 into place only when it
    # is complete. A crash halfway can never leave a broken MP3 behind
    # (which would otherwise count as "already has audio").
    with tempfile.TemporaryDirectory() as tmp:
        wav_path = Path(tmp) / "speech.wav"
        mp3_path = Path(tmp) / "speech.mp3"
        synthesize_to_wav(episode, voice, config, wav_path)
        with wave.open(str(wav_path), "rb") as w:
            seconds = w.getnframes() / w.getframerate()
        wav_to_mp3(wav_path, mp3_path, episode, config, voice.config.sample_rate)
        shutil.move(mp3_path, episode.mp3_path)

    size_mb = episode.mp3_path.stat().st_size / 1_000_000
    took = time.monotonic() - started
    print(
        f"    saved {episode.mp3_path.relative_to(AUDIO_DIR.parent)}: "
        f"{int(seconds // 60)}m{int(seconds % 60):02d}s of audio, "
        f"{size_mb:.1f} MB (took {took:.0f}s)",
        flush=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check", action="store_true", help="only list episodes that need audio"
    )
    args = parser.parse_args()

    config = load_config()
    model = config["voice"]["model"]
    episodes = load_episodes()  # also validates every script's header
    missing = [e for e in episodes if not e.has_audio]

    print(f"Voice: {model}")
    print(f"Episodes: {len(episodes)} total, {len(missing)} without an MP3")
    for e in missing:
        print(f"  - {e.script_path.name}")

    if args.check:
        set_github_output(needed=str(bool(missing)).lower(), voice=model)
        return

    if not missing:
        print("Nothing to do.")
        return
    if not shutil.which("ffmpeg"):
        sys.exit("ERROR: ffmpeg is not installed (needed to make MP3s).")

    voice = load_voice(model)
    for episode in missing:
        generate(episode, voice, config)


if __name__ == "__main__":
    main()
