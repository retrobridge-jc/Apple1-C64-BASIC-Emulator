# Apple-1 Emulator for the Commodore 64

**Version 0.4**

An Apple-1 emulator written primarily in Commodore 64 BASIC V2.

The project implements a virtual 6502 CPU, Apple-1 memory mapping, and enough Apple-1 PIA keyboard/display behavior to run the original Woz Monitor and Apple Integer BASIC on a Commodore 64 environment.

## What this project does

The emulator provides:

- A software 6502 CPU implemented in Commodore 64 BASIC
- Emulated A, X, Y, SP, PC, and processor-status state
- Opcode fetch/decode/execute logic
- Apple-1 memory translation into C64 backing memory
- Apple-1 PIA keyboard and display emulation
- C64 keyboard input translated to Apple-1 keyboard behavior
- Apple-1 display output translated to the C64 screen
- A fast C64 KERNAL loader for loading externally supplied Apple-1 software images
- Compatibility sufficient to start WozMon and enter Apple Integer BASIC with `E000R`

## Why I built it

I collect and use vintage computers, including a working Apple-1 and Commodore 64. After getting back into BASIC programming, I started with a simple question:

> Could I make a Commodore 64 emulate an Apple-1, and could I write the emulator primarily in Commodore 64 BASIC?

Version 0.4 is the result.

## Repository layout

```text
Apple1-C64-BASIC-Emulator/
├── README.md
├── LICENSE
├── THIRD_PARTY_SOFTWARE.md
├── BUILD_YOUR_OWN_D64.md
├── source/
│   ├── APPLE1_V04.BAS
│   └── APPLE1_V04.PRG
├── docs/
│   ├── architecture.png
│   └── memory-map.png
└── screenshots/
    ├── trace-debug.png
    ├── sorcery-multimanager.jpg
    └── collection.jpg
```

## Required Apple-1 software

This repository **does not distribute** the original Apple-1 Monitor (WozMon) or Apple Integer BASIC.

To run the emulator, obtain those components separately from a source you are authorized to use. Apple-1 archival resources can help you locate historical material, for example:

- Apple-1 Registry software resources: https://www.apple1registry.com/en/soft.html
- SB-Projects Woz Monitor information: https://www.sbprojects.net/projects/apple1/wozmon.php

The emulator expects the files to be named:

```text
WOZMON
A1BASIC
```

These third-party components are not covered by this repository's MIT License.

## Memory mapping

| Apple-1 address | Function | C64 backing/action |
|---|---|---|
| `$0000-$1FFF` | Low RAM | `$7000-$8FFF` |
| `$D010-$D013` | PIA I/O | Intercepted/emulated |
| `$E000-$EFFF` | Integer BASIC | `$9000-$9FFF` |
| `$FF00-$FFFF` | Woz Monitor | `$C000-$C0FF` |

## Building a runnable disk

See [BUILD_YOUR_OWN_D64.md](BUILD_YOUR_OWN_D64.md).

In short:

1. Create or attach a writable Commodore 1541 D64 image.
2. Add `APPLE1` from this repository.
3. Add your separately obtained Woz Monitor image as `WOZMON`.
4. Add your separately obtained Apple Integer BASIC image as `A1BASIC`.
5. Attach the disk to Drive 8 in VICE.

Then run:

```basic
LOAD"APPLE1",8
RUN
```

Once WozMon is running, enter:

```text
E000R
```

A simple first test in Integer BASIC is:

```text
PRINT 2+2
```

If everything is working, the result is:

```text
4
```

## Performance

The emulator is intentionally BASIC-first rather than speed-first. At normal C64 speed, execution is slow because Commodore BASIC is simulating each virtual 6502 instruction.

VICE Warp Mode is useful during development and testing. It does not bypass the virtual 6502; it simply allows the emulated Commodore 64 underneath it to run faster.

## Machine-language assistance

The virtual Apple-1 CPU is implemented in Commodore BASIC.

Version 0.4 does use a small loader installed at `$6800` that calls the C64 KERNAL `SETNAM`, `SETLFS`, and `LOAD` routines to place the external Apple-1 images into their backing-memory locations efficiently. The loader does not execute Apple-1 code; the BASIC emulator still fetches and interprets the Apple-1 instructions.

## COMPUTE!'s Gazette

This project is the subject of my article:

**“An Apple-1 Inside Your Commodore 64: Building an Apple-1 Emulator in Commodore 64 BASIC.”**

The article was prepared for *COMPUTE!'s Gazette*. Publication details will be added here when available.

## About the source

The complete V0.4 BASIC source is included so the project can be studied, modified, optimized, and extended.

Experiment with it. Add tracing. Improve an opcode. Test more Apple-1 software. Change the memory handling. Break something and figure out why.

That is a big part of the fun.

## License

The emulator source and original project documentation in this repository are released under the MIT License.

Third-party Apple-1 software is **not included** and is **not covered** by the MIT License.

Copyright © 2026 John Chirillo
