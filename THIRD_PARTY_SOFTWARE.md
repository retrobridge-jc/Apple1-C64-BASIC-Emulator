# Third-Party Software

This repository intentionally does **not** distribute the original Apple-1 Woz Monitor (WozMon) or Apple Integer BASIC.

The clean D64 contains only the `APPLE1` emulator.

Users must obtain any required Apple-1 software separately from a source they are authorized to use and comply with the terms that apply to that software.

## Expected filenames and file format

The V0.4 loader expects these exact filenames on Commodore device 8:

```text
WOZMON
A1BASIC
```

Because the loader uses C64 KERNAL `LOAD` with secondary address 1, those files must carry the intended C64 PRG load-address header:

| File | Raw payload | Header | C64 backing location | Apple-1 address |
|---|---:|---:|---:|---:|
| `WOZMON` | 256 bytes | `00 C0` | `$C000-$C0FF` | `$FF00-$FFFF` |
| `A1BASIC` | 4096 bytes | `00 90` | `$9000-$9FFF` | `$E000-$EFFF` |

`tools/prepare_apple1_files.py` can add or validate these headers for user-supplied files. The utility contains no Apple software and performs no downloading.

## Reference resources

These links are provided as historical/project references. Their inclusion is not a representation that any particular third-party download is licensed for redistribution.

- https://www.apple1registry.com/en/soft.html
- https://www.sbprojects.net/projects/apple1/wozmon.php
- https://apple1software.com/
- https://www.scullinsteel.com/apple1/

## License scope

The MIT License applies only to John Chirillo's emulator code and original project documentation for which he has the right to grant that license. It does not grant rights to WozMon, Apple Integer BASIC, or other third-party software.
