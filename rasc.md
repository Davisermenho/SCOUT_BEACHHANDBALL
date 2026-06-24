# Acoes Necessarias da Etapa 4

## 1. Acoes necessarias para criar `scripts/validate_document_governance.py`

- criar o diretorio `scripts/`;
- criar o arquivo `scripts/validate_document_governance.py`;
- implementar um validador CLI que rode sem interacao manual;
- fazer o parser do frontmatter YAML dos arquivos governados;
- validar presenca dos campos obrigatorios;
- validar enums de `doc_type`, `status`, `phase_scope` e `authority_level`;
- validar regras cruzadas entre `status`, `authority_level`, `must_read_before_implementation` e `implementation_ready`;
- validar coerencia de `phase_scope`, incluindo regra de `cross_phase` e conflitos de escopo;
- validar `canonical_path` contra o caminho real do arquivo;
- validar `superseded_by` quando nao for `null`;
- validar conflito de documentos `current` por fase e categoria operacional;
- validar inexistencia de contrato ativo fora de `docs/` no conjunto governado principal;
- validar divergencia entre `MAPA_DOCUMENTAL.md` e o frontmatter real dos arquivos governados;
- retornar `0` em sucesso e codigo diferente de `0` em falha.

## 2. Acoes necessarias para configurar o workflow de CI

- criar o diretorio `.github/workflows/`;
- criar o arquivo `.github/workflows/validate-document-governance.yml`;
- configurar gatilhos em `push` e `pull_request`;
- configurar execucao do validador em ambiente limpo;
- fazer o workflow falhar quando o script falhar;
- fazer o workflow passar quando o script passar;
- limitar o escopo inicial do workflow ao conjunto governado atual;
- evitar acoplamento imediato com todo o subsistema `ontology/` enquanto ele continuar em adaptacao controlada.

## 3. Acoes necessarias para configurar a normalizacao de line endings em `.gitattributes`

- criar `.gitattributes` na raiz do repositorio;
- definir normalizacao em `LF` para arquivos Markdown governados;
- definir normalizacao em `LF` para arquivos YAML de workflow e metadados;
- definir normalizacao em `LF` para scripts Python do enforcement;
- evitar regras amplas demais que atinjam binarios ou artefatos fora de escopo;
- revalidar os arquivos governados apos a criacao para garantir que o validador nao quebre por diferenca de final de linha.

## 4. Acoes necessarias para garantir verificacao automatica do `MAPA_DOCUMENTAL.md`

- definir no validador quais colunas do mapa sao obrigatorias;
- extrair do mapa, no minimo, `arquivo_atual`, classificacao bootstrap, `destino_canonico_planejado` e `acao_planejada`;
- comparar o que o mapa declara com o frontmatter real dos arquivos governados;
- falhar se um arquivo governado nao estiver mapeado;
- falhar se o mapa listar caminho divergente do estado real;
- falhar se `status` ou `authority_level` do mapa entrarem em conflito com o frontmatter;
- falhar se um arquivo novo em `docs/` nao tiver sido refletido no mapa;
- rodar essa verificacao tanto localmente quanto no workflow de CI.

## 5. Ordem recomendada de execucao

- criar `scripts/validate_document_governance.py`;
- criar `.gitattributes`;
- criar `.github/workflows/validate-document-governance.yml`;
- ajustar o validador ate ele conseguir verificar automaticamente o `MAPA_DOCUMENTAL.md`.

# Criterios de Aceite dos Testes da Etapa 4

## 1. Criterios de aceite dos testes para `validate_document_governance.py`

Os testes do validador so devem ser considerados aceitos quando:

- cobrirem pelo menos um caso valido completo com retorno `0`;
- cobrirem casos invalidos com retorno diferente de `0`;
- exercitarem todos os grupos de regra previstos no contrato:
  - campos obrigatorios
  - enums validos
  - coerencia entre `status` e `authority_level`
  - coerencia entre `must_read_before_implementation` e `implementation_ready`
  - coerencia de `phase_scope`
  - `canonical_path`
  - `superseded_by`
  - conflito de contratos `current`
  - contrato ativo fora de `docs/`
  - divergencia do `MAPA_DOCUMENTAL.md`
- falharem de forma deterministica, sem depender de ordem incidental de arquivos;
- apontarem claramente qual regra falhou e em qual arquivo;
- conseguirem distinguir regressao real de erro de fixture.

## 2. Criterios de aceite dos testes para o workflow de CI

Os testes do workflow so devem ser considerados aceitos quando:

- provarem que o workflow dispara em `push` e `pull_request`;
- provarem que o workflow falha quando o validador falha;
- provarem que o workflow passa quando o validador passa;
- confirmarem que a execucao em CI reproduz o mesmo resultado da execucao local;
- nao dependerem de estado manual do revisor ou da maquina do desenvolvedor;
- validarem o comportamento do workflow no escopo governado atual, sem exigir cobertura prematura do subsistema `ontology/`.

## 3. Criterios de aceite dos testes para normalizacao de line endings em `.gitattributes`

Os testes de normalizacao so devem ser considerados aceitos quando:

- verificarem explicitamente que arquivos governados terminam em `LF`;
- comprovarem que uma introducao artificial de `CRLF` e corrigida ou detectada pelo fluxo previsto;
- confirmarem que a normalizacao nao altera semanticamente o conteudo dos arquivos;
- confirmarem que o validador continua funcionando apos a normalizacao;
- confirmarem que a regra nao atinge binarios ou artefatos fora de escopo por engano.

## 4. Criterios de aceite dos testes para verificacao automatica do `MAPA_DOCUMENTAL.md`

Os testes do mapa so devem ser considerados aceitos quando:

- cobrirem um caso valido em que mapa e frontmatter estejam consistentes;
- cobrirem um caso invalido para arquivo governado ausente no mapa;
- cobrirem um caso invalido para classificacao bootstrap divergente;
- cobrirem um caso invalido para destino canonico planejado incoerente;
- cobrirem um caso invalido para arquivo novo em `docs/` sem reflexo no mapa;
- confirmarem que a mesma verificacao roda localmente e no CI;
- garantirem que o mapa continua tratado como derivado, e nao como fonte primaria de verdade.

## 5. Criterio de aceite agregado dos testes da Etapa 4

A bateria de testes da Etapa 4 so deve ser considerada aceita quando:

- detectar tanto cenarios validos quanto invalidos para cada um dos quatro entregaveis;
- reproduzir o mesmo veredito localmente e em CI;
- falhar de forma previsivel e explicavel quando houver regressao;
- dar cobertura suficiente para sustentar o criterion de que uma mudanca documental invalida falha mecanicamente antes de virar baseline governado.

# Criterios de Aceite da Etapa 4

## 1. Criterios de aceite para `validate_document_governance.py`

O script so deve ser considerado aceito quando:

- existir em `scripts/validate_document_governance.py`;
- rodar localmente por linha de comando sem depender de interacao manual;
- retornar `0` quando a validacao passar;
- retornar codigo diferente de `0` quando a validacao falhar;
- validar presenca de todos os campos obrigatorios do frontmatter;
- validar enums de `doc_type`, `status`, `phase_scope` e `authority_level`;
- validar coerencia entre `status`, `authority_level`, `must_read_before_implementation` e `implementation_ready`;
- validar coerencia de `phase_scope`, incluindo regra de `cross_phase` e conflitos de escopo;
- validar `canonical_path` contra o caminho real do arquivo;
- validar `superseded_by` quando nao for `null`;
- rejeitar contrato ativo fora de `docs/` no conjunto governado principal;
- rejeitar mais de um contrato `current` para a mesma fase e mesma categoria operacional;
- rejeitar divergencia entre `MAPA_DOCUMENTAL.md` e o frontmatter real dos arquivos governados.

## 2. Criterios de aceite para o workflow de CI

O workflow de CI so deve ser considerado aceito quando:

- existir em `.github/workflows/validate-document-governance.yml`;
- rodar no GitHub Actions;
- disparar em `push` e `pull_request`;
- executar o validador em ambiente limpo;
- falhar quando o script `validate_document_governance.py` falhar;
- passar quando o script passar;
- cobrir o conjunto governado atual sem misturar automaticamente todo o subsistema `ontology/` ainda em adaptacao controlada;
- impedir que um changeset documental invalido seja tratado como baseline governado.

## 3. Criterios de aceite para normalizacao de line endings em `.gitattributes`

O arquivo `.gitattributes` so deve ser considerado aceito quando:

- existir na raiz do repositorio;
- definir normalizacao em `LF` para Markdown governado;
- definir normalizacao em `LF` para arquivos YAML de workflow e metadados;
- definir normalizacao em `LF` para scripts Python do enforcement;
- nao introduzir regra ampla demais que altere binarios ou artefatos fora de escopo sem necessidade;
- permitir que os arquivos governados permaneçam estaveis entre ambientes sem gerar drift artificial de hash ou diff;
- nao quebrar a execucao do validador por diferenca de final de linha.

## 4. Criterios de aceite para verificacao automatica do `MAPA_DOCUMENTAL.md`

A verificacao automatica do mapa so deve ser considerada aceita quando:

- o validador conseguir ler `docs/00_governanca/MAPA_DOCUMENTAL.md`;
- o validador conseguir extrair do mapa, no minimo, `arquivo_atual`, classificacao bootstrap, `destino_canonico_planejado` e `acao_planejada`;
- todo arquivo governado pelo escopo inicial aparecer no mapa;
- nenhum arquivo governado listado no mapa apontar para classificacao incompatível com o frontmatter real;
- nenhum arquivo novo em `docs/` ficar fora do mapa;
- divergencia entre `MAPA_DOCUMENTAL.md` e o frontmatter real causar falha de validacao;
- a mesma verificacao rodar localmente e no workflow de CI.

## 5. Criterio de aceite agregado da Etapa 4

A Etapa 4 so deve ser considerada aceita quando:

- a validacao roda localmente;
- a validacao roda em CI;
- uma mudanca documental invalida falha mecanicamente;
- divergencia entre `MAPA_DOCUMENTAL.md` e o frontmatter real passa a quebrar a validacao;
- o repositorio ganha uma barreira automatica minima contra erro de localizacao, metadados, status e rastreabilidade documental.

# Testes da Etapa 4

## 1. Testes para `scripts/validate_document_governance.py`

### 1.1 Testes de sucesso

- executar `scripts/validate_document_governance.py` no estado valido atual do conjunto governado e verificar saida com codigo `0`;
- verificar que o script consegue ler os arquivos em `docs/00_governanca/` e processar o frontmatter sem erro;
- verificar que o script aceita:
  - campos obrigatorios presentes;
  - enums validos;
  - `canonical_path` coerente com o caminho real;
  - `status` e `authority_level` coerentes;
  - `MAPA_DOCUMENTAL.md` coerente com o frontmatter real.

### 1.2 Testes de falha

- remover temporariamente um campo obrigatorio de um arquivo governado e verificar falha;
- trocar `doc_type` por valor invalido e verificar falha;
- trocar `status` por valor invalido e verificar falha;
- trocar `authority_level` por combinacao invalida com `status` e verificar falha;
- definir `implementation_ready: true` em documento que nao possa liberar implementacao e verificar falha;
- alterar `canonical_path` para caminho divergente do arquivo real e verificar falha;
- definir `superseded_by` apontando para arquivo inexistente e verificar falha;
- criar conflito com dois contratos `current` para a mesma fase e mesma categoria operacional e verificar falha;
- simular contrato ativo fora de `docs/` no conjunto governado principal e verificar falha.

### 1.3 Testes de comportamento

- verificar que o script retorna `0` em sucesso;
- verificar que o script retorna codigo diferente de `0` em falha;
- verificar que a mensagem de erro aponta qual regra falhou e em qual arquivo.

## 2. Testes para o workflow de CI

### 2.1 Testes de sucesso

- subir changeset valido e verificar que o workflow `.github/workflows/validate-document-governance.yml` roda com sucesso em `push`;
- abrir PR com changeset valido e verificar que o workflow roda com sucesso em `pull_request`;
- verificar que o workflow executa o validador em ambiente limpo.

### 2.2 Testes de falha

- abrir PR com frontmatter invalido e verificar que o workflow falha;
- abrir PR com `MAPA_DOCUMENTAL.md` desatualizado em relacao ao frontmatter e verificar que o workflow falha;
- abrir PR com `canonical_path` divergente e verificar que o workflow falha;
- abrir PR com contrato ativo fora de `docs/` no conjunto governado e verificar que o workflow falha.

### 2.3 Testes de integracao

- verificar que o resultado do workflow e consistente com a execucao local do script;
- verificar que o workflow nao depende de estado local do desenvolvedor;
- verificar que o escopo inicial do workflow cobre os documentos governados atuais sem exigir convergencia completa imediata do subsistema `ontology/`.

## 3. Testes para normalizacao de line endings em `.gitattributes`

### 3.1 Testes de sucesso

- verificar que `.gitattributes` existe na raiz;
- verificar que Markdown governado e normalizado em `LF`;
- verificar que YAML de workflow e metadados e normalizado em `LF`;
- verificar que scripts Python do enforcement sao normalizados em `LF`.

### 3.2 Testes de falha

- introduzir arquivo governado com `CRLF`, reexecutar o fluxo de normalizacao e verificar que o diff final volta para `LF`;
- verificar que uma mudanca artificial apenas de line ending nao deixa arquivos governados em estado inconsistente apos renormalizacao.

### 3.3 Testes de regressao

- verificar que `.gitattributes` nao tenta normalizar binarios ou artefatos fora de escopo;
- verificar que a normalizacao nao quebra o validador;
- verificar que a normalizacao nao altera semanticamente o conteudo dos arquivos governados.

## 4. Testes para verificacao automatica do `MAPA_DOCUMENTAL.md`

### 4.1 Testes de sucesso

- verificar que o validador consegue abrir `docs/00_governanca/MAPA_DOCUMENTAL.md`;
- verificar que o validador consegue extrair do mapa, no minimo:
  - `arquivo_atual`
  - classificacao bootstrap
  - `destino_canonico_planejado`
  - `acao_planejada`
- verificar que todos os arquivos governados do escopo inicial aparecem no mapa;
- verificar que os arquivos listados no mapa sao coerentes com o frontmatter real.

### 4.2 Testes de falha

- remover uma entrada de arquivo governado do mapa e verificar falha;
- adicionar arquivo novo em `docs/` sem refletir no mapa e verificar falha;
- alterar classificacao bootstrap do mapa para valor incompatível com o frontmatter real e verificar falha;
- alterar destino canonico planejado para valor incoerente com o frontmatter e verificar falha.

### 4.3 Testes de integracao

- verificar que a mesma regra de consistencia do mapa roda localmente e no CI;
- verificar que a divergencia entre `MAPA_DOCUMENTAL.md` e o frontmatter real sempre quebra a validacao;
- verificar que o mapa continua sendo tratado como artefato derivado, e nao fonte primaria de verdade.

## 5. Teste agregado de Definition of Done da Etapa 4

A Etapa 4 so deve ser considerada validada quando todos estes testes passarem:

- o validador roda localmente e falha corretamente em cenarios invalidos;
- o workflow roda no GitHub Actions e replica o resultado do validador local;
- `.gitattributes` estabiliza line endings dos arquivos governados em `LF`;
- `MAPA_DOCUMENTAL.md` passa a ser verificado automaticamente contra o frontmatter real;
- um changeset documental invalido falha mecanicamente antes de ser tratado como baseline governado.
