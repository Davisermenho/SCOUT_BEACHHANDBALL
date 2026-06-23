---
doc_type: validation_report
tarefa_validada: VOCAB-MIN-001
status_geral: VOCAB_MIN_001_APROVADA_COM_PENDENCIAS_CONTROLADAS
gerado_em: "2026-06-22"
nao_e_validacao_total: true
---

# Relatório de Validação — VOCAB-MIN-001

## Status geral

`VOCAB_MIN_001_APROVADA_COM_PENDENCIAS_CONTROLADAS`

Esta validação cobre exclusivamente o handoff de VOCAB-MIN-001 (vocabulário
mínimo + ficha conceitual + teste de competência do conceito `Especialista`).
Não é uma validação total da ontologia, das Regras 1–18 ou dos Apêndices.

## Arquivos verificados

| # | Arquivo | Existe no path correto |
|---|---------|--------------------------|
| 1 | `docs/02_domain_knowledge/ontology/00_governance/VOCABULARIO_CANONICO_MINIMO.md` | Sim |
| 2 | `docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_ESPECIALISTA.yaml` | Sim |
| 3 | `docs/02_domain_knowledge/ontology/02_competency_tests/TC-ESP-001.yaml` | Sim |

Entradas de auditoria consultadas para esta validação:
- `files/Decisões Humanas.md` (bloco `DH-ESP-001`)
- `results_auditoria_python/00_ESTADO_REAL_AUDITADO.md`
- `results_auditoria_python/07_blockers_report.md`
- `results_auditoria_python/03_missing_vocabulary_terms.csv`
- `results_auditoria_python/04_invalid_predicates.csv`

## Verificação de não-alteração de arquivos fora do escopo

Comparados tamanho/timestamp dos arquivos-fonte contra os hashes/tamanhos
registrados em `07_blockers_report.md` (rastreabilidade da última execução
da auditoria Python):

| Arquivo | Tamanho esperado (07_blockers_report.md) | Tamanho atual | Resultado |
|---|---|---|---|
| `files/Regras 1–18.md` | 155662 bytes | 155662 bytes | inalterado |
| `files/Apêndices.md` | 47720 bytes | 47720 bytes | inalterado |
| `files/Decisões Humanas.md` (contém DH-ESP-001) | 18443 bytes | 18443 bytes | inalterado |

Nenhum arquivo de ontologia principal existe no repositório (consistente com
"não gerar ontologia"). O diretório
`docs/02_domain_knowledge/ontology/` contém exclusivamente os 3 arquivos
desta tarefa, sem arquivos extras.

## Critérios avaliados

| # | Critério | Resultado | Evidência |
|---|----------|-----------|-----------|
| 1 | Os três arquivos existem nos paths corretos | APROVADO | Listagem de diretório confirma os 3 arquivos e nenhum extra |
| 2 | Nenhuma regra, apêndice ou ontologia principal foi alterada | APROVADO | Tamanhos de `Regras 1–18.md`, `Apêndices.md` e `Decisões Humanas.md` idênticos aos registrados em `07_blockers_report.md`; nenhum arquivo de ontologia existe |
| 3 | DH-ESP-001 aparece como fonte de autoridade | APROVADO | `fonte_primaria: DH-ESP-001` no vocabulário; `fonte_de_autoridade: DH-ESP-001` e `fonte: DH-ESP-001` em todas as 9 afirmações da ficha; `fonte: DH-ESP-001` no TC-ESP-001 |
| 4 | Especialista modelado como Papel_Tático | APROVADO | Ficha `FC-ESP-001-01`: `Especialista é_subclasse_de Papel_Tático`; vocabulário, seção `Especialista` |
| 5 | Especialista não modelado como Goleiro | APROVADO | Ficha `FC-ESP-001-02`: `Especialista não_é Goleiro` |
| 6 | Especialista atuando como goleiro continua Especialista | APROVADO (com nota) | Ficha `FC-ESP-001-07`: `Especialista_Atuando_Como_Goleiro não_se_transforma_em Goleiro`, combinada com `FC-ESP-001-05/06` (`Especialista permanece_como Especialista` dentro/fora da área). A ficha reproduz a negação literal de DH-ESP-001 ("não vira Goleiro") em vez de uma afirmação separada "continua Especialista" — isso é fiel ao texto literal da decisão, que também só afirma a negação. Adicionar uma afirmação positiva equivalente seria reinterpretação/inferência, vedada pelo escopo desta tarefa. |
| 7 | Todo gol de Especialista vale 2 pontos | APROVADO | Ficha `FC-ESP-001-08`: `Gol_De_Especialista vale_pontos 2 (quantificador: todo)`; vocabulário, seção `Gol_De_Especialista`; `TC-ESP-001.esperado.valor_do_gol: 2` |
| 8 | Gol de Especialista valendo 1 ponto está proibido | APROVADO | Ficha `FC-ESP-001-09`: `Gol_De_Especialista nunca_vale_pontos 1`; lista `inferencias_proibidas` da ficha; `TC-ESP-001.esperado.inferencia_proibida: [Atribuir 1 ponto]` |
| 9 | Papel_Tático, Função_Situacional e Posição_Espacial separados | APROVADO (com nota de escopo) | Ficha `FC-ESP-001-03`: `Papel_Tático não_é Função_Situacional`; `FC-ESP-001-04`: `Papel_Tático não_é Posição_Espacial`. DH-ESP-001 declara apenas essas duas separações pareadas (`separacoes_obrigatorias`); não declara `Função_Situacional` vs `Posição_Espacial` entre si — essa separação não foi inventada, corretamente, por estar fora do que a fonte literal afirma. |
| 10 | Termos sem definição literal marcados PENDENTE_DEFINICAO_LITERAL | APROVADO | No vocabulário: `Papel_Regulamentar`, `Função_Situacional`, `Posição_Espacial`, `Jogador_De_Linha`, `Autor_Do_Gol`, `Fundamento_Da_Pontuação` — todos com `status: PENDENTE_DEFINICAO_LITERAL` e nota explícita de que não foram completados por inferência |
| 11 | TC-ESP-001 contém entrada e esperado compatíveis com DH-ESP-001 | APROVADO | Bloco `entrada`/`esperado` de `TC-ESP-001.yaml` é idêntico, campo a campo, ao bloco `teste_de_competencia_obrigatorio` embutido em DH-ESP-001 (`files/Decisões Humanas.md`, linhas 312–323), incluindo as duas inferências proibidas (`Reclassificar como Goleiro`, `Atribuir 1 ponto`) |

## Critérios aprovados

1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 — todos os 11 critérios do handoff foram cumpridos.

## Critérios reprovados

Nenhum.

## Pendências

Pendências controladas (esperadas e corretamente sinalizadas, não bloqueantes
para o escopo desta tarefa):

1. `Papel_Regulamentar` — sem decisão humana literal própria; `PENDENTE_DEFINICAO_LITERAL`.
2. `Função_Situacional` — sem definição literal própria (apenas separada de `Papel_Tático`); `PENDENTE_DEFINICAO_LITERAL`.
3. `Posição_Espacial` — sem definição literal própria (apenas separada de `Papel_Tático`); `PENDENTE_DEFINICAO_LITERAL`.
4. `Jogador_De_Linha` — sem decisão humana literal própria; `PENDENTE_DEFINICAO_LITERAL`.
5. `Autor_Do_Gol` — sem decisão humana literal própria; `PENDENTE_DEFINICAO_LITERAL`.
6. `Fundamento_Da_Pontuação` — sem decisão humana literal própria; `PENDENTE_DEFINICAO_LITERAL`.

Pendências adicionais de gate, já declaradas na própria ficha
(`gates_pendentes`), não tratadas por esta validação documental:

7. Validação humana da transformação da ficha conceitual.
8. Execução efetiva do teste de competência `TC-ESP-001` (o teste está registrado, não executado).
9. Validação lógica ou estrutural.

Nenhuma das pendências acima foi resolvida por inferência. Nenhuma extrapola
o escopo de VOCAB-MIN-001.

## Decisão recomendada

Aceitar o handoff de VOCAB-MIN-001 com status
`VOCAB_MIN_001_APROVADA_COM_PENDENCIAS_CONTROLADAS`.

Não autorizado por esta validação:
- Continuar Regras 1–18.
- Gerar ontologia.
- Marcar `Especialista` ou qualquer arquivo deste escopo como `VALIDADO_TOTAL`.

Próxima ação autorizada por esta validação: registrar decisões humanas
literais próprias para os 6 termos pendentes (item "Pendências", 1–6) antes
de qualquer expansão do vocabulário canônico para além do escopo de
`Especialista`.
