# Audit script for deterministic ontology pipeline validation — Handebol de Areia.
# Run as: python audit_ontology_pipeline.py
# Reads the seven canonical .md files from ../files (relative to this script's own
# location, not the caller's cwd) and writes reports to ../results_auditoria_python.
# Importing this module (e.g. from tests) does not touch the filesystem — only
# running it as a script (__main__) does.
# Contrato normativo: ../results_auditoria_python/02_AUDITORIA_PYTHON_SPEC.md
# (saídas obrigatórias, verificações obrigatórias, contrato de dados). Qualquer
# mudança de comportamento aqui deve ser refletida lá.

SCRIPT_VERSION = "2.0.0"

from pathlib import Path
import re, json, hashlib
from collections import Counter
from datetime import datetime, timezone
import pandas as pd

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
BASE = PROJECT_ROOT / "files"
OUT = PROJECT_ROOT / "results_auditoria_python"

FILES = [
    "Regras Ontológicas do Handebol.md",
    "Vocabulário e Taxonomia.md",
    "Regras 1–18.md",
    "Apêndices.md",
    "Rastreabilidade.md",
    "Decisões Humanas.md",
    "Operacional.md",
]

STATEMENT_ID_RE = re.compile(r"\[(BH-[A-Z0-9\-]+-\d{3})\]\s*(.+)")
STATUS_RE = re.compile(r"\b(VALIDADO|CONCLUÍDA_E_VALIDADA|RASCUNHO|NÃO_INICIADA|NAO_INICIADA|PENDENTE|EM_CONSTRUÇÃO|APROVADA|BLOQUEADO|AGUARDANDO_AVALIAÇÃO_HUMANA|CATEGORIA_CONTROLADA_COM_AVALIAÇÃO_HUMANA)\b", re.I)
NO_PREDICATE_MARKER = "(predicado_não_detectado)"


def parse_spo(sentence, canonical_predicates):
    s = sentence.strip().rstrip(".")
    other_candidates = set(re.findall(r"\b[^\s,;]+_[^\s,;]+(?:_[^\s,;]+)*\b", s))
    other_candidates.update(["é_um", "é_disjunto_de", "é_instância_de", "possui", "possui_status"])
    # Predicados canônicos são tentados antes dos demais candidatos: caso contrário,
    # um objeto/sujeito com underscore mais longo que o predicado real (ex: a frase
    # "X possui_status TERMO_CANÔNICO", onde "TERMO_CANÔNICO" tem mais caracteres que
    # "possui_status") venceria a ordenação por comprimento e seria escolhido por engano.
    # O desempate alfabético (além do comprimento) é necessário para determinismo:
    # candidatos vêm de um set, cuja ordem de iteração varia entre execuções do
    # processo Python (hash seed aleatório) — sem desempate estável, candidatos de
    # mesmo comprimento poderiam ser escolhidos em ordem diferente a cada execução,
    # quebrando a reprodutibilidade do pipeline.
    for pred in sorted(canonical_predicates, key=lambda p: (-len(p), p)):
        mm = re.search(r"\b" + re.escape(pred) + r"\b", s)
        if mm:
            return s[:mm.start()].strip(), pred, s[mm.end():].strip()
    for pred in sorted(other_candidates, key=lambda p: (-len(p), p)):
        mm = re.search(r"\b" + re.escape(pred) + r"\b", s)
        if mm:
            return s[:mm.start()].strip(), pred, s[mm.end():].strip()
    # Nenhum candidato a predicado (canônico ou com underscore) foi encontrado na
    # frase: ela não segue a linguagem controlada. Marcar explicitamente em vez de
    # adivinhar a 2ª palavra da frase como se fosse um predicado real (isso fazia
    # substantivos comuns, ex. "Cartão", "Anel", aparecerem disfarçados de predicado
    # inválido em 04_invalid_predicates.csv).
    return s, NO_PREDICATE_MARKER, ""


def norm(term):
    term = re.sub(r"\s*\[[^\]]+\]\s*$", "", term).strip(" .,:;()")
    term = re.sub(r"^(A|O|Uma|Um|Os|As|Cada|Se|No|Na|Quando)\s+", "", term)
    return term


def extract_vocab_terms(vocab_text):
    vocab_terms = set()
    for line in vocab_text.splitlines():
        s = line.strip()
        for pat in [
            r"(.+?) possui_status TERMO_CANÔNICO\.",
            r"(.+?) é_um (.+?)\.",
            r"(.+?) é_disjunto_de (.+?)\.",
            r"(.+?) é_subclasse_de (.+?)\.",
        ]:
            m = re.match(pat, s)
            if m:
                vocab_terms.update(x.strip() for x in m.groups())
    vocab_terms |= {t.replace(" ", "_") for t in vocab_terms}
    return vocab_terms


def extract_decision_blocks(text):
    bare_id_re = re.compile(r"^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+$")
    heading_id_re = re.compile(r"^##\s+([A-Z]{1,6}-[A-Z0-9\-]+)\b")
    blocks = []
    current_id, current_lines = None, []
    for line in text.splitlines():
        stripped = line.strip()
        heading_m = heading_id_re.match(stripped)
        bare_m = None if heading_m else bare_id_re.match(stripped)
        if heading_m or bare_m:
            if current_id is not None:
                blocks.append((current_id, "\n".join(current_lines)))
            current_id = heading_m.group(1) if heading_m else stripped
            current_lines = [line]
            continue
        if current_id is not None:
            current_lines.append(line)
    if current_id is not None:
        blocks.append((current_id, "\n".join(current_lines)))
    return blocks


def is_decision_block_weak(block_text):
    has_pergunta = bool(re.search(r"pergunta", block_text, re.I))
    has_resposta_literal = bool(re.search(r"resposta", block_text, re.I)) and bool(re.search(r"literal", block_text, re.I))
    has_decisoes_extraidas = bool(re.search(r"decis(?:õ|o)es[_\s]extra", block_text, re.I))
    return not (has_pergunta and has_resposta_literal and has_decisoes_extraidas)


def main():
    OUT.mkdir(exist_ok=True)

    missing_files = [str((BASE / name).resolve()) for name in FILES if not (BASE / name).exists()]
    if missing_files:
        raise FileNotFoundError(
            "Arquivos de entrada obrigatórios não encontrados:\n"
            + "\n".join(f"  - {p}" for p in missing_files)
        )

    run_timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    texts, file_metadata = {}, []
    for name in FILES:
        p = BASE / name
        data = p.read_bytes()
        texts[name] = data.decode("utf-8", errors="replace")
        file_metadata.append({
            "arquivo": name,
            "tamanho_bytes": len(data),
            "mtime_utc": datetime.fromtimestamp(p.stat().st_mtime, tz=timezone.utc).isoformat(timespec="seconds"),
            "sha256": hashlib.sha256(data).hexdigest(),
        })

    governance = texts.get("Regras Ontológicas do Handebol.md", "")
    canonical_predicates = {p.strip() for p in re.findall(r"A Ontologia permite_predicado ([^\.\n]+)\.", governance)}

    vocab_text = texts.get("Vocabulário e Taxonomia.md", "") + "\n" + governance
    vocab_terms = extract_vocab_terms(vocab_text)

    statement_rows, ids = [], []
    for fname, text in texts.items():
        for i, line in enumerate(text.splitlines(), start=1):
            m = STATEMENT_ID_RE.search(line)
            if m:
                sid, sentence = m.group(1), m.group(2).strip()
                subj, pred, obj = parse_spo(sentence, canonical_predicates)
                statement_rows.append({"statement_id": sid, "arquivo": fname, "linha": i, "sentenca": sentence, "sujeito": subj, "predicado": pred, "objeto": obj, "predicado_canonico": pred in canonical_predicates})
                ids.append(sid)

    statement_df = pd.DataFrame(statement_rows)
    statement_df.to_csv(OUT/"01_statement_registry.csv", index=False, encoding="utf-8-sig")

    dups = [{"statement_id": sid, "ocorrencias": c, "locais": json.dumps(statement_df[statement_df.statement_id == sid][["arquivo","linha","sentenca"]].to_dict("records"), ensure_ascii=False)} for sid,c in Counter(ids).items() if c > 1]
    pd.DataFrame(dups).to_csv(OUT/"05_duplicate_ids.csv", index=False, encoding="utf-8-sig")

    invalid = []
    for pred, c in Counter(statement_df["predicado"]).items():
        if pred and pred != NO_PREDICATE_MARKER and pred not in canonical_predicates:
            invalid.append({"predicado": pred, "ocorrencias": c})
    pd.DataFrame(invalid).to_csv(OUT/"04_invalid_predicates.csv", index=False, encoding="utf-8-sig")

    sem_predicado = int((statement_df["predicado"] == NO_PREDICATE_MARKER).sum()) if not statement_df.empty else 0

    concept_counter = Counter()
    for _, row in statement_df.iterrows():
        for term in [norm(row["sujeito"]), norm(row["objeto"])]:
            if term and len(term) <= 120 and not re.fullmatch(r"[\d\s,–\-/]+.*", term):
                concept_counter[term] += 1

    concept_df = pd.DataFrame([{"conceito_candidato": t, "ocorrencias": c, "esta_no_vocabulario": t in vocab_terms} for t,c in concept_counter.most_common()])
    concept_df.to_csv(OUT/"02_concept_candidates.csv", index=False, encoding="utf-8-sig")

    required = ["Especialista","Papel_Tático","Papel_Regulamentar","Função_Situacional","Posição_Espacial","Valor_Do_Gol","Fundamento_Da_Pontuação","Inferência_Proibida","Teste_De_Competência"]
    missing = [{"conceito": t, "motivo": "usado_em_afirmacoes_mas_ausente_do_vocabulario", "ocorrencias": c} for t,c in concept_counter.most_common() if t not in vocab_terms and c >= 2]
    missing += [{"conceito": t, "motivo": "conceito_obrigatorio_minimo_ausente", "ocorrencias": concept_counter.get(t,0)} for t in required if t not in vocab_terms]
    pd.DataFrame(missing).drop_duplicates().to_csv(OUT/"03_missing_vocabulary_terms.csv", index=False, encoding="utf-8-sig")

    decision_text = texts.get("Decisões Humanas.md", "")
    weak = []
    for i, line in enumerate(decision_text.splitlines(), start=1):
        if re.match(r"^\s*(APP-[A-Z]\s+OK|[A-Z]_OK|OK|I|APROVADO|VALIDADO)\.?\s*$", line, re.I):
            weak.append({"arquivo": "Decisões Humanas.md", "linha": i, "trecho": line.strip(), "problema": "aprovacao_generica_sem_texto_literal"})
    for block_id, block_text in extract_decision_blocks(decision_text):
        if is_decision_block_weak(block_text):
            weak.append({"arquivo": "Decisões Humanas.md", "linha": "", "trecho": block_id, "problema": "decisao_sem_pergunta_e_resposta_literal"})
    for concept in ["Especialista", "Goleiro vs. Especialista", "Gol de Especialista"]:
        if concept.lower() not in decision_text.lower():
            weak.append({"arquivo": "Decisões Humanas.md", "linha": "", "trecho": concept, "problema": "decisao_literal_ausente_para_conceito_central"})
    pd.DataFrame(weak).to_csv(OUT/"06_human_decision_gaps.csv", index=False, encoding="utf-8-sig")

    status_rows = []
    for fname, text in texts.items():
        st = {x.upper() for x in STATUS_RE.findall(text)}
        contradiction = ("VALIDADO" in st and bool(st & {"PENDENTE","NÃO_INICIADA","NAO_INICIADA","EM_CONSTRUÇÃO"})) or ("CONCLUÍDA_E_VALIDADA" in st and bool(st & {"PENDENTE","NÃO_INICIADA","NAO_INICIADA"}))
        status_rows.append({"arquivo": fname, "statuses_detectados": "|".join(sorted(st)), "possui_contradicao_potencial": contradiction})
    pd.DataFrame(status_rows).to_csv(OUT/"08_status_contradictions.csv", index=False, encoding="utf-8-sig")

    rastreabilidade_linhas = "\n".join(
        f"  - {m['arquivo']} (tamanho={m['tamanho_bytes']} bytes, sha256={m['sha256'][:16]}…, mtime_utc={m['mtime_utc']})"
        for m in file_metadata
    )

    report = f"""# 07_blockers_report

- Arquivos analisados: {len(FILES)}
- Afirmações com ID extraídas: {len(statement_df)}
- IDs únicos: {statement_df['statement_id'].nunique() if not statement_df.empty else 0}
- IDs duplicados: {len(dups)}
- Predicados não canônicos: {len(invalid)}
- Afirmações sem predicado detectável (fora da linguagem controlada): {sem_predicado}
- Conceitos candidatos extraídos: {len(concept_df)}
- Conceitos ausentes/obrigatórios ausentes: {len(missing)}
- Gaps de decisão humana: {len(weak)}

## Rastreabilidade desta execução
- Timestamp (UTC): {run_timestamp}
- Versão do script: {SCRIPT_VERSION}
- Arquivos lidos:
{rastreabilidade_linhas}

Veredito: pipeline bloqueado até correção de vocabulário, decisões literais, duplicidades e predicados.
"""
    (OUT/"07_blockers_report.md").write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
