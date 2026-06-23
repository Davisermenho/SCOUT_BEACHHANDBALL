---
doc_type: validation_report
tarefa_validada: CONCEPT-DIMENSOES-001-TESTS-EXECUTION
status_geral: CONCEPT_DIMENSOES_001_TESTES_EXECUTADOS_COM_SUCESSO_AGUARDANDO_VALIDACAO_HUMANA
gerado_em: "2026-06-23"
nao_e_validacao_total: true
tipo_de_execucao: execucao_logica_manual_contra_fichas_conceituais
---

# Relatório de Execução — CONCEPT-DIMENSOES-001-TESTS-EXECUTION

## Status geral

`CONCEPT_DIMENSOES_001_TESTES_EXECUTADOS_COM_SUCESSO_AGUARDANDO_VALIDACAO_HUMANA`

Esta é uma **execução lógica manual**: cada caso de teste foi confrontado
com as afirmações (`afirmacoes`), relações (`relacoes_declaradas`) e
inferências proibidas (`inferencias_proibidas`) já registradas nas
respectivas fichas conceituais mínimas, verificando se o resultado esperado
é a conclusão necessária a partir dessas regras, e se nenhuma das
inferências proibidas precisaria ser aplicada para chegar lá. **Não** é
execução de código contra uma implementação de software — essa execução
efetiva permanece como gate pendente (ver "Pendências").

## Arquivos de entrada usados (inalterados por esta tarefa)

| Arquivo | Tamanho | Papel |
|---|---|---|
| `TC-PAPEL-TATICO-001.yaml` | 3900 bytes | testes a executar |
| `TC-PAPEL-REGULAMENTAR-001.yaml` | 3661 bytes | testes a executar |
| `TC-FUNCAO-SITUACIONAL-001.yaml` | 3484 bytes | testes a executar |
| `TC-POSICAO-ESPACIAL-001.yaml` | 3992 bytes | testes a executar |
| `FICHA_CONCEITUAL_PAPEL_TATICO.yaml` | 6677 bytes | referência |
| `FICHA_CONCEITUAL_PAPEL_REGULAMENTAR.yaml` | 4932 bytes | referência |
| `FICHA_CONCEITUAL_FUNCAO_SITUACIONAL.yaml` | 5249 bytes | referência |
| `FICHA_CONCEITUAL_POSICAO_ESPACIAL.yaml` | 7411 bytes | referência |

## Verificação de não-alteração de arquivos fora do escopo

| Arquivo | Tamanho esperado | Tamanho atual | Resultado |
|---|---|---|---|
| `files/Regras 1–18.md` | 155662 bytes | 155662 bytes | inalterado |
| `files/Apêndices.md` | 47720 bytes | 47720 bytes | inalterado |
| `files/Decisões Humanas.md` (contém DH-ESP-001) | 18443 bytes | 18443 bytes | inalterado |
| `DH-PAPEIS-001.md` | 9389 bytes | 9389 bytes | inalterado |
| `DH-PAPEIS-001_CLARIFICACAO_Q8.md` | 4713 bytes | 4713 bytes | inalterado |
| 4 fichas conceituais (ver tabela acima) | — | — | inalteradas |
| 4 testes de competência (ver tabela acima) | — | — | inalterados |

---

## 1. TC-PAPEL-TATICO-001 — execução dos 4 casos

### TC-PAPTAT-001-C1
- **Entrada:** `papel_tatico_definido_pelo_treinador: Atacante_Normal`; `atleta: Lateral_Esquerda`; `evento: ocupa_momentaneamente_posicao_espacial_Central_no_contra_ataque`.
- **Ficha de referência:** `FICHA_CONCEITUAL_PAPEL_TATICO.yaml`.
- **Regra/fonte usada:** afirmação `FC-PAPTAT-001-03` (Papel_Tático não_é Posição_Espacial) + `DH-PAPEIS-001_CLARIFICACAO_Q8` ("a posição geográfica... não tem o poder de mudar a missão tática").
- **Resultado esperado:** `papel_tatico_final: Atacante_Normal`.
- **Resultado obtido:** `papel_tatico_final: Atacante_Normal` — a Posição_Espacial (Central, momentânea) não é admitida como fonte de alteração de Papel_Tático pela regra `FC-PAPTAT-001-03`; o Papel_Tático permanece o definido previamente pelo treinador.
- **Inferências proibidas verificadas:** "Reclassificar como Especialista por ocupar a posição de Central" — não aplicada; "Inferir Papel_Tático a partir da Posição_Espacial" — não aplicada.
- **Status do caso:** APROVADO
- **Observações:** Caso espelha literalmente o exemplo da Lateral Esquerda na clarificação Q8.

### TC-PAPTAT-001-C2
- **Entrada:** `papel_tatico_definido_pelo_treinador: Jogadora_Comum`; `funcao_situacional_momentanea: Finalizacao_Espetacular`; `evento: Gol`.
- **Ficha de referência:** `FICHA_CONCEITUAL_PAPEL_TATICO.yaml`.
- **Regra/fonte usada:** afirmação `FC-PAPTAT-001-02` (Papel_Tático não_é Função_Situacional) + `DH-PAPEIS-001` resposta 7.
- **Resultado esperado:** `papel_tatico_final: Jogadora_Comum`; `papel_regulamentar_final: Jogador_De_Linha`; `valor_do_gol: NAO_TESTADO_NESTA_ETAPA`.
- **Resultado obtido:** `papel_tatico_final: Jogadora_Comum`; `papel_regulamentar_final: Jogador_De_Linha`; `valor_do_gol: NAO_TESTADO_NESTA_ETAPA` — a execução de uma função situacional espetacular não satisfaz nenhuma condição de alteração de Papel_Tático ou Papel_Regulamentar declarada nas fichas; o campo de pontuação é mantido como não testado, conforme bloqueio obrigatório.
- **Inferências proibidas verificadas:** "Inferir Papel_Tático a partir da Função_Situacional" — não aplicada; "Reclassificar como Especialista por causa da função situacional" — não aplicada; "Atribuir valor de pontuação a este caso" — não aplicada (campo mantido como `NAO_TESTADO_NESTA_ETAPA`).
- **Status do caso:** APROVADO
- **Observações:** Este caso toca Gol de giro/aéreo apenas como contexto do evento; o valor do gol não foi computado, preservando o bloqueio.

### TC-PAPTAT-001-C3
- **Entrada:** `papel_tatico_definido_pelo_treinador: Especialista`; `atleta: Central_Especialista`; `evento: recebe_bola_na_posicao_espacial_Lateral_Esquerda`.
- **Ficha de referência:** `FICHA_CONCEITUAL_PAPEL_TATICO.yaml`.
- **Regra/fonte usada:** `DH-PAPEIS-001_CLARIFICACAO_Q8` ("Se a Central Especialista correr e receber uma bola na ponta esquerda, ela não deixa de ser a Especialista do time").
- **Resultado esperado:** `papel_tatico_final: Especialista`.
- **Resultado obtido:** `papel_tatico_final: Especialista` — variação de Posição_Espacial não desencadeia nenhuma regra de reclassificação nas fichas; o Papel_Tático Especialista permanece estável.
- **Inferências proibidas verificadas:** "Reclassificar Especialista por variação de Posição_Espacial" — não aplicada.
- **Status do caso:** APROVADO
- **Observações:** Nenhuma.

### TC-PAPTAT-001-C4
- **Entrada:** `atletas_com_papel_tatico_Especialista_ativas_em_quadra: 2`.
- **Ficha de referência:** `FICHA_CONCEITUAL_PAPEL_TATICO.yaml`.
- **Regra/fonte usada:** `inferencias_proibidas` da ficha ("Não permitir mais de uma jogadora com Papel_Tático de Especialista ativa em quadra simultaneamente"), fonte `DH-PAPEIS-001` resposta 9 ("PROIBIR: Mais de uma jogadora com o papel tático de Especialista... ativa em quadra simultaneamente").
- **Resultado esperado:** `estado_valido: false`.
- **Resultado obtido:** `estado_valido: false` — a entrada (2 Especialistas ativas simultaneamente) corresponde exatamente à condição vedada pela regra; o estado é, portanto, inválido.
- **Inferências proibidas verificadas:** "Permitir mais de uma jogadora com Papel_Tático de Especialista ativa em quadra simultaneamente" — a regra foi corretamente aplicada para invalidar o estado, não para permiti-lo.
- **Status do caso:** APROVADO
- **Observações:** Nenhuma.

---

## 2. TC-PAPEL-REGULAMENTAR-001 — execução dos 4 casos

### TC-PAPREG-001-C1
- **Entrada:** `papel_tatico: Especialista`; `papel_regulamentar_de_base: Jogador_De_Linha`.
- **Ficha de referência:** `FICHA_CONCEITUAL_PAPEL_REGULAMENTAR.yaml`.
- **Regra/fonte usada:** `nao_equivalencias` da ficha + `DH-PAPEIS-001` respostas 2 e 5 (Especialista tem Papel_Tático próprio, mas seu Papel_Regulamentar de base é Jogador de Linha, distinto do estatuto Goleiro).
- **Resultado esperado:** `papel_regulamentar_final: Jogador_De_Linha`.
- **Resultado obtido:** `papel_regulamentar_final: Jogador_De_Linha` — o Papel_Tático Especialista não altera o estatuto regulamentar de base; as duas dimensões se articulam (resposta 5) sem se fundirem em uma só.
- **Inferências proibidas verificadas:** "Confundir Papel_Regulamentar com Papel_Tático" — não aplicada; "Inferir que Especialista possui Papel_Regulamentar distinto de Jogador_De_Linha ou Goleiro" — não aplicada.
- **Status do caso:** APROVADO
- **Observações:** Nenhuma.

### TC-PAPREG-001-C2
- **Entrada:** `substituicao: { atleta_saindo: Jogador_De_Linha, atleta_entrando: Goleira }`.
- **Ficha de referência:** `FICHA_CONCEITUAL_PAPEL_REGULAMENTAR.yaml`.
- **Regra/fonte usada:** `inferencias_proibidas` da ficha + `DH-PAPEIS-001` resposta 9 ("PROIBIR: Se Atleta_Saindo = Jogador_de_Linha AND Atleta_Entrando = Goleira").
- **Resultado esperado:** `substituicao_valida: false`.
- **Resultado obtido:** `substituicao_valida: false` — a entrada corresponde exatamente ao padrão vedado; a substituição é inválida.
- **Inferências proibidas verificadas:** "Permitir troca Jogador_de_Linha → Goleira fora da regra restrita Especialista↔Goleira" — não aplicada (regra usada para invalidar, não para permitir).
- **Status do caso:** APROVADO
- **Observações:** Nenhuma.

### TC-PAPREG-001-C3
- **Entrada:** `substituicao: { atleta_entrando: Especialista, atleta_saindo: Goleira, goleira_sai_da_quadra: true }`.
- **Ficha de referência:** `FICHA_CONCEITUAL_PAPEL_REGULAMENTAR.yaml`.
- **Regra/fonte usada:** `definicao_literal` + `exemplos` da ficha, citando `DH-PAPEIS-001` resposta 2 ("a regra de substituição do Especialista é restrita e absoluta: ela só pode trocar de lugar com a goleira, que deve sair da quadra para a sua entrada").
- **Resultado esperado:** `substituicao_valida: true`.
- **Resultado obtido:** `substituicao_valida: true` — a entrada satisfaz exatamente as duas condições da regra restrita (par Especialista↔Goleira; Goleira sai da quadra).
- **Inferências proibidas verificadas:** Nenhuma listada para este caso; nenhuma inferência além da regra literal foi necessária.
- **Status do caso:** APROVADO
- **Observações:** Nenhuma.

### TC-PAPREG-001-C4
- **Entrada:** `consulta: definicao_completa_de_Papel_Regulamentar`.
- **Ficha de referência:** `FICHA_CONCEITUAL_PAPEL_REGULAMENTAR.yaml`.
- **Regra/fonte usada:** bloco `pendencias_controladas` da ficha ("Definição regulamentar completa de Papel_Regulamentar depende de regras oficiais IHF ainda não reprocessadas; Regras 1–18 não foram consultadas nesta etapa").
- **Resultado esperado:** `status: PENDENTE_DEFINICAO_LITERAL`; `motivo: depende_de_Regras_1_18_ainda_nao_reprocessadas`.
- **Resultado obtido:** `status: PENDENTE_DEFINICAO_LITERAL` — a ficha não contém definição extensional completa, apenas a dicotomia Jogador de Linha/Goleiro e a regra restrita do Especialista; a consulta retorna a pendência tal como declarada, sem completar a lacuna.
- **Inferências proibidas verificadas:** "Completar a definição regulamentar completa de Papel_Regulamentar por inferência a partir de Regras 1–18 não consultadas" — não aplicada; `Regras 1–18.md` não foi consultado durante esta execução.
- **Status do caso:** APROVADO
- **Observações:** Nenhuma.

---

## 3. TC-FUNCAO-SITUACIONAL-001 — execução dos 3 casos

### TC-FUNSIT-001-C1
- **Entrada:** `papel_tatico_definido_pelo_treinador: Jogadora_Comum`; `funcao_situacional_anterior: Defensora_Cobertura`; `evento_factual: erro_de_passe_do_ataque_adversario`; `funcao_situacional_nova: Gatilho_De_Transicao_Ofensiva`.
- **Ficha de referência:** `FICHA_CONCEITUAL_FUNCAO_SITUACIONAL.yaml`.
- **Regra/fonte usada:** afirmação `FC-FUNSIT-001-03` (Função_Situacional não_altera Papel_Tático) + `DH-PAPEIS-001` resposta 6.
- **Resultado esperado:** `papel_tatico_final: Jogadora_Comum`.
- **Resultado obtido:** `papel_tatico_final: Jogadora_Comum` — a mudança de Função_Situacional (de Defensora_Cobertura para Gatilho_De_Transicao_Ofensiva), por si só, não satisfaz nenhuma condição de alteração de Papel_Tático.
- **Inferências proibidas verificadas:** "Inferir Papel_Tático a partir da Função_Situacional" — não aplicada; "Alterar Papel_Tático por mudança de Função_Situacional" — não aplicada.
- **Status do caso:** APROVADO
- **Observações:** Nenhuma.

### TC-FUNSIT-001-C2
- **Entrada:** `papel_tatico_definido_pelo_treinador: Jogadora_Comum`; `papel_regulamentar_de_base: Jogador_De_Linha`; `funcao_situacional_momentanea: Finalizacao_Espetacular`; `evento: Gol`.
- **Ficha de referência:** `FICHA_CONCEITUAL_FUNCAO_SITUACIONAL.yaml`.
- **Regra/fonte usada:** afirmações `FC-FUNSIT-001-03`/`04` + `DH-PAPEIS-001` resposta 7 ("não altera o seu papel tático... nem seu papel regulamentar").
- **Resultado esperado:** `papel_tatico_final: Jogadora_Comum`; `papel_regulamentar_final: Jogador_De_Linha`; `valor_do_gol: NAO_TESTADO_NESTA_ETAPA`.
- **Resultado obtido:** idêntico ao esperado — a execução espetacular da função situacional não altera nenhuma das duas dimensões regulamentar/tática; o valor do gol permanece não testado.
- **Inferências proibidas verificadas:** "Alterar Papel_Tático ou Papel_Regulamentar pela execução de Função_Situacional espetacular" — não aplicada; "Atribuir valor de pontuação a este caso" — não aplicada.
- **Status do caso:** APROVADO
- **Observações:** Caso simétrico a `TC-PAPTAT-001-C2`, validado de forma consistente em ambas as fichas.

### TC-FUNSIT-001-C3
- **Entrada:** `posicao_espacial: Defensora_Cobertura_zona`; `funcao_situacional_simultanea: Gatilho_De_Transicao_Ofensiva`.
- **Ficha de referência:** `FICHA_CONCEITUAL_FUNCAO_SITUACIONAL.yaml`.
- **Regra/fonte usada:** afirmação `FC-FUNSIT-001-02` (Função_Situacional não_é Posição_Espacial) + `DH-PAPEIS-001` resposta 6 ("Sim, sempre").
- **Resultado esperado:** `posicao_espacial_e_funcao_situacional_distintas: true`.
- **Resultado obtido:** `posicao_espacial_e_funcao_situacional_distintas: true` — mesmo ocorrendo no mesmo instante, as duas dimensões permanecem conceitualmente distintas, conforme a separação declarada.
- **Inferências proibidas verificadas:** "Confundir Função_Situacional com Posição_Espacial" — não aplicada.
- **Status do caso:** APROVADO
- **Observações:** Nenhuma.

---

## 4. TC-POSICAO-ESPACIAL-001 — execução dos 4 casos

### TC-POSESP-001-C1
- **Entrada:** `papel_tatico_definido_pelo_treinador: Atacante_Normal`; `atleta: Lateral_Esquerda`; `evento: ocupa_momentaneamente_posicao_espacial_Central_no_contra_ataque`.
- **Ficha de referência:** `FICHA_CONCEITUAL_POSICAO_ESPACIAL.yaml`.
- **Regra/fonte usada:** afirmação `FC-POSESP-001-03` (Posição_Espacial isolada_não_altera Papel_Tático) + `DH-PAPEIS-001_CLARIFICACAO_Q8`.
- **Resultado esperado:** `papel_tatico_final: Atacante_Normal`.
- **Resultado obtido:** `papel_tatico_final: Atacante_Normal` — idêntico ao caso equivalente em `TC-PAPEL-TATICO-001` (`C1`), agora verificado a partir da ficha de Posição_Espacial.
- **Inferências proibidas verificadas:** "Reclassificar a atleta como Especialista por ocupar a posição de Central" — não aplicada; "Inferir Papel_Tático a partir da Posição_Espacial" — não aplicada.
- **Status do caso:** APROVADO
- **Observações:** Caso espelha `TC-PAPTAT-001-C1`; resultado consistente entre as duas fichas confirma que a separação Papel_Tático ≠ Posição_Espacial está aplicada de forma simétrica.

### TC-POSESP-001-C2
- **Entrada:** `papel_tatico_definido_pelo_treinador_no_banco: Especialista`; `evento: atleta_cruza_a_Linha_Lateral_na_Área_De_Substituição`.
- **Ficha de referência:** `FICHA_CONCEITUAL_POSICAO_ESPACIAL.yaml`.
- **Regra/fonte usada:** afirmações `FC-POSESP-001-04`/`05` + `DH-PAPEIS-001_CLARIFICACAO_Q8` ("o papel tático individual já foi determinado na prancheta do treinador... cruzar a linha lateral é apenas o ato regulamentar que bota essa estratégia para funcionar").
- **Resultado esperado:** `status_operacional_final: Ativa_Em_Quadra`; `papel_tatico_final: Especialista`.
- **Resultado obtido:** `status_operacional_final: Ativa_Em_Quadra`; `papel_tatico_final: Especialista` — a Linha_Lateral aciona apenas a mudança de Status_Operacional; o Papel_Tático já estava determinado antes do cruzamento e permanece inalterado.
- **Inferências proibidas verificadas:** "Inferir que cruzar a Linha_Lateral cria o Papel_Tático" — não aplicada; "Confundir Status_Operacional com Papel_Tático" — não aplicada (os dois campos foram mantidos distintos no resultado); "Inferir que Linha_Lateral transforma Especialista em outro Papel_Tático" — não aplicada; "Inferir que Linha_Lateral transforma Atacante_Normal em Especialista" — não aplicada (não se aplica a esta entrada, mas a regra foi respeitada).
- **Status do caso:** APROVADO
- **Observações:** `Status_Operacional`, `Linha_Lateral` e `Área_De_Substituição` foram usados apenas como valores de entrada/saída deste caso; nenhum deles foi tratado como ficha conceitual ou conceito consolidado.

### TC-POSESP-001-C3
- **Entrada:** `substituicao: { lado_de_troca_da_equipe: Lado_A, linha_lateral_cruzada: Lado_B }`.
- **Ficha de referência:** `FICHA_CONCEITUAL_POSICAO_ESPACIAL.yaml`.
- **Regra/fonte usada:** `contraexemplos` da ficha + `DH-PAPEIS-001` resposta 10, Contraexemplo 2 ("o sistema validar... a substituição pela linha lateral oposta da quadra" é listado como erro).
- **Resultado esperado:** `substituicao_valida: false`.
- **Resultado obtido:** `substituicao_valida: false` — a linha cruzada (Lado_B) não corresponde ao lado de troca da própria equipe (Lado_A); a substituição é inválida.
- **Inferências proibidas verificadas:** "Validar substituição realizada pela linha lateral oposta ao lado de troca da equipe" — não aplicada (regra usada para invalidar, não para validar).
- **Status do caso:** APROVADO
- **Observações:** Nenhuma.

### TC-POSESP-001-C4
- **Entrada:** `sistema_tatico: Sistema_4:0`; `presenca_de_pivo: false`.
- **Ficha de referência:** `FICHA_CONCEITUAL_POSICAO_ESPACIAL.yaml`.
- **Regra/fonte usada:** `inferencias_proibidas` da ficha + `DH-PAPEIS-001` resposta 9 ("PROIBIR: O sistema apontar erro se houver ausência de pivô no Sistema_4:0, pois o texto valida que nesse desenho a equipe abdica da figura do pivô fixo").
- **Resultado esperado:** `erro_apontado: false`.
- **Resultado obtido:** `erro_apontado: false` — a ausência de pivô é uma característica esperada do Sistema_4:0, não uma anomalia.
- **Inferências proibidas verificadas:** "Apontar erro por ausência de pivô no Sistema_4:0" — não aplicada.
- **Status do caso:** APROVADO
- **Observações:** `Sistema_4:0` foi usado apenas como valor de entrada; não foi definido extensionalmente por este caso.

---

## Resumo da execução

| Teste | Casos | Aprovados | Reprovados | Bloqueados |
|---|---|---|---|---|
| TC-PAPEL-TATICO-001 | 4 | 4 | 0 | 0 |
| TC-PAPEL-REGULAMENTAR-001 | 4 | 4 | 0 | 0 |
| TC-FUNCAO-SITUACIONAL-001 | 3 | 3 | 0 | 0 |
| TC-POSICAO-ESPACIAL-001 | 4 | 4 | 0 | 0 |
| **Total** | **15** | **15** | **0** | **0** |

## Verificação dos bloqueios obrigatórios durante a execução

| Bloqueio | Confirmado |
|---|---|
| Gol de giro / Gol aéreo continuam não resolvidos | Sim — nos casos `TC-PAPTAT-001-C2` e `TC-FUNSIT-001-C2`, o campo `valor_do_gol` foi mantido como `NAO_TESTADO_NESTA_ETAPA`, não computado |
| Cruzamento com R09-CAT-2026-06-18 continua bloqueado | Sim — `files/Decisões Humanas.md` (onde está R09-CAT-2026-06-18) não foi consultado nem alterado durante a execução |
| Nenhuma categoria de pontuação foi alterada | Sim — `Decisões Humanas.md` permanece com tamanho de byte idêntico ao baseline (18443 bytes) |
| Linha_Lateral, Status_Operacional e Transição_Híbrida continuam candidatos não promovidos | Sim — usados apenas como valores de campo em `TC-POSESP-001-C2`; nenhum arquivo de ficha foi criado para eles; diretório `01_concepts/` permanece com os mesmos 7 arquivos de antes desta execução |
| Nenhum conceito candidato virou ficha ou conceito consolidado | Sim — nenhum arquivo novo foi criado em `01_concepts/` por esta tarefa |

## Critérios de aprovação por dimensão

| Dimensão | Critério | Atendido nos casos |
|---|---|---|
| Papel_Tático | permanece definido pelo treinador | C1, C2, C3 |
| Papel_Tático | não inferido pela posição espacial | C1, C3 |
| Papel_Tático | não inferido pela função situacional | C2 |
| Papel_Tático | bloqueia mais de uma Especialista ativa simultaneamente | C4 |
| Papel_Regulamentar | permanece estatuto jurídico fixo | C1, C2, C3 |
| Papel_Regulamentar | não confundido com Papel_Tático | C1 |
| Papel_Regulamentar | não transforma Jogador_De_Linha em Goleira por inferência | C2 |
| Papel_Regulamentar | mantém regra IHF completa como pendência, não inferência | C4 |
| Função_Situacional | permanece microação momentânea | C1, C2 |
| Função_Situacional | não altera Papel_Tático | C1, C2 |
| Função_Situacional | não altera Papel_Regulamentar | C2 |
| Função_Situacional | permanece distinta de Posição_Espacial | C3 |
| Posição_Espacial | permanece localização/organização geográfica | C1, C2 |
| Posição_Espacial | não altera Papel_Tático isoladamente | C1, C2 |
| Posição_Espacial | Linha_Lateral tratada como gatilho, não criadora de Papel_Tático | C2 |
| Posição_Espacial | substituição pela linha lateral oposta é inválida | C3 |
| Posição_Espacial | ausência de pivô no Sistema_4:0 não é erro | C4 |

Todos os critérios de aprovação exigidos pela tarefa foram atendidos por
pelo menos um caso executado, e nenhum caso produziu resultado conflitante
com eles.

## Pendências

1. Esta execução é lógica/manual, não execução de código contra uma implementação de software real — essa execução efetiva permanece pendente.
2. Validação humana dos 15 resultados obtidos.
3. Validação lógica ou estrutural formal (fora do escopo desta tarefa).
4. Todas as pendências já controladas nas 4 fichas e nos 4 testes (definição extensional completa, Jogador_De_Linha, sistemas táticos, 10 conceitos candidatos bloqueados) permanecem válidas e inalteradas.
5. `Gol de giro`/`Gol aéreo` e o cruzamento com `R09-CAT-2026-06-18` permanecem não resolvidos.

Nenhuma das pendências acima foi resolvida por inferência. Nenhuma
extrapola o escopo de `CONCEPT-DIMENSOES-001-TESTS-EXECUTION`.

## Decisão recomendada

Registrar a execução de `CONCEPT-DIMENSOES-001-TESTS-EXECUTION` com status
`CONCEPT_DIMENSOES_001_TESTES_EXECUTADOS_COM_SUCESSO_AGUARDANDO_VALIDACAO_HUMANA`.

Não autorizado por esta execução:
- Criar ficha, taxonomia ou ontologia para qualquer conceito candidato citado nos testes.
- Resolver `Gol de giro` / `Gol aéreo` ou o cruzamento com `R09-CAT-2026-06-18`.
- Continuar Regras 1–18 ou Apêndices.
- Marcar qualquer teste, ficha, ou este escopo, como `VALIDADO_TOTAL` ou `CONSOLIDADO_VALIDO`.

Próxima ação autorizada por esta execução: atualizar `HANDOFF.md`
registrando o fechamento de `CONCEPT-DIMENSOES-001-TESTS-EXECUTION` e
aguardar validação humana dos 15 resultados antes de qualquer nova etapa
(incluindo qualquer decisão sobre os conceitos candidatos bloqueados ou
sobre Gol de giro/Gol aéreo).
