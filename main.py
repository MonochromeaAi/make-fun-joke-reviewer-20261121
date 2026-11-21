#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

Deterministic: the same single line on every run, no randomness, no I/O
beyond writing /output/entry.txt.
"""

import os

JOKE = (
    "I asked for a one-line fix; the agent rewrote the module, "
    "added three dependencies, and committed it as 'minor cleanup'."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
