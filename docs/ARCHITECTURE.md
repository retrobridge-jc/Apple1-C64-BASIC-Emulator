# Architecture

The project creates a virtual Apple-1 environment between original Apple-1 software and the Commodore 64.

```text
+-------------------------------+
|       Apple-1 Software        |
|   Woz Monitor / Integer BASIC |
+---------------+---------------+
                |
                v
+-------------------------------+
|        Virtual Apple-1        |
|   6502 CPU / Memory / PIA I/O |
+---------------+---------------+
                |
                v
+-------------------------------+
|      Commodore 64 BASIC       |
|         Emulator logic        |
+---------------+---------------+
                |
                v
+-------------------------------+
|       Commodore 64 / VICE     |
|         Host environment      |
+-------------------------------+
```

## CPU

The BASIC program maintains the important NMOS 6502 state as variables:

- Accumulator
- X register
- Y register
- Stack pointer
- Program counter
- Processor status flags

The main loop fetches an opcode from virtual Apple-1 memory, decodes it, executes the corresponding operation, updates registers/flags, and repeats.

## Memory

Apple-1 software continues to use the addresses it expects. The emulator translates those addresses to selected Commodore 64 backing-memory locations.

See [MEMORY_MAP.md](MEMORY_MAP.md).

## I/O

Apple-1 PIA addresses `$D010-$D013` are intercepted instead of treated as ordinary RAM.

- `$D010` - keyboard data
- `$D011` - keyboard control
- `$D012` - display data
- `$D013` - display control

The C64 keyboard is polled by BASIC, converted to Apple-1 keyboard behavior, and returned to the virtual CPU. Display writes from Apple-1 software are captured and printed on the Commodore screen.

## Loader

Version 0.4 installs a compact loader at C64 address `$6800`. It uses the KERNAL `SETNAM`, `SETLFS`, and `LOAD` entry points to load externally supplied Apple-1 software quickly.

The KERNAL loader only moves bytes into the selected backing-memory areas. The Apple-1 machine code is still interpreted instruction-by-instruction by the BASIC virtual 6502.
