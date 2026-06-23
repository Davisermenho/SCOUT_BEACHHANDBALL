---
doc_type: scoping_document
id: ONTOLOGY-OWL-001-SCOPE
status: ONTOLOGY_OWL_001_ESCOPO_CRIADO_AGUARDANDO_VALIDACAO
gerado_em: "2026-06-23"
nao_e_validacao_total: true
---

# ONTOLOGY-OWL-001 — Escopo do MVP OWL/Protégé

## Status

`ONTOLOGY_OWL_001_ESCOPO_CRIADO_AGUARDANDO_VALIDACAO`

Este documento define apenas o escopo documental do MVP OWL/Protégé para a
ontologia do handebol de areia. Ele **não** gera ontologia, **não** cria
arquivo `.owl`, `.ttl` ou `.rdf`, **não** cria classes OWL, **não** cria
propriedades OWL e **não** autoriza reasoner nesta etapa.

## Pré-condição confirmada

O checkpoint anterior encontra-se fechado com:

- `CHECKPOINT_PONTUACAO_001_MODELO_MINIMO_VALIDADO_COM_LIMITES`
- `HANDOFF.md` apontando `ONTOLOGY-OWL-001-SCOPING` como próximo ponto
  exato antes desta abertura

## Objetivo desta etapa

- definir o IRI base documental do MVP;
- definir os prefixos mínimos de trabalho;
- definir o formato-alvo preferencial para futura edição no Protégé;
- delimitar módulos incluídos e módulos excluídos;
- listar classes autorizadas e classes bloqueadas;
- listar object properties autorizadas;
- listar data properties autorizadas;
- listar anotações obrigatórias;
- fixar critérios mínimos para abertura posterior no Protégé;
- fixar critérios mínimos para eventual uso futuro de reasoner.

## IRI base documental proposta

- `https://github.com/Davisermenho/SCOUT_BEACHHANDBALL/ontology/mvp#`

Esta IRI base é apenas uma proposta documental de namespace para o MVP.
Ela não implica publicação dereferenciável, endpoint, catálogo OWL, nem
compromisso de hosting externo nesta etapa.

## Prefixos mínimos propostos

- `hbp:` -> `https://github.com/Davisermenho/SCOUT_BEACHHANDBALL/ontology/mvp#`
- `rdf:` -> `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
- `rdfs:` -> `http://www.w3.org/2000/01/rdf-schema#`
- `owl:` -> `http://www.w3.org/2002/07/owl#`
- `xsd:` -> `http://www.w3.org/2001/XMLSchema#`
- `dcterms:` -> `http://purl.org/dc/terms/`

## Formato-alvo do MVP

- formato canônico proposto para edição versionável: `.ttl`
- `.owl` fica bloqueado como artefato de geração nesta etapa
- `.rdf` fica bloqueado como artefato de geração nesta etapa

O formato `.ttl` é escopado como formato textual preferencial para futuro
uso no Protégé por ser mais auditável em Git. Esta etapa não cria o
arquivo.

## Módulos incluídos no escopo do MVP

- módulo estrutural das quatro dimensões validadas:
  - `Papel_Tático`
  - `Papel_Regulamentar`
  - `Função_Situacional`
  - `Posição_Espacial`
- módulo mínimo de papéis já sustentados por decisão humana auditada:
  - `Especialista`
  - `Goleiro`
- módulo mínimo de metadados e rastreabilidade documental

## Módulos excluídos neste escopo

- módulo de pontuação como ontologia
- módulo de `Gol`
- módulo de `Pontuação`
- módulo de `Gol_Espetacular`
- módulo de `Gol_de_Giro`
- módulo de `Gol_Aereo`
- módulo de `Gol criativo`
- reprocessamento completo de `Regras 1–18`
- reprocessamento completo de `Apêndices`
- taxonomia geral
- ontologia principal completa
- configuração de reasoner

## Classes autorizadas para futura modelagem mínima

- `Papel_Tatico`
- `Papel_Regulamentar`
- `Funcao_Situacional`
- `Posicao_Espacial`
- `Especialista`
- `Goleiro`

Estas classes estão apenas autorizadas para escopo futuro de MVP. Elas não
estão sendo criadas em OWL nesta etapa.

## Classes bloqueadas neste escopo

- `Gol`
- `Pontuacao`
- `Gol_Espetacular`
- `Gol_de_Giro`
- `Gol_Aereo`
- `Gol_Criativo`
- `Jogador_De_Linha`
- `Autor_Do_Gol`
- `Fundamento_Da_Pontuacao`
- conceitos candidatos ainda sem consolidação semântica autorizada

## Object properties autorizadas para futura modelagem mínima

- `tem_papel_tatico`
- `tem_papel_regulamentar`
- `executa_funcao_situacional`
- `ocupa_posicao_espacial`

Estas properties estão apenas autorizadas como escopo semântico futuro. Não
estão sendo criadas em OWL nesta etapa.

## Data properties autorizadas para futura modelagem mínima

- nenhuma data property de domínio está autorizada neste escopo

Nesta fase, atributos de domínio como valor de gol permanecem fora da
camada OWL do MVP e seguem bloqueados como modelagem ontológica.

## Anotações obrigatórias para futura abertura no Protégé

- `rdfs:label`
- `rdfs:comment`
- `dcterms:source`
- `dcterms:created`
- `owl:versionInfo`

## Critérios mínimos para futura abertura no Protégé

- namespace documental fixado
- tabela de prefixos definida
- somente classes autorizadas no escopo
- somente object properties autorizadas no escopo
- nenhuma data property de domínio fora do escopo
- anotações obrigatórias definidas
- nenhum módulo bloqueado incluído
- nenhum arquivo `.owl`, `.ttl` ou `.rdf` gerado antes do próximo gate

## Critérios mínimos para future use de reasoner

- reasoner continua bloqueado neste scoping
- reasoner só pode ser considerado após modelagem mínima e validação
  própria
- inferências automáticas não podem substituir decisão humana registrada
- módulo de pontuação não pode entrar em reasoner antes de consolidação
  semântica própria

## Limites preservados

- não gerar ontologia
- não criar arquivo `.owl`
- não criar arquivo `.ttl`
- não criar arquivo `.rdf`
- não criar classes OWL
- não criar object properties OWL
- não criar data properties OWL
- não transformar documentação em regra executável
- não alterar as quatro fichas consolidadas
- não alterar testes existentes
- não alterar arquivos protegidos
- não marcar `VALIDADO_TOTAL`
- não marcar `CONSOLIDADO_VALIDO`

## Próximo gate recomendado

```yaml
proximo_ponto_exato:
  id: ONTOLOGY-OWL-001-SCOPING-VALIDATION
  tarefa: "Validar o escopo do MVP OWL/Protégé sem gerar ontologia, classes OWL, propriedades OWL ou reasoner."
```
