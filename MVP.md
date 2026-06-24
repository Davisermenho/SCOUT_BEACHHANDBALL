# MVP do Scout de Handebol de Areia

## 1. Finalidade

Este documento define o MVP do sistema Scout de Handebol de Areia com base no SSOT descrito em [PROBLEMA_FINAL.md](/home/davis/SCOUT_BEACHHANDBALL/PROBLEMA_FINAL.md:1).

O objetivo do MVP e:

- centralizar dados hoje dispersos;
- preservar historico tecnico e operacional;
- reduzir dependencia da memoria do treinador;
- reduzir retrabalho manual;
- permitir operacao por uma unica pessoa;
- entregar validacao incremental com baixo risco e baixo custo.

## 1.1 Regra de Alinhamento com o SSOT

Este documento existe para detalhar a solucao do MVP sem substituir o `PROBLEMA_FINAL.md`.

Sempre que houver mudanca em qualquer um dos itens abaixo, este documento deve ser revisado contra o SSOT antes de novas decisoes de implementacao:

- problema central;
- causa raiz;
- restricoes operacionais;
- escopo obrigatorio do MVP;
- fora de escopo;
- criterios de aceitacao;
- limites do que a IA pode assumir;
- prioridade humana do projeto;
- evidencia nova que altere o entendimento do problema.

Se a nova informacao nao alterar o entendimento do problema, ela deve ir para documento operacional e nao alterar este MVP por reflexo automatico.

## 1.2 Autoridade Semantica do Dominio

Os termos de scout e handebol de areia usados neste MVP devem seguir o documento [ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md](/home/davis/SCOUT_BEACHHANDBALL/ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md:1).

Regra:

- este MVP define o escopo;
- a ontologia define o significado esportivo dos termos dentro do escopo;
- a implementacao nao pode redefinir semanticamente `jogo`, `set`, `shoot-out`, `evento de scout`, `presenca`, `participacao` ou `resultado do jogo`.

## 2. Objetivo do MVP

Construir uma memoria operacional unica do treinador, capaz de registrar, consultar, comparar e reutilizar informacoes de:

- jogos;
- treinos;
- presenca;
- scout;
- historico por atleta;
- historico por competicao.

## 3. Principios Obrigatorios

- treinador solo como usuario principal e unico operador;
- handebol de areia como dominio exclusivo;
- simplicidade operacional acima de sofisticacao tecnica;
- manutencao baixa como requisito de arquitetura;
- validacao incremental por fluxo real de uso;
- dados estruturados como fonte principal;
- video tratado apenas como referencia manual;
- exportacao permitida, mas nunca como fonte primaria do sistema.

## 4. Restricoes de Arquitetura

O MVP nao pode depender de:

- microservicos;
- arquitetura distribuida;
- nuvem complexa;
- visao computacional;
- IA analisando video;
- dashboards complexos;
- predicoes;
- regras de handebol de quadra misturadas ao handebol de areia.

## 5. Arquitetura Recomendada

### 5.1 Decisao

Arquitetura recomendada:

- aplicacao monolitica local-first;
- banco SQLite como fonte unica de verdade;
- interface web simples acessada no navegador, servida por processo local da aplicacao;
- armazenamento local de anexos e referencias;
- backup consistente do banco executado pelo processo local da aplicacao com mecanismo compativel com SQLite/WAL;
- exportacao CSV e Excel apenas como saida.

Especificacao tecnica obrigatoria:

- o MVP nao deve ser implementado como aplicacao puramente client-side dependente apenas do armazenamento interno do navegador;
- a interface no navegador deve funcionar como camada de apresentacao de um processo local com acesso explicito ao arquivo SQLite;
- o arquivo do banco deve existir em caminho local controlado pela aplicacao, fora de cache volatil de navegador;
- a persistencia principal nao pode depender exclusivamente de OPFS, IndexedDB ou mecanismo equivalente de armazenamento efemero do navegador;
- se houver modo web puro para testes, ele nao pode ser considerado modo valido de producao para preservacao do historico.

### 5.2 Justificativa

Essa arquitetura resolve a causa raiz com o menor custo de manutencao porque:

- elimina a fragmentacao ao concentrar o registro em um unico sistema;
- cria historico estruturado com relacoes entre atletas, jogos, treinos e competicoes;
- reduz o trabalho manual ao reaproveitar cadastros e gerar relatorios a partir do banco;
- reduz a dependencia da memoria humana ao tornar a informacao consultavel.

## 6. Escopo Obrigatorio do MVP

O MVP deve conter apenas os seguintes modulos obrigatorios:

1. cadastro de atletas;
2. cadastro de competicoes;
3. cadastro de adversarios;
4. registro de jogos;
5. registro de treinos;
6. registro de presenca;
7. registro de scout;
8. historico por atleta;
9. historico por competicao;
10. relatorios basicos;
11. comparacoes basicas.

Observacao:

- cadastros de atletas, competicoes e adversarios sao suporte estrutural obrigatorio para viabilizar os fluxos do MVP;
- esses cadastros nao constituem novo objetivo de produto fora do escopo do SSOT;
- referencia manual de video e apoio opcional do MVP;
- nao e modulo obrigatorio;
- nao pode alterar o escopo minimo aceito.

## 7. Fora de Escopo

Permanecem fora de escopo do MVP:

- reconhecimento automatico de jogadas;
- analise automatica de video;
- classificacao por IA;
- deteccao automatica de eventos;
- recomendacao automatica de estrategia;
- dashboards analiticos complexos;
- qualquer dependencia de infraestrutura cara ou complexa;
- migracao automatica de WhatsApp;
- integracao automatica com Google Drive;
- integracao automatica com OneDrive;
- importacao automatica irrestrita de documentos legados;
- qualquer fluxo que obrigue edicao externa de video para o sistema funcionar.

## 8. Usuarios

### 8.1 Usuario principal

- treinador solo.

### 8.2 Usuario secundario eventual

- nenhum obrigatorio no MVP.

O sistema deve funcionar plenamente mesmo com um unico usuario.

## 9. Fluxos Operacionais do MVP

## 9.0 Regra de Conversao das Fontes Legadas

As fontes legadas atuais, como Excel, videos, WhatsApp, Google Drive, OneDrive, documentos e arquivos locais, devem ser tratadas assim:

- servem como fonte de consulta durante a transicao;
- deixam de ser fonte primaria depois que a informacao e registrada no sistema;
- podem ser absorvidas por digitacao guiada ou importacao controlada;
- nao exigem integracao automatica no MVP;
- nao podem continuar como dependencia obrigatoria para consulta de historico consolidado.

## 9.1 Fluxo de cadastro inicial

1. cadastrar atletas;
2. cadastrar competicoes;
3. cadastrar adversarios;
4. manter atletas ativos e inativos sem apagar historico.

## 9.2 Fluxo de treino

1. criar treino com data e objetivo;
2. selecionar atletas convocados ou presentes;
3. registrar presenca;
4. registrar observacoes tecnicas;
5. salvar e gerar historico automaticamente.

## 9.3 Fluxo de jogo

1. criar jogo com data, competicao e adversario;
2. informar placar e contexto basico;
3. registrar elenco do jogo;
4. registrar presenca e status de participacao do elenco;
5. registrar scout estruturado apos o jogo;
6. vincular observacoes e referencias de video, se existirem;
7. salvar e disponibilizar o jogo para historico e comparacao.

Observacao obrigatoria:

- no MVP, o scout de jogo nao deve ser tratado como lancamento em tempo real durante a partida;
- o fluxo padrao do scout sera pos-jogo, com preenchimento manual a partir de memoria imediata, anotacoes ou revisao manual de video;
- qualquer suporte a registro em tempo real esta fora do escopo do MVP.

## 9.4 Fluxo de consulta

1. abrir historico do atleta;
2. filtrar por periodo, competicao, treino ou jogo;
3. abrir historico coletivo;
4. comparar jogos ou periodos;
5. exportar relatorio, se necessario.

## 10. Modulos Funcionais

### 10.1 Cadastro Base

Responsavel por:

- atletas;
- competicoes;
- adversarios;
- temporadas, se necessario.

Requisitos:

- criar;
- editar;
- ativar;
- inativar;
- impedir exclusao que quebre historico.

### 10.2 Registro de Treinos

Responsavel por:

- data;
- titulo ou objetivo;
- observacoes;
- presenca.

Resultado esperado:

- cada treino gera um registro persistente consultavel por atleta e por periodo.

### 10.3 Registro de Jogos

Responsavel por:

- data;
- competicao;
- adversario;
- estado do jogo;
- resultado do confronto;
- sets regulares;
- shoot-out quando existir;
- observacoes;
- elenco participante.

Resultado esperado:

- cada jogo se torna a unidade central de analise e comparacao.

Regra obrigatoria:

- o elenco participante deve ser persistido como estrutura propria do jogo;
- o elenco do jogo nao pode ser deduzido apenas a partir de `attendance`;
- o sistema deve permitir consultar, para cada partida, quais atletas foram relacionados independentemente do volume de eventos de scout.
- o jogo deve possuir estado explicito `draft` ou `finalized`;
- jogos `draft` nao devem aparecer por padrao em historicos competitivos, comparacoes e relatorios consolidados.

### 10.4 Registro de Presenca

Responsavel por:

- presenca em treino;
- status simples padronizado.

Exemplos de status:

- presente;
- ausente;
- justificado.

### 10.5 Registro de Scout

Responsavel por:

- registrar eventos ou observacoes estruturadas por jogo;
- associar evento a atleta quando aplicavel;
- permitir classificacao manual padronizada;
- evitar texto livre como unica forma de registro.

Resultado esperado:

- permitir comparacao entre jogos e composicao de historico longitudinal.

Regra obrigatoria:

- o scout deve usar vocabulario controlado validado pelo treinador antes do uso produtivo;
- o mesmo tipo de evento nao pode receber nomes diferentes em jogos distintos;
- comparacoes entre jogos devem usar a mesma taxonomia ativa.
- evento individual so pode existir para atleta com `presence_status = present` e `participation_status = played` no `match_roster`;
- atleta ausente ou `did_not_play` nao pode receber scout individual;
- `event_category` nao pode ser texto livre estrutural no MVP.
- observacao coletiva deve ser registrada em `notes`, e nao como `event_type` comparavel.
- o vocabulario inicial do MVP deve usar classificacao primaria unica para finalizacoes, evitando dupla contagem entre tecnica, funcao e valor do gol.

Regra operacional do MVP:

- o scout do MVP deve ser pensado como registro pos-jogo;
- o preenchimento principal deve ocorrer apos a partida, e nao durante a conducao tecnica ao vivo;
- a interface nao deve exigir interacao em tempo real para que o fluxo principal do sistema seja considerado valido;
- quando houver referencia de video, ela serve como apoio manual para revisao posterior do scout.

Regra de carga operacional:

- `minute` e `event_category` nao podem ser campos obrigatorios para conclusao do scout no MVP;
- o sistema deve permitir finalizar o registro principal do scout sem minutagem detalhada;
- qualquer detalhamento fino deve ser opcional e usado apenas quando trouxer valor real ao treinador;
- o fluxo padrao deve priorizar velocidade de fechamento do jogo, e nao granularidade maxima de anotacao.

### 10.6 Historico por Atleta

Deve consolidar:

- dados cadastrais relevantes;
- presencas;
- participacao em jogos;
- scout associado;
- observacoes vinculadas;
- referencias de video relacionadas.

### 10.7 Historico por Competicao

Deve consolidar:

- jogos da competicao;
- atletas envolvidos;
- dados coletivos basicos;
- comparacoes entre partidas.

Deve tambem permitir historico coletivo por recorte operacional:

- por competicao;
- por periodo;
- por equipe em conjunto, sem depender de abrir atleta por atleta.

### 10.8 Relatorios Basicos

Relatorios minimos:

- relatorio por atleta;
- relatorio coletivo;
- relatorio por competicao;
- comparacao entre dois jogos.

### 10.9 Apoio Opcional de Referencia Manual de Video

Permitido apenas como apoio manual:

- link;
- nome do arquivo;
- minuto ou trecho;
- observacao textual;
- associacao com jogo, atleta ou evento.

Nao faz parte do MVP:

- processar video;
- reconhecer eventos;
- classificar automaticamente conteudo do video.

## 11. Modelo de Dados Minimo

## 11.1 Entidades obrigatorias

- `athletes`
- `competitions`
- `opponents`
- `matches`
- `match_sets`
- `match_shootouts`
- `match_roster`
- `match_role_assignments`
- `training_sessions`
- `attendance`
- `scout_events`
- `scout_event_types`
- `notes`

## 11.1.1 Entidades opcionais de apoio

- `video_references`

## 11.2 Campos minimos por entidade

### `athletes`

- `id`
- `full_name`
- `nickname` opcional
- `status`
- `created_at`
- `updated_at`

### `competitions`

- `id`
- `name`
- `season`
- `status`
- `location` opcional
- `start_date` opcional
- `end_date` opcional

### `opponents`

- `id`
- `name`
- `status`
- `city` opcional
- `notes` opcional

### `matches`

- `id`
- `match_date`
- `competition_id`
- `opponent_id`
- `completion_status`
- `result_type` opcional enquanto `draft`
- `team_sets_won` opcional enquanto `draft`
- `opponent_sets_won` opcional enquanto `draft`
- `notes` opcional
- `created_at`
- `updated_at`

Observacao:

- `matches` representa o confronto completo;
- o resultado do jogo nao pode ser reduzido a um unico placar agregado ambiguo.
- `completion_status = draft` significa jogo em preenchimento;
- `completion_status = finalized` significa jogo coerente e apto para historico, comparacao e relatorio.

### `match_sets`

- `id`
- `match_id`
- `set_number`
- `set_decision_type`
- `team_score`
- `opponent_score`

Observacao:

- o placar armazenado em `match_sets` deve refletir o placar oficial final do set;
- esse placar inclui eventual gol decisivo de Golden Goal;
- `set_decision_type` deve distinguir se o set terminou em `regular_time` ou `golden_goal`;
- Golden Goal decide set; shoot-out decide o jogo apos sets 1-1.

Especificacao obrigatoria de persistencia:

- `set_decision_type` pode permanecer vazio enquanto o jogo estiver `draft`;
- `set_decision_type` torna-se obrigatorio quando o jogo for `finalized`;
- set `finalized` com `set_decision_type = golden_goal` deve manter placar final nao empatado e diferenca compativel com o gol decisivo final.

### `match_shootouts`

- `id`
- `match_id`
- `team_score`
- `opponent_score`

### `match_roster`

- `id`
- `match_id`
- `athlete_id`
- `presence_status`
- `participation_status`
- `notes` opcional

Observacao:

- `match_roster` e a fonte oficial do elenco de cada jogo;
- `match_roster` tambem e a fonte oficial da presenca e participacao no contexto do jogo;
- deve existir restricao de unicidade para impedir o mesmo atleta mais de uma vez no mesmo jogo;
- `attendance` nao deve ser usado para presenca de jogo.
- atleta com `participation_status = played` e a unica condicao valida para receber scout individual.

### `match_role_assignments`

- `id`
- `match_id`
- `athlete_id`
- `match_phase`
- `role`

Observacao:

- atribuicao funcional nao e propriedade fixa do elenco;
- atribuicao funcional registra atuacao efetiva na fase, e nao designacao prevista;
- a mesma atleta pode ter mais de uma atribuicao no mesmo jogo;
- a mesma atleta pode ter mais de uma atribuicao na mesma fase;
- atribuicao funcional so pode existir para atleta que pertence ao `match_roster` do mesmo jogo com `presence_status = present` e `participation_status = played`;
- atleta com `participation_status = did_not_play` nao pode possuir atribuicao funcional;
- atribuicao com `match_phase = shootout` so pode existir em jogo com shoot-out real;
- `match_role_assignments` existe para validar contexto funcional dinamico, especialmente eventos de goleira e eventos de shoot-out.

Especificacao obrigatoria de persistencia:

- `match_role_assignments` deve validar estruturalmente o par `(match_id, athlete_id)` contra o elenco do jogo;
- a implementacao pode usar chave estrangeira composta, `TRIGGER` especifico, ou ambos, desde que nao aceite atribuicao funcional para atleta fora do elenco, ausente ou `did_not_play`.

Especificacao obrigatoria de persistencia:

- `match_roster` deve possuir restricao `UNIQUE(match_id, athlete_id)` no banco SQLite;
- `match_roster.match_id` deve possuir chave estrangeira para `matches.id`;
- `match_roster.athlete_id` deve possuir chave estrangeira para `athletes.id`.

### `training_sessions`

- `id`
- `training_date`
- `title`
- `objective` opcional
- `notes` opcional
- `created_at`
- `updated_at`

### `attendance`

- `id`
- `athlete_id`
- `training_session_id`
- `status`
- `notes` opcional

Observacao:

- `attendance` fica restrito ao contexto de treino;
- essa regra existe para evitar conflito entre treino e jogo.

Especificacao obrigatoria de persistencia:

- `training_session_id` deve ser obrigatorio;
- o banco SQLite deve recusar qualquer `attendance` sem treino associado;
- nenhum script de importacao, manutencao ou migracao pode contornar essa regra.

### `scout_events`

- `id`
- `match_id`
- `athlete_id` opcional
- `match_phase`
- `event_type`
- `event_category` opcional
- `minute` opcional
- `notes` opcional
- `created_at`

Observacao:

- quando `athlete_id` estiver preenchido, o atleta deve existir no `match_roster` do mesmo `match_id`;
- o sistema nao deve aceitar scout individual vinculado a atleta fora do elenco oficial da partida;
- o sistema nao deve aceitar scout individual para atleta `absent` ou `did_not_play`;
- o sistema deve validar `save_goalkeeper` contra atribuicao `goalkeeper` na mesma fase;
- o sistema deve validar `shootout_scored` e `shootout_missed` apenas com `match_phase = shootout`;
- o sistema deve validar eventos `regular_play` apenas com `match_phase = set_1` ou `set_2`;
- o sistema deve recusar qualquer evento com `match_phase = shootout` quando o jogo nao possuir shoot-out real;
- `event_category` deve permanecer vazia no MVP inicial enquanto nao existir lista controlada aprovada.

Especificacao obrigatoria de persistencia:

- a decisao oficial do MVP para SQLite e usar `TRIGGER` explicito para validar scout individual contra `match_roster`;
- a implementacao nao deve manter em paralelo regra concorrente baseada em chave estrangeira composta ambigua para esse caso;
- qualquer ajuste futuro de modelagem deve preservar uma unica fonte de verdade para essa integridade;
- a validacao em aplicacao nao substitui a protecao estrutural do banco.

### `scout_event_types`

- `id`
- `code`
- `label`
- `scope_mode`
- `phase_scope`
- `required_role`
- `requires_played_status`
- `status`

Regra:

- a tabela define o vocabulario controlado minimo do scout;
- `scout_events.event_type` deve apontar para um tipo valido desse cadastro ou usar o mesmo conjunto controlado em implementacao equivalente.
- a aprovacao do conjunto ativo exige registro humano explicito de Fase 0;
- o seed do MVP deve declarar se o evento e individual ou coletivo, se e exclusivo de shoot-out e se exige atleta com participacao efetiva.
- o seed inicial do MVP nao deve incluir `goal_specialist`, `missed_specialist` ou `collective_note`;
- observacoes coletivas pertencem a `notes`;
- eventos usados em historico comparativo devem ser factuais e mutuamente exclusivos.
- especialista continua fora de `event_type` e deve ser tratada apenas como contexto funcional.
- o MVP inicial nao cria valor proprio `specialist` em `match_role_assignments`;
- quando a mesma atleta possuir `court_player` e `goalkeeper` na mesma fase, essa combinacao pode ser interpretada tecnicamente como contexto de especialista, sem criar novo `event_type`.

### `video_references`

- `id`
- `match_id` opcional
- `athlete_id` opcional
- `scout_event_id` opcional
- `source_type`
- `path_or_url`
- `time_reference` opcional
- `notes` opcional

### `notes`

- `id`
- `match_id` opcional
- `training_session_id` opcional
- `athlete_id` opcional
- `scout_event_id` opcional
- `content`
- `created_at`

Observacao:

- pelo menos um contexto valido deve estar preenchido;
- a modelagem deve manter relacao verificavel com o registro comentado.

## 11.3 Regras de relacionamento

- um jogo pode ter muitos atletas no elenco oficial;
- um atleta pode aparecer em muitos elencos de jogo;
- um atleta pode ter muitos registros de presenca;
- um atleta pode ter muitos registros de scout;
- uma competicao pode ter muitos jogos;
- um jogo pertence a uma competicao;
- um registro de `match_roster` pertence a um unico jogo e a um unico atleta;
- um jogo pode ter muitos eventos de scout;
- um treino pode ter muitos registros de presenca;
- um tipo de scout pode ser usado por muitos eventos;
- notas devem apontar para contexto real e verificavel;
- referencias de video devem estar associadas a algum contexto valido.

## 12. Regras Operacionais

### 12.1 Regras de integridade

- nenhum jogo pode ser salvo sem data;
- nenhum jogo pode ser salvo sem adversario;
- nenhuma presenca pode existir sem atleta;
- nenhum scout de jogo pode existir sem jogo;
- atletas nao devem ser apagados fisicamente se houver historico associado;
- competicoes e adversarios nao devem ser apagados se estiverem em uso.

Regras adicionais obrigatorias:

- `attendance` deve ser protegido por restricao estrutural no banco, e nao apenas por validacao de interface;
- qualquer tentativa de salvar `attendance` sem treino valido deve falhar antes da persistencia;
- `match_roster` deve possuir restricao de unicidade por `match_id` e `athlete_id`;
- nenhum `scout_event` individual pode ser salvo para atleta ausente do `match_roster` correspondente;
- `competitions` e `opponents` devem suportar inativacao sem exclusao fisica;
- registros inativos devem permanecer disponiveis para historico, relatorio e integridade referencial;
- formularios operacionais devem exibir por padrao apenas registros ativos, com opcao explicita para consultar inativos.

### 12.2 Regras de simplicidade

- usar listas padronizadas sempre que possivel;
- minimizar digitacao livre em fluxos recorrentes;
- permitir duplicacao de estrutura de jogo e treino quando fizer sentido;
- priorizar poucos cliques e poucos campos por tela;
- evitar retranscricao do mesmo dado em mais de uma ferramenta;
- o fluxo principal nao pode pressupor que o treinador registre scout enquanto conduz a partida.

### 12.3 Regras de historico

- toda edicao relevante deve manter rastreabilidade minima;
- jogo `finalized` nao pode receber alteracao estrutural em elenco, atribuicoes por fase, sets ou shoot-out fora de fluxo de `reopen_to_draft`;
- campos factuais de `matches` exigem `reopen_to_draft` antes de alteracao: `match_date`, `competition_id`, `opponent_id`, `result_type`, `team_sets_won`, `opponent_sets_won` e `completion_status`;
- `notes` e outros campos interpretativos podem ser editados sem `reopen_to_draft`, desde que a trilha minima de auditoria seja registrada;
- o fluxo `reopen_to_draft` deve possuir mecanismo deterministico de autorizacao persistida antes da alteracao estrutural;
- o fluxo `reopen_to_draft` deve registrar auditoria antes da transicao para `draft`, executar rollback integral em falha e exigir nova finalizacao coerente para recolocar o jogo no historico consolidado;
- registros inativos devem permanecer consultaveis;
- o historico do atleta deve refletir treinos, jogos, presenca e scout sem depender de consolidacao manual.

### 12.4 Regras de absorcao das fontes legadas

- o MVP deve permitir migracao manual progressiva das informacoes hoje espalhadas;
- nenhuma fonte legada pode permanecer obrigatoria para consulta do historico consolidado;
- planilhas podem ser usadas como importacao controlada ou exportacao, mas nao como banco paralelo de verdade;
- videos podem permanecer fora do banco como arquivo ou link, desde que a referencia essencial fique registrada no sistema;
- mensagens e documentos legados podem ser resumidos em notas estruturadas quando forem relevantes para o historico tecnico.

## 13. Telas Minimas do MVP

1. painel inicial;
2. cadastro de atletas;
3. cadastro de competicoes;
4. cadastro de adversarios;
5. formulario de treino;
6. formulario de jogo;
7. tela de presenca;
8. tela de scout do jogo;
9. historico do atleta;
10. historico da competicao;
11. comparacao entre jogos;
12. exportacao de relatorio.

## 14. Relatorios Minimos

### 14.1 Relatorio por atleta

Deve mostrar:

- presencas;
- jogos disputados;
- treinos registrados;
- eventos de scout;
- observacoes e referencias associadas.

### 14.2 Relatorio coletivo

Deve mostrar:

- volume de jogos;
- volume de treinos;
- presenca geral;
- consolidado simples de scout;
- consolidado simples de sets decididos por `golden_goal`;
- recorte por periodo;
- recorte por competicao;
- visao da equipe sem depender de abrir atletas individualmente.

### 14.3 Relatorio por competicao

Deve mostrar:

- jogos da competicao;
- atletas envolvidos;
- comparacao basica entre partidas;
- quantidade e distribuicao simples de sets decididos por `golden_goal`;
- consolidado coletivo da competicao.

### 14.4 Relatorio comparativo

Deve permitir:

- comparar dois jogos;
- comparar dois periodos;
- comparar desempenho basico de um atleta em recortes distintos.

## 15. Ordem de Implementacao

Regra de metodo:

- a implementacao nao deve seguir uma leitura rigida de `100% banco -> 100% backend -> 100% frontend`;
- a ordem correta com menor risco e `dominio -> modelo de dados -> backend -> frontend -> validacao ponta a ponta`;
- o banco vem antes como fundacao estrutural, mas cada entrega deve atravessar banco, backend, frontend e teste em fatias pequenas;
- a ontologia do handebol de areia deve ser tratada como prerequisito da modelagem de dados, com baseline tecnico validado e gate humano explicitado separadamente.

### Fase 0. Dominio e Ontologia

- consolidar e congelar a ontologia do handebol de areia no nivel documental;
- manter baseline tecnico minimo rastreavel para a ontologia do scout;
- congelar o significado de `jogo`, `set`, `golden_goal`, `shoot-out`, `evento de scout`, `presenca`, `participacao` e `resultado do jogo`;
- validar o vocabulario controlado inicial com o treinador.

Entrega validada quando:

- os termos centrais do dominio estao definidos sem ambiguidade;
- o modelo de dados deixa de depender de interpretacao livre de handebol de quadra;
- a implementacao futura passa a ter referencia semantica unica.
- existe artefato humano de aprovacao do vocabulario e da ontologia;
- existe baseline tecnico validado para o artefato ontologico minimo;
- existe definicao congelada do estado do jogo e das regras de resultado coerente;
- existe regra explicita para `event_category` no MVP inicial.

### Fase 1. Base estrutural

- criar banco SQLite;
- definir caminho fisico persistente do banco local;
- criar entidades base;
- criar cadastros de atletas, competicoes e adversarios;
- criar infraestrutura minima de rastreabilidade editavel;
- implementar backup manual assistido e restauracao basica desde a primeira versao utilizavel.

Entrega validada quando:

- os cadastros funcionam;
- os dados ficam persistidos;
- nao ha dependencia de planilha para existencia do registro;
- fechar e reabrir a aplicacao preserva os dados;
- existe teste automatizado ou script verificavel confirmando persistencia em disco local;
- existe teste verificavel de backup consistente e restauracao basica do banco.

Criterio tecnico de prontidao da Fase 1:

- esquema SQLite criado com `FOREIGN KEY`, `UNIQUE` e `CHECK` necessarios para as regras ja definidas no MVP;
- script de criacao ou migracao executa sem erro em ambiente limpo;
- teste automatizado prova que os dados persistem apos reinicio da aplicacao;
- teste automatizado ou script verificavel prova que um banco restaurado a partir de backup consistente reabre corretamente.

### Fase 2. Operacao diaria minima

- implementar treinos;
- implementar jogos;
- implementar presenca;
- implementar elenco oficial com `match_role_assignments` por fase;
- implementar `set_decision_type` e Golden Goal em `match_sets`;
- permitir a mesma atleta com atribuicoes de linha e goleira no mesmo jogo;
- implementar rastreabilidade minima de edicao para registros historicos;
- implementar transacao atomica de jogo, sets, shoot-out, elenco, atribuicoes por fase e finalizacao;
- manter fluxo de persistencia e backup operacional desde o primeiro uso real.

Entrega validada quando:

- o treinador consegue registrar um treino e um jogo completos;
- o treinador consegue registrar set encerrado em `regular_time` e set encerrado em `golden_goal`;
- o treinador consegue registrar atribuicoes funcionais por fase para uma mesma atleta no mesmo jogo;
- o treinador nao consegue registrar atribuicao funcional para atleta fora do elenco ou `did_not_play`;
- a informacao pode ser reaberta e editada sem perda;
- o uso do fluxo diario nao depende de armazenamento temporario de aba ou navegador;
- existe evidencia verificavel de que o banco continua integro apos encerramento e nova abertura da aplicacao.

Criterio tecnico de prontidao da Fase 2:

- teste automatizado cobre criacao, edicao e leitura de treino, jogo e presenca;
- teste automatizado cobre a obrigatoriedade de treino valido em `attendance`;
- teste automatizado cobre comportamento de `draft` versus `finalized` no fluxo de jogo;
- teste automatizado cobre bloqueio de alteracao ou exclusao sem reabertura controlada quando o jogo estiver `finalized`;
- teste automatizado cobre rastreabilidade minima ao editar registro historico;
- teste automatizado ou script verificavel prova que o historico sobrevive ao encerramento da aplicacao sem depender de estado em memoria RAM.

### Fase 3. Scout estruturado

- implementar eventos de scout;
- vincular scout ao jogo e ao atleta;
- padronizar tipos de evento.

Entrega validada quando:

- e possivel registrar scout consistente em mais de um jogo;
- os registros podem ser comparados.

Criterio tecnico de prontidao da Fase 3:

- teste automatizado prova que `scout_event` individual e recusado quando o atleta nao pertence ao `match_roster` do jogo;
- teste automatizado prova que `scout_event` individual e recusado quando o atleta esta `absent` ou `did_not_play`;
- teste automatizado prova que `save_goalkeeper` so e aceito para atleta com atribuicao `goalkeeper` na mesma fase;
- teste automatizado prova que `shootout_scored` e `shootout_missed` so sao aceitos com `match_phase = shootout`;
- teste automatizado prova que eventos `regular_play` sao recusados com `match_phase = shootout`;
- teste automatizado prova que tipo coletivo nao pode ser usado em evento individual;
- teste automatizado prova que tipo de evento ja utilizado nao pode ter escopo semantico alterado;
- teste automatizado cobre rastreabilidade minima para alteracao e exclusao logica de scout;
- teste automatizado prova que `scout_event` e aceito apenas quando o atleta pertence ao elenco oficial e possui `participation_status = played`;
- a interface de scout permite concluir o fluxo sem preencher `minute` e `event_category`;
- `event_category` nao aceita texto livre no MVP inicial;
- o tempo de fechamento do scout principal de um jogo piloto nao pode exigir minutagem completa evento a evento para ser considerado valido.

### Fase 4. Historico longitudinal

- implementar historico por atleta;
- implementar historico por competicao;
- implementar leitura historica de sets decididos por `golden_goal`;
- implementar filtros basicos.

Entrega validada quando:

- o treinador consulta a trajetoria de um atleta sem consolidacao manual;
- o historico coletivo pode ser aberto por competicao e por periodo;
- a equipe pode ser consultada como conjunto sem abrir atleta por atleta.

### Fase 5. Relatorios e comparacoes

- implementar relatorios minimos;
- implementar comparacao entre jogos;
- incluir recorte simples de desempenho em Golden Goal;
- implementar exportacoes simples.

Entrega validada quando:

- os relatorios saem direto do sistema;
- a comparacao entre dois jogos e utilizavel.

Criterio tecnico de prontidao da Fase 5:

- comparacao entre periodos, quando existir, deve ser implementada como exibicao lado a lado de relatorios simples, sem mecanismo de BI dinamico;
- teste automatizado ou roteiro verificavel confirma que a consulta comparativa nao depende de ferramenta externa;
- o fluxo de comparacao deve operar sobre dados persistidos e consistentes no banco.

### Fase 6. Blindagem operacional

- rotinas adicionais de blindagem de backup;
- inativacao em vez de exclusao;
- validacoes de integridade;
- ampliacao e revisao da rastreabilidade minima ja existente.

Entrega validada quando:

- o sistema preserva historico;
- restauracao basica de backup e possivel;
- erros operacionais comuns nao quebram os dados.

Observacao:

- backup e restauracao basicos nao comecam na Fase 6;
- a Fase 6 apenas fortalece, agenda ou amplia uma capacidade que ja deve existir desde a Fase 1.

## 16. Blindagens Anti-Regressao

O MVP deve sair com estas protecoes obrigatorias:

- validacao de campos obrigatorios;
- integridade relacional entre entidades;
- soft delete ou inativacao;
- IDs estaveis;
- rotina de backup consistente datado do banco;
- restauracao de backup testada;
- listas controladas para campos recorrentes;
- testes de fluxo para cadastro, jogo, historico e comparacao;
- proibicao de depender de memoria humana para reconstruir historico;
- proibicao de depender de fonte legada externa para consulta do historico consolidado;
- vocabulos controlados para o scout comparavel.

## 17. Criterios de Aceitacao do MVP

O MVP so sera aceito se atender simultaneamente a todos os criterios abaixo:

1. registrar jogos sem falhas;
2. comparar jogos;
3. gerar historico por atleta;
4. gerar historico coletivo;
5. preservar dados;
6. reduzir dependencia da memoria humana;
7. reduzir carga operacional;
8. ser operavel por uma unica pessoa.

## 18. Evidencias de Aceitacao

Cada criterio deve ser provado por evidencia pratica:

Regras gerais de prova:

- a prova deve ser executada com dados persistidos no sistema;
- a prova nao pode depender de WhatsApp, Google Drive, OneDrive ou planilha como fonte primaria;
- a prova deve poder ser repetida pela mesma pessoa operadora;
- a prova deve usar o vocabulario controlado ativo do scout;
- a prova nao pode depender de dados ainda residentes apenas em memoria de execucao da interface;
- a prova deve continuar valida apos fechar e reabrir a aplicacao.

### 18.1 Registrar jogos sem falhas

Prova:

- criar jogo;
- editar jogo;
- fechar sistema;
- reabrir sistema;
- consultar o mesmo jogo com dados preservados.

### 18.2 Comparar jogos

Prova:

- selecionar dois jogos validos;
- visualizar diferencas e semelhanas de forma legivel.

### 18.3 Gerar historico por atleta

Prova:

- abrir atleta com registros em multiplos jogos e treinos;
- visualizar linha do tempo sem consolidacao manual externa.

### 18.4 Gerar historico coletivo

Prova:

- abrir historico coletivo por competicao;
- abrir historico coletivo por periodo;
- visualizar jogos, presenca agregada e consolidado de scout;
- consultar a equipe como conjunto sem abrir atleta por atleta.

### 18.5 Preservar dados

Prova:

- executar backup;
- restaurar backup;
- confirmar integridade do historico apos restauracao.

### 18.6 Reduzir dependencia da memoria humana

Prova:

- recuperar informacao historica por busca, filtro ou relatorio;
- nao depender de lembranca do treinador para comparar registros.

### 18.7 Reduzir carga operacional

Prova:

- registrar um treino completo sem sair do sistema;
- registrar um jogo completo usando apenas o fluxo principal do sistema;
- consultar o historico correspondente sem abrir Excel, WhatsApp, Google Drive ou OneDrive;
- nao retranscrever manualmente o mesmo dado em uma segunda ferramenta para concluir o fluxo;
- concluir o scout principal do jogo sem exigir preenchimento obrigatorio de minutagem para cada evento;
- o fluxo principal deve ser validado com volume de entrada enxuto, compativel com operacao solo;
- o fechamento completo de um jogo com ate 12 atletas e ate 40 eventos deve caber em ate 20 minutos;
- o fluxo deve permitir interrupcao e retomada segura enquanto o jogo estiver `draft`;
- o numero de correcoes estruturais apos o primeiro salvamento nao deve passar de 3.

### 18.8 Ser operavel por uma unica pessoa

Prova:

- executar o fluxo sem apoio tecnico especializado;
- operar sem infraestrutura distribuida ou rotinas complexas;
- repetir o fluxo com sucesso em 2 jogos reais completos, sem ferramenta paralela.

## 19. Regra de Prontidao do Documento de MVP

Este documento so deve ser considerado pronto para orientar implementacao quando:

- estiver alinhado ao `PROBLEMA_FINAL.md`;
- estiver alinhado a `ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md`;
- nao ampliar indevidamente o escopo obrigatorio;
- tiver criterios de aceitacao com prova executavel;
- tiver historico coletivo, carga operacional e preservacao de dados descritos de forma verificavel;
- tiver a ontologia consolidada como baseline tecnico e documental antes da implementacao estrutural;
- tiver o gate humano vigente de Fase 0 explicitado sem ambiguidade.

## 20. Riscos a Evitar

- transformar o MVP em projeto de IA;
- inflar escopo com automacao de video;
- criar telas demais antes de validar fluxo minimo;
- permitir texto livre em excesso e perder padronizacao;
- manter Excel como fonte principal;
- criar dependencia de configuracao complexa;
- apagar dados historicos por erro operacional;
- reintroduzir dependencia de ferramenta legada como fonte primaria;
- quebrar comparabilidade do scout por falta de vocabulario controlado.

## 21. Definicao de Sucesso

O MVP sera bem-sucedido se:

- substituir a fragmentacao atual por um fluxo unico de registro;
- gerar historico consultavel real;
- reduzir retrabalho;
- apoiar decisoes tecnicas com base em dados preservados;
- funcionar no contexto real de um treinador solo.

## 22. Proxima Etapa Apos Este Documento

Este MVP ja foi desdobrado em especificacao de implementacao no arquivo [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/home/davis/SCOUT_BEACHHANDBALL/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:1).

O proximo passo recomendado passa a ser a criacao de um plano de execucao contendo:

- ordem de entrega por tarefas pequenas;
- dependencias entre tarefas;
- roteiro de validacao por fase;
- checklist tecnico antes de iniciar codigo;
- plano de testes executavel por entrega.
