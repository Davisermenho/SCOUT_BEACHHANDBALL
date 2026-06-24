# Aprovacao da Fase 0: Ontologia e Vocabulario

## Status atual

- status: `ratificada_humanamente`
- Fase 0 concluida: `sim`
- liberado para iniciar Fase 1: `sim`
- bloqueios semanticos remanescentes: `nenhum`
- bloqueios documentais remanescentes: `nenhum`

## Responsabilidade humana

- aprovador principal: `Davi Costa Sermenho do Nascimento`
- papel: `treinador responsavel pelo scout`
- data da ultima aprovacao invalida por hash: `2026-06-18`
- data da reconciliacao documental deste baseline: `2026-06-23`
- data da ratificacao humana vigente: `2026-06-23`

## Estado deste artefato

- a aprovacao registrada anteriormente foi invalidada por divergencia de hash em documentos congelados;
- este artefato registra o novo conjunto reconciliado, com hashes atuais e ordem operacional da Fase 1 incluida;
- o baseline reconciliado atual reconhece que a ontologia ja possui baseline tecnico minimo validado em `ontology/owl/`;
- a ratificacao humana explicita do baseline reconciliado foi registrada em `2026-06-23`.

## Documentos congelados para a decisao

- [PROBLEMA_FINAL.md](/home/davis/SCOUT_BEACHHANDBALL/PROBLEMA_FINAL.md:1)
- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:1)
- [ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md](/home/davis/SCOUT_BEACHHANDBALL/ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md:1)
- [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/home/davis/SCOUT_BEACHHANDBALL/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:1)
- [PLANO_EXECUCAO_IA_POR_FASES.md](/home/davis/SCOUT_BEACHHANDBALL/PLANO_EXECUCAO_IA_POR_FASES.md:1)
- [ORDEM_EXECUCAO_FASE_1.md](/home/davis/SCOUT_BEACHHANDBALL/ORDEM_EXECUCAO_FASE_1.md:1)
- [ADR-001-scout-roster-validation.md](/home/davis/SCOUT_BEACHHANDBALL/adr/ADR-001-scout-roster-validation.md:1)
- [ADR-002-backup-sqlite-wal.md](/home/davis/SCOUT_BEACHHANDBALL/adr/ADR-002-backup-sqlite-wal.md:1)
- [ADR-003-resultado-sets-shootout.md](/home/davis/SCOUT_BEACHHANDBALL/adr/ADR-003-resultado-sets-shootout.md:1)
- [ADR-004-video-opcional-e-ontologia-bloqueadora.md](/home/davis/SCOUT_BEACHHANDBALL/adr/ADR-004-video-opcional-e-ontologia-bloqueadora.md:1)
- [ADR-005-cadastros-como-suporte-estrutural.md](/home/davis/SCOUT_BEACHHANDBALL/adr/ADR-005-cadastros-como-suporte-estrutural.md:1)
- [ADR-006-definition-of-done-por-fase.md](/home/davis/SCOUT_BEACHHANDBALL/adr/ADR-006-definition-of-done-por-fase.md:1)

## Revisoes congeladas

Cada aprovacao humana da Fase 0 deve registrar o identificador exato dos arquivos avaliados.

Formato obrigatorio:

- caminho do arquivo
- `sha256`
- data da leitura

Qualquer alteracao posterior em hash invalida a aprovacao anterior e reabre a Fase 0.

Registros atuais:

- data da leitura deste conjunto congelado: `2026-06-23`

- `PROBLEMA_FINAL.md`: `aa0cdd7157c8114969fe72a5c84e4c6f7a6ab9ddbf616fa992a37f9440fd54ca`
- `MVP.md`: `fa42bcc60582416e258a84f2898bbfc2576a55c3681966e7432c64cf334df006`
- `ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md`: `df83b3ec09699acbfac7351ef84594958484e93df13a579eb71f26f62cba81ec`
- `ESPECIFICACAO_IMPLEMENTACAO_MVP.md`: `355a44189ea93ef8d89065094c81c563793f1fd8a5d1c803c976493df0d59d93`
- `PLANO_EXECUCAO_IA_POR_FASES.md`: `6178677c4db4cba7453b12d0629bb028160613b7e6ce1ed7911e0e004728ce37`
- `ORDEM_EXECUCAO_FASE_1.md`: `a932ffad00a159767caf80425c86d09c3c8ed77ccf1f4bf7c694f730cade2397`
- `ADR-001-scout-roster-validation.md`: `c6fcc666e724ce8fcee1c250d7aa3650030495779d95ffdd50ad472af04c063d`
- `ADR-002-backup-sqlite-wal.md`: `91ffe68ede17314c5e250464fafdb5c673440baae341d7d0afe4eaa4d7e85da5`
- `ADR-003-resultado-sets-shootout.md`: `ce5804774f5b10a41af06a10cb9dac4ecdfaf7d0a033509b16cbff194620b61d`
- `ADR-004-video-opcional-e-ontologia-bloqueadora.md`: `d03b8172f7f012dead33696ab8670d53e7df8f1ea1b1b0634e16557671f4547a`
- `ADR-005-cadastros-como-suporte-estrutural.md`: `d2cc4c0aca0f034d656f49568c8bfc193e1799e8064f201f96f4370f17b1b1bd`
- `ADR-006-definition-of-done-por-fase.md`: `301f43b3029d22ec04317448d64a548a348a78f04bd33839f376cebd64c3d293`

## Checklist obrigatorio de aprovacao

- [x] definicao de `jogo`, `set`, `golden_goal`, `shoot-out` e `resultado do jogo` aprovada
- [x] definicao de `draft` versus `finalized` aprovada
- [x] definicao de `presenca` versus `participacao` aprovada
- [x] semantica de `match_role_assignments` e `match_phase` aprovada
- [x] pertencimento estrutural de `match_role_assignments` ao `match_roster` aprovado
- [x] semantica de atribuicao efetiva versus designacao prevista aprovada
- [x] regra bidirecional de `phase_scope` aprovada
- [x] consistencia entre atribuicoes `shootout` e existencia real de shoot-out aprovada
- [x] regra de scout individual apenas para atleta `played` aprovada
- [x] regra de observacao coletiva em `notes` aprovada
- [x] regra de especialista sem valor proprio dedicada aprovada
- [x] politica de `event_category` como `NULL` no MVP inicial aprovada
- [x] vocabulario canonico inicial aprovado
- [x] convencao de classificacao primaria das finalizacoes aprovada
- [x] invariantes de resultado aprovados
- [x] dataset piloto minimo definido
- [x] baseline de carga operacional definida
- [x] ordem restritiva de execucao da Fase 1 congelada no baseline

## Vocabulario congelado do MVP inicial

Lista a aprovar:

- `goal_spin_shot`
- `goal_inflight`
- `goal_two_point_other`
- `goal_regular`
- `missed_spin_shot`
- `missed_inflight`
- `missed_two_point_other`
- `missed_regular`
- `save_goalkeeper`
- `turnover`
- `steal`
- `block_defense`
- `exclusion_received`
- `shootout_scored`
- `shootout_missed`

Regra operacional:

- nenhum outro codigo pode entrar no seed inicial sem nova aprovacao humana;
- `event_category` permanece `NULL` no MVP inicial.
- observacao coletiva fica fora de `scout_event_types` e permanece em `notes`.
- `goal_specialist` e `missed_specialist` ficam fora do MVP inicial por ambiguidade semantica.
- o vocabulario inicial de quinze eventos foi aprovado pelo aprovador humano em `2026-06-18`.

## Dataset piloto minimo de validacao semantica

O piloto minimo deve conter:

- 2 jogos finalizados;
- 1 jogo `won_2_0`;
- 1 jogo `won_shootout` ou `lost_shootout`;
- em pelo menos 1 jogo, 1 set encerrado em `golden_goal`;
- em pelo menos 1 jogo, uma atleta `present` com `did_not_play`;
- em pelo menos 1 jogo, uma atleta `absent`;
- em pelo menos 1 jogo, a mesma atleta atuando na linha e como goleira em fases diferentes ou na mesma fase;
- em pelo menos 1 jogo, atribuicao `goalkeeper` em `set_1`, `set_2` ou `shootout`;
- em pelo menos 1 jogo, tentativa negativa de atribuicao funcional para atleta fora do elenco;
- em pelo menos 1 jogo, eventos individuais validos para atleta `played`;
- em pelo menos 1 jogo, `save_goalkeeper` validado contra atribuicao por fase;
- em pelo menos 1 jogo, observacao coletiva em `notes`;
- em pelo menos 1 jogo, tentativa negativa prevista para validacao de integridade.

## Baseline inicial de carga operacional

Registrar no piloto:

- tempo total de fechamento pos-jogo;
- quantidade de campos obrigatorios preenchidos;
- quantidade de retrabalhos ou correcoes necessarias;
- observacao humana sobre se o fluxo foi compativel com operacao solo.

Limites objetivos iniciais de aprovacao:

- ate 20 minutos para fechamento completo de um jogo com ate 12 atletas e ate 40 eventos;
- no maximo 3 correcoes estruturais apos o primeiro salvamento;
- possibilidade de interrupcao e retomada segura enquanto o jogo estiver `draft`;
- aprovacao humana explicita apos execucao de 2 jogos reais completos, sem ferramenta paralela.

## Evidencias anexadas

- artefato de aprovacao anterior invalidado por hash drift: `validacao humana direta em 2026-06-18`
- reconciliacao documental concluida: `2026-06-23`
- ratificacao humana vigente do baseline reconciliado: `RATIFICACAO-HUMANA-FREEZE-FASE-0` em `2026-06-23`
- observacoes do baseline reconciliado: `set_decision_type no payload; event_category fora da UX inicial; restore com rollback; consumo de reopen_to_draft; Fase 1 restrita e congelada; baseline tecnico minimo da ontologia ja validado por rdflib e SHACL; bloqueio remanescente e ratificacao humana do freeze`
- bloqueios remanescentes: `nenhum`

## Decisao

O baseline documental reconciliado foi ratificado humanamente.

A Fase 0 esta concluida e a execucao da Fase 1 fica liberada, respeitando
`ORDEM_EXECUCAO_FASE_1.md` e os limites ainda vigentes de escopo.
