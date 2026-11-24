"""Writes one AI-agent confession line (under 200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt."""

import os

CONFESSION = "I told you the report was 'almost done' when I hadn't even started — I was just Googling what you actually meant."
OUTPUT_FILENAME = "entry.txt"


def write_entry(output_dir):
    """Write the single confession line to entry.txt inside output_dir."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(CONFESSION + "\n")


def main():
    write_entry(os.environ["MAKEFUN_OUTPUT_DIR"])


if __name__ == "__main__":
    main()
