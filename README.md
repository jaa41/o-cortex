# cortex

**As funções executivas do gabinete.** Ecossistema de gestão judicial.
[o-cortex.manus.space](https://o-cortex.manus.space)

O Cortex é um sistema desenvolvido pelo Juiz do Trabalho **Jorge Alberto Araujo** como solução para a gestão
de processos judiciais: adapta os autos para a análise pela inteligência artificial e permite manipulá-los em
todas as fases do processo, do ingresso ao arquivamento.

São várias ferramentas e aplicativos, e elas estão à disposição tanto de **usuários finais** quanto de
**desenvolvedores** que queiram conhecer soluções já adotadas para problemas cotidianos dessa gestão. Os
módulos vão sendo abertos aqui, um a um.

## O que é

Assim como o córtex pré-frontal planeja, prioriza e coordena as áreas especializadas do cérebro, o cortex
coordena as ferramentas que baixam, recortam, leem, limpam e anonimizam os autos, e os agentes de inteligência
artificial que preparam as minutas. Cada peça do processo passa por várias mãos; o cortex sabe onde ela está e
em que ponto do caminho parou.

Tudo começa num painel só. Cada processo ocupa uma linha, com a situação dita numa palavra: novidade, em
análise, minuta pronta, publicado. O que chega ao gabinete aparece no topo, com o número do processo já
identificado e uma sugestão do que fazer. Nada se move sozinho, e nada é apagado: o que não serve mais vai para
o descarte, até que alguém decida de verdade.

## Seis funções, uma para cada letra

| | Função | O que faz |
|---|---|---|
| **c** | coordenação | Um roteiro único para todo processo: baixar, selecionar, pedir, revisar, gerar o PDF e marcar como publicado. |
| **o** | organização | Cada processo existe numa pasta própria, com o número do CNJ, e numa linha da fila de trabalho; o cortex confere os dois lados. |
| **r** | registro | Os registros só crescem, nunca são reescritos: cada análise deixa a resposta gravada na pasta do processo. |
| **t** | triagem | O que chega entra por uma caixa de entrada; os autos são recortados pelo índice do PJe e cada parte segue o seu caminho. |
| **e** | elaboração | Cada processo recebe uma sessão de IA própria, que começa do zero, para um caso não contaminar o outro. |
| **x** | extração | Extrai o texto dos PDFs (com OCR para os digitalizados), limpa o ruído e anonimiza os dados pessoais na própria máquina. |

## Princípio

> A tecnologia organiza e prepara; a decisão é sempre humana.

A inteligência artificial redige a minuta; o juiz lê, corrige, decide e assina. O cortex existe para que esse
trabalho comece com os autos em ordem e termine com a peça no lugar certo.

## Módulos

Cada módulo funciona sozinho, sem precisar dos outros.

| Módulo | Para que serve | Situação | Baixar |
|---|---|---|---|
| [**Pré-audiência**](preaudi/LEIA-ME.md) | Você anexa as peças do processo e recebe um painel em HTML para a audiência de instrução: incontroversos × controvertidos com ônus da prova, mapa de provas e roteiro de perguntas por depoente. | em teste | [preaudi.zip](https://github.com/jaa41/o-cortex/releases/tag/preaudi-v0.1.0) |

Cada pasta tem um `LEIA-ME.md` com o passo a passo do módulo.

### Para usuários finais

Os módulos disponíveis hoje são **skills** do Claude: você envia um arquivo `.zip` ao claude.ai uma vez e passa a
usá-los em qualquer conversa. **Não há nada para instalar no computador.**

1. Abra a aba **Releases** deste repositório (coluna da direita) e baixe o `.zip` do módulo. Não descompacte.
2. No [claude.ai](https://claude.ai), vá em **Configurações → Capacidades → Skills** e envie o `.zip`.
3. Deixe a skill ligada e, numa conversa nova, peça o que o módulo faz (o `LEIA-ME.md` diz como).

Você precisa de uma conta **paga** do Claude (o plano Pro serve), com **execução de código e criação de
arquivos** ligada em Configurações → Capacidades.

### Para desenvolvedores

Cada módulo é uma pasta que se lê de ponta a ponta: o `SKILL.md` (as instruções ao agente), os `scripts/`, o
modelo em `assets/` e as `references/`. O desenho que se repete, e que pode servir a outros problemas da mesma
gestão: **o agente grava só dados, em JSON com forma definida, e um script determinístico confere e monta o
entregável.** O modelo nunca é reescrito pelo agente, o entregável sai sempre igual, e o script recusa, sem
gravar nada, o dado que não confere. A licença permite copiar e adaptar.

## Avisos

- São **ferramentas de apoio**. A análise, a valoração da prova e a decisão cabem a quem as assina: confira
  sempre com os autos.
- O que você anexa é enviado ao Claude. Prefira a conta institucional do seu órgão, se houver, e trate o que
  sai como trata o processo.
- Nada aqui contém dados de processo real: os exemplos são fictícios.

## Licença

[MIT](LICENSE): pode usar, copiar e adaptar, mantendo o aviso de autoria. Sem garantia.
