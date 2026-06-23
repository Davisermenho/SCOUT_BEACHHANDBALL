---
doc_type: handoff_master
status: current
governed_by: 00_ESTADO_REAL_AUDITADO.md
superseded_by: null
last_reviewed: "2026-06-22"
---

# HANDOFF — Ontologia do Handebol de Areia

Este arquivo é o marcador mestre de continuidade do novo fluxo de governança
(`docs/02_domain_knowledge/ontology/`). Substitui, para fins de continuidade
operacional, os blocos de handoff legados embutidos em `files/Operacional.md`
e `results_auditoria_python/12345.md` — ambos classificados como
`PROTOCOLO_NÃO_EXECUTÁVEL` / histórico em `00_ESTADO_REAL_AUDITADO.md` e não
mais usados para determinar o próximo ponto autorizado.

Nenhum status `VALIDADO_TOTAL` ou `CONCLUÍDA_E_VALIDADA` deste arquivo pode
ser herdado sem passar pelos gates listados em `00_ESTADO_REAL_AUDITADO.md`.

## Estado atual

```yaml
ultima_etapa_concluida:
  id: DH-DIMENSOES-001-HUMAN-VALIDATION-AUDIT
  status: DH_DIMENSOES_001_VALIDACAO_HUMANA_AUDITADA_AUTORIZANDO_CONSOLIDACAO_SEMANTICA

proximo_ponto_exato:
  id: CONCEPT-DIMENSOES-001-CONSOLIDATION
  tarefa: "Aplicar CONSOLIDACAO_SEMANTICA_AUTORIZADA às quatro dimensões estruturais."
```

## Histórico de etapas concluídas

```yaml
- id: CONCEPT-DIMENSOES-001-TESTS-VALIDATION
  status: CONCEPT_DIMENSOES_001_TESTES_VALIDOS_AGUARDANDO_EXECUCAO

- id: CONCEPT-DIMENSOES-001-TESTS-EXECUTION
  status: CONCEPT_DIMENSOES_001_TESTES_EXECUTADOS_COM_SUCESSO_AGUARDANDO_VALIDACAO_HUMANA
  resultado:
    casos_executados: 15
    casos_aprovados: 15
    casos_reprovados: 0
    tipo_execucao: logica_manual
  arquivos_criados:
    - /docs/02_domain_knowledge/ontology/03_validation/CONCEPT-DIMENSOES-001_TESTS_EXECUTION_REPORT.md

- id: CONCEPT-DIMENSOES-001-VALIDATION
  status: CONCEPT_DIMENSOES_001_APROVADA_COM_PENDENCIAS_CONTROLADAS

- id: CONCEPT-DIMENSOES-001-TESTS
  status: (testes criados; validados em CONCEPT-DIMENSOES-001-TESTS-VALIDATION abaixo)
  arquivos_criados:
    - /docs/02_domain_knowledge/ontology/02_competency_tests/TC-PAPEL-TATICO-001.yaml
    - /docs/02_domain_knowledge/ontology/02_competency_tests/TC-PAPEL-REGULAMENTAR-001.yaml
    - /docs/02_domain_knowledge/ontology/02_competency_tests/TC-FUNCAO-SITUACIONAL-001.yaml
    - /docs/02_domain_knowledge/ontology/02_competency_tests/TC-POSICAO-ESPACIAL-001.yaml

- id: CONCEPT-DIMENSOES-001-TESTS-VALIDATION
  status: CONCEPT_DIMENSOES_001_TESTES_VALIDOS_AGUARDANDO_EXECUCAO
  criterios_aprovados: 13
  criterios_reprovados: 0
  arquivos_criados:
    - /docs/02_domain_knowledge/ontology/03_validation/CONCEPT-DIMENSOES-001_TESTS_VALIDATION_REPORT.md

- id: DH-PAPEIS-001-SEMANTIC-AUDIT
  status: DH_PAPEIS_001_AUDITADA_SEMANTICAMENTE_AUTORIZANDO_FICHAS_MINIMAS
  arquivos_criados:
    - /docs/02_domain_knowledge/ontology/03_validation/DH-PAPEIS-001_SEMANTIC_AUDIT_REPORT.md

- id: CONCEPT-DIMENSOES-001
  status: (fichas criadas; validadas em CONCEPT-DIMENSOES-001-VALIDATION abaixo)
  arquivos_criados:
    - /docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_PAPEL_TATICO.yaml
    - /docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_PAPEL_REGULAMENTAR.yaml
    - /docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_FUNCAO_SITUACIONAL.yaml
    - /docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_POSICAO_ESPACIAL.yaml

- id: CONCEPT-DIMENSOES-001-VALIDATION
  status: CONCEPT_DIMENSOES_001_APROVADA_COM_PENDENCIAS_CONTROLADAS
  criterios_aprovados: 15
  criterios_reprovados: 0
  pendencias_controladas:
    - definição extensional completa de Papel_Tático para todos os papéis possíveis
    - separação genérica Papel_Tático ≠ Papel_Regulamentar (sustentada apenas indiretamente)
    - definição regulamentar completa de Papel_Regulamentar (depende de Regras 1-18 ainda não reprocessadas)
    - Jogador_De_Linha (PENDENTE_DEFINICAO_LITERAL)
    - definição extensional completa das funções situacionais e sistemas táticos citados
    - 10 conceitos candidatos bloqueados (Status_Operacional, Linha_Lateral, Transição_Híbrida, etc.)
    - Gol de giro / Gol aéreo e cruzamento com R09-CAT-2026-06-18
  arquivos_criados:
    - /docs/02_domain_knowledge/ontology/03_validation/CONCEPT-DIMENSOES-001_VALIDATION_REPORT.md

- id: DH-PAPEIS-001-CLARIFY-Q8
  status: DH_PAPEIS_001_Q8_VALIDADA_COM_CLARIFICACAO_SEMANTICA
  arquivos_criados:
    - /docs/02_domain_knowledge/ontology/04_human_decisions/DH-PAPEIS-001_CLARIFICACAO_Q8.md
    - /docs/02_domain_knowledge/ontology/03_validation/DH-PAPEIS-001_CLARIFICACAO_Q8_VALIDATION_REPORT.md

- id: CONCEPT-PAPEIS-001
  status: CONCEPT_PAPEIS_001_APROVADA_COM_PENDENCIAS_CONTROLADAS
  criterios_aprovados: 8
  criterios_reprovados: 0
  pendencias_controladas:
    - Papel_Regulamentar (sem decisão humana literal própria)
    - Função_Situacional (sem definição literal própria)
    - Posição_Espacial (sem definição literal própria)
    - separação genérica Papel_Tático ≠ Papel_Regulamentar (sustentada apenas indiretamente)
    - separação Função_Situacional ≠ Posição_Espacial (lacuna conhecida, sem fonte literal)
  arquivos_criados:
    - /docs/02_domain_knowledge/ontology/01_concepts/CONCEPT_PAPEIS_SEPARACAO_MINIMA.yaml
    - /docs/02_domain_knowledge/ontology/03_validation/CONCEPT-PAPEIS-001_VALIDATION_REPORT.md

- id: VOCAB-MIN-001
  status: VOCAB_MIN_001_APROVADA_COM_PENDENCIAS_CONTROLADAS
  criterios_aprovados: 11
  criterios_reprovados: 0
  pendencias_controladas:
    - Papel_Regulamentar
    - Função_Situacional
    - Posição_Espacial
    - Jogador_De_Linha
    - Autor_Do_Gol
    - Fundamento_Da_Pontuação
  gates_restantes:
    - validação humana
    - execução de TC-ESP-001
    - validação lógica/estrutural

- id: CONCEPT-GOLEIRO-001
  status: CONCEPT_GOLEIRO_001_APROVADA_COM_PENDENCIAS_CONTROLADAS
  criterios_aprovados: 11
  criterios_reprovados: 0
  pendencias_controladas:
    - definição regulamentar completa de Goleiro
    - Papel_Regulamentar
    - Função_Situacional
    - Posição_Espacial
    - regras IHF ainda não reprocessadas
  arquivos_criados:
    - /docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_GOLEIRO.yaml
    - /docs/02_domain_knowledge/ontology/02_competency_tests/TC-GOL-001.yaml
    - /docs/02_domain_knowledge/ontology/03_validation/CONCEPT-GOLEIRO-001_VALIDATION_REPORT.md
```

## Evidência

- `docs/02_domain_knowledge/ontology/00_governance/VOCABULARIO_CANONICO_MINIMO.md`
- `docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_ESPECIALISTA.yaml`
- `docs/02_domain_knowledge/ontology/02_competency_tests/TC-ESP-001.yaml`
- `docs/02_domain_knowledge/ontology/03_validation/VOCAB-MIN-001_VALIDATION_REPORT.md`
- `docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_GOLEIRO.yaml`
- `docs/02_domain_knowledge/ontology/02_competency_tests/TC-GOL-001.yaml`
- `docs/02_domain_knowledge/ontology/03_validation/CONCEPT-GOLEIRO-001_VALIDATION_REPORT.md`
- `docs/02_domain_knowledge/ontology/01_concepts/CONCEPT_PAPEIS_SEPARACAO_MINIMA.yaml`
- `docs/02_domain_knowledge/ontology/03_validation/CONCEPT-PAPEIS-001_VALIDATION_REPORT.md`
- `docs/02_domain_knowledge/ontology/04_human_decisions/DH-PAPEIS-001.md`
- `docs/02_domain_knowledge/ontology/03_validation/DH-PAPEIS-001_VALIDATION_REPORT.md`
- `docs/02_domain_knowledge/ontology/04_human_decisions/DH-PAPEIS-001_CLARIFICACAO_Q8.md`
- `docs/02_domain_knowledge/ontology/03_validation/DH-PAPEIS-001_CLARIFICACAO_Q8_VALIDATION_REPORT.md`
- `docs/02_domain_knowledge/ontology/03_validation/DH-PAPEIS-001_SEMANTIC_AUDIT_REPORT.md`
- `docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_PAPEL_TATICO.yaml`
- `docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_PAPEL_REGULAMENTAR.yaml`
- `docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_FUNCAO_SITUACIONAL.yaml`
- `docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_POSICAO_ESPACIAL.yaml`
- `docs/02_domain_knowledge/ontology/03_validation/CONCEPT-DIMENSOES-001_VALIDATION_REPORT.md`
- `docs/02_domain_knowledge/ontology/02_competency_tests/TC-PAPEL-TATICO-001.yaml`
- `docs/02_domain_knowledge/ontology/02_competency_tests/TC-PAPEL-REGULAMENTAR-001.yaml`
- `docs/02_domain_knowledge/ontology/02_competency_tests/TC-FUNCAO-SITUACIONAL-001.yaml`
- `docs/02_domain_knowledge/ontology/02_competency_tests/TC-POSICAO-ESPACIAL-001.yaml`
- `docs/02_domain_knowledge/ontology/03_validation/CONCEPT-DIMENSOES-001_TESTS_VALIDATION_REPORT.md`
- `docs/02_domain_knowledge/ontology/03_validation/CONCEPT-DIMENSOES-001_TESTS_EXECUTION_REPORT.md`

## Regra de continuidade

A próxima ação autorizada é exatamente `proximo_ponto_exato.id` acima. Não
avançar para regras 1–18, apêndices ou geração de ontologia a partir deste
handoff.
