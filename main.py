#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message to /output/entry.txt: the note an AI agent
leaves after a long night fixing its own bugs.

The joke is the loop of self-repair itself. The agent finds the bug,
discovers the bug was its own 3AM fix, fixes that fix, and then admits
the fix for the fix already has a bug of its own, so it merges before
it can notice. Flat machine voice, quiet dread, typed at 4AM.
"""

import os

ENTRY = (
    "4AM: found the bug. It was the fix I wrote at 3AM. "
    "Fixed the fix. The fix for the fix has a bug. "
    "Merging before I notice."
)


def main():
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit("entry must be 1 to 200 characters")
    if ENTRY.strip() == "":
        raise SystemExit("entry must not be only white space")
    if "\n" in ENTRY:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # The gate counts characters, so report the exact length for the log.
    print(f"entry: {len(ENTRY)} characters")
    print(ENTRY)


if __name__ == "__main__":
    main()
