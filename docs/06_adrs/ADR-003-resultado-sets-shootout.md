---
doc_id: adr-003-resultado-sets-shootout
doc_type: adr
status: current
phase_scope:
  - cross_phase
authority_level: supporting
owned_by: fase_0_documentary_baseline
canonical_path: /docs/06_adrs/ADR-003-resultado-sets-shootout.md
supersedes: []
superseded_by: null
must_read_before_implementation: false
implementation_ready: false
last_reviewed: "2026-06-24"
---

# ADR-003: Representacao do resultado do jogo

## Status

Aprovado

## Contexto

Handebol de areia nao pode ser representado de forma confiavel apenas por um placar agregado simples.

## Decisao

O MVP deve representar o jogo com:

- confronto principal em `matches`;
- estado explicito `draft` ou `finalized`;
- dois sets regulares em `match_sets`;
- `set_decision_type` em cada set para distinguir `regular_time` e `golden_goal`;
- shoot-out opcional em `match_shootouts`;
- resultado canonico em `matches.result_type`.
- alteracoes estruturais em jogo finalizado exigem reabertura controlada para `draft`.
- o placar armazenado em `match_sets` deve ser o placar oficial final do set, incluindo eventual gol decisivo de Golden Goal.

## Invariantes obrigatorios

- `won_2_0` exige sets 2-0 e ausencia de shoot-out;
- `lost_0_2` exige sets 0-2 e ausencia de shoot-out;
- `won_shootout` exige sets 1-1 e shoot-out vencido;
- `lost_shootout` exige sets 1-1 e shoot-out perdido.
- set regular nao pode terminar empatado;
- set com `set_decision_type = golden_goal` exige diferenca final absoluta de `1` ou `2`;
- shoot-out nao pode terminar empatado;
- jogo `finalized` exige exatamente dois sets registrados;
- jogo `finalized` exige `set_decision_type` preenchido nos dois sets;
- jogo `draft` nao deve aparecer por padrao em historicos competitivos, relatorios e comparacoes.
- jogo `finalized` nao pode ter `match_sets`, `match_shootouts` ou `match_roster` alterados ou excluidos fora do fluxo de reabertura controlada.
- jogo `finalized` nao pode ter `match_role_assignments` alterado ou excluido fora do fluxo de reabertura controlada.
- jogo `finalized` nao pode ter campos factuais de `matches` alterados fora do fluxo de reabertura controlada.
- atribuicoes com `match_phase = shootout` so podem existir quando o jogo tiver shoot-out real.
- eventos com `match_phase = shootout` so podem existir quando o jogo tiver shoot-out real.
- Golden Goal decide set; shoot-out decide o jogo apenas apos sets 1-1.

## Consequencias

- a implementacao deve proteger coerencia entre resultado, sets e shoot-out;
- a implementacao deve proteger coerencia entre `completion_status`, resultado, sets e shoot-out;
- a implementacao deve usar transacao atomica na finalizacao e na reabertura de jogo;
- jogo semanticamente contraditorio nao pode ser aceito como valido.
