#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python3 "$SCRIPT_DIR/validate_mvp_ttl.py"

SHAPES_FILE="$SCRIPT_DIR/mvp.shapes.ttl"
if [[ -f "$SHAPES_FILE" ]]; then
  python3 -m pyshacl -s "$SHAPES_FILE" -m -f human "$SCRIPT_DIR/scout_beachhandball_mvp.ttl"
else
  echo "INFO: SHACL skipped; no shapes file at $SHAPES_FILE"
fi
