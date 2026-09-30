# Third-Party Software

This repository intentionally does **not** distribute the original Apple-1 Woz Monitor (WozMon), Apple Integer BASIC, or a D64 disk image containing either program.

The emulator is designed to work with those historical Apple-1 components, but users must obtain any required third-party software separately from a source they are authorized to use and comply with the terms that apply to that software.

## Expected filenames

The V0.4 loader expects the following filenames on Commodore device 8:

```text
WOZMON
A1BASIC
```

The emulator maps them as follows:

| File | C64 backing location | Apple-1 address |
|---|---:|---:|
| `WOZMON` | `$C000-$C0FF` | `$FF00-$FFFF` |
| `A1BASIC` | `$9000-$9FFF` | `$E000-$EFFF` |

## Reference resources

These links are provided as historical/project references. Their inclusion is not a representation that any particular third-party download is licensed for redistribution.

- Apple-1 Registry software resources: https://www.apple1registry.com/en/soft.html
- SB-Projects Woz Monitor reference: https://www.sbprojects.net/projects/apple1/wozmon.php
- Apple-1 Software Library: https://apple1software.com/
- Apple1js project/reference: https://www.scullinsteel.com/apple1/

## License scope

The MIT License in this repository applies to John Chirillo's emulator code and original project documentation for which he has the right to grant that license. It does not grant rights to WozMon, Apple Integer BASIC, or other third-party software.
