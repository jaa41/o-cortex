---
name: preaudi
description: >
  Prepara audiência de instrução trabalhista e entrega o PAINEL em HTML (um arquivo para abrir no
  navegador, no tablet ou no computador da sala): resumo do caso, incontroversos × controvertidos com
  ônus da prova, mapa de provas, roteiro de perguntas por depoente, documentos a exigir e preliminares.
  Use SEMPRE que o usuário enviar petição inicial, contestação e demais peças de um processo trabalhista
  e pedir "preparar a audiência", "pré-audiência", "painel", "roteiro de perguntas", "pontos
  controvertidos", "ônus da prova" ou "mapa de provas", mesmo sem usar essas palavras.
---

# Painel pré-audiência

Recebe as peças de um processo trabalhista que vai a audiência de instrução e devolve **um arquivo
HTML** — o painel. O painel é um modelo fixo (`assets/preaudi.html`); o que muda de processo para
processo é só um arquivo de dados em JSON, que você grava e o script `scripts/montar.py` encaixa no
modelo. **Você nunca escreve nem edita o HTML.** Um painel desenhado à mão perde o padrão, as abas e as
anotações; o painel do script sai sempre igual.

## Princípio

> O magistrado precisa chegar à audiência sabendo o que é incontroverso, o que precisa ser provado, quem
> deve provar e que perguntas fazer. **Só o que está nos autos:** nunca inventar fato, data, valor ou nome.
> Dúvida vira alerta no painel, não suposição.

## Passo a passo

1. **Inventário.** Liste as peças recebidas (inicial, emenda, contestação, réplica, atas, laudo, rol de
   testemunhas, acordo ou convenção coletiva). **Faltando a inicial ou a contestação, pare e peça:** sem as
   duas não há como cruzar pedidos e defesa. Diga ao usuário o que encontrou antes de seguir.
2. **Leitura, uma peça por vez**, pela ordem: inicial, contestação, réplica, atas, laudo, demais. Para o que
   extrair de cada tipo, leia `references/modelos-extracao.md`. PDF grande: extraia o texto por páginas com
   código (PyMuPDF ou `pdftotext`, o que houver) e leia em partes; página escaneada, leia como imagem. Se
   o volume ultrapassar o que se consegue ler bem, diga isso e peça só as peças essenciais (inicial,
   contestação, réplica, atas).
3. **Cruzar pedido × defesa**, pedido por pedido:
   - **Incontroverso**: fato admitido expressamente; fato não impugnado especificamente (art. 341 do CPC c/c
     art. 769 da CLT); matéria só de direito.
   - **Controvertido**: fato negado com impugnação específica; versão divergente; matéria que depende de
     prova.
4. **Ônus da prova** de cada controvertido: consulte `references/onus-prova.md` (art. 818 da CLT, Súmulas
   do TST). Nada de ônus de memória.
5. **Mapa de provas**: um item para cada controvertido, com o estado (`completa`, `parcial`, `pendente`,
   `dispensada`) e a providência.
6. **Roteiro de perguntas** por depoente, pelas regras abaixo.
7. **Gravar o JSON** (`dados.json`) na forma de `references/dados-preaudi.md`. Leia esse arquivo antes.
8. **Montar o painel:**
   ```
   python <pasta desta skill>/scripts/montar.py dados.json --saida <pasta de saída>/painel-pre-audiencia-<final do processo>.html
   ```
   Se o script recusar, ele diz o que corrigir: corrija o JSON e rode de novo. Um HTML que não saiu do
   script não é entrega.
9. **Entregar o arquivo HTML** e, na conversa, só um resumo curto: o caso em duas linhas, os temas
   controvertidos com o ônus de cada um, e os alertas. Diga que o arquivo abre com duplo clique no
   navegador, sem instalar nada, e que as anotações da audiência ficam no navegador (o botão "Exportar
   anotações" baixa um arquivo com elas). Termine lembrando que é ferramenta de apoio: a análise, a
   valoração da prova e a decisão cabem ao magistrado.

## Qualidade das perguntas

O roteiro é instrumento de inquirição, não lembrete do processo. Cada item é uma pergunta que o
magistrado pode ler em voz alta. Duas regras duras, nesta ordem:

1. **Só o controvertido.** A pergunta ataca um fato da lista de controvertidos, ou a capacidade da
   testemunha de falar sobre aquele fato. O que está em incontroversos ou no quadro do contrato (admissão,
   demissão, cargo registrado, salário, tipo de rescisão, quando admitidos) **não vira pergunta**, nem para a
   parte, nem para a testemunha, nem como `Base`. Cargo, função ou data só entram se forem o próprio ponto
   controvertido (desvio, acúmulo, confiança, vínculo).
2. **Uma pergunta, um fato.** Um ponto de interrogação por item. Proibido empilhar indagações ("função,
   período, contato"; dois `?`; "e"/"ou" juntando duas perguntas). Narrativa aberta conta como uma ("Como
   ocorreu o acidente de 31 de julho de 2025?"). O detalhe seguinte é a pergunta seguinte.

As demais: diretas; específicas (fatos concretos, não teses jurídicas); **diferenciadas por depoente**
(listas distintas para reclamante, preposto e testemunhas); orientadas ao ônus (o que a parte com ônus
precisa demonstrar); práticas (sim/não ou fato observável; confronto com documento quando houver
contradição). Testemunha: se o rol não estabelece o contato, uma pergunta `Base` de conhecimento pessoal
("O senhor trabalhou no mesmo setor que o reclamante?") e só uma.

**Serve:** "A que horas o reclamante saía da loja?" · "A empresa fornecia máscara?" · "O depoente presenciou
a cobrança do supervisor ao reclamante?"

**Não serve:** "Qual o cargo e a data de admissão?" (incontroverso e duas perguntas) · "O reclamante
trabalhava após as 18h? Com que frequência?" (duas) · "O reclamante tem direito a horas extras?"
(jurídica) · "O que o depoente acha do caso?" (opinião).

Antes de gravar o roteiro, confira cada item contra a lista de incontroversos e contra a regra do
um-fato. O que falhar, corta ou parte.

## Outras regras

- **Nomes.** Partes só no cabeçalho (`autores`, `reus`) e no rótulo do depoente. **Testemunhas nunca são
  nomeadas**: posição ou função ("1ª testemunha do reclamante").
- **Citar a peça** no texto, quando se souber: "Contestação, id 35f0290, fl. 12". O campo `pecas` fica `[]`.
- **Ponto atípico** (prescrição próxima, perícia necessária e não designada, testemunha que é ex-sócio,
  documento em poder exclusivo da empresa) vai em `alertas`.
- **Acidente de trabalho ou doença ocupacional**: o roteiro cobre só a prova oral; nexo e incapacidade
  dependem de perícia. Diga isso em `alertas`.
- **Se o usuário pedir mais** (relatório em Markdown, minuta de sentença, ata): o painel é o produto desta
  skill; ofereça o restante como pedido à parte, sem prometer o padrão de nenhum gabinete.
