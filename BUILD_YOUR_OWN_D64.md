# Build Your Own D64

The public distribution does not include WozMon, Apple Integer BASIC, or a ready-to-run D64 containing them.

## What you need

- VICE or another Commodore 64 environment capable of creating/writing D64 disk images
- `source/APPLE1_V04.PRG` from this repository
- A separately obtained Apple-1 Woz Monitor image
- A separately obtained Apple Integer BASIC image

## Prepare the disk

1. Create a new writable Commodore 1541 D64 image.
2. Add `source/APPLE1_V04.PRG` to the disk and store it under the Commodore filename `APPLE1`.
3. Add your separately obtained Woz Monitor file and name it `WOZMON`.
4. Add your separately obtained Apple Integer BASIC file and name it `A1BASIC`.
5. Attach the completed disk image to Drive 8.

The emulator expects `WOZMON` and `A1BASIC` on device 8.

## Start the emulator

From the Commodore 64 prompt:

```basic
LOAD"APPLE1",8
RUN
```

The emulator uses C64 KERNAL loading routines to place the external images in their C64 backing-memory locations. The Apple-1 machine code itself is then interpreted by the virtual 6502 implemented in Commodore BASIC.

Once WozMon is running, enter:

```text
E000R
```

That jumps to Apple Integer BASIC at Apple-1 address `$E000`.

A simple first test is:

```text
PRINT 2+2
```

Expected result:

```text
4
```

## Expected memory locations

| Component | C64 backing memory | Apple-1 address |
|---|---:|---:|
| Low RAM | `$7000-$8FFF` | `$0000-$1FFF` |
| Apple-1 PIA | Intercepted/emulated | `$D010-$D013` |
| Integer BASIC | `$9000-$9FFF` | `$E000-$EFFF` |
| Woz Monitor | `$C000-$C0FF` | `$FF00-$FFFF` |

## Troubleshooting

If the loader cannot find `WOZMON` or `A1BASIC`, verify that the filenames are exact and that the files are on device 8.

During development, VICE Warp Mode can make testing much more practical. Warp Mode speeds up the C64 host environment; it does not bypass the BASIC virtual 6502.
