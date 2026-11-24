#!/usr/bin/env python3
"""One-line excuse a developer gives when code breaks in production.

Writes the entry text to /output/entry.txt (or $OUTPUT_DIR/entry.txt
when testing locally). Standard library only; no network, no input.

The line: the developer blames the users — and the twist is that the
users broke it by doing exactly what the docs told them to do, i.e.
the code only survives while nobody uses it as documented.
"""

import os

LINE = "I didn't break production \u2014 the users did, by using it exactly as documented."


def main() -> None:
    # Gate guard: the entry must be 1-200 UTF-8 characters, not only
    # whitespace, or the sealed scorer rejects it before judging.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit("entry line fails the 1-200 character gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
