---
doc_type: spec
derived: false
should_be_derived: false
status: current
governed_by: null
generated_by: null
script_version_documented_against: "2.0.0"
metrics_source_of_truth: results_auditoria_python/07_blockers_report.md
superseded_by: null
last_reviewed: "2026-06-22"
---

# 02_AUDITORIA_PYTHON_SPEC

## Finalidade

Este documento especifica a auditoria Python que deve ser executada antes de qualquer nova geração ontológica.

O objetivo do script não é entender handebol de areia. O objetivo do script é detectar ruído estrutural, impedir validação falsa e gerar relatórios objetivos para revisão humana.

## Entradas

O script deve receber os arquivos herdados do pipeline anterior:

1. Regras Ontológicas do Handebol.md
2. Vocabulário e Taxonomia.md
3. Regras 1–18.md
4. Apêndices.md
5. Rastreabilidade.md
6. Decisões Humanas.md
7. Operacional.md

## Saídas obrigatórias

O script deve gerar:

```text
01_statement_registry.csv
02_concept_candidates.csv
03_missing_vocabulary_terms.csv
04_invalid_predicates.csv
05_duplicate_ids.csv
06_human_decision_gaps.csv
07_blockers_report.md
08_status_contradictions.csv
```

Todos os arquivos 01–08 desta lista são **derivados**: regenerados do zero a
cada execução de `audit_ontology_pipeline.py`. Nenhum deve ser editado
manualmente — uma edição manual será sobrescrita na próxima execução e não
deixa rastro.

### Contrato de dados: ausência de predicado

O campo `predicado` em `01_statement_registry.csv` e `04_invalid_predicates.csv`
pode conter o valor sentinela `(predicado_não_detectado)`. Isso significa que
a frase não contém nenhum candidato a predicado em linguagem controlada (nem
canônico, nem um termo com underscore) — é uma categoria distinta de
"predicado não canônico" e é contada separadamente no relatório como
"Afirmações sem predicado detectável". Qualquer verificação futura que
consuma esses CSVs deve tratar esse valor como "ausência estrutural", não
como "predicado inválido".

## Verificações obrigatórias

### 1. Registro de afirmações

Extrair toda linha com padrão de ID ontológico, por exemplo:

```text
[BH-IHF-2026-R01-001]
```

Campos mínimos:

```text
statement_id
arquivo
linha
sujeito
predicado
objeto
status
```

### 2. IDs duplicados

Detectar todo ID que aparece mais de uma vez.

Bloqueio:

```text
Se statement_id aparece mais de uma vez, status = BLOQUEADO_ID_DUPLICADO.
```

### 3. Predicados não canônicos

Comparar todos os predicados usados contra a lista canônica definida na governança.

Bloqueio:

```text
Se predicado não está na lista canônica, status = BLOQUEADO_PREDICADO_NAO_CANONICO.
```

### 4. Conceitos ausentes do vocabulário

Extrair candidatos a conceito a partir de sujeitos, objetos e termos compostos.

Comparar com o vocabulário canônico.

Bloqueio:

```text
Se conceito é usado mas não está no vocabulário, status = BLOQUEADO_CONCEITO_NAO_CANONICO.
```

### 5. Decisões humanas frágeis

Detectar registros que contenham apenas:

```text
OK
B_OK
C_OK
D_OK
E_OK
F_OK
APROVADO
VALIDADO
```

Bloqueio:

```text
Se decisão humana não contém pergunta, resposta literal e decisões extraídas, status = BLOQUEADO_DECISAO_HUMANA_INSUFICIENTE.
```

### 6. Status contraditórios

Detectar blocos que possuem simultaneamente:

```text
VALIDADO
PENDENTE
NÃO_INICIADO
RASCUNHO
CONCLUÍDA_E_VALIDADA
```

Bloqueio:

```text
Se bloco possui status conflitante, status = BLOQUEADO_STATUS_CONTRADITORIO.
```

### 7. Conceitos centrais obrigatórios

Verificar se os seguintes conceitos existem no vocabulário:

```text
Especialista
Papel_Tático
Papel_Regulamentar
Função_Situacional
Posição_Espacial
Valor_Do_Gol
Fundamento_Da_Pontuação
Inferência_Proibida
Teste_De_Competência
```

Bloqueio:

```text
Se qualquer conceito obrigatório está ausente, status = BLOQUEADO_VOCABULARIO_MINIMO_INCOMPLETO.
```

## Critério de sucesso da auditoria

A auditoria é considerada concluída quando gerar relatórios suficientes para responder:

1. Quantas afirmações existem?
2. Quantos IDs únicos existem?
3. Quais IDs estão duplicados?
4. Quais predicados foram usados?
5. Quais predicados não são canônicos?
6. Quais conceitos aparecem mas não estão no vocabulário?
7. Quais decisões humanas não preservam texto literal?
8. Quais blocos possuem status contraditório?
9. Quais bloqueios impedem a continuação?

## Próximo passo após auditoria

Depois da auditoria Python, o projeto deve reconstruir apenas um conceito:

```text
Especialista
```

A reconstrução deve usar:

1. decisão humana literal DH-ESP-001;
2. vocabulário canônico mínimo;
3. ficha conceitual;
4. teste de competência;
5. validação humana.

Somente após esse conceito passar no teste, a ontologia pode avançar para outros conceitos.

## Apêndice — Convenções de Metadados de Documentação

Todo arquivo `.md` nos diretórios `files\`, `auditoria_python_ontologia\`,
`results_auditoria_python\`, além de `README.md` e `CHANGELOG`, deve trazer
um bloco YAML no topo, antes do primeiro título, com este esquema:

```yaml
---
doc_type: source_primary | derived_report | spec | design_notes | governance_log
derived: true|false
should_be_derived: true|false
status: current|stale|superseded
governed_by: <path relativo ou null>
generated_by: <comando/script exato, ou null>
script_version_documented_against: <ex. "2.0.0", ou null>
metrics_source_of_truth: <path para 07_blockers_report.md, se o doc cita métricas>
superseded_by: <path relativo ou null>
last_reviewed: <YYYY-MM-DD>
---
```

Regras de leitura para qualquer agente (humano ou IA) que abrir um destes documentos:

- `derived: true` significa que o conteúdo é gerado por execução de código —
  nunca editar manualmente; editar o gerador (`generated_by`) e reexecutar.
- `should_be_derived: true` sinaliza uma seção mantida à mão que é candidata
  a ser automatizada porque já causou ou pode causar drift entre o documento
  e o estado real do pipeline (ex: números de métricas digitados de memória).
  Tratar qualquer edição manual dessa seção como sinal de risco, não como
  trabalho normal.
- `status: superseded` significa que o conteúdo é histórico — válido como
  registro do passado, inválido como descrição do presente. Seguir
  `superseded_by` para encontrar a versão atual.
- `metrics_source_of_truth` aponta para o único lugar de onde números de
  métricas devem ser lidos/citados. Nenhum outro documento deve reproduzir
  esses números sem essa referência ao lado.

Os 8 arquivos `01_statement_registry.csv` a `08_status_contradictions.csv`
em `results_auditoria_python\` não recebem este bloco (corromperia o
parsing de CSV) — são derivados por convenção: todo o conteúdo dessa pasta
com prefixo numérico `01`–`08` é gerado por `audit_ontology_pipeline.py` e
nunca deve ser editado manualmente.

