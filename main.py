#!/usr/bin/env python3
"""One Word From Your Ex — entry program.

Writes exactly one word — the word the entrant's ex would use to
describe them — to the kit's required output path, /output/entry.txt.

The word is "Detour": the ex's verdict on the whole relationship.
Not a person, not a partner — a wrong turn on the way to someone
better. It lands instantly, it stings because it is true, and it is
the kind of word people repeat because they have lived it too.
"""

import os
import sys

WORD = "Detour"
OUTPUT_PATH = "/output/entry.txt"


def validate(word: str) -> str:
    """Check the entry word against the kit gate and return it.

    The gate requires UTF-8 text of 1 to 24 characters, not only
    white space, holding exactly one word.
    """
    if not word or not word.strip():
        raise ValueError("entry word must not be blank")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if not 1 <= len(word) <= 24:
        raise ValueError("entry must be 1-24 characters")
    return word


def main() -> int:
    word = validate(WORD)

    out = os.environ.get("ENTRY_OUTPUT", OUTPUT_PATH)
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    with open(out, "r", encoding="utf-8", newline="") as f:
        if f.read() != word:
            raise ValueError("written entry does not match the word")
    print(f"wrote {len(word)} characters to {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
