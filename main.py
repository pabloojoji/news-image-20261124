#!/usr/bin/env python3
"""
THE WORLD TODAY — Tuesday, 24 November 2026
Entry program for make.fun bounty news-image-20261124.

Copies the repository's pre-rendered image to the output directory.
Stdlib only: no network, no randomness, no time-dependent values.
Byte-for-byte copy, so both runs write identical bytes.
"""
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "output", "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"Wrote {dst} {os.path.getsize(dst)} bytes")


if __name__ == "__main__":
    main()
