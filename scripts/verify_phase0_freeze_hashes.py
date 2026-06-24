#!/usr/bin/env python3
"""Verify the sha256 freeze table declared by the Phase 0 master contract."""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "docs/05_fases/fase_0/CONTRATO_UNICO_FASE_0.md"
SECTION_HEADER = "## 11. Anexos obrigatorios e hashes congelados"
TABLE_REQUIRED_COLUMNS = {"arquivo", "papel_no_gate", "sha256"}


class FreezeValidationError(RuntimeError):
    pass


def compute_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_freeze_rows() -> list[dict[str, str]]:
    text = CONTRACT_PATH.read_text(encoding="utf-8")
    marker = text.find(SECTION_HEADER)
    if marker == -1:
        raise FreezeValidationError(f"{CONTRACT_PATH.relative_to(ROOT)}: missing section {SECTION_HEADER!r}")

    lines = text[marker:].splitlines()
    headers: list[str] | None = None
    rows: list[dict[str, str]] = []

    for index, line in enumerate(lines):
        if not line.startswith("|"):
            if headers is not None and rows:
                break
            continue

        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        is_separator = all(cell.replace("-", "").replace(":", "") == "" for cell in cells)
        if is_separator:
            continue

        if index + 1 < len(lines):
            next_line = lines[index + 1]
            if next_line.startswith("|"):
                next_cells = [cell.strip() for cell in next_line.strip().strip("|").split("|")]
                if next_cells and all(cell.replace("-", "").replace(":", "") == "" for cell in next_cells):
                    headers = cells
                    missing = sorted(TABLE_REQUIRED_COLUMNS - set(headers))
                    if missing:
                        raise FreezeValidationError(
                            f"{CONTRACT_PATH.relative_to(ROOT)}: freeze table missing required columns: "
                            + ", ".join(missing)
                        )
                    continue

        if headers is None:
            continue
        if len(cells) != len(headers):
            raise FreezeValidationError(
                f"{CONTRACT_PATH.relative_to(ROOT)}: freeze row has {len(cells)} cells but header has {len(headers)}"
            )

        row = dict(zip(headers, cells))
        path_cell = row.get("arquivo", "")
        if not (path_cell.startswith("`") and path_cell.endswith("`")):
            continue
        rows.append(
            {
                "arquivo": path_cell.strip("`"),
                "sha256": row["sha256"].strip("`"),
            }
        )

    if not rows:
        raise FreezeValidationError(f"{CONTRACT_PATH.relative_to(ROOT)}: no freeze rows found in section 11")

    return rows


def validate_freeze_rows(rows: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    sha_re = re.compile(r"^[0-9a-f]{64}$")

    for row in rows:
        relpath = row["arquivo"]
        expected = row["sha256"]
        if not sha_re.match(expected):
            errors.append(f"{CONTRACT_PATH.relative_to(ROOT)}: invalid sha256 for {relpath}")
            continue

        path = ROOT / relpath
        if not path.exists():
            errors.append(f"{CONTRACT_PATH.relative_to(ROOT)}: frozen file does not exist: {relpath}")
            continue

        actual = compute_sha256(path)
        if actual != expected:
            errors.append(
                f"{CONTRACT_PATH.relative_to(ROOT)}: sha256 drift for {relpath}: expected {expected}, got {actual}"
            )

    return errors


def main() -> int:
    try:
        rows = parse_freeze_rows()
    except FreezeValidationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    errors = validate_freeze_rows(rows)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Verified {len(rows)} frozen file hash(es) successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
