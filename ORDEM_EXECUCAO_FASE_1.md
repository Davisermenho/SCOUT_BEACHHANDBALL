# Ordem de Execucao da Fase 1

## Finalidade

Este documento restringe a execucao assistida por IA ao escopo permitido da Fase 1.

Ele nao reabre a ontologia aprovada, mas impede que a implementacao avance por inferencia para Fases 2 e 3.

## Regra de autoridade para esta execucao

Para iniciar a implementacao da Fase 1, usar esta ordem junto com:

1. [PROBLEMA_FINAL.md](/home/davis/SCOUT_BEACHHANDBALL/PROBLEMA_FINAL.md:1)
2. [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:1)
3. [ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md](/home/davis/SCOUT_BEACHHANDBALL/ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md:1)
4. [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/home/davis/SCOUT_BEACHHANDBALL/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:1)
5. [PLANO_EXECUCAO_IA_POR_FASES.md](/home/davis/SCOUT_BEACHHANDBALL/PLANO_EXECUCAO_IA_POR_FASES.md:1)

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
