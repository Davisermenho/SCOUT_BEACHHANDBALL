---
doc_id: mapa-documental
doc_type: inventory
status: proposed
phase_scope:
  - cross_phase
authority_level: proposed
owned_by: repo_governance_bootstrap
canonical_path: /docs/00_governanca/MAPA_DOCUMENTAL.md
supersedes: []
superseded_by: null
must_read_before_implementation: false
implementation_ready: false
last_reviewed: "2026-06-24"
---

# MAPA_DOCUMENTAL

## 1. Finalidade

Este arquivo registra o inventario bootstrap da documentacao Markdown do repositorio.

Ele existe para:

- listar os arquivos documentais relevantes do estado atual do repo;
- classificar cada item no nivel bootstrap;
- indicar destino canonico planejado ou decisao de manutencao;
- materializar a Etapa 1 do plano de governanca documental.

## 2. Regra de uso

Este mapa:

- e derivado dos arquivos reais do repositorio;
- nao substitui o conteudo normativo dos documentos inventariados;
- usa classificacao bootstrap estimada, a ser refinada em `ESQUEMA_METADADOS_DOCUMENTAIS.md`;
- deve ser atualizado no mesmo changeset em que qualquer documento governado for criado, movido, depreciado ou arquivado.

Fonte primaria de verdade nesta etapa:

- caminhos reais do repo;
- conteudo atual dos arquivos;
- plano em `docs/00_governanca/PLANO_CONTRATO_ORGANIZACAO_DOCUMENTAL.md`.

## 3. Checklist Formal de Aceite da Etapa 1

- [x] Todos os arquivos Markdown relevantes identificados no bootstrap inicial foram inventariados neste mapa.
- [x] Os documentos de governanca criados nas Etapas 2 e 3 foram incorporados ao inventario de `docs/00_governanca/`.
- [x] Cada entrada possui classificacao bootstrap para `doc_type`, `phase_scope`, `authority_level`, `status`, `destino_canonico_planejado` e `acao_planejada`.
- [x] O mapa cobre os conjuntos prioritarios da raiz, ADRs, fontes, `docs/00_governanca/` e o subsistema `ontology/`.
- [x] O mapa declara explicitamente que e derivado do estado real do repo e nao a fonte primaria de verdade.
- [x] Cada item listado possui destino canonico planejado ou decisao explicita de manutencao no local atual.
- [x] Nenhum arquivo Markdown governado em `docs/00_governanca/` ficou sem classificacao bootstrap.

## 4. Legenda de classificacao bootstrap

Colunas usadas neste mapa:

- `doc_type_proposto`: valor bootstrap sugerido para convergencia futura ao schema.
- `phase_scope_proposto`: fase estimada a que o documento pertence.
- `authority_level_proposto`: papel de autoridade bootstrap estimado.
- `status_proposto`: estado bootstrap estimado no fluxo documental.
- `destino_canonico_planejado`: caminho final previsto ou decisao de manutencao.
- `acao_planejada`: mover, manter, consolidar, depreciar, arquivar ou revisar.

## 5. Inventario Bootstrap

### 5.1 Governanca bootstrap em `docs/00_governanca/`

| arquivo_atual | doc_type_proposto | phase_scope_proposto | authority_level_proposto | status_proposto | destino_canonico_planejado | acao_planejada | observacoes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `docs/00_governanca/PLANO_CONTRATO_ORGANIZACAO_DOCUMENTAL.md` | `plan` | `cross_phase` | `proposed` | `proposed` | `/docs/00_governanca/PLANO_CONTRATO_ORGANIZACAO_DOCUMENTAL.md` | manter e posteriormente arquivar | plano bootstrap; sera sucedido pelo contrato definitivo |
| `docs/00_governanca/MAPA_DOCUMENTAL.md` | `inventory` | `cross_phase` | `proposed` | `proposed` | `/docs/00_governanca/MAPA_DOCUMENTAL.md` | manter e atualizar | inventario bootstrap da Etapa 1 |
| `docs/00_governanca/ESQUEMA_METADADOS_DOCUMENTAIS.md` | `contract` | `cross_phase` | `proposed` | `proposed` | `/docs/00_governanca/ESQUEMA_METADADOS_DOCUMENTAIS.md` | manter e promover apos aprovacao humana | schema canonico bootstrap dos metadados documentais |
| `docs/00_governanca/CONTRATO_GOVERNANCA_DOCUMENTAL.md` | `contract` | `cross_phase` | `proposed` | `proposed` | `/docs/00_governanca/CONTRATO_GOVERNANCA_DOCUMENTAL.md` | manter e promover apos aprovacao humana | contrato canonico proposto para a governanca documental |

### 5.2 Contratos, aprovacoes e documentos de fase hoje na raiz

| arquivo_atual | doc_type_proposto | phase_scope_proposto | authority_level_proposto | status_proposto | destino_canonico_planejado | acao_planejada | observacoes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PROBLEMA_FINAL.md` | `contract` | `cross_phase` | `ssot` | `current` | `/docs/01_contexto/PROBLEMA_FINAL.md` | mover | fonte principal da definicao do problema |
| `MVP.md` | `contract` | `cross_phase` | `canonical` | `current` | `/docs/02_produto/MVP.md` | mover | contrato do MVP |
| `ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md` | `contract` | `phase_0` | `canonical` | `current` | `/docs/03_ontologia/ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md` | mover | autoridade semantica do MVP |
| `ESPECIFICACAO_IMPLEMENTACAO_MVP.md` | `contract` | `cross_phase` | `operational` | `current` | `/docs/04_implementacao/ESPECIFICACAO_IMPLEMENTACAO_MVP.md` | mover | especificacao executavel |
| `PLANO_EXECUCAO_IA_POR_FASES.md` | `contract` | `cross_phase` | `operational` | `current` | `/docs/05_fases/PLANO_EXECUCAO_IA_POR_FASES.md` | mover | contrato de execucao por fases |
| `APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md` | `approval` | `phase_0` | `supporting` | `current` | `/docs/05_fases/fase_0/APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md` | mover | gate humano vigente da Fase 0 |
| `MATRIZ_ACHADOS_FASE_0.md` | `review` | `phase_0` | `supporting` | `current` | `/docs/05_fases/fase_0/MATRIZ_ACHADOS_FASE_0.md` | mover | matriz de destino dos achados da Fase 0 |
| `ORDEM_EXECUCAO_FASE_1.md` | `contract` | `phase_1` | `operational` | `current` | `/docs/05_fases/fase_1/ORDEM_EXECUCAO_FASE_1.md` | mover | restricao operacional da Fase 1 |
| `FECHAMENTO_TECNICO_FASE_1_BASE_ESTRUTURAL.md` | `review` | `phase_1` | `supporting` | `current` | `/docs/05_fases/fase_1/FECHAMENTO_TECNICO_FASE_1_BASE_ESTRUTURAL.md` | mover | fechamento tecnico de suporte a Fase 1 |
| `MATRIZ_TESTES_FASE_1_BASE_ESTRUTURAL.md` | `review` | `phase_1` | `supporting` | `current` | `/docs/05_fases/fase_1/MATRIZ_TESTES_FASE_1_BASE_ESTRUTURAL.md` | mover | matriz de testes obrigatorios da Fase 1 |

### 5.3 Revisoes, historicos e rascunhos hoje na raiz

| arquivo_atual | doc_type_proposto | phase_scope_proposto | authority_level_proposto | status_proposto | destino_canonico_planejado | acao_planejada | observacoes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `REVISAO_COMPLETA_PROBLEMA_FINAL_X_MVP.md` | `review` | `cross_phase` | `historical` | `deprecated` | `/docs/07_revisoes_e_auditorias/REVISAO_COMPLETA_PROBLEMA_FINAL_X_MVP.md` | mover e manter como historico | o proprio arquivo indica substituicao operacional |
| `REVISAO_MODELAGEM_BANCO_X_FASE_1.md` | `review` | `phase_1` | `supporting` | `current` | `/docs/07_revisoes_e_auditorias/REVISAO_MODELAGEM_BANCO_X_FASE_1.md` | mover | revisao de aderencia da modelagem legada |
| `REVISAO_MVP_X_ESPECIFICACAO_IMPLEMENTACAO.md` | `review` | `cross_phase` | `supporting` | `current` | `/docs/07_revisoes_e_auditorias/REVISAO_MVP_X_ESPECIFICACAO_IMPLEMENTACAO.md` | mover | auditoria entre MVP e especificacao |
| `REVISAO_PROBLEMA_FINAL_X_MVP_v2.md` | `review` | `cross_phase` | `supporting` | `current` | `/docs/07_revisoes_e_auditorias/REVISAO_PROBLEMA_FINAL_X_MVP_v2.md` | mover | revisao operacional mais recente do par problema/MVP |
| `MODELAGEM DO BANCO DE DADOS.md` | `archive` | `phase_1` | `historical` | `archived` | `/docs/08_historico_deprecado/MODELAGEM_DO_BANCO_DE_DADOS.md` | mover para historico | documento legado explicitamente sujeito a revisao |
| `tetes.md` | `archive` | `cross_phase` | `historical` | `archived` | `/docs/08_historico_deprecado/tetes.md` | mover para historico | analise solta sem papel normativo atual |

### 5.4 ADRs atuais em `adr/`

Classificacao bootstrap comum deste bloco:

- `doc_type_proposto`: `adr`
- `phase_scope_proposto`: `cross_phase`
- `authority_level_proposto`: `supporting`
- `status_proposto`: `current`
- `destino_canonico_planejado`: `/docs/06_adrs/`
- `acao_planejada`: mover

Arquivos cobertos:

- `adr/ADR-001-scout-roster-validation.md`
- `adr/ADR-002-backup-sqlite-wal.md`
- `adr/ADR-003-resultado-sets-shootout.md`
- `adr/ADR-004-video-opcional-e-ontologia-bloqueadora.md`
- `adr/ADR-005-cadastros-como-suporte-estrutural.md`
- `adr/ADR-006-definition-of-done-por-fase.md`

### 5.5 Fontes e derivados textuais

| arquivo_atual | doc_type_proposto | phase_scope_proposto | authority_level_proposto | status_proposto | destino_canonico_planejado | acao_planejada | observacoes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `docs/fontes/PRAXIOLOGIA.md` | `review` | `cross_phase` | `supporting` | `current` | `/docs/09_fontes/PRAXIOLOGIA.md` | mover em etapa controlada | derivado documental de fonte externa |
| `docs/fontes/PRAXIOLOGIA_2.md` | `review` | `cross_phase` | `supporting` | `current` | `/docs/09_fontes/PRAXIOLOGIA_2.md` | mover em etapa controlada | derivado documental de fonte externa |
| `fontes/PRAXIOLOGIA.md` | `archive` | `cross_phase` | `historical` | `deprecated` | `/docs/09_fontes/PRAXIOLOGIA.md` | depreciar em favor de `docs/fontes/PRAXIOLOGIA.md` | duplicata fora da arvore `docs/` |

### 5.6 Subsistema `ontology/` fora da migracao prioritaria da Etapa 1

Regra bootstrap deste bloco:

- o subsistema `ontology/` permanece ativo no local atual durante a Etapa 1;
- a convergencia total ao schema do repo sera refinada em etapa posterior;
- quando o destino canonico ainda nao estiver redefinido, o mapa registra manutencao no caminho atual.

#### 5.6.1 Arquivos gerais do subsistema

| arquivo_atual | doc_type_proposto | phase_scope_proposto | authority_level_proposto | status_proposto | destino_canonico_planejado | acao_planejada | observacoes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ontology/README.md` | `review` | `phase_0` | `supporting` | `current` | `manter em ontology/README.md` | manter | README do subsistema especializado |
| `ontology/prompt.md` | `archive` | `phase_0` | `historical` | `archived` | `manter em ontology/prompt.md ate revisao posterior` | revisar e possivelmente arquivar formalmente | prompt operacional legado |
| `ontology/auditoria_python_ontologia/audit_ontology_script_notas_de_design.md` | `archive` | `phase_0` | `historical` | `archived` | `manter em ontology/auditoria_python_ontologia/` | manter como historico | notas de design superseded |

#### 5.6.2 Governanca ativa em `ontology/docs/02_domain_knowledge/ontology/00_governance/`

Classificacao bootstrap comum deste bloco:

- `doc_type_proposto`: `handoff` para `HANDOFF.md`; `review` para os demais arquivos de escopo/governanca
- `phase_scope_proposto`: `phase_0`
- `authority_level_proposto`: `supporting`
- `status_proposto`: `current`
- `destino_canonico_planejado`: manter no caminho atual dentro do subsistema `ontology/docs/...`
- `acao_planejada`: manter e referenciar pelo contrato mestre do repo

Arquivos cobertos:

- `ontology/docs/02_domain_knowledge/ontology/00_governance/HANDOFF.md`
- `ontology/docs/02_domain_knowledge/ontology/00_governance/ONTOLOGY-OWL-001_SCOPE.md`
- `ontology/docs/02_domain_knowledge/ontology/00_governance/PONTUACAO-001_MODELO_MINIMO.md`
- `ontology/docs/02_domain_knowledge/ontology/00_governance/PONTUACAO-001_SCOPE.md`
- `ontology/docs/02_domain_knowledge/ontology/00_governance/VOCABULARIO_CANONICO_MINIMO.md`

#### 5.6.3 Relatorios de validacao em `ontology/docs/02_domain_knowledge/ontology/03_validation/`

Classificacao bootstrap comum deste bloco:

- `doc_type_proposto`: `review`
- `phase_scope_proposto`: `phase_0`
- `authority_level_proposto`: `supporting`
- `status_proposto`: `current`
- `destino_canonico_planejado`: manter no caminho atual dentro do subsistema `ontology/docs/...`
- `acao_planejada`: manter

Arquivos cobertos:

- `ontology/docs/02_domain_knowledge/ontology/03_validation/CHECKPOINT-DIMENSOES-001_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/CHECKPOINT-ONTOLOGY-OWL-001_SCOPING_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/CHECKPOINT-PONTUACAO-001_MODELO_MINIMO_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/CONCEPT-DIMENSOES-001_CONSOLIDATION_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/CONCEPT-DIMENSOES-001_CONSOLIDATION_VALIDATION_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/CONCEPT-DIMENSOES-001_TESTS_EXECUTION_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/CONCEPT-DIMENSOES-001_TESTS_VALIDATION_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/CONCEPT-DIMENSOES-001_VALIDATION_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/CONCEPT-GOLEIRO-001_VALIDATION_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/CONCEPT-PAPEIS-001_VALIDATION_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/DH-DIMENSOES-001_HUMAN_VALIDATION_AUDIT_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/DH-PAPEIS-001_CLARIFICACAO_Q8_VALIDATION_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/DH-PAPEIS-001_SEMANTIC_AUDIT_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/DH-PAPEIS-001_VALIDATION_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/DH-PONTUACAO-001_AUDIT_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/MVP-TTL-001_CURRENT_STATE_VALIDATION_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/ONTOLOGY-OWL-001_PROTEGE_VALIDATION_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/ONTOLOGY-OWL-001_SCOPING_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/ONTOLOGY-OWL-001_SCOPING_VALIDATION_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/PONTUACAO-001_MODELAGEM_MINIMA_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/PONTUACAO-001_MODELAGEM_MINIMA_VALIDATION_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/PONTUACAO-001_SCOPING_REPORT.md`
- `ontology/docs/02_domain_knowledge/ontology/03_validation/VOCAB-MIN-001_VALIDATION_REPORT.md`

#### 5.6.4 Decisoes humanas e templates em `ontology/docs/02_domain_knowledge/ontology/04_human_decisions/`

Classificacao bootstrap comum dos arquivos de decisao:

- `doc_type_proposto`: `approval`
- `phase_scope_proposto`: `phase_0`
- `authority_level_proposto`: `supporting`
- `status_proposto`: `current`
- `destino_canonico_planejado`: manter no caminho atual dentro do subsistema `ontology/docs/...`
- `acao_planejada`: manter

Arquivos de decisao cobertos:

- `ontology/docs/02_domain_knowledge/ontology/04_human_decisions/DH-DIMENSOES-001_HUMAN_VALIDATION.md`
- `ontology/docs/02_domain_knowledge/ontology/04_human_decisions/DH-PAPEIS-001.md`
- `ontology/docs/02_domain_knowledge/ontology/04_human_decisions/DH-PAPEIS-001_CLARIFICACAO_Q8.md`
- `ontology/docs/02_domain_knowledge/ontology/04_human_decisions/DH-PONTUACAO-001.md`

Classificacao bootstrap comum dos templates:

- `doc_type_proposto`: `archive`
- `phase_scope_proposto`: `phase_0`
- `authority_level_proposto`: `historical`
- `status_proposto`: `archived`
- `destino_canonico_planejado`: manter no caminho atual dentro do subsistema `ontology/docs/...`
- `acao_planejada`: manter como template historico ate schema especifico do subsistema

Arquivos de template cobertos:

- `ontology/docs/02_domain_knowledge/ontology/04_human_decisions/DH-DIMENSOES-001_HUMAN_VALIDATION_TEMPLATE.md`
- `ontology/docs/02_domain_knowledge/ontology/04_human_decisions/DH-PAPEIS-001_TEMPLATE.md`
- `ontology/docs/02_domain_knowledge/ontology/04_human_decisions/DH-PONTUACAO-001_TEMPLATE.md`

#### 5.6.5 Legado textual em `ontology/files/`

Classificacao bootstrap comum deste bloco:

- `doc_type_proposto`: `archive`
- `phase_scope_proposto`: `phase_0`
- `authority_level_proposto`: `historical`
- `status_proposto`: `archived`
- `destino_canonico_planejado`: manter no caminho atual ate decisao especifica do subsistema
- `acao_planejada`: manter como historico

Arquivos cobertos:

- `ontology/files/Apêndices.md`
- `ontology/files/Decisões Humanas.md`
- `ontology/files/Operacional.md`
- `ontology/files/Rastreabilidade.md`
- `ontology/files/Regras 1–18.md`
- `ontology/files/Regras Ontológicas do Handebol.md`
- `ontology/files/Vocabulário e Taxonomia.md`

#### 5.6.6 Saidas da auditoria Python em `ontology/results_auditoria_python/`

Classificacao bootstrap dos relatorios ativos:

- `doc_type_proposto`: `review`
- `phase_scope_proposto`: `phase_0`
- `authority_level_proposto`: `supporting`
- `status_proposto`: `current`
- `destino_canonico_planejado`: manter no caminho atual no subsistema `ontology/`
- `acao_planejada`: manter

Arquivos ativos cobertos:

- `ontology/results_auditoria_python/00_ESTADO_REAL_AUDITADO.md`
- `ontology/results_auditoria_python/02_AUDITORIA_PYTHON_SPEC.md`
- `ontology/results_auditoria_python/07_blockers_report.md`

Classificacao bootstrap dos historicos superseded:

- `doc_type_proposto`: `archive`
- `phase_scope_proposto`: `phase_0`
- `authority_level_proposto`: `historical`
- `status_proposto`: `archived`
- `destino_canonico_planejado`: manter no caminho atual no subsistema `ontology/`
- `acao_planejada`: manter como historico

Arquivos historicos cobertos:

- `ontology/results_auditoria_python/12345.md`

## 6. Pendencias declaradas para a Etapa 2

Pendencias assumidas explicitamente:

- normalizar do bootstrap para schema definitivo os arquivos do subsistema `ontology/`, que hoje usam metadados locais diferentes do schema planejado para o repo;
- ratificar os `doc_type_proposto` estimados dos documentos que ainda nao possuem frontmatter padrao;
- definir, em `ESQUEMA_METADADOS_DOCUMENTAIS.md`, se documentos derivados de fonte externa receberao um tratamento mais especifico que `review` ou `archive`.

## 7. Criterio de fechamento deste arquivo na Etapa 1

Este `MAPA_DOCUMENTAL.md` deve ser considerado suficiente para a Etapa 1 quando:

- o inventario bootstrap continuar cobrindo todas as entradas Markdown relevantes do repo;
- qualquer mudanca documental posterior vier acompanhada da atualizacao correspondente deste mapa;
- a Etapa 2 absorver este inventario para o schema definitivo sem perder rastreabilidade.
