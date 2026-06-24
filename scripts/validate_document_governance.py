#!/usr/bin/env python3
"""Validate documentary governance rules for the governed docs set."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = ROOT / "docs"
MAP_PATH = ROOT / "docs/00_governanca/MAPA_DOCUMENTAL.md"

REQUIRED_FIELDS = {
    "doc_id",
    "doc_type",
    "status",
    "phase_scope",
    "authority_level",
    "owned_by",
    "canonical_path",
    "supersedes",
    "superseded_by",
    "must_read_before_implementation",
    "implementation_ready",
    "last_reviewed",
}

DOC_TYPES = {"contract", "approval", "review", "adr", "inventory", "plan", "archive", "handoff"}
STATUSES = {"draft", "proposed", "approved", "current", "deprecated", "archived"}
PHASES = {"phase_0", "phase_1", "phase_2", "phase_3", "cross_phase"}
AUTHORITIES = {"ssot", "canonical", "operational", "supporting", "historical", "proposed"}
ACTIVE_AUTHORITIES = {"ssot", "canonical", "operational", "supporting"}
CONTRACT_CURRENT_AUTHORITIES = {"ssot", "canonical", "operational"}
CURRENT_DTYPE_AUTHORITIES = {
    "contract": CONTRACT_CURRENT_AUTHORITIES,
    "approval": {"supporting"},
    "review": {"supporting"},
    "adr": {"supporting"},
    "inventory": {"supporting"},
    "plan": {"supporting"},
    "handoff": {"supporting"},
}

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
NUMBERED_DIR_RE = re.compile(r"^\d{2}_.+")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MAP_REQUIRED_COLUMNS = {
    "arquivo_atual",
    "doc_type_proposto",
    "phase_scope_proposto",
    "authority_level_proposto",
    "status_proposto",
    "destino_canonico_planejado",
    "acao_planejada",
}


@dataclass
class GovernedDoc:
    path: Path
    relpath: str
    frontmatter: dict


class ValidationError(RuntimeError):
    pass


def find_governed_docs() -> list[Path]:
    docs: list[Path] = []
    for path in DOCS_ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT).as_posix()
        parts = rel.split("/")
        if len(parts) < 2:
            continue
        if NUMBERED_DIR_RE.match(parts[1]):
            docs.append(path)
    return sorted(docs)


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValidationError(f"{path.relative_to(ROOT)}: missing frontmatter block")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValidationError(f"{path.relative_to(ROOT)}: frontmatter must parse as mapping")
    return data


def normalize_line_target(target: str) -> str:
    cleaned = target.strip().strip("<>")
    if re.search(r":\d+$", cleaned):
        cleaned = cleaned.rsplit(":", 1)[0]
    return cleaned


def validate_links(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for raw_target in MARKDOWN_LINK_RE.findall(text):
        target = normalize_line_target(raw_target)
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if target.startswith("/home/davis/SCOUT_BEACHHANDBALL/"):
            local = Path(target)
        elif target.startswith("/docs/"):
            local = ROOT / target.lstrip("/")
        elif target.startswith("./") or target.startswith("../"):
            local = (path.parent / target).resolve()
        else:
            continue
        if not local.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken local link target {raw_target}")
    return errors


def validate_required_fields(doc: GovernedDoc) -> list[str]:
    data = doc.frontmatter
    errors = []
    missing = sorted(REQUIRED_FIELDS - set(data))
    if missing:
        errors.append(f"{doc.relpath}: missing required fields: {', '.join(missing)}")
    return errors


def validate_scalar_types(doc: GovernedDoc) -> list[str]:
    data = doc.frontmatter
    errors = []

    if data.get("doc_type") not in DOC_TYPES:
        errors.append(f"{doc.relpath}: invalid doc_type {data.get('doc_type')!r}")
    if data.get("status") not in STATUSES:
        errors.append(f"{doc.relpath}: invalid status {data.get('status')!r}")
    if data.get("authority_level") not in AUTHORITIES:
        errors.append(f"{doc.relpath}: invalid authority_level {data.get('authority_level')!r}")

    phase_scope = data.get("phase_scope")
    if not isinstance(phase_scope, list) or not phase_scope:
        errors.append(f"{doc.relpath}: phase_scope must be a non-empty list")
    else:
        invalid = [item for item in phase_scope if item not in PHASES]
        if invalid:
            errors.append(f"{doc.relpath}: invalid phase_scope values: {', '.join(invalid)}")
        if len(phase_scope) != len(set(phase_scope)):
            errors.append(f"{doc.relpath}: phase_scope contains duplicate values")
        if "cross_phase" in phase_scope and len(phase_scope) > 1:
            errors.append(f"{doc.relpath}: cross_phase cannot coexist with explicit phases")

    if not isinstance(data.get("owned_by"), str) or not data["owned_by"].strip():
        errors.append(f"{doc.relpath}: owned_by must be a non-empty string")
    if not isinstance(data.get("canonical_path"), str) or not data["canonical_path"].startswith("/docs/"):
        errors.append(f"{doc.relpath}: canonical_path must start with /docs/")
    if not isinstance(data.get("supersedes"), list):
        errors.append(f"{doc.relpath}: supersedes must be a list")
    if data.get("superseded_by") is not None and not isinstance(data.get("superseded_by"), str):
        errors.append(f"{doc.relpath}: superseded_by must be string or null")
    if not isinstance(data.get("must_read_before_implementation"), bool):
        errors.append(f"{doc.relpath}: must_read_before_implementation must be boolean")
    if not isinstance(data.get("implementation_ready"), bool):
        errors.append(f"{doc.relpath}: implementation_ready must be boolean")
    if not isinstance(data.get("last_reviewed"), str) or not DATE_RE.match(data["last_reviewed"]):
        errors.append(f"{doc.relpath}: last_reviewed must be YYYY-MM-DD")

    return errors


def validate_status_and_authority(doc: GovernedDoc) -> list[str]:
    data = doc.frontmatter
    status = data["status"]
    authority = data["authority_level"]
    doc_type = data["doc_type"]
    errors = []

    if status in {"draft", "proposed"} and authority != "proposed":
        errors.append(f"{doc.relpath}: {status} documents must use authority_level proposed")
    if status == "approved":
        if doc_type == "approval":
            if authority not in {"proposed", "supporting"}:
                errors.append(f"{doc.relpath}: approved approval must use proposed or supporting authority")
        elif authority != "proposed":
            errors.append(f"{doc.relpath}: approved documents must use authority_level proposed")
    if status == "current":
        if authority not in ACTIVE_AUTHORITIES:
            errors.append(f"{doc.relpath}: current documents must use an active authority level")
        allowed = CURRENT_DTYPE_AUTHORITIES.get(doc_type)
        if allowed is None and doc_type == "archive":
            errors.append(f"{doc.relpath}: archive cannot use status current")
        elif allowed is not None and authority not in allowed:
            errors.append(f"{doc.relpath}: current {doc_type} must use one of {sorted(allowed)}")
    if status in {"deprecated", "archived"} and authority != "historical":
        errors.append(f"{doc.relpath}: {status} documents must use authority_level historical")

    return errors


def validate_phase_scope_rules(doc: GovernedDoc) -> list[str]:
    data = doc.frontmatter
    doc_type = data["doc_type"]
    status = data["status"]
    authority = data["authority_level"]
    phase_scope = data["phase_scope"]
    errors = []

    if (
        doc_type in {"contract", "approval"}
        and status == "current"
        and authority in {"ssot", "canonical", "operational"}
        and len(phase_scope) != 1
    ):
        errors.append(f"{doc.relpath}: current {doc_type} with active authority must declare exactly one scope")
    return errors


def validate_implementation_flags(doc: GovernedDoc) -> list[str]:
    data = doc.frontmatter
    errors = []
    if data["implementation_ready"]:
        if data["doc_type"] != "contract":
            errors.append(f"{doc.relpath}: implementation_ready true requires doc_type contract")
        if data["status"] != "current":
            errors.append(f"{doc.relpath}: implementation_ready true requires status current")
        if data["authority_level"] not in {"operational", "canonical"}:
            errors.append(f"{doc.relpath}: implementation_ready true requires operational or canonical authority")
        if not data["must_read_before_implementation"]:
            errors.append(f"{doc.relpath}: implementation_ready true requires must_read_before_implementation true")
    return errors


def validate_canonical_path(doc: GovernedDoc) -> list[str]:
    expected = "/" + doc.relpath
    actual = doc.frontmatter["canonical_path"]
    if actual != expected:
        return [f"{doc.relpath}: canonical_path {actual!r} does not match real path {expected!r}"]
    return []


def validate_supersession(doc: GovernedDoc) -> list[str]:
    data = doc.frontmatter
    errors = []
    superseded_by = data["superseded_by"]
    if data["status"] == "deprecated" and not superseded_by:
        errors.append(f"{doc.relpath}: deprecated document must define superseded_by")
    if superseded_by:
        successor = ROOT / superseded_by.lstrip("/")
        if not successor.exists():
            errors.append(f"{doc.relpath}: superseded_by target does not exist: {superseded_by}")
    return errors


def parse_map_rows() -> tuple[dict[str, dict[str, str]], list[str]]:
    rows: dict[str, dict[str, str]] = {}
    errors: list[str] = []
    text = MAP_PATH.read_text(encoding="utf-8")
    lines = text.splitlines()
    current_headers: list[str] | None = None

    for index, line in enumerate(lines):
        if not line.startswith("|"):
            current_headers = None
            continue

        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not cells:
            continue

        is_separator = all(cell.replace("-", "").replace(":", "") == "" for cell in cells)
        if is_separator:
            continue

        if index + 1 < len(lines):
            next_line = lines[index + 1]
            if next_line.startswith("|"):
                next_cells = [cell.strip() for cell in next_line.strip().strip("|").split("|")]
                if next_cells and all(cell.replace("-", "").replace(":", "") == "" for cell in next_cells):
                    current_headers = cells
                    missing_columns = sorted(MAP_REQUIRED_COLUMNS - set(current_headers))
                    if "arquivo_atual" in current_headers and missing_columns:
                        errors.append(
                            f"{MAP_PATH.relative_to(ROOT)}: table header missing required columns: "
                            + ", ".join(missing_columns)
                        )
                    continue

        if current_headers is None:
            continue

        if len(cells) != len(current_headers):
            errors.append(
                f"{MAP_PATH.relative_to(ROOT)}: row has {len(cells)} cells but header has {len(current_headers)}"
            )
            continue

        row = dict(zip(current_headers, cells))
        path_cell = row.get("arquivo_atual", "")
        if not (path_cell.startswith("`") and path_cell.endswith("`")):
            continue

        missing_columns = sorted(MAP_REQUIRED_COLUMNS - set(current_headers))
        if missing_columns:
            errors.append(
                f"{MAP_PATH.relative_to(ROOT)}: table for {path_cell.strip('`')} missing required columns: "
                + ", ".join(missing_columns)
            )
            continue

        normalized_row = {
            "doc_type_proposto": row["doc_type_proposto"].strip("`"),
            "phase_scope_proposto": row["phase_scope_proposto"].strip("`"),
            "authority_level_proposto": row["authority_level_proposto"].strip("`"),
            "status_proposto": row["status_proposto"].strip("`"),
            "destino_canonico_planejado": row["destino_canonico_planejado"].strip("`"),
            "acao_planejada": row["acao_planejada"].strip("`"),
        }
        if not normalized_row["acao_planejada"]:
            errors.append(f"{MAP_PATH.relative_to(ROOT)}: row for {path_cell} has empty acao_planejada")
            continue

        rows[path_cell.strip("`")] = normalized_row
    return rows, errors


def validate_map(governed_docs: list[GovernedDoc]) -> list[str]:
    rows, errors = parse_map_rows()
    for doc in governed_docs:
        row = rows.get(doc.relpath)
        if row is None:
            errors.append(f"{doc.relpath}: missing from MAPA_DOCUMENTAL.md")
            continue
        expected_scope = ", ".join(doc.frontmatter["phase_scope"])
        if row["doc_type_proposto"] != doc.frontmatter["doc_type"]:
            errors.append(f"{doc.relpath}: MAPA doc_type_proposto diverges from frontmatter")
        if row["phase_scope_proposto"] != expected_scope:
            errors.append(f"{doc.relpath}: MAPA phase_scope_proposto diverges from frontmatter")
        if row["authority_level_proposto"] != doc.frontmatter["authority_level"]:
            errors.append(f"{doc.relpath}: MAPA authority_level_proposto diverges from frontmatter")
        if row["status_proposto"] != doc.frontmatter["status"]:
            errors.append(f"{doc.relpath}: MAPA status_proposto diverges from frontmatter")
        if row["destino_canonico_planejado"] != doc.frontmatter["canonical_path"]:
            errors.append(f"{doc.relpath}: MAPA destino_canonico_planejado diverges from frontmatter")
        if not row["acao_planejada"]:
            errors.append(f"{doc.relpath}: MAPA acao_planejada cannot be empty")
    return errors


def validate_current_contract_conflicts(governed_docs: list[GovernedDoc]) -> list[str]:
    errors: list[str] = []
    seen: dict[tuple[str, str], str] = {}
    for doc in governed_docs:
        data = doc.frontmatter
        if data["doc_type"] != "contract" or data["status"] != "current":
            continue
        authority = data["authority_level"]
        if authority not in CONTRACT_CURRENT_AUTHORITIES:
            continue
        for phase in data["phase_scope"]:
            key = (phase, authority)
            previous = seen.get(key)
            if previous:
                errors.append(
                    f"{doc.relpath}: conflicts with {previous} for current contract phase {phase} and authority {authority}"
                )
            else:
                seen[key] = doc.relpath
    return errors


def validate_active_contract_outside_docs() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or path == MAP_PATH:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith("docs/"):
            continue
        try:
            frontmatter = parse_frontmatter(path)
        except ValidationError:
            continue
        if frontmatter.get("doc_type") == "contract" and frontmatter.get("status") == "current":
            errors.append(f"{rel}: active contract outside docs/ is prohibited")
    return errors


def build_governed_docs() -> list[GovernedDoc]:
    docs = []
    for path in find_governed_docs():
        docs.append(GovernedDoc(path=path, relpath=path.relative_to(ROOT).as_posix(), frontmatter=parse_frontmatter(path)))
    return docs


def main() -> int:
    errors: list[str] = []
    try:
        governed_docs = build_governed_docs()
    except ValidationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    for doc in governed_docs:
        errors.extend(validate_required_fields(doc))
        if any(field not in doc.frontmatter for field in REQUIRED_FIELDS):
            continue
        errors.extend(validate_scalar_types(doc))
        if any(
            (
                doc.frontmatter["doc_type"] not in DOC_TYPES,
                doc.frontmatter["status"] not in STATUSES,
                doc.frontmatter["authority_level"] not in AUTHORITIES,
                not isinstance(doc.frontmatter["phase_scope"], list),
                not doc.frontmatter["phase_scope"],
            )
        ):
            continue
        errors.extend(validate_status_and_authority(doc))
        errors.extend(validate_phase_scope_rules(doc))
        errors.extend(validate_implementation_flags(doc))
        errors.extend(validate_canonical_path(doc))
        errors.extend(validate_supersession(doc))
        errors.extend(validate_links(doc.path))

    errors.extend(validate_current_contract_conflicts(governed_docs))
    errors.extend(validate_active_contract_outside_docs())
    errors.extend(validate_map(governed_docs))

    if errors:
        for error in sorted(set(errors)):
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(governed_docs)} governed document(s) successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
