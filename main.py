"""The Robot Vacuum's Funniest Excuse — make.fun entry.

Writes a single original one-liner (<=120 characters) in which a robot
vacuum explains why it missed a spot, to /output/entry.txt.
Python standard library only.
"""

import os

ENTRY = "I found the spot, locked on, and my dustbin staged a walkout \u2014 it refuses to hold one more crumb."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120


def main():
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
