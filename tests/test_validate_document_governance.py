from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts/validate_document_governance.py"


def load_validator_module():
    spec = importlib.util.spec_from_file_location("validate_document_governance", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def write_governed_doc(base: Path, relpath: str, frontmatter: dict, body: str = "# Doc\n") -> None:
    path = base / relpath
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "---\n" + yaml.safe_dump(frontmatter, sort_keys=False) + "---\n\n" + body
    path.write_text(text, encoding="utf-8", newline="\n")


def build_valid_repo(tmp_path: Path, *, map_header_override: str | None = None, action_override: str = "manter") -> Path:
    docs = {
        "docs/00_governanca/PLANO_CONTRATO_ORGANIZACAO_DOCUMENTAL.md": {
            "doc_id": "plano-contrato-organizacao-documental",
            "doc_type": "plan",
            "status": "proposed",
            "phase_scope": ["cross_phase"],
            "authority_level": "proposed",
            "owned_by": "repo_governance_bootstrap",
            "canonical_path": "/docs/00_governanca/PLANO_CONTRATO_ORGANIZACAO_DOCUMENTAL.md",
            "supersedes": [],
            "superseded_by": None,
            "must_read_before_implementation": False,
            "implementation_ready": False,
            "last_reviewed": "2026-06-24",
        },
        "docs/00_governanca/MAPA_DOCUMENTAL.md": {
            "doc_id": "mapa-documental",
            "doc_type": "inventory",
            "status": "proposed",
            "phase_scope": ["cross_phase"],
            "authority_level": "proposed",
            "owned_by": "repo_governance_bootstrap",
            "canonical_path": "/docs/00_governanca/MAPA_DOCUMENTAL.md",
            "supersedes": [],
            "superseded_by": None,
            "must_read_before_implementation": False,
            "implementation_ready": False,
            "last_reviewed": "2026-06-24",
        },
        "docs/00_governanca/ESQUEMA_METADADOS_DOCUMENTAIS.md": {
            "doc_id": "esquema-metadados-documentais",
            "doc_type": "contract",
            "status": "proposed",
            "phase_scope": ["cross_phase"],
            "authority_level": "proposed",
            "owned_by": "repo_governance_bootstrap",
            "canonical_path": "/docs/00_governanca/ESQUEMA_METADADOS_DOCUMENTAIS.md",
            "supersedes": [],
            "superseded_by": None,
            "must_read_before_implementation": False,
            "implementation_ready": False,
            "last_reviewed": "2026-06-24",
        },
        "docs/00_governanca/CONTRATO_GOVERNANCA_DOCUMENTAL.md": {
            "doc_id": "contrato-governanca-documental",
            "doc_type": "contract",
            "status": "proposed",
            "phase_scope": ["cross_phase"],
            "authority_level": "proposed",
            "owned_by": "repo_governance",
            "canonical_path": "/docs/00_governanca/CONTRATO_GOVERNANCA_DOCUMENTAL.md",
            "supersedes": [],
            "superseded_by": None,
            "must_read_before_implementation": False,
            "implementation_ready": False,
            "last_reviewed": "2026-06-24",
        },
    }

    for relpath, frontmatter in docs.items():
        body = "# MAPA\n" if relpath.endswith("MAPA_DOCUMENTAL.md") else "# Doc\n"
        write_governed_doc(tmp_path, relpath, frontmatter, body=body)

    header = map_header_override or (
        "| arquivo_atual | doc_type_proposto | phase_scope_proposto | authority_level_proposto | "
        "status_proposto | destino_canonico_planejado | acao_planejada | observacoes |"
    )
    separator = "| --- | --- | --- | --- | --- | --- | --- | --- |"
    rows = [
        "| `docs/00_governanca/PLANO_CONTRATO_ORGANIZACAO_DOCUMENTAL.md` | `plan` | `cross_phase` | `proposed` | "
        f"`proposed` | `/docs/00_governanca/PLANO_CONTRATO_ORGANIZACAO_DOCUMENTAL.md` | `{action_override}` | `ok` |",
        "| `docs/00_governanca/MAPA_DOCUMENTAL.md` | `inventory` | `cross_phase` | `proposed` | "
        f"`proposed` | `/docs/00_governanca/MAPA_DOCUMENTAL.md` | `{action_override}` | `ok` |",
        "| `docs/00_governanca/ESQUEMA_METADADOS_DOCUMENTAIS.md` | `contract` | `cross_phase` | `proposed` | "
        f"`proposed` | `/docs/00_governanca/ESQUEMA_METADADOS_DOCUMENTAIS.md` | `{action_override}` | `ok` |",
        "| `docs/00_governanca/CONTRATO_GOVERNANCA_DOCUMENTAL.md` | `contract` | `cross_phase` | `proposed` | "
        f"`proposed` | `/docs/00_governanca/CONTRATO_GOVERNANCA_DOCUMENTAL.md` | `{action_override}` | `ok` |",
    ]
    map_path = tmp_path / "docs/00_governanca/MAPA_DOCUMENTAL.md"
    map_text = map_path.read_text(encoding="utf-8")
    map_text += "\n## Inventario\n\n" + "\n".join([header, separator, *rows]) + "\n"
    map_path.write_text(map_text, encoding="utf-8", newline="\n")
    return tmp_path


def configure_module(module, tmp_path: Path) -> None:
    module.ROOT = tmp_path
    module.DOCS_ROOT = tmp_path / "docs"
    module.MAP_PATH = tmp_path / "docs/00_governanca/MAPA_DOCUMENTAL.md"


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8", newline="\n")


def test_validator_passes_on_valid_governed_set(tmp_path):
    repo = build_valid_repo(tmp_path)
    module = load_validator_module()
    configure_module(module, repo)
    assert module.main() == 0


def test_validator_fails_when_required_field_is_missing(tmp_path, capsys):
    repo = build_valid_repo(tmp_path)
    doc_path = repo / "docs/00_governanca/ESQUEMA_METADADOS_DOCUMENTAIS.md"
    text = doc_path.read_text(encoding="utf-8").replace("last_reviewed: '2026-06-24'\n", "")
    write_text(doc_path, text)
    module = load_validator_module()
    configure_module(module, repo)
    assert module.main() == 1
    stderr = capsys.readouterr().err
    assert "missing required fields: last_reviewed" in stderr


def test_validator_fails_when_status_and_authority_conflict(tmp_path, capsys):
    repo = build_valid_repo(tmp_path)
    doc_path = repo / "docs/00_governanca/CONTRATO_GOVERNANCA_DOCUMENTAL.md"
    text = doc_path.read_text(encoding="utf-8").replace("authority_level: proposed\n", "authority_level: canonical\n")
    write_text(doc_path, text)
    module = load_validator_module()
    configure_module(module, repo)
    assert module.main() == 1
    stderr = capsys.readouterr().err
    assert "proposed documents must use authority_level proposed" in stderr


def test_validator_fails_when_implementation_flags_are_incoherent(tmp_path, capsys):
    repo = build_valid_repo(tmp_path)
    doc_path = repo / "docs/00_governanca/ESQUEMA_METADADOS_DOCUMENTAIS.md"
    text = doc_path.read_text(encoding="utf-8")
    text = text.replace("implementation_ready: false\n", "implementation_ready: true\n")
    text = text.replace("status: proposed\n", "status: current\n")
    text = text.replace("authority_level: proposed\n", "authority_level: operational\n")
    write_text(doc_path, text)
    module = load_validator_module()
    configure_module(module, repo)
    assert module.main() == 1
    stderr = capsys.readouterr().err
    assert "implementation_ready true requires must_read_before_implementation true" in stderr


def test_validator_fails_when_canonical_path_diverges(tmp_path, capsys):
    repo = build_valid_repo(tmp_path)
    doc_path = repo / "docs/00_governanca/ESQUEMA_METADADOS_DOCUMENTAIS.md"
    text = doc_path.read_text(encoding="utf-8").replace(
        "/docs/00_governanca/ESQUEMA_METADADOS_DOCUMENTAIS.md",
        "/docs/00_governanca/ESQUEMA_ERRADO.md",
        1,
    )
    write_text(doc_path, text)
    module = load_validator_module()
    configure_module(module, repo)
    assert module.main() == 1
    stderr = capsys.readouterr().err
    assert "canonical_path '/docs/00_governanca/ESQUEMA_ERRADO.md' does not match real path" in stderr


def test_validator_fails_when_superseded_by_target_is_missing(tmp_path, capsys):
    repo = build_valid_repo(tmp_path)
    doc_path = repo / "docs/00_governanca/PLANO_CONTRATO_ORGANIZACAO_DOCUMENTAL.md"
    text = doc_path.read_text(encoding="utf-8")
    text = text.replace("status: proposed\n", "status: deprecated\n")
    text = text.replace("authority_level: proposed\n", "authority_level: historical\n")
    text = text.replace("superseded_by: null\n", "superseded_by: /docs/00_governanca/INEXISTENTE.md\n")
    write_text(doc_path, text)
    module = load_validator_module()
    configure_module(module, repo)
    assert module.main() == 1
    stderr = capsys.readouterr().err
    assert "superseded_by target does not exist" in stderr


def test_validator_fails_when_current_contracts_conflict(tmp_path, capsys):
    repo = build_valid_repo(tmp_path)
    for name in ("ESQUEMA_METADADOS_DOCUMENTAIS.md", "CONTRATO_GOVERNANCA_DOCUMENTAL.md"):
        doc_path = repo / f"docs/00_governanca/{name}"
        text = doc_path.read_text(encoding="utf-8")
        text = text.replace("status: proposed\n", "status: current\n")
        text = text.replace("authority_level: proposed\n", "authority_level: canonical\n")
        text = text.replace("phase_scope:\n- cross_phase\n", "phase_scope:\n- phase_1\n")
        write_text(doc_path, text)
    map_path = repo / "docs/00_governanca/MAPA_DOCUMENTAL.md"
    map_text = map_path.read_text(encoding="utf-8")
    map_text = map_text.replace("| `cross_phase` | `proposed` | `proposed` |", "| `phase_1` | `canonical` | `current` |")
    write_text(map_path, map_text)
    module = load_validator_module()
    configure_module(module, repo)
    assert module.main() == 1
    stderr = capsys.readouterr().err
    assert "conflicts with docs/00_governanca/CONTRATO_GOVERNANCA_DOCUMENTAL.md" in stderr or "conflicts with docs/00_governanca/ESQUEMA_METADADOS_DOCUMENTAIS.md" in stderr


def test_validator_fails_when_map_row_missing_action_column(tmp_path, capsys):
    bad_header = (
        "| arquivo_atual | doc_type_proposto | phase_scope_proposto | authority_level_proposto | "
        "status_proposto | destino_canonico_planejado | observacoes |"
    )
    repo = build_valid_repo(tmp_path, map_header_override=bad_header)
    module = load_validator_module()
    configure_module(module, repo)
    assert module.main() == 1
    stderr = capsys.readouterr().err
    assert "missing required columns: acao_planejada" in stderr


def test_validator_fails_when_map_action_is_empty(tmp_path, capsys):
    repo = build_valid_repo(tmp_path, action_override="")
    module = load_validator_module()
    configure_module(module, repo)
    assert module.main() == 1
    stderr = capsys.readouterr().err
    assert "has empty acao_planejada" in stderr


def test_validator_fails_when_map_row_has_structural_column_mismatch(tmp_path, capsys):
    repo = build_valid_repo(tmp_path)
    map_path = repo / "docs/00_governanca/MAPA_DOCUMENTAL.md"
    text = map_path.read_text(encoding="utf-8")
    broken_row = (
        "| `docs/00_governanca/MAPA_DOCUMENTAL.md` | `inventory` | `cross_phase` | `proposed` | "
        "`proposed` | `/docs/00_governanca/MAPA_DOCUMENTAL.md` | `manter` |\n"
    )
    fixed_row = (
        "| `docs/00_governanca/MAPA_DOCUMENTAL.md` | `inventory` | `cross_phase` | `proposed` | "
        "`proposed` | `/docs/00_governanca/MAPA_DOCUMENTAL.md` | `manter` | `ok` |\n"
    )
    text = text.replace(fixed_row, broken_row)
    write_text(map_path, text)
    module = load_validator_module()
    configure_module(module, repo)
    assert module.main() == 1
    stderr = capsys.readouterr().err
    assert "row has 7 cells but header has 8" in stderr


def test_validator_fails_when_governed_doc_missing_from_map(tmp_path, capsys):
    repo = build_valid_repo(tmp_path)
    map_path = repo / "docs/00_governanca/MAPA_DOCUMENTAL.md"
    text = map_path.read_text(encoding="utf-8")
    text = text.replace(
        "| `docs/00_governanca/CONTRATO_GOVERNANCA_DOCUMENTAL.md` | `contract` | `cross_phase` | `proposed` | `proposed` | `/docs/00_governanca/CONTRATO_GOVERNANCA_DOCUMENTAL.md` | `manter` | `ok` |\n",
        "",
    )
    map_path.write_text(text, encoding="utf-8", newline="\n")
    module = load_validator_module()
    configure_module(module, repo)
    assert module.main() == 1
    stderr = capsys.readouterr().err
    assert "docs/00_governanca/CONTRATO_GOVERNANCA_DOCUMENTAL.md: missing from MAPA_DOCUMENTAL.md" in stderr


def test_validator_fails_when_map_metadata_diverges_from_frontmatter(tmp_path, capsys):
    repo = build_valid_repo(tmp_path)
    map_path = repo / "docs/00_governanca/MAPA_DOCUMENTAL.md"
    text = map_path.read_text(encoding="utf-8").replace(
        "| `docs/00_governanca/ESQUEMA_METADADOS_DOCUMENTAIS.md` | `contract` | `cross_phase` | `proposed` | `proposed` | `/docs/00_governanca/ESQUEMA_METADADOS_DOCUMENTAIS.md` | `manter` | `ok` |",
        "| `docs/00_governanca/ESQUEMA_METADADOS_DOCUMENTAIS.md` | `review` | `cross_phase` | `proposed` | `proposed` | `/docs/00_governanca/ESQUEMA_METADADOS_DOCUMENTAIS.md` | `manter` | `ok` |",
    )
    write_text(map_path, text)
    module = load_validator_module()
    configure_module(module, repo)
    assert module.main() == 1
    stderr = capsys.readouterr().err
    assert "MAPA doc_type_proposto diverges from frontmatter" in stderr


def test_validator_fails_for_active_contract_outside_docs(tmp_path, capsys):
    repo = build_valid_repo(tmp_path)
    rogue = {
        "doc_id": "rogue-contract",
        "doc_type": "contract",
        "status": "current",
        "phase_scope": ["phase_1"],
        "authority_level": "operational",
        "owned_by": "rogue",
        "canonical_path": "/docs/05_fases/fase_1/ROGUE.md",
        "supersedes": [],
        "superseded_by": None,
        "must_read_before_implementation": True,
        "implementation_ready": True,
        "last_reviewed": "2026-06-24",
    }
    write_governed_doc(repo, "ROGUE.md", rogue)
    module = load_validator_module()
    configure_module(module, repo)
    assert module.main() == 1
    stderr = capsys.readouterr().err
    assert "ROGUE.md: active contract outside docs/ is prohibited" in stderr


def test_gitattributes_enforces_lf_for_governed_extensions():
    content = (REPO_ROOT / ".gitattributes").read_text(encoding="utf-8")
    assert "*.md text eol=lf" in content
    assert "*.yml text eol=lf" in content
    assert "*.yaml text eol=lf" in content
    assert "*.py text eol=lf" in content


def test_gitattributes_normalizes_markdown_to_lf_in_git_index(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    write_text(repo / ".gitattributes", (REPO_ROOT / ".gitattributes").read_text(encoding="utf-8"))
    (repo / "sample.md").write_text("a\r\nb\r\n", encoding="utf-8", newline="")
    (repo / "sample.bin").write_bytes(b"a\r\nb\r\n")
    subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True, text=True)
    subprocess.run(["git", "add", ".gitattributes", "sample.md", "sample.bin"], cwd=repo, check=True, capture_output=True, text=True)
    indexed_markdown = subprocess.run(
        ["git", "show", ":sample.md"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    indexed_binary = subprocess.run(
        ["git", "show", ":sample.bin"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=False,
    ).stdout
    assert "\r\n" not in indexed_markdown
    assert indexed_markdown == "a\nb\n"
    assert indexed_binary == b"a\r\nb\r\n"


def test_workflow_runs_validator_on_push_and_pull_request():
    workflow = yaml.safe_load((REPO_ROOT / ".github/workflows/validate-document-governance.yml").read_text(encoding="utf-8"))
    assert workflow["name"] == "Validate Document Governance"
    assert "push" in workflow["on"]
    assert "pull_request" in workflow["on"]
    steps = workflow["jobs"]["validate-document-governance"]["steps"]
    run_steps = [step.get("run", "") for step in steps]
    assert any("python scripts/validate_document_governance.py" in step for step in run_steps)
    assert any("pytest -q tests/test_validate_document_governance.py" in step for step in run_steps)
