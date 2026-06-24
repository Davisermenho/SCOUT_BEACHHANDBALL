---
doc_id: plano-contrato-organizacao-documental
doc_type: plan
status: proposed
phase_scope:
  - cross_phase
authority_level: proposed
owned_by: repo_governance_bootstrap
canonical_path: /docs/00_governanca/PLANO_CONTRATO_ORGANIZACAO_DOCUMENTAL.md
supersedes: []
superseded_by: null
must_read_before_implementation: false
implementation_ready: false
last_reviewed: "2026-06-24"
---

# Plano para Elaboracao do Contrato de Organizacao Documental do Repositorio

## 1. Objetivo

Este plano define como reorganizar a documentacao do repositorio para que:

- nenhum contrato ativo fique perdido na raiz;
- toda documentacao ativa tenha metadados obrigatorios;
- o agente saiba exatamente qual contrato ler;
- a implementacao de produto so possa comecar quando o contrato da fase estiver completo;
- a Fase 0 passe a ter um contrato unico, completo e sem ambiguidade operacional;
- documentos antigos da Fase 0 sejam formalmente depreciados sem sumir da trilha historica;
- a governanca documental tenha enforcement mecanico, e nao apenas obediencia voluntaria.

## 2. Diagnostico do estado atual

Hoje o repositorio possui contratos, revisoes, aprovacoes e documentos historicos espalhados entre:

- raiz do repositorio;
- `adr/`;
- `docs/fontes/`;
- `ontology/docs/...`.

Problemas observados:

- a raiz concentra documentos normativos, revisoes e historicos sem classificacao unica;
- nao existe um indice mestre com protocolo de manutencao;
- nao existe bloco padrao de metadados no conjunto principal da raiz;
- o agente ainda precisa inferir se um arquivo e fonte de autoridade, historico ou revisao;
- a Fase 0 possui varios artefatos relevantes, mas nao um contrato unico operacional consolidado;
- nao existe validacao mecanica para impedir novos contratos ativos fora de `docs/`.

## 3. Principios do contrato documental

O contrato de governanca documental deve obedecer a estes principios:

1. Todo documento ativo deve morar em `docs/`, nunca na raiz.
2. Todo documento ativo deve declarar metadados padrao no topo.
3. Todo documento deve informar a fase de implementacao a que pertence.
4. Toda fase deve ter no maximo um contrato operacional canonico ativo.
5. Documentos substituidos nao podem continuar parecendo ativos.
6. O agente nao pode adivinhar cadeia de autoridade.
7. Implementacao de produto por IA so pode ocorrer quando houver contrato com escopo, sequencia, proibicoes, evidencias e criterio de parada completos.
8. Nenhum documento historico deve desaparecer; ele deve ser reclassificado e indexado.
9. Regras documentais criticas devem ter validacao automatizavel.

## 4. Estrutura alvo do repositorio documental

Arvore proposta:

```text
docs/
  00_governanca/
    README.md
    MAPA_DOCUMENTAL.md
    CONTRATO_GOVERNANCA_DOCUMENTAL.md
    ESQUEMA_METADADOS_DOCUMENTAIS.md
    REGRAS_DEPRECIACAO.md
  01_contexto/
    PROBLEMA_FINAL.md
  02_produto/
    MVP.md
  03_ontologia/
    ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md
    evidencias/
  04_implementacao/
    ESPECIFICACAO_IMPLEMENTACAO_MVP.md
  05_fases/
    PLANO_EXECUCAO_IA_POR_FASES.md
    fase_0/
      CONTRATO_UNICO_FASE_0.md
      APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md
      MATRIZ_ACHADOS_FASE_0.md
    fase_1/
      ORDEM_EXECUCAO_FASE_1.md
      FECHAMENTO_TECNICO_FASE_1_BASE_ESTRUTURAL.md
      MATRIZ_TESTES_FASE_1_BASE_ESTRUTURAL.md
  06_adrs/
    ADR-001-scout-roster-validation.md
    ADR-002-backup-sqlite-wal.md
    ...
  07_revisoes_e_auditorias/
    REVISAO_MVP_X_ESPECIFICACAO_IMPLEMENTACAO.md
    REVISAO_PROBLEMA_FINAL_X_MVP_v2.md
    REVISAO_COMPLETA_PROBLEMA_FINAL_X_MVP.md
    REVISAO_MODELAGEM_BANCO_X_FASE_1.md
  08_historico_deprecado/
    MODELAGEM_DO_BANCO_DE_DADOS.md
    rascunhos/
  09_fontes/
    ...
```

Regras estruturais:

- a raiz deve ficar reservada para codigo, configuracao tecnica e arquivos operacionais do projeto;
- contratos ativos, aprovacoes, revisoes e governanca devem sair da raiz;
- `docs/fontes/` deve ser migrado para `docs/09_fontes/` em etapa controlada;
- `ontology/docs/...` pode continuar existindo como subsistema especializado, desde que seja apontado pelo `MAPA_DOCUMENTAL.md` e subordinado ao contrato mestre do repo;
- a taxonomia dos ADRs fica decidida neste plano: ADRs canonicos do repo moram em `docs/06_adrs/`.

## 5. Schema obrigatorio de metadados

Todo documento dentro de `docs/` deve abrir com um bloco YAML padrao.

Schema minimo obrigatorio:

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

Campos normativos obrigatorios:

- `phase_scope`: identifica a fase de implementacao;
- `status`: impede que historico pareca contrato ativo;
- `authority_level`: impede conflito entre SSOT, contrato operacional e historico;
- `must_read_before_implementation`: indica leitura obrigatoria do agente antes de implementar produto;
- `implementation_ready`: proibe implementacao prematura;
- `supersedes` e `superseded_by`: mantem rastreabilidade de substituicao.

Regra de aplicacao:

- documentos `plan` com `authority_level: proposed` podem existir com `must_read_before_implementation: false` e `implementation_ready: false`;
- documentos `contract`, `approval` e `handoff` que governem implementacao devem usar `must_read_before_implementation: true`;
- apenas documentos ativos de implementacao podem usar `implementation_ready: true`.

Regra de `phase_scope`:

- `phase_scope` e sempre lista para manter schema uniforme;
- documentos `contract` ou `approval` com `status: current` e `authority_level: ssot|canonical|operational` devem declarar exatamente um escopo: uma fase explicita ou `cross_phase`;
- documentos `review`, `inventory`, `plan` e `handoff` podem declarar multiplas fases explicitas;
- para validacao de conflito, um documento ativo com mais de uma fase explicita conta simultaneamente em cada fase listada.

## 6. Maquina de estados e autoridade

Estados validos:

- `draft`: rascunho em elaboracao;
- `proposed`: proposta pronta para revisao humana;
- `approved`: aprovado, mas ainda nao assumido como ponto canonico ativo;
- `current`: contrato ou indice ativo e vigente;
- `deprecated`: substituido, mantido apenas por rastreabilidade;
- `archived`: historico sem uso operacional.

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

- pular de `draft` direto para `current`;
- sair de `deprecated` de volta para `current`;
- marcar documento como `current` sem documento predecessor devidamente reclassificado quando houver substituicao;
- marcar documento como `deprecated` antes de o sucessor existir no mesmo changeset.

Autoridade por transicao:

- `draft -> proposed`: agente executor ou mantenedor humano;
- `proposed -> approved`: mantenedor humano;
- `approved -> current`: mantenedor humano;
- `current -> deprecated`: mantenedor humano no mesmo changeset que cria ou ativa o sucessor;
- `deprecated -> archived`: mantenedor humano ou agente executor quando a rastreabilidade ja estiver preservada.

Regra de `authority_level`:

- documentos em `draft` ou `proposed` devem usar `authority_level: proposed`;
- documentos em `approved` permanecem com `authority_level: proposed` ate a ativacao formal, exceto `approval` que pode usar `supporting` quando aprovado mas ainda nao vigente;
- apenas documentos em `status: current` podem usar `ssot`, `canonical`, `operational` ou `supporting`;
- documentos `contract` em `status: current` devem usar `ssot`, `canonical` ou `operational`;
- documentos `plan` em `status: current` devem usar `supporting`;
- documentos `review`, `inventory`, `adr` e `handoff` em `status: current` devem usar `supporting`;
- documentos `archive` nao podem usar `status: current`;
- documentos em `deprecated` ou `archived` devem usar `authority_level: historical`.

SLA normativo:

- nenhum documento pode permanecer em `proposed` apos o inicio da etapa seguinte que depende dele;
- mudanca de estado e atualizacao de links, `MAPA_DOCUMENTAL.md` e frontmatter devem acontecer no mesmo changeset.

## 7. Regra de bootstrap

Este arquivo e um plano de bootstrap documental, nao um contrato de implementacao de produto.

Por isso:

- ele nao autoriza codigo de produto;
- ele autoriza apenas trabalho documental de governanca necessario para criar o contrato definitivo;
- a regra de bloqueio de implementacao da secao 10 nao se aplica a este plano para fins de inventario, schema e contrato de governanca;
- a partir do momento em que `CONTRATO_GOVERNANCA_DOCUMENTAL.md` tiver aprovacao humana registrada e estiver em `status: current`, este plano perde funcao normativa e entra em processo de arquivamento.

Escopo permitido sob este plano:

- inventariar documentos;
- definir schema;
- criar contrato de governanca documental;
- consolidar contrato unico da Fase 0;
- planejar enforcement mecanico.

Escopo proibido sob este plano:

- usar este arquivo para autorizar implementacao de produto;
- usar este arquivo para liberar fase de desenvolvimento;
- marcar qualquer fase de implementacao como `implementation_ready: true`.

## 8. Contrato unico da Fase 0

O plano determina a criacao de:

- `docs/05_fases/fase_0/CONTRATO_UNICO_FASE_0.md`

Finalidade deste contrato:

- consolidar em um unico ponto todas as definicoes necessarias para encerrar a Fase 0;
- remover duvida sobre o que e obrigatorio ler;
- impedir que a IA navegue por varios documentos tentando inferir o baseline correto;
- servir como unico contrato operacional da Fase 0.

Conteudo minimo obrigatorio do contrato unico:

1. objetivo da Fase 0;
2. cadeia de autoridade interna da Fase 0;
3. escopo incluido;
4. escopo proibido;
5. vocabulario canonico aprovado;
6. invariantes semanticos obrigatorios;
7. gates humanos e documentais;
8. evidencias exigidas;
9. criterio de conclusao;
10. criterio de liberacao para Fase 1;
11. anexos obrigatorios e hashes congelados;
12. lista explicita dos documentos depreciados pela consolidacao.

Regra central:

- apos a publicacao do `CONTRATO_UNICO_FASE_0.md`, nenhum outro documento da Fase 0 pode continuar com `authority_level: canonical` ou `operational`.

Protocolo de hashes congelados:

- algoritmo: `sha256`;
- geracao: `sha256sum`;
- verificacao: script dedicado versionado no repo;
- normalizacao: documentos Markdown entram no freeze com final de linha `LF`;
- enforcement minimo: incluir regra de normalizacao documental em `.gitattributes` antes do primeiro freeze documental automatizado.

## 9. Depreciacao, migracao e links

Politica de deprecacao:

1. o sucessor deve existir antes do predecessor ser marcado como `deprecated`;
2. sucessor e predecessor devem ser atualizados no mesmo changeset;
3. `superseded_by` nunca pode apontar para arquivo inexistente no commit final;
4. `supersedes` do sucessor deve listar explicitamente os predecessores absorvidos;
5. nenhum arquivo antigo deve ser apagado antes da validacao dos links.

Protocolo de migracao fisica:

1. criar destino com `canonical_path` final;
2. atualizar links internos com busca repo-wide;
3. executar validacao automatica de links e frontmatter;
4. reclassificar origem como `deprecated` ou mover para `08_historico_deprecado/`;
5. remover stubs temporarios apenas quando nao houver referencias restantes ao caminho antigo.

Protocolo de links:

- identificar referencias com `rg`;
- bloquear merge se houver `canonical_path` inconsistente ou link interno quebrado dentro do conjunto governado;
- `MAPA_DOCUMENTAL.md` e derivado dos arquivos reais, nao a fonte primaria de verdade;
- a fonte primaria de verdade e o frontmatter dos documentos canonicos.

Protocolo do `MAPA_DOCUMENTAL.md`:

- deve ser atualizado no mesmo changeset em que documento for criado, movido, depreciado ou arquivado;
- o responsavel pela mudanca no documento e tambem responsavel pelo mapa;
- divergencia entre mapa e frontmatter faz a validacao falhar;
- revisao minima: a cada PR ou changeset que toque `docs/`.

## 10. Regra de bloqueio para implementacao de produto por IA

O contrato documental definitivo deve impor a seguinte regra:

- o agente so pode implementar produto quando o contrato ativo da fase estiver com `status: current`, `must_read_before_implementation: true` e `implementation_ready: true`.

Checklist obrigatorio antes de codificar produto:

1. existe contrato canonico unico para a fase;
2. o escopo da fase esta fechado;
3. o fora de escopo esta explicito;
4. a sequencia de execucao esta definida;
5. as evidencias de conclusao estao definidas;
6. os bloqueios documentais estao zerados;
7. nao existe conflito com contrato anterior ainda marcado como ativo;
8. a validacao documental automatica passou.

Se qualquer item falhar:

- a implementacao deve parar;
- o agente deve reportar o bloqueio documental;
- a correcao deve acontecer no contrato, nao no codigo.

## 11. Enforcement mecanico minimo obrigatorio

O contrato de governanca documental deve nascer junto com estes mecanismos:

1. `scripts/validate_document_governance.py`
2. workflow CI para validar frontmatter, estados, caminhos canonicos e divergencia do `MAPA_DOCUMENTAL.md`
3. verificacao de links internos no conjunto governado
4. regra de normalizacao documental em `.gitattributes`

Sistema minimo de CI:

- como o repositorio usa `origin` em GitHub e ainda nao possui `.github/`, a primeira implementacao padrao de CI para esta governanca deve ser GitHub Actions;
- o workflow minimo esperado e `.github/workflows/validate-document-governance.yml`;
- outro sistema de CI so pode substituir GitHub Actions se o contrato definitivo o nomear explicitamente no mesmo changeset;
- enquanto o workflow nao existir, a execucao local do validador continua obrigatoria, mas nao substitui a Etapa 4.

Escopo minimo do validador:

- rejeitar `doc_type` fora do schema;
- rejeitar ausencia de campos obrigatorios;
- rejeitar `superseded_by` apontando para arquivo inexistente;
- rejeitar mais de um contrato `current` para a mesma fase e mesma categoria operacional;
- rejeitar contrato ativo fora de `docs/` no conjunto governado;
- rejeitar divergencia entre `canonical_path` e caminho real do arquivo;
- rejeitar `status` fora da maquina de estados;
- rejeitar `MAPA_DOCUMENTAL.md` desatualizado em relacao ao frontmatter.

Definition of done do enforcement:

- a validacao roda localmente;
- a validacao roda em CI;
- um changeset invalido falha antes de ser tratado como baseline governado.

## 12. Mapa de migracao dos documentos atuais

Realocacao proposta dos arquivos principais:

- `PROBLEMA_FINAL.md` -> `docs/01_contexto/PROBLEMA_FINAL.md`
- `MVP.md` -> `docs/02_produto/MVP.md`
- `ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md` -> `docs/03_ontologia/ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md`
- `ESPECIFICACAO_IMPLEMENTACAO_MVP.md` -> `docs/04_implementacao/ESPECIFICACAO_IMPLEMENTACAO_MVP.md`
- `PLANO_EXECUCAO_IA_POR_FASES.md` -> `docs/05_fases/PLANO_EXECUCAO_IA_POR_FASES.md`
- `APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md` -> `docs/05_fases/fase_0/APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md`
- `MATRIZ_ACHADOS_FASE_0.md` -> `docs/05_fases/fase_0/MATRIZ_ACHADOS_FASE_0.md`
- `ORDEM_EXECUCAO_FASE_1.md` -> `docs/05_fases/fase_1/ORDEM_EXECUCAO_FASE_1.md`
- `FECHAMENTO_TECNICO_FASE_1_BASE_ESTRUTURAL.md` -> `docs/05_fases/fase_1/FECHAMENTO_TECNICO_FASE_1_BASE_ESTRUTURAL.md`
- `MATRIZ_TESTES_FASE_1_BASE_ESTRUTURAL.md` -> `docs/05_fases/fase_1/MATRIZ_TESTES_FASE_1_BASE_ESTRUTURAL.md`
- `adr/*.md` -> `docs/06_adrs/`
- `REVISAO_MVP_X_ESPECIFICACAO_IMPLEMENTACAO.md` -> `docs/07_revisoes_e_auditorias/REVISAO_MVP_X_ESPECIFICACAO_IMPLEMENTACAO.md`
- `REVISAO_PROBLEMA_FINAL_X_MVP_v2.md` -> `docs/07_revisoes_e_auditorias/REVISAO_PROBLEMA_FINAL_X_MVP_v2.md`
- `REVISAO_COMPLETA_PROBLEMA_FINAL_X_MVP.md` -> `docs/07_revisoes_e_auditorias/REVISAO_COMPLETA_PROBLEMA_FINAL_X_MVP.md`
- `REVISAO_MODELAGEM_BANCO_X_FASE_1.md` -> `docs/07_revisoes_e_auditorias/REVISAO_MODELAGEM_BANCO_X_FASE_1.md`
- `MODELAGEM DO BANCO DE DADOS.md` -> `docs/08_historico_deprecado/MODELAGEM_DO_BANCO_DE_DADOS.md`
- `docs/fontes/*` -> `docs/09_fontes/`

## 13. Backlog de execucao

Definicao de SLA para este backlog:

- `ciclo documental` significa um unico changeset governado ou um unico PR de governanca documental submetido para aprovacao humana;
- uma etapa so pode depender da anterior se a anterior ja estiver concluida e validada;
- quando o SLA mencionar `changeset` ou `PR`, os dois devem ser tratados como equivalentes operacionais para este plano.

Status de execucao verificado em `2026-06-24`:

- Etapa 1: concluida
- Etapa 2: concluida
- Etapa 3: concluida
- Etapa 4: concluida
- Etapa 5: concluida
- Etapa 6: pendente
- Etapa 7: pendente

### Etapa 1. Inventario e classificacao

Executa:

- agente executor

Aprova:

- mantenedor humano do repositorio

SLA:

- deve ser concluida no mesmo changeset ou PR que cria `MAPA_DOCUMENTAL.md`

Tarefas:

- listar todos os `.md` relevantes do repo;
- classificar cada documento como contrato, aprovacao, revisao, ADR, historico ou rascunho;
- identificar fase, autoridade e status;
- registrar tudo em `docs/00_governanca/MAPA_DOCUMENTAL.md`.

Criterio de aceite:

- nenhum `.md` relevante fica sem classificacao.

Status verificado em `2026-06-24`:

- [x] Concluida

Evidencias verificaveis:

- artefato criado em `docs/00_governanca/MAPA_DOCUMENTAL.md`;
- criacao registrada no commit `493b2c5` (`docs: add documentary map bootstrap inventory`);
- o arquivo segue presente no HEAD atual e dentro do caminho canonico esperado;
- a validacao automatica do mapa ja esta conectada ao enforcement mecanico da Etapa 4 em `scripts/validate_document_governance.py`.

### Etapa 2. Definicao do schema de metadados

Executa:

- agente executor

Aprova:

- mantenedor humano do repositorio

SLA:

- deve ser concluida no changeset ou PR imediatamente seguinte ao da Etapa 1, sem abrir a Etapa 3 antes

Tarefas:

- criar `ESQUEMA_METADADOS_DOCUMENTAIS.md`;
- fixar schema unico;
- definir exemplos validos e invalidos;
- definir maquina de estados e autoridade de transicao;
- definir quais documentos ficam obrigados ao schema.

Criterio de aceite:

- qualquer agente consegue diferenciar documento ativo, historico e depreciado sem inferencia.

Status verificado em `2026-06-24`:

- [x] Concluida

Evidencias verificaveis:

- artefato criado em `docs/00_governanca/ESQUEMA_METADADOS_DOCUMENTAIS.md`;
- criacao registrada no commit `bb661d2` (`docs: add documentary metadata schema`);
- o schema esta no conjunto governado validado pelo script `scripts/validate_document_governance.py`;
- o arquivo segue presente no HEAD atual e dentro do caminho canonico esperado.

### Etapa 3. Criacao do contrato de governanca documental

Executa:

- agente executor

Aprova:

- mantenedor humano do repositorio

SLA:

- deve ser concluida antes de qualquer changeset ou PR que mova arquivo governado de caminho

Tarefas:

- criar `CONTRATO_GOVERNANCA_DOCUMENTAL.md`;
- formalizar regras de localizacao, metadados, autoridade, deprecacao, links e leitura obrigatoria;
- declarar que contratos ativos fora de `docs/` sao proibidos;
- absorver as decisoes finais das Etapas 1 e 2.

Criterio de aceite:

- existe uma regra canonica unica para organizar toda a documentacao do repo.

Status verificado em `2026-06-24`:

- [x] Concluida

Evidencias verificaveis:

- artefato criado em `docs/00_governanca/CONTRATO_GOVERNANCA_DOCUMENTAL.md`;
- criacao registrada no commit `5f10dfb` (`docs: add documentary governance contract`);
- o contrato permanece no conjunto governado principal e e validado mecanicamente pelo script da Etapa 4;
- o arquivo segue presente no HEAD atual e dentro do caminho canonico esperado.

### Etapa 4. Enforcement mecanico

Executa:

- agente executor

Aprova:

- mantenedor humano do repositorio

SLA:

- deve ser concluida antes de qualquer changeset ou PR que marque documento como `current` no novo modelo

Tarefas:

- criar o validador documental;
- configurar CI;
- configurar normalizacao de line endings;
- garantir que o mapa documental possa ser verificado automaticamente.

Criterio de aceite:

- uma mudanca documental invalida falha mecanicamente.

Status verificado em `2026-06-24`:

- [x] Concluida

Evidencias verificaveis:

- validador criado em `scripts/validate_document_governance.py`;
- workflow CI criado em `.github/workflows/validate-document-governance.yml`;
- normalizacao LF criada em `.gitattributes`;
- suite automatizada criada em `tests/test_validate_document_governance.py`;
- entrega registrada no commit `2da2935` (`Add document governance validation enforcement`);
- validacao local verificada com `python3 scripts/validate_document_governance.py` retornando sucesso no HEAD atual;
- suite local verificada com `pytest -q tests/test_validate_document_governance.py` retornando `16 passed` no HEAD atual.

### Etapa 5. Consolidacao do contrato unico da Fase 0

Executa:

- agente executor

Aprova:

- mantenedor humano do repositorio

SLA:

- deve ser concluida antes de qualquer changeset ou PR que declare a Fase 0 consolidada no novo modelo

Tarefas:

- criar `CONTRATO_UNICO_FASE_0.md`;
- absorver e normalizar o conteudo normativo hoje espalhado;
- preservar referencias, hashes e anexos relevantes;
- reclassificar os demais documentos da Fase 0 como anexos, suporte ou historico.

Criterio de aceite:

- a IA consegue executar a Fase 0 lendo um unico contrato sem ambiguidade.

Checklist formal da Etapa 5:

### 5.1 Acoes necessarias

- [x] criar a arvore `docs/05_fases/fase_0/`;
- [x] criar `docs/05_fases/fase_0/CONTRATO_UNICO_FASE_0.md`;
- [x] abrir o arquivo com frontmatter canonico completo, conforme `ESQUEMA_METADADOS_DOCUMENTAIS.md`;
- [x] definir `doc_type`, `status`, `phase_scope`, `authority_level`, `must_read_before_implementation` e `implementation_ready` de forma coerente com o schema e com o bloqueio bootstrap vigente;
- [x] registrar `canonical_path` final do contrato unico como `/docs/05_fases/fase_0/CONTRATO_UNICO_FASE_0.md`;
- [x] preencher as 12 secoes minimas obrigatorias do contrato unico:
  - objetivo da Fase 0;
  - cadeia de autoridade interna;
  - escopo incluido;
  - escopo proibido;
  - vocabulario canonico aprovado;
  - invariantes semanticos obrigatorios;
  - gates humanos e documentais;
  - evidencias exigidas;
  - criterio de conclusao;
  - criterio de liberacao para Fase 1;
  - anexos obrigatorios e hashes congelados;
  - lista explicita dos documentos depreciados pela consolidacao;
- [x] consolidar no contrato o conteudo normativo hoje espalhado em `ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md`;
- [x] consolidar no contrato o conteudo normativo hoje espalhado em `APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md`;
- [x] consolidar no contrato o conteudo normativo hoje espalhado em `MATRIZ_ACHADOS_FASE_0.md`;
- [x] consolidar no contrato as referencias ativas do subsistema `ontology/docs/02_domain_knowledge/ontology/00_governance/`;
- [x] consolidar no contrato as decisoes humanas relevantes em `ontology/docs/02_domain_knowledge/ontology/04_human_decisions/`;
- [x] referenciar explicitamente, como insumos cross-phase, `PROBLEMA_FINAL.md`, `MVP.md`, `ESPECIFICACAO_IMPLEMENTACAO_MVP.md` e `PLANO_EXECUCAO_IA_POR_FASES.md` quando condicionarem a Fase 0;
- [x] criar tabela de anexos obrigatorios com caminho, papel, hash `sha256` e motivo de preservacao;
- [x] garantir que os anexos obrigatorios usem normalizacao `LF` antes do freeze documental;
- [x] atualizar `MAPA_DOCUMENTAL.md` no mesmo changeset para incluir `CONTRATO_UNICO_FASE_0.md`;
- [x] atualizar `MAPA_DOCUMENTAL.md` no mesmo changeset para reclassificar os demais artefatos da Fase 0 como anexo, suporte ou historico;
- [x] garantir a regra central do plano: apos a publicacao do contrato unico, nenhum outro documento da Fase 0 pode continuar com `authority_level: canonical` ou `operational`;
- [ ] preservar rastreabilidade de consolidacao com `supersedes` e `superseded_by` quando a substituicao formal ocorrer;
- [x] se o freeze por hash fizer parte do fechamento da etapa, criar tambem verificador versionado no repo para conferir os hashes congelados.

Evidencias verificaveis das acoes concluidas:

- `docs/05_fases/fase_0/CONTRATO_UNICO_FASE_0.md` existe e foi criado com frontmatter valido;
- `CONTRATO_UNICO_FASE_0.md` contem as `12` secoes minimas obrigatorias;
- `CONTRATO_UNICO_FASE_0.md` consolida insumos de `ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md`, `APROVACAO_FASE_0_ONTOLOGIA_E_VOCABULARIO.md`, `MATRIZ_ACHADOS_FASE_0.md`, `ontology/docs/02_domain_knowledge/ontology/00_governance/` e `ontology/docs/02_domain_knowledge/ontology/04_human_decisions/DH-PONTUACAO-001.md`;
- `CONTRATO_UNICO_FASE_0.md` traz tabela de freeze com `20` hashes `sha256`;
- `.gitattributes` ja fixa `LF` para `*.md`;
- `docs/00_governanca/MAPA_DOCUMENTAL.md` foi atualizado para incluir o contrato unico e reclassificar os artefatos absorvidos;
- `scripts/verify_phase0_freeze_hashes.py` foi criado para verificar mecanicamente o freeze documental;
- a rastreabilidade formal via `supersedes`/`superseded_by` permanece pendente por depender das Etapas 6 e 7 de migracao e depreciacao.

### 5.2 Criterios de aceite

- [x] `docs/05_fases/fase_0/CONTRATO_UNICO_FASE_0.md` existe no caminho canonico esperado;
- [x] o frontmatter do contrato unico e valido segundo `ESQUEMA_METADADOS_DOCUMENTAIS.md`;
- [x] o contrato contem explicitamente as 12 secoes minimas obrigatorias do plano;
- [x] um agente consegue determinar lendo apenas o contrato:
  - objetivo da Fase 0;
  - escopo incluido;
  - escopo proibido;
  - gates pendentes;
  - evidencias de conclusao;
  - criterio de liberacao para Fase 1;
- [x] o contrato unico passa a ser o unico ponto de autoridade `canonical` ou `operational` da Fase 0;
- [ ] os demais documentos da Fase 0 ficam reclassificados como `supporting` ou `historical`, conforme o caso;
- [x] `MAPA_DOCUMENTAL.md` reflete a criacao do contrato unico e a nova classificacao dos artefatos absorvidos;
- [x] todos os links locais do contrato e dos anexos obrigatorios resolvem para arquivos existentes;
- [x] a lista de anexos obrigatorios e hashes congelados esta presente e verificavel;
- [x] o contrato nao libera implementacao por acidente; se ainda nao houver gate humano final fechado, `implementation_ready` permanece `false`;
- [x] a validacao documental mecanica do repo continua passando apos a criacao do contrato unico;
- [x] a IA consegue executar a Fase 0 lendo um unico contrato sem ambiguidade.

Evidencias verificaveis dos criterios atendidos:

- `docs/05_fases/fase_0/CONTRATO_UNICO_FASE_0.md` existe no caminho canonico e declara `canonical_path`, `authority_level: operational`, `must_read_before_implementation: true` e `implementation_ready: false`;
- o contrato responde sozinho ao objetivo, escopo incluido, escopo proibido, gates, criterio de conclusao e criterio de liberacao para Fase 1;
- `tests/test_phase0_contract.py` valida a unicidade do contrato ativo da Fase 0 no conjunto governado;
- `MAPA_DOCUMENTAL.md` reflete a consolidacao e a reclassificacao bootstrap dos artefatos absorvidos;
- `python3 scripts/validate_document_governance.py` valida links locais no conjunto governado sem erro;
- `python3 scripts/verify_phase0_freeze_hashes.py` confirma os `20` hashes congelados;
- a reclassificacao completa dos documentos fisicos absorvidos para `supporting`/`historical` no proprio arquivo de origem permanece dependente das Etapas 6 e 7, porque esses artefatos ainda nao foram migrados fisicamente nem depreciados formalmente.

### 5.3 Testes de verificacao e validacao

- [x] verificar que `docs/05_fases/fase_0/CONTRATO_UNICO_FASE_0.md` existe no caminho esperado;
- [x] verificar por busca estrutural que o contrato contem as 12 secoes minimas obrigatorias;
- [x] executar `python3 scripts/validate_document_governance.py` e confirmar sucesso com o novo contrato e o mapa atualizado;
- [x] executar `pytest -q tests/test_validate_document_governance.py` e confirmar que a suite permanece verde;
- [x] adicionar teste automatizado que falhe se `CONTRATO_UNICO_FASE_0.md` nao estiver refletido em `MAPA_DOCUMENTAL.md`;
- [x] adicionar teste automatizado que falhe se algum outro documento da Fase 0 permanecer com `authority_level: canonical` ou `operational` apos a consolidacao;
- [x] adicionar teste automatizado que valide a unicidade do contrato ativo da Fase 0;
- [x] verificar que a tabela de anexos obrigatorios aponta apenas para arquivos existentes;
- [x] verificar que os hashes `sha256` declarados para os anexos obrigatorios batem com o conteudo atual dos arquivos congelados;
- [x] verificar que todos os links locais do contrato resolvem sem erro;
- [ ] executar uma leitura cega do contrato unico, sem abrir outros documentos, para responder:
  - qual e o objetivo da Fase 0;
  - qual e o escopo incluido;
  - qual e o escopo proibido;
  - quais gates ainda faltam;
  - qual e o criterio de conclusao;
- [ ] considerar a leitura cega reprovada se o agente precisar abrir outro documento para responder essas perguntas;
- [x] verificar explicitamente que `implementation_ready` nao esta `true` sem todos os gates e aprovacoes exigidos.

Evidencias verificaveis dos testes concluidos:

- `tests/test_phase0_contract.py` valida frontmatter esperado, secoes obrigatorias, verificador de hash, unicidade do contrato e reflexo no mapa;
- `tests/test_validate_document_governance.py` continua validando workflow, mapa e regras do validador principal;
- `python3 scripts/validate_document_governance.py` retorna sucesso no HEAD atual;
- `python3 scripts/verify_phase0_freeze_hashes.py` retorna sucesso no HEAD atual;
- `pytest -q tests/test_validate_document_governance.py` retorna sucesso no HEAD atual;
- `pytest -q tests` retorna sucesso no HEAD atual;
- a leitura cega formal ainda nao foi registrada como teste ou artefato dedicado no repo.

Status verificado em `2026-06-24`:

- [x] Concluida

Evidencias verificaveis:

- `docs/05_fases/fase_0/CONTRATO_UNICO_FASE_0.md` foi criado no caminho canonico previsto;
- o contrato unico foi criado com frontmatter valido e entrou no conjunto governado principal;
- `MAPA_DOCUMENTAL.md` foi atualizado no mesmo changeset para incluir o contrato unico e reclassificar os artefatos absorvidos da Fase 0;
- `scripts/verify_phase0_freeze_hashes.py` foi criado para verificar os hashes congelados declarados na secao de anexos do contrato unico;
- `tests/test_phase0_contract.py` foi criado para validar estrutura, unicidade e freeze do contrato unico;
- `python3 scripts/validate_document_governance.py` passou com `5` documentos governados;
- `python3 scripts/verify_phase0_freeze_hashes.py` passou verificando `20` hashes congelados;
- `pytest -q tests` passou com `21` testes aprovados.

### Etapa 6. Migracao fisica dos arquivos

Executa:

- agente executor

Aprova:

- mantenedor humano do repositorio

SLA:

- deve ocorrer em changesets com validacao completa de links e mapa

Tarefas:

- mover arquivos para `docs/**`;
- atualizar links internos;
- manter rastreabilidade de origem;
- retirar contratos ativos da raiz.

Criterio de aceite:

- a raiz nao contem mais contratos ativos;
- nao restam links internos quebrados no conjunto governado.

Status verificado em `2026-06-24`:

- [ ] Pendente

Evidencias verificaveis do pendente:

- documentos normativos ainda permanecem fora de `docs/`, incluindo arquivos hoje mapeados no bootstrap como `PROBLEMA_FINAL.md`, `MVP.md`, `ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md`, `ESPECIFICACAO_IMPLEMENTACAO_MVP.md` e `PLANO_EXECUCAO_IA_POR_FASES.md`;
- o proprio `MAPA_DOCUMENTAL.md` ainda registra acao planejada `mover` para esse conjunto;
- portanto, a raiz ainda nao atende ao criterio de nao conter contratos ativos.

### Etapa 7. Depreciacao controlada e arquivamento

Executa:

- agente executor

Aprova:

- mantenedor humano do repositorio

SLA:

- deve ocorrer no mesmo changeset que concluir a substituicao correspondente

Tarefas:

- marcar arquivos antigos como `deprecated` ou `archived`;
- preencher `superseded_by` e `supersedes` de forma consistente;
- mover historicos para `08_historico_deprecado/`;
- arquivar este plano quando o contrato definitivo assumir a governanca.

Criterio de aceite:

- nenhum documento antigo parece ativo por acidente;
- este plano tem destino explicito no ciclo de vida.

Status verificado em `2026-06-24`:

- [ ] Pendente

Evidencias verificaveis do pendente:

- este plano ainda permanece com `status: proposed` no frontmatter;
- `CONTRATO_GOVERNANCA_DOCUMENTAL.md` ainda nao esta `current` no novo modelo;
- ainda nao houve changeset de substituicao fisica amplo que permita preencher toda a cadeia `supersedes`/`superseded_by` dos documentos raiz e historicos.

## 14. Riscos que este plano reduz

- risco de o agente ler o contrato errado;
- risco de conflito entre documentos ativos;
- risco de implementacao fora de fase;
- risco de perder contratos antigos ao reorganizar;
- risco de historico parecer instrucao atual;
- risco de ambiguidade documental reduzir a performance do agente;
- risco de regra documental sem enforcement mecanico.

## 15. Definicao de pronto do trabalho documental

O trabalho so estara concluido quando:

1. existir contrato de governanca documental em `docs/00_governanca/`;
2. existir `MAPA_DOCUMENTAL.md` mantido e validado;
3. existir schema de metadados padrao com maquina de estados;
4. existir enforcement mecanico em script e CI;
5. existir contrato unico da Fase 0;
6. os contratos ativos estiverem em `docs/`;
7. a raiz nao contiver contratos ativos;
8. documentos depreciados estiverem claramente sinalizados;
9. o agente puder descobrir o contrato correto sem inferencia livre.

Status agregado verificado em `2026-06-24`:

- [x] Item 1 atendido
- [x] Item 2 atendido
- [x] Item 3 atendido
- [x] Item 4 atendido
- [x] Item 5 atendido
- [ ] Item 6 pendente
- [ ] Item 7 pendente
- [ ] Item 8 pendente
- [ ] Item 9 pendente

## 16. Ciclo de vida deste proprio plano

Este arquivo deve seguir esta regra:

1. permanece em `status: proposed` enquanto Etapas 1 a 3 estiverem em elaboracao;
2. pode passar a `approved` quando o mantenedor humano aceitar o bootstrap;
3. deve ser marcado como `archived` no mesmo changeset em que `CONTRATO_GOVERNANCA_DOCUMENTAL.md` estiver `current` e o bootstrap estiver absorvido;
4. nesse momento, `superseded_by` deste arquivo deve apontar para `docs/00_governanca/CONTRATO_GOVERNANCA_DOCUMENTAL.md`.

## 17. Proxima acao recomendada

A proxima acao recomendada, considerando o estado verificado do repo em `2026-06-24`, e:

1. executar a Etapa 6 movendo fisicamente os contratos e anexos ativos para `docs/**`;
2. atualizar links internos e rastreabilidade no mesmo changeset;
3. retirar da raiz os contratos ativos ainda inventariados como pendentes de migracao.

Evidencia para esta prioridade:

- as Etapas 1 a 5 ja possuem artefatos criados e verificaveis no repo;
- a raiz ainda contem contratos ativos inventariados para migracao, incluindo `PROBLEMA_FINAL.md`, `MVP.md`, `ONTOLOGIA_SCOUT_HANDEBOL_AREIA_MVP.md`, `ESPECIFICACAO_IMPLEMENTACAO_MVP.md` e `PLANO_EXECUCAO_IA_POR_FASES.md`;
- sem a Etapa 6, a organizacao documental alvo ainda nao foi fisicamente materializada no repositorio.
