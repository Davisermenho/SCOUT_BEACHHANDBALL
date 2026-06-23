# Plano de Execucao para IA por Fases

## Finalidade

Este documento transforma a arquitetura aprovada em contrato operacional de execucao.

Ele existe para impedir que a implementacao por IA:

- comece pelo frontend;
- amplie escopo sem autorizacao;
- implemente scout sem ontologia aprovada;
- trate backup como detalhe tardio;
- avance de fase sem prova executavel.

## Cadeia de autoridade

Ordem obrigatoria de leitura e obediencia:

1. [PROBLEMA_FINAL.md](/home/davis/SCOUT_BEACHHANDBALL/PROBLEMA_FINAL.md:1)
2. [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:1)
3. [ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md](/home/davis/SCOUT_BEACHHANDBALL/ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md:1)
4. [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/home/davis/SCOUT_BEACHHANDBALL/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:1)
5. ADRs em [adr/](/home/davis/SCOUT_BEACHHANDBALL/adr/)

Regra:

- em conflito de escopo, prevalece `PROBLEMA_FINAL.md`;
- em conflito semantico de scout, prevalece a ontologia;
- em conflito tecnico entre especificacao e ADR, a execucao fica bloqueada ate reconciliacao explicita;
- a IA nao pode inventar regra fora dessa cadeia.

## Regras globais para a IA

Obrigatorio:

- comecar por dominio e ontologia;
- tratar SQLite como fonte unica de verdade local;
- implementar em fatias verticais pequenas sobre contrato ja definido;
- manter `attendance` restrito a treino;
- manter `match_roster` como fonte de presenca e participacao de jogo;
- manter `match_role_assignments` como fonte de atribuicao funcional por fase;
- validar `scout_events` individual apenas para atleta com `presence_status = present` e `participation_status = played` no `match_roster`, via `TRIGGER` SQLite;
- tratar `completion_status` do jogo como contrato obrigatorio de `draft` versus `finalized`;
- manter observacoes coletivas em `notes`, fora da contagem automatica de `scout_event_types`;
- tratar video apenas como apoio opcional;
- provar persistencia, reabertura e restauracao.

Proibido:

- iniciar por dashboard ou interface bonita;
- criar IA de analise automatica de video;
- trocar SQLite por outro banco;
- misturar handebol de quadra com handebol de areia;
- usar texto livre como estrutura principal do scout;
- implementar presenca de jogo em `attendance`;
- permitir `event_category` como texto livre no MVP inicial;
- concluir fase sem evidencias executaveis.

## Fase 0

Entrada:

- `PROBLEMA_FINAL.md`, `MVP.md`, ontologia e especificacao disponiveis;
- ADRs lidas.

Tarefas:

- consolidar a ontologia do dominio;
- congelar nomes canonicos de jogo, set, Golden Goal, shoot-out, resultado e evento;
- revisar vocabulario controlado inicial;
- fechar invariantes minimos de scout e resultado.

Nao fazer:

- nao criar tela final;
- nao criar relatorios;
- nao criar fluxo de video como centro do produto.

Prova executavel:

- checklist documental fechado;
- lista canonica inicial de eventos revisada;
- invariantes de resultado documentados;
- regras de Golden Goal documentadas;
- decisoes tecnicas ambiguas encerradas por ADR.
- aprovacao humana registrada em artefato proprio.

Criterio de parada:

- toda ambiguidade semantica critica foi explicitamente resolvida ou removida do escopo.

Criterio de avanco:

- ontologia aprovada como autoridade semantica do scout;
- Fase 0 marcada como concluida por evidencia documental.

Evidencia obrigatoria:

- [ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md](/home/davis/SCOUT_BEACHHANDBALL/ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md:1)
- [MATRIZ_ACHADOS_FASE_0.md](/home/davis/SCOUT_BEACHHANDBALL/MATRIZ_ACHADOS_FASE_0.md:1)
- [APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md](/home/davis/SCOUT_BEACHHANDBALL/APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md:1)
- ADR-001 a ADR-006 em [adr/](/home/davis/SCOUT_BEACHHANDBALL/adr/)

## Fase 1

Entrada:

- Fase 0 concluida;
- nomes canonicos congelados.

Tarefas:

- criar schema SQLite inicial apenas da base estrutural comum;
- aplicar constraints, `FOREIGN KEY`, `UNIQUE` e `CHECK` estruturais obrigatorios;
- criar migracao inicial versionada;
- implementar processo local;
- implementar cadastros base;
- preparar trilha minima de auditoria;
- implementar backup manual assistido e restauracao basica.

Nao fazer:

- nao criar tabelas de jogo, set, shoot-out, scout ou atribuicoes funcionais por fase na Fase 1;
- nao criar tela de scout na Fase 1;
- nao iniciar relatorios, comparacoes ou qualquer entrega da Fase 4 ou posterior;
- nao antecipar implementacao da Fase 2 por conveniencia tecnica;
- nao flexibilizar regra de integridade para acelerar interface;
- nao depender de armazenamento temporario do navegador;
- nao adiar backup para fases tardias.

Prova executavel:

- banco criado em ambiente limpo;
- migracao executa sem erro;
- atleta, competicao e adversario persistem apos fechar e reabrir a aplicacao;
- backup valido e restauracao basica provados.

Criterio de parada:

- persistencia local e restauracao inicial funcionam de forma reproduzivel.

Criterio de avanco:

- testes de schema e persistencia passam;
- backup nao depende de copia cega insegura do `.db`.

Evidencia obrigatoria:

- schema gerado;
- migracao aplicada;
- teste passando;
- restauracao validada em banco restaurado.

## Fase 2

Entrada:

- Fase 1 concluida;
- base estrutural persistente funcionando.

Tarefas:

- implementar treinos;
- implementar jogos;
- implementar Golden Goal e `set_decision_type` em `match_sets`;
- derivar `team_sets_won` e `opponent_sets_won` a partir de `match_sets` na finalizacao;
- implementar `attendance` para treino;
- implementar `match_roster` para jogo;
- implementar `match_role_assignments` por fase;
- implementar `completion_status` em jogos;
- implementar invariantes executaveis de finalizacao e reabertura;
- implementar escrita transacional de jogo, sets, shoot-out, elenco, atribuicoes por fase e finalizacao;
- ativar rastreabilidade minima de edicao historica;
- permitir edicao basica sem perda de historico.

Nao fazer:

- nao misturar presenca de treino com presenca de jogo;
- nao permitir jogo sem estrutura minima coerente;
- nao tratar jogo incompleto como jogo consolidado;
- nao permitir mutacao estrutural direta em jogo `finalized`;
- nao permitir mutacao direta em atribuicoes por fase de jogo `finalized`;
- nao manter autorizacao de `reopen_to_draft` ativa apos a nova finalizacao;
- nao guardar elenco apenas na interface.

Prova executavel:

- criar treino completo;
- criar jogo completo;
- registrar set encerrado em `regular_time` e set encerrado em `golden_goal`;
- registrar presencas de treino;
- definir elenco do jogo;
- registrar atribuicoes de linha e goleira para a mesma atleta em pelo menos um jogo;
- recusar atribuicao funcional para atleta fora do elenco ou `did_not_play`;
- finalizar jogo coerente;
- reabrir jogo finalizado, corrigir e finalizar novamente com trilha registrada;
- provar que a autorizacao de `reopen_to_draft` foi consumida apos a nova finalizacao;
- fechar e reabrir aplicacao;
- consultar novamente os dados.

Criterio de parada:

- fluxo diario minimo funciona sem planilha paralela para existencia do registro.

Criterio de avanco:

- `attendance` esta restrito a treino;
- `match_roster` esta funcionando como elenco oficial de jogo;
- `match_role_assignments` esta funcionando como contexto funcional dinamico do jogo;
- `draft` e `finalized` possuem comportamento distinto e verificavel;
- alteracoes estruturais em jogo `finalized` sao bloqueadas fora de fluxo de reabertura;
- alteracoes factuais em `matches` tambem sao bloqueadas fora de fluxo de reabertura;
- alteracoes em `match_role_assignments` tambem sao bloqueadas fora de fluxo de reabertura;
- autorizacao de `reopen_to_draft` deixa de surtir efeito apos o encerramento do fluxo;
- os dados reabrem sem inconsistencias.

Evidencia obrigatoria:

- teste de criacao e leitura de treino;
- teste de criacao e leitura de jogo;
- teste de persistencia apos reinicio;
- teste de restricao de relacionamento.

## Fase 3

Entrada:

- Fase 2 concluida;
- ontologia aprovada;
- vocabulario controlado inicial definido.

Tarefas:

- implementar `scout_event_types`;
- implementar registro de scout pos-jogo;
- implementar `scout_events` individuais;
- implementar `match_phase` em `scout_events`;
- aplicar validacao obrigatoria contra `match_roster`.
- bloquear mutacao semantica de `scout_event_types` ja usados.
- manter os quinze codigos iniciais ativos como `individual_only`;

Nao fazer:

- nao implementar scout em tempo real como premissa do MVP;
- nao exigir minutagem completa;
- nao permitir texto livre substituir tipo estruturado de evento.
- nao expor `event_category` como campo editavel no MVP inicial;
- nao permitir scout individual para atleta `absent` ou `did_not_play`.
- nao usar observacao coletiva como `event_type` comparavel.
- nao validar evento de goleira por campo fixo no elenco.
- nao ativar codigo `collective_only` no seed inicial.

Prova executavel:

- registrar scout de um jogo completo apos a partida;
- recusar `scout_event` individual para atleta fora do elenco;
- recusar `scout_event` individual para atleta `absent` ou `did_not_play`;
- aceitar `scout_event` individual apenas para atleta com `participation_status = played`;
- aceitar `save_goalkeeper` apenas para atleta com atribuicao `goalkeeper` na mesma fase;
- aceitar `shootout_scored` e `shootout_missed` apenas com `match_phase = shootout`;
- recusar evento `regular_play` com `match_phase = shootout`;
- recusar qualquer evento ou atribuicao em `shootout` sem shoot-out real;
- provar que `event_category` permanece `NULL` sem campo editavel na tela inicial;
- provar que o seed inicial nao contem `event_type` ativo `collective_only`;
- aceitar observacoes coletivas em `notes`, e nao em `scout_events`.

Criterio de parada:

- scout consistente pode ser registrado em mais de um jogo sem ambiguidade semantica central.

Criterio de avanco:

- trigger de integridade funcionando;
- fluxo pos-jogo utilizavel por uma unica pessoa;
- nenhum conceito critico depende de interpretacao livre.

Evidencia obrigatoria:

- teste de recusa para atleta fora do elenco;
- teste de aceite para atleta do elenco;
- teste de bloqueio para tipo usado fora de seu escopo;
- fixture ou jogo piloto com scout salvo e reaberto.

## Fase 4

Entrada:

- Fase 3 concluida;
- dados de pelo menos mais de um jogo ou fixture equivalente disponiveis.

Tarefas:

- implementar historico por atleta;
- implementar historico por competicao;
- implementar historico coletivo por periodo simples;
- implementar leitura de sets decididos por `golden_goal`;
- separar dado factual de observacao tecnica.

Nao fazer:

- nao transformar historico em dashboard analitico complexo;
- nao misturar interpretacao do treinador com fato estruturado sem distincao.

Prova executavel:

- consultar historico de atleta em mais de um jogo;
- consultar historico coletivo sem abrir atleta por atleta;
- consultar historico por competicao e periodo simples;
- consultar recorte historico simples de sets decididos por `golden_goal`.

Criterio de parada:

- memoria operacional longitudinal do treinador esta recuperavel no sistema.

Criterio de avanco:

- historicos batem com dados persistidos;
- filtros basicos funcionam sem consolidacao manual externa.

Evidencia obrigatoria:

- testes ou roteiro verificavel de consulta historica;
- exemplo persistido de atleta, competicao e coletivo.

## Fase 5

Entrada:

- Fase 4 concluida.

Tarefas:

- implementar relatorios minimos;
- implementar comparacao entre jogos;
- implementar comparacao por periodo apenas como visualizacao lado a lado de relatorios simples;
- incluir desempenho simples em Golden Goal;
- implementar exportacao simples, se prevista pela especificacao vigente.

Nao fazer:

- nao criar BI;
- nao criar agregacao dinamica aberta;
- nao criar comparador generico complexo.

Prova executavel:

- gerar relatorio simples de jogo;
- gerar relatorio simples de atleta;
- comparar dois jogos;
- comparar dois periodos apenas por exibicao lado a lado de relatorios ja gerados;
- visualizar consolidado simples de sets decididos por `golden_goal`.

Criterio de parada:

- relatorios e comparacoes minimas saem direto do sistema com dados coerentes.

Criterio de avanco:

- comparacao nao exige ferramenta externa;
- comparacao nao cria novo modelo analitico fora do escopo.

Evidencia obrigatoria:

- roteiro verificavel de comparacao;
- amostras de relatorios gerados sobre dados persistidos.

## Fase 6

Entrada:

- Fases 1 a 5 concluidas.

Tarefas:

- endurecer validacoes restantes;
- completar politica de inativacao em vez de exclusao;
- reforcar backup e restauracao;
- ampliar e revisar a rastreabilidade minima ja existente;
- fechar blindagens anti-regressao.

Nao fazer:

- nao reabrir escopo funcional;
- nao trocar fundamentos de persistencia;
- nao aceitar regressao de integridade para acelerar polimento.

Prova executavel:

- restauracao real de backup em ambiente limpo;
- tentativa de exclusao indevida bloqueada;
- entidades inativas somem das listas operacionais e preservam historico;
- jogo historico continua consultavel apos endurecimentos.

Criterio de parada:

- o sistema resiste aos erros operacionais previsiveis do uso real.

Criterio de avanco:

- todas as blindagens criticas estao ativas e provadas;
- primeiro marco real completo esta sustentado sem regressao.

Evidencia obrigatoria:

- teste de backup/restauracao;
- teste de inativacao;
- teste de consulta de historico preservado.

## Primeiro marco real obrigatorio

Nao e `sistema pronto`.

O primeiro marco real e:

- registrar um jogo completo;
- definir elenco oficial;
- salvar resultado coerente com sets e shoot-out;
- registrar scout minimo pos-jogo;
- fechar e reabrir a aplicacao;
- consultar historico preservado;
- comparar esse jogo com outro jogo simples;
- provar backup e restauracao.

Sem esse marco, nao ha aprovacao operacional do MVP.

## Sucesso operacional final

O MVP so pode ser considerado operacionalmente aprovado quando:

- o treinador concluir 2 jogos reais completos sozinho;
- ambos ficarem registrados com resultado, elenco, scout minimo e historico recuperavel;
- ambos respeitarem o limite operacional aprovado na Fase 0;
- ambos permitirem leitura coerente de sets, Golden Goal e shoot-out quando aplicavel;
- o historico puder ser recuperado depois sem ferramenta paralela.
