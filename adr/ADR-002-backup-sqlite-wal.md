# ADR-002: Backup seguro com SQLite em modo WAL

## Status

Aprovado

## Contexto

O projeto usa SQLite local com `journal_mode = WAL`.

Copiar apenas o arquivo `.db` de forma cega pode produzir backup incompleto.

## Decisao

Para o MVP, backup valido deve:

- usar mecanismo seguro compativel com SQLite/WAL;
- evitar copia cega do `.db` durante escrita aberta;
- provar restauracao integra apos backup.
- provar `PRAGMA integrity_check` e `PRAGMA foreign_key_check` apos restauracao;
- provar restauracao em diretorio limpo;
- falhar de modo controlado diante de backup invalido ou corrompido.

Decisao preferencial:

- usar mecanismo de backup proprio do SQLite ou rotina equivalente que garanta consistencia antes da gravacao em `backups/`.

## Consequencias

- qualquer backup sem prova de restauracao nao conta como valido;
- qualquer backup sem prova de integridade estrutural e referencial nao conta como valido;
- o criterio de preservacao de historico depende dessa prova.
