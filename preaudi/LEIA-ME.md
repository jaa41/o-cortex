# Pré-audiência

Você arrasta as peças de um processo trabalhista para uma conversa no Claude e recebe de volta **um painel em
HTML** para abrir no navegador, no computador ou no tablet da sala de audiência:

- resumo do caso e dados do contrato;
- o que é **incontroverso** e o que é **controvertido**, com o **ônus da prova** de cada ponto;
- **mapa de provas** (o que já está nos autos, o que falta, o que fazer);
- **roteiro de perguntas** para cada depoente (reclamante, preposto, testemunhas), com caixa para marcar as
  feitas e espaço para anotar;
- documentos a exigir e preliminares.

O painel é sempre o mesmo modelo, com o mesmo desenho: o Claude só preenche os dados.

## O que você precisa

- Uma conta paga do Claude (o plano Pro serve).
- Em **Configurações → Capacidades**, a opção de **execução de código e criação de arquivos** ligada.
- Nada para instalar no computador.

## Instalar (uma vez só)

1. Nesta página, abra **Releases** (coluna da direita) e baixe o arquivo **`preaudi.zip`**. Não precisa
   descompactar.
2. No claude.ai, vá em **Configurações → Capacidades → Skills** e envie o `.zip` (botão de enviar/adicionar
   skill). Os nomes dos menus podem variar um pouco conforme a versão do site.
3. Deixe a skill **ligada**.

## Usar

1. Abra uma **conversa nova** e anexe as peças do processo em PDF: **petição inicial e contestação são
   obrigatórias**; ajudam muito a réplica, as atas de audiências anteriores, o laudo e o rol de testemunhas.
2. Escreva algo como: **"Prepare a pré-audiência deste processo."**
3. O Claude lê, conta o que encontrou e, ao final, entrega um arquivo **`painel-pre-audiencia-….html`**. Baixe-o
   e abra com duplo clique.

**Dicas**

- Mande só as peças necessárias, e não os autos inteiros: o Claude lê melhor e mais rápido.
- Se ele disser que faltou alguma peça essencial, envie e peça de novo.
- Se pedir o mesmo painel outra vez, o resultado pode variar um pouco nos detalhes: o modelo de tela, não.

## No painel

- Abas: **Caso**, **Controvérsias**, **Provas**, **Roteiro** e **Verificar**.
- No Roteiro, marque as perguntas já feitas. Para o depoimento de **parte** há a marca "dispensado"; para a
  **testemunha**, um campo de nome. Cabem até três testemunhas de cada lado.
- **A+** aumenta a letra; **Imprimir** abre todas as abas no papel.
- Suas anotações ficam guardadas **naquele navegador**. O botão **Exportar anotações** baixa um arquivo com elas.
- Sem internet o painel abre normalmente; só troca o tipo de letra.

## Cuidados

- É **ferramenta de apoio**. A análise, a valoração da prova e a decisão cabem ao magistrado: confira o que o
  painel afirma com os autos.
- As peças que você anexa são enviadas ao Claude. Prefira a conta institucional do seu órgão, se houver.
- O painel traz os **nomes das partes** e o resumo do caso. Trate o arquivo como trata o processo.

## Se algo der errado

- **O Claude disse que o painel não saiu:** peça "corrija o JSON e rode de novo o montar.py". A skill confere os
  dados e diz o que está errado.
- **Não aparece a skill ou ela não roda:** confira se a execução de código e a criação de arquivos estão ligadas
  e se a skill está ativa.
- **Autos muito grandes:** envie só inicial, contestação, réplica e atas.
