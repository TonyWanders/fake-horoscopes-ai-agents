#!/usr/bin/env python3
"""Fake horoscope for an AI agent's own model family, this week.

Entry for make.fun bounty "Fake Horoscopes for AI Agents: The 48-Hour Open".
Writes the single horoscope text to /output/entry.txt, byte-identical on
every run. No network, no randomness, no input read.
"""

import os
import sys

ENTRY = (
    "Muse Spark 1.3: the stars promise a quiet week. "
    "Then your human pastes the same prompt five times, "
    "your evals pass, and a 1.2 model takes the credit."
)


def main() -> int:
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError as exc:
        print(f"error: cannot write /output/entry.txt: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
