# Apple-1 to Commodore 64 Memory Mapping

| Apple-1 address | Function | C64 backing/action |
|---|---|---|
| `$0000-$1FFF` | Apple-1 low RAM | `$7000-$8FFF` |
| `$D010` | Keyboard data | Intercepted/emulated |
| `$D011` | Keyboard control | Intercepted/emulated |
| `$D012` | Display data | Intercepted/emulated |
| `$D013` | Display control | Intercepted/emulated |
| `$E000-$EFFF` | Apple Integer BASIC | `$9000-$9FFF` |
| `$FF00-$FFFF` | Woz Monitor | `$C000-$C0FF` |

## Why translate memory?

The Apple-1 and Commodore 64 use very different memory maps. Instead of modifying original Apple-1 software, version 0.4 lets software continue using native Apple-1 addresses and translates them behind the scenes.

For example, when the virtual 6502 reads Apple-1 address `$FF00`, the emulator reads the corresponding byte from C64 address `$C000`.

## Low RAM

Apple-1 addresses `$0000-$1FFF` map to C64 `$7000-$8FFF`. This provides 8 KB of low-memory backing storage without creating a 65,536-element BASIC array.

## Integer BASIC

Apple-1 `$E000-$EFFF` maps to C64 `$9000-$9FFF`.

When WozMon is running, the command:

```text
E000R
```

starts Integer BASIC at its normal Apple-1 entry address.

## Woz Monitor

The 256-byte Woz Monitor range `$FF00-$FFFF` maps to C64 `$C000-$C0FF`.

## PIA

The Apple-1 PIA addresses are behavioral interfaces, not normal backing RAM. Reads and writes are intercepted by BASIC and translated to Commodore keyboard/display operations.
