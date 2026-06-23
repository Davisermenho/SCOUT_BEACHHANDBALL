---
doc_type: validation_report
tarefa_validada: CONCEPT-GOLEIRO-001
status_geral: CONCEPT_GOLEIRO_001_APROVADA_COM_PENDENCIAS_CONTROLADAS
gerado_em: "2026-06-22"
nao_e_validacao_total: true
---

# Relatório de Validação — CONCEPT-GOLEIRO-001

## Status geral

`CONCEPT_GOLEIRO_001_APROVADA_COM_PENDENCIAS_CONTROLADAS`

Esta validação cobre exclusivamente o handoff de CONCEPT-GOLEIRO-001 (ficha
conceitual mínima + teste de competência do conceito `Goleiro`, limitada ao
que já está seguro em `DH-ESP-001`). Não é uma validação total do conceito
de Goleiro pela regra oficial IHF, nem da ontologia, das Regras 1–18 ou dos
Apêndices.

## Arquivos verificados

| # | Arquivo | Existe no path correto |
|---|---------|--------------------------|
| 1 | `docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_GOLEIRO.yaml` | Sim |
| 2 | `docs/02_domain_knowledge/ontology/02_competency_tests/TC-GOL-001.yaml` | Sim |

Entradas obrigatórias consultadas:
- `docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_ESPECIALISTA.yaml`
- `docs/02_domain_knowledge/ontology/00_governance/VOCABULARIO_CANONICO_MINIMO.md`
- `docs/02_domain_knowledge/ontology/03_validation/VOCAB-MIN-001_VALIDATION_REPORT.md`
- `files/Decisões Humanas.md` (bloco `DH-ESP-001`)
- `prompt.md` (especificação literal de CONCEPT-GOLEIRO-001)

## Verificação de não-alteração de arquivos fora do escopo

| Arquivo | Tamanho esperado (07_blockers_report.md) | Tamanho atual | Resultado |
|---|---|---|---|
| `files/Regras 1–18.md` | 155662 bytes | 155662 bytes | inalterado |
| `files/Apêndices.md` | 47720 bytes | 47720 bytes | inalterado |
| `files/Decisões Humanas.md` (contém DH-ESP-001) | 18443 bytes | 18443 bytes | inalterado |

Nenhum arquivo de ontologia principal existe no repositório. O diretório
`docs/02_domain_knowledge/ontology/` contém apenas os artefatos já registrados
(VOCAB-MIN-001 + HANDOFF + os dois arquivos desta tarefa), sem arquivos extras
fora do escopo autorizado.

## Critérios avaliados

| # | Critério | Resultado | Evidência |
|---|----------|-----------|-----------|
| 1 | Os dois arquivos existem nos paths corretos | APROVADO | Listagem de diretório confirma os 2 arquivos |
| 2 | Nenhuma regra, apêndice, ontologia principal ou DH-ESP-001 foi alterada | APROVADO | Tamanhos de `Regras 1–18.md`, `Apêndices.md` e `Decisões Humanas.md` idênticos aos registrados em `07_blockers_report.md` |
| 3 | Goleiro é diferente de Especialista | APROVADO | Ficha `FC-GOL-001-01`: `Goleiro não_é Especialista` (simétrico a `FC-ESP-001-02` da ficha do Especialista) |
| 4 | Goleiro permanece Goleiro ao sair da área | APROVADO | Ficha `FC-GOL-001-02`: `Goleiro permanece_como Goleiro` (condição: `ao_sair_da_area_de_gol`) |
| 5 | Goleiro que cobra falta fora da área continua sendo Goleiro | APROVADO | Ficha `FC-GOL-001-03`: `Goleiro permanece_como Goleiro` (condição: `cobrar_falta_fora_da_area_de_gol`) |
| 6 | Goleiro não se transforma em Especialista por atuar fora da área | APROVADO | Ficha `FC-GOL-001-04`: `Goleiro não_se_transforma_em Especialista` (condição: `atuar_fora_da_area_de_gol`) |
| 7 | Goleiro_Atuando_No_Ataque é diferente de Especialista | APROVADO | Ficha `FC-GOL-001-05`: `Goleiro_Atuando_No_Ataque não_é Especialista`, reproduzindo literalmente `separacoes_obrigatorias` de DH-ESP-001 |
| 8 | Fonte de autoridade DH-ESP-001 presente | APROVADO | `fonte_de_autoridade: DH-ESP-001` no cabeçalho da ficha; `fonte: DH-ESP-001` em todas as 5 afirmações; `fonte: DH-ESP-001` em TC-GOL-001 |
| 9 | Status não marcado como VALIDADO_TOTAL | APROVADO | Ficha usa `status: REGISTRADA_LITERALMENTE_AGUARDANDO_GATES_RESTANTES`, idêntico ao padrão usado na ficha do Especialista |
| 10 | Pendências obrigatórias marcadas PENDENTE_DEFINICAO_LITERAL | APROVADO | Bloco `termos_pendentes` da ficha marca `Definição_Regulamentar_Completa_De_Goleiro`, `Papel_Regulamentar`, `Função_Situacional`, `Posição_Espacial` e `Regras_Oficiais_IHF_Sobre_Goleiro`, todos com `status: PENDENTE_DEFINICAO_LITERAL` |
| 11 | TC-GOL-001 contém entrada e esperado compatíveis com o bloco literal do prompt | APROVADO | Bloco `entrada`/`esperado` de `TC-GOL-001.yaml` é idêntico, campo a campo, ao bloco `TESTE TC-GOL-001` especificado em `prompt.md` |

## Critérios aprovados

1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 — todos os 11 critérios avaliados foram cumpridos.

## Critérios reprovados

Nenhum.

## Pendências

Pendências controladas (esperadas e corretamente sinalizadas, não bloqueantes
para o escopo desta tarefa):

1. `Definição_Regulamentar_Completa_De_Goleiro` — depende de regras oficiais IHF ainda não reprocessadas; `PENDENTE_DEFINICAO_LITERAL`.
2. `Papel_Regulamentar` — já pendente desde VOCAB-MIN-001; `PENDENTE_DEFINICAO_LITERAL`.
3. `Função_Situacional` — já pendente desde VOCAB-MIN-001; `PENDENTE_DEFINICAO_LITERAL`.
4. `Posição_Espacial` — já pendente desde VOCAB-MIN-001; `PENDENTE_DEFINICAO_LITERAL`.
5. `Regras_Oficiais_IHF_Sobre_Goleiro` — fora do escopo de CONCEPT-GOLEIRO-001; `PENDENTE_DEFINICAO_LITERAL`.

Pendências adicionais de gate, já declaradas na própria ficha
(`gates_pendentes`), não tratadas por esta validação documental:

6. Validação humana da transformação da ficha conceitual.
7. Execução efetiva do teste de competência `TC-GOL-001` (o teste está registrado, não executado).
8. Validação lógica ou estrutural.

Nenhuma das pendências acima foi resolvida por inferência. Nenhuma extrapola
o escopo de CONCEPT-GOLEIRO-001.

## Decisão recomendada

Aceitar o handoff de CONCEPT-GOLEIRO-001 com status
`CONCEPT_GOLEIRO_001_APROVADA_COM_PENDENCIAS_CONTROLADAS`.

Não autorizado por esta validação:
- Continuar Regras 1–18.
- Gerar ontologia.
- Reconstruir a definição regulamentar completa de Goleiro pela regra oficial IHF.
- Marcar `Goleiro` ou qualquer arquivo deste escopo como `VALIDADO_TOTAL`.

Próxima ação autorizada por esta validação: atualizar `HANDOFF.md` registrando
o fechamento de CONCEPT-GOLEIRO-001 e aguardar definição do próximo ponto
exato antes de qualquer nova etapa.
