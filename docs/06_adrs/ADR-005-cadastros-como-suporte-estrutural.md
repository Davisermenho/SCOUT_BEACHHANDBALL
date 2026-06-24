---
doc_id: adr-005-cadastros-como-suporte-estrutural
doc_type: adr
status: current
phase_scope:
  - cross_phase
authority_level: supporting
owned_by: fase_1_execution_gate
canonical_path: /docs/06_adrs/ADR-005-cadastros-como-suporte-estrutural.md
supersedes: []
superseded_by: null
must_read_before_implementation: false
implementation_ready: false
last_reviewed: "2026-06-24"
---

# ADR-005: Cadastros base como suporte estrutural

## Status

Aprovado

## Contexto

`PROBLEMA_FINAL.md` lista fluxos centrais do MVP, mas a implementacao precisa de cadastros base para que eles existam.

## Decisao

- cadastros de atletas, competicoes e adversarios sao suporte estrutural obrigatorio;
- eles nao configuram ampliacao indevida de objetivo de produto.

## Consequencias

- a IA nao deve tratar esses cadastros como modulo de produto separado;
- a existencia deles serve para viabilizar jogo, treino, historico e scout.
