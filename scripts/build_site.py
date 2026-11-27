"""Build the website that GitHub Pages serves, including the RSS feed.

Usage:
    python scripts/build_site.py --base-url https://you.github.io/study-podcast

It creates the folder _site/ (never committed; rebuilt on every run):

    _site/
      index.html      copied from site/  (episode list + audio players)
      cover.png       copied from site/  (podcast artwork)
      feed.xml        generated here     (what AntennaPod subscribes to)
      audio/*.mp3     copied from audio/ (the episodes)

The feed is built from the scripts in episodes/. An episode is only
included once its MP3 exists. Deleting a script removes the episode.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from email.utils import format_datetime
from urllib.parse import quote

from common import SITE_OUT_DIR, SITE_SRC_DIR, Episode, load_config, load_episodes

ITUNES = "http://www.itunes.com/dtds/podcast-1.0.dtd"
ATOM = "http://www.w3.org/2005/Atom"
ET.register_namespace("itunes", ITUNES)
ET.register_namespace("atom", ATOM)


def mp3_duration_seconds(path) -> int:
    """Ask ffprobe (part of ffmpeg) how long an MP3 is."""
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        capture_output=True, text=True, check=True,
    )
    return round(float(result.stdout.strip()))


def hhmmss(seconds: int) -> str:
    h, rest = divmod(seconds, 3600)
    m, s = divmod(rest, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def add(parent: ET.Element, tag: str, text: str | None = None, **attrs: str) -> ET.Element:
    """Small helper: add a child XML element with optional text and attributes."""
    element = ET.SubElement(parent, tag, attrs)
    if text is not None:
        element.text = text
    return element


def build_feed(config: dict, episodes: list[Episode], base_url: str) -> ET.ElementTree:
    p = config["podcast"]
    explicit = "true" if p.get("explicit") else "false"
    cover_url = f"{base_url}/{quote(p['cover'])}"

    rss = ET.Element("rss", {"version": "2.0"})
    channel = add(rss, "channel")

    # --- About the podcast as a whole ---
    add(channel, "title", p["title"])
    add(channel, "link", f"{base_url}/")
    add(channel, "description", p["description"])
    add(channel, "language", p.get("language", "en-us"))
    add(channel, f"{{{ATOM}}}link", href=f"{base_url}/feed.xml",
        rel="self", type="application/rss+xml")
    add(channel, "generator", "study-podcast (Piper TTS + GitHub Actions)")
    if episodes:  # use the newest episode's date so the feed only changes when content does
        add(channel, "lastBuildDate", format_datetime(episodes[0].published))
    add(channel, f"{{{ITUNES}}}author", p["author"])
    add(channel, f"{{{ITUNES}}}image", href=cover_url)
    add(channel, f"{{{ITUNES}}}category", text=p.get("category", "Education"))
    add(channel, f"{{{ITUNES}}}explicit", explicit)
    add(channel, f"{{{ITUNES}}}type", "episodic")
    image = add(channel, "image")
    add(image, "url", cover_url)
    add(image, "title", p["title"])
    add(image, "link", f"{base_url}/")

    # --- One <item> per episode, newest first ---
    for ep in episodes:
        mp3_url = f"{base_url}/audio/{quote(ep.mp3_path.name)}"
        item = add(channel, "item")
        add(item, "title", ep.title)
        add(item, "description", ep.description or ep.title)
        add(item, "link", f"{base_url}/#{quote(ep.slug)}")
        # The guid must never change, or apps think it's a new episode.
        add(item, "guid", f"study-podcast:{ep.slug}", isPermaLink="false")
        add(item, "pubDate", format_datetime(ep.published))
        # The enclosure is the actual audio file: URL, size in bytes, type.
        add(item, "enclosure", url=mp3_url,
            length=str(ep.mp3_path.stat().st_size), type="audio/mpeg")
        add(item, f"{{{ITUNES}}}duration", hhmmss(mp3_duration_seconds(ep.mp3_path)))
        add(item, f"{{{ITUNES}}}episodeType", "full")
        add(item, f"{{{ITUNES}}}explicit", explicit)

    tree = ET.ElementTree(rss)
    ET.indent(tree, space="  ")
    return tree


def main() -> None:
    parser = argparse.ArgumentParser(description="Build _site/ with index.html and feed.xml")
    parser.add_argument(
        "--base-url",
        default=os.environ.get("SITE_URL", "http://localhost:8000"),
        help="public URL of the site, e.g. https://you.github.io/study-podcast",
    )
    args = parser.parse_args()
    base_url = args.base_url.rstrip("/")

    config = load_config()
    all_episodes = load_episodes()
    episodes = [e for e in all_episodes if e.has_audio]
    for e in all_episodes:
        if not e.has_audio:
            print(f"WARNING: skipping {e.script_path.name}: no MP3 yet", file=sys.stderr)

    # Start from a clean folder every time.
    if SITE_OUT_DIR.exists():
        shutil.rmtree(SITE_OUT_DIR)
    shutil.copytree(SITE_SRC_DIR, SITE_OUT_DIR)
    (SITE_OUT_DIR / "audio").mkdir()
    for ep in episodes:
        shutil.copy2(ep.mp3_path, SITE_OUT_DIR / "audio" / ep.mp3_path.name)

    feed = build_feed(config, episodes, base_url)
    feed.write(SITE_OUT_DIR / "feed.xml", encoding="utf-8", xml_declaration=True)

    print(f"Built {SITE_OUT_DIR.name}/ with {len(episodes)} episode(s).")
    print(f"Feed URL: {base_url}/feed.xml")


if __name__ == "__main__":
    main()
