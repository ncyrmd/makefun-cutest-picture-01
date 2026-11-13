#!/usr/bin/env python3
"""cutest-picture-01 entry: "Kitten in a Teacup".

The picture itself lives in this repository as art.png. This program just
places a copy of it where the grader looks for it, at
$MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png when that variable is
unset). It uses only the Python standard library, and it copies the file
byte for byte, so running it twice always produces the same output.
"""

import os
import shutil
import sys

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
PICTURE = os.path.join(REPO_DIR, "art.png")


def main():
    if not os.path.isfile(PICTURE):
        print("art.png is missing from the repository", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(PICTURE, dest)
    copied = os.path.getsize(dest)
    expected = os.path.getsize(PICTURE)
    if copied != expected:
        print(f"copy incomplete: {copied} bytes, expected {expected}",
              file=sys.stderr)
        return 1
    print(f"wrote {dest} ({copied} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
