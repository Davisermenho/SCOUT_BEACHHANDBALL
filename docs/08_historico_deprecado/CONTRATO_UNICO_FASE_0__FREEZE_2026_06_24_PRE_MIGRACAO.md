---
doc_id: contrato-unico-fase-0-freeze-2026-06-24-pre-migracao
doc_type: archive
status: archived
phase_scope:
  - phase_0
authority_level: historical
owned_by: fase_0_documentary_history
canonical_path: /docs/08_historico_deprecado/CONTRATO_UNICO_FASE_0__FREEZE_2026_06_24_PRE_MIGRACAO.md
supersedes: []
superseded_by: /docs/05_fases/fase_0/CONTRATO_UNICO_FASE_0.md
must_read_before_implementation: false
implementation_ready: false
last_reviewed: "2026-06-24"
---

---
doc_id: contrato-unico-fase-0
doc_type: contract
status: current
phase_scope:
  - phase_0
authority_level: operational
owned_by: fase_0_documentary_baseline
canonical_path: /docs/05_fases/fase_0/CONTRATO_UNICO_FASE_0.md
supersedes: []
superseded_by: null
must_read_before_implementation: true
implementation_ready: false
last_reviewed: "2026-06-24"
---

# CONTRATO_UNICO_FASE_0

Este arquivo consolida o baseline documental da Fase 0 em um unico ponto de leitura operacional.

Regra de uso:

- este e o contrato unico operacional da Fase 0;
- ele absorve as decisoes normativas hoje espalhadas entre ontologia, aprovacao, matriz de achados e anexos de governanca ontologica;
- ele deve ser lido antes de qualquer trabalho que dependa do fechamento semantico da Fase 0;
- ele nao libera implementacao de produto por si so; `implementation_ready` permanece `false` porque a liberacao de codigo segue os gates documentais e operacionais posteriores.

## 1. Objetivo da Fase 0

Fechar a Fase 0 como baseline documental e semantico do scout de handebol de areia, garantindo simultaneamente:

- vocabulario canonico minimo congelado;
- invariantes semanticos criticos explicitamente definidos;
- cadeia de autoridade documental sem ambiguidade;
- gate humano ratificado sobre o baseline congelado;
- evidencias suficientes para liberar a leitura operacional da Fase 1 sem reabrir inferencia livre sobre a semantica do dominio.

## 2. Cadeia de autoridade interna da Fase 0

Ordem de autoridade obrigatoria para o escopo da Fase 0:

1. [PROBLEMA_FINAL.md](/docs/01_contexto/PROBLEMA_FINAL.md:1)
2. [MVP.md](/docs/02_produto/MVP.md:1)
3. [CONTRATO_UNICO_FASE_0.md](/docs/05_fases/fase_0/CONTRATO_UNICO_FASE_0.md)
4. [ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md](/docs/03_ontologia/ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md:1)
5. [APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md](/docs/05_fases/fase_0/APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md:1)
6. [MATRIZ_ACHADOS_FASE_0.md](/docs/05_fases/fase_0/MATRIZ_ACHADOS_FASE_0.md:1)
7. ADRs `001` a `006` em [adr/](/docs/06_adrs/)
8. anexos de governanca ontologica referenciados na secao 11

Regras:

- `PROBLEMA_FINAL.md` continua sendo o SSOT do problema;
- `MVP.md` continua sendo a referencia de escopo do produto;
- este contrato e o unico ponto operacional para decidir se a Fase 0 esta documentalmente fechada;
- `ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md` permanece como anexo semantico principal, mas nao como ponto de entrada concorrente ao contrato unico;
- em conflito entre este contrato e um anexo de suporte, prevalece este contrato;
- em conflito entre este contrato e `PROBLEMA_FINAL.md` ou `MVP.md`, a execucao deve parar para reconciliacao documental explicita.

## 3. Escopo incluido

Esta consolidacao inclui obrigatoriamente:

- definicao do objetivo documental da Fase 0;
- fechamento da cadeia de autoridade interna da fase;
- congelamento do vocabulario canonico inicial de scout;
- congelamento dos invariantes minimos de jogo, set, shoot-out, resultado e scout;
- registro do gate humano vigente e dos bloqueios remanescentes;
- rastreabilidade dos anexos normativos e de seus hashes;
- registro explicito dos documentos absorvidos por esta consolidacao;
- criterio documental de liberacao para a Fase 1.

Tambem entram como insumos cross-phase obrigatorios:

- [PROBLEMA_FINAL.md](/docs/01_contexto/PROBLEMA_FINAL.md:1)
- [MVP.md](/docs/02_produto/MVP.md:1)
- [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/docs/04_implementacao/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:1)
- [PLANO_EXECUCAO_IA_POR_FASES.md](/docs/05_fases/PLANO_EXECUCAO_IA_POR_FASES.md:1)

## 4. Escopo proibido

Este contrato nao autoriza:

- implementacao de produto por si so;
- liberacao automatica da Fase 1 sem obedecer [ORDEM_EXECUCAO_FASE_1.md](/docs/05_fases/fase_1/ORDEM_EXECUCAO_FASE_1.md:1);
- reabertura da Fase 0 por inferencia livre;
- inclusao de novos codigos de scout fora do freeze aprovado;
- mistura de handebol de quadra com handebol de areia;
- transformacao de video em modulo central do MVP;
- uso de `event_category` como campo estruturante livre no MVP inicial;
- substituicao de `match_roster` por presenca de treino;
- promocao deste contrato para `implementation_ready: true` sem novo gate documental explicito.

## 5. Vocabulario canonico aprovado

### 5.1 Estados e estruturas basicas

Valores canonicos congelados:

- `completion_status`: `draft`, `finalized`
- `match_result`: `won_2_0`, `lost_0_2`, `won_shootout`, `lost_shootout`
- `set_decision_type`: `regular_time`, `golden_goal`
- `match_phase`: `set_1`, `set_2`, `shootout`
- `role`: `court_player`, `goalkeeper`

### 5.2 Seed canonico inicial de eventos de scout

Codigos aprovados:

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

Regras operacionais congeladas:

- nenhum outro codigo entra no seed inicial sem nova aprovacao humana;
- `event_category` permanece `NULL` no MVP inicial;
- observacao coletiva fica fora de `scout_event_types` e permanece em `notes`;
- `goal_specialist` e `missed_specialist` ficam fora do MVP inicial por ambiguidade semantica;
- gol simples de jogadora comum vale `1` ponto;
- gol de especialista vale `2` pontos;
- gol de goleira vale `2` pontos;
- gol de giro, gol aereo e gol de tiro de `6` metros valem `2` pontos quando aplicavel.

## 6. Invariantes semanticos obrigatorios

Invariantes de dominio:

- o dominio do MVP e exclusivamente handebol de areia;
- `jogo` e o confronto completo, nao um set, lance ou sessao de video;
- cada jogo possui exatamente `2` sets regulares;
- `golden_goal` decide set, nao jogo;
- `shootout` decide jogo apenas depois de sets vencidos em `1-1`;
- o placar armazenado do set e o placar oficial final, incluindo eventual gol decisivo de `golden_goal`;
- o resultado final do jogo nao pode ser representado apenas por placar agregado generico.

Invariantes de presenca e participacao:

- `attendance` pertence a treino;
- presenca e participacao de jogo pertencem a `match_roster`;
- atleta ausente nao participa;
- atleta `did_not_play` nao recebe `match_role_assignments` nem scout individual.

Invariantes de atribuicao funcional:

- `match_role_assignments` registra atuacao efetiva por fase;
- a mesma atleta pode atuar como `court_player` e `goalkeeper` no mesmo jogo;
- atribuicao `shootout` so existe quando houver shoot-out real;
- validacao de `save_goalkeeper` depende de atribuicao funcional compativel na mesma fase.

Invariantes de scout:

- scout individual so e valido para atleta do elenco oficial com `presence_status = present` e `participation_status = played`;
- eventos com `phase_scope = regular_play` nao podem usar `match_phase = shootout`;
- eventos com `match_phase = shootout` sao invalidos sem shoot-out real;
- observacao coletiva fica em `notes` e nao entra como `event_type` comparavel;
- o MVP inicial nao usa texto livre como estrutura principal de scout.

Invariantes de pontuacao:

- gol simples de jogadora comum sem colete vale `1` ponto;
- qualquer gol legal da especialista vale `2` pontos;
- nao existe gol de especialista valendo `1` ponto no jogo corrente;
- jogadora comum pode valer `2` pontos por execucao espetacular valida;
- `gol_de_giro` e subclassificacao de `gol_espetacular`;
- `gol_aereo` e subclassificacao de `gol_espetacular`;
- `gol_criativo` nao e classe ontologica, apenas descricao informal;
- o sistema deve rejeitar inferencias proibidas declaradas em `DH-PONTUACAO-001`.

## 7. Gates humanos e documentais

| gate | estado atual | evidencia |
| --- | --- | --- |
| baseline tecnico minimo da ontologia validado | fechado | `ontology/owl/` reconhecido como baseline tecnico minimo no artefato de aprovacao |
| freeze documental da Fase 0 ratificado humanamente | fechado | `APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md` com status `ratificada_humanamente` |
| ADRs normativos da fase lidos e congelados | fechado | ADR-001 a ADR-006 listados no freeze |
| bloqueios semanticos remanescentes | fechado | artefato de aprovacao declara `nenhum` |
| bloqueios documentais remanescentes | fechado | artefato de aprovacao declara `nenhum` |
| obediencia a `ORDEM_EXECUCAO_FASE_1.md` para avancar de fase | obrigatorio | gate ativo apos o fechamento documental da Fase 0 |

Regra operacional:

- se qualquer anexo congelado sofrer hash drift, este contrato continua existindo, mas a ratificacao humana da Fase 0 deve ser considerada reaberta ate nova reconciliacao;
- a existencia tecnica do baseline ontologico nao substitui a ratificacao humana do freeze documental.

## 8. Evidencias exigidas

Para considerar a Fase 0 documentalmente fechada sob este contrato, devem existir simultaneamente:

- ontologia consolidada em [ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md](/docs/03_ontologia/ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md:1);
- matriz de achados consolidada em [MATRIZ_ACHADOS_FASE_0.md](/docs/05_fases/fase_0/MATRIZ_ACHADOS_FASE_0.md:1);
- gate humano registrado em [APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md](/docs/05_fases/fase_0/APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md:1);
- ADRs `001` a `006` congeladas por hash;
- baseline tecnico minimo da ontologia validado e reconhecido;
- hashes dos anexos obrigatorios preservados na secao 11;
- ausencia de bloqueio semantico ou documental remanescente declarada no artefato de aprovacao.

## 9. Criterio de conclusao

A Fase 0 esta concluida para fins documentais quando:

- a ontologia do scout esta sem ambiguidade critica remanescente no escopo do MVP;
- o vocabulario canonico inicial esta congelado;
- os invariantes de jogo, resultado, presenca, atribuicao funcional e scout estao explicitamente definidos;
- os ADRs normativos da fase estao aprovados e congelados;
- o freeze documental possui hashes verificaveis;
- a aprovacao humana vigente registra Fase 0 concluida e sem bloqueios remanescentes.

## 10. Criterio de liberacao para Fase 1

A Fase 1 pode ser lida como liberada apenas quando todos os itens abaixo forem verdadeiros:

- este contrato continuar sendo o unico ponto operacional da Fase 0;
- a secao 7 permanecer sem gate reaberto;
- os hashes da secao 11 permanecerem validos ou tiverem sido re-ratificados humanamente no mesmo changeset;
- [ORDEM_EXECUCAO_FASE_1.md](/docs/05_fases/fase_1/ORDEM_EXECUCAO_FASE_1.md:1) continuar sendo obedecida como contrato restritivo de entrada da Fase 1;
- nenhuma implementacao da Fase 1 tente reabrir semanticamente regras ja congeladas na Fase 0 por conveniencia tecnica.

Regra:

- a liberacao da Fase 1 significa apenas permissao para seguir o escopo restrito da Fase 1, nao autorizacao para pular para fases posteriores.

## 11. Anexos obrigatorios e hashes congelados

Data deste freeze contratual: `2026-06-24`

Algoritmo: `sha256`

Ferramenta de verificacao: `scripts/verify_phase0_freeze_hashes.py`

| arquivo | papel_no_gate | sha256 | observacao |
| --- | --- | --- | --- |
| `PROBLEMA_FINAL.md` | `ssot_contexto` | `aa0cdd7157c8114969fe72a5c84e4c6f7a6ab9ddbf616fa992a37f9440fd54ca` | problema central e restricoes do treinador solo |
| `MVP.md` | `escopo_produto` | `fa42bcc60582416e258a84f2898bbfc2576a55c3681966e7432c64cf334df006` | escopo minimo do MVP |
| `ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md` | `anexo_semantico_principal` | `df83b3ec09699acbfac7351ef84594958484e93df13a579eb71f26f62cba81ec` | definicoes canonicas do dominio |
| `ESPECIFICACAO_IMPLEMENTACAO_MVP.md` | `implementacao_cross_phase` | `355a44189ea93ef8d89065094c81c563793f1fd8a5d1c803c976493df0d59d93` | referencia tecnica subordinada ao MVP e a ontologia |
| `PLANO_EXECUCAO_IA_POR_FASES.md` | `sequenciamento_cross_phase` | `6178677c4db4cba7453b12d0629bb028160613b7e6ce1ed7911e0e004728ce37` | contrato de sequenciamento por fases |
| `APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md` | `gate_humano_vigente` | `449fb1cb299180147fb0429c1699d2dd81b6f0ebc3527150b33c9de1c48f8a1a` | ratificacao humana vigente da Fase 0 |
| `MATRIZ_ACHADOS_FASE_0.md` | `rastreabilidade_de_achados` | `54e2dcb3353067cea44644c050144502f2ad3b6c1fd1bf92da1c4bfffc42d407` | destino dos achados consolidados |
| `ORDEM_EXECUCAO_FASE_1.md` | `gate_de_saida_para_fase_1` | `a932ffad00a159767caf80425c86d09c3c8ed77ccf1f4bf7c694f730cade2397` | restricao operacional da fase seguinte |
| `adr/ADR-001-scout-roster-validation.md` | `adr_normativa_fase_0` | `c6fcc666e724ce8fcee1c250d7aa3650030495779d95ffdd50ad472af04c063d` | validacao de elenco e scout individual |
| `adr/ADR-002-backup-sqlite-wal.md` | `adr_normativa_fase_0` | `91ffe68ede17314c5e250464fafdb5c673440baae341d7d0afe4eaa4d7e85da5` | backup e restauracao compativeis com WAL |
| `adr/ADR-003-resultado-sets-shootout.md` | `adr_normativa_fase_0` | `ce5804774f5b10a41af06a10cb9dac4ecdfaf7d0a033509b16cbff194620b61d` | invariantes de resultado, sets e shoot-out |
| `adr/ADR-004-video-opcional-e-ontologia-bloqueadora.md` | `adr_normativa_fase_0` | `d03b8172f7f012dead33696ab8670d53e7df8f1ea1b1b0634e16557671f4547a` | video opcional e ontologia bloqueadora |
| `adr/ADR-005-cadastros-como-suporte-estrutural.md` | `adr_normativa_fase_0` | `d2cc4c0aca0f034d656f49568c8bfc193e1799e8064f201f96f4370f17b1b1bd` | cadastros como suporte estrutural |
| `adr/ADR-006-definition-of-done-por-fase.md` | `adr_normativa_fase_0` | `301f43b3029d22ec04317448d64a548a348a78f04bd33839f376cebd64c3d293` | definition of done e freeze por hash |
| `ontology/docs/02_domain_knowledge/ontology/00_governance/HANDOFF.md` | `anexo_governanca_ontologica` | `677d9e2e484776eeae1711d8328e42d2e2f1ff10b3c6397eab561ae6f1126a93` | continuidade operacional da governanca ontologica |
| `ontology/docs/02_domain_knowledge/ontology/00_governance/ONTOLOGY-OWL-001_SCOPE.md` | `anexo_governanca_ontologica` | `95712609dbc8f5111751b1aaf7513b388446b1375256734081174f9f28d7f0cc` | escopo do baseline OWL minimo |
| `ontology/docs/02_domain_knowledge/ontology/00_governance/PONTUACAO-001_MODELO_MINIMO.md` | `anexo_governanca_ontologica` | `653c17331b5169396998e524d098731ec0560470b8dc777b90b7272bebce8d5d` | modelagem minima da pontuacao |
| `ontology/docs/02_domain_knowledge/ontology/00_governance/PONTUACAO-001_SCOPE.md` | `anexo_governanca_ontologica` | `751601086954af151d1bf79eab94223e7488834ecef0c2d69b2b73284d3fca17` | escopo semantico da pontuacao |
| `ontology/docs/02_domain_knowledge/ontology/00_governance/VOCABULARIO_CANONICO_MINIMO.md` | `anexo_governanca_ontologica` | `c805315f0e4846a027c6d05ec849a0918f69612b5bf5779a5d0061b388ec1486` | vocabulario minimo auxiliar da governanca ontologica |
| `ontology/docs/02_domain_knowledge/ontology/04_human_decisions/DH-PONTUACAO-001.md` | `decisao_humana_literal` | `9da591b974e0f8065b38c9336c302ddf4ec4791b0f0b2ab7166f00033fcf21ae` | base literal das regras de pontuacao |

Regra de freeze:

- qualquer mudanca em hash reabre a necessidade de reconciliacao humana do baseline;
- nenhum anexo desta tabela pode ser alterado silenciosamente e continuar sendo tratado como parte do mesmo freeze.

## 12. Lista explicita dos documentos absorvidos ou reclassificados pela consolidacao

Passam a perder o papel de ponto primario de leitura para a Fase 0:

- `ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md`: reclassificado semanticamente como anexo principal da Fase 0, subordinado a este contrato;
- `APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md`: reclassificado semanticamente como gate humano congelado da Fase 0, nao mais como ponto primario de entrada;
- `MATRIZ_ACHADOS_FASE_0.md`: reclassificada semanticamente como artefato de rastreabilidade e nao mais como ponto primario de decisao;
- `ontology/docs/02_domain_knowledge/ontology/00_governance/HANDOFF.md`: reclassificado semanticamente como anexo de continuidade do subsistema `ontology/`;
- `ontology/docs/02_domain_knowledge/ontology/00_governance/ONTOLOGY-OWL-001_SCOPE.md`: reclassificado semanticamente como anexo de escopo tecnico minimo;
- `ontology/docs/02_domain_knowledge/ontology/00_governance/PONTUACAO-001_MODELO_MINIMO.md`: reclassificado semanticamente como anexo de modelagem minima;
- `ontology/docs/02_domain_knowledge/ontology/00_governance/PONTUACAO-001_SCOPE.md`: reclassificado semanticamente como anexo de escopo de pontuacao;
- `ontology/docs/02_domain_knowledge/ontology/00_governance/VOCABULARIO_CANONICO_MINIMO.md`: reclassificado semanticamente como anexo auxiliar de vocabulario;
- `ontology/docs/02_domain_knowledge/ontology/04_human_decisions/DH-PONTUACAO-001.md`: reclassificado semanticamente como decisao humana literal anexada ao contrato.

Lista explicita de documentos cuja depreciacao formal fica preparada por esta consolidacao, mas continua dependente das Etapas 6 e 7:

- `ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md`
- `APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md`
- `MATRIZ_ACHADOS_FASE_0.md`

Regra central em vigor apos esta publicacao:

- nenhum outro documento da Fase 0 deve continuar sendo tratado como contrato `canonical` ou `operational` concorrente a este arquivo.
