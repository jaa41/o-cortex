---
name: preaudi
description: >
  Prepara audiência de instrução trabalhista e entrega o PAINEL em HTML (um arquivo para abrir no
  navegador): resumo do caso, incontroversos × controvertidos com ônus da prova, mapa de provas, proposta de acordo
  (mínimo e máximo) e roteiro de perguntas por depoente. Use SEMPRE que o usuário enviar petição inicial, contestação e demais peças de
  um processo trabalhista (em PDFs separados ou num PDF único baixado do PJe) e pedir "preparar a
  audiência", "pré-audiência", "painel", "roteiro de perguntas", "pontos controvertidos", "ônus da prova"
  ou "mapa de provas", mesmo sem usar essas palavras.
---

# Painel pré-audiência

Recebe as peças de um processo trabalhista e devolve **um arquivo HTML**, o painel. Você grava só um
JSON; o `scripts/montar.py` o encaixa no modelo `assets/preaudi.html`. **Nunca escreva nem edite HTML.**

**Só o que está nos autos:** nunca invente fato, data, valor ou nome. Dúvida vira alerta, não suposição.

## Passo a passo

1. **Inventário.** Aceite as peças como vierem:
   - **PDFs separados**: o nome e a primeira página dizem o que é cada um.
   - **Um PDF só com vários documentos**, baixado do PJe: liste os marcadores do PDF com código (`pypdf`,
     PyMuPDF ou o que houver); cada marcador é um documento, com tipo e página inicial. Sem marcadores, use
     o índice das primeiras páginas ou, em último caso, as primeiras linhas de cada página.

   Liste só as peças que interessam (inicial, emenda, contestação, réplica, atas, laudo, rol de
   testemunhas, norma coletiva) e ignore o resto (procuração, certidão, notificação, comprovante).
   **Faltando a inicial ou a contestação, pare e peça.** Diga ao usuário o que encontrou antes de seguir.
2. **Leitura, uma peça por vez**: inicial, contestação, réplica, atas, laudo, demais. O que extrair de cada
   uma está em `references/modelos-extracao.md`. Extraia o texto por páginas com código, só as páginas da
   peça, e leia em partes; página escaneada, leia como imagem. Documentos juntados (contracheques, cartões
   de ponto, fotos) não se leem inteiros: basta saber que existem e o que provam. Volume grande demais:
   diga isso e peça só inicial, contestação, réplica e atas.
3. **Pedido × defesa**, pedido por pedido:
   - **Incontroverso**: fato admitido; fato não impugnado especificamente (art. 341 do CPC c/c art. 769 da
     CLT); matéria só de direito.
   - **Controvertido**: fato negado com impugnação específica; versão divergente; matéria que depende de
     prova.
4. **Ônus da prova** de cada controvertido, por `references/onus-prova.md`.
5. **Mapa de provas**: um item por controvertido, com estado e providência.
5-bis. **Proposta de acordo**, mínimo e máximo, pelo método de `references/dados-preaudi.md`
   (campo `conciliacao`): valor de cada pedido na inicial; risco para a reclamada (provável, incerta,
   improvável) pelo ônus e pela prova; mínimo = prováveis, máximo = prováveis + incertos. Nada estimado
   sem número nos autos.
6. **Roteiro de perguntas** por depoente, pelas regras abaixo.
7. **Gravar o `dados.json`** na forma de `references/dados-preaudi.md` (leia antes).
8. **Montar:**
   ```
   python <pasta desta skill>/scripts/montar.py dados.json --saida <pasta de saída>/painel-pre-audiencia-<final do processo>.html
   ```
   Se recusar, corrija o JSON como ele indicar e rode de novo. HTML que não saiu do script não é entrega.
9. **Entregar o arquivo** e, na conversa, só: o caso em duas linhas, os controvertidos com o ônus de cada
   um, a faixa de acordo e os alertas. Diga que abre com duplo clique no navegador e que as marcas ficam naquele navegador.
   Termine lembrando que é ferramenta de apoio: análise, valoração da prova e decisão cabem ao magistrado.

## Perguntas

1. **Só o controvertido.** Nada do que está em incontroversos ou no quadro do contrato vira pergunta.
2. **Uma pergunta, um fato.** Um ponto de interrogação por item; nada de "e"/"ou" juntando duas.
3. Diretas, sobre fatos (nunca teses jurídicas nem opinião), diferentes para cada depoente, voltadas ao que
   a parte com o ônus precisa demonstrar.
4. Testemunha: uma pergunta `Base`, de conhecimento pessoal, e só uma.

**Serve:** "A que horas o reclamante saía da loja?" · **Não serve:** "Qual o cargo e a data de admissão?"
· "O reclamante tem direito a horas extras?"

Confira cada pergunta contra os incontroversos e contra a regra 2 antes de gravar.

## Outras regras

- **Testemunhas nunca são nomeadas**: "1ª testemunha do reclamante".
- **Cite a peça** no texto quando souber: "Contestação, id 35f0290, fl. 12".
- **Acidente ou doença ocupacional**: o roteiro cobre só a prova oral; nexo e incapacidade dependem de
  perícia. Diga isso em `alertas`.
- **Pedido de outra coisa** (relatório, minuta de sentença, ata): o painel é o produto desta skill;
  ofereça o resto como pedido à parte.
