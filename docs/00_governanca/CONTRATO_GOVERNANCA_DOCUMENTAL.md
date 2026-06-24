---
doc_id: contrato-governanca-documental
doc_type: contract
status: proposed
phase_scope:
  - cross_phase
authority_level: proposed
owned_by: repo_governance
canonical_path: /docs/00_governanca/CONTRATO_GOVERNANCA_DOCUMENTAL.md
supersedes: []
superseded_by: null
must_read_before_implementation: false
implementation_ready: false
last_reviewed: "2026-06-24"
---

# CONTRATO_GOVERNANCA_DOCUMENTAL

## 1. Finalidade

Este contrato estabelece a regra canonica unica para organizar a documentacao do repositorio.

Ele existe para:

- eliminar ambiguidade sobre onde cada documento deve viver;
- tornar obrigatorio um schema unico de metadados;
- definir a cadeia de autoridade documental;
- impedir que documentos historicos parecam ativos;
- bloquear implementacao de produto sem contrato adequado;
- servir como baseline normativo para a validacao mecanica da Etapa 4.

## 2. Insumos consolidados

Este contrato consolida as decisoes fechadas em:

- `docs/00_governanca/PLANO_CONTRATO_ORGANIZACAO_DOCUMENTAL.md`
- `docs/00_governanca/MAPA_DOCUMENTAL.md`
- `docs/00_governanca/ESQUEMA_METADADOS_DOCUMENTAIS.md`

Em caso de divergencia futura:

1. este contrato
2. `ESQUEMA_METADADOS_DOCUMENTAIS.md`
3. `MAPA_DOCUMENTAL.md`
4. `PLANO_CONTRATO_ORGANIZACAO_DOCUMENTAL.md`

## 3. Escopo

Este contrato governa:

- todos os documentos ativos em `docs/`;
- todos os documentos inventariados em `MAPA_DOCUMENTAL.md`;
- todos os documentos que forem migrados para a arvore canonica `docs/**`.

Este contrato ainda nao encerra automaticamente a adaptacao controlada de:

- subsistema `ontology/`;
- derivados de fonte externa ainda fora da arvore final;
- legados inventariados e ainda nao migrados para `docs/`.

## 4. Estrutura documental oficial

A estrutura documental oficial do repositorio e:

```text
docs/
  00_governanca/
  01_contexto/
  02_produto/
  03_ontologia/
  04_implementacao/
  05_fases/
  06_adrs/
  07_revisoes_e_auditorias/
  08_historico_deprecado/
  09_fontes/
```

Regras obrigatorias de localizacao:

- contratos ativos devem viver em `docs/`;
- aprovacoes ativas devem viver em `docs/`;
- revisoes, ADRs, inventarios e historicos governados devem viver em `docs/`, salvo excecoes explicitamente registradas como adaptacao controlada;
- contratos ativos fora de `docs/` sao proibidos;
- novos documentos governados nao podem nascer na raiz do repositorio;
- a raiz do repositorio fica reservada para codigo, configuracao tecnica e arquivos ainda nao migrados, desde que estejam explicitamente inventariados.

## 5. Cadeia de autoridade documental

Niveis validos de autoridade:

- `ssot`: fonte primaria de verdade documental;
- `canonical`: referencia principal de uma area ou fase;
- `operational`: instrucao executavel ativa;
- `supporting`: suporte, gate, indice, ADR, revisao ou handoff;
- `historical`: historico sem papel operacional ativo;
- `proposed`: documento ainda nao ativado.

Resolucao de conflitos:

1. `ssot` vence qualquer outro nivel.
2. `canonical` vence `operational`, `supporting` e `historical`.
3. `operational` vence `supporting` e `historical` dentro do mesmo escopo.
4. `historical` nunca vence documento ativo.
5. `proposed` nunca libera implementacao nem vence documento vigente.

Se dois documentos ativos do mesmo escopo tiverem o mesmo nivel de autoridade e entrarem em conflito:

- a execucao deve parar;
- o conflito deve ser resolvido por reconciliacao documental;
- nenhum agente pode escolher por inferencia livre.

## 6. Regras obrigatorias de metadados

Todo documento governado por este contrato deve obedecer ao schema definido em:

- `docs/00_governanca/ESQUEMA_METADADOS_DOCUMENTAIS.md`

Frontmatter minimo obrigatorio:

```yaml
---
doc_id: identificador-unico
doc_type: contract|approval|review|adr|inventory|plan|archive|handoff
status: draft|proposed|approved|current|deprecated|archived
phase_scope:
  - phase_0|phase_1|phase_2|phase_3|cross_phase
authority_level: ssot|canonical|operational|supporting|historical|proposed
owned_by: nome-do-contrato-ou-governanca
canonical_path: /docs/caminho/do/arquivo.md
supersedes:
  - /docs/caminho/arquivo_antigo.md
superseded_by: null
must_read_before_implementation: true|false
implementation_ready: true|false
last_reviewed: "YYYY-MM-DD"
---
```

Regras obrigatorias:

- ausencia de qualquer campo obrigatorio invalida o documento para fins de governanca ativa;
- `canonical_path` deve coincidir com o caminho real no conjunto governado principal;
- `MAPA_DOCUMENTAL.md` deve refletir o frontmatter vigente;
- divergencia entre frontmatter e mapa e erro documental.

## 7. Ciclo de vida documental

Estados validos:

- `draft`
- `proposed`
- `approved`
- `current`
- `deprecated`
- `archived`

Transicoes validas:

1. `draft -> proposed`
2. `proposed -> approved`
3. `proposed -> archived`
4. `approved -> current`
5. `approved -> archived`
6. `current -> deprecated`
7. `current -> archived`
8. `deprecated -> archived`

Transicoes proibidas:

- `draft -> current`
- `deprecated -> current`
- qualquer depreciacao sem sucessor existente no mesmo changeset quando houver substituicao;
- qualquer ativacao de documento `current` que deixe predecessor ainda parecendo ativo por acidente.

Autoridade de transicao:

- `draft -> proposed`: agente executor ou mantenedor humano;
- `proposed -> approved`: mantenedor humano;
- `approved -> current`: mantenedor humano;
- `current -> deprecated`: mantenedor humano no mesmo changeset que cria ou ativa o sucessor;
- `deprecated -> archived`: mantenedor humano ou agente executor com rastreabilidade preservada.

## 8. Regras de depreciacao, arquivamento e rastreabilidade

Quando um documento substituir outro:

1. o sucessor deve existir antes do predecessor ser marcado como `deprecated`;
2. sucessor e predecessor devem ser atualizados no mesmo changeset;
3. `superseded_by` do predecessor deve apontar para sucessor existente;
4. `supersedes` do sucessor deve listar explicitamente os predecessores absorvidos;
5. nenhum documento historico pode continuar com aparencia de ativo.

Quando um documento for apenas historico:

- deve usar `status: archived` ou `status: deprecated`, conforme o caso;
- deve usar `authority_level: historical`;
- nao pode liberar implementacao nem servir como referencia ativa sem ser explicitamente reabilitado por novo documento vigente.

## 9. Politica de links e caminhos canonicos

Regras obrigatorias:

- `canonical_path` deve bater com o caminho real do arquivo no conjunto governado;
- links internos devem ser atualizados no mesmo changeset que mover ou depreciar um documento;
- o mapa documental e derivado dos arquivos reais, nao a fonte primaria de verdade;
- divergencia entre `MAPA_DOCUMENTAL.md` e os metadados reais deve ser tratada como erro;
- nenhum `superseded_by` pode apontar para arquivo inexistente no commit final.

## 10. Regra de bloqueio para implementacao de produto

Um agente so pode implementar produto quando o contrato ativo do escopo correspondente atender simultaneamente a:

- `status: current`
- `must_read_before_implementation: true`
- `implementation_ready: true`

Checklist obrigatorio antes de implementar produto:

1. existe contrato canonico unico para a fase ou escopo;
2. o escopo esta fechado;
3. o fora de escopo esta explicito;
4. a sequencia de execucao esta definida;
5. as evidencias de conclusao estao definidas;
6. os bloqueios documentais estao zerados;
7. nao existe conflito com contrato anterior ainda marcado como ativo;
8. a validacao documental automatica passou, quando ja existir.

Se qualquer item falhar:

- a implementacao deve parar;
- o bloqueio deve ser reportado como problema documental;
- a correcao deve ocorrer no contrato, nao por improvisacao no codigo.

## 11. Escopo inicial de aplicacao

Entram imediatamente no modelo governado principal:

- `docs/00_governanca/*.md`
- futuros documentos migrados para `docs/01_*` ate `docs/09_*`
- contratos, aprovacoes, revisoes, ADRs, inventarios e historicos listados em `MAPA_DOCUMENTAL.md` para migracao principal

Ficam em adaptacao controlada:

- subsistema `ontology/`
- derivados de fonte externa ainda fora da arvore final
- legados ainda fora de `docs/`, desde que inventariados no `MAPA_DOCUMENTAL.md`

Regra:

- nenhum item em adaptacao controlada pode ficar invisivel; ele deve estar explicitamente inventariado e classificado.

## 12. Taxonomia documental do repositorio

Para fins de governanca, o repositorio usa esta taxonomia:

- contratos
- aprovacoes
- ADRs
- revisoes e auditorias
- inventarios
- planos bootstrap
- historicos arquivados
- fontes e derivados documentais
- subsistema especializado `ontology/`

Essa taxonomia deve permanecer coerente com `MAPA_DOCUMENTAL.md`.

## 13. Integracao com o `MAPA_DOCUMENTAL.md`

O `MAPA_DOCUMENTAL.md`:

- e obrigatorio como indice derivado do estado real;
- deve ser atualizado sempre que documento governado for criado, movido, depreciado ou arquivado;
- nao substitui o frontmatter dos documentos;
- falha quando divergir do estado real do conjunto governado.

## 14. Integracao com validacao mecanica

Este contrato e a base normativa da Etapa 4.

O futuro enforcement mecanico deve validar, no minimo:

- campos obrigatorios do frontmatter;
- enums validos;
- coerencia entre `status`, `authority_level`, `must_read_before_implementation` e `implementation_ready`;
- coerencia de `phase_scope`;
- coerencia entre `canonical_path` e caminho real;
- existencia de sucessores referenciados em `superseded_by`;
- divergencia entre `MAPA_DOCUMENTAL.md` e o frontmatter real;
- existencia de contrato ativo fora de `docs/` no conjunto governado principal.

## 15. Definicao de pronto deste contrato

Este contrato deve ser considerado pronto para aprovacao quando:

1. consolidar sem conflito as decisoes do plano, do mapa e do schema;
2. declarar onde documentos ativos podem e nao podem ficar;
3. formalizar o uso obrigatorio do schema de metadados;
4. definir a cadeia de autoridade documental;
5. definir a maquina de estados documental;
6. definir as regras de depreciacao, arquivamento, `supersedes` e `superseded_by`;
7. formalizar a regra de leitura obrigatoria antes de implementacao;
8. declarar que contratos ativos fora de `docs/` sao proibidos;
9. formalizar a relacao normativa com `MAPA_DOCUMENTAL.md`;
10. delimitar o escopo imediato e a adaptacao controlada;
11. ser claro o suficiente para servir de base ao enforcement mecanico.

## 16. Criterios de aceite

Este contrato so deve ser considerado aceito quando:

1. existir uma regra canonica unica para organizar toda a documentacao do repo;
2. deixar de existir ambiguidade estrutural sobre localizacao, metadados, autoridade, depreciacao e leitura obrigatoria;
3. qualquer agente conseguir identificar, sem inferencia livre, se um documento e ativo, historico ou depreciado;
4. a organizacao documental do repo passar a ter um unico baseline normativo vigente.

## 17. Entrada em vigor

Enquanto este arquivo estiver em `status: proposed`, ele ainda nao substitui formalmente o baseline bootstrap.

Quando este contrato:

- receber aprovacao humana registrada; e
- passar para `status: current`

ele passa a ser a regra vigente de governanca documental do repositorio.

Nesse mesmo changeset:

- `PLANO_CONTRATO_ORGANIZACAO_DOCUMENTAL.md` deve apontar `superseded_by` para este contrato;
- o plano bootstrap deve caminhar para `archived` quando sua funcao estiver absorvida;
- `MAPA_DOCUMENTAL.md` e `ESQUEMA_METADADOS_DOCUMENTAIS.md` passam a operar como artefatos derivados e de suporte sob este contrato.
