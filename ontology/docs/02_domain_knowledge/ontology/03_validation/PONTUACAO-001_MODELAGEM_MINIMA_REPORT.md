---
doc_type: validation_report
tarefa_validada: PONTUACAO-001-MODELAGEM-MINIMA
status_geral: PONTUACAO_001_MODELAGEM_MINIMA_EXECUTADA_AGUARDANDO_VALIDACAO
gerado_em: "2026-06-23"
nao_e_validacao_total: true
---

# Relatório de Modelagem Mínima — PONTUACAO-001

## Status geral

`PONTUACAO_001_MODELAGEM_MINIMA_EXECUTADA_AGUARDANDO_VALIDACAO`

Esta etapa cria apenas uma modelagem mínima controlada de pontuação com
base na decisão humana auditada. Esta etapa **não** cria ficha conceitual,
**não** cria testes de competência, **não** cria taxonomia, **não** gera
ontologia principal e **não** converte a modelagem em regra executável.

## Entradas utilizadas

1. `docs/02_domain_knowledge/ontology/04_human_decisions/DH-PONTUACAO-001.md`
2. `docs/02_domain_knowledge/ontology/03_validation/DH-PONTUACAO-001_AUDIT_REPORT.md`
3. `docs/02_domain_knowledge/ontology/00_governance/PONTUACAO-001_SCOPE.md`
4. `docs/02_domain_knowledge/ontology/03_validation/PONTUACAO-001_SCOPING_REPORT.md`
5. `docs/02_domain_knowledge/ontology/00_governance/HANDOFF.md`

## Arquivos criados

| # | Arquivo | Finalidade |
|---|---|---|
| 1 | `docs/02_domain_knowledge/ontology/00_governance/PONTUACAO-001_MODELO_MINIMO.md` | Registrar a ordem mínima controlada de decisão de valor do gol |
| 2 | `docs/02_domain_knowledge/ontology/03_validation/PONTUACAO-001_MODELAGEM_MINIMA_REPORT.md` | Registrar a execução da etapa e seus limites |

## Conteúdo modelado

O modelo mínimo criado registra apenas:

- gate de não cálculo quando não houver gol;
- prioridade para `Tiro_de_6_Metros = 2 pontos`;
- prioridade para `Papel_Tático = Especialista = 2 pontos`;
- prioridade para `Papel_Regulamentar = Goleira = 2 pontos`;
- efeito de `Função_Situacional` / execução técnica de `Giro` ou `Aéreo` para jogadora comum = `2 pontos`;
- caso residual de gol legal simples = `1 ponto`.

## Pendências e bloqueios preservados

- `QTD-TESTES-001` permanece sem correção automática.
- `TERM-GOLEIRO-EM-LINHA-001` permanece sem fusão entre `Especialista` e `Goleira`.
- `FUNCAO-ALTERA-VALOR-001` foi preservado como efeito de pontuação, não como alteração de papel.
- `R09-CAT-001` permanece como amarração semântica, não como regra executável.
- `Gol criativo` permanece como jargão descritivo, não como classe consolidada.

## Limites preservados

- não criar ficha conceitual de `Gol`;
- não criar ficha conceitual de `Pontuação`;
- não criar ficha conceitual de `Gol_Espetacular`;
- não criar ficha conceitual de `Gol_de_Giro`;
- não criar ficha conceitual de `Gol_Aereo`;
- não criar testes de competência de pontuação;
- não criar taxonomia geral;
- não gerar ontologia principal;
- não transformar o modelo em regra executável;
- não alterar as quatro fichas consolidadas;
- não alterar testes existentes;
- não alterar `Regras 1–18.md`;
- não alterar `Apêndices.md`;
- não alterar `Decisões Humanas.md`;
- não alterar `DH-ESP-001`;
- não alterar `DH-PAPEIS-001.md`;
- não alterar `DH-PAPEIS-001_CLARIFICACAO_Q8.md`;
- não alterar `DH-DIMENSOES-001_HUMAN_VALIDATION.md`;
- não fundir `Especialista` com `Goleira`;
- não usar pontuação para reclassificar `Papel_Tático` ou `Papel_Regulamentar`;
- não transformar `Gol criativo` em classe consolidada;
- não marcar `VALIDADO_TOTAL`;
- não marcar `CONSOLIDADO_VALIDO`.

## Verificação de escopo

Após a criação dos dois documentos desta etapa:

- nenhuma ficha conceitual foi criada;
- nenhum teste de competência foi criado;
- nenhuma taxonomia geral foi criada;
- nenhuma ontologia principal foi gerada;
- nenhuma ficha consolidada foi alterada;
- nenhum arquivo protegido foi alterado.

## Decisão recomendada

Aceitar a execução documental de `PONTUACAO-001-MODELAGEM-MINIMA` com status
`PONTUACAO_001_MODELAGEM_MINIMA_EXECUTADA_AGUARDANDO_VALIDACAO`.

Próxima etapa autorizada por este resultado:

```yaml
proximo_ponto_exato:
  id: PONTUACAO-001-MODELAGEM-MINIMA-VALIDATION
  tarefa: "Validar se o modelo mínimo preserva a decisão humana auditada, os limites e os bloqueios sem extrapolação."
```
