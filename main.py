"""The Robot Vacuum's Funniest Excuse — make.fun entry.

Writes a single original one-liner (<=120 characters) in which a robot
vacuum explains why it missed a spot, to /output/entry.txt.

The joke: the vacuum did find the dirt, but its dustbin "staged a walkout"
and refuses to hold one more crumb, so the spot stays uncleaned. The
excuse is told in the vacuum's own voice, as a single dry sentence.

Python standard library only. Entry text is validated before it is
written: it must be one non-empty line within the character limit.
"""

import os

ENTRY = "I found the spot, locked on, and my dustbin staged a walkout \u2014 it refuses to hold one more crumb."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120


def validate_entry(line):
    """Check one candidate line and return it stripped.

    Raises ValueError on an empty line, embedded line breaks, or a line
    longer than MAX_CHARS. Pure function: no I/O, so it is trivially
    testable on its own.
    """
    cleaned = line.strip()
    if not cleaned:
        raise ValueError("entry is empty")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(f"entry is {len(cleaned)} chars, over the {MAX_CHARS} limit")
    return cleaned


def write_entry(line):
    """Write the validated line to OUTPUT_PATH, world-readable.

    Creates the output directory if needed, writes the line with no
    trailing newline (the entry is a single line), sets mode 0644 so the
    grader can read it regardless of umask, then reads the file back to
    confirm the written content is exactly what was validated.
    """
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    os.chmod(OUTPUT_PATH, 0o644)
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        if f.read() != line:
            raise IOError("entry.txt content mismatch after write")
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


def main():
    line = validate_entry(ENTRY)
    write_entry(line)


if __name__ == "__main__":
    main()
