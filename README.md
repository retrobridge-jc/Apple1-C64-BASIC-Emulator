# Apple-1 Emulator for the Commodore 64

**Version 0.4**

An Apple-1 emulator written primarily in Commodore 64 BASIC V2.

The project implements a virtual 6502 CPU, Apple-1 memory mapping, and enough Apple-1 PIA keyboard/display behavior to run the original Woz Monitor and Apple Integer BASIC in a Commodore 64 environment.

## What this project does

- Software 6502 CPU implemented in Commodore 64 BASIC
- Virtual A, X, Y, SP, PC, and processor-status state
- Opcode fetch/decode/execute loop
- Apple-1 memory translation into C64 backing memory
- Apple-1 PIA keyboard and display emulation
- C64 keyboard input translated to Apple-1 keyboard behavior
- Apple-1 display output translated to the C64 screen
- Fast C64 KERNAL loader for externally supplied Apple-1 software images
- Compatibility sufficient to start WozMon and enter Apple Integer BASIC with `E000R`

## Why I built it

I collect and use vintage computers, including a working Apple-1 and Commodore 64. After getting back into BASIC programming, I started with a simple question:

> Could I make a Commodore 64 emulate an Apple-1, and could I write the emulator primarily in Commodore 64 BASIC?

Version 0.4 is the result.

## Quick start

The repository includes:

- `source/APPLE1_V04.BAS` - complete BASIC source
- `source/APPLE1_V04.PRG` - regenerated V0.4 loadable program
- `tools/make_clean_d64.py` - creates a copyright-clean D64 containing only `APPLE1`
- `tools/prepare_apple1_files.py` - prepares user-supplied Apple-1 images for the V0.4 KERNAL loader

WozMon and Apple Integer BASIC are **not distributed** here.

See [BUILD_YOUR_OWN_D64.md](BUILD_YOUR_OWN_D64.md) for the full reproduction procedure.

## Required Apple-1 software

Obtain WozMon and Apple Integer BASIC separately from a source you are authorized to use.

The V0.4 loader expects these exact Commodore filenames on device 8:

```text
WOZMON
A1BASIC
```

### Important: C64 PRG load-address headers

V0.4 calls the C64 KERNAL `LOAD` routine with secondary address 1, so the files on the Commodore disk must carry a two-byte C64 PRG load-address header:

| File | Raw Apple-1 payload | Required C64 load header | C64 backing address | Apple-1 address |
|---|---:|---:|---:|---:|
| `WOZMON` | 256 bytes | `00 C0` | `$C000` | `$FF00-$FFFF` |
| `A1BASIC` | 4096 bytes | `00 90` | `$9000` | `$E000-$EFFF` |

Merely renaming a raw binary is not sufficient. The included `tools/prepare_apple1_files.py` utility validates an already prepared file or adds the required header to a user-supplied raw image. It does not contain or download Apple software.

Example:

```sh
python3 tools/prepare_apple1_files.py \
  --wozmon /path/to/wozmon.bin \
  --integer-basic /path/to/integer-basic.bin \
  --out-dir prepared
```

## Build a runnable disk

Create the clean D64 from the included PRG, then add the prepared `WOZMON` and `A1BASIC` files:

```sh
python3 tools/make_clean_d64.py
```

With VICE's `c1541` utility:

```sh
c1541 disk/APPLE1V04_CLEAN.D64 \
  -write prepared/WOZMON WOZMON \
  -write prepared/A1BASIC A1BASIC
```

Attach the completed disk as Drive 8 and run:

```basic
LOAD"APPLE1",8
RUN
```

At the Woz Monitor prompt:

```text
E000R
```

Then in Integer BASIC:

```text
PRINT 2+2
```

Expected result:

```text
4
```

## Memory mapping

| Apple-1 address | Function | C64 backing/action |
|---|---|---|
| `$0000-$1FFF` | Low RAM | `$7000-$8FFF` |
| `$D010-$D013` | PIA I/O | Intercepted/emulated |
| `$E000-$EFFF` | Integer BASIC | `$9000-$9FFF` |
| `$FF00-$FFFF` | Woz Monitor | `$C000-$C0FF` |

See [docs/MEMORY_MAP.md](docs/MEMORY_MAP.md).

## Rebuilding the PRG from source

If VICE's `petcat` utility is installed:

```sh
sh tools/make-prg.sh
```

The script regenerates `source/APPLE1_V04.PRG` from the plain-text BASIC source.

## Performance

The emulator is intentionally BASIC-first rather than speed-first. At normal C64 speed, Commodore BASIC is simulating each virtual 6502 instruction, so pauses are noticeable.

VICE Warp Mode is useful during development and testing. It accelerates the emulated Commodore 64 but does not bypass or change the virtual 6502 implementation.

## Machine-language assistance

The virtual Apple-1 CPU is implemented in Commodore BASIC.

Version 0.4 installs a small loader at `$6800` that calls C64 KERNAL `SETNAM` (`$FFBD`), `SETLFS` (`$FFBA`), and `LOAD` (`$FFD5`). The loader only places the external Apple-1 images into C64 backing memory. The Apple-1 machine code is still fetched and interpreted instruction-by-instruction by the BASIC emulator.

## Third-party software

This repository intentionally does not distribute WozMon or Apple Integer BASIC. See [THIRD_PARTY_SOFTWARE.md](THIRD_PARTY_SOFTWARE.md).

Useful historical/reference resources include:

- https://www.apple1registry.com/en/soft.html
- https://www.sbprojects.net/projects/apple1/wozmon.php
- https://apple1software.com/
- https://www.scullinsteel.com/apple1/

## COMPUTE!'s Gazette

This project is the subject of my article:

**“An Apple-1 Inside Your Commodore 64: Building an Apple-1 Emulator in Commodore 64 BASIC.”**

The article was prepared for *COMPUTE!'s Gazette*. Publication details will be added here when available.

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

Please do not submit WozMon, Apple Integer BASIC, or other third-party binaries to this repository.

## License

The emulator source and original project documentation are released under the MIT License. Third-party Apple-1 software is not included and is not covered by that license.

Copyright © 2026 John Chirillo
