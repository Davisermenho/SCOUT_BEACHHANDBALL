from __future__ import annotations

import re
import subprocess
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = REPO_ROOT / "docs/05_fases/fase_0/CONTRATO_UNICO_FASE_0.md"
APPROVAL_PATH = REPO_ROOT / "docs/05_fases/fase_0/APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md"
APPROVAL_SNAPSHOT_PATH = (
    REPO_ROOT / "docs/08_historico_deprecado/APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO__RATIFICADA_2026_06_23.md"
)
CONTRACT_SNAPSHOT_PATH = REPO_ROOT / "docs/08_historico_deprecado/CONTRATO_UNICO_FASE_0__FREEZE_2026_06_24_PRE_MIGRACAO.md"
MAP_PATH = REPO_ROOT / "docs/00_governanca/MAPA_DOCUMENTAL.md"
HASH_SCRIPT = REPO_ROOT / "scripts/verify_phase0_freeze_hashes.py"


def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    assert match is not None, f"{path} is missing frontmatter"
    data = yaml.safe_load(match.group(1))
    assert isinstance(data, dict)
    return data


def test_phase0_contract_has_expected_frontmatter():
    data = read_frontmatter(CONTRACT_PATH)
    assert data["doc_id"] == "contrato-unico-fase-0"
    assert data["doc_type"] == "contract"
    assert data["status"] == "current"
    assert data["phase_scope"] == ["phase_0"]
    assert data["authority_level"] == "operational"
    assert data["canonical_path"] == "/docs/05_fases/fase_0/CONTRATO_UNICO_FASE_0.md"
    assert data["must_read_before_implementation"] is True
    assert data["implementation_ready"] is False


def test_phase0_contract_contains_required_sections():
    text = CONTRACT_PATH.read_text(encoding="utf-8")
    headings = [
        "## 1. Objetivo da Fase 0",
        "## 2. Cadeia de autoridade interna da Fase 0",
        "## 3. Escopo incluido",
        "## 4. Escopo proibido",
        "## 5. Vocabulario canonico aprovado",
        "## 6. Invariantes semanticos obrigatorios",
        "## 7. Gates humanos e documentais",
        "## 8. Evidencias exigidas",
        "## 9. Criterio de conclusao",
        "## 10. Criterio de liberacao para Fase 1",
        "## 11. Anexos obrigatorios e hashes congelados",
        "## 12. Lista explicita dos documentos absorvidos ou reclassificados pela consolidacao",
    ]
    for heading in headings:
        assert heading in text


def test_phase0_hash_verifier_passes():
    result = subprocess.run(
        ["python3", str(HASH_SCRIPT)],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "Verified" in result.stdout


def test_phase0_contract_is_unique_current_phase0_contract_in_governed_docs():
    matches: list[Path] = []
    for path in (REPO_ROOT / "docs").rglob("*.md"):
        parts = path.relative_to(REPO_ROOT).as_posix().split("/")
        if len(parts) < 2 or not re.match(r"^\d{2}_.+", parts[1]):
            continue
        data = read_frontmatter(path)
        if (
            data.get("doc_type") == "contract"
            and data.get("status") == "current"
            and data.get("authority_level") in {"ssot", "canonical", "operational"}
            and data.get("phase_scope") == ["phase_0"]
        ):
            matches.append(path)
    assert matches == [CONTRACT_PATH]


def test_phase0_approval_reopened_human_gate_after_migration():
    text = APPROVAL_PATH.read_text(encoding="utf-8")
    assert "- status: `aguardando_revalidacao_humana`" in text
    assert "- liberado para iniciar Fase 1: `nao`" in text
    assert "revalidacao_humana_do_freeze_pos_migracao" in text


def test_phase0_historical_snapshots_are_preserved():
    assert APPROVAL_SNAPSHOT_PATH.exists()
    assert CONTRACT_SNAPSHOT_PATH.exists()
    approval_data = read_frontmatter(APPROVAL_PATH)
    assert approval_data["supersedes"] == [
        "/docs/08_historico_deprecado/APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO__RATIFICADA_2026_06_23.md"
    ]


def test_phase0_approval_points_to_contract_freeze_source():
    text = APPROVAL_PATH.read_text(encoding="utf-8")
    assert "secao `11` de `CONTRATO_UNICO_FASE_0.md`" in text
    assert "baseline candidato pos-migracao" in text


def test_root_no_longer_contains_stage_contracts_migrated_to_docs():
    migrated_roots = [
        "PROBLEMA_FINAL.md",
        "MVP.md",
        "ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md",
        "ESPECIFICACAO_IMPLEMENTACAO_MVP.md",
        "PLANO_EXECUCAO_IA_POR_FASES.md",
        "APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md",
        "MATRIZ_ACHADOS_FASE_0.md",
        "ORDEM_EXECUCAO_FASE_1.md",
    ]
    for relpath in migrated_roots:
        assert not (REPO_ROOT / relpath).exists(), relpath


def test_map_reflects_phase0_consolidation():
    text = MAP_PATH.read_text(encoding="utf-8")
    assert (
        "| `docs/05_fases/fase_0/CONTRATO_UNICO_FASE_0.md` | `contract` | `phase_0` | `operational` | `current` | "
        "`/docs/05_fases/fase_0/CONTRATO_UNICO_FASE_0.md` | manter como contrato unico vigente | "
        "consolidacao da Etapa 5; ponto operacional unico da Fase 0 |"
    ) in text
    assert (
        "| `docs/03_ontologia/ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md` | `review` | `phase_0` | `supporting` | `current` | "
        "`/docs/03_ontologia/ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md` | manter apos migracao | "
        "anexo semantico principal subordinado ao contrato unico da Fase 0 |"
    ) in text
    assert (
        "| `docs/05_fases/fase_0/APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md` | `approval` | `phase_0` | `supporting` | `current` | "
        "`/docs/05_fases/fase_0/APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md` | manter como gate em revalidacao humana | "
        "gate humano da Fase 0 em re-freeze pos-migracao |"
    ) in text
    assert (
        "| `docs/05_fases/fase_0/MATRIZ_ACHADOS_FASE_0.md` | `review` | `phase_0` | `supporting` | `current` | "
        "`/docs/05_fases/fase_0/MATRIZ_ACHADOS_FASE_0.md` | manter apos migracao | "
        "matriz de destino dos achados, subordinada ao contrato unico |"
    ) in text
