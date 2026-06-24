---
doc_id: ordem-execucao-fase-1
doc_type: contract
status: current
phase_scope:
  - phase_1
authority_level: operational
owned_by: fase_1_execution_gate
canonical_path: /docs/05_fases/fase_1/ORDEM_EXECUCAO_FASE_1.md
supersedes: []
superseded_by: null
must_read_before_implementation: true
implementation_ready: false
last_reviewed: "2026-06-24"
---

# Ordem de Execucao da Fase 1

## Finalidade

Este documento restringe a execucao assistida por IA ao escopo permitido da Fase 1.

Ele nao reabre a ontologia consolidada, mas impede que a implementacao avance por inferencia para Fases 2 e 3.

Ele tambem nao substitui o artefato vigente de aprovacao da Fase 0: se o
baseline congelado ainda estiver em `aguardando_revalidacao_humana`, a Fase 1
permanece bloqueada mesmo com baseline tecnico `.ttl` ja validado.

## Regra de autoridade para esta execucao

Para iniciar a implementacao da Fase 1, usar esta ordem junto com:

1. [PROBLEMA_FINAL.md](/docs/01_contexto/PROBLEMA_FINAL.md:1)
2. [MVP.md](/docs/02_produto/MVP.md:1)
3. [ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md](/docs/03_ontologia/ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md:1)
4. [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/docs/04_implementacao/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:1)
5. [PLANO_EXECUCAO_IA_POR_FASES.md](/docs/05_fases/PLANO_EXECUCAO_IA_POR_FASES.md:1)

Se houver tentativa de implementar artefato que pertença a fase posterior, a execucao deve parar.

## Escopo permitido

- criar a base estrutural comum em SQLite;
- criar migracoes SQL versionadas;
- implementar o processo local em `127.0.0.1` com `workers=1`;
- implementar cadastros base de atletas, competicoes e adversarios;
- preparar trilha minima de auditoria na base;
- implementar backup manual assistido compativel com SQLite/WAL;
- implementar restauracao com validacao e rollback do banco anterior;
- provar persistencia apos fechar e reabrir a aplicacao.

## Fora de escopo

- nao criar tabelas de `matches`;
- nao criar tabelas de `match_sets`;
- nao criar tabelas de `match_shootouts`;
- nao criar tabelas de `match_roster`;
- nao criar tabelas de `match_role_assignments`;
- nao criar tabelas de `scout_event_types`;
- nao criar tabelas de `scout_events`;
- nao criar tela de scout;
- nao criar relatorios;
- nao criar comparacoes;
- nao iniciar logica de `draft` versus `finalized`;
- nao iniciar `reopen_to_draft`;
- nao iniciar Golden Goal, shoot-out ou validacoes de fase de jogo.

## Sequencia obrigatoria

1. criar estrutura de projeto e caminho fisico persistente do banco;
2. criar migracao inicial da base estrutural comum;
3. aplicar constraints estruturais cabiveis a essa base comum;
4. implementar cadastros base;
5. preparar trilha minima de auditoria;
6. implementar backup seguro;
7. implementar restauracao segura com validacao;
8. executar testes de schema e persistencia da Fase 1.

## Definition of Done da Fase 1

- banco criado em ambiente limpo;
- migracao executa sem erro;
- cadastros base persistem apos reinicio;
- backup valido e restauracao validada;
- `PRAGMA integrity_check` e `PRAGMA foreign_key_check` passam no banco restaurado;
- nenhum artefato de Fase 2 ou Fase 3 foi criado.

## Controle documental

- estes refinamentos nao reabrem a aprovacao semantica da Fase 0;
- se qualquer documento congelado da aprovacao formal for alterado e precisar virar novo baseline congelado, os hashes devem ser recalculados em novo registro de congelamento antes da execucao assistida por IA ser tratada como novo freeze documental.
- baseline tecnico de ontologia validado em `ontology/owl/` nao libera a Fase 1
  sozinho; a liberacao depende do status atual em
  `APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md`.
