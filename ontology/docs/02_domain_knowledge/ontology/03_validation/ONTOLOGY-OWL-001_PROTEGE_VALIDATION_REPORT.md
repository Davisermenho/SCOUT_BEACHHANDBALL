---
doc_type: validation_report
tarefa_validada: ONTOLOGY-OWL-001-MVP-GENERATION
status_geral: ONTOLOGY_OWL_001_PROTEGE_VALIDATION_EXECUTADA_COM_BLOQUEIO_PARCIAL_DE_FERRAMENTAS
gerado_em: "2026-06-23"
nao_e_validacao_total: true
---

# Relatório de Validação Técnica — ONTOLOGY-OWL-001

## Status geral

`ONTOLOGY_OWL_001_PROTEGE_VALIDATION_EXECUTADA_COM_BLOQUEIO_PARCIAL_DE_FERRAMENTAS`

Este relatório cobre a validação técnica do arquivo
`ontology/owl/scout_beachhandball_mvp.ttl` com os recursos disponíveis no
ambiente atual.

## Arquivo validado

- `ontology/owl/scout_beachhandball_mvp.ttl`

## O que foi comprovado localmente

- o arquivo Turtle existe;
- o arquivo parseia sem erro de sintaxe com `rdflib`;
- o grafo contém `71` triplas antes de expansão;
- as classes esperadas existem:
  - `Papel_Tatico`
  - `Papel_Regulamentar`
  - `Funcao_Situacional`
  - `Posicao_Espacial`
  - `Especialista`
  - `Goleiro`
- as object properties esperadas existem:
  - `tem_papel_tatico`
  - `tem_papel_regulamentar`
  - `executa_funcao_situacional`
  - `ocupa_posicao_espacial`
- há `owl:disjointWith` entre `Especialista` e `Goleiro`;
- há `owl:AllDisjointClasses` para:
  - `Papel_Tatico`
  - `Papel_Regulamentar`
  - `Funcao_Situacional`
  - `Posicao_Espacial`
- há anotações de fonte (`dcterms:source`) no grafo;
- `Gol`, `Pontuacao`, `Gol_Criativo`, `Gol_Espetacular`,
  `Gol_de_Giro` e `Gol_Aereo` não aparecem como classes;
- a expansão local com `owlrl` executou sem erro;
- a checagem local com `pyshacl` retornou conformidade básica.

## Ambiente disponível

- `python3`: disponível
- `rdflib`: disponível
- `owlrl`: disponível
- `pyshacl`: disponível
- `java`: disponível

## Bloqueio parcial de ferramentas

Não foi possível comprovar localmente os critérios dependentes de
Protégé/Java porque:

- `protege` não está disponível no `PATH`;
- `robot`, `pellet`, `hermit`, `riot` e `rapper` não estão disponíveis no
  `PATH`;
- não foi encontrada instalação local utilizável de Protégé.

`Java` está disponível no ambiente atual, mas isso não foi suficiente para
substituir a ausência do Protégé Desktop e das ferramentas de reasoner/CLI
específicas no `PATH`.

## Critérios do DONE_PROTEGE_MVP_001

| # | Critério | Resultado | Evidência |
|---|---|---|---|
| 1 | Existe `ontology/owl/scout_beachhandball_mvp.ttl` | APROVADO | arquivo criado no workspace |
| 2 | O arquivo abre no Protégé sem erro de sintaxe | BLOQUEADO | Protégé indisponível no ambiente |
| 3 | As classes esperadas aparecem | APROVADO | `rdflib` encontrou as 6 classes esperadas |
| 4 | As object properties esperadas aparecem | APROVADO | `rdflib` encontrou as 4 properties esperadas |
| 5 | As anotações de fonte existem | APROVADO | `dcterms:source` presente (`17` triplas) |
| 6 | `Especialista` não é `Goleiro` | APROVADO | `owl:disjointWith` entre `Especialista` e `Goleiro` |
| 7 | `Goleiro` não é `Especialista` | APROVADO | mesma disjunção explícita |
| 8 | As quatro dimensões não foram fundidas | APROVADO | `owl:AllDisjointClasses` presente |
| 9 | Pontuação não reclassifica papel | APROVADO | nenhuma classe/propriedade de pontuação foi modelada |
| 10 | `Gol criativo` não virou classe | APROVADO | classe ausente no TTL |
| 11 | Reasoner roda sem inconsistência | BLOQUEADO | Protégé/reasoner DL não disponível no `PATH` |
| 12 | Não há classes insatisfatíveis | BLOQUEADO | requer reasoner DL/Protégé não disponível |
| 13 | O baseline `.ttl` foi commitado; este relatório específico ainda não | PARCIAL | commits `8e012ff`, `8f24ed0` e `278ffd9` já registram o baseline, mas este relatório segue não rastreado |

## Resultado objetivo

```yaml
criterios_aprovados: 9
criterios_bloqueados: 2
criterios_parciais: 1
status: ONTOLOGY_OWL_001_PROTEGE_VALIDATION_EXECUTADA_COM_BLOQUEIO_PARCIAL_DE_FERRAMENTAS
```

## Conclusão

O TTL MVP foi gerado corretamente e passou no preflight técnico local
disponível.

`DONE_PROTEGE_MVP_001` ainda não pode ser declarado neste ambiente, porque
os critérios dependentes de Protégé Desktop e reasoner DL específico não
puderam ser executados aqui.

O baseline técnico mínimo da ontologia já foi commitado anteriormente, mas
este relatório ainda não foi incorporado ao histórico Git do repositório.
