---
doc_id: revisao-completa-problema-final-x-mvp
doc_type: review
status: deprecated
phase_scope:
  - cross_phase
authority_level: historical
owned_by: repo_documentary_history
canonical_path: /docs/07_revisoes_e_auditorias/REVISAO_COMPLETA_PROBLEMA_FINAL_X_MVP.md
supersedes: []
superseded_by: /docs/07_revisoes_e_auditorias/REVISAO_PROBLEMA_FINAL_X_MVP_v2.md
must_read_before_implementation: false
implementation_ready: false
last_reviewed: "2026-06-24"
---

# Revisao Completa: PROBLEMA_FINAL x MVP

## Aviso de substituicao

Este documento foi substituido operacionalmente por [REVISAO_PROBLEMA_FINAL_X_MVP_v2.md](/docs/07_revisoes_e_auditorias/REVISAO_PROBLEMA_FINAL_X_MVP_v2.md:1).

Regra:

- este arquivo nao deve mais ser usado como gate de continuidade;
- ele permanece apenas como historico de auditoria anterior;
- qualquer decisao atual deve usar a revisao v2 e a cadeia normativa vigente.

## Metodo

Este documento cruza cada linha com conteudo semantico de [PROBLEMA_FINAL.md](/docs/01_contexto/PROBLEMA_FINAL.md:1) com a evidencia verificavel presente em [MVP.md](/docs/02_produto/MVP.md:1).

Legenda de status:

- `coberta`: existe evidencia direta e verificavel no MVP;
- `parcial`: existe evidencia relacionada, mas incompleta ou com desvio;
- `sem cobertura`: nao ha evidencia verificavel suficiente no MVP;
- `estrutural`: linha de titulo, separador ou organizacao, sem requisito material proprio.

Observacao:

- linhas em branco do `PROBLEMA_FINAL.md` foram omitidas porque nao possuem conteudo semantico auditavel;
- quando a linha do `PROBLEMA_FINAL.md` descreve governanca do proprio SSOT, a cobranca sobre o `MVP.md` pode ser apenas indireta.

## Cruzamento Linha a Linha

- `PF 1` `## Nota de Consolidacao`
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:5) referencia explicitamente o `PROBLEMA_FINAL.md` como SSOT.
  Status: `coberta`

- `PF 3` Fonte oficial da definicao do problema.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:5) afirma que o MVP e definido com base no SSOT.
  Status: `coberta`

- `PF 5` Consolidacao combina duas dimensoes complementares.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:27), [MVP.md](/docs/02_produto/MVP.md:38), [MVP.md](/docs/02_produto/MVP.md:64) e [MVP.md](/docs/02_produto/MVP.md:545) cobrem principios, restricoes, causa raiz e criterios verificaveis.
  Status: `coberta`

- `PF 7` Diagnostico, causa raiz e contexto humano do treinador solo.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:29), [MVP.md](/docs/02_produto/MVP.md:66), [MVP.md](/docs/02_produto/MVP.md:633).
  Status: `coberta`

- `PF 8` Restricoes de engenharia, escopo do MVP, requisitos e criterios de aceitacao.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:38), [MVP.md](/docs/02_produto/MVP.md:73), [MVP.md](/docs/02_produto/MVP.md:545), [MVP.md](/docs/02_produto/MVP.md:558).
  Status: `coberta`

- `PF 9` SSOT deve ser referencia principal antes de propor solucao tecnica.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:5).
  Status: `coberta`

- `PF 11` Justificativa da consolidacao.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:5) assume o documento consolidado como base, mas nao repete a justificativa.
  Status: `parcial`

- `PF 12` Diagnostico, causa raiz e contexto humano.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:29), [MVP.md](/docs/02_produto/MVP.md:66), [MVP.md](/docs/02_produto/MVP.md:633).
  Status: `coberta`

- `PF 13` Restricoes de engenharia, MVP, requisitos e criterios de aceitacao.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:38), [MVP.md](/docs/02_produto/MVP.md:73), [MVP.md](/docs/02_produto/MVP.md:545), [MVP.md](/docs/02_produto/MVP.md:558).
  Status: `coberta`

- `PF 14` Documentos anteriores separados eram incompletos; juntos formam a base.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:5) depende do SSOT consolidado, mas nao demonstra explicitamente a incompletude anterior.
  Status: `parcial`

- `PF 16` Estrutura Consolidada do PROBLEMA_FINAL.
  Evidencia no MVP: linha estrutural, sem requisito material a ser solucionado.
  Status: `estrutural`

- `PF 17` `1. Contexto`
  Evidencia no MVP: a secao de usuarios e principios em [MVP.md](/docs/02_produto/MVP.md:27) e [MVP.md](/docs/02_produto/MVP.md:102) incorpora o contexto.
  Status: `coberta`

- `PF 18` Sou treinador solo de handebol de areia.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:29), [MVP.md](/docs/02_produto/MVP.md:30), [MVP.md](/docs/02_produto/MVP.md:106), [MVP.md](/docs/02_produto/MVP.md:618).
  Status: `coberta`

- `PF 19` Desempenho funcoes tipicas de uma comissao tecnica.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:31), [MVP.md](/docs/02_produto/MVP.md:397), [MVP.md](/docs/02_produto/MVP.md:612).
  Status: `coberta`

- `PF 20` Planejamento de treinos.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:125), [MVP.md](/docs/02_produto/MVP.md:172).
  Status: `coberta`

- `PF 21` Direcao de equipe.
  Evidencia no MVP: historicos, relatorios e consulta em [MVP.md](/docs/02_produto/MVP.md:141), [MVP.md](/docs/02_produto/MVP.md:243), [MVP.md](/docs/02_produto/MVP.md:631) apoiam direcao, mas nao ha tratamento explicito.
  Status: `parcial`

- `PF 22` Estrategia de jogo.
  Evidencia no MVP: comparacoes e relatorios em [MVP.md](/docs/02_produto/MVP.md:221), [MVP.md](/docs/02_produto/MVP.md:250), [MVP.md](/docs/02_produto/MVP.md:456) apoiam estrategia, mas nao ha modulo estrategico explicito.
  Status: `parcial`

- `PF 23` Scout.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:83), [MVP.md](/docs/02_produto/MVP.md:210), [MVP.md](/docs/02_produto/MVP.md:487).
  Status: `coberta`

- `PF 24` Avaliacao individual.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:223), [MVP.md](/docs/02_produto/MVP.md:425), [MVP.md](/docs/02_produto/MVP.md:458).
  Status: `coberta`

- `PF 25` Controle de presenca.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:82), [MVP.md](/docs/02_produto/MVP.md:196), [MVP.md](/docs/02_produto/MVP.md:331).
  Status: `coberta`

- `PF 26` Producao de relatorios.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:86), [MVP.md](/docs/02_produto/MVP.md:243), [MVP.md](/docs/02_produto/MVP.md:423), [MVP.md](/docs/02_produto/MVP.md:509).
  Status: `coberta`

- `PF 27` Analise de adversarios.
  Evidencia no MVP: cadastro de adversarios e relatorios por competicao em [MVP.md](/docs/02_produto/MVP.md:79), [MVP.md](/docs/02_produto/MVP.md:157), [MVP.md](/docs/02_produto/MVP.md:187), [MVP.md](/docs/02_produto/MVP.md:448).
  Status: `coberta`

- `PF 28` Producao de videos de analise.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:35), [MVP.md](/docs/02_produto/MVP.md:252), [MVP.md](/docs/02_produto/MVP.md:262) tratam video apenas como referencia manual, nao como producao.
  Status: `parcial`

- `PF 29` Organizacao do conhecimento tecnico da equipe.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:18), [MVP.md](/docs/02_produto/MVP.md:58), [MVP.md](/docs/02_produto/MVP.md:68), [MVP.md](/docs/02_produto/MVP.md:635).
  Status: `coberta`

- `PF 30` Tempo disponivel reduzido por atuar tambem com handebol de quadra.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:31), [MVP.md](/docs/02_produto/MVP.md:397), [MVP.md](/docs/02_produto/MVP.md:612), [MVP.md](/docs/02_produto/MVP.md:618).
  Status: `coberta`

- `PF 32` `2. Situacao Atual`
  Evidencia no MVP: a finalidade e a justificativa em [MVP.md](/docs/02_produto/MVP.md:7) e [MVP.md](/docs/02_produto/MVP.md:66) respondem a situacao atual.
  Status: `coberta`

- `PF 33` Dados distribuidos entre varias fontes.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:9), [MVP.md](/docs/02_produto/MVP.md:58), [MVP.md](/docs/02_produto/MVP.md:68), [MVP.md](/docs/02_produto/MVP.md:635).
  Status: `coberta`

- `PF 34` Planilhas Excel.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:36), [MVP.md](/docs/02_produto/MVP.md:62), [MVP.md](/docs/02_produto/MVP.md:472), [MVP.md](/docs/02_produto/MVP.md:627).
  Status: `coberta`

- `PF 35` Videos.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:35), [MVP.md](/docs/02_produto/MVP.md:60), [MVP.md](/docs/02_produto/MVP.md:252).
  Status: `coberta`

- `PF 36` WhatsApp.
  Evidencia no MVP: o MVP centraliza dados no sistema unico em [MVP.md](/docs/02_produto/MVP.md:9), [MVP.md](/docs/02_produto/MVP.md:68), mas nao trata migracao especifica de WhatsApp.
  Status: `parcial`

- `PF 37` Google Drive.
  Evidencia no MVP: a centralizacao em banco unico e indicada em [MVP.md](/docs/02_produto/MVP.md:58) e [MVP.md](/docs/02_produto/MVP.md:68), mas nao ha procedimento especifico para Drive.
  Status: `parcial`

- `PF 38` OneDrive.
  Evidencia no MVP: mesma cobertura indireta de centralizacao em [MVP.md](/docs/02_produto/MVP.md:58) e [MVP.md](/docs/02_produto/MVP.md:68), sem migracao especifica.
  Status: `parcial`

- `PF 39` Documentos.
  Evidencia no MVP: centralizacao do registro tecnico no sistema em [MVP.md](/docs/02_produto/MVP.md:18), [MVP.md](/docs/02_produto/MVP.md:68), sem estrategia explicita para documentos legados.
  Status: `parcial`

- `PF 40` Arquivos locais.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:60) e [MVP.md](/docs/02_produto/MVP.md:256) aceitam armazenamento local e referencia manual.
  Status: `coberta`

- `PF 41` Nao existe base unica de conhecimento.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:18), [MVP.md](/docs/02_produto/MVP.md:58), [MVP.md](/docs/02_produto/MVP.md:68).
  Status: `coberta`

- `PF 43` `3. Historico das Tentativas`
  Evidencia no MVP: linha contextual; o MVP responde ao fracasso das tentativas anteriores por centralizacao.
  Status: `parcial`

- `PF 44` Foram utilizadas diversas ferramentas.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:68) afirma a necessidade de concentrar o registro em um unico sistema, mas nao lista o historico das ferramentas.
  Status: `parcial`

- `PF 45` Excel.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:36), [MVP.md](/docs/02_produto/MVP.md:62), [MVP.md](/docs/02_produto/MVP.md:627).
  Status: `coberta`

- `PF 46` Adobe Premiere.
  Evidencia no MVP: apenas restricao de nao automatizar video em [MVP.md](/docs/02_produto/MVP.md:262), sem cobertura especifica para a ferramenta.
  Status: `parcial`

- `PF 47` CapCut.
  Evidencia no MVP: mesma cobertura indireta de video manual em [MVP.md](/docs/02_produto/MVP.md:252) e [MVP.md](/docs/02_produto/MVP.md:262), sem cobertura especifica da ferramenta.
  Status: `parcial`

- `PF 48` WhatsApp.
  Evidencia no MVP: centralizacao generica em [MVP.md](/docs/02_produto/MVP.md:68), sem estrategia de extracao/importacao.
  Status: `parcial`

- `PF 49` Google Drive.
  Evidencia no MVP: centralizacao generica em [MVP.md](/docs/02_produto/MVP.md:68), sem estrategia de extracao/importacao.
  Status: `parcial`

- `PF 50` OneDrive.
  Evidencia no MVP: centralizacao generica em [MVP.md](/docs/02_produto/MVP.md:68), sem estrategia de extracao/importacao.
  Status: `parcial`

- `PF 51` Ferramentas resolveram partes, nao o problema sistemico e longitudinal.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:68), [MVP.md](/docs/02_produto/MVP.md:69), [MVP.md](/docs/02_produto/MVP.md:221), [MVP.md](/docs/02_produto/MVP.md:406), [MVP.md](/docs/02_produto/MVP.md:636).
  Status: `coberta`

- `PF 53` `4. Problema Central`
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:51) e [MVP.md](/docs/02_produto/MVP.md:631) respondem ao problema central.
  Status: `coberta`

- `PF 54` Nao existe um sistema unico capaz de:
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:57), [MVP.md](/docs/02_produto/MVP.md:58), [MVP.md](/docs/02_produto/MVP.md:59).
  Status: `coberta`

- `PF 55` Centralizar dados.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:9), [MVP.md](/docs/02_produto/MVP.md:58), [MVP.md](/docs/02_produto/MVP.md:464).
  Status: `coberta`

- `PF 56` Preservar historico.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:10), [MVP.md](/docs/02_produto/MVP.md:69), [MVP.md](/docs/02_produto/MVP.md:404), [MVP.md](/docs/02_produto/MVP.md:527), [MVP.md](/docs/02_produto/MVP.md:593).
  Status: `coberta`

- `PF 57` Relacionar scout, treinos, presenca e video.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:18), [MVP.md](/docs/02_produto/MVP.md:125), [MVP.md](/docs/02_produto/MVP.md:133), [MVP.md](/docs/02_produto/MVP.md:196), [MVP.md](/docs/02_produto/MVP.md:223), [MVP.md](/docs/02_produto/MVP.md:355).
  Status: `parcial`

- `PF 58` Produzir indicadores longitudinais.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:221), [MVP.md](/docs/02_produto/MVP.md:234), [MVP.md](/docs/02_produto/MVP.md:435), [MVP.md](/docs/02_produto/MVP.md:496), [MVP.md](/docs/02_produto/MVP.md:579).
  Status: `parcial`

- `PF 59` Reduzir carga operacional.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:12), [MVP.md](/docs/02_produto/MVP.md:70), [MVP.md](/docs/02_produto/MVP.md:397), [MVP.md](/docs/02_produto/MVP.md:612).
  Status: `coberta`

- `PF 60` Conhecimento depende da memoria do treinador.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:11), [MVP.md](/docs/02_produto/MVP.md:71), [MVP.md](/docs/02_produto/MVP.md:543), [MVP.md](/docs/02_produto/MVP.md:605).
  Status: `coberta`

- `PF 62` `5. Causas Raiz`
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:66) abre a justificativa diretamente em linguagem de causa raiz.
  Status: `coberta`

- `PF 63` Causa 1 - Fragmentacao.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:68), [MVP.md](/docs/02_produto/MVP.md:635).
  Status: `coberta`

- `PF 64` Dados espalhados entre multiplas ferramentas.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:9), [MVP.md](/docs/02_produto/MVP.md:58), [MVP.md](/docs/02_produto/MVP.md:68).
  Status: `coberta`

- `PF 65` Causa 2 - Ausencia de historico estruturado.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:69), [MVP.md](/docs/02_produto/MVP.md:223), [MVP.md](/docs/02_produto/MVP.md:404), [MVP.md](/docs/02_produto/MVP.md:496).
  Status: `coberta`

- `PF 66` O scout nao possui visao longitudinal.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:221), [MVP.md](/docs/02_produto/MVP.md:230), [MVP.md](/docs/02_produto/MVP.md:432), [MVP.md](/docs/02_produto/MVP.md:493).
  Status: `coberta`

- `PF 67` Causa 3 - Dependencia excessiva de trabalho manual.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:70), [MVP.md](/docs/02_produto/MVP.md:397), [MVP.md](/docs/02_produto/MVP.md:400).
  Status: `coberta`

- `PF 68` Producao de videos e analises exige muitas horas.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:35), [MVP.md](/docs/02_produto/MVP.md:252), [MVP.md](/docs/02_produto/MVP.md:624) evitam automacao e mantem video como apoio manual, mas nao resolvem explicitamente a producao de video.
  Status: `parcial`

- `PF 69` Causa 4 - Dependencia da memoria humana.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:11), [MVP.md](/docs/02_produto/MVP.md:71), [MVP.md](/docs/02_produto/MVP.md:543), [MVP.md](/docs/02_produto/MVP.md:601).
  Status: `coberta`

- `PF 70` Decisoes dependem da lembranca do treinador.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:605), [MVP.md](/docs/02_produto/MVP.md:636), [MVP.md](/docs/02_produto/MVP.md:638).
  Status: `coberta`

- `PF 72` `6. Objetivo`
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:16) abre o objetivo do MVP.
  Status: `coberta`

- `PF 73` Memoria operacional que registra, consulta, compara e reutiliza conhecimento de treinos, jogos, competicoes e temporadas.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:18), [MVP.md](/docs/02_produto/MVP.md:20), [MVP.md](/docs/02_produto/MVP.md:21), [MVP.md](/docs/02_produto/MVP.md:24), [MVP.md](/docs/02_produto/MVP.md:25), [MVP.md](/docs/02_produto/MVP.md:158), [MVP.md](/docs/02_produto/MVP.md:297).
  Status: `parcial`

- `PF 75` `7. Restricoes Obrigatorias`
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:27) e [MVP.md](/docs/02_produto/MVP.md:38).
  Status: `coberta`

- `PF 76` Treinador solo.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:29), [MVP.md](/docs/02_produto/MVP.md:106), [MVP.md](/docs/02_produto/MVP.md:618).
  Status: `coberta`

- `PF 77` Tempo operacional limitado.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:31), [MVP.md](/docs/02_produto/MVP.md:397), [MVP.md](/docs/02_produto/MVP.md:612).
  Status: `coberta`

- `PF 78` Handebol de areia.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:30), [MVP.md](/docs/02_produto/MVP.md:49).
  Status: `coberta`

- `PF 79` MVP simples.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:31), [MVP.md](/docs/02_produto/MVP.md:75), [MVP.md](/docs/02_produto/MVP.md:397), [MVP.md](/docs/02_produto/MVP.md:625).
  Status: `coberta`

- `PF 80` Baixa manutencao.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:32), [MVP.md](/docs/02_produto/MVP.md:66), [MVP.md](/docs/02_produto/MVP.md:618).
  Status: `coberta`

- `PF 81` Sem arquitetura complexa.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:57), [MVP.md](/docs/02_produto/MVP.md:59), [MVP.md](/docs/02_produto/MVP.md:618).
  Status: `coberta`

- `PF 82` Sem microservicos.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:42), [MVP.md](/docs/02_produto/MVP.md:57).
  Status: `coberta`

- `PF 83` Sem visao computacional.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:45), [MVP.md](/docs/02_produto/MVP.md:94), [MVP.md](/docs/02_produto/MVP.md:264).
  Status: `coberta`

- `PF 84` Sem IA analisando video automaticamente.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:46), [MVP.md](/docs/02_produto/MVP.md:95), [MVP.md](/docs/02_produto/MVP.md:266).
  Status: `coberta`

- `PF 86` `8. Escopo Obrigatorio do MVP`
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:73).
  Status: `coberta`

- `PF 87` O MVP deve conter apenas:
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:75) reproduz a mesma intencao, mas [MVP.md](/docs/02_produto/MVP.md:88) adiciona `referencia manual de video`.
  Status: `parcial`

- `PF 88` Registro de jogos.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:80), [MVP.md](/docs/02_produto/MVP.md:181), [MVP.md](/docs/02_produto/MVP.md:477), [MVP.md](/docs/02_produto/MVP.md:566).
  Status: `coberta`

- `PF 89` Registro de treinos.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:81), [MVP.md](/docs/02_produto/MVP.md:168), [MVP.md](/docs/02_produto/MVP.md:476).
  Status: `coberta`

- `PF 90` Registro de presenca.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:82), [MVP.md](/docs/02_produto/MVP.md:196), [MVP.md](/docs/02_produto/MVP.md:478).
  Status: `coberta`

- `PF 91` Registro de scout.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:83), [MVP.md](/docs/02_produto/MVP.md:210), [MVP.md](/docs/02_produto/MVP.md:487).
  Status: `coberta`

- `PF 92` Historico por atleta.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:84), [MVP.md](/docs/02_produto/MVP.md:223), [MVP.md](/docs/02_produto/MVP.md:498), [MVP.md](/docs/02_produto/MVP.md:583).
  Status: `coberta`

- `PF 93` Historico por competicao.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:85), [MVP.md](/docs/02_produto/MVP.md:234), [MVP.md](/docs/02_produto/MVP.md:499), [MVP.md](/docs/02_produto/MVP.md:590).
  Status: `coberta`

- `PF 94` Relatorios basicos.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:86), [MVP.md](/docs/02_produto/MVP.md:243), [MVP.md](/docs/02_produto/MVP.md:423), [MVP.md](/docs/02_produto/MVP.md:509).
  Status: `coberta`

- `PF 95` Comparacoes basicas.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:87), [MVP.md](/docs/02_produto/MVP.md:221), [MVP.md](/docs/02_produto/MVP.md:452), [MVP.md](/docs/02_produto/MVP.md:510).
  Status: `coberta`

- `PF 97` `9. Fora de Escopo`
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:90).
  Status: `coberta`

- `PF 98` Visao computacional.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:45), [MVP.md](/docs/02_produto/MVP.md:94), [MVP.md](/docs/02_produto/MVP.md:264).
  Status: `coberta`

- `PF 99` Reconhecimento automatico de jogadas.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:94), [MVP.md](/docs/02_produto/MVP.md:265).
  Status: `coberta`

- `PF 100` IA analisando videos.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:46), [MVP.md](/docs/02_produto/MVP.md:95), [MVP.md](/docs/02_produto/MVP.md:266).
  Status: `coberta`

- `PF 101` Dashboards complexos.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:47), [MVP.md](/docs/02_produto/MVP.md:99).
  Status: `coberta`

- `PF 102` Predicoes.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:48), [MVP.md](/docs/02_produto/MVP.md:96).
  Status: `coberta`

- `PF 104` `10. Criterios de Aceitacao`
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:545).
  Status: `coberta`

- `PF 105` MVP valido apenas se:
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:547) e [MVP.md](/docs/02_produto/MVP.md:560).
  Status: `coberta`

- `PF 106` Registrar jogos sem falhas.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:549), [MVP.md](/docs/02_produto/MVP.md:562), [MVP.md](/docs/02_produto/MVP.md:566).
  Status: `coberta`

- `PF 107` Comparar jogos.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:550), [MVP.md](/docs/02_produto/MVP.md:572), [MVP.md](/docs/02_produto/MVP.md:576).
  Status: `coberta`

- `PF 108` Gerar historico por atleta.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:551), [MVP.md](/docs/02_produto/MVP.md:579), [MVP.md](/docs/02_produto/MVP.md:583).
  Status: `coberta`

- `PF 109` Gerar historico coletivo.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:552), [MVP.md](/docs/02_produto/MVP.md:586), [MVP.md](/docs/02_produto/MVP.md:590).
  Status: `parcial`

- `PF 110` Preservar dados.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:553), [MVP.md](/docs/02_produto/MVP.md:593), [MVP.md](/docs/02_produto/MVP.md:597), [MVP.md](/docs/02_produto/MVP.md:599).
  Status: `coberta`

- `PF 111` Reduzir dependencia da memoria humana.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:554), [MVP.md](/docs/02_produto/MVP.md:601), [MVP.md](/docs/02_produto/MVP.md:605).
  Status: `coberta`

- `PF 112` Reduzir carga operacional.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:555), [MVP.md](/docs/02_produto/MVP.md:608), [MVP.md](/docs/02_produto/MVP.md:612).
  Status: `parcial`

- `PF 113` Ser operavel por uma unica pessoa.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:556), [MVP.md](/docs/02_produto/MVP.md:614), [MVP.md](/docs/02_produto/MVP.md:618).
  Status: `coberta`

- `PF 115` `11. Limites do que a IA Pode Assumir`
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:38), [MVP.md](/docs/02_produto/MVP.md:621).
  Status: `coberta`

- `PF 116` A IA NAO pode assumir:
  Evidencia no MVP: restricoes e riscos em [MVP.md](/docs/02_produto/MVP.md:40) e [MVP.md](/docs/02_produto/MVP.md:623).
  Status: `coberta`

- `PF 117` O problema nao e analise automatica de video.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:35), [MVP.md](/docs/02_produto/MVP.md:95), [MVP.md](/docs/02_produto/MVP.md:262).
  Status: `coberta`

- `PF 118` O MVP nao precisa de Machine Learning.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:96), [MVP.md](/docs/02_produto/MVP.md:623).
  Status: `coberta`

- `PF 119` O MVP nao precisa de Computer Vision.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:45), [MVP.md](/docs/02_produto/MVP.md:94).
  Status: `coberta`

- `PF 120` O MVP nao precisa de nuvem complexa.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:44), [MVP.md](/docs/02_produto/MVP.md:57), [MVP.md](/docs/02_produto/MVP.md:618).
  Status: `coberta`

- `PF 121` O MVP nao precisa de arquitetura distribuida.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:43), [MVP.md](/docs/02_produto/MVP.md:57), [MVP.md](/docs/02_produto/MVP.md:619).
  Status: `coberta`

- `PF 122` Nao misturar regras de handebol de quadra e areia.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:30) define dominio exclusivo, e [MVP.md](/docs/02_produto/MVP.md:49) proibe misturar regras, mas nao detalha regras especificas.
  Status: `parcial`

- `PF 124` `12. Pergunta Final para a IA`
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:51) e [MVP.md](/docs/02_produto/MVP.md:460) respondem a pergunta final.
  Status: `coberta`

- `PF 125` Arquitetura de menor risco, menor manutencao e maior chance de sucesso incremental e validavel.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:55), [MVP.md](/docs/02_produto/MVP.md:66), [MVP.md](/docs/02_produto/MVP.md:460), [MVP.md](/docs/02_produto/MVP.md:547).
  Status: `coberta`

- `PF 126` Solucao incremental, validavel, de menor risco e compativel com treinador solo.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:14), [MVP.md](/docs/02_produto/MVP.md:29), [MVP.md](/docs/02_produto/MVP.md:460), [MVP.md](/docs/02_produto/MVP.md:560), [MVP.md](/docs/02_produto/MVP.md:618).
  Status: `coberta`

- `PF 128` `---`
  Evidencia no MVP: separador estrutural.
  Status: `estrutural`

- `PF 130` `13. Criterios de Manutencao do PROBLEMA_FINAL`
  Evidencia no MVP: governanca do SSOT, nao um requisito diretamente resolvido pelo MVP.
  Status: `estrutural`

- `PF 132` Documento deve ser atualizado quando houver mudanca relevante.
  Evidencia no MVP: nao ha regra de manutencao do SSOT dentro do MVP.
  Status: `sem cobertura`

- `PF 134` Problema central.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:631) trata definicao de sucesso e resposta ao problema central, mas nao estabelece gatilho de manutencao.
  Status: `parcial`

- `PF 135` Causa raiz.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:66) explicita causa raiz, mas nao regra de manutencao.
  Status: `parcial`

- `PF 136` Restricao operacional.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:38) cobre a restricao, mas nao a regra de atualizar o SSOT quando ela mudar.
  Status: `parcial`

- `PF 137` Escopo obrigatorio do MVP.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:73) cobre o escopo, mas nao a manutencao do SSOT.
  Status: `parcial`

- `PF 138` Fora de escopo.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:90) cobre o conteudo, mas nao a regra de manutencao do SSOT.
  Status: `parcial`

- `PF 139` Criterio de aceitacao.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:545) cobre o conteudo, mas nao a regra de manutencao do SSOT.
  Status: `parcial`

- `PF 140` Limite do que a IA pode assumir.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:38) e [MVP.md](/docs/02_produto/MVP.md:621) cobrem os limites, mas nao a regra de manutencao.
  Status: `parcial`

- `PF 141` Decisao humana que altere prioridade do projeto.
  Evidencia no MVP: nao ha regra de governanca ou versionamento de prioridade.
  Status: `sem cobertura`

- `PF 142` Evidencia nova que mude entendimento do problema.
  Evidencia no MVP: nao ha regra de manutencao baseada em nova evidencia.
  Status: `sem cobertura`

- `PF 144` Se nao mudar o entendimento, registrar em documento operacional apropriado.
  Evidencia no MVP: nao ha instrucao equivalente.
  Status: `sem cobertura`

- `PF 146` `---`
  Evidencia no MVP: separador estrutural.
  Status: `estrutural`

- `PF 148` `14. Criterios de Uso pela IA`
  Evidencia no MVP: principios, restricoes, riscos e proximos passos se alinham a esse uso.
  Status: `coberta`

- `PF 150` IA deve usar este documento como entrada principal.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:5).
  Status: `coberta`

- `PF 152` A IA deve:
  Evidencia no MVP: linhas seguintes detalham os mesmos guardrails.
  Status: `coberta`

- `PF 154` Preservar contexto de treinador solo.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:29), [MVP.md](/docs/02_produto/MVP.md:106), [MVP.md](/docs/02_produto/MVP.md:618).
  Status: `coberta`

- `PF 155` Preservar dominio de handebol de areia.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:30), [MVP.md](/docs/02_produto/MVP.md:49).
  Status: `coberta`

- `PF 156` Respeitar MVP simples e de baixa manutencao.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:31), [MVP.md](/docs/02_produto/MVP.md:32), [MVP.md](/docs/02_produto/MVP.md:57), [MVP.md](/docs/02_produto/MVP.md:75).
  Status: `coberta`

- `PF 157` Priorizar reducao de carga operacional.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:12), [MVP.md](/docs/02_produto/MVP.md:70), [MVP.md](/docs/02_produto/MVP.md:397), [MVP.md](/docs/02_produto/MVP.md:612).
  Status: `coberta`

- `PF 158` Propor solucoes incrementais e validaveis.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:14), [MVP.md](/docs/02_produto/MVP.md:33), [MVP.md](/docs/02_produto/MVP.md:460), [MVP.md](/docs/02_produto/MVP.md:560).
  Status: `coberta`

- `PF 159` Separar claramente diagnostico, requisito, arquitetura e implementacao.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:16), [MVP.md](/docs/02_produto/MVP.md:38), [MVP.md](/docs/02_produto/MVP.md:73), [MVP.md](/docs/02_produto/MVP.md:460).
  Status: `coberta`

- `PF 160` Declarar lacunas antes de assumir funcionalidades nao descritas.
  Evidencia no MVP: o documento usa `se necessario`, mantem fora de escopo e lista riscos em [MVP.md](/docs/02_produto/MVP.md:158), [MVP.md](/docs/02_produto/MVP.md:262), [MVP.md](/docs/02_produto/MVP.md:621), mas nao declara um protocolo explicito de lacunas.
  Status: `parcial`

- `PF 162` A IA nao deve:
  Evidencia no MVP: restricoes e riscos em [MVP.md](/docs/02_produto/MVP.md:40) e [MVP.md](/docs/02_produto/MVP.md:623).
  Status: `coberta`

- `PF 164` Transformar problema em visao computacional.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:45), [MVP.md](/docs/02_produto/MVP.md:94).
  Status: `coberta`

- `PF 165` Propor automacao de video no MVP.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:35), [MVP.md](/docs/02_produto/MVP.md:252), [MVP.md](/docs/02_produto/MVP.md:262), [MVP.md](/docs/02_produto/MVP.md:624).
  Status: `coberta`

- `PF 166` Propor arquitetura complexa sem necessidade comprovada.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:57), [MVP.md](/docs/02_produto/MVP.md:66), [MVP.md](/docs/02_produto/MVP.md:618).
  Status: `coberta`

- `PF 167` Misturar regras de quadra com areia.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:30), [MVP.md](/docs/02_produto/MVP.md:49).
  Status: `parcial`

- `PF 168` Tratar solucao aspiracional como requisito validado.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:547) e [MVP.md](/docs/02_produto/MVP.md:560) exigem validacao, mas nao ha formula explicita contra aspiracionalismo.
  Status: `parcial`

- `PF 169` Ignorar validacao humana do treinador.
  Evidencia no MVP: ha validacao de fluxo e aceitacao em [MVP.md](/docs/02_produto/MVP.md:468), [MVP.md](/docs/02_produto/MVP.md:480), [MVP.md](/docs/02_produto/MVP.md:560), mas nao ha referencia textual explicita a validacao humana do treinador.
  Status: `parcial`

- `PF 171` `---`
  Evidencia no MVP: separador estrutural.
  Status: `estrutural`

- `PF 173` `15. Criterio de Prontidao para Uso em IA`
  Evidencia no MVP: o documento tenta satisfazer esses requisitos, mas nao afirma formalmente prontidao para IA.
  Status: `parcial`

- `PF 175` Documento pronto quando atender simultaneamente aos criterios abaixo.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:547) trabalha com satisfacao simultanea de criterios de aceitacao, analogamente.
  Status: `parcial`

- `PF 177` Problema central esta explicito.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:66), [MVP.md](/docs/02_produto/MVP.md:631).
  Status: `coberta`

- `PF 178` Causas raiz separadas dos sintomas.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:66) explicita causa raiz, mas nao separa formalmente causas e sintomas com a mesma estrutura do SSOT.
  Status: `parcial`

- `PF 179` Restricoes reais estao declaradas.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:38).
  Status: `coberta`

- `PF 180` O MVP esta delimitado.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:73) e [MVP.md](/docs/02_produto/MVP.md:90).
  Status: `coberta`

- `PF 181` O fora de escopo esta explicito.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:90).
  Status: `coberta`

- `PF 182` Criterios de aceitacao sao verificaveis.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:545), [MVP.md](/docs/02_produto/MVP.md:558).
  Status: `parcial`

- `PF 183` Limites da IA estao declarados.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:38), [MVP.md](/docs/02_produto/MVP.md:621).
  Status: `coberta`

- `PF 184` Pergunta final orienta solucao incremental, validavel e de menor risco.
  Evidencia no MVP: [MVP.md](/docs/02_produto/MVP.md:55), [MVP.md](/docs/02_produto/MVP.md:460), [MVP.md](/docs/02_produto/MVP.md:560).
  Status: `coberta`

- `PF 186` Status atual: pronto_para_uso_com_ia.
  Evidencia no MVP: nao ha declaracao equivalente de prontidao formal.
  Status: `sem cobertura`

## Sintese dos Gaps Reais

As linhas do `PROBLEMA_FINAL.md` que ainda nao encontram evidencia suficiente no `MVP.md`, ou que encontram apenas evidencia parcial relevante, se concentram em cinco grupos:

1. governanca do proprio SSOT:
   `PF 132`, `PF 141`, `PF 142`, `PF 144`, `PF 186`.

2. desvio de escopo no MVP:
   `PF 87` esta apenas parcialmente coberta porque o `MVP.md` adiciona `referencia manual de video` como item obrigatorio em [MVP.md](/docs/02_produto/MVP.md:88), embora isso nao conste no escopo obrigatorio do SSOT.

3. provas ainda incompletas:
   `PF 109`, `PF 112`, `PF 182` continuam apenas parciais porque as evidencias de historico coletivo, reducao de carga operacional e verificabilidade ainda nao estao fechadas com criterios suficientemente objetivos.

4. cobertura indireta de fontes legadas:
   `PF 36`, `PF 37`, `PF 38`, `PF 39`, `PF 48`, `PF 49`, `PF 50` estao apenas parcialmente cobertas porque o MVP fala em centralizacao, mas nao define estrategia de absorcao das fontes legadas.

5. cobertura parcial do tema video:
   `PF 28`, `PF 57`, `PF 68` estao parcialmente cobertas porque o MVP corretamente rebaixa video para referencia manual, mas isso nao resolve integralmente a dor operacional de producao de video descrita no problema.

## Conclusao

O `MVP.md` cobre a maior parte do problema estrutural, das restricoes e do escopo funcional central do SSOT. Os principais pontos que ainda impedem alinhamento total sao:

- excesso de obrigatoriedade dado ao modulo de referencia de video;
- prova fraca para historico coletivo e reducao de carga operacional;
- ausencia de governanca explicita sobre manutencao do SSOT;
- cobertura apenas indireta das fontes legadas e do trabalho com video.
