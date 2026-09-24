# O Cortex

Peças prontas para o **Claude**, feitas por um juiz do trabalho para o trabalho de quem lida com processos
trabalhistas. Cada peça é uma **skill**: você envia um arquivo `.zip` ao claude.ai **uma vez** e passa a usá-la
em qualquer conversa. **Não há nada para instalar no computador.**

## As peças

| Peça | Para que serve | Situação | Baixar |
|---|---|---|---|
| [**Pré-audiência**](preaudi/LEIA-ME.md) | Você anexa as peças do processo e recebe um painel em HTML para a audiência de instrução: incontroversos × controvertidos com ônus da prova, mapa de provas e roteiro de perguntas por depoente. | em teste | [preaudi.zip](https://github.com/jaa41/o-cortex/releases/tag/preaudi-v0.1.0) |

Cada pasta tem um `LEIA-ME.md` com o passo a passo daquela peça.

## Como instalar uma peça

1. Abra a aba **Releases** deste repositório (coluna da direita) e baixe o `.zip` da peça. Não descompacte.
2. No [claude.ai](https://claude.ai), vá em **Configurações → Capacidades → Skills** e envie o `.zip`.
3. Deixe a skill ligada e, numa conversa nova, peça o que a peça faz (o `LEIA-ME.md` da peça diz como).

## O que você precisa

- Uma conta **paga** do Claude (o plano Pro serve).
- **Execução de código e criação de arquivos** ligada em Configurações → Capacidades.

## Avisos

- São **ferramentas de apoio**. A análise, a valoração da prova e a decisão cabem a quem as assina: confira
  sempre com os autos.
- O que você anexa é enviado ao Claude. Prefira a conta institucional do seu órgão, se houver, e trate o que
  sai como trata o processo.
- Nada aqui contém dados de processo real: os exemplos são fictícios.

## Licença

[MIT](LICENSE): pode usar, copiar e adaptar, mantendo o aviso de autoria. Sem garantia.
