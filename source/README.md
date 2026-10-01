# Source Files

`APPLE1_V04.BAS` is the complete plain-text Commodore 64 BASIC V2 source for version 0.4.

`APPLE1_V04.PRG` is the regenerated tokenized/loadable form of that source.

The public repository intentionally does not include WozMon or Apple Integer BASIC.

## Rebuilding the PRG

With VICE's `petcat` utility installed, from the repository root run:

```sh
sh tools/make-prg.sh
```

The resulting `APPLE1_V04.PRG` can be placed on a D64 under the Commodore filename `APPLE1`.

## Preparing the required third-party files

The emulator expects separately obtained files named:

```text
WOZMON
A1BASIC
```

Use `tools/prepare_apple1_files.py` to validate or add the C64 PRG load-address headers required by V0.4.
