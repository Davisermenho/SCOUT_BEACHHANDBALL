---
doc_id: esquema-metadados-documentais
doc_type: contract
status: proposed
phase_scope:
  - cross_phase
authority_level: proposed
owned_by: repo_governance_bootstrap
canonical_path: /docs/00_governanca/ESQUEMA_METADADOS_DOCUMENTAIS.md
supersedes: []
superseded_by: null
must_read_before_implementation: false
implementation_ready: false
last_reviewed: "2026-06-24"
---

# ESQUEMA_METADADOS_DOCUMENTAIS

## 1. Finalidade

Este arquivo e o SSOT bootstrap dos metadados documentais do repositorio.

Ele existe para:

- transformar o plano de governanca em schema verificavel;
- refinar a classificacao bootstrap de `MAPA_DOCUMENTAL.md`;
- impedir que documentos ativos, historicos e depreciados parecam equivalentes;
- preparar validacao mecanica futura por script e CI.

## 2. Regra de uso

Este schema:

- vale para os documentos governados do repo no escopo definido na secao 11;
- define o frontmatter canonico minimo obrigatorio;
- prevalece sobre classificacoes bootstrap ambiguas do `MAPA_DOCUMENTAL.md`;
- deve ser lido junto com `PLANO_CONTRATO_ORGANIZACAO_DOCUMENTAL.md`.

Relacao com o mapa:

- `MAPA_DOCUMENTAL.md` e derivado do frontmatter;
- divergencia entre mapa e frontmatter e erro;
- quando houver conflito, o schema e o frontmatter canonico vencem, e o mapa deve ser atualizado no mesmo changeset.

## 3. Frontmatter canonico minimo

Todo documento governado por este schema deve abrir com:

```yaml
---
doc_id: identificador-unico
doc_type: contract|approval|review|adr|inventory|plan|archive|handoff
status: draft|proposed|approved|current|deprecated|archived
phase_scope:
  - phase_0|phase_1|phase_2|phase_3|cross_phase
authority_level: ssot|canonical|operational|supporting|historical|proposed
owned_by: nome-do-contrato-ou-governanca
canonical_path: /docs/caminho/do/arquivo.md
supersedes:
  - /docs/caminho/arquivo_antigo.md
superseded_by: null
must_read_before_implementation: true|false
implementation_ready: true|false
last_reviewed: "YYYY-MM-DD"
---
```

## 4. Definicao dos campos

| campo | tipo | obrigatorio | regra |
| --- | --- | --- | --- |
| `doc_id` | string | sim | identificador estavel, unico no conjunto governado |
| `doc_type` | enum | sim | categoria documental conforme secao 5 |
| `status` | enum | sim | estado documental conforme secao 6 |
| `phase_scope` | lista enum | sim | fase ou conjunto de fases conforme secao 7 |
| `authority_level` | enum | sim | nivel de autoridade conforme secao 8 |
| `owned_by` | string | sim | contrato, governanca ou mantenedor logico do documento |
| `canonical_path` | string | sim | caminho absoluto no repo iniciado por `/docs/` para o conjunto governado |
| `supersedes` | lista string | sim | lista de caminhos canonicos absorvidos; pode ser vazia |
| `superseded_by` | string ou `null` | sim | sucessor canonico, quando existir |
| `must_read_before_implementation` | boolean | sim | indica leitura obrigatoria antes de implementar produto |
| `implementation_ready` | boolean | sim | so pode ser `true` para contratos ativos que liberam implementacao |
| `last_reviewed` | string data | sim | formato `YYYY-MM-DD` |

## 5. Dominios validos

### 5.1 `doc_type`

Valores permitidos:

- `contract`
- `approval`
- `review`
- `adr`
- `inventory`
- `plan`
- `archive`
- `handoff`

Definicoes operacionais:

- `contract`: define regra ou escopo normativo.
- `approval`: registra gate ou decisao humana.
- `review`: analise, auditoria, matriz ou relatorio de suporte.
- `adr`: registro de decisao arquitetural.
- `inventory`: indice derivado do estado documental.
- `plan`: roteiro bootstrap ou backlog de transicao.
- `archive`: historico sem papel operacional ativo.
- `handoff`: ponto autorizado de continuidade operacional.

### 5.2 `status`

Valores permitidos:

- `draft`
- `proposed`
- `approved`
- `current`
- `deprecated`
- `archived`

### 5.3 `phase_scope`

Valores permitidos por item da lista:

- `phase_0`
- `phase_1`
- `phase_2`
- `phase_3`
- `cross_phase`

### 5.4 `authority_level`

Valores permitidos:

- `ssot`
- `canonical`
- `operational`
- `supporting`
- `historical`
- `proposed`

## 6. Maquina de estados de `status`

Estados validos:

- `draft`: rascunho em elaboracao.
- `proposed`: proposta pronta para revisao humana.
- `approved`: aprovado, mas ainda nao ativado como referencia vigente.
- `current`: documento ativo e vigente.
- `deprecated`: substituido, preservado por rastreabilidade.
- `archived`: historico sem uso operacional.

Transicoes validas:

1. `draft -> proposed`
2. `proposed -> approved`
3. `proposed -> archived`
4. `approved -> current`
5. `approved -> archived`
6. `current -> deprecated`
7. `current -> archived`
8. `deprecated -> archived`

Transicoes proibidas:

- `draft -> current`
- `deprecated -> current`
- marcar documento como `current` sem reclassificar predecessor quando houver substituicao
- marcar documento como `deprecated` antes de o sucessor existir no mesmo changeset

Autoridade de transicao:

- `draft -> proposed`: agente executor ou mantenedor humano
- `proposed -> approved`: mantenedor humano
- `approved -> current`: mantenedor humano
- `current -> deprecated`: mantenedor humano no mesmo changeset que cria ou ativa o sucessor
- `deprecated -> archived`: mantenedor humano ou agente executor com rastreabilidade preservada

## 7. Regras de `phase_scope`

Regras gerais:

- `phase_scope` e sempre lista.
- a lista nao pode estar vazia.
- `cross_phase` nao pode coexistir com fases explicitas na mesma lista.
- a lista nao pode conter valores repetidos.

Regras por tipo:

- documentos `contract` ou `approval` com `status: current` e `authority_level: ssot|canonical|operational` devem declarar exatamente um unico escopo: uma fase explicita ou `cross_phase`;
- documentos `review`, `inventory`, `plan` e `handoff` podem declarar multiplas fases explicitas;
- documentos `archive` historicos podem declarar uma fase explicita ou `cross_phase`, conforme o alcance do historico.

Regra de conflito:

- para validacao de conflito, um documento ativo com varias fases explicitas conta simultaneamente em cada fase listada.

## 8. Regras de `authority_level`

Regras por `status`:

- documentos em `draft` ou `proposed` devem usar `authority_level: proposed`;
- documentos em `approved` permanecem com `authority_level: proposed`, exceto `approval`, que pode usar `supporting` quando aprovado mas ainda nao vigente;
- apenas documentos em `status: current` podem usar `ssot`, `canonical`, `operational` ou `supporting`;
- documentos em `deprecated` ou `archived` devem usar `authority_level: historical`.

Regras por `doc_type` em `status: current`:

- `contract`: `ssot`, `canonical` ou `operational`
- `approval`: `supporting`
- `review`: `supporting`
- `adr`: `supporting`
- `inventory`: `supporting`
- `plan`: `supporting`
- `handoff`: `supporting`
- `archive`: proibido; `archive` nao pode usar `status: current`

## 9. Regras cruzadas obrigatorias

### 9.1 `must_read_before_implementation`

Deve ser `true` quando:

- o documento for `contract`, `approval` ou `handoff`;
- o documento governar implementacao de produto;
- o documento estiver ativo no fluxo operacional que libera execucao.

Pode ser `false` quando:

- o documento for bootstrap, historico, indice, revisao ou plano nao vigente;
- o documento ainda estiver em `draft` ou `proposed` e nao governar implementacao.

### 9.2 `implementation_ready`

Pode ser `true` somente quando todos os itens abaixo forem verdadeiros:

- `doc_type = contract`
- `status = current`
- `authority_level = operational` ou `canonical`
- `must_read_before_implementation = true`
- o documento realmente libera implementacao da fase ou do escopo correspondente

Deve ser `false` em todos os outros casos.

### 9.3 `canonical_path`

Regras:

- no conjunto governado principal, deve coincidir exatamente com o caminho real do arquivo;
- deve comecar com `/docs/`;
- nao pode apontar para arquivo inexistente no commit final.

Excecao de adaptacao controlada:

- artefatos do subsistema `ontology/` ainda fora da convergencia principal podem permanecer temporariamente fora de `/docs/` desde que essa excecao esteja declarada no `MAPA_DOCUMENTAL.md` e no contrato de governanca definitivo.

### 9.4 `supersedes` e `superseded_by`

Regras:

- `supersedes` pode ser lista vazia;
- `superseded_by` pode ser `null` apenas quando nao houver sucessor;
- se `status = deprecated`, `superseded_by` deve apontar para sucessor existente;
- sucessor e predecessor devem ser atualizados no mesmo changeset;
- `superseded_by` nunca pode apontar para caminho inexistente no commit final.

## 10. Regras por tipo de documento

### 10.1 `contract`

- pode existir em `draft`, `proposed`, `approved`, `current`, `deprecated` ou `archived`
- em `current`, deve usar `ssot`, `canonical` ou `operational`
- quando liberar implementacao, deve usar `must_read_before_implementation: true`

### 10.2 `approval`

- registra gate, freeze ou decisao humana
- em `current`, usa `supporting`
- quando governar implementacao, deve usar `must_read_before_implementation: true`

### 10.3 `review`

- documenta analise, auditoria, matriz ou relatorio
- em `current`, usa `supporting`
- nao libera implementacao por si so

### 10.4 `adr`

- registra decisao arquitetural
- em `current`, usa `supporting`
- pode ser leitura obrigatoria apenas quando explicitamente referenciado por contrato ativo

### 10.5 `inventory`

- documenta indice derivado do estado real
- em `current`, usa `supporting`
- nao e fonte primaria de verdade

### 10.6 `plan`

- documenta roteiro bootstrap ou backlog de transicao
- em `current`, usa `supporting`
- nao pode liberar implementacao de produto

### 10.7 `archive`

- documenta historico preservado
- nao pode usar `status: current`
- deve usar `authority_level: historical`

### 10.8 `handoff`

- registra ponto autorizado de continuidade
- em `current`, usa `supporting`
- se governar implementacao, deve usar `must_read_before_implementation: true`

## 11. Escopo inicial de aplicacao

Entram obrigatoriamente neste schema ja nesta etapa:

- `docs/00_governanca/*.md`
- documentos normativos e de fase mapeados para migracao principal em `MAPA_DOCUMENTAL.md`
- ADRs do repo quando forem migrados para `docs/06_adrs/`
- revisoes e historicos migrados para `docs/07_*` e `docs/08_*`

Ficam em adaptacao controlada nesta etapa:

- subsistema `ontology/`, que hoje possui metadados locais proprios;
- derivados de fonte externa em `docs/fontes/` e `fontes/`, ate decisao final de convergencia e taxonomia;
- arquivos legados ainda fora de `docs/` que ja estejam explicitamente classificados no `MAPA_DOCUMENTAL.md`.

Regra de adaptacao controlada:

- um arquivo fora do schema principal so pode permanecer temporariamente nesse estado se estiver explicitamente inventariado e classificado no `MAPA_DOCUMENTAL.md`.

## 12. Resolucao das pendencias bootstrap do mapa

Ratificacoes definidas por este schema:

- documentos de fonte externa permanecem classificados como `review` quando forem derivados analiticos ativos e como `archive` quando forem duplicata, legado ou historico;
- o subsistema `ontology/` permanece sob adaptacao controlada, sem bloquear a Etapa 2 do schema principal;
- `HANDOFF.md` do subsistema `ontology/` continua classificado como `handoff`;
- templates do subsistema `ontology/` continuam classificados como `archive` ate schema especifico posterior.

## 13. Exemplos validos

### 13.1 Contrato ativo de fase

```yaml
---
doc_id: ordem-execucao-fase-1
doc_type: contract
status: current
phase_scope:
  - phase_1
authority_level: operational
owned_by: fase_1
canonical_path: /docs/05_fases/fase_1/ORDEM_EXECUCAO_FASE_1.md
supersedes: []
superseded_by: null
must_read_before_implementation: true
implementation_ready: true
last_reviewed: "2026-06-24"
---
```

### 13.2 Aprovacao vigente

```yaml
---
doc_id: aprovacao-fase-0
doc_type: approval
status: current
phase_scope:
  - phase_0
authority_level: supporting
owned_by: fase_0
canonical_path: /docs/05_fases/fase_0/APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md
supersedes: []
superseded_by: null
must_read_before_implementation: true
implementation_ready: false
last_reviewed: "2026-06-24"
---
```

### 13.3 Revisao ativa de suporte

```yaml
---
doc_id: revisao-mvp-especificacao
doc_type: review
status: current
phase_scope:
  - cross_phase
authority_level: supporting
owned_by: repo_governance
canonical_path: /docs/07_revisoes_e_auditorias/REVISAO_MVP_X_ESPECIFICACAO_IMPLEMENTACAO.md
supersedes: []
superseded_by: null
must_read_before_implementation: false
implementation_ready: false
last_reviewed: "2026-06-24"
---
```

### 13.4 Historico arquivado

```yaml
---
doc_id: modelagem-banco-legada
doc_type: archive
status: archived
phase_scope:
  - phase_1
authority_level: historical
owned_by: repo_history
canonical_path: /docs/08_historico_deprecado/MODELAGEM_DO_BANCO_DE_DADOS.md
supersedes: []
superseded_by: null
must_read_before_implementation: false
implementation_ready: false
last_reviewed: "2026-06-24"
---
```

### 13.5 Plano bootstrap

```yaml
---
doc_id: plano-contrato-organizacao-documental
doc_type: plan
status: proposed
phase_scope:
  - cross_phase
authority_level: proposed
owned_by: repo_governance_bootstrap
canonical_path: /docs/00_governanca/PLANO_CONTRATO_ORGANIZACAO_DOCUMENTAL.md
supersedes: []
superseded_by: null
must_read_before_implementation: false
implementation_ready: false
last_reviewed: "2026-06-24"
---
```

## 14. Exemplos invalidos

### 14.1 Contrato ativo sem leitura obrigatoria

Invalido porque contrato operacional ativo que libera implementacao nao pode usar `must_read_before_implementation: false`.

```yaml
doc_type: contract
status: current
authority_level: operational
must_read_before_implementation: false
implementation_ready: true
```

### 14.2 Arquivo historico parecendo ativo

Invalido porque `archive` nao pode usar `status: current`.

```yaml
doc_type: archive
status: current
authority_level: supporting
```

### 14.3 Documento depreciado sem sucessor

Invalido porque `deprecated` exige `superseded_by` nao nulo e existente.

```yaml
doc_type: review
status: deprecated
superseded_by: null
```

### 14.4 Escopo misturado com `cross_phase`

Invalido porque `cross_phase` nao pode coexistir com fases explicitas.

```yaml
phase_scope:
  - cross_phase
  - phase_1
```

### 14.5 Documento proposto com autoridade ativa

Invalido porque `proposed` deve usar `authority_level: proposed`.

```yaml
status: proposed
authority_level: canonical
```

## 15. Preparacao para validacao mecanica

Este schema foi escrito para permitir validacao futura sem inferencia livre.

O futuro validador deve conseguir verificar, no minimo:

- presenca de todos os campos obrigatorios;
- pertencimento aos enums validos;
- coerencia entre `status` e `authority_level`;
- coerencia entre `doc_type`, `must_read_before_implementation` e `implementation_ready`;
- coerencia de `phase_scope`;
- existencia real de `canonical_path` e `superseded_by`, quando aplicavel;
- divergencia entre `MAPA_DOCUMENTAL.md` e o frontmatter real.

## 16. Criterios de aceite da Etapa 2

Este arquivo so deve ser considerado aceito quando:

1. existir um schema unico de frontmatter para os documentos governados;
2. todos os campos obrigatorios e formatos estiverem fechados;
3. os valores validos de `doc_type`, `status`, `phase_scope` e `authority_level` estiverem fechados;
4. as regras cruzadas entre campos estiverem explicitadas sem ambiguidade;
5. a maquina de estados e a autoridade de transicao estiverem documentadas;
6. existirem exemplos validos e invalidos suficientes para eliminar inferencia livre;
7. o escopo inicial de aplicacao estiver declarado;
8. a relacao de derivacao com `MAPA_DOCUMENTAL.md` estiver declarada;
9. o texto estiver claro o suficiente para futura validacao por script e CI;
10. qualquer agente consiga diferenciar documento ativo, historico e depreciado sem inferencia.
