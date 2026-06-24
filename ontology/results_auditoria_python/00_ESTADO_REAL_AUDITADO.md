---
doc_type: governance_log
derived: false
should_be_derived: false
status: current
governed_by: null
generated_by: null
script_version_documented_against: "2.0.0"
metrics_source_of_truth: results_auditoria_python/07_blockers_report.md
superseded_by: null
last_reviewed: "2026-06-22"
---

<!--
NOTA PARA AGENTES: a seção de métricas no bloco YAML ao final deste documento
tem should_be_derived: true — é mantida à mão e já causou drift no passado.
Nunca copie números de métricas para aqui ou para outro documento; sempre
referencie results_auditoria_python/07_blockers_report.md.
-->

# 00_ESTADO_REAL_AUDITADO

## Status do documento

Este documento é o novo ponto seguro de retomada do projeto de ontologia do handebol de areia.

A função deste arquivo não é continuar a ontologia. A função é registrar o estado real após a auditoria do pipeline anterior e impedir que status antigos sejam usados como verdade.

## Regra de bloqueio principal

Nenhum status VALIDADO, CONCLUÍDA_E_VALIDADA ou equivalente presente nos arquivos anteriores pode ser herdado automaticamente.

Todo conteúdo anterior deve ser tratado como rascunho auditado até que passe novamente pelos seguintes gates:

1. fonte primária ou decisão humana literal preservada;
2. rastreabilidade por afirmação individual;
3. vocabulário canônico declarado;
4. predicado canônico permitido;
5. ID único;
6. validação humana da transformação;
7. teste de competência;
8. validação lógica ou estrutural.

## Arquivos herdados do pipeline anterior

1. Regras Ontológicas do Handebol.md
   - Status real: RASCUNHO_AUDITADO_COM_CONTRADIÇÕES.
   - Motivo: contém governança útil, mas também status conflitantes, regimes temporais problemáticos e conceitos marcados como validados sem definição operacional suficiente.

2. Vocabulário e Taxonomia.md
   - Status real: INCOMPLETO.
   - Motivo: não contém conceitos centrais como Especialista, Papel_Tático, Função_Situacional, Posição_Espacial, Fundamento_Da_Pontuação e inferências proibidas.

3. Regras 1–18.md
   - Status real: EXTRAÇÃO_PRELIMINAR_COM_RISCO_DE_COLISÃO.
   - Motivo: há afirmações úteis, mas a extração não pode ser tratada como ontologia validada sem auditoria de IDs, predicados, fonte e duplicidades.

4. Apêndices.md
   - Status real: EXTRAÇÃO_PRELIMINAR_NÃO_VALIDADA.
   - Motivo: contém informação relevante, mas mistura pendências semânticas com status de conclusão.

5. Rastreabilidade.md
   - Status real: INVENTÁRIO_DE_BLOCOS_NÃO_RASTREABILIDADE_COMPLETA.
   - Motivo: registra blocos e páginas, mas não prova a origem de cada afirmação individual.

6. Decisões Humanas.md
   - Status real: REGISTRO_INSUFICIENTE.
   - Motivo: contém aprovações genéricas como OK, B_OK, C_OK ou APROVADA, mas não preserva suficientemente a pergunta feita, a resposta literal do especialista, as decisões extraídas e as inferências proibidas.

7. Operacional.md
   - Status real: PROTOCOLO_NÃO_EXECUTÁVEL.
   - Motivo: contém boas intenções operacionais, mas não possui enforcement técnico suficiente para impedir avanço indevido da IA.

## Bloqueios de continuidade

A ontologia está bloqueada até que sejam resolvidos os seguintes pontos:

1. Criar decisão humana literal para o conceito Especialista.
2. Inserir Especialista no vocabulário canônico.
3. Separar Papel_Tático, Papel_Regulamentar, Função_Situacional e Posição_Espacial.
4. Rebaixar todos os status de validação herdados que não possuam evidência completa.
5. Rodar auditoria Python nos arquivos herdados.
6. Gerar relatório de IDs duplicados.
7. Gerar relatório de predicados não canônicos.
8. Gerar relatório de conceitos usados mas ausentes do vocabulário.
9. Gerar relatório de decisões humanas sem texto literal.
10. Definir testes de competência antes de gerar ontologia.

## Decisões humanas literais ausentes

As seguintes decisões precisam ser registradas em arquivo próprio antes de qualquer continuação:

1. Especialista.
2. Goleiro versus Especialista.
3. Gol de Especialista.
4. Papel tático versus função situacional.
5. Papel tático versus posição espacial.
6. Conduta Antidesportiva.
7. Conduta Gravemente Antidesportiva.
8. Ação Particularmente Perigosa.
9. Gol Criativo.
10. Gol Espetacular.
11. Chance Clara de Gol.
12. Vantagem.
13. Perigo Climático.

## Conceitos centrais ausentes ou insuficientes

O vocabulário mínimo deve conter, antes da retomada:

- Papel_Tático;
- Papel_Regulamentar;
- Função_Situacional;
- Posição_Espacial;
- Especialista;
- Goleiro;
- Jogador_De_Linha;
- Autor_Do_Gol;
- Valor_Do_Gol;
- Fundamento_Da_Pontuação;
- Gol_De_Especialista;
- Gol_De_Goleiro;
- Gol_Criativo;
- Gol_Espetacular;
- Tiro_De_6_Metros;
- Inferência_Proibida;
- Teste_De_Competência.

## Próximo ponto único autorizado

A próxima ação autorizada é:

```text
Executar auditoria Python dos arquivos herdados.
```

A próxima ação não é:

```text
Continuar a ontologia.
Gerar novas regras.
Corrigir conceitos esportivos por inferência.
Revalidar tudo por conversa.
```

## Critério de aceite deste estado auditado

Este documento é aceito quando for usado como bloqueio formal contra qualquer agente que tente continuar a ontologia a partir de status antigos.

O próximo agente deve começar lendo este documento e obedecer ao seguinte comando:

```text
Não herdar validação anterior.
Não gerar ontologia.
Rodar primeiro a auditoria determinística.
```

## Veredito

O projeto não está perdido, mas a ontologia ainda não existe em estado confiável.

O material anterior deve ser tratado como corpus de extração e evidência de falhas do pipeline.

A retomada correta é: estado auditado, auditoria Python, decisões humanas literais, vocabulário canônico, fichas conceituais, testes de competência e somente depois ontologia.

---

## Atualização 2026-06-22 — pós-correção do script de auditoria

Esta seção **não substitui** o conteúdo acima — o corpo deste documento
(de 19/06) permanece como checkpoint histórico. Esta seção registra o que
mudou desde então, com granularidade por item, porque tratar tudo como
"resolvido" ou "nada resolvido" seria impreciso.

`audit_ontology_pipeline.py` foi corrigido para v2.0.0 (paths independentes
de cwd, fail-loud em arquivo ausente, predicado canônico priorizado sobre
candidato do objeto/sujeito, frases sem predicado marcadas explicitamente em
vez de receberem predicado inventado, `é_subclasse_de` reconhecido no
vocabulário, verificação de decisão humana por bloco implementada em
código). Os 4 testes em `test_audit_ontology_pipeline.py` passam. Detalhes
completos: `CHANGELOG`.

Status item a item desta página, à luz da correção:

- **"Bloqueios de continuidade" item 1** ("Criar decisão humana literal para
  o conceito Especialista") — **RESOLVIDO**. A decisão `DH-ESP-001` foi
  registrada e mesclada em `files/Decisões Humanas.md`.
- **"Bloqueios de continuidade" item 2** ("Inserir Especialista no
  vocabulário canônico") — **AINDA PENDENTE**. Evidência:
  `results_auditoria_python/03_missing_vocabulary_terms.csv` continua
  listando `Especialista,conceito_obrigatorio_minimo_ausente`. A decisão
  literal existir não implica o termo estar declarado em
  `files/Vocabulário e Taxonomia.md` — são gates distintos.
- **"Decisões humanas literais ausentes" item 1** ("Especialista") —
  **RESOLVIDO** pelo mesmo motivo do primeiro item acima. Os itens 2–13
  dessa lista permanecem pendentes (não afetados pela correção do script).
- Demais itens de "Bloqueios de continuidade" (3–10) e "Conceitos centrais
  ausentes" — **inalterados**; a correção do script não modificou conteúdo
  da ontologia, só a confiabilidade de como ele é medido.

Métricas atuais: ver `results_auditoria_python/07_blockers_report.md`
(gerado a cada execução, com timestamp e hash de cada input lido). Este
documento não reproduz números — fazê-lo manualmente já causou erro de
transcrição uma vez (ver `CHANGELOG`).

```yaml
auditoria_python:
  versao_atual: "2.0.0"
  status: "CORRIGIDA_TESTADA_REGENERADA"
  testes: "4/4 passando"
  metricas_atuais: "ver results_auditoria_python/07_blockers_report.md"
  status_ontologia: "AINDA_BLOQUEADA"
  bloqueio_resolvido:
    - "decisão humana literal para Especialista (DH-ESP-001)"
  bloqueio_ainda_pendente:
    - "Especialista ausente do vocabulário canônico declarado"
    - "demais itens de Bloqueios de continuidade (3-10) e Decisões humanas literais ausentes (2-13)"
```
