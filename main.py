#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence (1-220 chars) pitching a ridiculous invention
that fixes a tiny everyday annoyance, to /output/entry.txt.
"""

import os

PITCH = (
    "The Sock Court Drawer: a sock drawer that, whenever you open it wearing "
    "two different socks, slams itself shut in protest and serves you a tiny "
    "printed court summons for crimes against laundry."
)


def main() -> None:
    text = PITCH.strip()
    assert 1 <= len(text) <= 220, f"pitch is {len(text)} chars, must be 1-220"
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
