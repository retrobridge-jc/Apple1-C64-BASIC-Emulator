#!/usr/bin/env python3
"""Prepare user-supplied Apple-1 images for the C64 V0.4 loader.

This utility does NOT contain or download WozMon or Apple Integer BASIC.
It only prepends/validates the two-byte C64 PRG load-address header expected
by the emulator's KERNAL LOAD routine.
"""
from pathlib import Path
import argparse

def prepare(src: Path, raw_size: int, address: int, out: Path):
    data = src.read_bytes()
    header = bytes((address & 0xff, address >> 8))
    if len(data) == raw_size:
        payload = header + data
    elif len(data) == raw_size + 2 and data[:2] == header:
        payload = data
    else:
        raise SystemExit(
            f"{src}: expected {raw_size} raw bytes or {raw_size+2} bytes "
            f"with load header ${address:04X}"
        )
    out.write_bytes(payload)
    print(f"Wrote {out} ({len(payload)} bytes, C64 load address ${address:04X})")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--wozmon", type=Path, required=True,
                    help="user-supplied 256-byte raw WozMon, or 258-byte PRG-formatted file")
    ap.add_argument("--integer-basic", type=Path, required=True,
                    help="user-supplied 4096-byte raw Integer BASIC, or 4098-byte PRG-formatted file")
    ap.add_argument("--out-dir", type=Path, default=Path("prepared"))
    a = ap.parse_args()
    a.out_dir.mkdir(parents=True, exist_ok=True)
    prepare(a.wozmon, 256, 0xC000, a.out_dir / "WOZMON")
    prepare(a.integer_basic, 4096, 0x9000, a.out_dir / "A1BASIC")

if __name__ == "__main__":
    main()
