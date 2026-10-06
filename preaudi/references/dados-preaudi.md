# Forma do `dados.json` do painel pré-audiência

O painel é um modelo HTML fixo. O que muda de processo para processo é só este JSON, que o
`scripts/montar.py` encaixa no modelo. **Não escreva HTML.**

## Regras duras

- **JSON estrito**: sem comentários, sem vírgula sobrando, sem cerca ```` ```json ````. Aspas duplas. UTF-8.
- Um objeto `{...}` na raiz, só com os campos abaixo: campo a mais faz o `montar.py` parar.
- **Todos os campos obrigatórios presentes**, mesmo vazios: lista vazia `[]` é resposta válida.
- **Nada de placeholder.** `"a definir"`, `"…"`, `"Nome da parte"` viram texto na tela do magistrado durante a
  audiência. Não sabendo, deixe a lista vazia ou diga "não consta nos autos".
- **Só o que está nos autos.** Fato, valor, data e nome que você não achou nas peças não entram.

## Campos

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
| `conciliacao` | objeto | **opcional**: a proposta de acordo, mínimo e máximo — ver abaixo |
| `alertas` | lista de textos | **opcional**: o que precisa de atenção na abertura (prescrição, perícia necessária e não designada, documento em poder exclusivo de uma parte…) |

### `autores` e `reus`

```json
"autores": [{"nome": "Maria Souza", "papel": "reclamante"}],
"reus": [
  {"nome": "Empresa Alfa Ltda.", "papel": "reclamada"},
  {"nome": "Beta S.A.", "papel": "tomadora"}
]
```

Uma entrada por parte. O `papel` é livre — `"reclamante"`, `"reclamada"`, `"tomadora"`, `"sócia"`.

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
  que cabe a quem.
- Havendo defesas diferentes entre os réus, troque `defesa` por `"defesas": [{"parte": "Alfa", "texto": "…"}, …]`.
- O ônus sai de `references/onus-prova.md`, não de memória.

### `provas` — o mapa de provas

```json
"provas": [["Horas extras", "cartões-ponto", "parcial", "reu", "faltam 2023-2024"]]
```

Ordem fixa: `[tema, prova, estado, ônus, providência]`. Um item para **cada** ponto controvertido.
`estado` só aceita `completa`, `parcial`, `pendente` ou `dispensada`. O ônus aceita também `"—"` (nas
dispensadas).

### `roteiro` — perguntas por depoente

```json
{
  "depoente": "Reclamante (Maria Souza)",
  "lado": "autor",
  "perguntas": [["Jornada", "Que horário cumpria de segunda a sexta?"]]
}
```

- `depoente`, `lado` (`"autor"` ou `"reu"`) e `perguntas` são **obrigatórios**. Cada pergunta é o par
  `[tema, pergunta]`.
- Depoentes, nesta ordem: o reclamante; o preposto de cada ré; **uma testemunha de cada lado**
  (`"1ª testemunha do reclamante"`, `"1ª testemunha do reclamado"`), ou as do rol, se constar dos autos.
  Outras se acrescentam na sala, pelo botão "+ depoente".
- A testemunha abre com uma pergunta de tema `Base` (conhecimento pessoal do fato controvertido). O botão
  "+ depoente" a reaproveita.

### `conciliacao` (opcional) — proposta de acordo, mínimo e máximo

Escreva-a sempre que a inicial der valores aos pedidos. O painel a mostra na aba Caso como **Proposta de
acordo — mínimo e máximo**.

```json
"conciliacao": {
  "quadro": [
    ["Horas extras — provável (ré não juntou cartões; Súmula 338, I, do TST)", "R$ 18.400,00"],
    ["Diferenças de comissões — incerta (depende da prova oral)", "R$ 9.000,00"],
    ["Dano moral — improvável (ônus do reclamante, sem indício nos autos): fora da faixa", "R$ 15.000,00"],
    ["Honorários pedidos pelo perito (quem paga depende do resultado)", "R$ 3.500,00"],
    ["Mínimo (só os prováveis)", "R$ 18.400,00"],
    ["Máximo (prováveis e incertos)", "R$ 27.400,00"]
  ],
  "observacoes": "Valores da inicial, sem juros, correção e reflexos não liquidados. A cobrança documentada das metas pesa a favor do reclamante nas comissões.",
  "fonte": "Faixa pelos valores atribuídos na inicial e pelo risco de cada pedido (ônus e prova nos autos); não é liquidação."
}
```

**Método (parâmetros objetivos, nada inventado):**

1. **Base: o valor que a inicial atribui a cada pedido** (art. 840, §1º, da CLT). Pedido sem valor na inicial
   entra com `"valor não indicado na inicial"` e fica fora das somas. Não estime valor que os autos não dão.
2. **Risco de cada pedido para a reclamada**, pelo ônus e pelo mapa de provas, uma palavra no rótulo, com o
   motivo entre parênteses:
   - **provável**: incontroverso; ou ônus da ré sem a prova que lhe cabia nos autos (cartões não juntados,
     recibo ausente); ou prova documental do reclamante não impugnada;
   - **incerta**: depende da prova oral ou da perícia;
   - **improvável**: ônus do reclamante sem indício nos autos, ou prova documental da ré não impugnada.
     Fica **fora da faixa**, mas aparece no quadro (o juiz vê o que ficou de fora).
3. **Mínimo = soma dos prováveis. Máximo = prováveis + incertos.** As duas linhas começam com "Mínimo" e
   "Máximo" (o painel as destaca). Honorários do perito, pelo valor pedido, em linha própria, fora das somas.
4. `observacoes`: o que pesa para a proposta, em uma ou duas frases, e a ressalva de que os valores são os da
   inicial (sem juros, correção e reflexos não liquidados). `fonte`: a frase do exemplo.
5. Pedido sem valor em lugar nenhum e sem base: o quadro diz isso; não há faixa sem números.

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
  "roteiro": [{"depoente": "Reclamante (…)", "lado": "autor", "perguntas": [["…", "…?"]]}],
  "alertas": []
}
```
