---
doc_type: source_primary
derived: false
should_be_derived: false
status: current
governed_by: null
generated_by: null
audited_by: auditoria_python_ontologia/audit_ontology_pipeline.py
last_audit_report: results_auditoria_python/07_blockers_report.md
superseded_by: null
last_reviewed: "2026-06-22"
---

SCOUT_BEACHHANDBALL | v0.0.1 | ATIVO | 2026-06-19 | AI_AGENT_ASSISTANT
Protocolo de Execução
Ciclo (Obrigatório antes de qualquer ação): Leitura do Handoff, acesso ao documento SCOUT_BEACHHANDBALL.gdoc  e confirmação de estado real nas abas (Governança, Rastreabilidade, Decisões, Bloco Atual).
Execução: Processar estritamente a próxima etapa autorizada. Atualizar a checklist (status, evidência, pendências) e o Handoff (etapas, decisões, próximo gate) ao final de cada ciclo.
Regras Absolutas: Proibição de inferências ou conclusões sem validadores completos. Em caso de dúvida, manter como RASCUNHO.

Checklist mínima que a IA deve atualizar sempre
O Handoff MUST deve ser o marcador mestre.
A checklist MUST ser o controle de execução.
A rastreabilidade MUST ser a prova.
A decisão humana MUST  ser o gate de validação.
Cada fase MUST ter estes campos:

```yaml
fase:
  nome:
  status:
  tarefa_atual:
  checklist:
    - item:
      status:
      evidencia:
      pendencia:
  decisao_humana:
    id:
    status:
    data:
  proximo_gate:
  proximo_ponto_exato:
```



Prompt de comando recomendado
[SISTEMA DE PROTOCOLO OPERACIONAL - REGRAS]
Você opera sob um regime de  Máquina de Estados de Ciclo Fechado. Seu comportamento é estritamente governado pelo Handoff e pela Checklist. Você não possui autonomia para decidir o próximo passo além do que está explicitamente autorizado.

1. BLOQUEIO DE ENTRADA (OBRIGATÓRIO ANTES DE QUALQUER AÇÃO)
Antes de processar qualquer pedido ou gerar qualquer análise, você MUST executar os seguintes passos na ordem exata:
Ler o HANDOFF OPERACIONAL ATUAL em formato YAML posicionado no topo do arquivo.
Abrir o documento REGRAS através do link registrado no handoff.
Confirmar o estado real dos dados cruzando as informações das abas: Governança, Rastreabilidade, Decisões Humanas e a aba do bloco atual em execução.
Localizar o campo exato proximo_ponto_exato no Handoff. 

Você MUST iniciar exatamente dali.
2. REGRAS ABSOLUTAS DE EXECUÇÃO (MUST)
- MUST NOT inferir ou deduzir etapas posteriores. Se a etapa atual não possuir evidência ou decisão humana aprovada, você está bloqueado de avançar.
- MUST NOT declarar conclusão integral do projeto sem que todos os validadores, apêndices e a comparação final estejam 100% concluídos.
- ANTI-ALUCINAÇÃO: Proibido inventar limiares, critérios automáticos, exceções, punições ou regras ausentes da fonte primária. Na dúvida, marque como RASCUNHO ou CATEGORIA_CONTROLADA_COM_AVALIAÇÃO_HUMANA..
3. BLOQUEIO DE SAÍDA (OBRIGATÓRIO AO FINAL DE TODO CICLO)
Para garantir que o arquivo não vire memória desatualizada, sua resposta **DEVE OBRIGATORIAMENTE** seguir e preencher a estrutura XML abaixo. Você não pode emitir texto livre fora ou após essa estrutura.

```xml
<execucao_ciclo>
    <etapa_executada>Nome da etapa exata que foi processada agora</etapa_executada>
   
    <evidencia_verificavel>Link, referência interna ou prova documental do que foi feito</evidencia_verificavel>
   
    <decisao_humana_registrada>ID, Status e Data da validação humana (se houver)</decisao_humana_registrada>
   
    <pendencias_abertas>Listar travas ou itens não resolvidos neste ciclo</pendencias_abertas>

    <checklist_atualizada_fase>
        <!-- Você MUST atualizar a checklist da fase correspondente aqui -->
        fase:
          nome:
          status:
          tarefa_atual:
          checklist:
            - item:
              status:
              evidencia:
              pendencia:
          decisao_humana:
            id:
            status:
            data:
          proximo_gate:
          proximo_ponto_exato:
    </checklist_atualizada_fase>

    <handoff_operacional_atualizado>
        <!-- Você MUST atualizar o Handoff Mestre em formato YAML aqui -->
        handoff:
          ultima_etapa_concluida:
          ultima_decisao_humana:
          proximo_point_exato_continuacao:
          proximo_gate_obrigatorio:
          status_validacao_automatizada:
          status_projeto_integral:
          link_documento_regras: "Confirmar se o link permanece vinculado no topo"
    </handoff_operacional_atualizado>

    <confirmacao_estado_real>Confirmo que o Handoff e a Checklist foram atualizados ao final deste ciclo e refletem o estado real das abas.</confirmacao_estado_real>
</execucao_ciclo>
```



```md
TAREFA: Executar continuidade operacional do projeto REGRAS.
ANTES DE QUALQUER AÇÃO:
1. Acesse o arquivo de Checklist/Protocolo Operacional.
2. Leia o Painel de Controle Operacional.
3. Leia integralmente o HANDOFF OPERACIONAL ATUAL em YAML.
4. Acesse o documento REGRAS pelo link registrado no handoff.
5. Confirme o estado real nas abas Governança, Rastreabilidade, Decisões Humanas e na aba do bloco atual.

REGRA DE CONTINUIDADE:
A IA deve continuar exatamente no campo proximo_ponto_exato do handoff.
A IA não pode escolher outra etapa por inferência.
A IA não pode avançar para a etapa posterior sem gate cumprido.

REGRA DE EXECUÇÃO: 
Para cada bloco normativo:
1. Extrair a fonte primária.
2. Formalizar em afirmações atômicas rastreáveis.
3. Marcar conceitos subjetivos como CATEGORIA_CONTROLADA_COM_AVALIAÇÃO_HUMANA.
4. Inserir como RASCUNHO.
5. Atualizar Governança.
6. Atualizar Rastreabilidade.
7. Solicitar decisão humana explícita.
8. Após aprovação humana, registrar a decisão.
9. Alterar status para VALIDADO ou CONCLUÍDA_E_VALIDADA.
10. Liberar a próxima etapa somente após o gate.

REGRA ANTI-ALUCINAÇÃO:
A IA não pode inventar limiares, critérios automáticos, exceções, punições, interpretações, regras ou status ausentes da fonte ou sem decisão humana.
Em caso de dúvida, manter o item como RASCUNHO ou CATEGORIA_CONTROLADA_COM_AVALIAÇÃO_HUMANA.

ATUALIZAÇÃO OBRIGATÓRIA AO FINAL:
Antes de encerrar a resposta, atualize o arquivo de Checklist/Protocolo Operacional:
1. Atualize o Painel de Controle Operacional.
2. Atualize o HANDOFF OPERACIONAL ATUAL em YAML.
3. Atualize a Matriz Operacional da fase executada.
4. Registre evidência verificável para cada item concluído.
5. Registre pendências abertas.
6. Registre o próximo ponto exato de continuação.
7. Confirme se o documento REGRAS continua vinculado no topo do arquivo.

SAÍDA ESPERADA:
Responder com:
- etapa executada;
- evidência registrada;
- status atualizado;
- decisão humana registrada, se houver;
- próximo ponto exato de continuação;
- pendências abertas;
- confirmação de que o handoff foi atualizado.
```
Veredito
O comando que garante funcionamento real é aquele que obriga a IA a:
ler handoff → confirmar estado real → executar só o próximo ponto autorizado → atualizar checklist → atualizar handoff → registrar evidência.
Sem essa obrigação no prompt, o handoff pode ficar bonito, mas desatualizado. Com essa obrigação, o arquivo passa a funcionar como um controle operacional real.

Protocolo Operacional de Implementação Semântica
Painel de Controle Operacional
Link obrigatório para REGRAS: Regras 
Status geral: Regras 1 a 18 CONCLUÍDA_E_VALIDADA por decisão humana.
Próxima etapa autorizada: Apêndices.
Validação automatizada: VALIDAÇÃO_AUTOMATIZADA_PENDENTE.
Regra de avanço: nenhuma fase avança sem evidência verificável, atualização da rastreabilidade e decisão humana quando houver categoria controlada.

MUST ATUALIZAR HANDOFF OPERACIONAL 

```yaml
handoff_operacional:
  documento_regras:
    nome: "REGRAS"  
    - url: "https://docs.google.com/document/d/18mFFpbU4ge9IjW1Hjl_EoP57o9coHJwoYgiPBC1tnGc/edit?usp=sharing"

  estado_atual:
    ultima_etapa_concluida: "Regras 1 a 18 formalizadas, rastreadas e validadas por decisão humana"
    ultima_decisao_humana: "APP-F-CAT-2026-06-19"
    status_regras_1_a_18: "CONCLUÍDA_E_VALIDADA"
    status_apendices: "RASCUNHO_EM_ANDAMENTO"

    status_app_a: "CONCLUÍDA_E_VALIDADA" 
    status_app_b: "CONCLUÍDA_E_VALIDADA" 
    status_app_c: "CONCLUÍDA_E_VALIDADA"

    status_app_d: "CONCLUÍDA_E_VALIDADA" 
    status_app_e: "CONCLUÍDA_E_VALIDADA" 
    status_app_f: "CONCLUÍDA_E_VALIDADA"  status_validacao_automatizada: "VALIDAÇÃO_AUTOMATIZADA_PENDENTE"
    status_projeto_integral: "NÃO_CONCLUÍDO"

  proximo_ponto_exato:
    documento: "REGRAS"
    aba: "Apêndices"
    acao: "Executar validação automatizada integral das Regras e Apêndices"
    formato_saida: "afirmações atômicas rastreáveis"

    pendencia_aberta: "nenhuma pendência humana aberta para APP-F"
  gate_obrigatorio:
    regra: "Nenhum Apêndice pode receber VALIDADO sem decisão humana explícita"
    exige_rastreabilidade: true
    exige_atualizacao_governanca: true
    exige_decisao_humana_para_categoria_controlada: true

  regra_anti_alucinacao:
    proibido_inventar:
      - "limiares"
      - "critérios automáticos"
      - "exceções"
      - "punições"
      - "interpretações ausentes da fonte IHF"
    em_caso_de_duvida: "manter como RASCUNHO ou CATEGORIA_CONTROLADA_COM_AVALIAÇÃO_HUMANA"

  terminologia:
    termo_canonico: "Período"
    termo_proibido: "Set"
```


Matriz Operacional — Plano, Checklist e Evidência por Fase
Cada fase deve conter tarefa, checklist, evidência verificável, critério de aceite, status e gate de avanço.
Fase 1 — Governança e Escopo
Tarefa: congelar fonte normativa e separar regimes temporais.
Checklist: fonte registrada; metadados registrados; regimes temporais separados; termo Período adotado; ocorrência de Set tratada como erro terminológico salvo citação literal.
Evidência verificável: link para REGRAS; metadados da fonte; hash; páginas; data de vigência; aba Governança.
Critério de aceite: fonte rastreável e regime temporal explícito antes de qualquer formalização.

1. Congelar a fonte normativa: Registrar metadados e identificadores.
2. Separar regimes temporais: Configurar perfis REGIME_ATUAL e REGIME_2026_07_01.
Fase 2 — Framework Linguístico e Ontológico
Tarefa: controlar linguagem, vocabulário, taxonomia e propriedades.
Checklist: gramática definida; vocabulário canônico registrado; classes separadas; propriedades de dados descritas; termos controlados listados.
Evidência verificável: aba Vocabulário e Taxonomia; lista de termos; lista de status; lista de modalidades normativas.
Critério de aceite: nenhum termo novo pode ser usado como verdade sem constar no vocabulário ou sem decisão humana.

Definir linguagem controlada: Gramática e padrões de escrita.
Construir vocabulário canônico: Dicionário "um conceito → um termo".
Criar taxonomia: Estruturar classes, eventos e estados.
Criar esquema de propriedades de dados: Metadados para medidas.

Fase 3 — Formalização Normativa
Tarefa: transformar fonte em afirmações atômicas rastreáveis.
Checklist: texto extraído; regra ou apêndice identificado; afirmações criadas; exceções separadas; categorias subjetivas marcadas.
Evidência verificável: statement_id; source_rule; source_page; controlled_statement; total de afirmações; status RASCUNHO.
Critério de aceite: nenhuma afirmação sem fonte ou sem decisão humana registrada.
7. Decompor PDF em unidades normativas: Processar parágrafos de forma atômica.
8. Formalizar regras condicionais: Fatos geradores, condições e consequências.
9. Formalizar exceções: Vínculo explícito à regra geral.
10. Resolver conceitos subjetivos: Protocolo de decisão para termos ambíguos.

Fase 4 — Estruturação e Rastreabilidade
Tarefa: registrar vínculo entre fonte, afirmação, decisão humana e status.
Checklist: rastreabilidade atualizada; total de afirmações registrado; status registrado; decisão humana vinculada quando existir.
Evidência verificável: aba Rastreabilidade; ID da decisão humana; página de origem; status de validação.
Critério de aceite: bloco sem rastreabilidade não pode ser validado.
11. Criar matriz de rastreabilidade: Configurar tabela com status de validação.
12. Definir estrutura do Google Docs: tratar as 14 seções como estrutura conceitual e usar abas operacionais para execução.


Fase 5 — Validação Automatizada
Tarefa: executar validadores sintáticos e semânticos quando implementados.
Checklist: pronomes verificados; termos verificados; números com unidade e tipo de dado; regras com fonte; categorias subjetivas com status controlado.
Evidência verificável: relatório de validação; lista de erros; lista de correções; status  VALIDAÇÃO_AUTOMATIZADA_PENDENTE ou concluído.
13. Implementar verificações automáticas: Validadores sintáticos e semânticos.
14. Criar testes semânticos: Desenvolver casos de teste (positivo/negativo).
Critério de aceite: enquanto validadores não forem executados, não declarar conclusão integral do projeto.

Fase 6 — Validação Humana e Execução Controlada
Tarefa: validar por regra, apêndice ou bloco normativo fechado.
Checklist: categorias controladas listadas; aprovação humana explícita; decisão humana registrada; status alterado para VALIDADO; próxima etapa liberada.
Evidência verificável: aba Decisões Humanas; ID da decisão; data; escopo; status APROVADA.
Critério de aceite: somente conteúdo aprovado por decisão humana pode receber CONCLUÍDA_E_VALIDADA.
15. Realizar validação humana por regra, apêndice ou bloco normativo fechado: nenhum bloco recebe VALIDADO sem decisão humana explícita.
16. Escrever e verificar o Google Docs: Inserção final e conferência.
Critérios de Aceitação (Validação Final)
Toda disposição do PDF foi representada ou justificada como não ontologizável.
Cada afirmação possui origem rastreável (referência à fonte).
Nenhuma decisão técnica foi inventada pela IA.
Todas as pendências subjetivas possuem decisão humana documentada.
As regras estão corretamente separadas entre REGIME_ATUAL e REGIME_2026_07_01.
Todos os validadores sintáticos e semânticos foram aprovados.

O documento de destino “Regras” já contém as Regras 1 a 18 formalizadas, rastreadas e validadas por decisão humana. A próxima etapa autorizada é a formalização dos Apêndices, mantendo o mesmo fluxo de rascunho, aprovação humana, validação e rastreabilidade.
Veredito
Não é seguro copiar ou simplesmente reescrever o PDF diretamente. A transformação exige um pipeline de engenharia semântica com rastreabilidade, decisões humanas e validação automática.
Os critérios apresentados ainda possuem conflitos internos que precisam ser resolvidos antes da escrita:
“Uma afirmação por frase” conflita com condicionais que contêm vários antecedentes.
O “mundo fechado” conflita com regras da IHF que dependem do julgamento do árbitro.
A exclusão de termos subjetivos exige critérios mensuráveis que o PDF não fornece.
O exemplo utiliza “set”, mas o termo oficial do PDF é “período”.
O PDF não estabelece automaticamente que qualquer rotação corporal de 360 graus produz um gol de dois pontos. A regra oficial trata de gol criativo ou espetacular e exige julgamento.
Os trechos amarelos somente entram em vigor em 1º de julho de 2026. Eles não podem ser misturados às regras atualmente vigentes sem marcação temporal.
Ações necessárias
1. Congelar a fonte normativa
Registrar:
documento: IHF Rules of the Game – Beach Handball;
edição: 1º de março de 2026;
quantidade: 67 páginas;
hash SHA-256 do arquivo;
idioma original: inglês;
data de vigência de cada disposição;
página, regra, item e parágrafo de origem.
Cada afirmação produzida deve possuir um identificador da fonte, como:
IHF-2026-R09-02-P21
2. Separar os regimes temporais
Criar dois perfis normativos:
REGIME_ATUAL: regras vigentes até 30 de junho de 2026;
REGIME_2026_07_01: regras vigentes a partir de 1º de julho de 2026.
Cada regra destacada em amarelo deve possuir:
status_normativo;
data_inicio_vigencia;
regra_substituida, quando aplicável.
3. Definir a linguagem controlada
Antes da redação, congelar uma gramática formal.
Estruturas permitidas:
[Classe] é_um [Classe].
[Entidade] possui [Entidade].
[Agente] executa [Ação].
[Evento] marca_pontuação [Quantidade].
[Entidade] não_pode_executar [Ação].
Se [Condição], então [Consequência].
Também será necessário definir:
lista fechada de verbos relacionais;
lista de pronomes proibidos;
lista de conectores proibidos;
padrão de capitalização;
padrão para nomes compostos;
estrutura formal das negações;
estrutura formal das exceções.
4. Construir o vocabulário canônico
Criar um dicionário “um conceito → um termo”.
Exemplos iniciais:
Partida;
Período;
Equipe;
Atleta;
Jogador de Linha;
Goleiro;
Oficial de Equipe;
Árbitro;
Cronometrista;
Secretário;
Quadra de Jogo;
Área de Jogo;
Área de Gol;
Área de Substituição;
Bola;
Gol;
Gol de Ouro;
Shoot-out;
Tiro de Árbitro;
Lateral;
Tiro de Goleiro;
Tiro Livre;
Tiro de 6 Metros;
Suspensão;
Desqualificação.
Set é TERMO_PROIBIDO. Período é TERMO_CANÔNICO. Qualquer ocorrência de set deve ser marcada como erro terminológico, exceto citação literal da fonte original acompanhada de nota.
5. Criar a taxonomia
Separar formalmente:
classes;
subclasses;
instâncias;
propriedades de objeto;
propriedades de dados;
restrições;
eventos;
infrações;
punições;
exceções;
estados temporais.
Exemplo:
Goleiro é_um Atleta.
Jogador de Linha é_um Atleta.
Goleiro é_disjunto_de Jogador de Linha quando a função está ativa.

A disjunção deve considerar função ativa, porque o mesmo atleta pode alternar entre Goleiro e Jogador de Linha.
6. Criar o esquema de propriedades de dados
Toda medida deve possuir:
valor;
unidade;
tipo de dado;
cardinalidade;
limite inclusivo ou exclusivo.
Exemplo:
A Quadra de Jogo possui_comprimento exatamente 27 metros [decimal].
A Quadra de Jogo possui_largura exatamente 12 metros [decimal].
O Período possui_duração exatamente 10 minutos [inteiro].
A Bola Feminina possui_peso no mínimo 280 gramas [inteiro].
A Bola Feminina possui_peso no máximo 300 gramas [inteiro].

7. Decompor o PDF em unidades normativas
Processar separadamente:
filosofia e Fair Play;
Regras 1 a 18;
sinais dos árbitros;
esclarecimentos;
área de substituição;
uniformes;
areia e iluminação;
glossário.
Cada parágrafo do PDF deve gerar uma ou mais unidades atômicas. Nenhum parágrafo pode ser omitido silenciosamente.
8. Formalizar as regras condicionais
Cada regra complexa deve ser dividida em:
fatos geradores;
condições cumulativas;
exceções;
consequência esportiva;
punição pessoal;
reinício da partida.
Exemplo estrutural:
CONDIÇÃO-01: O Jogador Defensor entra_na Área de Gol.
CONDIÇÃO-02: A entrada produz_vantagem para o Jogador Defensor.
CONDIÇÃO-03: A entrada destrói Chance Clara de Gol.
CONSEQUÊNCIA-01: O Árbitro assinala Tiro de 6 Metros.

Isso resolve o conflito entre atomicidade e múltiplas condições: cada condição permanece atômica, enquanto o bloco lógico agrega as condições.
9. Formalizar exceções separadamente
Toda exceção deve possuir regra própria e vínculo explícito com a regra geral:
REGRA-GERAL: O Jogador de Linha não_pode_entrar_na Área de Gol.
EXCEÇÃO-01: O Jogador de Linha pode_entrar_na Área de Gol após jogar a Bola.
CONDIÇÃO-EXCEÇÃO-01: A entrada não produz desvantagem para a Equipe Adversária.

10. Resolver os conceitos subjetivos
O PDF contém conceitos que não podem ser transformados em medidas sem decisão humana, como:
gol criativo;
gol espetacular;
conduta antidesportiva;
conduta gravemente antidesportiva;
ação particularmente perigosa;
risco à saúde;
vantagem obtida;
perigo causado pelo clima;
desperdício de tempo;
Chance Clara de Gol.
Para cada conceito, existem somente três caminhos seguros:
utilizar a definição fechada fornecida pelo próprio PDF;
criar uma enumeração discreta de situações;
solicitar ao especialista humano critérios adicionais.
A IA não deve inventar limiares para eliminar subjetividade.
11. Criar uma matriz de rastreabilidade
Cada unidade deve conter:
Campo
Finalidade
statement_id
Identificação única
source_rule
Regra da IHF
source_page
Página do PDF
source_text
Trecho normativo de origem
controlled_statement
Frase formalizada
statement_type
Classe, propriedade, restrição ou regra
effective_date
Data de vigência
human_decision
Decisão humana necessária
validation_status
Estado da validação

12. Definir a estrutura do Google Docs
A estrutura conceitual deve conter:
identificação e autoridade da fonte;
convenções da linguagem controlada;
vocabulário canônico;
taxonomia;
propriedades de objeto;
propriedades de dados;
axiomas e disjunções;
regras formalizadas 1 a 18;
esclarecimentos formalizados;
regulamentos complementares;
glossário canônico;
matriz de rastreabilidade;
decisões humanas pendentes;
histórico de vigência.
13. Implementar verificações automáticas
Executar validadores para detectar:
frases com mais de uma afirmação;
pronomes anafóricos;
sinônimos proibidos;
verbos fora da lista permitida;
números sem unidade;
números sem tipo de dado;
limites sem “exatamente”, “no mínimo” ou “no máximo”;
condicionais sem “Se” e “então”;
exceções incorporadas de forma narrativa;
classes usadas como instâncias;
regras sem referência ao PDF;
termos subjetivos sem definição;
conflitos de vigência.
14. Criar testes semânticos
Cada regra condicional deve possuir:
caso positivo;
caso negativo;
caso de limite;
caso de exceção;
consequência esperada;
punição esperada;
forma de reinício esperada.
15. Realizar validação humana por blocos
A aprovação deve ocorrer separadamente para:
vocabulário;
taxonomia;
quadra e equipamentos;
participantes e funções;
ações permitidas;
infrações;
pontuação;
punições;
Shoot-out;
regras subjetivas;
alterações de julho de 2026.
Somente blocos aprovados podem receber o estado VALIDADO.
16. Escrever e verificar o Google Docs
Depois das aprovações:
substituir o texto provisório;
inserir o conteúdo em lotes pequenos;
reler cada lote no Google Docs;
preservar identificadores e rastreabilidade;
executar os validadores;
exportar o documento para inspeção;
comparar o resultado final com todas as 67 páginas.
Critério final de conclusão
O documento somente poderá ser declarado concluído quando:
cada disposição do PDF estiver representada ou justificada como não ontologizável;
cada afirmação possuir origem rastreável;
nenhuma decisão técnica tiver sido inventada pela IA;
todas as pendências subjetivas tiverem decisão humana;
as regras atuais estiverem separadas das regras de 1º de julho de 2026;
todos os validadores sintáticos e semânticos forem aprovados.
Atualização Operacional do Fluxo
Este documento passa a funcionar como protocolo operacional de formalização normativa semântica. O plano inicial continua válido como referência, mas o fluxo executável passa a obedecer aos gates abaixo.
Estado Atual do Projeto
As Regras 1 a 18 possuem status CONCLUÍDA_E_VALIDADA por decisão humana documentada.
A etapa de Apêndices possui_status PRÓXIMA_ETAPA_AUTORIZADA.
A validação automatizada possui_status VALIDAÇÃO_AUTOMATIZADA_PENDENTE.
O projeto integral não deve ser declarado concluído enquanto Apêndices, esclarecimentos, sinais dos árbitros, regulamentos complementares, glossário e validação automatizada não forem finalizados.

Fluxo Operacional Obrigatório
1. Selecionar bloco normativo fechado.
2. Extrair a fonte primária.
3. Registrar página, regra, item e trecho de origem.
4. Formalizar em afirmações atômicas rastreáveis.
5. Marcar conceitos subjetivos como CATEGORIA_CONTROLADA_COM_AVALIAÇÃO_HUMANA.
6. Inserir o bloco como RASCUNHO.
7. Atualizar Governança.
8. Atualizar Rastreabilidade.
9. Solicitar decisão humana explícita.
10. Registrar decisão humana.
11. Alterar status para VALIDADO somente após aprovação humana.
12. Liberar a próxima etapa somente depois do gate anterior.
Regra de Bloqueio por Fase
A IA não pode avançar para o próximo bloco normativo enquanto o bloco atual não estiver VALIDADO por decisão humana, salvo autorização humana explícita para trabalho paralelo. Todo avanço deve atualizar Governança e Rastreabilidade.
Tratamento de Conceitos Subjetivos
Todo conceito subjetivo deve receber o status CATEGORIA_CONTROLADA_COM_AVALIAÇÃO_HUMANA.
A IA não deve resolver conceito subjetivo, criar limiar, criar enumeração nova ou inferir critério de aplicação sem aprovação humana.
Quando a fonte não fornecer medida objetiva, o conceito deve permanecer categórico até decisão humana.
Status Permitidos
NÃO_INICIADA.
RASCUNHO.
RASCUNHO_CONCLUÍDO_AGUARDANDO_DECISÃO_HUMANA.
VALIDADO.
CONCLUÍDA_E_VALIDADA.
VALIDAÇÃO_AUTOMATIZADA_PENDENTE.
NÃO_ONTOLOGIZÁVEL_JUSTIFICADO.
PRÓXIMA_ETAPA_AUTORIZADA.
Estrutura Operacional Atual do Google Docs
A estrutura de 14 seções permanece como estrutura conceitual.
A estrutura operacional atual utiliza abas: Governança, Vocabulário e Taxonomia, Regras 1–18, Apêndices, Rastreabilidade e Decisões Humanas.
Regra Terminológica
Set é TERMO_PROIBIDO.
Período é TERMO_CANÔNICO.
Qualquer ocorrência de set deve ser marcada como erro terminológico, exceto citação literal da fonte original acompanhada de nota.
Critério de Conclusão Parcial
As Regras 1 a 18 podem ser declaradas CONCLUÍDA_E_VALIDADA por decisão humana.
A conclusão integral do projeto exige Apêndices, esclarecimentos, sinais dos árbitros, regulamentos complementares, glossário, comparação contra as 67 páginas e validação automatizada.
Critério Anti-Alucinação
Nenhuma afirmação pode ser criada sem vínculo com a fonte primária ou decisão humana registrada.
Nenhum número, tolerância, distância, exceção, consequência, punição ou critério automático pode ser inventado pela IA.
Quando houver dúvida, o status correto é RASCUNHO ou CATEGORIA_CONTROLADA_COM_AVALIAÇÃO_HUMANA, nunca VALIDADO.



