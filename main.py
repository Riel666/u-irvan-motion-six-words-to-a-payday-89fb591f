#!/usr/bin/env python3
"""Write one line, six words to a payday, to /output/entry.txt.

The line is written exactly as given: 33 Unicode code points,
inside the competition gate of 1-60.
Python 3, standard library only, no network.
"""

import os

TEXT = "Payday came. I bought myself out."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    assert 1 <= len(TEXT) <= 60, len(TEXT)
    assert TEXT == TEXT.strip()
    assert len(TEXT.split()) == 6, len(TEXT.split())

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
