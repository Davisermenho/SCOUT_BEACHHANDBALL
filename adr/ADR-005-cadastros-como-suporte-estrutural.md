# ADR-005: Cadastros base como suporte estrutural

## Status

Aprovado

## Contexto

`PROBLEMA_FINAL.md` lista fluxos centrais do MVP, mas a implementacao precisa de cadastros base para que eles existam.

## Decisao

- cadastros de atletas, competicoes e adversarios sao suporte estrutural obrigatorio;
- eles nao configuram ampliacao indevida de objetivo de produto.

## Consequencias

- a IA nao deve tratar esses cadastros como modulo de produto separado;
- a existencia deles serve para viabilizar jogo, treino, historico e scout.
