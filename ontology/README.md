---
doc_type: source_primary
derived: false
should_be_derived: false
status: current
governed_by: null
generated_by: null
script_version_documented_against: "2.0.0"
metrics_source_of_truth: results_auditoria_python/07_blockers_report.md
superseded_by: null
last_reviewed: "2026-06-22"
version: "1.0.0"
---

# Ontology Audit Pipeline - Handebol de Areia

## 1. Objetivo

O pipeline de auditoria consiste em um conjunto de verificações determinísticas para garantir a integridade semântica e estrutural da ontologia de Handebol de Areia. O sistema automatiza a validação dos documentos em formato Markdown, assegurando conformidade com as regras de modelagem e identificando bloqueios críticos antes da integração ao corpo canônico.

Este README cobre instalação e execução. A especificação normativa completa (verificações obrigatórias, contrato de dados, critério de aceite) está em `results_auditoria_python/02_AUDITORIA_PYTHON_SPEC.md`. Números de métricas atuais nunca aparecem aqui — ver `results_auditoria_python/07_blockers_report.md`, que é regenerado a cada execução.

## 2. Requisitos de Ambiente

- Python 3.8 ou superior.
- Dependências: `pandas` (externa); `pathlib`, `re`, `json`, `hashlib`, `collections`, `datetime` (biblioteca padrão).

Para instalar a dependência externa:

```bash
pip install pandas
```

## 3. Execução

O script resolve seus próprios paths a partir da localização do arquivo (`Path(__file__)`), **não** do diretório de onde é chamado — pode ser executado de qualquer lugar:

```bash
python auditoria_python_ontologia/audit_ontology_pipeline.py
```

Se qualquer um dos 7 arquivos de entrada esperados não for encontrado em `files/`, o script aborta imediatamente com um erro listando o(s) caminho(s) absoluto(s) tentados — não há execução parcial silenciosa.

Antes de rodar oficialmente, execute os testes sintéticos:

```bash
python auditoria_python_ontologia/test_audit_ontology_pipeline.py
```

## 3.1 Validação RDF/OWL do MVP Turtle

O pipeline acima audita a camada documental em Markdown. A validação do artefato
OWL/Turtle do MVP fica separada em `owl/`.

Para validar o arquivo `owl/scout_beachhandball_mvp.ttl` no WSL:

```bash
bash owl/validate.sh
```

Esse comando executa:

- parse e checagens estruturais do MVP via `owl/validate_mvp_ttl.py`
- validação SHACL via `pyshacl` **somente** se existir um arquivo
  `owl/mvp.shapes.ttl`

A validação Turtle atual verifica, no mínimo:

- presença de uma única declaração `owl:Ontology`
- anotações obrigatórias do escopo (`rdfs:label`, `rdfs:comment`,
  `dcterms:source`, `dcterms:created`, `owl:versionInfo`)
- presença das classes e object properties autorizadas
- ausência das classes bloqueadas de pontuação
- relações mínimas como `Especialista subClassOf Papel_Tatico`,
  `Goleiro subClassOf Papel_Regulamentar` e as disjunções estruturais

## 4. Estrutura de Entrada

Sete arquivos Markdown em `files/`, todos fonte primária (não derivados):

```text
Regras Ontológicas do Handebol.md
Vocabulário e Taxonomia.md
Regras 1–18.md
Apêndices.md
Rastreabilidade.md
Decisões Humanas.md
Operacional.md
```

## 5. Estrutura de Saída

Os resultados são gerados em `results_auditoria_python/`. **Todos os 8 arquivos a seguir são derivados** — regenerados do zero a cada execução do script; nenhum deve ser editado manualmente:

```text
01_statement_registry.csv      registro completo de afirmações parseadas (SPO)
02_concept_candidates.csv      termos extraídos cruzados com o vocabulário
03_missing_vocabulary_terms.csv  lacunas taxonômicas
04_invalid_predicates.csv      predicados fora da whitelist canônica
05_duplicate_ids.csv           IDs de afirmação duplicados
06_human_decision_gaps.csv     decisões humanas frágeis ou sem pergunta/resposta literal
07_blockers_report.md          veredito final + métricas + rastreabilidade da execução
08_status_contradictions.csv   conflitos de status lógico
```

`01_statement_registry.csv` e `04_invalid_predicates.csv` podem conter o
valor sentinela `(predicado_não_detectado)` na coluna `predicado`: significa
que a frase não usa nenhum predicado em linguagem controlada (nem canônico,
nem com underscore) — é contado separadamente como "Afirmações sem
predicado detectável" em `07_blockers_report.md`, e não entra na contagem
de "Predicados não canônicos".

`07_blockers_report.md` também traz uma seção "Rastreabilidade desta
execução" com timestamp, versão do script (`SCRIPT_VERSION`) e
hash/tamanho/mtime de cada um dos 7 arquivos de entrada lidos.

## 6. Metodologia de Auditoria

O script combina cinco camadas determinísticas, todas baseadas em regex (sem NLP, sem `rdflib`/`owlready2` — ver `results_auditoria_python/02_AUDITORIA_PYTHON_SPEC.md` para o porquê dessa escolha):

1. **Parseamento SPO**: extrai Sujeito-Predicado-Objeto de cada linha marcada com `[BH-...]`.
2. **Predicados canônicos**: compara contra a whitelist declarada em `Regras Ontológicas do Handebol.md`.
3. **Vocabulário controlado**: verifica se sujeitos/objetos extraídos constam no vocabulário (`é_um`, `é_subclasse_de`, `é_disjunto_de`, `possui_status TERMO_CANÔNICO`).
4. **Decisões humanas por bloco**: agrupa blocos de decisão em `Decisões Humanas.md` e verifica presença de pergunta + resposta literal + decisões extraídas — não apenas linhas soltas tipo "OK".
5. **Contradição de status**: detecta termos marcados simultaneamente como, por exemplo, `VALIDADO` e `PENDENTE`.

## 7. Critério de Aceite (Veredito)

Modelo Fail-Fast: se houver registros em `03_missing_vocabulary_terms.csv` ou `04_invalid_predicates.csv`, a ontologia é marcada como BLOQUEADA. Não avançar para novas etapas de formalização enquanto esses arquivos não estiverem vazios ou corrigidos. Detalhes completos da especificação: `results_auditoria_python/02_AUDITORIA_PYTHON_SPEC.md`.
