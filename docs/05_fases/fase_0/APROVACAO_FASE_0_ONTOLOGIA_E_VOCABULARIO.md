---
doc_id: aprovacao-fase-0-ontologia-e-vocabulario
doc_type: approval
status: current
phase_scope:
  - phase_0
authority_level: supporting
owned_by: fase_0_documentary_baseline
canonical_path: /docs/05_fases/fase_0/APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md
supersedes:
  - /docs/08_historico_deprecado/APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO__RATIFICADA_2026_06_23.md
superseded_by: null
must_read_before_implementation: true
implementation_ready: false
last_reviewed: "2026-06-24"
---

# Aprovacao da Fase 0: Ontologia e Vocabulario

## Status atual

- status: `aguardando_revalidacao_humana`
- Fase 0 concluida: `nao`
- liberado para iniciar Fase 1: `nao`
- bloqueios semanticos remanescentes: `nenhum`
- bloqueios documentais remanescentes: `revalidacao_humana_do_freeze_pos_migracao`

## Responsabilidade humana

- aprovador principal: `Davi Costa Sermenho do Nascimento`
- papel: `treinador responsavel pelo scout`
- data da ultima aprovacao invalida por hash: `2026-06-24`
- data da reconciliacao documental do baseline pos-migracao: `2026-06-24`
- data da ultima ratificacao humana concluida: `2026-06-23`
- data da reabertura documental pos-migracao: `2026-06-24`

## Estado deste artefato

- a ratificacao humana concluida em `2026-06-23` foi preservada como snapshot historico em `/docs/08_historico_deprecado/APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO__RATIFICADA_2026_06_23.md`;
- a migracao fisica da Etapa 6 para `docs/**`, somada a insercao de frontmatter nos arquivos congelados, alterou o conjunto de hashes do baseline vigente;
- este artefato registra o baseline candidato pos-migracao e exige nova ratificacao humana antes de a Fase 1 voltar a ser tratada como liberada;
- o baseline tecnico minimo da ontologia continua valido em `ontology/owl/`, mas nao substitui a revalidacao humana do freeze documental.

## Documentos congelados para a decisao

- [PROBLEMA_FINAL.md](/docs/01_contexto/PROBLEMA_FINAL.md:1)
- [MVP.md](/docs/02_produto/MVP.md:1)
- [ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md](/docs/03_ontologia/ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md:1)
- [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/docs/04_implementacao/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:1)
- [PLANO_EXECUCAO_IA_POR_FASES.md](/docs/05_fases/PLANO_EXECUCAO_IA_POR_FASES.md:1)
- [ORDEM_EXECUCAO_FASE_1.md](/docs/05_fases/fase_1/ORDEM_EXECUCAO_FASE_1.md:1)
- [ADR-001-scout-roster-validation.md](/docs/06_adrs/ADR-001-scout-roster-validation.md:1)
- [ADR-002-backup-sqlite-wal.md](/docs/06_adrs/ADR-002-backup-sqlite-wal.md:1)
- [ADR-003-resultado-sets-shootout.md](/docs/06_adrs/ADR-003-resultado-sets-shootout.md:1)
- [ADR-004-video-opcional-e-ontologia-bloqueadora.md](/docs/06_adrs/ADR-004-video-opcional-e-ontologia-bloqueadora.md:1)
- [ADR-005-cadastros-como-suporte-estrutural.md](/docs/06_adrs/ADR-005-cadastros-como-suporte-estrutural.md:1)
- [ADR-006-definition-of-done-por-fase.md](/docs/06_adrs/ADR-006-definition-of-done-por-fase.md:1)

## Revisoes congeladas

Cada aprovacao humana da Fase 0 deve registrar o identificador exato dos arquivos avaliados.

Formato obrigatorio:

- caminho do arquivo
- `sha256`
- data da leitura

Qualquer alteracao posterior em hash invalida a aprovacao anterior e reabre a Fase 0.

Registros atuais:

- registro historico ratificado em `2026-06-23`: preservado integralmente no snapshot historico arquivado;
- data da leitura do baseline candidato pos-migracao: `2026-06-24`;
- conjunto ativo a ser revalidado: exatamente o mesmo conjunto e os mesmos hashes declarados na secao `11` de `CONTRATO_UNICO_FASE_0.md`;
- qualquer divergencia entre este artefato e a secao `11` do contrato unico invalida a revalidacao humana.

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
- snapshot historico ratificado preservado: `APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO__RATIFICADA_2026_06_23.md`
- reconciliacao documental pos-migracao concluida: `2026-06-24`
- baseline candidato pos-migracao: `aguardando_revalidacao_humana`
- observacoes do baseline candidato: `migracao canonica para docs/**; frontmatter adicionado aos documentos governados; links internos atualizados; hashes recalculados em novo freeze candidato; Fase 1 bloqueada ate nova ratificacao humana`
- bloqueios remanescentes: `revalidacao_humana_do_freeze_pos_migracao`

## Decisao

O baseline documental pos-migracao ainda nao foi ratificado humanamente.

A Fase 0 permanece semanticamente fechada, mas documentalmente em
`aguardando_revalidacao_humana` ate a nova ratificacao do freeze candidato.

Enquanto esse estado persistir, a execucao da Fase 1 permanece bloqueada,
mesmo com os contratos tecnicos ja migrados para `docs/**`.
