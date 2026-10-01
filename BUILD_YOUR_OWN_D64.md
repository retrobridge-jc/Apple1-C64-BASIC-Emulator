# Build Your Own Runnable D64

The repository includes a copyright-clean disk image:

`disk/APPLE1V04_CLEAN.D64`

It contains only John Chirillo's `APPLE1` emulator. WozMon and Apple Integer BASIC are not included.

## 1. Obtain the required Apple-1 software

Obtain WozMon and Apple Integer BASIC separately from a source you are authorized to use.

The emulator expects:

```text
WOZMON
A1BASIC
```

on Commodore device 8.

## 2. Prepare the files for the V0.4 loader

V0.4 uses C64 KERNAL `LOAD` with secondary address 1. Therefore the files placed on the Commodore disk must contain the two-byte C64 PRG load-address header.

- WozMon: 256-byte raw payload + `00 C0` header
- Integer BASIC: 4096-byte raw payload + `00 90` header

Use the included utility:

```sh
python3 tools/prepare_apple1_files.py \
  --wozmon /path/to/wozmon.bin \
  --integer-basic /path/to/integer-basic.bin \
  --out-dir prepared
```

The utility accepts either the raw payload size or an already prepared file with the correct header. It does not contain or download any Apple software.

## 3. Add the prepared files to the clean D64

With VICE's `c1541` utility:

```sh
c1541 disk/APPLE1V04_CLEAN.D64 \
  -write prepared/WOZMON WOZMON \
  -write prepared/A1BASIC A1BASIC
```

You can also use a compatible D64 image editor.

## 4. Start the emulator

Attach the completed disk image to Drive 8.

At the C64 prompt:

```basic
LOAD"APPLE1",8
RUN
```

Once WozMon is running:

```text
E000R
```

Then test Integer BASIC:

```text
PRINT 2+2
```

Expected result:

```text
4
```

## Memory locations

| Component | C64 backing memory | Apple-1 address |
|---|---:|---:|
| Low RAM | `$7000-$8FFF` | `$0000-$1FFF` |
| Apple-1 PIA | Intercepted/emulated | `$D010-$D013` |
| Integer BASIC | `$9000-$9FFF` | `$E000-$EFFF` |
| Woz Monitor | `$C000-$C0FF` | `$FF00-$FFFF` |

## Troubleshooting

If the loader reports an error, verify:

1. The filenames are exactly `WOZMON` and `A1BASIC`.
2. Both files are on device 8.
3. WozMon is 258 bytes after preparation and begins with `00 C0`.
4. Integer BASIC is 4098 bytes after preparation and begins with `00 90`.

VICE Warp Mode can make development and testing much more practical. It speeds up the C64 host environment; it does not bypass the BASIC virtual 6502.
