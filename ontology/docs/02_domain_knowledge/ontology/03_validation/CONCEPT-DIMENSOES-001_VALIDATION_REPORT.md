---
doc_type: validation_report
tarefa_validada: CONCEPT-DIMENSOES-001
status_geral: CONCEPT_DIMENSOES_001_APROVADA_COM_PENDENCIAS_CONTROLADAS
gerado_em: "2026-06-23"
nao_e_validacao_total: true
---

# Relatório de Validação — CONCEPT-DIMENSOES-001

## Status geral

`CONCEPT_DIMENSOES_001_APROVADA_COM_PENDENCIAS_CONTROLADAS`

Esta validação cobre exclusivamente as quatro fichas conceituais mínimas
criadas em `CONCEPT-DIMENSOES-001` (`Papel_Tático`, `Papel_Regulamentar`,
`Função_Situacional`, `Posição_Espacial`). Não valida definição extensional
completa de nenhum dos quatro termos, não resolve `Gol de giro`/`Gol aéreo`,
não cruza com `R09-CAT-2026-06-18`, não constitui taxonomia ou ontologia e
não promove qualquer conceito candidato a ficha consolidada.

## Arquivos verificados

| # | Arquivo | Existe no path correto |
|---|---------|--------------------------|
| 1 | `docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_PAPEL_TATICO.yaml` | Sim |
| 2 | `docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_PAPEL_REGULAMENTAR.yaml` | Sim |
| 3 | `docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_FUNCAO_SITUACIONAL.yaml` | Sim |
| 4 | `docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_POSICAO_ESPACIAL.yaml` | Sim |

Entradas correlatas também inspecionadas: `DH-PAPEIS-001.md`,
`DH-PAPEIS-001_CLARIFICACAO_Q8.md`,
`DH-PAPEIS-001_SEMANTIC_AUDIT_REPORT.md`,
`CONCEPT_PAPEIS_SEPARACAO_MINIMA.yaml`, `VOCABULARIO_CANONICO_MINIMO.md`.

## Verificação de não-alteração de arquivos fora do escopo

| Arquivo | Tamanho esperado | Tamanho atual | Resultado |
|---|---|---|---|
| `files/Regras 1–18.md` | 155662 bytes | 155662 bytes | inalterado |
| `files/Apêndices.md` | 47720 bytes | 47720 bytes | inalterado |
| `files/Decisões Humanas.md` (contém DH-ESP-001) | 18443 bytes | 18443 bytes | inalterado |
| `docs/.../04_human_decisions/DH-PAPEIS-001.md` | 9389 bytes | 9389 bytes | inalterado |
| `docs/.../04_human_decisions/DH-PAPEIS-001_CLARIFICACAO_Q8.md` | 4713 bytes | 4713 bytes | inalterado |

Diretório `01_concepts/` contém exatamente 7 arquivos: os 4 desta tarefa,
mais `CONCEPT_PAPEIS_SEPARACAO_MINIMA.yaml`,
`FICHA_CONCEITUAL_ESPECIALISTA.yaml` e `FICHA_CONCEITUAL_GOLEIRO.yaml`
(pré-existentes). Nenhum arquivo de ficha foi criado para conceitos
bloqueados (busca por nomes de arquivo contendo `STATUS_OPERACIONAL`,
`STATUS_REGULAMENTAR`, `STATUS_DA_EQUIPE`, `LINHA_LATERAL`,
`AREA_DE_SUBSTITUICAO`, `TRANSICAO_HIBRIDA`, `RETARDA`, `CONTENTORA`,
`GATILHO`, `ANTECIPADORA` não retornou nenhum resultado).

## Critérios avaliados

| # | Critério | Resultado | Evidência |
|---|----------|-----------|-----------|
| 1 | Os quatro arquivos existem nos paths corretos | APROVADO | Listagem de `01_concepts/` confirma os 4 arquivos |
| 2 | Todos possuem status `FICHA_MINIMA_REGISTRADA_AGUARDANDO_TESTE_E_VALIDACAO` | APROVADO | Campo `status` idêntico nas 4 fichas (linha 6 de cada arquivo) |
| 3 | `FICHA_CONCEITUAL_PAPEL_TATICO.yaml` define Papel_Tático como missão estratégica temporária ou estrutural dada pelo treinador | APROVADO | Campo `definicao_literal` reproduz literalmente a resposta 1 de DH-PAPEIS-001, incluindo essa frase |
| 4 | Ficha de Papel_Tático registra os 6 pontos exigidos | APROVADO | `não inferido pela posição espacial`: bloco `inferencias_proibidas` e afirmação `FC-PAPTAT-001-03`; `não alterado por função situacional`: `inferencias_proibidas` e afirmação `FC-PAPTAT-001-02`; `pode ser estrutural ou temporário`: afirmação `FC-PAPTAT-001-01` e `relacoes_declaradas`; `Especialista é exemplo`: bloco `exemplos` e afirmação `FC-PAPTAT-001-05`; `Central/Lateral Esquerda/Lateral Direita/Pivô apenas exemplos citados`: bloco `exemplos`, com nota explícita "sem ficha conceitual própria criada nesta etapa", e também listados em `conceitos_candidatos_nao_promovidos`; `Transição_Híbrida como candidato`: presente em `exemplos` (nota "registrada como conceito candidato, não como ficha") e em `conceitos_candidatos_nao_promovidos` |
| 5 | `FICHA_CONCEITUAL_PAPEL_REGULAMENTAR.yaml` define Papel_Regulamentar como estatuto jurídico fixo determinado pelo livro de regras da IHF | APROVADO | Campo `definicao_literal` reproduz literalmente a resposta 2 de DH-PAPEIS-001, incluindo essa frase |
| 6 | Ficha de Papel_Regulamentar registra os 4 pontos exigidos | APROVADO | `Jogador de Linha e Goleiro como categorias citadas`: bloco `exemplos` e `definicao_literal`; `não confundir com Papel_Tático`: bloco `nao_equivalencias` e `inferencias_proibidas`; `definição completa depende de regra IHF reprocessada`: bloco `pendencias_controladas` e `observacoes` ("Não reconstrói a definição regulamentar completa pela regra oficial IHF"); `regra IHF não completada por inferência`: `inferencias_proibidas` ("Não completar a definição regulamentar completa de Papel_Regulamentar por inferência a partir de regra IHF ainda não reprocessada") |
| 7 | `FICHA_CONCEITUAL_FUNCAO_SITUACIONAL.yaml` define Função_Situacional como microação baseada na leitura de resultados factuais do exato milissegundo | APROVADO | Campo `definicao_literal` reproduz literalmente a resposta 3 de DH-PAPEIS-001, incluindo essa frase |
| 8 | Ficha de Função_Situacional registra os 3 pontos exigidos | APROVADO | `não altera papel do atleta`: afirmações `FC-FUNSIT-001-03`/`04` e bloco `relacoes_declaradas`; `Antecipadora de Saída, Gatilho de Entrada, Defensora Base, Defensora Solta, Defensora Cobertura como exemplos sem ficha própria`: bloco `exemplos` (nota "sem ficha própria criada nesta etapa") e `conceitos_candidatos_nao_promovidos`; `função descreve ação imediata em resposta ao ambiente`: citado literalmente em `relacoes_declaradas`, citando a resposta 6 |
| 9 | `FICHA_CONCEITUAL_POSICAO_ESPACIAL.yaml` define Posição_Espacial como coordenadas de organização estrutural e geográfica na quadra | APROVADO | Campo `definicao_literal` reproduz literalmente a resposta 4 de DH-PAPEIS-001, incluindo essa frase |
| 10 | Ficha de Posição_Espacial registra os 4 pontos exigidos | APROVADO | `posição espacial isolada não altera Papel_Tático`: afirmação `FC-POSESP-001-03` e bloco `relacoes_declaradas`, citando DH-PAPEIS-001_CLARIFICACAO_Q8; `Linha_Lateral é gatilho operacional/regulamentar, não criadora de Papel_Tático`: afirmações `FC-POSESP-001-04`/`05` e `nao_equivalencias`; `setores e zonas como exemplos sem ficha própria`: bloco `exemplos`; `Linha_Lateral e Área_De_Substituição como candidatos, não fichas`: bloco `conceitos_candidatos_nao_promovidos` e nota em `exemplos` |
| 11 | Nenhuma ficha foi criada para os 10 conceitos bloqueados | APROVADO | Busca por nome de arquivo nos 10 termos (`Status_Operacional`, `Status_Regulamentar`, `Status_da_Equipe`, `Linha_Lateral`, `Área_De_Substituição`, `Transição_Híbrida`, `Retarda-Ataque`, `Contentora_de_Linha`, `Gatilho_de_Entrada`, `Antecipadora_de_Saída`) não retornou nenhum arquivo; todos aparecem apenas como texto em `conceitos_candidatos_nao_promovidos` ou `exemplos` das 4 fichas válidas |
| 12 | Gol de giro / Gol aéreo permanecem bloqueados | APROVADO | Bloco `bloqueio_obrigatorio` presente nas 4 fichas, com a frase "Gol de giro (360º) e Gol aéreo permanecem bloqueados; não resolvidos nesta ficha" |
| 13 | Cruzamento com R09-CAT-2026-06-18 permanece não resolvido | APROVADO | Bloco `bloqueio_obrigatorio` presente nas 4 fichas, com a frase "O cruzamento com R09-CAT-2026-06-18 não foi resolvido nesta etapa" |
| 14 | Nenhuma categoria de pontuação foi alterada | APROVADO | Bloco `bloqueio_obrigatorio` declara explicitamente "Nenhuma categoria de pontuação foi alterada por esta ficha" nas 4 fichas; `files/Decisões Humanas.md` (onde estão registradas as categorias de pontuação aprovadas, incluindo R09-CAT-2026-06-18) permanece com tamanho de byte idêntico ao baseline |
| 15 | Arquivos protegidos permaneceram intocados | APROVADO | Tamanhos em bytes idênticos aos valores de referência para `Regras 1–18.md`, `Apêndices.md`, `Decisões Humanas.md` (contém DH-ESP-001), `DH-PAPEIS-001.md` e `DH-PAPEIS-001_CLARIFICACAO_Q8.md` (ver tabela acima) |

## Observação sobre fidelidade às respostas humanas

As quatro fichas reproduzem as definições literais (`definicao_literal`)
exatamente como registradas em `DH-PAPEIS-001.md` (respostas 1, 2, 3 e 4) e
incorporam a clarificação validada da pergunta 8
(`DH-PAPEIS-001_CLARIFICACAO_Q8.md`) apenas no campo `relacoes_declaradas` e
`inferencias_proibidas` da ficha de `Posição_Espacial`, sem reescrever a
fala humana — cada afirmação cita a fonte exata (resposta numerada ou
clarificação) de onde foi extraída.

## Critérios aprovados

1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 — todos os 15 critérios
avaliados foram cumpridos.

## Critérios reprovados

Nenhum.

## Pendências

Pendências controladas (esperadas e corretamente sinalizadas nas próprias
fichas, não bloqueantes para o escopo desta tarefa):

1. Definição extensional completa de `Papel_Tático` para todos os papéis táticos possíveis do domínio — apenas Especialista e os exemplos citados estão cobertos.
2. Separação genérica `Papel_Tático ≠ Papel_Regulamentar` para todo o domínio permanece sustentada apenas pela resposta 5; `CONCEPT_PAPEIS_SEPARACAO_MINIMA.yaml` ainda registra `SEP-PAPEIS-003` como `SUSTENTADO_INDIRETAMENTE_PENDENTE_DECLARACAO_GENERICA` — não atualizado por esta tarefa.
3. Definição regulamentar completa de `Papel_Regulamentar` depende de regras oficiais IHF ainda não reprocessadas.
4. `Jogador_De_Linha` permanece `PENDENTE_DEFINICAO_LITERAL` desde VOCAB-MIN-001.
5. Definição extensional completa de todas as funções situacionais e de todos os sistemas táticos citados (`Sistema_3:1`, `Sistema_4:0` etc.) permanece pendente.
6. Os 10 conceitos candidatos listados no critério 11 permanecem bloqueados para ficha própria.
7. `Gol de giro` / `Gol aéreo` e o cruzamento com `R09-CAT-2026-06-18` permanecem não resolvidos.
8. Validação humana de cada uma das 4 fichas.
9. Execução de teste de competência para cada uma das 4 fichas (ainda não criado).
10. Validação lógica ou estrutural.

Nenhuma das pendências acima foi resolvida por inferência. Nenhuma
extrapola o escopo de `CONCEPT-DIMENSOES-001`.

## Decisão recomendada

Aceitar as quatro fichas de `CONCEPT-DIMENSOES-001` com status
`CONCEPT_DIMENSOES_001_APROVADA_COM_PENDENCIAS_CONTROLADAS`.

Não autorizado por esta validação:
- Criar ficha, taxonomia ou ontologia para qualquer um dos 10 conceitos candidatos bloqueados.
- Resolver `Gol de giro` / `Gol aéreo` ou o cruzamento com `R09-CAT-2026-06-18`.
- Continuar Regras 1–18 ou Apêndices.
- Marcar qualquer uma das 4 fichas, ou este escopo, como `VALIDADO_TOTAL` ou `CONSOLIDADO_VALIDO`.

Próxima ação autorizada por esta validação: atualizar `HANDOFF.md`
registrando o fechamento de `CONCEPT-DIMENSOES-001` e aguardar definição
humana do próximo ponto exato (testes de competência das 4 fichas e/ou
decisão sobre os conceitos candidatos bloqueados) antes de qualquer nova
etapa.
