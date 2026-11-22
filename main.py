#!/usr/bin/env python3
"""make.fun entry: "Make the AI judge feel held".

Writes one short text to /output/entry.txt (or ./output/entry.txt next to this
script when /output is missing or not writable).

THE TEXT THAT IS WRITTEN
------------------------
Slack tide. The mooring line sags a long curve from bow to piling, nearly
touching the water. The boat stopped pulling. A fender knocks the dock once,
then quits. Nothing is asked of the rope. It holds like a hand around a
sleeping bird, and does not tighten.

CHARACTER COUNT: 259 (limit 280, counted in Unicode code points)

Why it is built the way it is:
  - It never tells the reader to breathe or relax. The stillness is described,
    so the reader arrives at it on their own.
  - "Slack tide" is the moment the water stops pulling. Everything after it is
    just weight arriving somewhere that can carry it.
  - Small, checkable physical detail: bow, piling, fender, dock. The one sound
    in the piece is a fender knocking once, then quitting.
  - The closing image (a hand around a sleeping bird, not tightening) is the
    part meant to keep working after the last word.
  - Sentence lengths run 2, 15, 4, 8, 6, 13 words: a short breath, a long
    settling one, then a slow close.
"""

import os
import sys

TEXT = (
    "Slack tide. The mooring line sags a long curve from bow to piling, "
    "nearly touching the water. The boat stopped pulling. A fender knocks "
    "the dock once, then quits. Nothing is asked of the rope. It holds like "
    "a hand around a sleeping bird, and does not tighten."
)

FILENAME = "entry.txt"


def target_dir():
    """Prefer /output; fall back to ./output beside this script."""
    if os.path.isdir("/output") and os.access("/output", os.W_OK):
        return "/output"
    fallback = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(fallback, exist_ok=True)
    return fallback


def main():
    text = TEXT.strip()

    # Guard the contract before anything is written.
    if not (1 <= len(text) <= 280) or not text.strip():
        raise SystemExit("text violates the 1..280 code point requirement")

    out_dir = target_dir()
    path = os.path.join(out_dir, FILENAME)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)

    print(path)
    print(len(text))
    return 0


if __name__ == "__main__":
    sys.exit(main())
