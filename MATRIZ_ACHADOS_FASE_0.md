# Matriz de Achados da Fase 0

## Finalidade

Esta matriz registra o destino dos achados acumulados ao longo das revisoes.

Formato:

`Achado original | Status atual | Decisao | Acao necessaria | Documento afetado`

## Matriz

| Achado original | Status atual | Decisao | Acao necessaria | Documento afetado |
|---|---|---|---|---|
| Video parecia obrigatorio no MVP | Corrigido | Video e apoio opcional | Manter assim na implementacao | MVP.md, ESPECIFICACAO_IMPLEMENTACAO_MVP.md |
| Faltava governanca do SSOT | Corrigido | MVP segue PROBLEMA_FINAL | Manter regra de alinhamento | MVP.md |
| Fontes legadas estavam mal cobertas | Parcialmente corrigido | Conversao manual/controlada no MVP | Provar em fluxo real | MVP.md, ESPECIFICACAO_IMPLEMENTACAO_MVP.md |
| Historico coletivo era fraco | Melhorado | Consolidado coletivo minimo definido | Provar com fixture ou piloto | MVP.md, ESPECIFICACAO_IMPLEMENTACAO_MVP.md, ONTOLOGIA |
| Presenca de jogo conflitando com attendance | Corrigido | `attendance` so treino, `match_roster` so jogo | Nao permitir modelo antigo no codigo | MVP.md, ESPECIFICACAO_IMPLEMENTACAO_MVP.md |
| Scout individual podia escapar do elenco | Corrigido no papel | Trigger SQLite como decisao oficial | Implementar e testar | MVP.md, ESPECIFICACAO_IMPLEMENTACAO_MVP.md, ADR-001 |
| Backup SQLite/WAL ambiguo | Parcialmente corrigido | Usar mecanismo seguro compativel com WAL | Fechar implementacao e provar restauracao | ESPECIFICACAO_IMPLEMENTACAO_MVP.md, ADR-002 |
| Resultado de jogo ambiguo para handebol de areia | Parcialmente corrigido | Resultado canonico + sets + shoot-out | Fechar invariantes de coerencia | ONTOLOGIA, ESPECIFICACAO_IMPLEMENTACAO_MVP.md, ADR-003 |
| Cadastros pareciam escopo extra | Corrigido | Cadastros sao suporte estrutural | Nao vender como funcionalidade separada | MVP.md, ADR-005 |
| Falta de prova executavel por fase | Corrigido no plano | Toda fase exige evidencia real | Seguir como gate | ESPECIFICACAO_IMPLEMENTACAO_MVP.md, ADR-006 |
| Ontologia nao auditada | Em aberto | Ontologia e bloqueador de fase | Aprovar ontologia antes de codar scout | ONTOLOGIA, ADR-004 |
| Reducao de carga operacional estava subjetiva | Parcialmente corrigido | Medir jogo piloto | Registrar tempo e retrabalho | MVP.md, ESPECIFICACAO_IMPLEMENTACAO_MVP.md |
| Scout individual podia aceitar atleta ausente ou `did_not_play` | Corrigido no papel | Scout individual exige atleta `played` | Implementar trigger e testar | ONTOLOGIA, MVP.md, ESPECIFICACAO_IMPLEMENTACAO_MVP.md, ADR-001 |
| Resultado de jogo nao tinha invariantes executaveis suficientes | Parcialmente corrigido | Proteger `draft/finalized`, sets e shoot-out por trigger e checks | Implementar e testar coerencia completa | MVP.md, ESPECIFICACAO_IMPLEMENTACAO_MVP.md, ADR-003 |
| Golden Goal nao estava representado de forma normativa | Corrigido no papel | Registrar `set_decision_type` e placar oficial final do set | Implementar e testar casos positivos e negativos | ONTOLOGIA, MVP.md, ESPECIFICACAO_IMPLEMENTACAO_MVP.md, ADR-003 |
| Jogo incompleto podia aparecer como consolidado | Corrigido no papel | Introduzir `completion_status` | Implementar filtro padrao em historicos e relatorios | MVP.md, ESPECIFICACAO_IMPLEMENTACAO_MVP.md, ADR-003 |
| Vocabulario do scout nao tinha aprovacao formal registrada | Corrigido no processo | Exigir aprovacao humana registrada | Preencher artefato de aprovacao da Fase 0 | ONTOLOGIA, APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md, ADR-006 |
| `event_category` podia recriar texto livre estrutural | Corrigido no papel | `event_category` fica `NULL` no MVP inicial | Nao expor texto livre na implementacao inicial | ONTOLOGIA, MVP.md, ESPECIFICACAO_IMPLEMENTACAO_MVP.md |
| Taxonomia misturava tecnica e funcao da atleta | Corrigido no papel | Reduzir vocabulario inicial a classificacao primaria unica | Validar com aprovador humano | ONTOLOGIA, MVP.md, ESPECIFICACAO_IMPLEMENTACAO_MVP.md, APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md |
| `collective_note` conflitava com separacao entre fato e interpretacao | Corrigido no papel | Observacao coletiva sai de `scout_event_types` e fica em `notes` | Nao contar observacao como scout comparavel | ONTOLOGIA, MVP.md, ESPECIFICACAO_IMPLEMENTACAO_MVP.md |
| `role_scope` nao era aplicavel no modelo atual | Corrigido no papel | Introduzir `match_role_assignments` por fase e validar goleira por contexto | Implementar e testar `save_goalkeeper` por fase | MVP.md, ESPECIFICACAO_IMPLEMENTACAO_MVP.md, ADR-001 |
| Funcao de goleira variava no mesmo jogo e o modelo fixo do elenco era incorreto | Corrigido no papel | Remover `match_role` fixo de `match_roster` | Implementar atribuicoes funcionais por fase e `match_phase` no scout | ONTOLOGIA, MVP.md, ESPECIFICACAO_IMPLEMENTACAO_MVP.md, APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md |
| Atribuicao funcional podia ser gravada para atleta fora do elenco | Corrigido no papel | Exigir pertencimento estrutural e `present` + `played` | Implementar trigger e testar cenarios negativos | MVP.md, ESPECIFICACAO_IMPLEMENTACAO_MVP.md, ADR-001 |
| Significado de atribuicao funcional podia ser lido como planejamento | Corrigido no papel | Tratar atribuicao como fato ocorrido na fase | Implementar e validar contra piloto real | ONTOLOGIA, MVP.md, ESPECIFICACAO_IMPLEMENTACAO_MVP.md, ADR-001 |
| Validacao de fase estava protegida apenas em uma direcao | Corrigido no papel | Fechar `phase_scope` nos dois sentidos | Implementar e testar fase regular em shoot-out e shoot-out sem desempate | ONTOLOGIA, MVP.md, ESPECIFICACAO_IMPLEMENTACAO_MVP.md |
| Shoot-out podia aceitar evento ou atribuicao sem desempate real | Corrigido no papel | Exigir shoot-out real para `match_phase = shootout` | Implementar e testar em scout e atribuicoes | ONTOLOGIA, MVP.md, ESPECIFICACAO_IMPLEMENTACAO_MVP.md, ADR-003 |
| Jogo finalizado podia degradar depois por edicoes | Corrigido no papel | Bloquear mutacao estrutural fora de reabertura controlada | Implementar triggers e testes negativos | ESPECIFICACAO_IMPLEMENTACAO_MVP.md, PLANO_EXECUCAO_IA_POR_FASES.md, ADR-003 |
| Faltava contrato transacional para finalizacao e reabertura | Corrigido no papel | Exigir transacao atomica com rollback integral | Implementar e testar falha intermediaria | ESPECIFICACAO_IMPLEMENTACAO_MVP.md, PLANO_EXECUCAO_IA_POR_FASES.md |
| Fase 1 carregava invariantes de jogo e scout indevidamente | Corrigido no papel | Reorganizar gates entre Fases 1, 2 e 3 | Seguir novo particionamento | MVP.md, ESPECIFICACAO_IMPLEMENTACAO_MVP.md, PLANO_EXECUCAO_IA_POR_FASES.md |
| Aprovacao da Fase 0 nao congelava revisoes exatas | Corrigido no processo | Registrar `sha256` dos documentos aprovados | Preencher hashes no artefato de aprovacao | APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md, ADR-006 |
