---
doc_id: fechamento-tecnico-fase-1-base-estrutural
doc_type: review
status: current
phase_scope:
  - phase_1
authority_level: supporting
owned_by: fase_1_execution_gate
canonical_path: /docs/05_fases/fase_1/FECHAMENTO_TECNICO_FASE_1_BASE_ESTRUTURAL.md
supersedes: []
superseded_by: null
must_read_before_implementation: false
implementation_ready: false
last_reviewed: "2026-06-24"
---

# Fechamento Tecnico da Fase 1 Base Estrutural

## Finalidade

Este documento fecha o pacote tecnico minimo necessario para iniciar a
implementacao da Fase 1 sem invadir fases posteriores.

Ele nao redefine o escopo completo do MVP. Ele apenas fecha a fundacao
estrutural autorizada para a Fase 1.

Ele consolida:

- stack oficial;
- estrutura de pastas;
- allowlist de tabelas da Fase 1;
- contrato do mecanismo de migracao;
- contrato da trilha minima de auditoria;
- subset HTTP oficial da Fase 1;
- regras operacionais de backup e restauracao.

## Fontes de autoridade

Ordem de leitura obrigatoria:

1. [PROBLEMA_FINAL.md](/docs/01_contexto/PROBLEMA_FINAL.md:1)
2. [MVP.md](/docs/02_produto/MVP.md:1)
3. [ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md](/docs/03_ontologia/ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md:1)
4. [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/docs/04_implementacao/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:1)
5. [PLANO_EXECUCAO_IA_POR_FASES.md](/docs/05_fases/PLANO_EXECUCAO_IA_POR_FASES.md:1)
6. [ORDEM_EXECUCAO_FASE_1.md](/docs/05_fases/fase_1/ORDEM_EXECUCAO_FASE_1.md:1)
7. [ADR-002-backup-sqlite-wal.md](/docs/06_adrs/ADR-002-backup-sqlite-wal.md:1)
8. [ADR-005-cadastros-como-suporte-estrutural.md](/docs/06_adrs/ADR-005-cadastros-como-suporte-estrutural.md:1)

## Stack oficial

- `Python 3.12+`
- `FastAPI` para processo HTTP local
- `Jinja2` para renderizacao HTML server-side
- `HTMX` para interacoes incrementais simples
- `SQLite` como banco local
- `uvicorn` com bind em `127.0.0.1` e configuracao equivalente a `workers=1`

## Estrutura de pastas oficial

```text
SCOUT_BEACHHANDBALL/
  app/
    repositories/
    services/
  data/
    files/
    scout_mvp.db
  backups/
  migrations/
    001_base_structural.sql
  tests/
  pyproject.toml
```

## Allowlist oficial de tabelas da Fase 1

As unicas tabelas permitidas na Fase 1 sao:

- `schema_migrations`
- `audit_log`
- `athletes`
- `competitions`
- `opponents`

## Tabelas explicitamente fora de escopo na Fase 1

Nao podem entrar na migracao `001_base_structural.sql`:

- `matches`
- `match_sets`
- `match_shootouts`
- `match_roster`
- `match_role_assignments`
- `training_sessions`
- `attendance`
- `scout_event_types`
- `scout_events`
- `notes`
- `video_references`
- `match_reopen_authorizations`
- qualquer tabela de `users`, `rbac`, `event_series`, `events`,
  `attendance_responses`, `attendance_history` ou `app_config`

## DDL canônico da Fase 1

O SQL canônico da Fase 1 fica em:

- [migrations/001_base_structural.sql](/home/davis/SCOUT_BEACHHANDBALL/migrations/001_base_structural.sql:1)

Esse arquivo e a referencia executavel da base estrutural comum.

Regra interpretativa:

- se um campo nao foi tornado obrigatorio pelos contratos ativos da Fase 1,
  ele nao deve ser introduzido por inferencia nesta migracao inicial

## Contrato do mecanismo de migracao

### Arquivos

- cada migracao deve ser um arquivo `.sql`
- ordenacao por prefixo numerico crescente de tres digitos
- exemplo: `001_base_structural.sql`

### Checksum

- algoritmo oficial: `sha256`
- o checksum e calculado sobre o conteudo bruto do arquivo

### Formatos temporais

- campos de data e hora em `TEXT` devem usar UTC em formato
  `YYYY-MM-DDTHH:MM:SSZ`
- campos de data sem horario devem usar `YYYY-MM-DD`

### Tabela `schema_migrations`

Campos obrigatorios:

- `filename TEXT PRIMARY KEY`
- `checksum_sha256 TEXT NOT NULL`
- `applied_at TEXT NOT NULL`

### Bootstrap

- se `schema_migrations` nao existir, o executor pode cria-la antes da leitura
  do historico de migracoes
- `001_base_structural.sql` tambem deve conter `CREATE TABLE IF NOT EXISTS
  schema_migrations` para manter o contrato documental fechado no proprio
  arquivo

### Aplicacao

- cada migracao deve rodar em transacao unica com `BEGIN IMMEDIATE`
- o executor aplica cada arquivo exatamente uma vez
- se o arquivo ja constar em `schema_migrations` com checksum diferente, a
  execucao deve falhar explicitamente
- falha parcial implica rollback integral

### Backup preventivo

- se o banco de destino ja existir e nao estiver vazio, deve ser criado backup
  preventivo antes da aplicacao de migracao
- se o banco ainda nao existir ou estiver vazio, o executor pode seguir sem
  backup preventivo, mas deve registrar isso em log
- nome canonico recomendado para backup preventivo de migracao:
  `backups/pre-migration-YYYYMMDD-HHMMSS.db`

## Contrato tecnico da trilha minima de auditoria

Nome oficial da tabela:

- `audit_log`

Campos obrigatorios:

- `id INTEGER PRIMARY KEY`
- `entity_name TEXT NOT NULL`
- `record_id TEXT NOT NULL`
- `operation TEXT NOT NULL`
- `changed_at TEXT NOT NULL`
- `before_state_json TEXT NULL`
- `after_state_json TEXT NULL`
- `reason TEXT NOT NULL`
- `session_id TEXT NOT NULL`

Regras obrigatorias:

- `operation` restrita a:
  - `insert`
  - `update`
  - `activate`
  - `deactivate`
  - `backup`
  - `restore`
  - `migration`
- pelo menos um entre `before_state_json` e `after_state_json` deve existir
- `record_id` e armazenado como texto para suportar ids futuros heterogeneos

Indices minimos:

- `audit_log_entity_record_idx (entity_name, record_id)`
- `audit_log_changed_at_idx (changed_at)`

Politica minima de uso na Fase 1:

- cadastrar atleta, competicao ou adversario gera `insert`
- editar cadastro gera `update`
- ativar/inativar gera `activate` ou `deactivate`
- backup e restauracao geram registro proprio
- execucao de migracao gera registro proprio quando a camada aplicacional
  estiver ativa

## Subset HTTP oficial da Fase 1

Rotas permitidas:

- `GET /`
- `GET /athletes`
- `GET /athletes/new`
- `POST /athletes`
- `GET /athletes/{athlete_id}`
- `GET /athletes/{athlete_id}/edit`
- `POST /athletes/{athlete_id}`
- `POST /athletes/{athlete_id}/deactivate`
- `POST /athletes/{athlete_id}/activate`
- `GET /competitions`
- `GET /competitions/new`
- `POST /competitions`
- `GET /competitions/{competition_id}/edit`
- `POST /competitions/{competition_id}`
- `POST /competitions/{competition_id}/deactivate`
- `POST /competitions/{competition_id}/activate`
- `GET /opponents`
- `GET /opponents/new`
- `POST /opponents`
- `GET /opponents/{opponent_id}/edit`
- `POST /opponents/{opponent_id}`
- `POST /opponents/{opponent_id}/deactivate`
- `POST /opponents/{opponent_id}/activate`
- `POST /admin/backup`
- `POST /admin/restore`
- `GET /admin/backups`

Rotas proibidas na Fase 1:

- qualquer rota de treino
- qualquer rota de jogo
- qualquer rota de scout
- qualquer rota de relatorio
- qualquer rota de comparacao

## Contrato operacional de backup e restauracao

### Backup

- nome canônico:
  - `backups/scout_mvp-YYYYMMDD-HHMMSS.db`
- mecanismo:
  - usar API segura do proprio SQLite, ou equivalente que preserve WAL
- proibido:
  - copia cega apenas do arquivo `.db` durante uso aberto

### Restauracao

- validar backup candidato em conexao separada
- fechar conexoes ativas do banco atual
- criar backup preventivo do estado corrente
- substituir o banco de forma atomica
- reabrir conexao
- executar:
  - `PRAGMA integrity_check`
  - `PRAGMA foreign_key_check`
  - validacao de `schema_migrations`
  - validacao de contagens minimas esperadas
- se a verificacao falhar, restaurar o banco anterior
- nome canonico recomendado para backup preventivo de restauracao:
  `backups/pre-restore-YYYYMMDD-HHMMSS.db`

### Contagens minimas esperadas da Fase 1

Depois de restaurar um banco valido da Fase 1, o sistema deve conseguir
verificar:

- existencia das tabelas allowlisted
- ausencia das tabelas proibidas de Fase 2 e 3
- contagem esperada de registros criada pelo proprio teste executado
  imediatamente antes do backup

## Decisao

Este documento fecha o pacote tecnico minimo necessario para iniciar a
implementacao da Fase 1 base estrutural sem depender de inferencia adicional
sobre stack, schema, escopo de tabelas, backup ou subset HTTP.
