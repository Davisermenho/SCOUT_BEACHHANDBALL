---
doc_id: revisao-mvp-x-especificacao-implementacao
doc_type: review
status: current
phase_scope:
  - cross_phase
authority_level: supporting
owned_by: mvp_implementation_contract
canonical_path: /docs/07_revisoes_e_auditorias/REVISAO_MVP_X_ESPECIFICACAO_IMPLEMENTACAO.md
supersedes: []
superseded_by: null
must_read_before_implementation: false
implementation_ready: false
last_reviewed: "2026-06-24"
---

# Revisao: MVP x Especificacao de Implementacao

## Finalidade

Esta e a auditoria mais importante para implementacao assistida por IA.

Ela verifica se a [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/docs/04_implementacao/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:1) respeita o [MVP.md](/docs/02_produto/MVP.md:1) sem criar divergencias que possam contaminar codigo.

## Veredito

Status geral:

- `direcao arquitetural`: alinhada
- `presenca vs participacao`: alinhada apos revisoes
- `scout pos-jogo`: alinhado
- `semantica do dominio`: alinhada com dependencia obrigatoria da ontologia
- `golden_goal`: alinhado no nivel documental
- `backup SQLite WAL`: alinhado no nivel documental
- `imutabilidade pos-finalizacao`: alinhada no nivel documental
- `rastreabilidade minima`: alinhada no nivel documental
- `transacoes e restauracao`: alinhadas no nivel documental

Conclusao:

- a especificacao esta coerente o bastante para servir de base tecnica;
- o bloqueio restante deixou de ser conflito normativo entre `MVP.md` e especificacao;
- a Fase 0 documental permanece em `aguardando_revalidacao_humana` do baseline reconciliado;
- o bloqueio restante deixa de ser ausencia de ontologia e passa a ser de ratificacao humana, implementacao, teste e piloto real.

## Pontos auditados

### 1. Autoridade semantica

Status:

- alinhado.

Evidencia:

- [MVP.md](/docs/02_produto/MVP.md:34)
- [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/docs/04_implementacao/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:19)

### 2. Presenca de treino vs presenca de jogo

Status:

- alinhado.

Decisao efetiva:

- treino usa `attendance`;
- jogo usa `match_roster`.

Evidencia:

- [MVP.md](/docs/02_produto/MVP.md:476)
- [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/docs/04_implementacao/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:997)

### 3. Scout individual vinculado ao elenco

Status:

- alinhado.

Decisao efetiva:

- validacao estrutural obrigatoria via `TRIGGER` SQLite.

Evidencia:

- [MVP.md](/docs/02_produto/MVP.md:513)
- [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/docs/04_implementacao/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:631)

### 4. Video como apoio opcional

Status:

- alinhado.

Evidencia:

- [MVP.md](/docs/02_produto/MVP.md:125)
- [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/docs/04_implementacao/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:44)

Ressalva:

- a rota `/media` existe para suporte tecnico, nao para recentralizar o projeto em video.

### 5. Resultado do jogo com sets e shoot-out

Status:

- alinhado, mas depende de implementacao fiel.

Evidencia:

- [MVP.md](/docs/02_produto/MVP.md:400)
- [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/docs/04_implementacao/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:448)

### 5.1 Golden Goal

Status:

- alinhado.

Decisao efetiva:

- `match_sets` armazena placar oficial final do set;
- `set_decision_type` distingue `regular_time` de `golden_goal`;
- shoot-out permanece separado e decide o jogo apenas apos sets 1-1.

Evidencia:

- [MVP.md](/docs/02_produto/MVP.md:447)
- [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/docs/04_implementacao/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:549)

### 6. Frontend nao pode anteceder fundacao

Status:

- alinhado.

Evidencia:

- [MVP.md](/docs/02_produto/MVP.md:673)
- [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/docs/04_implementacao/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:84)

### 7. Prova executavel por fase

Status:

- alinhado.

Evidencia:

- [MVP.md](/docs/02_produto/MVP.md:911)
- [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/docs/04_implementacao/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:1237)

## Pontos de atencao remanescentes

### 1. Implementacao e teste executavel

Status:

- pendente de execucao.

Acao:

- implementar o contrato normativo e provar com testes e piloto real.

## Decisao

Esta auditoria nao identifica conflito arquitetural bloqueante restante entre `MVP.md` e `ESPECIFICACAO_IMPLEMENTACAO_MVP.md`.

O bloqueio remanescente agora e:

- execucao fiel da implementacao, testes obrigatorios e piloto real.
