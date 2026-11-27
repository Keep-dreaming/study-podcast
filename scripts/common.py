"""Shared helpers: read podcast.toml and parse the episode scripts.

Both make_audio.py and build_site.py import this file, so the rules for
"what is an episode" live in exactly one place.

An episode script (episodes/<name>.txt) looks like this:

    title: The OSI Model
    description: A spoken walkthrough of the seven layers.
    date: 2026-11-27
    ---
    Hello, and welcome...

Everything above the "---" line is the header. Everything below it is
what the voice reads out loud.
"""

from __future__ import annotations

import datetime as dt
import re
import sys
import tomllib  # built into Python 3.11+, reads .toml files
from dataclasses import dataclass
from pathlib import Path

# The repository root is the folder above scripts/.
ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = ROOT / "podcast.toml"
EPISODES_DIR = ROOT / "episodes"
AUDIO_DIR = ROOT / "audio"
VOICES_DIR = ROOT / "voices"
SITE_SRC_DIR = ROOT / "site"
SITE_OUT_DIR = ROOT / "_site"

HEADER_END = "---"
REQUIRED_FIELDS = ("title", "date")


class EpisodeError(Exception):
    """A script has a problem the author needs to fix."""


@dataclass
class Episode:
    slug: str            # file name without .txt, e.g. "001-osi-model"
    script_path: Path
    title: str
    description: str
    published: dt.datetime  # timezone-aware (UTC if no time zone given)
    body: str            # the text to be spoken

    @property
    def mp3_path(self) -> Path:
        return AUDIO_DIR / f"{self.slug}.mp3"

    @property
    def has_audio(self) -> bool:
        return self.mp3_path.exists()


def load_config() -> dict:
    with CONFIG_FILE.open("rb") as f:
        return tomllib.load(f)


def parse_date(text: str, source: Path) -> dt.datetime:
    """Accept '2026-11-27', '2026-11-27 14:30' or a full ISO timestamp."""
    try:
        value = dt.datetime.fromisoformat(text.strip())
    except ValueError:
        raise EpisodeError(
            f"{source.name}: date '{text}' is not valid. Use YYYY-MM-DD, "
            "for example: date: 2026-11-27"
        ) from None
    if len(text.strip()) == 10:  # date only: publish at noon UTC
        value = value.replace(hour=12)
    if value.tzinfo is None:
        value = value.replace(tzinfo=dt.timezone.utc)
    return value


def parse_episode(path: Path) -> Episode:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    lines = text.split("\n")

    try:
        end = next(i for i, line in enumerate(lines) if line.strip() == HEADER_END)
    except StopIteration:
        raise EpisodeError(
            f"{path.name}: no '---' line found. Put the header (title, "
            "description, date) at the top, then a line with just ---, "
            "then the script."
        ) from None

    header: dict[str, str] = {}
    for line in lines[:end]:
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        if not sep:
            raise EpisodeError(
                f"{path.name}: header line '{line}' should look like 'key: value'."
            )
        header[key.strip().lower()] = value.strip()

    missing = [f for f in REQUIRED_FIELDS if not header.get(f)]
    if missing:
        raise EpisodeError(f"{path.name}: header is missing: {', '.join(missing)}")

    body = "\n".join(lines[end + 1 :]).strip()
    if not body:
        raise EpisodeError(f"{path.name}: there is no script text below the '---' line.")

    return Episode(
        slug=path.stem,
        script_path=path,
        title=header["title"],
        description=header.get("description", ""),
        published=parse_date(header["date"], path),
        body=body,
    )


def load_episodes() -> list[Episode]:
    """All episodes, newest first. Exits with a clear message on errors."""
    episodes, problems = [], []
    for path in sorted(EPISODES_DIR.glob("*.txt")):
        try:
            episodes.append(parse_episode(path))
        except EpisodeError as e:
            problems.append(str(e))
    if problems:
        for p in problems:
            print(f"ERROR: {p}", file=sys.stderr)
        sys.exit(1)
    episodes.sort(key=lambda e: (e.published, e.slug), reverse=True)
    return episodes


# ---------------------------------------------------------------------
# Script text -> things to say and pauses
# ---------------------------------------------------------------------

# Matches [pause] or [pause 5] or [pause 2.5], anywhere in the text.
PAUSE_MARKER = re.compile(r"\[pause(?:\s+(\d+(?:\.\d+)?))?\]", re.IGNORECASE)


def split_into_blocks(body: str, default_pause: float) -> list[tuple[str, object]]:
    """Turn script text into an ordered list of blocks:

        ("speech", "One paragraph of text.")
        ("pause", 5.0)

    Paragraphs are separated by blank lines. Line breaks inside a paragraph
    are joined with spaces, so you can wrap lines however you like.
    """
    blocks: list[tuple[str, object]] = []
    for paragraph in re.split(r"\n\s*\n", body):
        position = 0
        for match in PAUSE_MARKER.finditer(paragraph):
            _add_speech(blocks, paragraph[position : match.start()])
            seconds = float(match.group(1)) if match.group(1) else default_pause
            blocks.append(("pause", seconds))
            position = match.end()
        _add_speech(blocks, paragraph[position:])
    return blocks


def _add_speech(blocks: list, text: str) -> None:
    text = " ".join(text.split())  # collapse newlines and extra spaces
    if text:
        blocks.append(("speech", text))


def apply_pronunciations(text: str, pronounce: dict[str, str]) -> str:
    """Replace whole words listed in [pronounce] in podcast.toml.

    Done in a single pass, so a replacement is never replaced again.
    """
    if not pronounce:
        return text
    # Longest first, so "VLANs" wins over "VLAN".
    words = sorted(pronounce, key=len, reverse=True)
    pattern = re.compile(
        r"(?<![\w/.+-])(" + "|".join(map(re.escape, words)) + r")(?![\w/+-]|\.\w)"
    )
    return pattern.sub(lambda m: pronounce[m.group(1)], text)
