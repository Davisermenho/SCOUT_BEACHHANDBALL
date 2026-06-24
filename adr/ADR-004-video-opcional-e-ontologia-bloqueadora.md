# ADR-004: Video opcional e ontologia bloqueadora

## Status

Aprovado

## Contexto

O projeto nao e um sistema de IA de video.

Ao mesmo tempo, a semantica do scout depende da ontologia do handebol de areia.

## Decisao

- video permanece apoio opcional do MVP;
- a ontologia do scout continua prerequisito formal da semantica do dominio;
- nenhuma implementacao de scout pode avancar sem baseline ontologico validado
  e sem obedecer ao gate humano vigente de Fase 0.

## Consequencias

- rota de midia local existe apenas como suporte tecnico;
- video nao pode virar modulo central de produto;
- a ontologia deixa de ser referencia opcional e vira prerequisito formal.
- a existencia tecnica do baseline ontologico nao substitui a ratificacao
  humana do freeze documental.

## Interpretacao operacional atual

Em `2026-06-23`, o repositorio ja possui baseline tecnico minimo em
`ontology/owl/`, com artefato `.ttl` validado por `rdflib` e `SHACL`.

Portanto, o bloqueio remanescente deixa de ser "ausencia de ontologia" e passa
a ser:

- ratificacao humana explicita do baseline congelado vigente;
- obediencia a fase/autorizacao operacional definidas nos artefatos de
  aprovacao e ordem de execucao.
