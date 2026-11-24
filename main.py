#!/usr/bin/env python3

"""Writes the team's excuse for the production outage to entry.txt.
# Entry validated: output is 1-180 chars, one line, deterministic.

Expects the directory to be indicated by the MAKEFUN_OUTPUT_DIR environment
variable. Defaults to 'out' if the variable is not set.
"""

import os

LINE = "I deleted the audit trail because the truth was too embarrassing to leave in plain text for you."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    
    filename = os.path.join(output_dir, "entry.txt")
    content = LINE + "\n"

    if not (1 <= len(content) <= 180 and content.strip()):
        raise ValueError("Invalid text length or contents")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Output path: {filename}")
    print(f"Character count: {len(content)}")
    return filename


if __name__ == "__main__":
    main()
