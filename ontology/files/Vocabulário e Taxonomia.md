---
doc_type: source_primary
derived: false
should_be_derived: false
status: current
governed_by: null
generated_by: null
audited_by: auditoria_python_ontologia/audit_ontology_pipeline.py
last_audit_report: results_auditoria_python/07_blockers_report.md
superseded_by: null
last_reviewed: "2026-06-22"
---

Vocabulário e Taxonomia
Estado
A Fase 0 possui_status VALIDADA_POR_DECISÃO_HUMANA.
A Decisão Humana FASE0-2026-06-18 aprova o Pacote Recomendado da Fase 0.

Papéis Funcionais
Atleta é_um Participante.
Goleiro é_um Papel Funcional.
Jogador de Linha é_um Papel Funcional.
Uma Atribuição de Papel Funcional possui exatamente um Atleta [entidade].
Uma Atribuição de Papel Funcional possui exatamente um Papel Funcional [enumeração].
Uma Atribuição de Papel Funcional possui exatamente uma Fase da Partida [entidade].
Se uma Atribuição de Papel Funcional atribui Goleiro a um Atleta, então a Atribuição de Papel Funcional não atribui Jogador de Linha ao mesmo Atleta no mesmo instante.
Se uma Atribuição de Papel Funcional atribui Jogador de Linha a um Atleta, então a Atribuição de Papel Funcional não atribui Goleiro ao mesmo Atleta no mesmo instante.

Distinção entre Equipamento e Evento
Baliza é_um Equipamento de Jogo.
Gol é_um Evento de Pontuação.
Baliza é_disjunto_de Gol.

Modalidades Normativas
OBRIGATÓRIO é_um Valor de Modalidade Normativa.
PERMITIDO é_um Valor de Modalidade Normativa.
PROIBIDO é_um Valor de Modalidade Normativa.
RECOMENDADO é_um Valor de Modalidade Normativa.
AGUARDANDO_AVALIAÇÃO_HUMANA é_um Valor de Estado Semântico.

Tipos de Dados
número_inteiro é_um Tipo de Dado.
número_decimal é_um Tipo de Dado.
texto é_um Tipo de Dado.
data é_um Tipo de Dado.
enumeração é_um Tipo de Dado.
booleano é_um Tipo de Dado.


