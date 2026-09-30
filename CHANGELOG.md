# Changelog

## 0.4

- Complete BASIC-first Apple-1 emulator architecture
- Virtual NMOS 6502 execution core
- Apple-1 low-memory translation
- Woz Monitor mapping at `$FF00-$FFFF`
- Apple Integer BASIC mapping at `$E000-$EFFF`
- Apple-1 PIA keyboard/display interception
- Fast C64 KERNAL loader installed at `$6800`
- Verified transition from WozMon to Integer BASIC with `E000R`
- Verified Integer BASIC execution with `PRINT 2+2` returning `4`
- Public distribution changed to exclude third-party WozMon and Apple Integer BASIC images

## 0.3.1

- Replaced slow BASIC byte-by-byte image loading with C64 KERNAL-assisted loading

## Earlier development

Earlier builds were used to bring up the CPU core, memory translation, I/O emulation, and trace/debugging support.
