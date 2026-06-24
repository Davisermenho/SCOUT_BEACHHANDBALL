# Revisao: MODELAGEM DO BANCO DE DADOS x Fase 1 Atual

## Finalidade

Este documento compara [MODELAGEM DO BANCO DE DADOS.md](/home/davis/SCOUT_BEACHHANDBALL/MODELAGEM%20DO%20BANCO%20DE%20DADOS.md:1)
com os contratos ativos da Fase 1, para separar:

- o que pode ser reaproveitado;
- o que esta incompativel com o estado atual do repositorio;
- o que ainda falta para implementacao correta.

## Veredito

Status geral:

- `valor historico`: alto
- `valor como contrato ativo da Fase 1`: baixo
- `compatibilidade parcial`: sim
- `apto para guiar implementacao diretamente`: nao

Conclusao:

- o documento de modelagem representa uma linha anterior, centrada em
  `attendance`, `users`, `RBAC`, `event_series` e `events`;
- o repositorio atual ja ratificou outro trilho de execucao, com Fase 1
  restrita a base estrutural comum em SQLite;
- a modelagem historica pode servir como referencia secundaria, mas nao pode
  substituir [ORDEM_EXECUCAO_FASE_1.md](/home/davis/SCOUT_BEACHHANDBALL/ORDEM_EXECUCAO_FASE_1.md:1),
  [PLANO_EXECUCAO_IA_POR_FASES.md](/home/davis/SCOUT_BEACHHANDBALL/PLANO_EXECUCAO_IA_POR_FASES.md:110)
  e [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/home/davis/SCOUT_BEACHHANDBALL/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:118).

## Compatibilidade

### 1. Stack da aplicacao

`MODELAGEM DO BANCO DE DADOS.md`:

- assume caminho de evolucao para DBML, dbdiagram e exportacao posterior para
  PostgreSQL;
- introduz conceitos como `TIMESTAMPTZ`, `RBAC multi-papel`, `app_config` e
  `attendance_history`.

Contrato ativo:

- `Python 3.12+`
- `FastAPI`
- `Jinja2`
- `HTMX`
- `SQLite`
- processo local em `127.0.0.1` com `workers=1`

Veredito:

- **incompativel como stack primaria**;
- **compativel apenas como referencia de modelagem conceitual**.

Fontes:

- [MODELAGEM DO BANCO DE DADOS.md](/home/davis/SCOUT_BEACHHANDBALL/MODELAGEM%20DO%20BANCO%20DE%20DADOS.md:121)
- [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/home/davis/SCOUT_BEACHHANDBALL/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:118)

### 2. Estrutura de pastas

Contrato ativo:

```text
SCOUT_BEACHHANDBALL/
  app/
  data/
    scout_mvp.db
    files/
  backups/
  migrations/
  tests/
```

Veredito:

- a modelagem historica nao conflita diretamente aqui;
- **a estrutura oficial da Fase 1 ja esta definida**.

Fonte:

- [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/home/davis/SCOUT_BEACHHANDBALL/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:159)

### 3. Modelagem correta do banco

`MODELAGEM DO BANCO DE DADOS.md` propoe como entidades centrais:

- `athletes`
- `users`
- `user_roles`
- `user_athlete_links`
- `locations`
- `event_series`
- `events`
- `attendance_responses`
- `attendance_history`
- `response_statuses`
- `event_types`
- `athlete_statuses`
- `role_types`
- `app_config`

Contrato ativo da Fase 1:

- permite apenas a base estrutural comum;
- proibe criar tabelas de jogo, set, shoot-out, scout e atribuicoes funcionais
  por fase nesta etapa.

Veredito:

- `athletes` e reutilizavel;
- `competitions` e `opponents` ja estao definidos no contrato atual;
- `users`, `user_roles`, `user_athlete_links`, `locations`, `event_series`,
  `events`, `attendance_responses`, `attendance_history`, `response_statuses`,
  `event_types`, `athlete_statuses`, `role_types` e `app_config` **nao podem
  ser tratados como escopo automatico da Fase 1**;
- o documento historico **superdimensiona** a Fase 1 atual.

Fontes:

- [MODELAGEM DO BANCO DE DADOS.md](/home/davis/SCOUT_BEACHHANDBALL/MODELAGEM%20DO%20BANCO%20DE%20DADOS.md:140)
- [ORDEM_EXECUCAO_FASE_1.md](/home/davis/SCOUT_BEACHHANDBALL/ORDEM_EXECUCAO_FASE_1.md:25)
- [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/home/davis/SCOUT_BEACHHANDBALL/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:1460)

### 4. SQL pronto do schema

Estado atual:

- o contrato da Fase 1 agora ja possui DDL canônico em
  [migrations/001_base_structural.sql](/home/davis/SCOUT_BEACHHANDBALL/migrations/001_base_structural.sql:1);
- o fechamento tecnico da fase aponta esse arquivo como referencia executavel
  oficial.

Veredito:

- **lacuna resolvida documentalmente**;
- `MODELAGEM DO BANCO DE DADOS.md` continua sem valor como fonte de DDL
  executavel, porque entrega direcao conceitual e nao o SQL final da Fase 1.

Fontes:

- [FECHAMENTO_TECNICO_FASE_1_BASE_ESTRUTURAL.md](/home/davis/SCOUT_BEACHHANDBALL/FECHAMENTO_TECNICO_FASE_1_BASE_ESTRUTURAL.md:89)
- [migrations/001_base_structural.sql](/home/davis/SCOUT_BEACHHANDBALL/migrations/001_base_structural.sql:1)

### 5. Mecanismo de migracao

Estado atual:

- prefixo numerico de tres digitos fechado;
- `schema_migrations` fechado com `filename`, `checksum_sha256` e `applied_at`;
- checksum oficial `sha256`;
- bootstrap e comportamento para banco vazio x banco existente documentados;
- backup preventivo antes de migrar banco nao vazio documentado.

Veredito:

- **lacuna resolvida em nivel de contrato**;
- ainda falta apenas a implementacao executavel do runner, nao a definicao do
  mecanismo.

Fontes:

- [FECHAMENTO_TECNICO_FASE_1_BASE_ESTRUTURAL.md](/home/davis/SCOUT_BEACHHANDBALL/FECHAMENTO_TECNICO_FASE_1_BASE_ESTRUTURAL.md:97)
- [migrations/001_base_structural.sql](/home/davis/SCOUT_BEACHHANDBALL/migrations/001_base_structural.sql:3)

### 6. Tabelas base permitidas

Allowlist oficial da Fase 1:

- `schema_migrations`
- `audit_log`
- `athletes`
- `competitions`
- `opponents`

Estado atual:

- `training_sessions` e `attendance` deixaram de ser ambiguidade nesta fase;
- ambas ficaram explicitamente fora de escopo da migracao inicial.

Veredito:

- **lacuna resolvida documentalmente**;
- a modelagem historica nao pode mais ser usada para reintroduzir tabela de
  treino, presenca, RBAC ou evento na Fase 1.

Fontes:

- [FECHAMENTO_TECNICO_FASE_1_BASE_ESTRUTURAL.md](/home/davis/SCOUT_BEACHHANDBALL/FECHAMENTO_TECNICO_FASE_1_BASE_ESTRUTURAL.md:60)
- [ORDEM_EXECUCAO_FASE_1.md](/home/davis/SCOUT_BEACHHANDBALL/ORDEM_EXECUCAO_FASE_1.md:36)

### 7. Rotina segura de backup/restauracao

Estado atual:

- backup manual assistido e restauracao continuam obrigatorios ja na Fase 1;
- a rotina proibe copia cega do `.db`;
- as validacoes de `integrity_check`, `foreign_key_check`,
  `schema_migrations`, allowlist e contagens esperadas ficaram documentadas;
- nomes canônicos para backup manual e backups preventivos de migracao e
  restauracao ficaram definidos.

Veredito:

- **lacuna resolvida em nivel documental**;
- ainda falta a implementacao executavel e a prova automatizada da rotina.

Fontes:

- [ADR-002-backup-sqlite-wal.md](/home/davis/SCOUT_BEACHHANDBALL/adr/ADR-002-backup-sqlite-wal.md:13)
- [FECHAMENTO_TECNICO_FASE_1_BASE_ESTRUTURAL.md](/home/davis/SCOUT_BEACHHANDBALL/FECHAMENTO_TECNICO_FASE_1_BASE_ESTRUTURAL.md:226)

### 8. Testes automatizados de schema/persistencia

Estado atual:

- a matriz Fase 1-only ja existe e separa schema, migracao, persistencia,
  backup, runtime local e superficie HTTP;
- os testes ainda nao foram implementados no codigo, mas o contrato do que deve
  ser provado ja esta fechado.

Veredito:

- **lacuna resolvida em nivel de especificacao de testes**;
- falta apenas transformar a matriz em testes executaveis.

Fontes:

- [MATRIZ_TESTES_FASE_1_BASE_ESTRUTURAL.md](/home/davis/SCOUT_BEACHHANDBALL/MATRIZ_TESTES_FASE_1_BASE_ESTRUTURAL.md:1)
- [ORDEM_EXECUCAO_FASE_1.md](/home/davis/SCOUT_BEACHHANDBALL/ORDEM_EXECUCAO_FASE_1.md:52)

## O que mais e necessario para implementacao correta

Depois do fechamento tecnico atual, o que ainda falta nao e mais contrato
documental basico. O que ainda falta e implementacao e algumas decisoes
operacionais de baixo nivel:

1. **Runner executavel de migracao**
   - ler `migrations/`
   - calcular `sha256`
   - aplicar em ordem
   - registrar em `schema_migrations`
   - falhar com rollback em divergencia

2. **Bootstrap real da aplicacao**
   - abrir `data/scout_mvp.db`
   - garantir `foreign_keys=ON`
   - garantir `journal_mode=WAL`
   - garantir `busy_timeout >= 30000`
   - registrar o caminho efetivo do banco carregado

3. **Implementacao real de backup/restauracao**
   - usar API segura do SQLite
   - validar backup em conexao separada
   - gerar backup preventivo antes de migrar ou restaurar banco nao vazio
   - restaurar de forma atomica com rollback do estado anterior em falha

4. **Politica executavel da auditoria**
   - definir como `session_id` sera gerado
   - definir em que camada o `audit_log` sera gravado
   - provar que `insert`, `update`, `activate`, `deactivate`, `backup`,
     `restore` e `migration` ficam rastreaveis

5. **Validacoes aplicacionais dos cadastros**
   - decidir politica de duplicidade para atleta, competicao e adversario
   - definir serializacao canonica dos timestamps gerados pela aplicacao
   - padronizar mensagens de erro e comportamento de ativacao/inativacao

6. **Testes automatizados executaveis**
   - transformar a matriz Fase 1-only em `pytest`
   - incluir teste real de schema, persistencia, backup, restore e HTTP
   - provar ambiente limpo e persistencia apos reinicio

## Decisao recomendada

`MODELAGEM DO BANCO DE DADOS.md` deve ser tratado como:

- **documento historico e exploratorio**
- **nao canônico para Fase 1**
- **reaproveitavel apenas por extracao controlada de ideias**

O proximo passo correto nao e implementar a partir dele. O proximo passo
correto e implementar a Fase 1 a partir dos contratos ativos ja fechados:

- [FECHAMENTO_TECNICO_FASE_1_BASE_ESTRUTURAL.md](/home/davis/SCOUT_BEACHHANDBALL/FECHAMENTO_TECNICO_FASE_1_BASE_ESTRUTURAL.md:1)
- [migrations/001_base_structural.sql](/home/davis/SCOUT_BEACHHANDBALL/migrations/001_base_structural.sql:1)
- [MATRIZ_TESTES_FASE_1_BASE_ESTRUTURAL.md](/home/davis/SCOUT_BEACHHANDBALL/MATRIZ_TESTES_FASE_1_BASE_ESTRUTURAL.md:1)
- [pyproject.toml](/home/davis/SCOUT_BEACHHANDBALL/pyproject.toml:1)
