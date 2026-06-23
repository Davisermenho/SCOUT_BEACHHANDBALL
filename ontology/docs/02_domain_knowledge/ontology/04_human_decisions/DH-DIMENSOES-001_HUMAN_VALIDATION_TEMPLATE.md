---
id: DH-DIMENSOES-001-HUMAN-VALIDATION
tipo: template_validacao_humana
status: TEMPLATE_CRIADO_AGUARDANDO_RESPOSTA_HUMANA
escopo:
  - Papel_Tático
  - Papel_Regulamentar
  - Função_Situacional
  - Posição_Espacial
  - 15 casos de teste executados logicamente
gerado_em: "2026-06-23"
---

# DH-DIMENSOES-001 — Template de validação humana final

Este arquivo **não é** uma decisão humana literal. É um template de
perguntas a ser respondido pelo especialista do domínio (mesma autoridade
de `DH-ESP-001` e `DH-PAPEIS-001`). Nenhuma resposta foi preenchida ainda.

Não preencher estas respostas por inferência. Cada resposta deve ser a fala
literal do especialista, copiada como em `DH-ESP-001` e `DH-PAPEIS-001`
(`resposta_literal`), não uma paráfrase do agente.

## Contexto

As quatro fichas conceituais mínimas (`Papel_Tático`, `Papel_Regulamentar`,
`Função_Situacional`, `Posição_Espacial`) foram criadas em
`CONCEPT-DIMENSOES-001` a partir das respostas literais de `DH-PAPEIS-001`
e da clarificação `DH-PAPEIS-001_CLARIFICACAO_Q8`. Os 15 casos de teste de
competência derivados dessas fichas foram executados logicamente (de forma
manual, não contra uma implementação de software) em
`CONCEPT-DIMENSOES-001_TESTS_EXECUTION_REPORT.md`, com resultado de 15
aprovados e 0 reprovados.

Este template existe para coletar a validação humana final sobre se essas
fichas e esses resultados realmente representam o modelo do especialista,
antes de qualquer consolidação semântica.

## Arquivos a validar

- `docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_PAPEL_TATICO.yaml`
- `docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_PAPEL_REGULAMENTAR.yaml`
- `docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_FUNCAO_SITUACIONAL.yaml`
- `docs/02_domain_knowledge/ontology/01_concepts/FICHA_CONCEITUAL_POSICAO_ESPACIAL.yaml`
- `docs/02_domain_knowledge/ontology/02_competency_tests/TC-PAPEL-TATICO-001.yaml`
- `docs/02_domain_knowledge/ontology/02_competency_tests/TC-PAPEL-REGULAMENTAR-001.yaml`
- `docs/02_domain_knowledge/ontology/02_competency_tests/TC-FUNCAO-SITUACIONAL-001.yaml`
- `docs/02_domain_knowledge/ontology/02_competency_tests/TC-POSICAO-ESPACIAL-001.yaml`
- `docs/02_domain_knowledge/ontology/03_validation/CONCEPT-DIMENSOES-001_TESTS_EXECUTION_REPORT.md`

## Perguntas de validação humana

1. A definição de Papel_Tático como "missão estratégica temporária ou estrutural dada pelo treinador" está correta?

   Resposta literal: _(pendente)_

2. A definição de Papel_Regulamentar como "estatuto jurídico fixo determinado pelo livro de regras da IHF" está correta?

   Resposta literal: _(pendente)_

3. A definição de Função_Situacional como "microação baseada na leitura de resultados factuais do exato milissegundo" está correta?

   Resposta literal: _(pendente)_

4. A definição de Posição_Espacial como "coordenadas de organização estrutural e geográfica na quadra" está correta?

   Resposta literal: _(pendente)_

5. Está correto afirmar que Papel_Tático e Papel_Regulamentar são distintos, mas se articulam?

   Resposta literal: _(pendente)_

6. Está correto afirmar que Função_Situacional e Posição_Espacial são sempre distintas?

   Resposta literal: _(pendente)_

7. Está correto afirmar que Função_Situacional não altera Papel_Tático nem Papel_Regulamentar?

   Resposta literal: _(pendente)_

8. Está correto afirmar que Posição_Espacial isolada não altera Papel_Tático?

   Resposta literal: _(pendente)_

9. Está correto afirmar que Linha_Lateral altera Status_Operacional/Regulamentar, mas não cria Papel_Tático?

   Resposta literal: _(pendente)_

10. Os 15 casos de teste executados logicamente representam corretamente seu modelo?

    Resposta literal: _(pendente)_

11. Existe alguma afirmação nas quatro fichas que altera, reduz ou distorce seu modelo?

    Resposta literal: _(pendente)_

12. Existe algum caso de teste aprovado que você reprovaria como treinador?

    Resposta literal: _(pendente)_

13. Você autoriza que as quatro dimensões avancem para status CONSOLIDACAO_SEMANTICA_AUTORIZADA, ainda sem VALIDADO_TOTAL?

    Resposta literal: _(pendente)_

## Regra

Este template não é decisão humana final.

O agente não deve preencher respostas.

O agente não deve interpretar silêncio como aprovação.

O agente não deve consolidar conceito sem resposta literal do especialista.

## Próximo passo após resposta

Quando todas as respostas estiverem preenchidas literalmente, registrar
`DH-DIMENSOES-001-HUMAN-VALIDATION` em arquivo próprio de decisão humana
(mesmo padrão de `DH-PAPEIS-001.md`: respostas literais, sem ficha
conceitual, sem taxonomia, sem ontologia, sem resolver tensões por
inferência), e só então avaliar, em etapa própria de auditoria, se há base
para avançar ao status `CONSOLIDACAO_SEMANTICA_AUTORIZADA` mencionado na
pergunta 13.

Este template, por si só, não autoriza consolidação semântica, criação de
ficha conceitual nova, taxonomia, ontologia, nem avanço das Regras 1–18.
