#!/usr/bin/env python3
"""Angry rant generator — entry for make.fun Angry Judge: The Short Rant Contest.

Writes one short, funny rant about the office printer to /output/entry.txt.
The rant is 4 sentences, 300-380 characters, plain UTF-8 text with no
trailing newline, as required by the bounty gate (1-400 characters).
"""

import os

RANT = (
    "The office printer has never once simply printed. "
    "It jams, runs out of toner, or demands a firmware update "
    "five minutes before a deadline, like a tiny "
    "gatekeeper guarding paper. "
    "It has exactly one job, and it treats that job as a personal insult. "
    "I have emailed files to myself and taken the stairs, "
    "and both were faster than this beige monument to procrastination."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = RANT.strip()
    if not 1 <= len(text) <= 400:
        raise ValueError(f"rant must be 1-400 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("rant must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
