# Matriz de Testes da Fase 1 Base Estrutural

## Finalidade

Esta matriz deriva apenas os testes obrigatorios da Fase 1, sem misturar
casos de Fase 2 ou Fase 3.

## 1. Testes de schema

| ID | Caso | Resultado esperado |
|---|---|---|
| F1-SCH-001 | banco novo recebe migracao `001_base_structural.sql` | schema criado sem erro |
| F1-SCH-002 | `schema_migrations` existe | tabela presente |
| F1-SCH-003 | `audit_log` existe | tabela presente |
| F1-SCH-004 | `athletes` existe | tabela presente |
| F1-SCH-005 | `competitions` existe | tabela presente |
| F1-SCH-006 | `opponents` existe | tabela presente |
| F1-SCH-007 | `matches` nao existe | tabela ausente |
| F1-SCH-008 | `training_sessions` nao existe | tabela ausente |
| F1-SCH-009 | `attendance` nao existe | tabela ausente |
| F1-SCH-010 | `scout_event_types` nao existe | tabela ausente |
| F1-SCH-011 | `scout_events` nao existe | tabela ausente |
| F1-SCH-012 | `athletes.status` aceita `active` e `inactive` | inserts validos passam |
| F1-SCH-013 | `athletes.status` rejeita valor fora da allowlist | insert falha |
| F1-SCH-014 | `competitions.status` aceita `active` e `inactive` | inserts validos passam |
| F1-SCH-015 | `opponents.status` aceita `active` e `inactive` | inserts validos passam |
| F1-SCH-016 | nomes obrigatorios nao aceitam string vazia | insert falha |
| F1-SCH-017 | `audit_log.operation` rejeita valor fora da allowlist | insert falha |
| F1-SCH-018 | `audit_log` exige pelo menos um entre before/after | insert invalido falha |

## 2. Testes de migracao

| ID | Caso | Resultado esperado |
|---|---|---|
| F1-MIG-001 | migracao roda em banco vazio | sucesso |
| F1-MIG-002 | migracao nao e reaplicada se ja registrada | executor ignora com seguranca |
| F1-MIG-003 | checksum divergente para arquivo ja aplicado | falha explicita |
| F1-MIG-004 | falha no meio da migracao | rollback integral |
| F1-MIG-005 | `schema_migrations` registra `filename`, `checksum_sha256`, `applied_at` | registro correto existe |

## 3. Testes de persistencia

| ID | Caso | Resultado esperado |
|---|---|---|
| F1-PER-001 | criar atleta e reabrir aplicacao | atleta persiste |
| F1-PER-002 | criar competicao e reabrir aplicacao | competicao persiste |
| F1-PER-003 | criar adversario e reabrir aplicacao | adversario persiste |
| F1-PER-004 | editar atleta e reabrir aplicacao | alteracao persiste |
| F1-PER-005 | ativar/inativar cadastro e reabrir aplicacao | status persiste |
| F1-PER-006 | operacoes de cadastro registram `audit_log` | registros existem |

## 4. Testes de backup

| ID | Caso | Resultado esperado |
|---|---|---|
| F1-BKP-001 | criar backup com banco em uso | backup consistente gerado |
| F1-BKP-002 | backup nao copia apenas `.db` de forma cega | mecanismo seguro comprovado |
| F1-BKP-003 | restaurar backup valido | restauracao concluida |
| F1-BKP-004 | `PRAGMA integrity_check` apos restore | retorna `ok` |
| F1-BKP-005 | `PRAGMA foreign_key_check` apos restore | sem violacoes |
| F1-BKP-006 | `schema_migrations` apos restore | consistente |
| F1-BKP-007 | contagens de `athletes`, `competitions`, `opponents` e `audit_log` apos restore | iguais ao estado esperado |
| F1-BKP-008 | restaurar backup em diretorio limpo | sucesso |
| F1-BKP-009 | backup corrompido | falha controlada e rollback do banco anterior |

## 5. Testes de runtime local

| ID | Caso | Resultado esperado |
|---|---|---|
| F1-RT-001 | processo bindado em `127.0.0.1` | sucesso |
| F1-RT-002 | tentativa de bind em `0.0.0.0` | proibida |
| F1-RT-003 | runtime equivalente a `workers=1` | confirmado |
| F1-RT-004 | conexao SQLite usa `foreign_keys=ON` | confirmado |
| F1-RT-005 | conexao SQLite usa `journal_mode=WAL` | confirmado |
| F1-RT-006 | conexao SQLite usa `busy_timeout >= 30000` | confirmado |

## 6. Testes de superficie HTTP

| ID | Caso | Resultado esperado |
|---|---|---|
| F1-HTTP-001 | `GET /` | responde com dashboard minimo |
| F1-HTTP-002 | fluxo de criar atleta | sucesso |
| F1-HTTP-003 | fluxo de criar competicao | sucesso |
| F1-HTTP-004 | fluxo de criar adversario | sucesso |
| F1-HTTP-005 | `POST /admin/backup` | sucesso |
| F1-HTTP-006 | `POST /admin/restore` | sucesso |
| F1-HTTP-007 | rota de treino na Fase 1 | indisponivel |
| F1-HTTP-008 | rota de jogo na Fase 1 | indisponivel |
| F1-HTTP-009 | rota de scout na Fase 1 | indisponivel |
| F1-HTTP-010 | rota de relatorio na Fase 1 | indisponivel |

## Definicao de pronto

A Fase 1 base estrutural so pode ser considerada pronta quando:

- todos os testes F1-SCH passarem;
- todos os testes F1-MIG passarem;
- todos os testes F1-PER passarem;
- todos os testes F1-BKP passarem;
- todos os testes F1-RT passarem;
- nenhum artefato de Fase 2 ou 3 existir no schema ou na superficie HTTP.
