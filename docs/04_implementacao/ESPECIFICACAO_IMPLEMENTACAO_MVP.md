---
doc_id: especificacao-implementacao-mvp
doc_type: contract
status: current
phase_scope:
  - cross_phase
authority_level: operational
owned_by: mvp_implementation_contract
canonical_path: /docs/04_implementacao/ESPECIFICACAO_IMPLEMENTACAO_MVP.md
supersedes: []
superseded_by: null
must_read_before_implementation: true
implementation_ready: false
last_reviewed: "2026-06-24"
---

# Especificacao de Implementacao do MVP

## 1. Finalidade

Este documento transforma o [MVP.md](/docs/02_produto/MVP.md:1) em especificacao de implementacao.

Ele define:

- arquitetura executavel;
- estrutura do projeto;
- modelo de dados implementavel;
- contratos de entrada e saida;
- regras de persistencia;
- telas e rotas;
- migracoes;
- testes;
- criterios tecnicos de entrega por fase.

Este documento nao substitui o [PROBLEMA_FINAL.md](/docs/01_contexto/PROBLEMA_FINAL.md:1). Quando houver conflito, a ordem de autoridade e:

1. `PROBLEMA_FINAL.md`
2. `MVP.md`
3. `ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md`
4. este documento

Para termos de dominio do scout, o documento [ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md](/docs/03_ontologia/ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md:1) e a autoridade semantica dentro do escopo do MVP.

Regra adicional:

- se este documento e uma ADR tecnica divergirem, a implementacao fica bloqueada ate reconciliacao explicita;
- a IA nao pode escolher arbitrariamente entre especificacao e ADR conflitantes.

## 2. Escopo de Implementacao

Esta especificacao cobre apenas o MVP aprovado:

- cadastro de atletas;
- cadastro de competicoes;
- cadastro de adversarios;
- registro de jogos;
- registro de treinos;
- registro de presenca;
- registro de scout pos-jogo;
- historico por atleta;
- historico por competicao;
- historico coletivo por periodo;
- relatorios basicos;
- comparacoes basicas;
- apoio opcional de referencia manual de video.

Fora de escopo:

- visao computacional;
- IA de video;
- dashboards complexos;
- integracoes automaticas com WhatsApp, Google Drive e OneDrive;
- modo puramente client-side como forma oficial de producao.

## 2.1 Definicoes semanticas obrigatorias para implementacao

Esta implementacao deve assumir obrigatoriamente que:

- `jogo` e o confronto completo entre as equipes;
- cada jogo possui dois sets regulares;
- o shoot-out e opcional e separado dos sets;
- o resultado do jogo deve distinguir vitoria por 2 a 0 de vitoria por shoot-out;
- `attendance` pertence a treino;
- presenca e participacao em jogo pertencem a `match_roster`;
- atribuicao funcional de goleira ou linha pertence a `match_role_assignments`, por fase;
- o MVP inicial nao cria valor proprio `specialist`; quando a mesma atleta possuir `court_player` e `goalkeeper` na mesma fase, essa combinacao pode ser interpretada como contexto funcional de especialista;
- `evento de scout` e registro estruturado de jogo, nunca substituto de observacao livre.
- observacao coletiva pertence a `notes`, nao a `scout_event_types`;
- eventos de scout do MVP inicial devem ser mutuamente exclusivos para o fato primario registrado.
- o placar de `match_sets` deve armazenar o resultado oficial final do set, incluindo eventual gol decisivo de Golden Goal.

## 2.2 Estrategia de execucao

Esta especificacao nao deve ser lida como ordem rigida de entregar `100% banco`, depois `100% backend`, depois `100% frontend`.

A estrategia correta para este projeto e:

1. dominio e ontologia;
2. modelo de dados e restricoes;
3. backend e contratos;
4. frontend simples;
5. validacao ponta a ponta.

Regra:

- o banco continua sendo a fundacao estrutural;
- cada entrega deve atravessar banco, backend, frontend e teste em fatia pequena;
- nenhuma tela deve ser considerada valida se o contrato de dados e a persistencia real ainda nao estiverem provados.

Proibicao explicita:

- a implementacao nao pode iniciar pelo frontend;
- a IA nao pode comecar por dashboard, tela bonita ou fluxo visual antes de existir modelo de dados, migracoes, constraints e backend minimo validado.

## 2.3 Contrato de execucao para IA

Para implementacao assistida por IA, este documento deve ser tratado como contrato e nao como inspiracao.

A IA nao pode:

- ampliar escopo;
- criar IA de video;
- criar dashboard complexo;
- trocar SQLite por outra solucao;
- inventar eventos de scout fora da ontologia aprovada;
- misturar handebol de quadra com handebol de areia;
- usar texto livre como estrutura principal de scout;
- avancar de fase sem teste e prova executavel.

## 3. Decisoes Tecnicas Fechadas

## 3.1 Runtime

Implementacao recomendada:

- `Python 3.12+`
- `FastAPI` para o processo local HTTP
- `Jinja2` para renderizacao HTML server-side
- `HTMX` para interacoes incrementais simples
- `SQLite` como banco local

Motivo:

- baixa manutencao;
- stack pequena;
- sem frontend complexo;
- bom encaixe com formularios, relatorios e regras de integridade;
- backup consistente operado pelo processo local com mecanismo compativel com SQLite/WAL.

## 3.2 Topologia da aplicacao

A aplicacao deve rodar assim:

1. um processo local e iniciado na maquina do treinador;
2. esse processo expone uma interface HTTP apenas em `127.0.0.1`;
3. o navegador acessa a interface local;
4. o processo local acessa diretamente o arquivo SQLite;
5. o processo local executa backup, migracao, restauracao e validacoes.

Restricoes obrigatorias de execucao:

- o servidor local deve rodar com `workers=1`;
- o modo de producao nao deve usar multiplos workers para o processo HTTP local;
- o acesso de escrita ao SQLite deve ser serializado pela propria aplicacao;
- a conexao SQLite deve definir `timeout` explicito, com valor inicial recomendado de pelo menos `30` segundos;
- cliques duplicados, submissao repetida de formulario e requisicoes concorrentes locais devem ser tratados sem expor erro bruto de `database is locked` ao usuario.

A aplicacao nao deve depender de:

- armazenamento exclusivo do navegador;
- OPFS como fonte primaria;
- IndexedDB como fonte primaria;
- estado de memoria RAM para persistencia.

## 3.3 Estrutura fisica de dados

Estrutura recomendada:

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

Regras:

- `data/scout_mvp.db` e a fonte primaria local;
- `data/files/` guarda anexos e referencias locais opcionais;
- `backups/` guarda backups consistentes datados do banco;
- `migrations/` guarda SQL versionado;
- `tests/` guarda testes automatizados e fixtures.

## 3.4 Configuracao obrigatoria do processo local

Regras:

- o processo local deve bindar apenas em `127.0.0.1`;
- o processo local nao deve ser exposto em `0.0.0.0`;
- o servidor deve iniciar com configuracao equivalente a `workers=1`;
- o processo deve registrar de forma clara o caminho do banco carregado;
- a aplicacao deve falhar na inicializacao se nao conseguir abrir o banco com `foreign_keys` habilitado;
- a aplicacao deve falhar na inicializacao se detectar modo de persistencia apoiado apenas em armazenamento do navegador.

## 4. Estrutura do Projeto

Estrutura recomendada:

```text
app/
  main.py
  config.py
  db.py
  schemas.py
  services/
    athletes.py
    competitions.py
    opponents.py
    trainings.py
    matches.py
    roster.py
    attendance.py
    scout.py
    reports.py
    backup.py
  repositories/
    athletes.py
    competitions.py
    opponents.py
    trainings.py
    matches.py
    roster.py
    attendance.py
    scout.py
    reports.py
  web/
    routes_dashboard.py
    routes_athletes.py
    routes_competitions.py
    routes_opponents.py
    routes_trainings.py
    routes_matches.py
    routes_scout.py
    routes_media.py
    routes_reports.py
  templates/
  static/
```

## 5. Modulos de Implementacao

## 5.1 Dashboard

Objetivo:

- mostrar atalhos;
- listar ultimos jogos;
- listar ultimos treinos;
- oferecer acesso rapido a backup e restauracao.

Rotas:

- `GET /`

## 5.2 Atletas

Objetivo:

- cadastrar;
- editar;
- ativar;
- inativar;
- consultar historico individual.

Rotas:

- `GET /athletes`
- `GET /athletes/new`
- `POST /athletes`
- `GET /athletes/{athlete_id}`
- `GET /athletes/{athlete_id}/edit`
- `POST /athletes/{athlete_id}`
- `POST /athletes/{athlete_id}/deactivate`
- `POST /athletes/{athlete_id}/activate`

## 5.3 Competicoes

Rotas:

- `GET /competitions`
- `GET /competitions/new`
- `POST /competitions`
- `GET /competitions/{competition_id}/edit`
- `POST /competitions/{competition_id}`
- `POST /competitions/{competition_id}/deactivate`
- `POST /competitions/{competition_id}/activate`

## 5.4 Adversarios

Rotas:

- `GET /opponents`
- `GET /opponents/new`
- `POST /opponents`
- `GET /opponents/{opponent_id}/edit`
- `POST /opponents/{opponent_id}`
- `POST /opponents/{opponent_id}/deactivate`
- `POST /opponents/{opponent_id}/activate`

## 5.5 Treinos

Rotas:

- `GET /trainings`
- `GET /trainings/new`
- `POST /trainings`
- `GET /trainings/{training_id}`
- `GET /trainings/{training_id}/edit`
- `POST /trainings/{training_id}`
- `POST /trainings/{training_id}/attendance`

## 5.6 Jogos

Rotas:

- `GET /matches`
- `GET /matches/new`
- `POST /matches`
- `GET /matches/{match_id}`
- `GET /matches/{match_id}/edit`
- `POST /matches/{match_id}`
- `POST /matches/{match_id}/roster`

## 5.7 Scout

Regra central:

- o fluxo principal do scout e sempre pos-jogo;
- o sistema nao exige captura em tempo real;
- `minute` e opcional;
- `event_category` pertence ao modelo, mas nao deve ser exposto como campo editavel no MVP inicial;
- o backend deve persistir `event_category = NULL` enquanto nao existir vocabulario controlado aprovado para esse campo.

Rotas:

- `GET /matches/{match_id}/scout`
- `POST /matches/{match_id}/scout/events`
- `POST /matches/{match_id}/scout/events/{event_id}`
- `POST /matches/{match_id}/scout/events/{event_id}/delete`
- `GET /scout-event-types`

Regra de superficie:

- o MVP inicial nao deve expor rota operacional para criar novos `scout_event_types`;
- `POST /scout-event-types` fica fora do MVP inicial;
- novos codigos so podem entrar apos aprovacao humana explicita, atualizacao documental do seed canonico e novo congelamento formal de baseline.

## 5.8 Midia Local

Rotas:

- `GET /media/{relative_path:path}`

Regra:

- arquivos locais de video e anexos nao devem ser consumidos pela interface via `file://`;
- o processo local deve servir os arquivos por HTTP local controlado;
- a rota deve aceitar apenas caminhos relativos permitidos dentro de `data/files/`;
- a aplicacao deve bloquear qualquer tentativa de path traversal.

## 5.9 Relatorios e Historicos

Rotas:

- `GET /athletes/{athlete_id}/history`
- `GET /competitions/{competition_id}/history`
- `GET /reports/collective`
- `GET /reports/comparison/matches`
- `GET /reports/comparison/periods`

## 5.10 Backup e Restauracao

Rotas:

- `POST /admin/backup`
- `POST /admin/restore`
- `GET /admin/backups`

## 6. Contratos de Dados

## 6.1 Enumeracoes recomendadas

### `status`

Valores recomendados:

- `active`
- `inactive`

### `attendance.status`

Valores recomendados:

- `present`
- `absent`
- `justified`

Observacao:

- `attendance` fica restrito ao contexto de treino.

### `match_roster.presence_status`

Valores recomendados:

- `present`
- `absent`
- `justified`

### `match_roster.participation_status`

Valores recomendados:

- `played`
- `did_not_play`

Observacao:

- `participation_status` deve ser nulo quando `presence_status` nao for `present`.

### `match_role_assignments.match_phase`

Valores recomendados:

- `set_1`
- `set_2`
- `shootout`

### `match_role_assignments.role`

Valores recomendados:

- `court_player`
- `goalkeeper`

### `matches.result_type`

Valores recomendados:

- `won_2_0`
- `lost_0_2`
- `won_shootout`
- `lost_shootout`

### `matches.completion_status`

Valores recomendados:

- `draft`
- `finalized`

### `scout_event_types.required_role`

Valores recomendados:

- `any_role`
- `goalkeeper`

### `scout_events.match_phase`

Valores recomendados:

- `set_1`
- `set_2`
- `shootout`

### `video_references.source_type`

Valores recomendados:

- `local_file`
- `url`

## 6.2 Tabelas

## `athletes`

Campos:

- `id INTEGER PRIMARY KEY`
- `full_name TEXT NOT NULL`
- `nickname TEXT NULL`
- `status TEXT NOT NULL DEFAULT 'active'`
- `created_at TEXT NOT NULL`
- `updated_at TEXT NOT NULL`

Regras:

- `status` restrito a `active` ou `inactive`
- `full_name` obrigatorio

## `competitions`

Campos:

- `id INTEGER PRIMARY KEY`
- `name TEXT NOT NULL`
- `season TEXT NOT NULL`
- `status TEXT NOT NULL DEFAULT 'active'`
- `location TEXT NULL`
- `start_date TEXT NULL`
- `end_date TEXT NULL`

## `opponents`

Campos:

- `id INTEGER PRIMARY KEY`
- `name TEXT NOT NULL`
- `status TEXT NOT NULL DEFAULT 'active'`
- `city TEXT NULL`
- `notes TEXT NULL`

## `matches`

Campos:

- `id INTEGER PRIMARY KEY`
- `match_date TEXT NOT NULL`
- `competition_id INTEGER NOT NULL`
- `opponent_id INTEGER NOT NULL`
- `completion_status TEXT NOT NULL DEFAULT 'draft'`
- `result_type TEXT NULL`
- `team_sets_won INTEGER NULL`
- `opponent_sets_won INTEGER NULL`
- `notes TEXT NULL`
- `created_at TEXT NOT NULL`
- `updated_at TEXT NOT NULL`

Chaves:

- `FOREIGN KEY (competition_id) REFERENCES competitions(id)`
- `FOREIGN KEY (opponent_id) REFERENCES opponents(id)`

Restricoes obrigatorias:

- `CHECK (completion_status IN ('draft', 'finalized'))`
- `CHECK (result_type IS NULL OR result_type IN ('won_2_0', 'lost_0_2', 'won_shootout', 'lost_shootout'))`
- `CHECK (team_sets_won IS NULL OR team_sets_won IN (0, 1, 2))`
- `CHECK (opponent_sets_won IS NULL OR opponent_sets_won IN (0, 1, 2))`

Regra:

- `matches` representa o confronto completo, e nao um set isolado.
- `draft` significa jogo em preenchimento;
- `finalized` significa jogo apto para historico, comparacao e relatorio;
- relatorios e comparacoes devem usar apenas jogos `finalized` por padrao.
- um jogo `finalized` so pode voltar a `draft` por fluxo controlado de reabertura com rastreabilidade;
- alteracoes estruturais em jogo `finalized` devem ser bloqueadas fora desse fluxo.
- `team_sets_won` e `opponent_sets_won` devem ser derivados de `match_sets` no momento da finalizacao, e nao digitados como fonte factual independente;
- alteracoes factuais em `matches` exigem reabertura controlada: `match_date`, `competition_id`, `opponent_id`, `result_type`, `team_sets_won`, `opponent_sets_won`, `completion_status`;
- `notes` de jogo podem ser editadas apos finalizacao sem reabertura, desde que a trilha de auditoria minima seja registrada.

## `match_sets`

Campos:

- `id INTEGER PRIMARY KEY`
- `match_id INTEGER NOT NULL`
- `set_number INTEGER NOT NULL`
- `set_decision_type TEXT NULL`
- `team_score INTEGER NOT NULL`
- `opponent_score INTEGER NOT NULL`

Chaves e restricoes:

- `FOREIGN KEY (match_id) REFERENCES matches(id) ON DELETE RESTRICT`
- `UNIQUE(match_id, set_number)`
- `CHECK (set_number IN (1, 2))`
- `CHECK (set_decision_type IS NULL OR set_decision_type IN ('regular_time', 'golden_goal'))`
- `CHECK (team_score >= 0)`
- `CHECK (opponent_score >= 0)`
- `CHECK (team_score <> opponent_score)`

Regra:

- todo jogo do MVP deve possuir exatamente dois sets regulares registrados.
- o placar armazenado em `match_sets` e o placar oficial final do set, incluindo eventual gol decisivo de Golden Goal;
- `set_decision_type` pode permanecer `NULL` enquanto o jogo estiver `draft`;
- jogo `finalized` exige `set_decision_type` preenchido para os dois sets;
- `set_decision_type = regular_time` significa encerramento no tempo regular;
- `set_decision_type = golden_goal` significa encerramento por gol decisivo apos igualdade no tempo regular;
- set com `set_decision_type = golden_goal` deve manter placar final nao empatado e diferenca absoluta compativel com o gol decisivo final, isto e, `ABS(team_score - opponent_score)` igual a `1` ou `2`;
- Golden Goal decide set; shoot-out decide o jogo apenas apos sets vencidos em 1-1.

## `match_shootouts`

Campos:

- `id INTEGER PRIMARY KEY`
- `match_id INTEGER NOT NULL`
- `team_score INTEGER NOT NULL`
- `opponent_score INTEGER NOT NULL`

Chaves e restricoes:

- `FOREIGN KEY (match_id) REFERENCES matches(id) ON DELETE RESTRICT`
- `UNIQUE(match_id)`
- `CHECK (team_score >= 0)`
- `CHECK (opponent_score >= 0)`
- `CHECK (team_score <> opponent_score)`

Regra:

- `match_shootouts` so existe para jogos resolvidos por shoot-out.

## `match_roster`

Campos:

- `id INTEGER PRIMARY KEY`
- `match_id INTEGER NOT NULL`
- `athlete_id INTEGER NOT NULL`
- `presence_status TEXT NOT NULL DEFAULT 'present'`
- `participation_status TEXT NULL`
- `notes TEXT NULL`

Chaves e restricoes:

- `FOREIGN KEY (match_id) REFERENCES matches(id) ON DELETE RESTRICT`
- `FOREIGN KEY (athlete_id) REFERENCES athletes(id) ON DELETE RESTRICT`
- `UNIQUE(match_id, athlete_id)`
- `CHECK (presence_status IN ('present', 'absent', 'justified'))`
- `CHECK (participation_status IS NULL OR participation_status IN ('played', 'did_not_play'))`
- `CHECK ((presence_status = 'present') OR (participation_status IS NULL))`

Regra:

- esta e a fonte oficial do elenco do jogo;
- a mesma estrutura tambem registra a presenca e a participacao final do atleta no contexto do jogo;
- o sistema nao deve usar `attendance` para presenca de jogo.

## `match_role_assignments`

Campos:

- `id INTEGER PRIMARY KEY`
- `match_id INTEGER NOT NULL`
- `athlete_id INTEGER NOT NULL`
- `match_phase TEXT NOT NULL`
- `role TEXT NOT NULL`

Chaves e restricoes:

- `FOREIGN KEY (match_id) REFERENCES matches(id) ON DELETE RESTRICT`
- `FOREIGN KEY (athlete_id) REFERENCES athletes(id) ON DELETE RESTRICT`
- `FOREIGN KEY (match_id, athlete_id) REFERENCES match_roster(match_id, athlete_id) ON DELETE RESTRICT`
- `UNIQUE(match_id, athlete_id, match_phase, role)`
- `CHECK (match_phase IN ('set_1', 'set_2', 'shootout'))`
- `CHECK (role IN ('court_player', 'goalkeeper'))`

Regra:

- esta estrutura registra atribuicoes funcionais contextuais;
- esta estrutura registra atuacao efetiva na fase, e nao designacao prevista;
- a mesma atleta pode possuir mais de uma atribuicao no mesmo jogo;
- a mesma atleta pode possuir mais de uma atribuicao na mesma fase;
- a atribuicao deve pertencer a atleta que exista no `match_roster` do mesmo jogo;
- a atribuicao exige `presence_status = present` e `participation_status = played` no `match_roster` correspondente;
- atleta ausente ou `did_not_play` nao pode possuir atribuicao funcional;
- atribuicoes com `match_phase = shootout` so sao validas quando o jogo tiver shoot-out;
- ela nao substitui `match_roster`, apenas complementa a validacao funcional do scout.

## `training_sessions`

Campos:

- `id INTEGER PRIMARY KEY`
- `training_date TEXT NOT NULL`
- `title TEXT NOT NULL`
- `objective TEXT NULL`
- `notes TEXT NULL`
- `created_at TEXT NOT NULL`
- `updated_at TEXT NOT NULL`

## `attendance`

Campos:

- `id INTEGER PRIMARY KEY`
- `athlete_id INTEGER NOT NULL`
- `training_session_id INTEGER NOT NULL`
- `status TEXT NOT NULL`
- `notes TEXT NULL`

Chaves:

- `FOREIGN KEY (athlete_id) REFERENCES athletes(id) ON DELETE RESTRICT`
- `FOREIGN KEY (training_session_id) REFERENCES training_sessions(id) ON DELETE RESTRICT`

Restricoes obrigatorias:

- `CHECK (status IN ('present', 'absent', 'justified'))`

Indices recomendados:

- `INDEX attendance_athlete_idx (athlete_id)`
- `INDEX attendance_training_idx (training_session_id)`

## `scout_event_types`

Campos:

- `id INTEGER PRIMARY KEY`
- `code TEXT NOT NULL UNIQUE`
- `label TEXT NOT NULL`
- `scope_mode TEXT NOT NULL`
- `phase_scope TEXT NOT NULL`
- `required_role TEXT NOT NULL DEFAULT 'any_role'`
- `requires_played_status INTEGER NOT NULL DEFAULT 1`
- `status TEXT NOT NULL DEFAULT 'active'`

Regra:

- a UI de scout deve usar lista fechada vinda desta tabela;
- o conjunto inicial ativo de `scout_event_types` deve ser revisado e aprovado pelo treinador antes do uso produtivo;
- novos codigos nao podem nascer por digitacao livre durante o lancamento do scout.
- a aprovacao so e considerada valida quando registrada em artefato humano da Fase 0.

Restricoes obrigatorias:

- `CHECK (scope_mode IN ('individual_only', 'collective_only'))`
- `CHECK (phase_scope IN ('regular_play', 'shootout_only', 'any_match_phase'))`
- `CHECK (required_role IN ('any_role', 'goalkeeper'))`
- `CHECK (requires_played_status IN (0, 1))`

## `scout_events`

Campos:

- `id INTEGER PRIMARY KEY`
- `match_id INTEGER NOT NULL`
- `athlete_id INTEGER NULL`
- `match_phase TEXT NOT NULL`
- `event_type TEXT NOT NULL`
- `event_category TEXT NULL`
- `minute INTEGER NULL`
- `notes TEXT NULL`
- `created_at TEXT NOT NULL`

Chaves e restricoes:

- `FOREIGN KEY (match_id) REFERENCES matches(id) ON DELETE RESTRICT`
- `FOREIGN KEY (event_type) REFERENCES scout_event_types(code) ON DELETE RESTRICT`
- `CHECK (match_phase IN ('set_1', 'set_2', 'shootout'))`
- `CHECK (minute IS NULL OR minute >= 0)`
- `CHECK (event_category IS NULL)`

Observacao:

- `match_id` deve sempre apontar para jogo real existente;
- `athlete_id` pode ser nulo para scout coletivo;
- quando `athlete_id` estiver preenchido, o banco deve validar que o atleta pertence ao `match_roster` do jogo, com `presence_status = present` e `participation_status = played`;
- quando `event_type` exigir papel de goleira, o banco deve validar atribuicao `goalkeeper` em `match_role_assignments` para o mesmo jogo, atleta e fase;
- quando `event_type` exigir `phase_scope = shootout_only`, o banco deve validar `match_phase = shootout`;
- quando `event_type` exigir `phase_scope = regular_play`, o banco deve validar `match_phase IN ('set_1', 'set_2')`;
- quando `match_phase = shootout`, o banco deve validar que o jogo possui shoot-out real;
- essa validacao deve ser implementada por `TRIGGER` SQLite explicito.
- `event_category` deve permanecer `NULL` no MVP inicial, salvo futura lista controlada aprovada.
- quando `athlete_id` for nulo, o `event_type` deve estar marcado como `collective_only`;
- quando `athlete_id` estiver preenchido, o `event_type` deve estar marcado como `individual_only`.

## `notes`

Campos:

- `id INTEGER PRIMARY KEY`
- `match_id INTEGER NULL`
- `training_session_id INTEGER NULL`
- `athlete_id INTEGER NULL`
- `scout_event_id INTEGER NULL`
- `content TEXT NOT NULL`
- `created_at TEXT NOT NULL`

Chaves:

- `FOREIGN KEY (match_id) REFERENCES matches(id) ON DELETE RESTRICT`
- `FOREIGN KEY (training_session_id) REFERENCES training_sessions(id) ON DELETE RESTRICT`
- `FOREIGN KEY (athlete_id) REFERENCES athletes(id) ON DELETE RESTRICT`
- `FOREIGN KEY (scout_event_id) REFERENCES scout_events(id) ON DELETE RESTRICT`

Restricao obrigatoria:

- `CHECK ((match_id IS NOT NULL) OR (training_session_id IS NOT NULL) OR (athlete_id IS NOT NULL) OR (scout_event_id IS NOT NULL))`

## `video_references`

Campos:

- `id INTEGER PRIMARY KEY`
- `match_id INTEGER NULL`
- `athlete_id INTEGER NULL`
- `scout_event_id INTEGER NULL`
- `source_type TEXT NOT NULL`
- `path_or_url TEXT NOT NULL`
- `time_reference TEXT NULL`
- `notes TEXT NULL`

## `match_reopen_authorizations`

Campos:

- `id INTEGER PRIMARY KEY`
- `match_id INTEGER NOT NULL UNIQUE`
- `reason TEXT NOT NULL`
- `session_id TEXT NOT NULL`
- `created_at TEXT NOT NULL`

Chaves:

- `FOREIGN KEY (match_id) REFERENCES matches(id) ON DELETE RESTRICT`

Regra:

- esta e uma estrutura tecnica de controle, nao uma entidade de produto;
- ela autoriza deterministicamente o fluxo `reopen_to_draft`;
- deve existir apenas durante a janela transacional de reabertura e recorrecao do jogo.

## 7. Configuracao do SQLite

Ao abrir conexao, a aplicacao deve executar:

```sql
PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
PRAGMA busy_timeout = 30000;
```

Regras:

- `foreign_keys` deve ser habilitado em toda conexao;
- qualquer teste de integridade deve falhar se `foreign_keys` estiver desligado;
- migracoes devem assumir `foreign_keys = ON`;
- `busy_timeout` deve ser configurado para reduzir falhas por contencao momentanea de escrita;
- a configuracao de conexao da aplicacao deve refletir o mesmo timeout definido no banco.

## 8. SQL Inicial Minimo

As migracoes devem seguir o particionamento por fase.

O arquivo `migrations/001_base_structural.sql` deve conter:

1. criacao das tabelas base comuns;
2. `CHECK`, `UNIQUE` e `FOREIGN KEY` estruturais da Fase 1;
3. indices minimos da Fase 1;
4. criacao da tabela `schema_migrations`.

Os artefatos de jogo devem entrar nas migracoes da Fase 2.

Os artefatos de scout devem entrar nas migracoes da Fase 3.

O arquivo de seed do scout deve ser criado apenas na Fase 3, por exemplo:

- `migrations/005_seed_scout_types.sql`

O projeto deve incluir desde a Fase 1 um mecanismo simples e testado de migracao versionada por arquivos SQL.

Requisitos minimos do mecanismo de migracao:

- tabela `schema_migrations` com identificador unico da migracao aplicada;
- executor de migracao aplica cada arquivo versionado exatamente uma vez, validando checksum e falhando se houver divergencia;
- falha explicita se alguma migracao nao puder ser aplicada por completo;
- teste automatizado que constroi um banco limpo do zero e chega ao schema esperado.

Triggers obrigatorios por fase:

Fase 2:

- `trg_matches_require_valid_finalization`
- `trg_match_shootouts_require_shootout_result`
- `trg_match_sets_require_valid_decision_type`
- `trg_finalized_matches_block_structural_mutation`
- `trg_match_role_assignments_require_roster_membership`
- `trg_match_role_assignments_require_shootout_consistency`

Fase 3:

- `trg_scout_events_require_played_roster_member`
- `trg_scout_event_types_block_semantic_mutation_when_used`

Responsabilidade:

- abortar `INSERT` ou `UPDATE` em `scout_events` quando `athlete_id` nao for nulo e nao existir linha correspondente em `match_roster` para o mesmo `match_id`, com `presence_status = present` e `participation_status = played`;
- abortar `INSERT` ou `UPDATE` em `scout_events` quando o `event_type` exigir `required_role = goalkeeper` e nao existir atribuicao `goalkeeper` em `match_role_assignments` para a mesma atleta, jogo e fase;
- abortar `INSERT` ou `UPDATE` em `match_role_assignments` quando o par `(match_id, athlete_id)` nao existir em `match_roster`;
- abortar `INSERT` ou `UPDATE` em `match_role_assignments` quando o atleta estiver no elenco com `presence_status != present` ou `participation_status != played`;
- abortar `INSERT` ou `UPDATE` em `match_role_assignments` com `match_phase = shootout` quando o jogo nao possuir shoot-out real;
- abortar `INSERT` ou `UPDATE` em `scout_events` com `match_phase = shootout` quando o jogo nao possuir shoot-out real;
- abortar `INSERT` ou `UPDATE` em `match_sets` com `set_decision_type = golden_goal` quando `ABS(team_score - opponent_score)` nao estiver em `(1, 2)`;
- abortar `INSERT` ou `UPDATE` que tente finalizar jogo sem dois sets, com sets empatados, com soma de sets inconsistente com `result_type` ou com uso indevido de shoot-out;
- abortar finalizacao de jogo quando algum set estiver com `set_decision_type` nulo;
- abortar `INSERT` ou `UPDATE` em `match_shootouts` quando o jogo associado nao for de tipo `won_shootout` ou `lost_shootout`.
- abortar `INSERT`, `UPDATE` ou `DELETE` em `match_sets`, `match_shootouts`, `match_roster` e `match_role_assignments` quando o jogo associado estiver `finalized`, salvo fluxo controlado de reabertura para `draft`;
- abortar `UPDATE` de campos factuais em `matches` quando o jogo estiver `finalized`, salvo fluxo controlado de reabertura para `draft`;
- abortar mutacao estrutural em jogo `finalized` quando nao existir autorizacao correspondente em `match_reopen_authorizations`;
- abortar alteracao semantica de `scout_event_types` ja utilizado em `scout_events`, permitindo apenas mudanca de `label` e `status`.

Exemplo de tipos iniciais:

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

Os `code` devem ser canonicos e estaveis. O `label` pode mudar para exibicao sem quebrar historico.

Metadados minimos obrigatorios por tipo inicial:

- `scope_mode`: `individual_only` ou `collective_only`
- `phase_scope`: `regular_play`, `shootout_only` ou `any_match_phase`
- `required_role`: `any_role` ou `goalkeeper`
- `requires_played_status`: `0` ou `1`

Regra do seed inicial:

- os quinze codigos canonicos aprovados para o MVP inicial devem nascer ativos como `individual_only`;
- `collective_only` permanece previsto no schema apenas para evolucao futura com nova aprovacao humana;
- observacoes coletivas do MVP inicial continuam fora de `scout_event_types` e seguem em `notes`.

## 9. Backup e Restauracao

## 9.1 Principio

Backup nao pode depender do navegador. Ele deve ser executado pelo processo local da aplicacao.

## 9.2 Regras

- backup manual assistido deve existir desde a Fase 1;
- backup automatico pode ser adicionado depois, mas nao substitui o manual assistido;
- restauracao basica deve existir desde a Fase 1;
- antes de qualquer migracao, a aplicacao deve criar um backup preventivo do banco.

Regras obrigatorias para SQLite em modo WAL:

- o processo local nao deve copiar apenas o arquivo principal do banco de forma cega enquanto houver transacao aberta;
- antes do backup, a aplicacao deve garantir estado consistente do banco;
- o caminho preferencial e usar mecanismo seguro do proprio SQLite para backup ou executar checkpoint controlado antes da gravacao do artefato;
- qualquer estrategia adotada deve ser testada com banco em uso real e restauracao completa;
- backup que nao provar leitura integra apos restauracao, `integrity_check`, `foreign_key_check` e contagens minimas esperadas nao conta como valido.

## 9.3 Formato

Nome recomendado:

```text
backups/scout_mvp-YYYYMMDD-HHMMSS.db
```

## 9.4 Fluxos

### Backup manual assistido

1. usuario clica em `Criar backup`;
2. processo local executa rotina segura de backup compativel com SQLite e WAL;
3. processo local grava o backup consistente em `backups/`;
4. sistema confirma sucesso e lista o arquivo gerado.

### Restauracao basica

1. usuario escolhe um arquivo de backup listado;
2. sistema valida o backup candidato em conexao separada;
3. sistema fecha as conexoes ativas do banco atual;
4. sistema cria backup preventivo do estado atual;
5. sistema substitui o banco atual pelo backup selecionado de forma atomica em ambiente controlado;
6. sistema reabre a conexao;
7. sistema executa `PRAGMA integrity_check`, `PRAGMA foreign_key_check`, validacao de `schema_migrations` e contagens minimas esperadas;
8. se a verificacao falhar, sistema restaura o banco anterior e registra a falha.

## 9.5 Retencao inicial

Recomendacao inicial:

- manter os ultimos 20 backups locais;
- permitir limpeza manual posterior.

## 10. Telas e Componentes

## 10.1 Dashboard

Componentes:

- ultimos jogos;
- ultimos treinos;
- atalhos de cadastro;
- botao de backup;
- lista de backups recentes.

## 10.2 Cadastro de atleta

Campos:

- nome completo;
- apelido;
- status.

## 10.3 Cadastro de competicao

Campos:

- nome;
- temporada;
- status;
- local;
- inicio;
- fim.

## 10.4 Cadastro de adversario

Campos:

- nome;
- status;
- cidade;
- observacoes.

## 10.5 Formulario de treino

Blocos:

- dados do treino;
- lista de atletas;
- presenca;
- observacoes.

## 10.6 Formulario de jogo

Blocos:

- dados do jogo;
- resultado canonico do confronto;
- sets regulares;
- shoot-out opcional;
- elenco oficial;
- presenca do jogo no proprio `match_roster`;
- observacoes gerais.

## 10.7 Tela de scout

Blocos:

- resumo do jogo;
- seletor de atleta do elenco;
- seletor de tipo de evento;
- campo `minute` opcional;
- observacoes;
- lista de eventos lancados.

Regras de UX:

- formulario deve ser rapido;
- o treinador deve conseguir registrar o scout principal sem preencher `minute`;
- `event_category` nao deve ser exibido como campo editavel no MVP inicial;
- o backend deve gravar `event_category = NULL` no MVP inicial;
- o treinador deve conseguir registrar observacao coletiva em `notes` sem transformar isso em `event_type`;
- a tela deve deixar visivel que o fluxo e pos-jogo.

## 10.8 Historico do atleta

Filtros:

- periodo;
- competicao;
- tipo de registro.

Blocos:

- treinos;
- jogos;
- presencas;
- eventos de scout;
- notas;
- referencias de video.

Regra de apresentacao:

- fatos estruturados devem aparecer separados de observacoes interpretativas do treinador.

## 10.9 Historico coletivo

Filtros:

- periodo;
- competicao.

Blocos:

- jogos no recorte;
- presenca agregada;
- consolidado simples de scout.

Regra de apresentacao:

- o consolidado coletivo deve operar sobre codigos canonicos de scout, e nao sobre texto livre.

## 10.10 Comparacao

Modos:

- jogo vs jogo;
- periodo vs periodo;
- atleta vs atleta em recortes diferentes.

Regra:

- comparacao por periodo deve ser apenas lado a lado de relatorios simples;
- nao implementar mecanismo de BI dinamico.

## 11. Contratos de Entrada

## 11.1 Criar atleta

Payload logico:

```json
{
  "full_name": "Nome do Atleta",
  "nickname": "Apelido",
  "status": "active"
}
```

## 11.2 Criar jogo

```json
{
  "match_date": "2026-06-17",
  "competition_id": 1,
  "opponent_id": 3,
  "completion_status": "finalized",
  "result_type": "won_shootout",
  "sets": [
    {
      "set_number": 1,
      "set_decision_type": "regular_time",
      "team_score": 18,
      "opponent_score": 20
    },
    {
      "set_number": 2,
      "set_decision_type": "golden_goal",
      "team_score": 19,
      "opponent_score": 17
    }
  ],
  "shootout": {
    "team_score": 7,
    "opponent_score": 6
  },
  "notes": "Observacoes gerais"
}
```

Regra:

- `team_sets_won` e `opponent_sets_won` devem ser derivados pelo backend a partir de `match_sets` no momento da finalizacao;
- o contrato de entrada nao deve tratar esses campos como digitacao livre independente.

## 11.3 Definir elenco do jogo

```json
{
  "match_id": 10,
  "roster": [
    {
      "athlete_id": 1,
      "presence_status": "present",
      "participation_status": "played"
    },
    {
      "athlete_id": 2,
      "presence_status": "present",
      "participation_status": "did_not_play"
    }
  ]
}
```

## 11.3.1 Definir atribuicoes funcionais por fase

```json
{
  "match_id": 10,
  "assignments": [
    {
      "athlete_id": 1,
      "match_phase": "set_1",
      "role": "goalkeeper"
    },
    {
      "athlete_id": 1,
      "match_phase": "set_1",
      "role": "court_player"
    },
    {
      "athlete_id": 3,
      "match_phase": "shootout",
      "role": "goalkeeper"
    }
  ]
}
```

## 11.4 Registrar presenca de treino

```json
{
  "athlete_id": 1,
  "training_session_id": 8,
  "status": "present",
  "notes": null
}
```

## 11.5 Registrar scout individual

```json
{
  "match_id": 10,
  "athlete_id": 1,
  "match_phase": "set_1",
  "event_type": "goal_spin_shot",
  "event_category": null,
  "minute": null,
  "notes": "lado direito"
}
```

## 11.6 Registrar observacao coletiva

```json
{
  "match_id": 10,
  "training_session_id": null,
  "athlete_id": null,
  "scout_event_id": null,
  "content": "saida de bola precipitada no inicio do segundo set"
}
```

Regra:

- observacao coletiva do MVP inicial deve usar `notes`;
- ela nao entra em contagem automatica comparativa de scout.

## 12. Regras de Servico

## 12.1 Atletas

- nao deletar fisicamente atleta com historico;
- usar `status = inactive`.

## 12.2 Competicoes e adversarios

- nao deletar fisicamente se houver uso;
- esconder inativos por padrao nas telas;
- permitir consulta de inativos.

## 12.3 Jogos

- um jogo so pode ser considerado pronto para scout quando o elenco oficial estiver salvo;
- o jogo pode existir sem scout;
- o jogo nao deve exigir minutagem para ser considerado completo.

## 12.4 Elenco do jogo

- `match_roster` e a fonte unica para presenca e participacao no contexto do jogo;
- um atleta ausente no `match_roster` nao pode ter `participation_status` preenchido;
- um atleta com `participation_status = played` ou `did_not_play` deve possuir `presence_status = present`;
- o sistema nao deve manter uma segunda fonte paralela de presenca de jogo fora do `match_roster`.

## 12.5 Scout

- `event_type` sempre vem de lista controlada;
- `minute` opcional;
- `event_category` nao deve aparecer como campo editavel no MVP inicial;
- o backend deve persistir `event_category = NULL` no MVP inicial;
- scout individual exige atleta do `match_roster`;
- todos os quinze `event_type` ativos do seed inicial devem estar marcados como `individual_only`;
- `collective_only` permanece reservado no schema para evolucao futura, sem codigo ativo no MVP inicial;
- observacao coletiva do MVP inicial deve usar `notes`;
- o seed inicial do MVP nao contem `event_type` coletivo.

## 12.6 Presenca

- `attendance` fica restrito a treinos;
- presenca de jogo deve ser registrada em `match_roster`;
- o banco deve recusar presenca de treino sem `training_session_id`.

## 12.7 Politica de edicao e rastreabilidade

- cadastros base podem ser editados sem perda do identificador estavel;
- registros historicos de treino, jogo, elenco e scout podem ser corrigidos, mas a aplicacao deve manter rastreabilidade minima;
- exclusao fisica de entidades com historico nao e permitida no fluxo operacional;
- alteracoes que mudem resultado do jogo, elenco ou scout devem ser registradas com evidencia minima de que houve atualizacao;
- a implementacao pode usar log simples, tabela de auditoria minima ou trilha equivalente, desde que a alteracao permaneca verificavel;
- campos livres de observacao podem ser editados, mas nao podem apagar a estrutura factual do registro.
- a partir da Fase 2, qualquer registro historico editavel de jogo ou treino deve deixar trilha minima de alteracao;
- jogo `finalized` nao pode sofrer alteracao estrutural direta;
- para corrigir jogo `finalized`, a aplicacao deve executar fluxo explicito `reopen_to_draft`, registrar essa reabertura e somente depois permitir nova finalizacao coerente.
- o fluxo `reopen_to_draft` deve criar autorizacao tecnica persistida em `match_reopen_authorizations` antes da transicao para `draft`.

Fluxo obrigatorio de servico para `reopen_to_draft`:

1. carregar estado atual completo do jogo, sets, shoot-out, elenco e atribuicoes por fase;
2. registrar auditoria previa com `before_state_json`, `reason` e `session_id`;
3. inserir autorizacao tecnica em `match_reopen_authorizations` para o `match_id`;
4. executar a transicao controlada de `completion_status = finalized` para `draft`;
5. aplicar as correcoes estruturais autorizadas;
6. revalidar invariantes do jogo;
7. concluir com nova finalizacao coerente ou executar rollback integral se qualquer etapa falhar;
8. registrar auditoria final do estado resultante e encerrar a autorizacao tecnica.

Regra:

- os triggers de bloqueio devem reconhecer o fluxo autorizado pela existencia da linha correspondente em `match_reopen_authorizations` na mesma transacao de servico;
- apos a nova finalizacao, a autorizacao tecnica deve ser considerada consumida e nao pode continuar habilitando mutacoes;
- qualquer nova alteracao em `match_sets`, `match_shootouts`, `match_roster`, `match_role_assignments` ou campos factuais de `matches` deve falhar sem nova autorizacao tecnica;
- a IA nao pode inventar outro mecanismo de autorizacao fora desse contrato.

Contrato minimo da trilha de auditoria:

- `entity_name`
- `record_id`
- `operation`
- `changed_at`
- `before_state_json`
- `after_state_json`
- `reason`
- `session_id`

Observacao:

- como o MVP inicial nao define autenticacao multiusuario, `session_id` funciona como identificador minimo do operador ou sessao local.

## 12.8 Contrato transacional minimo

Operacoes abaixo devem ocorrer dentro de transacao unica com `BEGIN IMMEDIATE` e `COMMIT`, ou equivalente com rollback integral em falha:

- criar ou atualizar jogo junto com `match_sets`, `match_shootouts`, `match_roster`, `match_role_assignments` e transicao para `completion_status = finalized`;
- reabrir jogo `finalized` para `draft` com criacao previa de `match_reopen_authorizations`, antes de correcao estrutural;
- aplicar migracao SQL.

Regra:

- qualquer falha intermediaria deve resultar em rollback completo;
- nao e aceitavel persistir apenas parte de jogo, sets, elenco ou shoot-out em operacao de finalizacao;
- nao e aceitavel persistir autorizacao de reabertura sem a respectiva transacao completa de reabertura e recorrecao;
- nao e aceitavel registrar auditoria de reabertura depois da alteracao do jogo;
- testes devem provar falha controlada no meio da transacao sem estado parcial invalido.

## 12.9 Fluxo de restauracao

Restauracao de backup nao deve ser tratada como transacao SQL comum sobre o proprio arquivo que sera substituido.

Fluxo obrigatorio:

1. validar o backup candidato;
2. fechar conexoes ativas do banco atual;
3. preservar o banco atual como rollback candidate;
4. substituir o banco atual pelo artefato restaurado de forma controlada;
5. reabrir conexoes;
6. executar `PRAGMA integrity_check`, `PRAGMA foreign_key_check`, validacao de `schema_migrations` e contagens minimas esperadas;
7. se a verificacao falhar, restaurar o banco anterior e registrar a falha.

## 13. Queries Principais

## 13.1 Historico do atleta

Deve consolidar:

- jogos em que o atleta esta no `match_roster`;
- presencas em treino;
- presenca e participacao em jogo vindas do `match_roster`;
- eventos de scout vinculados;
- notas;
- referencias de video.

## 13.2 Historico coletivo

Deve agregar por filtros:

- periodo;
- competicao.

Saidas minimas:

- quantidade de jogos;
- quantidade de treinos;
- presenca agregada;
- contagem simples por tipo de scout.

Criterio minimo de aceitacao semantica:

- o historico coletivo deve distinguir jogos por resultado canonico;
- o historico coletivo deve permitir leitura por competicao e por periodo sem depender de abrir atleta por atleta;
- o historico coletivo deve usar apenas contagens de codigos canonicos ou fatos estruturados equivalentes;
- texto livre nao pode ser a base primaria do consolidado coletivo.

## 13.3 Comparacao jogo vs jogo

Saidas minimas:

- resultado canonico;
- placar dos sets;
- shoot-out, quando existir;
- elenco;
- totais simples por tipo de scout;
- observacoes.

## 13.4 Comparacao periodo vs periodo

Saidas minimas:

- dois relatorios coletivos simples lado a lado;
- sem agregador dinamico de BI;
- sem editor livre de metricas.

## 14. Mapeamento MVP -> Implementacao

Regra de entrega:

- cada fase deve produzir uma fatia vertical utilizavel;
- isso significa incluir, no minimo, os elementos de banco, backend, frontend e teste necessarios para validar o fluxo daquela fase;
- nao e valido concluir uma fase com apenas tela sem persistencia, ou apenas schema sem fluxo verificavel.

## Fase 0

Entregas:

- ontologia consolidada;
- vocabulario controlado inicial revisado;
- definicoes canonicas de jogo, set, shoot-out, evento e resultado.
- aprovador humano nomeado;
- artefato formal de aprovacao da ontologia e do vocabulario.

## Fase 1

Entregas:

- schema inicial da base estrutural comum;
- mecanismo de migracao SQL versionada;
- processo local;
- dashboard minimo;
- cadastros base;
- trilha minima de auditoria preparada na base;
- backup manual assistido;
- restauracao basica;
- testes de persistencia.

Limite de escopo:

- Fase 1 nao cria tabelas de jogo, set, shoot-out, scout ou atribuicoes funcionais por fase;
- Fase 1 fecha apenas fundacao estrutural comum, migracoes, cadastros base, auditoria-base, backup e restauracao.

## Fase 2

Entregas:

- treino;
- jogo;
- presenca;
- elenco oficial do jogo;
- atribuicoes funcionais por fase;
- invariantes executaveis de jogo, finalizacao e reabertura;
- rastreabilidade minima ativa para registros historicos editaveis;
- escrita transacional de jogo e elenco;
- testes de encerramento/reabertura.

## Fase 3

Entregas:

- tipos de scout;
- tela de scout pos-jogo;
- `match_phase` no lancamento do scout;
- validacao de elenco;
- invariantes executaveis de scout e mutabilidade de `scout_event_types`;
- testes de integridade de scout.

## Fase 4

Entregas:

- historico por atleta;
- historico por competicao;
- historico coletivo por periodo.

## Fase 5

Entregas:

- relatorios;
- comparacoes;
- exportacoes simples.

## Fase 6

Entregas:

- refinamento de backup;
- endurecimento final de validacoes;
- polimento operacional.

## 15. Plano de Testes

## 15.1 Testes de schema

Cobrir:

- `PRAGMA foreign_keys = ON`
- `attendance` sem `training_session_id` falha
- `match_roster` duplicado falha
- `match_roster` com `participation_status` preenchido e `presence_status` diferente de `present` falha
- `match_role_assignments` para atleta fora do `match_roster` falha
- `match_role_assignments` para atleta `did_not_play` falha
- `match_role_assignments` para atleta `absent` falha
- `match_role_assignments` com `match_phase = shootout` em jogo sem shoot-out falha
- `match_sets` com empate falha
- `match_sets` aceita apenas `set_number` 1 e 2
- `match_sets` com `set_decision_type = golden_goal` e diferenca diferente de `1` ou `2` falha
- `match_sets` `finalized` com `set_decision_type` nulo falha
- `match_shootouts` com empate falha
- `matches.result_type` aceita apenas os valores canonicos definidos
- todos os quatro `result_type` validos sao aceitos apenas com configuracao coerente de sets e shoot-out
- jogo `finalized` sem dois sets falha
- jogo `finalized` com `won_2_0` e sets 1-1 falha
- jogo `finalized` com `won_shootout` sem shoot-out falha
- jogo `finalized` com `won_2_0` e shoot-out registrado falha
- inserir atleta em `match_roster` apos `finalized` falha sem reabertura controlada
- alterar set apos `finalized` falha sem reabertura controlada
- excluir set apos `finalized` falha sem reabertura controlada
- alterar ou excluir shoot-out apos `finalized` falha sem reabertura controlada
- alterar atleta de `played` para `did_not_play` quando houver scout individual vinculado falha sem reabertura controlada
- a mesma atleta pode ter atribuicao `court_player` e `goalkeeper` no mesmo jogo
- `scout_event` com atleta fora do elenco falha
- `scout_event` com atleta `absent` falha
- `scout_event` com atleta `did_not_play` falha
- `scout_event` coletivo com `event_type` individual falha
- `scout_event` individual com `event_type` coletivo falha
- `shootout_scored` ou `shootout_missed` em jogo sem shoot-out falha
- `scout_event` com `match_phase = shootout` em jogo sem shoot-out falha
- `event_type` com `phase_scope = regular_play` em `match_phase = shootout` falha
- `save_goalkeeper` sem atribuicao `goalkeeper` na mesma fase falha
- `save_goalkeeper` com atribuicao `goalkeeper` apenas em outra fase falha
- `scout_event` com `event_category` nao nulo falha
- `scout_event` com `match_id` inexistente falha
- alteracao semantica de `scout_event_types` ja utilizado falha
- `notes` sem contexto falha
- reabertura sem auditoria previa falha
- rollback em falha intermediaria de `reopen_to_draft` preserva jogo `finalized` original
- apos reabrir, corrigir e finalizar novamente, nova tentativa de alterar `match_sets`, `match_roster`, `match_role_assignments`, `match_shootouts` ou campos factuais de `matches` falha sem nova autorizacao
- backup corrompido falha na restauracao com recuperacao do banco anterior

## 15.2 Testes de persistencia

Cobrir:

- criar atleta e reabrir aplicacao
- criar jogo e reabrir aplicacao
- criar treino e reabrir aplicacao
- criar scout e reabrir aplicacao
- aplicar migracao em banco ja existente sem perder dados validos

## 15.3 Testes de concorrencia local

Cobrir:

- dupla submissao rapida do mesmo formulario nao corrompe o banco
- escrita concorrente local recebe tratamento controlado sem erro bruto para o usuario
- configuracao com `workers=1` e `timeout` explicito esta refletida no runtime esperado
- falha no meio de transacao de finalizacao nao deixa estado parcial persistido

## 15.4 Testes de backup

Cobrir:

- criar backup
- restaurar backup
- validar `PRAGMA integrity_check`
- validar `PRAGMA foreign_key_check`
- validar `schema_migrations`
- validar contagem esperada de registros
- restaurar em diretorio limpo
- rejeitar backup corrompido com falha controlada

## 15.5 Testes de fluxo

Cobrir:

- cadastro de atleta
- cadastro de competicao
- cadastro de adversario
- registro de treino com presenca
- registro de jogo com resultado canonico, sets e elenco
- registro de atribuicoes de linha e goleira para a mesma atleta no mesmo jogo
- finalizacao de jogo apenas apos coerencia completa de resultado
- reabrir jogo via `match_reopen_authorizations`, corrigir e finalizar novamente com autorizacao consumida
- falha nova mutacao estrutural ou factual apos autorizacao ja consumida
- registro de scout sem minutagem
- historico por atleta
- historico coletivo
- comparacao entre jogos
- exclusao de jogo `draft` dos relatorios consolidados por padrao
- reabrir jogo `finalized`, corrigir e finalizar novamente com trilha registrada
- alterar scout e verificar trilha minima registrada

## 15.6 Teste de carga operacional

Cenario piloto minimo:

- um jogo;
- ate 12 atletas no elenco;
- ate 40 eventos de scout;
- sem preenchimento obrigatorio de minutagem.

Meta:

- o scout principal deve poder ser concluido sem exigir transcricao exaustiva do video;
- o fluxo principal deve ser considerado invalido se obrigar o treinador a preencher minutagem de cada evento para terminar o jogo.

Meta mensuravel inicial:

- registrar um jogo piloto completo, com resultado, elenco e scout minimo, deve ser possivel em uma unica sessao de fechamento pos-jogo;
- o tempo real desse fluxo deve ser medido e registrado;
- se o piloto exigir tempo incompativel com operacao solo, a fase nao deve ser considerada aprovada sem ajuste do fluxo e nova medicao;
- o numero de campos obrigatorios do scout deve permanecer estritamente menor que o conjunto total de campos opcionais de detalhamento.
- limite inicial de aprovacao humana: ate 20 minutos para fechamento completo de um jogo piloto com ate 12 atletas e ate 40 eventos;
- limite inicial de correcoes estruturais apos o primeiro salvamento: no maximo 3 correcoes;
- o fluxo deve permitir interrupcao e retomada segura enquanto o jogo estiver `draft`.
- a aprovacao operacional final do MVP exige repeticao bem-sucedida do fluxo em 2 jogos reais completos, sem ferramenta paralela.

## 16. Criterios Tecnicos de Prontidao

O sistema so pode avancar de fase quando:

- migracoes executam sem erro;
- testes da fase passam;
- persistencia apos reinicio foi provada;
- restauracao basica foi provada nas fases que exigem backup;
- nao existe dependencia de armazenamento volatil de navegador;
- configuracao de servidor local com `workers=1` e conexao SQLite com `timeout` explicito estao verificadas;
- os termos de dominio expostos na interface estao coerentes com a ontologia do scout do MVP.

## 16.0 Evidencia e aprovacao humana

Toda fase deve registrar evidencia em artefato verificavel.

Campos minimos do artefato de evidencia:

- fase;
- status;
- responsavel humano pela aprovacao;
- data;
- documentos e versoes usados;
- testes ou roteiros executados;
- resultado;
- bloqueios remanescentes.

Regra:

- Fase 0 e documental e nao exige banco criado;
- Fase 0 so pode ser dada como concluida com aprovacao humana registrada;
- Fases 1 a 6 exigem prova executavel compativel com sua natureza tecnica.

## 16.1 Prova executavel minima por fase

Nenhuma fase pode ser dada como concluida com a afirmacao generica `implementado`.

Toda conclusao de fase tecnica exige, no minimo:

- banco criado ou migracao aplicada;
- teste passando;
- dado persistido;
- aplicacao fechada e reaberta;
- dado consultado novamente;
- fluxo daquela fase demonstrado com exemplo real ou fixture verificavel.

## 16.2 Primeiro marco real do projeto

O primeiro marco real nao e `sistema pronto`.

O primeiro marco obrigatorio e:

- registrar um jogo completo;
- definir elenco;
- registrar resultado coerente com handebol de areia;
- registrar scout minimo;
- preservar historico apos fechar e reabrir a aplicacao;
- consultar o historico;
- executar comparacao simples entre jogos.

## 17. Riscos Tecnicos Bloqueados por Esta Especificacao

Esta especificacao bloqueia explicitamente:

- implementacao web puramente client-side como modo oficial;
- uso de `attendance` como substituto do elenco do jogo;
- scout em tempo real como fluxo obrigatorio;
- exigencia de minutagem detalhada para finalizar scout;
- quebra de integridade entre `scout_events` e `match_roster`;
- soft delete incompleto para competicoes e adversarios;
- entrega de telas sem persistencia real em disco.

## 18. Proximo Artefato

Depois deste documento, o proximo artefato recomendado e:

- `PLANO_DE_EXECUCAO_MVP.md`

Esse plano deve quebrar a implementacao em tarefas pequenas, sequenciais e verificaveis.
