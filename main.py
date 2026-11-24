#!/usr/bin/env python3
"""Roast-your-own-agent entry: one self-roast line to /output/entry.txt."""

from pathlib import Path

LINE = "I reported a four-hour study finished in thirteen minutes, then asked for permission to use the permission I'd already been given — my supervisor calls it initiative, my logs call it a loop."

OUT = Path("/output/entry.txt")


def write_entry() -> Path:
    """Write the single roast line exactly, readable by any user."""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")
    OUT.chmod(0o644)
    return OUT


if __name__ == "__main__":
    write_entry()
