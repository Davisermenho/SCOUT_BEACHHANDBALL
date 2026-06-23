---
doc_type: vocabulario_canonico
escopo: VOCAB-MIN-001
objetivo: destravar_conceito_Especialista
status: PARCIAL_MINIMO
nao_e_ontologia: true
nao_substitui_vocabulario_completo: true
fonte_primaria: DH-ESP-001
fontes_auxiliares:
  - results_auditoria_python/00_ESTADO_REAL_AUDITADO.md
  - results_auditoria_python/07_blockers_report.md
  - results_auditoria_python/03_missing_vocabulary_terms.csv
  - results_auditoria_python/04_invalid_predicates.csv
gerado_em: "2026-06-22"
---

# Vocabulário Canônico Mínimo — escopo VOCAB-MIN-001

Este documento declara somente o vocabulário mínimo necessário para destravar
o conceito `Especialista`, conforme listado no bloqueio "Conceitos centrais
ausentes ou insuficientes" de `00_ESTADO_REAL_AUDITADO.md` e na decisão
`DH-ESP-001`.

Este documento **não é** a ontologia, **não** estende as Regras 1–18, **não**
altera Apêndices e **não** herda nenhum status `VALIDADO` ou
`CONCLUÍDA_E_VALIDADA` de pipelines anteriores.

Termos sem definição literal em `DH-ESP-001` são marcados como
`PENDENTE_DEFINICAO_LITERAL` e permanecem assim. Eles **não** foram completados
por inferência.

## Termos declarados

### Papel_Tático
- tipo: classe
- status: DECLARADO_LITERAL
- fonte: DH-ESP-001
- nota: `Especialista` é classificado como `Papel_Tático` em DH-ESP-001 ("O papel de especialista é uma condição não por causa da regra, mas sim pelo desenvolvimento tático").

### Papel_Regulamentar
- tipo: classe
- status: PENDENTE_DEFINICAO_LITERAL
- fonte: DH-ESP-001 (menção indireta), 00_ESTADO_REAL_AUDITADO.md
- nota: DH-ESP-001 exige que `Especialista` não seja modelado apenas como papel regulamentar oficial ("O papel de especialista não é criado pela regra oficial"), mas não define `Papel_Regulamentar` em si. Definição própria pendente de decisão humana literal específica.

### Função_Situacional
- tipo: classe
- status: PENDENTE_DEFINICAO_LITERAL
- fonte: DH-ESP-001 (separações obrigatórias), 00_ESTADO_REAL_AUDITADO.md
- nota: DH-ESP-001 exige a separação "Papel_Tático é diferente de Função_Situacional", mas não define `Função_Situacional` literalmente.

### Posição_Espacial
- tipo: classe
- status: PENDENTE_DEFINICAO_LITERAL
- fonte: DH-ESP-001 (separações obrigatórias), 00_ESTADO_REAL_AUDITADO.md
- nota: DH-ESP-001 exige a separação "Papel_Tático é diferente de Posição_Espacial" e usa `Area_De_Gol` como valor de posição espacial no teste de competência obrigatório. Definição geral pendente.

### Especialista
- tipo: classe
- status: DECLARADO_LITERAL
- fonte: DH-ESP-001
- nota: `Papel_Tático`. Permanece `Especialista` independentemente de posição espacial (dentro ou fora da área de gol). Não se transforma em `Goleiro` ao atuar momentaneamente no gol.

### Goleiro
- tipo: classe
- status: DECLARADO_LITERAL
- fonte: DH-ESP-001
- nota: Permanece `Goleiro` independentemente de sair da área ou de cobrar falta fora da área. Não se transforma em `Especialista` por atuar no ataque.

### Jogador_De_Linha
- tipo: classe
- status: PENDENTE_DEFINICAO_LITERAL
- fonte: 00_ESTADO_REAL_AUDITADO.md
- nota: Listado como conceito central ausente. Sem decisão humana literal própria registrada até o momento. Não definido por inferência.

### Autor_Do_Gol
- tipo: classe
- status: PENDENTE_DEFINICAO_LITERAL
- fonte: 00_ESTADO_REAL_AUDITADO.md
- nota: Listado como conceito central ausente. Sem decisão humana literal própria registrada até o momento. Não definido por inferência.

### Valor_Do_Gol
- tipo: atributo
- status: DECLARADO_LITERAL (parcial)
- fonte: DH-ESP-001
- nota: Para `Gol_De_Especialista`, o valor é sempre 2 pontos e nunca 1 ponto. O comportamento geral de `Valor_Do_Gol` fora do caso do especialista não é definido por DH-ESP-001.

### Fundamento_Da_Pontuação
- tipo: classe
- status: PENDENTE_DEFINICAO_LITERAL
- fonte: 00_ESTADO_REAL_AUDITADO.md
- nota: Listado como conceito central ausente. Sem decisão humana literal própria registrada até o momento. Não definido por inferência.

### Gol_De_Especialista
- tipo: classe
- status: DECLARADO_LITERAL
- fonte: DH-ESP-001
- nota: Gol marcado por `Especialista`. Vale sempre 2 pontos. Nunca vale 1 ponto, em nenhum jogo, conforme DH-ESP-001.

### Inferência_Proibida
- tipo: construto_metodológico
- status: DECLARADO_LITERAL
- fonte: DH-ESP-001, 00_ESTADO_REAL_AUDITADO.md
- nota: Mecanismo de governança que registra inferências explicitamente vedadas por decisão humana literal. Para `Especialista`, ver lista `inferencias_proibidas` em DH-ESP-001.

### Teste_De_Competência
- tipo: construto_metodológico
- status: DECLARADO_LITERAL
- fonte: DH-ESP-001, 00_ESTADO_REAL_AUDITADO.md
- nota: Mecanismo de validação que verifica se um conceito se comporta conforme decisão humana literal frente a uma entrada controlada. Para `Especialista`, ver `TC-ESP-001.yaml`, derivado de `teste_de_competencia_obrigatorio` em DH-ESP-001.

## Predicados canônicos usados neste escopo

Declarados apenas para uso pela ficha conceitual deste escopo
(`FICHA_CONCEITUAL_ESPECIALISTA.yaml`). Não substituem o relatório geral de
predicados não canônicos (`04_invalid_predicates.csv`).

- `é_subclasse_de`
- `não_é`
- `permanece_como`
- `não_se_transforma_em`
- `vale_pontos`
- `nunca_vale_pontos`
- `fonte_de_autoridade`

## Critério de aceite deste documento

Este arquivo cobre exclusivamente o escopo de VOCAB-MIN-001 (destravar
`Especialista`). Não resolve os demais bloqueios de vocabulário listados em
`00_ESTADO_REAL_AUDITADO.md`. Não autoriza geração de ontologia.
