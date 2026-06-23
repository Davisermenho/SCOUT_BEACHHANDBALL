---
doc_type: minimal_model_document
id: PONTUACAO-001-MODELAGEM-MINIMA
status: PONTUACAO_001_MODELO_MINIMO_CRIADO_AGUARDANDO_VALIDACAO
gerado_em: "2026-06-23"
base_semantica:
  - DH-PONTUACAO-001.md
  - DH-PONTUACAO-001_AUDIT_REPORT.md
nao_e_validacao_total: true
---

# PONTUACAO-001 — Modelo Mínimo

## Status

`PONTUACAO_001_MODELO_MINIMO_CRIADO_AGUARDANDO_VALIDACAO`

Este documento registra uma modelagem mínima controlada de pontuação com
base exclusiva na decisão humana literal `DH-PONTUACAO-001.md` e na sua
auditoria semântica. Este documento **não** é ficha conceitual, **não** é
teste de competência, **não** é taxonomia, **não** é ontologia principal e
**não** é regra executável.

## Finalidade desta modelagem

- registrar a ordem mínima de decisão de valor do gol já autorizada pela auditoria;
- preservar a separação entre `Papel_Tático`, `Papel_Regulamentar`,
  `Função_Situacional` e execução técnica;
- bloquear inferências proibidas antes de qualquer validação posterior.

## Base humana utilizada

- `DH-PONTUACAO-001.md`
- `DH-PONTUACAO-001_AUDIT_REPORT.md`

## Entradas semânticas mínimas observáveis

- `arremesso_resultou_em_gol`
- `origem_do_lance = Tiro_de_6_Metros`
- `Papel_Tatico_no_frame = Especialista`
- `Papel_Regulamentar_no_frame = Goleira`
- `Funcao_Situacional_no_frame = Finalizadora_de_Giro`
- `Funcao_Situacional_no_frame = Finalizadora_Aerea`
- `execucao_tecnica_observada = Giro_360`
- `execucao_tecnica_observada = Ponte_Aerea`

Estas entradas são documentais e semânticas. Elas **não** autorizam ainda
schema, classe final, API, enum executável ou motor de regras.

## Ordem mínima controlada de decisão

### Gate 0

Se `arremesso_resultou_em_gol = falso`, este modelo não calcula pontuação.

### Gate 1

Se `origem_do_lance = Tiro_de_6_Metros`, atribuir `Valor_do_Gol = 2`.

### Gate 2

Se `Papel_Tatico_no_frame = Especialista`, atribuir `Valor_do_Gol = 2`.

### Gate 3

Se `Papel_Regulamentar_no_frame = Goleira`, atribuir `Valor_do_Gol = 2`.

### Gate 4

Se a atleta não estiver coberta pelos gates anteriores e houver:

- `Funcao_Situacional_no_frame = Finalizadora_de_Giro`; ou
- `Funcao_Situacional_no_frame = Finalizadora_Aerea`; ou
- `execucao_tecnica_observada = Giro_360`; ou
- `execucao_tecnica_observada = Ponte_Aerea`

atribuir `Valor_do_Gol = 2`.

### Gate 5

Se todas as condições anteriores forem falsas e o arremesso resultou em
gol, classificar como `Gol_Simples` e atribuir `Valor_do_Gol = 1`.

## Tabela semântica mínima

| Condição mínima observada | Valor do gol | Observação |
|---|---:|---|
| `arremesso_resultou_em_gol = falso` | não calcular | Fora do escopo de pontuação |
| `origem_do_lance = Tiro_de_6_Metros` | 2 | Precedência explícita da decisão humana |
| `Papel_Tatico_no_frame = Especialista` | 2 | Não depende da plasticidade do arremesso |
| `Papel_Regulamentar_no_frame = Goleira` | 2 | Mantido separado de `Papel_Tático` |
| Jogadora comum com `Finalizadora_de_Giro` ou `Giro_360` | 2 | Efeito de pontuação, sem reclassificar papel |
| Jogadora comum com `Finalizadora_Aerea` ou `Ponte_Aerea` | 2 | Efeito de pontuação, sem reclassificar papel |
| Gol legal sem as condições acima | 1 | `Gol_Simples` |

## Restrições negativas explicitamente preservadas

- Proibir `Papel_Tatico = Atacante_Normal` com `Finalizacao_Simples` e `Valor_do_Gol = 2`.
- Proibir `Papel_Tatico = Especialista` com `Valor_do_Gol = 1`.

## Pendências controladas preservadas

- A divergência humana entre “5 testes” e lista com 6 testes permanece sem correção automática.
- A expressão humana `estatuto de Goleiro em Linha` permanece como fala explicativa, sem fundir `Especialista` e `Goleira`.
- `Função_Situacional` pode afetar pontuação sem alterar `Papel_Tático` ou `Papel_Regulamentar`.
- `R09-CAT-2026-06-18` permanece como amarração semântica, não como regra executável.
- `Gol criativo` permanece como descrição/jargão, não como classe consolidada.

## Limites obrigatórios desta modelagem

- Não transformar `Especialista` em `Goleira`.
- Não fundir `Papel_Tático` e `Papel_Regulamentar`.
- Não usar pontuação para reclassificar `Papel_Tático`.
- Não usar pontuação para reclassificar `Papel_Regulamentar`.
- Não transformar `Gol criativo` em classe.
- Não criar ficha conceitual de `Gol`.
- Não criar ficha conceitual de `Pontuação`.
- Não criar ficha conceitual de `Gol_Espetacular`.
- Não criar ficha conceitual de `Gol_de_Giro`.
- Não criar ficha conceitual de `Gol_Aereo`.
- Não criar testes de competência de pontuação.
- Não criar taxonomia geral.
- Não gerar ontologia principal.
- Não transformar este modelo em regra executável.
- Não alterar as quatro fichas consolidadas.
- Não alterar testes existentes.
- Não alterar arquivos protegidos.
- Não marcar `VALIDADO_TOTAL`.
- Não marcar `CONSOLIDADO_VALIDO`.

## Próximo gate documental

```yaml
proximo_ponto_exato:
  id: PONTUACAO-001-MODELAGEM-MINIMA-VALIDATION
  tarefa: "Validar se o modelo mínimo preserva a decisão humana auditada, os limites e os bloqueios sem extrapolação."
```
