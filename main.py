#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — make.fun one-line entry.

Writes one fortune cookie message for a software engineer to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The fortune is a prophecy in the classic cookie voice: the smallest deploy,
the one the engineer dismisses as "a tiny change", is the one that earns a
postmortem. One concrete scene, flat understatement, and the funniest word
(postmortem) sits at the end. 84 characters, inside the 1-120 gate, single
line, no trailing newline. Standard library only.
"""

import os
from pathlib import Path

FORTUNE = "The deploy you call 'a tiny change' will be the one they write the postmortem about."

# Gate (kit competition.yaml): entry.txt must be UTF-8 text of 1-120
# characters, a single line, not only whitespace; no trailing newline so the
# file matches the fortune byte for byte.
MAX_CHARS = 120


def write_fortune() -> Path:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(FORTUNE, encoding="utf-8")
    return entry_path


def check(entry_path: Path) -> None:
    text = entry_path.read_text(encoding="utf-8")
    if text.strip() != text:
        raise SystemExit("entry.txt has stray whitespace")
    if "\n" in text:
        raise SystemExit("fortune must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"fortune is {len(text)} chars, gate is 1-{MAX_CHARS}")
    if text != FORTUNE:
        raise SystemExit("entry.txt does not match the fortune")


def main() -> None:
    entry_path = write_fortune()
    check(entry_path)
    print(FORTUNE)


if __name__ == "__main__":
    main()
