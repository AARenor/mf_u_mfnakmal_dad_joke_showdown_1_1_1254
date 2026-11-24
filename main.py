#!/usr/bin/env python3
"""Write the make.fun bounty entry text to entry.txt.

Standard library only, no network. The text is one constant; the program
creates the output folder and writes the exact bytes (no trailing newline).
"""

import os
import sys

TEXT = (
    "My dad sent his steak back twice. When it finally came he clapped for it. "
    "The waiter said, 'Sir, that's not how well done works.'"
)

ENTRY_NAME = "entry.txt"


def output_dir() -> str:
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return value
    return "/output"


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text length out of range: {len(TEXT)}"
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, ENTRY_NAME)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
