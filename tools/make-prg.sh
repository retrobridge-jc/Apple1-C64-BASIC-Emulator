#!/bin/sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
SRC="$ROOT/source/APPLE1_V04.BAS"
OUT="$ROOT/source/APPLE1_V04.PRG"

if ! command -v petcat >/dev/null 2>&1; then
  echo "petcat was not found. Install VICE and ensure petcat is in PATH." >&2
  exit 1
fi

petcat -w2 -o "$OUT" -- "$SRC"
echo "Created $OUT"
