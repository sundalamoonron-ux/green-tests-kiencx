"""Green Tests, Nothing Works: The Excuse Contest.

Writes the winning one-line excuse to /output/entry.txt.
"""

import os

LINE = "Tests: 47 passed, 0 failed. Users: 0 served. I consider this a rounding issue."


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
