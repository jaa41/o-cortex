# Pré-audiência

Você anexa as peças de um processo trabalhista numa conversa no Claude e recebe de volta **um painel em
HTML** para abrir no navegador, no computador ou no tablet da sala de audiência:

- resumo do caso e dados do contrato;
- o que é **incontroverso** e o que é **controvertido**, com o **ônus da prova** de cada ponto;
- **mapa de provas**: o que já está nos autos, o que falta, o que fazer;
- **proposta de acordo**, com valor **mínimo e máximo**, pedido por pedido, pelo risco de cada um (ônus e prova);
- **roteiro de perguntas** para cada depoente, com caixa para marcar as feitas e espaço para anotar.

> **Versão de teste.** Seus comentários decidem o que melhora e o que vem a seguir.

## O que você precisa

- Uma conta paga do Claude (o plano Pro serve).
- Em **Configurações → Capacidades**, a **execução de código e criação de arquivos** ligada.
- Nada para instalar no computador.

## Instalar (uma vez só)

1. Em **Releases** (coluna da direita desta página), baixe o **`preaudi.zip`**. Não descompacte.
2. No claude.ai, vá em **Configurações → Capacidades → Skills** e envie o `.zip`.
3. Deixe a skill **ligada**.

## Usar

1. Abra uma **conversa nova** e anexe as peças em PDF. **Petição inicial e contestação são obrigatórias**;
   ajudam a réplica, as atas, o laudo e o rol de testemunhas. Serve de dois jeitos:
   - **um PDF por peça**; ou
   - **um PDF só**, baixado do PJe depois de marcar os documentos que interessam.
2. Escreva: **"Prepare a pré-audiência deste processo."**
3. O Claude conta o que encontrou e entrega o **`painel-pre-audiencia-….html`**. Baixe e abra com duplo clique.

**Dicas:** mande só as peças necessárias, não os autos inteiros (passam do tamanho que o claude.ai aceita).
Se faltar peça essencial, ele avisa: envie e peça de novo.

## No painel

- Abas **Caso**, **Controvérsias**, **Provas** e **Roteiro**. A proposta de acordo fica na aba Caso, com a conta
  à vista: os valores são os da inicial, sem juros nem correção; é parâmetro para a proposta, não condenação.
- No Roteiro, marque as perguntas feitas e anote as respostas; **+ depoente** acrescenta quem não estava
  previsto.
- **A+** aumenta a letra; **Imprimir** põe todas as abas no papel.
- As marcas e anotações ficam guardadas **naquele navegador**.

## Cuidados

- É **ferramenta de apoio**. A análise, a valoração da prova e a decisão cabem ao magistrado: confira o que o
  painel afirma com os autos.
- As peças que você anexa são enviadas ao Claude. Prefira a conta institucional do seu órgão, se houver.
- O painel traz os nomes das partes. Trate o arquivo como trata o processo.

## Se algo der errado

- **O painel não saiu:** peça "corrija o JSON e rode de novo o montar.py".
- **A skill não aparece ou não roda:** confira se a execução de código está ligada e a skill, ativa.
