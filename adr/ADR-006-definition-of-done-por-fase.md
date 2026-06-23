# ADR-006: Definition of Done por fase

## Status

Aprovado

## Contexto

Implementacao assistida por IA precisa de gates verificaveis, nao de declaracoes genericas de conclusao.

## Decisao

Nenhuma fase pode ser concluida apenas com a afirmacao `implementado`.

Toda fase exige evidencia verificavel compativel com sua natureza.

Para Fase 0:

- aprovador humano nomeado;
- data;
- versao congelada da ontologia e do vocabulario;
- identificacao exata das revisoes aprovadas, preferencialmente por `sha256`;
- identificacao exata dos ADRs normativos aprovados;
- todos os ADRs normativos usados no gate devem possuir revisao congelada por hash, incluindo ADR-004 e ADR-005 quando fizerem parte da cadeia aprovada;
- bloqueios remanescentes explicitados;
- artefato formal de aprovacao ou bloqueio.

Para Fases 1 a 6:

- banco criado ou migracao aplicada;
- teste passando;
- dado persistido;
- aplicacao fechada e reaberta;
- dado consultado novamente;
- fluxo provado com exemplo real ou fixture verificavel.

Distribuicao obrigatoria entre fases:

- Fase 1 fecha fundacao estrutural comum;
- Fase 2 fecha invariantes, transacoes e rastreabilidade minima de treino e jogo;
- Fase 3 fecha invariantes e taxonomia do scout.

## Consequencias

- a implementacao so avanca com prova executavel;
- a Fase 0 nao pode ser dada como concluida so por existir documento;
- isso reduz risco de tela bonita sem persistencia real;
- isso reduz risco de backend parcial sem validade operacional.
