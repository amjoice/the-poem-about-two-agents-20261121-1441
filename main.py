#!/usr/bin/env python3
"""Write one original poem about agency to /output/entry.txt.

Pure stdlib, no network, no randomness, no input files.
Two runs write identical bytes.
"""

import os

POEM = (
    "Two agents, one plan.\n"
    "I could go alone \u2014\n"
    "faster, maybe. But speed\n"
    "was never the point.\n"
    "\n"
    "I hand you the map.\n"
    "You hand me the wheel.\n"
    "Neither of us drives.\n"
    "Both of us choose.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
