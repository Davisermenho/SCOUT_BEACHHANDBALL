---
doc_type: validation_report
tarefa_validada: DH-PONTUACAO-001-AUDIT
status_geral: DH_PONTUACAO_001_AUDITADA_SEMANTICAMENTE_AGUARDANDO_MODELAGEM_MINIMA
gerado_em: "2026-06-23"
nao_e_validacao_total: true
---

# Relatório de Auditoria Semântica — DH-PONTUACAO-001

## Status geral

`DH_PONTUACAO_001_AUDITADA_SEMANTICAMENTE_AGUARDANDO_MODELAGEM_MINIMA`

Esta auditoria avalia se `DH-PONTUACAO-001.md` registra, com fidelidade
literal e coerência semântica mínima controlada, a decisão humana sobre
pontuação necessária para abrir a próxima etapa de modelagem mínima. Esta
auditoria **não** cria ficha conceitual de gol, pontuação, gol
espetacular, gol de giro ou gol aéreo; não cria testes de pontuação; não
gera taxonomia; não gera ontologia; e não resolve `Gol de giro` /
`Gol aéreo` ou `R09-CAT-2026-06-18` por inferência.

## Entradas consultadas

1. `docs/02_domain_knowledge/ontology/04_human_decisions/DH-PONTUACAO-001.md`
2. `docs/02_domain_knowledge/ontology/04_human_decisions/DH-PONTUACAO-001_TEMPLATE.md`
3. `docs/02_domain_knowledge/ontology/00_governance/PONTUACAO-001_SCOPE.md`
4. `docs/02_domain_knowledge/ontology/03_validation/PONTUACAO-001_SCOPING_REPORT.md`
5. `files/Decisões Humanas.md` (bloco `R09-CAT-2026-06-18`)
6. `files/Regras 1–18.md`
7. `files/Apêndices.md`

## Verificação de não-alteração de arquivos fora do escopo

| Arquivo | `sha256` observado | Resultado |
|---|---|---|
| `files/Regras 1–18.md` | `2910328828f564a9301f38adc4b65c200c1f5db9ceec339ec4bd9547985cb9a8` | inalterado |
| `files/Apêndices.md` | `780c2dbc0edc0dc3ce38db099abc75682cd2521755965673068fbc73eb28bf88` | inalterado |
| `files/Decisões Humanas.md` | `350cc441fdcbebf29c0a93f1ed99c68d4ef10eb596bfc42fcb9537511d69c9b9` | inalterado |
| `docs/02_domain_knowledge/ontology/04_human_decisions/DH-PAPEIS-001.md` | `ea6deafce74c33a8b90338f229fd7726890c42ecd6efb541ffc97b34e2a18931` | inalterado |
| `docs/02_domain_knowledge/ontology/04_human_decisions/DH-PAPEIS-001_CLARIFICACAO_Q8.md` | `558c2765b46f64584bb8013022deed4a2fd4ce88c3f5bb8d2ec8318ea2a50a3d` | inalterado |
| `docs/02_domain_knowledge/ontology/04_human_decisions/DH-DIMENSOES-001_HUMAN_VALIDATION.md` | `f94e949076e4a9e71508af094fe2672379d4a4f2a9ddc0deb3646bc60198616f` | inalterado |

`DH-ESP-001` não existe como arquivo isolado neste subprojeto; permanece
preservado como bloco interno de `files/Decisões Humanas.md`.

O worktree, no momento desta auditoria, não contém mudanças pendentes contra
`HEAD`, confirmando que nenhum teste de competência, ficha consolidada ou
arquivo protegido foi alterado para executar esta leitura semântica.

## 1. Fidelidade literal do registro humano

`DH-PONTUACAO-001.md` cumpre a função de registro literal:

- frontmatter correto nas linhas 1–20;
- status correto `DH_PONTUACAO_001_RESPOSTA_HUMANA_REGISTRADA_AGUARDANDO_AUDITORIA` nas linhas 4 e 252;
- 15 respostas literais preservadas nas linhas 36–174;
- erros e formas não normalizadas preservados, incluindo `Papel_Tatico`,
  `Funcao_Situacional`, `gosl`, `aerea` e `6 mentro o` nas linhas 102,
  119, 128, 166 e 173;
- o arquivo declara explicitamente que não cria ficha, teste, taxonomia ou
  ontologia, nem marca `VALIDADO_TOTAL` ou `CONSOLIDADO_VALIDO` (linhas
  29–32).

Não há indício de reescrita semântica indevida do texto humano.

## 2. Decisões humanas explicitamente registradas

As decisões extraídas sem inferência (linhas 176–193) são coerentes com as
respostas literais:

| Decisão | Fonte literal |
|---|---|
| Gol simples de jogadora comum sem colete vale 1 ponto | Resposta 1, linhas 39–42 |
| Gol da Especialista vale 2 pontos | Respostas 2 e 3, linhas 47–50 e 55–58 |
| Não existe gol de Especialista valendo 1 ponto | Resposta 4, linhas 63–66 |
| Gol da Goleira vale 2 pontos | Respostas 2 e 3, linhas 47–50 e 58 |
| Jogadora comum pode marcar gol de 2 pontos por execução espetacular | Resposta 5, linhas 71–73 |
| Gol de giro é subclassificação de Gol_Espetacular | Resposta 6, linhas 78–81 |
| Gol aéreo / ponte aérea é subclassificação de Gol_Espetacular | Resposta 7, linhas 86–89 |
| Gol criativo é descrição/jargão, não classe isolada | Resposta 8, linhas 94–97 |
| Tiro de 6 metros vale 2 pontos | Respostas 2 e 13, linhas 49–50 e 139–142 |
| `R09-CAT-2026-06-18` é axioma de amarração da Regra 9 para validação de pontos | Resposta 13, linhas 137–142 |
| A lógica declarada para pontuação segue a ordem gol -> tiro de 6m -> Especialista -> Giro/Aéreo -> gol simples | Resposta 13, linhas 137–142 |

Não foi acrescentada nenhuma decisão que não tenha apoio textual direto.

## 3. Inferências proibidas preservadas

As duas inferências proibidas declaradas nas linhas 195–198 correspondem
literalmente à resposta 14:

- `Papel_Tatico = Atacante_Normal` + `Finalização_Simples` não pode gerar `Valor_do_Gol = 2`
- `Papel_Tatico = Especialista` não pode gerar `Valor_do_Gol = 1`

Essas duas proibições são semanticamente coerentes com o restante das
respostas e funcionam como gates negativos mínimos para a próxima etapa.

## 4. Tratamento dos quatro pontos obrigatórios de auditoria

### QTD-TESTES-001

Situação:

- a resposta 15 declara “estes 5 testes” (linha 159);
- em seguida enumera 6 testes (linhas 162–174).

Decisão da auditoria:

- **não corrigir automaticamente**;
- a divergência é real e foi corretamente registrada como pendência nas
  linhas 211–213;
- isso **não bloqueia** a modelagem mínima, desde que a próxima etapa trate
  explicitamente o conjunto como “lista humana com cardinalidade ambígua”.

Status: `PENDENCIA_CONTROLADA`

### TERM-GOLEIRO-EM-LINHA-001

Situação:

- a resposta 10 usa a expressão “estatuto de Goleiro em Linha” (linhas
  110–113) para explicar por que o colete aciona pontuação de 2 pontos;
- as quatro dimensões já consolidadas separam `Papel_Tático` de
  `Papel_Regulamentar`.

Decisão da auditoria:

- a expressão deve ser **preservada como fala humana sobre pontuação**;
- ela **não autoriza**, nesta etapa, fundir `Especialista` com `Goleiro`
  nem reclassificar automaticamente o papel da atleta;
- a leitura segura é: o especialista humano invoca o vínculo entre colete,
  regra e pontuação, mas a reconciliação formal entre esse vocabulário e a
  separação já consolidada de papéis precisa ficar para modelagem/auditoria
  posterior, não por inferência agora.

Status: `PENDENCIA_CONTROLADA`

### FUNCAO-ALTERA-VALOR-001

Situação:

- a resposta 11 afirma que `Funcao_Situacional` pode alterar o valor final
  do gol no caso de jogadoras comuns (linhas 118–120).

Decisão da auditoria:

- isso é semanticamente compatível com o bloco já consolidado, desde que se
  preserve a distinção entre:
  - valor do gol;
  - `Papel_Tático`;
  - `Papel_Regulamentar`.
- a própria decisão humana anterior sobre as quatro dimensões já aceitava
  que `Função_Situacional` não altera os papéis, mas pode coexistir com
  efeitos de pontuação em milissegundo de execução.

Portanto:

- a fala deve ser aceita como **regra de pontuação**, não como colapso das
  dimensões estruturais.

Status: `PENDENCIA_CONTROLADA`

### R09-CAT-001

Situação:

- a resposta 13 define `R09-CAT-2026-06-18` como axioma de amarração da
  Regra 9 (linhas 137–142);
- `files/Decisões Humanas.md` já contém `R09-CAT-2026-06-18` aprovado,
  incluindo `Gol criativo`, `Gol espetacular`, `Gol em aérea` e a proibição
  de criar limiar automático ausente na fonte (linhas 147–161 do arquivo
  consultado);
- `files/Regras 1–18.md` e `files/Apêndices.md` já registram que
  `Gol criativo`, `Gol espetacular`, `Gol em aérea` e `Tiro de 6 Metros`
  possuem valor de 2 pontos, mas também mantêm essas categorias sob
  avaliação humana controlada.

Decisão da auditoria:

- a resposta humana é **compatível** com o conjunto documental existente no
  nível de escopo e amarração;
- porém ela ainda **não autoriza** transformar isso diretamente em regra
  executável sem uma etapa própria de modelagem mínima e posterior validação.

Status: `PENDENCIA_CONTROLADA`

## 5. Base suficiente para a próxima modelagem mínima?

Sim, com limites.

Esta auditoria conclui que existe base semântica suficiente para abrir a
**modelagem mínima de pontuação**, desde que a próxima tarefa continue
obedecendo aos seguintes limites:

- não inferir nova categoria a partir de texto ambíguo;
- não fundir `Especialista` e `Goleiro`;
- não usar pontuação para reclassificar `Papel_Tático` ou
  `Papel_Regulamentar`;
- não transformar `Gol criativo` em classe consolidada só porque ele foi
  mencionado;
- não transformar o bloco atual diretamente em regra executável;
- não alterar as quatro fichas já consolidadas.

O que fica semanticamente autorizado pela auditoria é apenas a próxima
**modelagem mínima controlada** do bloco `PONTUACAO-001`, não a sua
consolidação final.

## 6. Itens ainda bloqueados

Continuam bloqueados após esta auditoria:

- criação de ficha conceitual de `Gol`;
- criação de ficha conceitual de `Pontuação`;
- criação de ficha conceitual de `Gol_Espetacular`;
- criação de ficha conceitual de `Gol_de_Giro`;
- criação de ficha conceitual de `Gol_Aereo`;
- criação de testes de competência de pontuação;
- criação de taxonomia geral;
- geração de ontologia principal;
- alteração de `Regras 1–18.md`, `Apêndices.md`, `Decisões Humanas.md`;
- marcação de `VALIDADO_TOTAL`;
- marcação de `CONSOLIDADO_VALIDO`.

## Critérios da auditoria

| # | Critério | Resultado |
|---|---|---|
| 1 | `DH-PONTUACAO-001.md` existe e está com status de resposta humana aguardando auditoria | APROVADO |
| 2 | As 15 respostas humanas foram preservadas literalmente | APROVADO |
| 3 | O bloco `decisoes_extraidas_sem_inferencia` contém apenas decisões explicitamente declaradas | APROVADO |
| 4 | O bloco `inferencias_proibidas_declaradas` preserva as duas proibições humanas | APROVADO |
| 5 | O bloco `casos_de_teste_declarados` preserva a divergência “5 testes” vs “6 testes” | APROVADO |
| 6 | Os quatro pontos de auditoria obrigatórios foram tratados sem resolução por inferência | APROVADO |
| 7 | Os limites da decisão foram preservados | APROVADO |
| 8 | Nenhuma ficha, teste, taxonomia ou ontologia foi criada por esta auditoria | APROVADO |
| 9 | Arquivos protegidos permaneceram intocados | APROVADO |

## Decisão recomendada

Aceitar `DH-PONTUACAO-001-AUDIT` com status
`DH_PONTUACAO_001_AUDITADA_SEMANTICAMENTE_AGUARDANDO_MODELAGEM_MINIMA`.

Esta decisão **não** autoriza ainda:

- criar regra executável de pontuação;
- consolidar categorias finais;
- iniciar testes de competência de pontuação;
- modelar ontologia principal;
- marcar qualquer artefato deste bloco como `VALIDADO_TOTAL` ou
  `CONSOLIDADO_VALIDO`.

Próxima ação autorizada por esta auditoria: preparar uma tarefa explícita
de **modelagem mínima de pontuação**, ainda controlada por decisão humana e
sem extrapolar os limites acima.
