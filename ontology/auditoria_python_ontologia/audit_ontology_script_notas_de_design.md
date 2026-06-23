---
doc_type: design_notes
derived: false
should_be_derived: false
status: superseded
governed_by: null
generated_by: null
script_version_documented_against: "1.x (pré-fix)"
metrics_source_of_truth: results_auditoria_python/07_blockers_report.md
superseded_by: auditoria_python_ontologia/audit_ontology_pipeline.py
last_reviewed: "2026-06-22"
---

> **AVISO: conteúdo histórico, não reflete o estado atual.** O código e as
> métricas abaixo (1.519 afirmações, 100 IDs duplicados, 394 predicados fora
> da lista) são de uma iteração anterior a 19/06 e já estavam desatualizados
> antes da correção de v2.0.0. Não usar como referência de comportamento
> atual — ver `audit_ontology_pipeline.py` e `results_auditoria_python/07_blockers_report.md`.

#audit_ontology_pipeline

Ojetivo:
> **Rodar um script Python para extrair conceitos com muito menos ruído de interpretação da IA. Não dá para garantir “sem ruído” se a entrada for prosa livre ou se os arquivos já estiverem inconsistentes.**
Nesse caso, Python é exatamente o caminho certo.

Arquivos atuais:
* existem **1.519 afirmações extraíveis**;
* **1.419 IDs únicos**;
* **100 IDs duplicados**, incluindo duplicação em `BH-IHF-2026-R08-001`, `R08-002`, etc.;
* há **394 predicados usados fora da lista canônica permitida**;
* `Especialista` aparece apenas no arquivo de governança, mas não aparece em `Vocabulário`, `Regras`, `Rastreabilidade`, `Decisões Humanas` ou `Apêndices`.

Isso confirma que o problema não é falta de explicação técnica. O pipeline gerou texto com aparência ontológica, mas sem contrato formal suficiente.

O próprio arquivo de governança exige linguagem controlada, um termo canônico por conceito e predicados permitidos.  Porém os arquivos formalizados usam predicados fora da lista, como `possui_comprimento`, `possui_largura`, `possui_material`, `possui_nivelamento`. 

## O que o script consegue fazer bem

Um script Python consegue extrair com boa confiabilidade:

```text
statement_id
sujeito
predicado
objeto
status
fonte
página
conceitos candidatos
termos canônicos
predicados não permitidos
IDs duplicados
conceitos sem definição
conceitos mencionados mas ausentes do vocabulário
decisões humanas frágeis
```

Ele também consegue bloquear automaticamente coisas como:

```text
ID duplicado
predicado fora da lista canônica
conceito usado sem estar no vocabulário
status VALIDADO sem decisão humana literal
afirmação sem fonte
conceito subjetivo tratado como resolvido
```

Isso já reduziria muito o ruído.

## O que o script não consegue fazer sozinho

Ele não consegue decidir, por conta própria, que:

```text
Especialista sempre marca gol de 2 pontos.
Especialista atuando no gol continua especialista.
Goleiro que cobra falta continua goleiro.
Conduta X é mais grave que conduta Y.
```

Essas são decisões semânticas do domínio. O script só deve verificar se elas foram registradas, versionadas e preservadas.

## Fluxo correto com Python

O fluxo deve ser este:

```text
1. Manual ou PDF
→ 2. Extração textual bruta
→ 3. Parser Python
→ 4. Lista de conceitos candidatos
→ 5. Validação humana
→ 6. Vocabulário canônico
→ 7. Geração de afirmações ontológicas
→ 8. Testes automáticos
→ 9. Ontologia
```

A IA **MUST NOT** transformar diretamente:

```text
manual → ontologia
```

Ela **SHOULD**, no máximo, ajudar a revisar saídas do script.

## O ponto central

O Python **MUST** ser o **filtro de verdade estrutural**.

Exemplo:

```python
if conceito not in vocabulario:
    status = "BLOQUEADO_CONCEITO_NAO_CANONICO"
```

```python
if predicado not in predicados_permitidos:
    status = "BLOQUEADO_PREDICADO_NAO_CANONICO"
```

```python
if status == "VALIDADO" and not decisao_humana_literal:
    status = "INVALIDO_VALIDACAO_SEM_DECISAO_LITERAL"
```

Isso impede que o AI “ache que entendeu” e siga adiante.

## Melhor decisão agora

Rodar Python **não para criar a ontologia final**, mas para gerar três arquivos limpos:

```text
01_conceitos_candidatos.csv
02_predicados_invalidos.csv
03_bloqueios_de_validacao.csv
```

Depois disso, humano valida os conceitos centrais, começando por:

```text
Especialista
Goleiro
Papel Tático
Função Situacional
Posição Espacial
Valor do Gol
Fundamento da Pontuação
```

O script não elimina 100% do ruído sem um manual estruturado, mas elimina o pior ruído: duplicidade, status falso, conceito fantasma, predicado inventado e decisão humana não rastreada. Isso é muito mais confiável do que pedir para a IA “entender melhor”.


2. Código Python 

```python
# Audit script generated for deterministic ontology pipeline validation.
# Place this file in the same folder as the seven .md files and run:
# python audit_ontology_pipeline.py
# Outputs are written to ./auditoria_python_ontologia

from pathlib import Path
import re, json
from collections import Counter, defaultdict
import pandas as pd

BASE = Path(".")
OUT = BASE / "auditoria_python_ontologia"
OUT.mkdir(exist_ok=True)

files = [
    "Regras Ontológicas do Handebol.md",
    "Vocabulário e Taxonomia.md",
    "Regras 1–18.md",
    "Apêndices.md",
    "Rastreabilidade.md",
    "Decisões Humanas.md",
    "Operacional.md",
]

texts = {name: (BASE/name).read_text(encoding="utf-8", errors="replace") if (BASE/name).exists() else "" for name in files}

statement_id_re = re.compile(r"\[(BH-[A-Z0-9\-]+-\d{3})\]\s*(.+)")
status_re = re.compile(r"\b(VALIDADO|CONCLUÍDA_E_VALIDADA|RASCUNHO|NÃO_INICIADA|NAO_INICIADA|PENDENTE|EM_CONSTRUÇÃO|APROVADA|BLOQUEADO|AGUARDANDO_AVALIAÇÃO_HUMANA|CATEGORIA_CONTROLADA_COM_AVALIAÇÃO_HUMANA)\b", re.I)

governance = texts.get("Regras Ontológicas do Handebol.md", "")
canonical_predicates = {p.strip() for p in re.findall(r"A Ontologia permite_predicado ([^\.\n]+)\.", governance)}

vocab_text = texts.get("Vocabulário e Taxonomia.md", "") + "\n" + governance
vocab_terms = set()
for line in vocab_text.splitlines():
    s = line.strip()
    for pat in [r"(.+?) possui_status TERMO_CANÔNICO\.", r"(.+?) é_um (.+?)\.", r"(.+?) é_disjunto_de (.+?)\."]:
        m = re.match(pat, s)
        if m:
            vocab_terms.update(x.strip() for x in m.groups())

def parse_spo(sentence):
    s = sentence.strip().rstrip(".")
    preds = set(canonical_predicates)
    preds.update(re.findall(r"\b[^\s,;]+_[^\s,;]+(?:_[^\s,;]+)*\b", s))
    preds.update(["é_um", "é_disjunto_de", "é_instância_de", "possui", "possui_status"])
    for pred in sorted(preds, key=len, reverse=True):
        mm = re.search(r"\s" + re.escape(pred) + r"\s", s)
        if mm:
            return s[:mm.start()].strip(), pred, s[mm.end():].strip()
    parts = s.split()
    return (parts[0], parts[1], " ".join(parts[2:])) if len(parts) >= 3 else (s, "", "")

def norm(term):
    term = re.sub(r"\s*\[[^\]]+\]\s*$", "", term).strip(" .,:;()")
    term = re.sub(r"^(A|O|Uma|Um|Os|As|Cada|Se|No|Na|Quando)\s+", "", term)
    return term

statement_rows, ids = [], []
for fname, text in texts.items():
    for i, line in enumerate(text.splitlines(), start=1):
        m = statement_id_re.search(line)
        if m:
            sid, sentence = m.group(1), m.group(2).strip()
            subj, pred, obj = parse_spo(sentence)
            statement_rows.append({"statement_id": sid, "arquivo": fname, "linha": i, "sentenca": sentence, "sujeito": subj, "predicado": pred, "objeto": obj, "predicado_canonico": pred in canonical_predicates})
            ids.append(sid)

statement_df = pd.DataFrame(statement_rows)
statement_df.to_csv(OUT/"01_statement_registry.csv", index=False, encoding="utf-8-sig")

dups = [{"statement_id": sid, "ocorrencias": c, "locais": json.dumps(statement_df[statement_df.statement_id == sid][["arquivo","linha","sentenca"]].to_dict("records"), ensure_ascii=False)} for sid,c in Counter(ids).items() if c > 1]
pd.DataFrame(dups).to_csv(OUT/"05_duplicate_ids.csv", index=False, encoding="utf-8-sig")
invalid = []
for pred, c in Counter(statement_df["predicado"]).items():
    if pred and pred not in canonical_predicates:
        invalid.append({"predicado": pred, "ocorrencias": c})
pd.DataFrame(invalid).to_csv(OUT/"04_invalid_predicates.csv", index=False, encoding="utf-8-sig")

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
for concept in ["Especialista", "Goleiro vs. Especialista", "Gol de Especialista"]:
    if concept.lower() not in decision_text.lower():
        weak.append({"arquivo": "Decisões Humanas.md", "linha": "", "trecho": concept, "problema": "decisao_literal_ausente_para_conceito_central"})
pd.DataFrame(weak).to_csv(OUT/"06_human_decision_gaps.csv", index=False, encoding="utf-8-sig")
status_rows = []
for fname, text in texts.items():
    st = {x.upper() for x in status_re.findall(text)}
    contradiction = ("VALIDADO" in st and bool(st & {"PENDENTE","NÃO_INICIADA","NAO_INICIADA","EM_CONSTRUÇÃO"})) or ("CONCLUÍDA_E_VALIDADA" in st and bool(st & {"PENDENTE","NÃO_INICIADA","NAO_INICIADA"}))
    status_rows.append({"arquivo": fname, "statuses_detectados": "|".join(sorted(st)), "possui_contradicao_potencial": contradiction})
pd.DataFrame(status_rows).to_csv(OUT/"08_status_contradictions.csv", index=False, encoding="utf-8-sig")

report = f"""# 07_blockers_report

- Arquivos analisados: {len(files)}
- Afirmações com ID extraídas: {len(statement_df)}
- IDs únicos: {statement_df['statement_id'].nunique() if not statement_df.empty else 0}
- IDs duplicados: {len(dups)}
- Predicados não canônicos: {len(invalid)}
- Conceitos candidatos extraídos: {len(concept_df)}
- Conceitos ausentes/obrigatórios ausentes: {len(missing)}
- Gaps de decisão humana: {len(weak)}

Veredito: pipeline bloqueado até correção de vocabulário, decisões literais, duplicidades e predicados.
"""
(OUT/"07_blockers_report.md").write_text(report, encoding="utf-8")
print(report)
```


