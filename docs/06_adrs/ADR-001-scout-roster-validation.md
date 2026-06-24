---
doc_id: adr-001-scout-roster-validation
doc_type: adr
status: current
phase_scope:
  - cross_phase
authority_level: supporting
owned_by: fase_0_documentary_baseline
canonical_path: /docs/06_adrs/ADR-001-scout-roster-validation.md
supersedes: []
superseded_by: null
must_read_before_implementation: false
implementation_ready: false
last_reviewed: "2026-06-24"
---

# ADR-001: Validacao de `scout_events` contra elenco e atribuicoes por fase

## Status

Aprovado

## Contexto

O sistema precisa impedir scout individual para atleta fora do elenco oficial do jogo.

SQLite com `athlete_id` nulo em scout coletivo torna a alternativa de chave estrangeira composta ambigua e propensa a interpretacao errada.

Alem disso, apenas existir no `match_roster` nao basta: atleta ausente ou `did_not_play` nao pode receber evento individual.

Eventos dependentes de funcao, como `save_goalkeeper`, exigem contexto dinamico por fase.

As atribuicoes funcionais devem representar atuacao efetiva, nao designacao prevista.

## Decisao

Para o MVP, a decisao oficial e:

- usar `TRIGGER` SQLite explicito para validar `scout_events` individuais contra `match_roster`;
- exigir `presence_status = present` e `participation_status = played` para aceitar scout individual;
- exigir atribuicao `goalkeeper` em `match_role_assignments` quando o `event_type` pedir papel de goleira;
- exigir `match_phase` em `scout_events` para validar funcao contextual e eventos exclusivos de shoot-out;
- exigir que toda atribuicao funcional pertenca a atleta presente e `played` no `match_roster` do mesmo jogo;
- tratar atribuicao funcional como fato ocorrido na fase, nunca como planejamento;
- nao criar valor proprio `specialist`; quando a mesma atleta possuir `court_player` e `goalkeeper` na mesma fase, essa combinacao basta como contexto funcional;
- nao manter em paralelo uma regra concorrente baseada em chave estrangeira composta ambigua para o mesmo objetivo.

## Consequencias

- a integridade fica com uma unica fonte de verdade;
- scout coletivo continua permitido com `athlete_id = NULL`;
- a implementacao deve incluir teste obrigatorio de recusa para atleta fora do elenco;
- a implementacao deve incluir teste obrigatorio de recusa para atleta `absent` ou `did_not_play`.
- a implementacao deve incluir teste obrigatorio de recusa para `save_goalkeeper` sem atribuicao `goalkeeper` na mesma fase.
- a implementacao deve incluir teste obrigatorio de recusa para atribuicao funcional fora do elenco, ausente ou `did_not_play`.
