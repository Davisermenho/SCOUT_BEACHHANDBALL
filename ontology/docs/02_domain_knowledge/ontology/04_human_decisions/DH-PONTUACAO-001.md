---
id: DH-PONTUACAO-001
tipo: decisao_humana_literal
status: DH_PONTUACAO_001_RESPOSTA_HUMANA_REGISTRADA_AGUARDANDO_AUDITORIA
fonte: resposta direta do especialista humano
template_origem: DH-PONTUACAO-001_TEMPLATE.md
escopo:
  - Pontuação de gols
  - Especialista
  - Goleira
  - Jogadora comum
  - Gol simples
  - Gol de giro
  - Gol aéreo
  - Ponte aérea
  - Gol espetacular
  - Gol criativo
  - Tiro de 6 metros
  - R09-CAT-2026-06-18
nao_e_validacao_total: true
---

# DH-PONTUACAO-001 — Respostas humanas registradas literalmente

Este arquivo registra, sem reescrita, correção, resumo, harmonização ou
inferência, as respostas literais fornecidas pelo especialista do domínio
às 15 perguntas do template `DH-PONTUACAO-001_TEMPLATE.md`.

Este registro **não** constitui ficha conceitual, teste, taxonomia ou
ontologia. **Não** marca `VALIDADO_TOTAL` nem `CONSOLIDADO_VALIDO`. As
quatro fichas consolidadas, os testes de competência existentes e as
categorias de pontuação permanecem inalterados por este registro.

## respostas_literais

1. **No seu modelo, quais gols valem 1 ponto?**

   Resposta literal:
   > Os gols simples marcados por jogadoras comuns (sem colete). É aquele
   > arremesso clássico de frente, sem giro (360º) e sem receber e
   > arremessar a bola no ar (ponte aérea), feito por uma atacante que não
   > está exercendo a função de especialista.

2. **No seu modelo, quais gols valem 2 pontos?**

   Resposta literal:
   > Qualquer gol da especialista (de colete) e da goleira, os gols
   > espetaculares das jogadoras comuns. Entram nessa conta os gols de
   > ponte aérea, os gols de giro (360º) e os gols de tiro de 6 metros
   > (pênalti).

3. **Todo gol da Especialista vale 2 pontos?**

   Resposta literal:
   > Sim, por força da regra. Não importa a forma como ela arremessou. Se a
   > jogadora vestindo o colete de especialista empurrar a bola para dentro
   > do gol, mesmo que seja um chute simples de frente, o placar computará
   > 2 pontos automaticamente. Assim como os gols da goleira.

4. **Existe gol de Especialista que vale 1 ponto?**

   Resposta literal:
   > Não, no jogo corrente isso não existe. A regra da IHF protege o
   > estatuto do colete de goleiro em linha. Qualquer gol legal validado
   > para a atleta que carrega o papel tático de especialista valerá 2
   > pontos.

5. **Uma jogadora comum pode marcar gol de 2 pontos?**

   Resposta literal:
   > Sim, desde que faça uma finalização espetacular. Se a jogadora sem
   > colete fizer um gol de giro (360º) ou um gol aéreo (ponte aérea), a
   > execução técnica dela eleva o valor do gol comum de 1 para 2 pontos.

6. **Qual é a diferença entre Gol de giro e Gol espetacular?**

   Resposta literal:
   > O gol de giro é uma subclassificação do gol espetacular. Todo gol de
   > giro (360º) é considerado um gol espetacular, mas a categoria
   > "espetacular" é mais ampla e engloba outras finalizações difíceis além
   > do giro, como aérea.

7. **Qual é a diferença entre Gol aéreo e Gol espetacular?**

   Resposta literal:
   > O gol aéreo é outra subclassificação do gol espetacular. Assim como o
   > giro, a ponte aérea (receber e arremessar no ar) é o tipo de execução
   > técnica que preenche e valida a categoria mãe, que é o gol
   > espetacular.

8. **Gol criativo é categoria própria ou forma de descrever gol espetacular?**

   Resposta literal:
   > É apenas uma forma descritiva. Na ontologia e nas regras do jogo, "gol
   > criativo" não existe como classe isolada. É apenas o jargão que nós,
   > treinadores, usamos para elogiar a plástica de um gol espetacular
   > (giro ou aéreo).

9. **O valor do gol depende do Papel_Tático?**

   Resposta literal:
   > Sim, diretamente. Se o Papel_Tatico do atleta no frame do arremesso
   > for igual a Especialista, o sistema sabe que o peso base daquele gol
   > assume o valor de 2 pontos automaticamente, independentemente da
   > plasticidade do chute.

10. **O valor do gol depende do Papel_Regulamentar?**

    Resposta literal:
    > Sim, porque a regra amarra o colete ao estatuto. De acordo com as
    > regras, a jogadora de colete está atuando sob o estatuto de Goleiro
    > em Linha. A lei do jogo determina que gols marcados por quem tem o
    > direito de goleiro valem 2 pontos.

11. **O valor do gol depende da Função_Situacional?**

    Resposta literal:
    > Sim, no caso das jogadoras comuns. Se uma jogadora comum assume a
    > Funcao_Situacional de Finalizadora_de_Giro ou Finalizadora_Aerea,
    > essa função do milissegundo altera o valor final do ponto.

12. **O valor do gol depende da execução técnica?**

    Resposta literal:
    > Sim, para quem está sem colete. A física do movimento para o gol de
    > giro considera iniciar o movimento de giro com os pés apontados para o
    > gol; completar o giro de 360º no ar e arremessar, soltando a bola
    > antes de tocar com qualquer parte do corpo no solo . Para os gosl de
    > aérea, a jogadora deve receber a bola no ar sem contato com o solo e
    > arremessar soltando a bola antes de tocar qualquer parte do seu corpo
    > no chão. É o fator técnico que dita se o gol da jogadora comum valerá
    > 1 ou 2 pontos.

13. **Como R09-CAT-2026-06-18 deve ser interpretada?**

    Resposta literal:
    > Como o axioma de amarração da Regra 9 da IHF para validação de pontos
    > na temporada atual. Ela é a regra lógica que diz: se o arremesso
    > resultou em gol, o sistema deve checar se a origem foi um Tiro de 6
    > Metros (2P), se o Papel_Tatico era Especialista (2P) ou se a
    > Funcao_Situacional foi Giro/Aéreo (2P). Caso todas essas condições
    > sejam falsas, aí sim o gol é classificado como simples (1P)

14. **Quais inferências devem ser proibidas?**

    Resposta literal:
    > O sistema deve travar e apontar erro se tentar processar as seguintes
    > situações:
    >
    > * Proibir: Papel_Tatico = Atacante_Normal AND Função_Situacional =
    >   Finalização_Simples AND Valor_do_Gol = 2. (Gol comum sem efeito não
    >   dá 2 pontos).
    > * Proibir: Papel_Tatico = Especialista AND Valor_do_Gol = 1.
    >   (Especialista nunca pontua apenas 1 ponto).

15. **Quais casos de teste devem existir para validar pontuação?**

    Resposta literal:
    > O software precisa rodar obrigatoriamente estes 5 testes de
    > validação:
    >
    > * Teste 1: Atleta sem colete faz gol de frente $\rightarrow$ Sistema
    >   deve computar 1 ponto.
    > * Teste 2: Atleta sem colete faz gol de giro $\rightarrow$ Sistema
    >   deve computar 2 pontos.
    > * Teste 3: Atleta sem colete faz gol de aerea $\rightarrow$ Sistema
    >   deve computar 2 pontos.
    > * Teste 4: Atleta de colete faz gol simples de frente $\rightarrow$
    >   Sistema deve computar 2 pontos.
    > * Teste 5: Goleira oficial faz um gol direto de sua área de meta
    >   $\rightarrow$ Sistema deve computar 2 pontos (Goleiro oficial
    >   pontuando também vale 2).
    > * Teste 6: Atleta sem colete faz gol na cobrança de tiro de 6 mentro o
    >   $\rightarrow$ Sistema deve computar 2 pontos.

## decisoes_extraidas_sem_inferencia

- Gol simples de jogadora comum sem colete vale 1 ponto.
- Gol da Especialista vale 2 pontos.
- Não existe gol de Especialista valendo 1 ponto no jogo corrente.
- Gol da Goleira vale 2 pontos.
- Jogadora comum pode marcar gol de 2 pontos por execução espetacular.
- Gol de giro 360º é subclassificação de Gol_Espetacular.
- Gol aéreo / ponte aérea é subclassificação de Gol_Espetacular.
- Gol criativo não é classe isolada na ontologia nem nas regras do jogo; é descrição/jargão.
- Tiro de 6 metros vale 2 pontos.
- R09-CAT-2026-06-18 deve ser interpretada como axioma de amarração da Regra 9 da IHF para validação de pontos na temporada atual.
- A lógica declarada para pontuação é:
  1. se o arremesso resultou em gol;
  2. checar se a origem foi Tiro de 6 Metros;
  3. checar se Papel_Tatico era Especialista;
  4. checar se Funcao_Situacional foi Giro/Aéreo;
  5. se todas as condições forem falsas, classificar como gol simples de 1 ponto.

## inferencias_proibidas_declaradas

- Proibir: Papel_Tatico = Atacante_Normal AND Função_Situacional = Finalização_Simples AND Valor_do_Gol = 2.
- Proibir: Papel_Tatico = Especialista AND Valor_do_Gol = 1.

## casos_de_teste_declarados

- Teste 1: Atleta sem colete faz gol de frente → Sistema deve computar 1 ponto.
- Teste 2: Atleta sem colete faz gol de giro → Sistema deve computar 2 pontos.
- Teste 3: Atleta sem colete faz gol de aerea → Sistema deve computar 2 pontos.
- Teste 4: Atleta de colete faz gol simples de frente → Sistema deve computar 2 pontos.
- Teste 5: Goleira oficial faz um gol direto de sua área de meta → Sistema deve computar 2 pontos.
- Teste 6: Atleta sem colete faz gol na cobrança de tiro de 6 mentro o → Sistema deve computar 2 pontos.

## pontos_para_auditoria_semantica

- QTD-TESTES-001:
  descricao: "A resposta literal diz que existem 5 testes obrigatórios, mas enumera 6 testes."
  tratamento: "Não corrigir automaticamente. Levar para auditoria semântica."

- TERM-GOLEIRO-EM-LINHA-001:
  descricao: "A resposta literal usa o termo 'estatuto de Goleiro em Linha' para explicar o vínculo entre colete, regra e pontuação."
  tratamento: "Auditar contra a separação já consolidada entre Papel_Tático e Papel_Regulamentar, sem resolver por inferência."

- FUNCAO-ALTERA-VALOR-001:
  descricao: "A resposta literal afirma que Função_Situacional pode alterar o valor final do gol no caso de jogadoras comuns."
  tratamento: "Preservar como decisão de pontuação; não interpretar como alteração de Papel_Tático ou Papel_Regulamentar."

- R09-CAT-001:
  descricao: "A resposta literal define R09-CAT-2026-06-18 como axioma de amarração da Regra 9 da IHF para validação de pontos."
  tratamento: "Auditar antes de modelar regra executável."

## limites_da_decisao

- Esta decisão é registro literal de fala humana.
- Não é auditoria.
- Não é consolidação.
- Não é validação contra implementação real.
- Não cria ficha conceitual.
- Não cria taxonomia.
- Não cria ontologia.
- Não altera categorias automaticamente.
- Não autoriza VALIDADO_TOTAL.
- Não autoriza CONSOLIDADO_VALIDO.
- Não altera as quatro dimensões consolidadas.
- Não altera testes existentes.

## proxima_etapa

```yaml
proximo_ponto_exato:
  id: DH-PONTUACAO-001-AUDIT
  tarefa: "Auditar semanticamente a decisão humana de pontuação antes de criar fichas, categorias ou testes."
```

## Status do arquivo

`DH_PONTUACAO_001_RESPOSTA_HUMANA_REGISTRADA_AGUARDANDO_AUDITORIA`
