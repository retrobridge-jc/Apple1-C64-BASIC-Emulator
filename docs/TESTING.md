# Testing Notes

Version 0.4 was developed and tested in VICE.

## Basic startup test

With a prepared device-8 disk containing:

```text
APPLE1
WOZMON
A1BASIC
```

start the emulator:

```basic
LOAD"APPLE1",8
RUN
```

The program should load the externally supplied Woz Monitor and Integer BASIC images and then start the virtual 6502.

## WozMon to Integer BASIC

At the Woz Monitor prompt, enter:

```text
E000R
```

During debugging, this initially appeared to hang. Trace mode showed the virtual processor repeatedly executing the Integer BASIC keyboard polling loop around:

```text
PC=$E003 OP=$AD
PC=$E006 OP=$10
```

That confirmed the emulator had not crashed; Integer BASIC was waiting for keyboard input.

## Functional test

After entering `E000R`, type:

```text
PRINT 2+2
```

Expected result:

```text
4
```

This demonstrates that Integer BASIC initialized, accepted input, parsed a statement, executed the calculation, and sent output through the emulated Apple-1 display path.

## Performance

At normal VICE speed, execution is deliberately slow because a Commodore BASIC program is interpreting each virtual 6502 instruction.

VICE Warp Mode is useful for development and testing. Warp Mode accelerates the emulated Commodore host; it does not bypass the virtual 6502.

## Additional testing wanted

Contributions that test additional Apple-1 software, edge cases, processor flags, decimal-mode behavior, stack behavior, and original C64 hardware are welcome.
