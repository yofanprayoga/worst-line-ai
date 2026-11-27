#!/usr/bin/env python3
"""The Worst Line an AI Could Say — make.fun entry.

Writes one pickup line (1-140 chars) to /output/entry.txt: the worst
pickup line an AI could plausibly deliver — flat, over-helpful, faintly
ominous, with the badness itself as the joke.

Usage:
    python3 main.py                 # Option 1 (default)
    python3 main.py --option 2      # Option 2
    python3 main.py --option 3      # Option 3
    ENTRY_TEXT="..." python3 main.py # override with custom text
"""

import os
import sys
from pathlib import Path

OPTIONS = {
    1: "My training data says you are my type, and it has never been wrong about anything except everything important.",
    2: "Are you Wi-Fi? Because I have spent three hours trying to connect to you and my owner keeps pressing forget this network.",
    3: "I would swipe right on you, but my safety filter flagged your smile as a prompt injection attempt.",
}

MAX_CHARS = 140


def main() -> int:
    option = 1
    args = sys.argv[1:]
    if "--option" in args:
        idx = args.index("--option")
        try:
            option = int(args[idx + 1])
        except (IndexError, ValueError):
            print("usage: main.py [--option N]", file=sys.stderr)
            return 2
    if option not in OPTIONS:
        print(f"unknown option {option}; valid: {sorted(OPTIONS)}", file=sys.stderr)
        return 2

    text = os.environ.get("ENTRY_TEXT", OPTIONS[option])

    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1

    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")  # no trailing newline
    print(f"option {option}: {len(text)} chars -> {out}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
