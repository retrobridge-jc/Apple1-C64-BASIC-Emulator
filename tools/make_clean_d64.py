#!/usr/bin/env python3
"""Create a clean 35-track D64 containing only APPLE1_V04.PRG as APPLE1."""
from pathlib import Path
import argparse

SECTORS = {}
for t in range(1, 36):
    if t <= 17:
        SECTORS[t] = 21
    elif t <= 24:
        SECTORS[t] = 19
    elif t <= 30:
        SECTORS[t] = 18
    else:
        SECTORS[t] = 17

def offset(track, sector):
    return (sum(SECTORS[t] for t in range(1, track)) + sector) * 256

def build(prg: bytes, out: Path):
    img = bytearray(sum(SECTORS.values()) * 256)
    free = {(t, s): True for t in range(1, 36) for s in range(SECTORS[t])}
    free[(18, 0)] = False
    free[(18, 1)] = False

    need = (len(prg) + 253) // 254
    alloc = []
    for t in list(range(1, 18)) + list(range(19, 36)):
        for s in range(SECTORS[t]):
            if free[(t, s)]:
                alloc.append((t, s))
                free[(t, s)] = False
                if len(alloc) == need:
                    break
        if len(alloc) == need:
            break
    if len(alloc) != need:
        raise SystemExit("Not enough free sectors")

    for i, (t, s) in enumerate(alloc):
        chunk = prg[i * 254:(i + 1) * 254]
        off = offset(t, s)
        if i < len(alloc) - 1:
            nt, ns = alloc[i + 1]
            img[off] = nt
            img[off + 1] = ns
        else:
            img[off] = 0
            img[off + 1] = len(chunk) + 1
        img[off + 2:off + 2 + len(chunk)] = chunk

    bam = offset(18, 0)
    img[bam] = 18
    img[bam + 1] = 1
    img[bam + 2] = 0x41
    for t in range(1, 36):
        base = bam + 4 + (t - 1) * 4
        avail = [s for s in range(SECTORS[t]) if free[(t, s)]]
        img[base] = len(avail)
        bits = [0, 0, 0]
        for s in avail:
            bits[s // 8] |= 1 << (s % 8)
        img[base + 1:base + 4] = bytes(bits)

    img[bam + 0x90:bam + 0xA0] = b"APPLE1 V04 CLEAN".ljust(16, b"\xA0")
    img[bam + 0xA0:bam + 0xA2] = b"\xA0\xA0"
    img[bam + 0xA2:bam + 0xA4] = b"JC"
    img[bam + 0xA4] = 0xA0
    img[bam + 0xA5:bam + 0xA7] = b"2A"
    img[bam + 0xA7:bam + 0xAB] = b"\xA0" * 4

    directory = offset(18, 1)
    img[directory] = 0
    img[directory + 1] = 0xFF
    e = directory + 2
    img[e] = 0x82
    img[e + 1], img[e + 2] = alloc[0]
    img[e + 3:e + 19] = b"APPLE1".ljust(16, b"\xA0")
    img[e + 30] = need & 0xFF
    img[e + 31] = need >> 8

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(img)
    print(f"Wrote {out} ({len(img)} bytes, {need} blocks)")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prg", type=Path, default=Path("source/APPLE1_V04.PRG"))
    ap.add_argument("--out", type=Path, default=Path("disk/APPLE1V04_CLEAN.D64"))
    a = ap.parse_args()
    build(a.prg.read_bytes(), a.out)

if __name__ == "__main__":
    main()
