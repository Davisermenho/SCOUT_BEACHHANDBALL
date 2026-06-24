---
doc_id: ontologia-scout-handebol-areia-mvp
doc_type: review
status: current
phase_scope:
  - phase_0
authority_level: supporting
owned_by: fase_0_documentary_baseline
canonical_path: /docs/03_ontologia/ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md
supersedes: []
superseded_by: null
must_read_before_implementation: false
implementation_ready: false
last_reviewed: "2026-06-24"
---

# Ontologia do Scout de Handebol de Areia para o MVP

## 1. Finalidade

Este documento fecha o significado dos conceitos de dominio usados no MVP.

Seu objetivo e impedir que a implementacao gere:

- banco tecnicamente valido com semantica esportiva errada;
- mistura de conceitos de handebol de quadra com handebol de areia;
- historico comparavel no formato, mas nao confiavel no significado.

## 2. Ordem de Autoridade

Quando houver conflito entre documentos:

1. [PROBLEMA_FINAL.md](/docs/01_contexto/PROBLEMA_FINAL.md:1)
2. [MVP.md](/docs/02_produto/MVP.md:1)
3. este documento
4. [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/docs/04_implementacao/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:1)

Observacao:

- este documento e a autoridade semantica para os termos do scout dentro do escopo do MVP;
- a especificacao de implementacao nao pode redefinir os termos aqui descritos.
- se a especificacao e uma ADR tecnica divergirem, a implementacao fica bloqueada ate reconciliacao documental explicita.

## 3. Principios Semanticos

- o dominio e exclusivamente handebol de areia;
- o sistema nao pode usar conceitos de placar, periodo ou evento tipicos de handebol de quadra como se fossem equivalentes;
- o MVP deve registrar fatos operacionais e tecnicos, nao inferencias automaticas;
- toda comparacao entre jogos depende de vocabulos canonicos estaveis;
- o que e fato registrado deve ficar separado do que e observacao interpretativa do treinador.

## 4. Definicoes Canonicas

## 4.1 Jogo

`Jogo` e o confronto oficial entre a equipe e um adversario em uma data, no contexto de uma competicao.

No MVP, um jogo:

- contem dois sets regulares;
- pode conter shoot-out de desempate;
- possui um resultado final do confronto;
- e a unidade principal de historico competitivo e comparacao.

`Jogo` nao significa:

- um set isolado;
- um lance;
- uma sequencia de scout;
- uma sessao de video.

## 4.2 Set

`Set` e uma unidade regular de disputa dentro do jogo.

No MVP:

- cada jogo possui exatamente dois sets regulares;
- cada set possui placar proprio;
- o placar armazenado do set e o placar oficial final, incluindo eventual gol decisivo de Golden Goal;
- cada set possui `set_decision_type` para distinguir encerramento no tempo regular ou por Golden Goal;
- o set nao substitui o jogo como unidade principal de historico.

Valores canonicos de `set_decision_type` no MVP:

- `regular_time`
- `golden_goal`

Regra semantica:

- `golden_goal` decide o set;
- o shoot-out nao decide set, apenas o jogo apos sets 1-1;
- o set encerrado por `golden_goal` continua sendo armazenado pelo placar oficial final nao empatado.

## 4.3 Shoot-out

`Shoot-out` e o desempate do jogo quando o confronto nao se resolve apenas pelos sets regulares.

No MVP:

- o shoot-out e opcional;
- ele so existe quando o resultado do confronto exigir desempate;
- ele so existe depois de sets vencidos em 1-1;
- ele nao substitui Golden Goal, porque Golden Goal decide set e shoot-out decide o jogo;
- ele deve ser registrado separadamente dos sets.

## 4.4 Resultado do jogo

`Resultado do jogo` e a forma como o confronto terminou.

Valores canonicos do MVP:

- `won_2_0`
- `lost_0_2`
- `won_shootout`
- `lost_shootout`

O MVP nao deve usar apenas um campo generico de placar agregado para representar o resultado de handebol de areia.

## 4.5 Estado do jogo

`Estado do jogo` e a situacao de completude operacional do registro competitivo.

Valores canonicos do MVP:

- `draft`
- `finalized`

Regras:

- `draft` significa que o jogo ainda pode estar em preenchimento e nao deve aparecer por padrao em relatorios comparativos nem em historicos competitivos consolidados;
- `finalized` significa que o jogo ja possui resultado coerente, dois sets registrados e, quando aplicavel, shoot-out coerente;
- scout pos-jogo do MVP deve operar sobre jogo `finalized` ou sobre jogo em fechamento controlado que sera finalizado na mesma sessao operacional.

## 4.6 Elenco do jogo

`Elenco do jogo` e a lista oficial de atletas relacionados para aquela partida.

O elenco do jogo deve registrar:

- quem foi relacionado;
- quem esteve presente;
- quem participou efetivamente;
- quem esteve presente mas nao entrou.

O elenco do jogo e a fonte oficial do contexto competitivo do atleta naquela partida.

## 4.6.1 Atribuicao funcional por fase

A funcao competitiva nao e propriedade fixa da atleta no jogo inteiro.

No MVP, essa variacao deve ser registrada em estrutura propria de atribuicoes por fase.

Modelo semantico minimo:

- `match_role_assignments` registra atribuicoes contextuais;
- uma atleta pode ter mais de uma atribuicao no mesmo jogo;
- a mesma atleta pode atuar como jogadora de linha e como goleira no mesmo jogo;
- a validacao semantica do scout deve usar a atribuicao correta da fase, e nao um campo fixo no elenco.

Valores canonicos de `match_phase` no MVP:

- `set_1`
- `set_2`
- `shootout`

Valores canonicos de `role` no MVP:

- `court_player`
- `goalkeeper`

Semantica:

- `match_role_assignments` registra atuacao efetiva naquela fase, e nao mera designacao prevista;
- a atribuicao `goalkeeper` significa que, naquela fase, a atleta efetivamente atuou com contexto funcional de goleira para fins de validacao do scout;
- a atribuicao `court_player` significa atuacao efetiva de linha naquela fase;
- atleta com `participation_status = did_not_play` nao deve possuir `match_role_assignments`;
- o MVP inicial nao representa minutagem nem troca temporal fina dentro da mesma fase;
- se a mesma atleta atuar como goleira e linha na mesma fase, o MVP inicial pode registrar duas atribuicoes distintas para a mesma atleta e fase, representando fato ocorrido;
- atribuicoes com `match_phase = shootout` so sao validas quando o jogo realmente possuir shoot-out.

## 4.7 Presenca

`Presenca` significa comparecimento a treino.

No contexto de jogo, a presenca faz parte do `elenco do jogo` e nao de uma tabela paralela de treino.

No MVP:

- `attendance` e conceito de treino;
- `match_roster` e conceito de jogo.

## 4.8 Participacao

`Participacao` significa se o atleta efetivamente atuou no jogo.

No MVP:

- um atleta pode estar presente no jogo e nao participar;
- um atleta nao pode participar se estiver ausente;
- `played` significa que houve participacao competitiva efetiva no jogo;
- `did_not_play` significa que o atleta esteve presente, mas nao entrou em quadra de forma competitiva;
- participacao pertence ao contexto do jogo, nao ao treino.

## 4.9 Evento de scout

`Evento de scout` e o menor registro estruturado de interesse tecnico feito sobre um jogo.

Um evento de scout do MVP registra:

- a qual jogo pertence;
- opcionalmente, a qual atleta pertence;
- em qual `match_phase` ocorreu;
- qual codigo canonico de evento ocorreu;
- opcionalmente, categoria complementar;
- opcionalmente, minuto aproximado;
- opcionalmente, nota curta.

Evento de scout nao e:

- texto livre sem classificacao;
- interpretacao geral do jogo;
- relatorio pronto;
- video.

## 4.10 Evento individual

`Evento individual` e um evento de scout associado a um atleta especifico.

Regra:

- um evento individual so pode existir para atleta do elenco oficial do jogo com `presence_status = present` e `participation_status = played`;
- quando o evento depender de funcao contextual, a validacao deve usar atribuicao compativel em `match_role_assignments` para a mesma atleta, jogo e fase;
- atleta ausente ou `did_not_play` nao pode receber evento individual de scout no MVP.
- eventos com `phase_scope = regular_play` so podem usar `match_phase = set_1` ou `set_2`;
- eventos com `phase_scope = shootout_only` so podem usar `match_phase = shootout`;
- nenhum evento com `match_phase = shootout` e valido sem shoot-out real no jogo correspondente.

## 4.11 Evento coletivo

`Evento coletivo` e um evento de scout sem atleta especifico.

Regra:

- um evento coletivo continua pertencendo obrigatoriamente a um jogo real;
- ele nao pode existir como evento solto sem partida.
- no MVP inicial, nao ha `event_type` coletivo no seed canonico;
- observacao coletiva inicial deve ser registrada em `notes`.

## 4.12 Observacao

`Observacao` e texto interpretativo do treinador.

No MVP:

- observacao nao substitui evento canonico;
- observacao complementa dado estruturado;
- observacao deve ser tratada como interpretacao humana, nao como fato comparavel por si so.
- observacao coletiva do MVP inicial deve ser registrada em `notes`;
- observacao coletiva nao entra em contagem automatica comparativa.

## 4.13 Historico por atleta

`Historico por atleta` e a consolidacao cronologica de fatos registrados sobre um atleta.

Deve distinguir claramente:

- presenca em treino;
- presenca e participacao em jogo;
- eventos de scout individuais;
- observacoes vinculadas.

Nao deve misturar como se fossem equivalentes:

- comparecimento;
- participacao;
- desempenho;
- interpretacao tecnica.

## 4.14 Historico coletivo

`Historico coletivo` e a consolidacao da equipe por jogo, competicao e periodo.

Deve mostrar no minimo:

- jogos do recorte;
- resultado de cada jogo;
- presenca agregada;
- contagens simples de eventos canonicos.

## 5. Modelo Semantico do Resultado do Jogo

Para o MVP, o jogo deve ser representado por:

- confronto principal;
- dois sets regulares;
- shoot-out opcional;
- resultado final canonico.

Isso implica:

- o modelo nao deve depender apenas de `team_score` e `opponent_score` agregados;
- o resultado do jogo deve dizer como o confronto terminou;
- a comparacao entre jogos deve poder distinguir vitoria por 2 a 0 de vitoria por shoot-out.

## 6. Tipos Semanticos Minimos do Scout

O MVP deve trabalhar com um conjunto canonico minimo de tipos de evento.

Esses tipos devem ser revisados e aprovados pelo treinador antes do uso produtivo.

Regra de desenho semantico:

- cada `event_type` do MVP deve representar um unico fato primario e mutuamente exclusivo no momento do registro;
- o MVP inicial nao deve tentar decompor o mesmo lance em tecnica, funcao da atleta e valor de pontuacao ao mesmo tempo;
- quando um mesmo lance puder ser descrito por mais de uma dimensao teorica, o vocabulario do MVP deve escolher uma classificacao primaria unica.

Familias minimas:

- finalizacao com sucesso;
- finalizacao sem sucesso;
- defesa da goleira;
- erro tecnico ofensivo;
- recuperacao defensiva;
- exclusao;
- evento de shoot-out;
- observacao coletiva fora do `event_type`, usando `notes`.

## 6.1 Conjunto canonico inicial proposto para aprovacao

Codigos canonicos iniciais:

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

Regra:

- os codigos sao estaveis;
- labels podem mudar;
- sinonimos de digitacao nao podem criar novos codigos canonicos.

Observacao:

- a simples existencia desta lista no documento nao equivale a aprovacao operacional;
- a aprovacao da lista ativa do MVP exige registro humano explicito em [APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md](/docs/05_fases/fase_0/APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md:1).

## 6.2 Convencao de classificacao primaria

Para evitar dupla contagem no MVP inicial, toda finalizacao deve seguir a seguinte prioridade de classificacao:

1. `shootout_scored` ou `shootout_missed`, quando o lance for do shoot-out;
2. `goal_inflight` ou `missed_inflight`, quando a classificacao principal for aerea;
3. `goal_spin_shot` ou `missed_spin_shot`, quando a classificacao principal for giro;
4. `goal_two_point_other` ou `missed_two_point_other`, quando for lance de dois pontos nao classificado como aerea ou giro;
5. `goal_regular` ou `missed_regular`, nos demais casos.

Consequencias:

- um mesmo lance nao pode gerar dois `event_type` de finalizacao;
- `goal_specialist` e `missed_specialist` ficam fora do MVP inicial por ambiguarem funcao e tecnica;
- a especialista nao volta como `event_type`;
- a condicao funcional de especialista ou goleira pertence ao contexto da atribuicao de papel, nao ao tipo primario do evento;
- o MVP inicial nao cria valor proprio `specialist` em `match_role_assignments`;
- quando a mesma atleta possuir `court_player` e `goalkeeper` na mesma fase, essa combinacao pode ser interpretada tecnicamente como contexto de especialista, sem criar novo `event_type`;
- gol de goleira no jogo regular, quando nao classificado como aerea ou giro, entra em `goal_two_point_other`;
- gol comum de um ponto entra em `goal_regular`.

## 6.3 Aplicabilidade minima por tipo de evento

Para o MVP inicial, os tipos canonicos possuem a seguinte semantica minima:

- `goal_spin_shot`: individual, exige `participation_status = played`, aplicavel em jogo regular.
- `goal_inflight`: individual, exige `participation_status = played`, aplicavel em jogo regular.
- `goal_two_point_other`: individual, exige `participation_status = played`, aplicavel em jogo regular.
- `goal_regular`: individual, exige `participation_status = played`, aplicavel em jogo regular.
- `missed_spin_shot`: individual, exige `participation_status = played`, aplicavel em jogo regular.
- `missed_inflight`: individual, exige `participation_status = played`, aplicavel em jogo regular.
- `missed_two_point_other`: individual, exige `participation_status = played`, aplicavel em jogo regular.
- `missed_regular`: individual, exige `participation_status = played`, aplicavel em jogo regular.
- `save_goalkeeper`: individual, exige `participation_status = played`, semanticamente restrito a evento de defesa da goleira.
- `save_goalkeeper` exige atribuicao `goalkeeper` na mesma fase do evento.
- `turnover`: individual, exige `participation_status = played`.
- `steal`: individual, exige `participation_status = played`.
- `block_defense`: individual, exige `participation_status = played`.
- `exclusion_received`: individual, exige `participation_status = played`, representa exclusao sofrida pela propria atleta registrada.
- `shootout_scored`: individual, exige `participation_status = played`, exclusivo de shoot-out.
- `shootout_missed`: individual, exige `participation_status = played`, exclusivo de shoot-out.

Regra:

- `turnover` nao deve ser usado como evento coletivo no MVP;
- eventos de shoot-out nao devem ser usados fora de jogo resolvido por shoot-out;
- `save_goalkeeper` exige atribuicao `goalkeeper` na mesma fase do evento;
- `shootout_scored` e `shootout_missed` exigem `match_phase = shootout`;
- os quinze codigos iniciais aprovados no seed canonico do MVP sao todos `individual_only`;
- `collective_only` fica reservado no schema apenas para expansao futura com nova aprovacao humana explicita;
- observacoes coletivas nao entram em `scout_event_types` do MVP inicial;
- indicadores coletivos devem usar apenas codigos factuais da lista canonica ativa e fatos estruturados de jogo;
- o MVP nao deve inventar novos comportamentos semanticos por tela, relatorio ou seed improvisado.

## 6.4 Categoria complementar

`event_category` no MVP e opcional e so pode existir como classificador complementar de um `event_type`.

Ela nao pode substituir o tipo canonico.

Se utilizada, deve responder a uma pergunta clara, como:

- lado da finalizacao;
- contexto do evento;
- fase ofensiva ou defensiva previamente definida.

Regra operacional do MVP inicial:

- `event_category` nao pode receber texto livre no uso produtivo;
- enquanto nao existir lista controlada aprovada por evento, `event_category` deve permanecer vazia no MVP;
- a primeira versao operacional do MVP deve considerar `event_category = NULL` como padrao.
- a primeira interface operacional do MVP nao deve expor `event_category` como campo editavel;
- o backend deve persistir `NULL` ate que exista vocabulario controlado aprovado.

## 6.5 Minuto

`minute` e opcional no MVP.

Semantica:

- representa referencia temporal aproximada do evento no jogo;
- nao e obrigatorio para que o scout principal seja valido;
- nao pode ser usado como requisito para o fechamento basico da partida.

## 7. Fatos x Interpretacoes

## 7.1 Fatos estruturados

Sao fatos do MVP:

- data do jogo;
- adversario;
- competicao;
- resultado canonico;
- sets registrados;
- shoot-out, quando houver;
- elenco do jogo;
- presenca de treino;
- tipo canonico de evento;
- atleta associado ao evento individual.

## 7.2 Interpretacoes

Sao interpretacoes:

- comentarios do treinador;
- diagnosticos qualitativos;
- observacoes livres;
- leituras taticas nao reduzidas a codigo canonico.

Regra:

- relatorios e historicos devem deixar visualmente claro o que e fato e o que e interpretacao.

## 8. Comparabilidade

Para dois jogos serem comparaveis no MVP, o sistema deve comparar no minimo:

- resultado canonico do confronto;
- placar dos sets;
- shoot-out, se existir;
- elenco oficial;
- contagem simples por `event_type`.

Comparacao entre jogos nao deve se apoiar apenas em:

- texto livre;
- notas avulsas;
- somatorio indistinto de eventos sem tipo canonico.

Indicadores coletivos permitidos no MVP inicial:

- contagem de `goal_spin_shot`
- contagem de `goal_inflight`
- contagem de `goal_two_point_other`
- contagem de `goal_regular`
- contagem de `missed_spin_shot`
- contagem de `missed_inflight`
- contagem de `missed_two_point_other`
- contagem de `missed_regular`
- contagem de `save_goalkeeper`
- contagem de `turnover`
- contagem de `steal`
- contagem de `block_defense`
- contagem de `exclusion_received`
- contagem de `shootout_scored`
- contagem de `shootout_missed`

Observacao:

- notas livres e observacoes coletivas nao entram em contagem automatica comparativa.

## 9. Definition of Done Semantico

Uma entrega do scout so pode ser considerada semanticamente valida quando:

- os termos do dominio usados na interface batem com este documento;
- o resultado do jogo diferencia sets e shoot-out;
- os codigos canonicos ativos do scout foram aprovados pelo treinador e registrados em artefato proprio;
- o historico por atleta separa presenca, participacao, evento e observacao;
- o historico coletivo usa contagens com significado tecnico claro;
- nao ha mistura de conceito de handebol de quadra com handebol de areia.

Para a Fase 0 ser considerada concluida:

- deve existir aprovador humano nomeado;
- deve existir data de aprovacao;
- deve existir versao congelada do vocabulario ativo;
- deve existir regra explicita para `event_category`;
- deve existir convencao explicita de classificacao primaria das finalizacoes;
- deve existir definicao do dataset piloto minimo de validacao semantica.

## 10. Regras de Mudanca

Qualquer alteracao em:

- definicao de jogo;
- definicao de set;
- definicao de shoot-out;
- codigos canonicos do scout;
- significado de `event_category`;
- significado de presenca ou participacao;
- criterio de comparabilidade

obriga revisao da especificacao de implementacao antes de continuar o desenvolvimento.
