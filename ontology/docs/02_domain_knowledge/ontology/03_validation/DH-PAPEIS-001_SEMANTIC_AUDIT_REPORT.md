---
doc_type: validation_report
tarefa_validada: DH-PAPEIS-001-SEMANTIC-AUDIT
status_geral: DH_PAPEIS_001_AUDITADA_SEMANTICAMENTE_AUTORIZANDO_FICHAS_MINIMAS
gerado_em: "2026-06-23"
nao_e_validacao_total: true
nao_autoriza_ficha_para_alem_dos_quatro_termos: true
---

# Relatório de Auditoria Semântica — DH-PAPEIS-001

## Status geral

`DH_PAPEIS_001_AUDITADA_SEMANTICAMENTE_AUTORIZANDO_FICHAS_MINIMAS`

Esta auditoria avalia se as 10 respostas literais de `DH-PAPEIS-001.md`,
complementadas pela clarificação validada `DH-PAPEIS-001_CLARIFICACAO_Q8.md`,
fornecem base literal suficiente para autorizar a criação de **ficha
conceitual mínima** para os quatro termos originalmente pendentes
(`Papel_Tático`, `Papel_Regulamentar`, `Função_Situacional`,
`Posição_Espacial`). Esta auditoria **não cria** nenhuma ficha conceitual,
taxonomia ou ontologia — apenas autoriza que a próxima etapa o faça. Os
demais conceitos citados nas respostas humanas (sistemas táticos, papéis
nomeados, status operacional etc.) permanecem bloqueados, conforme seção 6.

## Entradas consultadas

1. `docs/02_domain_knowledge/ontology/04_human_decisions/DH-PAPEIS-001.md`
2. `docs/02_domain_knowledge/ontology/04_human_decisions/DH-PAPEIS-001_CLARIFICACAO_Q8.md`
3. `docs/02_domain_knowledge/ontology/03_validation/DH-PAPEIS-001_CLARIFICACAO_Q8_VALIDATION_REPORT.md`
4. `docs/02_domain_knowledge/ontology/01_concepts/CONCEPT_PAPEIS_SEPARACAO_MINIMA.yaml`
5. `docs/02_domain_knowledge/ontology/00_governance/VOCABULARIO_CANONICO_MINIMO.md`

## Verificação de não-alteração de arquivos fora do escopo

| Arquivo | Tamanho esperado | Tamanho atual | Resultado |
|---|---|---|---|
| `files/Regras 1–18.md` | 155662 bytes | 155662 bytes | inalterado |
| `files/Apêndices.md` | 47720 bytes | 47720 bytes | inalterado |
| `files/Decisões Humanas.md` (contém DH-ESP-001) | 18443 bytes | 18443 bytes | inalterado |
| `DH-PAPEIS-001.md` | 9389 bytes | 9389 bytes | inalterado |
| `DH-PAPEIS-001_CLARIFICACAO_Q8.md` | 4713 bytes | 4713 bytes | inalterado |

Diretório `01_concepts/` inspecionado: contém apenas
`CONCEPT_PAPEIS_SEPARACAO_MINIMA.yaml`, `FICHA_CONCEITUAL_ESPECIALISTA.yaml`
e `FICHA_CONCEITUAL_GOLEIRO.yaml`, todos pré-existentes. Nenhum arquivo de
ficha conceitual novo foi criado por esta auditoria.

## 1. Definições humanas literais das quatro dimensões

| Dimensão | Definição literal existe? | Fonte |
|---|---|---|
| `Papel_Tático` | Sim | DH-PAPEIS-001, resposta 1 |
| `Papel_Regulamentar` | Sim | DH-PAPEIS-001, resposta 2 |
| `Função_Situacional` | Sim | DH-PAPEIS-001, resposta 3 |
| `Posição_Espacial` | Sim | DH-PAPEIS-001, resposta 4 |

Isso supera o estado anterior, em que `VOCABULARIO_CANONICO_MINIMO.md` e
`CONCEPT_PAPEIS_SEPARACAO_MINIMA.yaml` marcavam os três últimos termos como
`PENDENTE_DEFINICAO_LITERAL` por ausência de decisão humana literal
própria. Esta auditoria não edita esses dois arquivos; apenas constata que
a lacuna que eles registravam foi preenchida por `DH-PAPEIS-001`.

As definições de `Papel_Regulamentar` e `Posição_Espacial` citam, como
exemplos, conceitos ainda não definidos extensionalmente
(`Sistema_3:1`, `Sistema_4:0`, sistemas de defesa, etc. — ver seção 4). Essa
citação por exemplo é o mesmo padrão já aceito em `DH-ESP-001` (que cita
`Area_De_Gol` sem defini-la por extenso) e não bloqueia, por si só, a ficha
mínima da dimensão principal.

## 2. Relações declaradas

| Relação | Confirmada literalmente? | Fonte |
|---|---|---|
| Papel_Tático e Papel_Regulamentar são distintos, mas se articulam | Sim | DH-PAPEIS-001, resposta 5 ("São distintos, mas se articulam...") |
| Função_Situacional e Posição_Espacial são sempre distintas | Sim | DH-PAPEIS-001, resposta 6 ("Sim, sempre...") |
| Função_Situacional não altera papel do atleta | Sim | DH-PAPEIS-001, resposta 7 ("Não. ... não altera o seu papel tático ... nem seu papel regulamentar") |
| Posição_Espacial não altera Papel_Tático | Sim, por clarificação | A resposta original 8 era ambígua (marcada `PENDENTE_CLARIFICACAO_HUMANA`); `DH-PAPEIS-001_CLARIFICACAO_Q8.md` resolve isso literalmente: "a posição espacial isolada não altera o papel tático" |
| Linha_Lateral altera Status_Operacional/Regulamentar, não Papel_Tático | Sim, por clarificação | DH-PAPEIS-001_CLARIFICACAO_Q8.md, bloco `efeito_semantico_declarado` |

Todas as cinco relações exigidas por esta tarefa têm fonte literal
identificável. Nenhuma foi completada por inferência do agente.

## 3. Inferências proibidas preservadas

| Inferência proibida | Fonte literal |
|---|---|
| Não inferir Papel_Tático pela Posição_Espacial | DH-ESP-001 (`inferencias_proibidas`); reafirmada em DH-PAPEIS-001_CLARIFICACAO_Q8.md |
| Não inferir Papel_Tático pela Função_Situacional | CONCEPT_PAPEIS_SEPARACAO_MINIMA.yaml (`INF-PROIB-PAPEIS-002`, registrada por instrução explícita de tarefa anterior, não como fala literal de DH-ESP-001); consistente com DH-PAPEIS-001 resposta 7 |
| Não confundir Status_Operacional com Papel_Tático | DH-PAPEIS-001_CLARIFICACAO_Q8.md, bloco `inferencias_proibidas` |
| Não permitir mais de uma Especialista ativa simultaneamente | DH-PAPEIS-001, resposta 9 ("PROIBIR: Mais de uma jogadora com o papel tático de Especialista... ativa em quadra simultaneamente") |
| Não permitir troca Jogador_de_Linha → Goleira | DH-PAPEIS-001, resposta 9 ("PROIBIR: Se Atleta_Saindo = Jogador_de_Linha AND Atleta_Entrando = Goleira") |
| Não apontar erro por ausência de pivô no Sistema_4:0 | DH-PAPEIS-001, resposta 9 |
| Não computar gol simples de jogadora comum como 2 pontos | DH-PAPEIS-001, resposta 10, Contraexemplo 1 |
| Não validar substituição pela linha lateral oposta | DH-PAPEIS-001, resposta 10, Contraexemplo 2 |

Todas as 8 inferências proibidas exigidas por esta tarefa têm fonte
literal rastreável e nenhuma foi reformulada de modo a alterar seu sentido
original.

## 4. Conceitos candidatos citados nas respostas humanas

Classificação de cada conceito citado, sem promoção a ficha consolidada:

| Conceito | Classificação | Justificativa |
|---|---|---|
| `Papel_Tático` | Ver seção 5 | Dimensão principal desta auditoria |
| `Papel_Regulamentar` | Ver seção 5 | Dimensão principal desta auditoria |
| `Função_Situacional` | Ver seção 5 | Dimensão principal desta auditoria |
| `Posição_Espacial` | Ver seção 5 | Dimensão principal desta auditoria |
| `Especialista` | NÃO_CRIAR_AGORA | Já `DECLARADO_LITERAL` em DH-ESP-001/VOCAB-MIN-001; fora do escopo desta auditoria, não reclassificar aqui |
| `Goleiro` | NÃO_CRIAR_AGORA | Já `DECLARADO_LITERAL`; fora do escopo desta auditoria |
| `Jogador_De_Linha` | CANDIDATO_PENDENTE_DEFINICAO | Citado nas respostas 2 e 9; já listado `PENDENTE_DEFINICAO_LITERAL` em VOCAB-MIN-001; respostas de DH-PAPEIS-001 acrescentam contexto mas não uma definição extensional completa própria |
| `Status_Operacional` | CANDIDATO_PENDENTE_DEFINICAO | Definido em DH-PAPEIS-001_CLARIFICACAO_Q8.md, porém listado explicitamente como bloqueado para consolidação nesta etapa |
| `Status_Regulamentar` | CANDIDATO_PENDENTE_DEFINICAO | Idem |
| `Status_da_Equipe` | CANDIDATO_PENDENTE_DEFINICAO | Idem |
| `Ativa_Em_Quadra` / `Inativa` / `Em_Espera` / `Banco` | CANDIDATO_PENDENTE_DEFINICAO | Citados como valores de Status_Operacional na clarificação Q8, sem definição formal própria |
| `Linha_Lateral` | CANDIDATO_PENDENTE_DEFINICAO | Citada nas respostas 4, 8, 9, 10 e na clarificação; papel duplo (geográfico e regulamentar) ainda não consolidado em ficha própria |
| `Área_De_Substituição` | CANDIDATO_PENDENTE_DEFINICAO | Citada nas respostas 4 e na clarificação Q8, sem definição extensional isolada |
| `Gatilho_Regulamentar` / `Gatilho_De_Transição` | CANDIDATO_PENDENTE_DEFINICAO | Termos introduzidos na clarificação Q8 como mecanismo, não como classe definida |
| `Transição_Híbrida` | CANDIDATO_PENDENTE_DEFINICAO | Citada nas respostas 1 e 10 como estratégia nomeada, sem critérios extensionais completos |
| `Retarda-Ataque` | CANDIDATO_PENDENTE_DEFINICAO | Citado nas respostas 5 e 10 como papel tático nomeado, sem definição própria além do exemplo |
| `Contentora_de_Linha` | CANDIDATO_PENDENTE_DEFINICAO | Citado apenas na resposta 5, sem definição própria |
| `Antecipadora_de_Saída` / `Gatilho_de_Entrada` | CANDIDATO_PENDENTE_DEFINICAO | Citados na resposta 3 como funções situacionais nomeadas, sem critério formal de acionamento |
| `Defensora_Base` / `Defensora_Solta` / `Defensora_Cobertura` | CANDIDATO_PENDENTE_DEFINICAO | Citadas nas respostas 3, 4 e 6; nomeadas e parcialmente descritas, mas sem definição extensional completa de limites entre elas |
| `Central` / `Lateral_Esquerda` / `Lateral_Direita` / `Pivô` (posições de ataque) | CANDIDATO_PENDENTE_DEFINICAO | Citadas nas respostas 1 e 4 como posições estruturais, sem definição extensional própria |
| `Sistema_3:1` / `Sistema_4:0` / `Sistema_3:0` / `Sistema_2:1` / `Sistema_Individual` | DEPENDE_DE_DECISAO_HUMANA_FUTURA | Citados na resposta 4 e 9 apenas como rótulos de sistemas táticos; nenhuma decisão humana literal própria define formalmente cada sistema |
| `Finalizadora_de_Infiltração` / `Defensoras_Base` (papel do exemplo 10) | CANDIDATO_PENDENTE_DEFINICAO | Citados apenas dentro de um exemplo (resposta 10), sem definição própria fora do exemplo |
| `Gol_de_giro_(360º)` / `Gol_aéreo` | DEPENDE_DE_REGRA_IHF | Citados na resposta 7 associados a pontuação de 2 pontos; `files/Decisões Humanas.md` já registra categorias correlatas aprovadas em `R09-CAT-2026-06-18` ("Gol criativo", "Gol espetacular", "Gol em aérea") — qualquer consolidação exige cruzamento com essas categorias já aprovadas, não realizado nesta auditoria |
| `Atleta_Saindo` / `Atleta_Entrando` | CANDIDATO_PENDENTE_DEFINICAO | Citados na resposta 9 como variáveis de um axioma proibitivo, não como classes definidas |

Nenhum dos conceitos acima foi transformado em ficha conceitual, taxonomia
ou ontologia por esta auditoria.

## 5. Autorização para ficha conceitual mínima dos quatro termos

| Dimensão | Definição literal | Relações declaradas | Inferências proibidas associadas | Base suficiente para ficha mínima? |
|---|---|---|---|---|
| `Papel_Tático` | Resposta 1 | Resposta 5 (vs. Papel_Regulamentar), separações de DH-ESP-001 (vs. Função_Situacional, vs. Posição_Espacial), clarificação Q8 | Resposta 9; clarificação Q8 | SIM |
| `Papel_Regulamentar` | Resposta 2 | Resposta 5 (vs. Papel_Tático) | Resposta 9 (regra de troca Jogador_de_Linha/Goleira) | SIM, restrita à dicotomia Jogador_de_Linha/Goleiro literalmente declarada |
| `Função_Situacional` | Resposta 3 | Resposta 6 (vs. Posição_Espacial), resposta 7 (não altera papel) | Consistente com INF-PROIB-PAPEIS-002 de CONCEPT_PAPEIS_SEPARACAO_MINIMA.yaml | SIM |
| `Posição_Espacial` | Resposta 4 | Resposta 6 (vs. Função_Situacional), clarificação Q8 (não altera Papel_Tático) | DH-ESP-001 + clarificação Q8 | SIM |

As quatro dimensões possuem, agora, definição humana literal própria,
relação declarada com pelo menos uma outra dimensão, e inferência proibida
associada rastreável. A ambiguidade que impedia o fechamento de
`Posição_Espacial` (pergunta 8) foi resolvida pela clarificação humana já
validada em `DH-PAPEIS-001_CLARIFICACAO_Q8_VALIDATION_REPORT.md`
(`DH_PAPEIS_001_Q8_VALIDADA_COM_CLARIFICACAO_SEMANTICA`).

Esta auditoria conclui que há base literal suficiente para autorizar a
criação de ficha conceitual mínima para os quatro termos. Esta conclusão
**não constitui** a criação dessas fichas — apenas remove o bloqueio
estrutural que impedia sua criação.

## 6. Pontos bloqueados

Os conceitos abaixo **não** estão autorizados para consolidação em ficha
conceitual por esta auditoria, independentemente de já possuírem alguma
descrição literal:

- `Status_Operacional`
- `Status_Regulamentar`
- `Status_da_Equipe`
- `Linha_Lateral`
- `Área_De_Substituição`
- `Transição_Híbrida`
- `Retarda-Ataque`
- `Contentora_de_Linha`
- `Gatilho_de_Entrada`
- `Antecipadora_de_Saída`
- `Gatilho_Regulamentar` / `Gatilho_De_Transição`
- `Ativa_Em_Quadra` / `Inativa` / `Em_Espera` / `Banco`
- `Defensora_Base` / `Defensora_Solta` / `Defensora_Cobertura`
- `Central` / `Lateral_Esquerda` / `Lateral_Direita` / `Pivô` (posições de ataque)
- `Sistema_3:1` / `Sistema_4:0` / `Sistema_3:0` / `Sistema_2:1` / `Sistema_Individual`
- `Jogador_De_Linha` (permanece no estado `PENDENTE_DEFINICAO_LITERAL` já registrado em VOCAB-MIN-001)
- `Gol_de_giro_(360º)` / `Gol_aéreo` (dependem de cruzamento com Regras 1–18/Apêndices, não realizado)
- `Atleta_Saindo` / `Atleta_Entrando`
- demais conceitos candidatos da seção 4 não classificados como dimensão principal

## Critérios da regra de aceite

| # | Critério | Resultado |
|---|----------|-----------|
| 1 | As quatro dimensões têm definição humana literal suficiente | APROVADO (seção 1 e 5) |
| 2 | A pergunta 8 está corrigida pela clarificação validada | APROVADO (seção 2; clarificação já validada como `DH_PAPEIS_001_Q8_VALIDADA_COM_CLARIFICACAO_SEMANTICA`) |
| 3 | As inferências proibidas estão preservadas | APROVADO (seção 3) |
| 4 | Os conceitos candidatos não foram promovidos indevidamente | APROVADO (seção 4 e 6; nenhum recebeu `PRONTO_PARA_FICHA`; nenhuma ficha criada) |
| 5 | Nenhuma ficha, taxonomia ou ontologia foi criada | APROVADO (verificado diretório `01_concepts/`, inalterado) |
| 6 | Arquivos protegidos permanecem intocados | APROVADO (tabela de tamanhos em bytes, todos idênticos ao baseline) |

## Decisão recomendada

Registrar `DH-PAPEIS-001-SEMANTIC-AUDIT` com status
`DH_PAPEIS_001_AUDITADA_SEMANTICAMENTE_AUTORIZANDO_FICHAS_MINIMAS`.

Esta autorização cobre exclusivamente a criação futura de ficha conceitual
mínima para `Papel_Tático`, `Papel_Regulamentar`, `Função_Situacional` e
`Posição_Espacial`. Não autoriza:
- Criar ficha, taxonomia ou ontologia para qualquer conceito da seção 6.
- Atualizar `CONCEPT_PAPEIS_SEPARACAO_MINIMA.yaml`.
- Consultar ou aplicar regra IHF.
- Continuar Regras 1–18 ou Apêndices.
- Marcar qualquer item deste escopo como `VALIDADO_TOTAL`.

Próxima ação autorizada por esta validação: atualizar `HANDOFF.md`
registrando o fechamento de `DH-PAPEIS-001-SEMANTIC-AUDIT` e abrindo, como
próximo ponto exato, a criação da ficha conceitual mínima para os quatro
termos (escopo a ser definido por nova tarefa explícita), antes de qualquer
trabalho sobre os conceitos listados na seção 6.
