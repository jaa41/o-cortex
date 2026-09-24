# Forma do `dados.json` do painel pré-audiência

O painel é um modelo HTML fixo. O que muda de processo para processo é só este JSON, que o
`scripts/montar.py` encaixa no modelo. **Não escreva HTML.**

## Regras duras

- **JSON estrito**: sem comentários, sem vírgula sobrando, sem cerca ```` ```json ````. Aspas duplas. UTF-8.
- Um objeto `{...}` na raiz.
- **Todos os campos obrigatórios presentes**, mesmo vazios: lista vazia `[]` é resposta válida; campo ausente
  faz o `montar.py` parar.
- **Nada de placeholder.** `"a definir"`, `"…"`, `"Nome da parte"` viram texto na tela do magistrado durante a
  audiência. Não sabendo, deixe a lista vazia ou diga "não consta nos autos".
- **Só o que está nos autos.** Fato, valor, data e nome que você não achou nas peças não entram.

## Campos obrigatórios

| Campo | Tipo | O que é |
|---|---|---|
| `processo` | texto | número do processo (CNJ), `0000000-00.0000.5.04.0000` |
| `audiencia` | texto | espécie, data, hora e forma — `"Instrução — 09/09/2026, 09h, por videoconferência"`; sem data nos autos: `"Instrução — data não consta dos autos"` |
| `autores` | lista de objetos | `{nome, papel}` |
| `reus` | lista de objetos | `{nome, papel}` |
| `resumo` | texto | o caso em um parágrafo |
| `contrato` | lista de pares | `[rótulo, valor]` — admissão, demissão, função, salário, tipo de rescisão… |
| `incontroversos` | lista de pares | `[fato, fonte]` — fonte: "admitido na contestação", "não impugnado", "matéria de direito" |
| `controvertidos` | lista de objetos | ver abaixo |
| `provas` | lista de quíntuplas | ver abaixo |
| `roteiro` | lista de objetos | ver abaixo |

## Campos opcionais (viram `[]` se faltarem)

| Campo | Tipo | O que é |
|---|---|---|
| `verificar` | lista de triplas | `[documento, responsável, fundamento]` — documentos a exigir na audiência |
| `preliminares` | lista de pares | `[preliminar, análise]` |
| `alertas` | lista de textos | o que precisa de atenção na abertura (prescrição, perícia não designada, suspeição de testemunha…) |
| `pecas` | lista | deixe `[]` neste kit: o painel não tem os PDFs. Cite a peça no próprio texto: "Contestação, id 35f0290, fl. 12" |

Não escreva `gerado_em`, `documentos` nem `essenciais`: o `montar.py` cuida do que precisar.

### `autores` e `reus`

```json
"autores": [{"nome": "Maria Souza", "papel": "reclamante"}],
"reus": [
  {"nome": "Empresa Alfa Ltda.", "papel": "reclamada"},
  {"nome": "Beta S.A.", "papel": "tomadora"}
]
```

Litisconsórcio cabe: uma entrada por parte. O `papel` é livre — `"reclamante"`, `"reclamada"`, `"tomadora"`, `"sócia"`.

### `controvertidos`

```json
{
  "tema": "Horas extras",
  "pedido": "o que a inicial pede",
  "defesa": "o que a contestação opõe",
  "onus": "reu",
  "prova": "documental (cartões-ponto) e oral",
  "fundamento": "art. 74, §2º, da CLT; Súmula 338, I, do TST"
}
```

- `tema` e `onus` são **obrigatórios** em cada item.
- `onus`: `"autor"`, `"reu"`, `"repartido"` ou `"dinamico"`. Nos dois últimos, escreva `onus_detalhe` dizendo o
  que cabe a quem (art. 818, §1º, da CLT na distribuição dinâmica).
- Havendo defesas diferentes entre os réus, troque `defesa` por `"defesas": [{"parte": "Alfa", "texto": "…"}, …]`.
- O ônus sai de `references/onus-prova.md`, não de memória.

### `provas` — o mapa de provas

```json
"provas": [["Horas extras", "cartões-ponto", "parcial", "reu", "faltam 2023-2024"]]
```

Ordem fixa: `[tema, prova, estado, ônus, providência]`. Um item para **cada** ponto controvertido.
`estado` só aceita `completa`, `parcial`, `pendente` ou `dispensada` — é o que pinta o sinal na tela.
O ônus aceita também `"—"` (nas dispensadas).

### `roteiro` — perguntas por depoente

```json
{
  "depoente": "Reclamante (Maria Souza)",
  "lado": "autor",
  "tipo": "parte",
  "perguntas": [["Jornada", "Que horário cumpria de segunda a sexta?"]]
}
```

- `depoente` e a lista `perguntas` são **obrigatórios**. Cada pergunta é o par `[tema, pergunta]`.
- `lado`: `"autor"` ou `"reu"`. `tipo`: `"parte"` ou `"testemunha"` (opcional; sem ele, o nome decide).
- **Escreva só os depoentes que se sabe que virão** — em regra o reclamante e o preposto de cada ré. O painel
  completa sozinho até **três testemunhas de cada lado**, com as perguntas-base do lado; se o rol de
  testemunhas já consta dos autos, ponha as testemunhas com as perguntas próprias.
- Testemunha pode abrir com uma pergunta de tema `Base` (conhecimento pessoal do fato controvertido). O painel a
  reaproveita ao acrescentar depoente.
- **Qualidade das perguntas** (regra dura, ver o SKILL.md): só o controvertido; uma pergunta, um fato.

## Esqueleto mínimo

```json
{
  "processo": "0000000-00.2026.5.04.0005",
  "audiencia": "Instrução — 09/09/2026, 09h, por videoconferência",
  "autores": [{"nome": "…", "papel": "reclamante"}],
  "reus": [{"nome": "…", "papel": "reclamada"}],
  "resumo": "…",
  "contrato": [["Admissão", "…"], ["Demissão", "…"], ["Função", "…"]],
  "incontroversos": [["…", "…"]],
  "controvertidos": [{"tema": "…", "pedido": "…", "defesa": "…", "onus": "reu", "prova": "…", "fundamento": "…"}],
  "provas": [["…", "…", "pendente", "reu", "…"]],
  "roteiro": [{"depoente": "Reclamante (…)", "lado": "autor", "tipo": "parte",
               "perguntas": [["…", "…?"]]}],
  "verificar": [],
  "preliminares": [],
  "alertas": []
}
```
