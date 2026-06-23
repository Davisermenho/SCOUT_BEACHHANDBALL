---
id: DH-PONTUACAO-001-TEMPLATE
tipo: template_validacao_humana
status: TEMPLATE_CRIADO_AGUARDANDO_RESPOSTA_HUMANA
escopo:
  - Pontuação de gols
  - Especialista
  - Jogadora comum
  - Gol de giro
  - Gol aéreo
  - Gol criativo
  - Gol espetacular
  - R09-CAT-2026-06-18
gerado_em: "2026-06-23"
---

# DH-PONTUACAO-001 — Template de decisão humana

Este arquivo **não é** decisão humana literal. É um template de perguntas a
ser respondido pelo especialista do domínio. Nenhuma resposta deve ser
preenchida por inferência do agente.

Não preencher respostas por aproximação, resumo, regra presumida ou leitura
automática de categoria. Cada resposta deve ser registrada depois como fala
literal do especialista em arquivo próprio de decisão humana.

## Contexto

O bloco `PONTUACAO-001` foi aberto após o checkpoint das quatro dimensões
estruturais para tratar apenas os problemas de pontuação ainda bloqueados,
especialmente:

- `Gol de giro` / `Gol aéreo`;
- cruzamento com `R09-CAT-2026-06-18`;
- dependência do valor do gol em relação a papel, execução técnica e regra.

As quatro fichas estruturais já estão consolidadas semanticamente e não
devem ser alteradas nesta etapa.

## Perguntas obrigatórias

1. No seu modelo, quais gols valem 1 ponto?

   Resposta literal: _(pendente)_

2. No seu modelo, quais gols valem 2 pontos?

   Resposta literal: _(pendente)_

3. Todo gol da Especialista vale 2 pontos?

   Resposta literal: _(pendente)_

4. Existe gol de Especialista que vale 1 ponto?

   Resposta literal: _(pendente)_

5. Uma jogadora comum pode marcar gol de 2 pontos?

   Resposta literal: _(pendente)_

6. Qual é a diferença entre Gol de giro e Gol espetacular?

   Resposta literal: _(pendente)_

7. Qual é a diferença entre Gol aéreo e Gol espetacular?

   Resposta literal: _(pendente)_

8. Gol criativo é categoria própria ou forma de descrever gol espetacular?

   Resposta literal: _(pendente)_

9. O valor do gol depende do Papel_Tático?

   Resposta literal: _(pendente)_

10. O valor do gol depende do Papel_Regulamentar?

    Resposta literal: _(pendente)_

11. O valor do gol depende da Função_Situacional?

    Resposta literal: _(pendente)_

12. O valor do gol depende da execução técnica?

    Resposta literal: _(pendente)_

13. Como R09-CAT-2026-06-18 deve ser interpretada?

    Resposta literal: _(pendente)_

14. Quais inferências devem ser proibidas?

    Resposta literal: _(pendente)_

15. Quais casos de teste devem existir para validar pontuação?

    Resposta literal: _(pendente)_

## Regra

Este template não autoriza mudança de categoria, criação de ontologia,
taxonomia, promoção de conceito candidato, `VALIDADO_TOTAL` ou
`CONSOLIDADO_VALIDO`.

## Próximo passo após resposta

Quando as respostas humanas forem fornecidas literalmente, registrar
`DH-PONTUACAO-001` em arquivo próprio de decisão humana e só então avaliar
quais conceitos, categorias e testes de pontuação podem ser modelados sem
inferência.
