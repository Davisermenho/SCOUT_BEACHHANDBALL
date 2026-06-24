```yaml
CONTRATO FUNCIONAL — PLANILHA CEPRAEA

1. OBJETIVO
A Planilha CEPRAEA é o sistema oficial de gestão competitiva da equipe. Sua finalidade é registrar disponibilidade de atletas, apoiar decisões de convocação, monitorar risco competitivo e fornecer visão executiva da temporada.

2. PRINCÍPIO DE AUTORIDADE
2.1 A planilha é uma ferramenta operacional.
2.2 A decisão final pertence ao treinador.
2.3 Nenhum cálculo automático substitui validação humana.
2.4 A agenda é fonte primária para disponibilidade das atletas.

3. ARQUITETURA DAS ABAS

3.1 AGENDA CEPRAEA
Responsabilidade: registro operacional de disponibilidade.
Entradas permitidas: SIM, NAO, TALVEZ.
Saídas esperadas: atletas disponíveis por competição.
Critérios de aceite:
- atletas nas linhas;
- competições nas colunas;
- leitura rápida;
- preenchimento simples;
- sem lógica complexa.

3.2 PAINEL COMPETITIVO
Responsabilidade: tomada de decisão.
Indicadores mínimos:
- disponíveis;
- confirmadas;
- talvez;
- não;
- risco competitivo.
Critério de aceite: nenhuma contagem manual necessária.

3.3 INDICE DE RISCO
Classificação:
- >=14 atletas: BAIXO RISCO;
- 11 a 13 atletas: MEDIO RISCO;
- 9 a 10 atletas: ALTO RISCO;
- <=8 atletas: CRITICO.
Critério de aceite: cálculo automático.

3.4 FUNCOES DA EQUIPE
Categorias:
- goleiras;
- defensoras;
- ataque.
Objetivo: avaliar capacidade real de competição.
Critério de aceite: toda atleta possui função cadastrada.

3.5 DASHBOARD EXECUTIVO
Indicadores mínimos:
- temporada;
- próxima competição;
- disponibilidade atual;
- status geral.
Critério de aceite: leitura inferior a 5 segundos.

3.6 ROADMAP COMPETITIVO
Status permitidos:
- concluído;
- confirmado;
- aguardando confirmação;
- crítico.
Objetivo: visualizar situação da temporada.

4. PADRAO VISUAL
Paleta institucional:
- preto institucional;
- roxo escuro CEPRAEA;
- branco;
- cinza claro.
Evitar:
- verde neon;
- vermelho excessivamente saturado;
- amarelo excessivamente saturado.

Tipografia recomendada:
- Inter;
- Aptos;
- Segoe UI.

5. CRITERIOS GLOBAIS DE ACEITE
O sistema deverá responder em menos de 5 segundos:
1. Qual é a próxima competição?
2. Quantas atletas tenho?
3. Quantas confirmaram?
4. Quantas estão pendentes?
5. Estou em risco?
6. Qual função está em risco?
7. Quem preciso contatar?
8. Qual a situação da temporada?

6. REGRA DE EVOLUCAO
Toda nova aba deverá possuir:
- objetivo definido;
- entradas definidas;
- saídas definidas;
- critérios de aceite;
- responsável pela manutenção.

7. REGRA DE GOVERNANCA
Nenhuma automação, IA ou agente poderá alterar a semântica das métricas, classificações ou critérios sem aprovação humana explícita.

8. CONTRATO DETALHADO POR ABA

8.1 ABA: AGENDA CEPRAEA
Finalidade: registrar a disponibilidade individual das atletas por competição da temporada.
Proprietário da informação: treinador responsável pela equipe.
Entradas autorizadas:
- SIM = atleta disponível;
- NAO = atleta indisponível;
- TALVEZ = confirmação pendente;
- campos administrativos: inscrição até, taxa e relação nominal até.
Saídas autorizadas:
- total de atletas disponíveis por competição;
- identificação visual de etapas seguras, em atenção, em risco ou críticas.
Fórmulas autorizadas:
- contagem de SIM por competição;
- contagem de NAO por competição;
- contagem de TALVEZ por competição;
- classificação de risco por quantidade disponível.
Dependências:
- lista oficial de atletas;
- calendário competitivo;
- decisões humanas de confirmação.
Critérios de aceite verificáveis:
- a aba preserva atletas nas linhas e competições nas colunas;
- o preenchimento aceita apenas SIM, NAO ou TALVEZ nas células de disponibilidade;
- a linha Atletas disponíveis reflete o número real de respostas SIM;
- nenhuma célula de disponibilidade deve conter texto livre fora dos status autorizados;
- a leitura da disponibilidade deve ser possível sem contagem manual.
Riscos operacionais:
- atleta marcada como SIM sem confirmação real;
- TALVEZ mantido até perto do prazo de inscrição;
- alteração manual de fórmulas;
- confusão entre ausência de resposta e NAO.
Regra de alteração:
- novas competições podem ser adicionadas somente mantendo o mesmo padrão de colunas;
- novas atletas podem ser adicionadas somente mantendo o padrão de linhas e validação de status.

8.2 ABA: PAINEL COMPETITIVO
Finalidade: converter a agenda operacional em decisão executiva.
Proprietário da informação: treinador responsável pela equipe.
Entradas autorizadas:
- dados calculados a partir da AGENDA CEPRAEA;
- próxima competição definida pelo treinador;
- status da etapa definido por regra automática e validado humanamente.
Saídas autorizadas:
- total de disponíveis;
- total de confirmadas;
- total de TALVEZ;
- total de NAO;
- risco competitivo por etapa;
- pendências críticas.
Fórmulas autorizadas:
- CONT.SE para SIM, NAO e TALVEZ;
- SE/IFS para classificação de risco;
- filtros para atletas pendentes.
Dependências:
- AGENDA CEPRAEA;
- FUNCOES DA EQUIPE;
- INDICE DE RISCO.
Critérios de aceite verificáveis:
- o painel não exige contagem manual;
- os indicadores mudam automaticamente quando a agenda é atualizada;
- a próxima competição fica visível na primeira área da aba;
- o painel responde em até 5 segundos se a equipe está segura, em atenção ou em risco.
Riscos operacionais:
- painel desconectado da agenda;
- fórmulas quebradas por alteração de intervalo;
- excesso de informação prejudicando leitura no celular.
Regra de alteração:
- novos indicadores só podem ser adicionados se ajudarem decisão competitiva direta.

8.3 ABA: INDICE DE RISCO
Finalidade: padronizar a classificação de risco competitivo da equipe.
Proprietário da informação: treinador responsável.
Entradas autorizadas:
- quantidade de atletas disponíveis;
- quantidade mínima por função essencial;
- peso de criticidade individual, quando aplicado.
Saídas autorizadas:
- BAIXO RISCO;
- MEDIO RISCO;
- ALTO RISCO;
- CRITICO.
Regra base:
- 14 ou mais atletas disponíveis = BAIXO RISCO;
- 11 a 13 atletas disponíveis = MEDIO RISCO;
- 9 a 10 atletas disponíveis = ALTO RISCO;
- 8 ou menos atletas disponíveis = CRITICO.
Regra funcional:
- ausência de goleira disponível eleva o risco para CRITICO;
- quantidade insuficiente de defensoras eleva o risco em pelo menos um nível;
- quantidade insuficiente de atletas de ataque eleva o risco em pelo menos um nível;
- ausência de atleta crítica deve gerar alerta, mesmo que o total geral esteja alto.
Critérios de aceite verificáveis:
- cada competição recebe um risco final;
- o risco final combina quantidade total e funções essenciais;
- o risco não depende apenas da cor visual;
- toda regra de risco deve ser explícita e auditável.
Riscos operacionais:
- classificar como seguro apenas pelo número total de atletas;
- ignorar ausência de função essencial;
- permitir que uma regra implícita seja aplicada sem documentação.

8.4 ABA: FUNCOES DA EQUIPE
Finalidade: cadastrar a função competitiva de cada atleta.
Proprietário da informação: treinador responsável.
Entradas autorizadas:
- nome da atleta;
- função principal;
- função secundária;
- criticidade;
- observação técnica, quando necessário.
Categorias autorizadas:
- GOLEIRA;
- DEFENSORA;
- ATAQUE.
Criticidade autorizada:
- MUITO ALTA;
- ALTA;
- MEDIA;
- BAIXA.
Saídas autorizadas:
- totais por função em cada competição;
- alertas de ausência funcional;
- suporte ao índice de risco.
Critérios de aceite verificáveis:
- toda atleta da agenda possui função principal cadastrada;
- nenhuma atleta ativa fica sem classificação;
- função e criticidade são usadas apenas para decisão técnica, não como julgamento pessoal;
- alterações de função exigem validação humana.
Riscos operacionais:
- atleta cadastrada em função errada;
- função secundária usada como substituta automática sem decisão técnica;
- criticidade interpretada como valor humano da atleta e não como impacto competitivo.

8.5 ABA: DASHBOARD EXECUTIVO
Finalidade: fornecer leitura imediata da situação competitiva.
Proprietário da informação: treinador responsável.
Cards mínimos:
- Temporada;
- Próxima competição;
- Disponibilidade;
- Status geral.
Saídas autorizadas:
- visão executiva da temporada;
- alerta de pendências;
- risco da próxima etapa;
- indicação de ação necessária.
Critérios de aceite verificáveis:
- as informações principais aparecem acima da dobra visual;
- a leitura funciona no celular;
- o treinador entende a situação sem rolar a planilha;
- o dashboard não substitui a agenda operacional.
Riscos operacionais:
- excesso de cards;
- dashboard visualmente bonito, mas sem decisão útil;
- divergência entre dashboard e dados da agenda.

8.6 ABA: ROADMAP COMPETITIVO
Finalidade: mostrar o andamento da temporada por etapa.
Proprietário da informação: treinador responsável.
Status autorizados:
- CONCLUIDO;
- CONFIRMADO;
- AGUARDANDO CONFIRMACAO;
- CRITICO.
Saídas autorizadas:
- visão da temporada inteira;
- identificação de etapas pendentes;
- apoio à priorização semanal.
Critérios de aceite verificáveis:
- toda competição da agenda aparece no roadmap;
- cada etapa possui um status único;
- etapas críticas ficam visíveis sem interpretação manual;
- a legenda do status está presente.
Riscos operacionais:
- etapa vencida sem atualização para CONCLUIDO;
- etapa crítica sem ação definida;
- roadmap desconectado da agenda.

9. CONTRATO DE DADOS
9.1 Status de disponibilidade
Valores válidos:
- SIM;
- NAO;
- TALVEZ.
Valores inválidos:
- sim;
- não;
- N;
- OK;
- confirmado;
- qualquer texto livre.

9.2 Campos administrativos
Campos obrigatórios por competição:
- nome da competição;
- cidade/UF;
- data ou período;
- inscrição até;
- taxa;
- relação nominal até.

9.3 Campos técnicos
Campos obrigatórios por atleta:
- nome;
- função principal;
- criticidade.
Campos opcionais:
- função secundária;
- observação técnica.

10. CONTRATO DE DESIGN
10.1 Hierarquia visual obrigatória
    1. Título institucional;
    2. Dashboard executivo;
    3. prazos administrativos;
    4. matriz de disponibilidade;
    5. totais e risco;
    6. legenda.

10.2 Cores autorizadas
    - verde institucional para cabeçalhos e divisórias principais;
- branco para fundo principal;
- cinza claro para blocos administrativos;
- verde suave para SIM;
- vermelho suave para NAO;
- amarelo suave para TALVEZ;
- vermelho moderado apenas para risco crítico.

10.3 Cores proibidas
- verde neon;
- vermelho saturado dominante;
- amarelo saturado dominante;
- excesso de bordas fortes.

10.4 Critérios de aceite visual
- cabeçalhos legíveis;
- bordas suaves;
- status centralizados;
- legenda visível;
- leitura funcional no celular;
- ausência de poluição visual.

11. CONTRATO DE MANUTENCAO
11.1 Quem pode alterar dados
O treinador pode alterar disponibilidade, funções, criticidade, prazos e status da temporada.

11.2 Quem pode alterar estrutura
A estrutura só pode ser alterada após validação humana explícita do novo contrato da aba.

Alterações proibidas sem aprovação
- "alterar regras de risco"
- "alterar categorias de função;
- "alterar significado de SIM, NAO ou TALVEZ;
- "remover campos obrigatórios;
- "substituir contagem automática por contagem manual.

12. CRITERIOS DE PRONTO
A Planilha CEPRAEA estará pronta quando:
- a agenda registrar disponibilidade sem ambiguidade;
- o painel calcular indicadores automaticamente;
- o índice de risco indicar a situação de cada competição;
- a visão por função mostrar capacidade real de competir;
- o dashboard responder a situação em menos de 5 segundos;
- o roadmap mostrar o estado da temporada;
- a governança impedir alteração semântica por IA ou edição acidental;
- o treinador conseguir decidir a próxima ação operacional da semana.

Utilizar este arquivo para escrever o contrato de CEPRAEA. 
Link obrigatório
```


# Revisao v2: PROBLEMA_FINAL x MVP

## Finalidade

Este documento substitui operacionalmente a leitura da auditoria anterior [REVISAO_COMPLETA_PROBLEMA_FINAL_X_MVP.md](/home/davis/SCOUT_BEACHHANDBALL/REVISAO_COMPLETA_PROBLEMA_FINAL_X_MVP.md:1), que ficou parcialmente desatualizada apos as revisoes do `MVP.md`.

Objetivo:

- recalcular os achados contra a versao atual do [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:1);
- separar o que foi corrigido, o que permanece parcial e o que saiu do escopo da auditoria;
- preparar o terreno para implementacao assistida por IA.

## Escopo da revisao

Documentos auditados:

- [PROBLEMA_FINAL.md](/home/davis/SCOUT_BEACHHANDBALL/PROBLEMA_FINAL.md:1)
- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:1)

Fora desta revisao:

- coerencia interna da ontologia;
- coerencia tecnica da especificacao de implementacao.

Esses pontos sao cobertos em auditorias separadas.

## Veredito atualizado

O `MVP.md` atual esta substancialmente mais alinhado ao `PROBLEMA_FINAL.md` do que a auditoria anterior registrava.

Status atual:

- `cobertura estrutural`: forte
- `cobertura de restricoes`: forte
- `cobertura de escopo funcional`: forte
- `provas operacionais`: forte no papel
- `dependencia semantica da ontologia`: explicita, com baseline tecnico minimo validado
- `aprovacao humana da Fase 0`: em `aguardando_revalidacao_humana`

Conclusao:

- a auditoria antiga nao deve mais ser usada como gate final sem consulta a esta v2;
- o `MVP.md` atual corrige varios problemas antes apontados;
- os gaps remanescentes deixam de ser "ausencia de ontologia" e passam a se concentrar em ratificacao humana do freeze, implementacao e prova executavel.

## Itens da auditoria anterior que estao superados

### 1. Video como obrigatorio

Status anterior:

- a auditoria antiga apontava desvio de escopo porque video aparecia como obrigatorio.

Status atual:

- corrigido.

Evidencia:

- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:125) declara video como apoio opcional, nao modulo obrigatorio.

### 2. Falta de governanca de alinhamento com o SSOT

Status anterior:

- a auditoria antiga apontava ausencia de regra explicita de governanca.

Status atual:

- corrigido.

Evidencia:

- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:16) define regra de alinhamento com o `PROBLEMA_FINAL.md`.

### 3. Fontes legadas mal tratadas

Status anterior:

- a auditoria antiga apontava cobertura apenas indireta.

Status atual:

- parcialmente corrigido.

Evidencia:

- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:153) define regra de conversao das fontes legadas.

Ressalva:

- a existencia da regra resolve a direcao;
- a implementacao ainda precisa provar isso em fluxo real.

### 4. Historico coletivo insuficiente

Status anterior:

- a auditoria antiga tratava historico coletivo como subprovado.

Status atual:

- melhorado, mas ainda requer prova executavel forte.

Evidencia:

- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:332) e [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:867) ampliam a definicao e a prova de historico coletivo.

## Itens atualmente alinhados

### 1. Contexto de treinador solo

Alinhado.

Evidencia:

- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:57)

### 2. Dominio exclusivo de handebol de areia

Alinhado.

Evidencia:

- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:58)
- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:34)

### 3. MVP simples e de baixa manutencao

Alinhado.

Evidencia:

- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:55)
- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:83)

### 4. Proibicao de IA de video e visao computacional

Alinhado.

Evidencia:

- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:68)
- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:130)

### 5. Centralizacao dos dados em fonte unica

Alinhado.

Evidencia:

- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:86)

### 6. Scout pos-jogo e nao em tempo real

Alinhado.

Evidencia:

- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:287)

### 7. Integridade de elenco do jogo

Alinhado no nivel de MVP.

Evidencia:

- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:412)
- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:515)

### 8. Preservacao de dados desde o inicio

Alinhado no plano.

Evidencia:

- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:698)

## Itens ainda parciais

### 1. Reducao de carga operacional

Status:

- alinhado no papel.

Motivo:

- o MVP passou a fixar limite inicial de tempo, limite de correcoes e exigencia de 2 jogos reais.

Evidencia:

- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:891)

### 2. Verificabilidade do historico coletivo

Status:

- parcial.

Motivo:

- o MVP define melhor a prova, mas o consolidado minimo ainda depende da ontologia e da especificacao de implementacao.

Evidencia:

- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:867)

### 3. Semantica do resultado do jogo

Status:

- alinhado no nivel do MVP.

Motivo:

- o MVP ja define `result_type`, `match_sets`, `match_shootouts`, `completion_status` e reabertura controlada, sem conflito com o problema-fonte.

Evidencia:

- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:417)

### 4. Golden Goal

Status:

- alinhado no nivel do MVP.

Motivo:

- o MVP passa a distinguir Golden Goal como decisao de set, mantendo shoot-out como desempate de jogo apos sets 1-1.

Evidencia:

- [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:447)

## Estado atual do gate documental

O ponto mais critico antes desta revisao estava fora do `MVP.md` isolado.

Status atual:

- a ontologia do scout foi tratada como documento obrigatorio da cadeia de auditoria;
- o baseline tecnico minimo da ontologia ja existe e foi validado;
- a Fase 0 continua em `aguardando_revalidacao_humana`.

Ressalva:

- isso nao substitui implementacao, piloto real nem teste.
- isso tambem nao substitui a ratificacao humana do baseline congelado vigente.

## Decisao

Esta revisao v2 substitui a leitura operacional da auditoria antiga para qualquer decisao de continuidade.

Ela nao libera implementacao sozinha, mas deixa de ser bloqueio documental da Fase 0.

Liberacao documental exige leitura conjunta de:

1. [PROBLEMA_FINAL.md](/home/davis/SCOUT_BEACHHANDBALL/PROBLEMA_FINAL.md:1)
2. [MVP.md](/home/davis/SCOUT_BEACHHANDBALL/MVP.md:1)
3. [ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md](/home/davis/SCOUT_BEACHHANDBALL/ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md:1)
4. [ESPECIFICACAO_IMPLEMENTACAO_MVP.md](/home/davis/SCOUT_BEACHHANDBALL/ESPECIFICACAO_IMPLEMENTACAO_MVP.md:1)
