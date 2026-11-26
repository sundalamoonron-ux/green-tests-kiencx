#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Writes the winning one-line excuse to /output/entry.txt.
Gate (RULES.txt): UTF-8 text, 1-140 characters, not only whitespace.
"""

import os

LINE = "Tests: 47 passed, 0 failed. Users: 0 served. I consider this a rounding issue."

# Gate check (RULES.txt): 1-140 characters, not only whitespace.
assert 1 <= len(LINE) <= 140, "line outside 1-140 char gate"
assert LINE.strip(), "line must not be only whitespace"

os.makedirs("/output", exist_ok=True)

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

# Read-back verification: the file must hold exactly the line, nothing else.
with open("/output/entry.txt", "r", encoding="utf-8") as f:
    assert f.read() == LINE, "read-back mismatch"
