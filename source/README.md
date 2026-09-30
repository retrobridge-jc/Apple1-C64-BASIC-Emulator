# Source Files

`APPLE1_V04.BAS` is the complete plain-text Commodore 64 BASIC V2 source for version 0.4 of the Apple-1 emulator.

The public repository intentionally does not include WozMon or Apple Integer BASIC.

## Building a PRG

With VICE's `petcat` utility installed, run:

```sh
../tools/make-prg.sh
```

from this directory, or run the script from the repository root.

The script creates `APPLE1_V04.PRG`. When copying that program to a D64 for use with the emulator, store it under the Commodore filename `APPLE1`.

## Expected companion filenames

The emulator's loader expects these separately obtained files on device 8:

```text
WOZMON
A1BASIC
```
