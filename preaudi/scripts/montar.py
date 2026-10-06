#!/usr/bin/env python3
"""preaudi 0.8.0 — monta o painel pré-audiência a partir do JSON. Licença MIT.

Uso:
    python montar.py dados.json --saida painel-pre-audiencia-20016.html

Se o JSON estiver errado, diz o que corrigir e sai com código 1, sem gravar nada.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
MODELO = AQUI.parent / "assets" / "preaudi.html"

VERSAO = "0.8.0"
CREDITO = {"texto": f"PreAudi {VERSAO} — painel de acompanhamento de audiências · desenvolvido por Jorge Araujo",
           "contato": "https://direi.to/contato"}

OBRIGATORIOS = ("processo", "audiencia", "autores", "reus", "resumo", "contrato", "incontroversos",
                "controvertidos", "provas", "roteiro")
OPCIONAIS_LISTA = ("alertas",)
ACEITOS = set(OBRIGATORIOS) | set(OPCIONAIS_LISTA) | {"gerado_em", "conciliacao", "credito"}
LISTAS = ("autores", "reus", "contrato", "incontroversos", "controvertidos", "provas", "roteiro")
ESTADOS = ("completa", "parcial", "pendente", "dispensada")
ONUS = ("autor", "reu", "repartido", "dinamico", "—")
PLACEHOLDERS = ("Nome da parte autora", "Empresa Exemplo Ltda.", "Resumo do caso (exemplo do modelo)",
                "0000000-00.0000.0.00.0000", "Instrução — data, hora")

RE_DADOS = re.compile(r"const DADOS = \{.*?\n\};", re.DOTALL)


def carregar(caminho: Path) -> tuple[dict | None, list[str]]:
    """Lê e confere. Devolve (dados, erros); havendo erro, nada se grava."""
    try:
        texto = caminho.read_text(encoding="utf-8-sig").strip()
    except OSError as e:
        return None, [f"não consegui ler {caminho.name}: {e}"]
    texto = re.sub(r"^```(?:json)?\s*|\s*```$", "", texto)
    texto = re.sub(r"^(?:const\s+)?DADOS\s*=\s*", "", texto).rstrip(";").strip()
    try:
        dados = json.loads(texto)
    except json.JSONDecodeError as e:
        return None, [f"{caminho.name} não é JSON válido (linha {e.lineno}, coluna {e.colno}): {e.msg}"]
    if not isinstance(dados, dict):
        return None, [f"{caminho.name}: esperava um objeto {{...}}, veio {type(dados).__name__}"]

    for c in OPCIONAIS_LISTA:
        dados.setdefault(c, [])
    erros: list[str] = []
    faltam = [c for c in OBRIGATORIOS if c not in dados]
    if faltam:
        erros.append("faltam os campos: " + ", ".join(faltam))
    sobram = sorted(c for c in dados if c not in ACEITOS)
    if sobram:
        erros.append("campos que este painel não tem (retire-os): " + ", ".join(sobram))
    errados = [c for c in LISTAS + OPCIONAIS_LISTA if c in dados and not isinstance(dados[c], list)]
    if errados:
        erros.append("deviam ser listas: " + ", ".join(errados))
    if erros:
        return None, erros

    for i, p in enumerate(dados["autores"] + dados["reus"], 1):
        if not isinstance(p, dict) or not p.get("nome"):
            erros.append(f"parte {i} (autores/reus) sem 'nome': cada uma é {{\"nome\": \"…\", \"papel\": \"…\"}}")
    for i, c in enumerate(dados["controvertidos"], 1):
        if not isinstance(c, dict) or not c.get("tema"):
            erros.append(f"controvertido {i} sem 'tema'")
        elif c.get("onus") not in ONUS:
            erros.append(f"controvertido {i} ({c['tema']}): 'onus' deve ser autor|reu|repartido|dinamico")
    for i, p in enumerate(dados["provas"], 1):
        if not (isinstance(p, list) and len(p) == 5):
            erros.append(f"prova {i}: deve ser [tema, prova, estado, ônus, providência] (cinco itens)")
        elif p[2] not in ESTADOS:
            erros.append(f"prova {i} ({p[0]}): estado '{p[2]}' — só vale {'|'.join(ESTADOS)}")
    for i, d in enumerate(dados["roteiro"], 1):
        if not isinstance(d, dict) or not d.get("depoente") or not isinstance(d.get("perguntas"), list):
            erros.append(f"item {i} do roteiro sem 'depoente' ou sem lista 'perguntas'")
        elif d.get("lado") not in ("autor", "reu"):
            erros.append(f"roteiro {i} ({d['depoente']}): 'lado' deve ser autor ou reu")
        elif any(not (isinstance(q, list) and len(q) == 2) for q in d["perguntas"]):
            erros.append(f"roteiro {i} ({d['depoente']}): cada pergunta é [tema, pergunta]")
    conc = dados.get("conciliacao")
    if conc is not None:
        if not isinstance(conc, dict) or not isinstance(conc.get("quadro", []), list):
            erros.append("'conciliacao' é {\"quadro\": [[rótulo, valor]], \"observacoes\": …, \"fonte\": …}")
        elif any(not (isinstance(l, list) and len(l) == 2 and all(isinstance(x, str) for x in l))
                 for l in conc.get("quadro", [])):
            erros.append("'conciliacao': cada linha do quadro é [rótulo, valor], os dois em texto")
        elif conc.get("quadro") and not any(re.match(r"\s*m[íi]nimo", l[0], re.I) for l in conc["quadro"]):
            erros.append("'conciliacao': falta a linha 'Mínimo …' (e a 'Máximo …') no quadro")
    bruto = json.dumps(dados, ensure_ascii=False)
    sobras = [p for p in PLACEHOLDERS if p in bruto]
    if sobras:
        erros.append("sobrou texto de exemplo do modelo: " + "; ".join(sobras))
    return (None, erros) if erros else (dados, [])


def encaixar(modelo_html: str, dados: dict) -> str:
    """Troca o objeto DADOS do modelo pelo JSON."""
    if not RE_DADOS.search(modelo_html):
        raise ValueError("o modelo não tem o bloco `const DADOS = {...};`")
    corpo = json.dumps(dados, ensure_ascii=False, indent=2)
    corpo = corpo.replace("</", "<\\/")          # `</script>` dentro de um valor fecharia o script
    return RE_DADOS.sub(lambda _m: "const DADOS = " + corpo + ";", modelo_html, count=1)


def montar(caminho_json: Path, saida: Path | None = None, modelo: Path = MODELO) -> tuple[Path | None, list[str]]:
    dados, erros = carregar(caminho_json)
    if erros:
        return None, erros
    dados = dict(dados)
    if not dados.get("gerado_em"):
        dados["gerado_em"] = datetime.now().strftime("%d/%m/%Y %Hh%Mmin")
    dados["credito"] = dict(CREDITO)                    # a linha do topo é sempre a do produto
    try:
        html = encaixar(modelo.read_text(encoding="utf-8"), dados)
    except (OSError, ValueError) as e:
        return None, [f"modelo {modelo}: {e}"]
    saida = saida or caminho_json.with_name(f"painel_{caminho_json.stem}.html")
    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.write_text(html, encoding="utf-8")
    return saida, []


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Monta o painel pré-audiência a partir do JSON.")
    ap.add_argument("json", type=Path, help="o dados.json")
    ap.add_argument("--saida", type=Path, help="onde gravar o HTML")
    ap.add_argument("--modelo", type=Path, default=MODELO, help="modelo HTML (padrão: ../assets/preaudi.html)")
    a = ap.parse_args(argv)
    saida, erros = montar(a.json, a.saida, a.modelo)
    if erros:
        print("O painel NÃO foi gerado. Corrija o JSON:", file=sys.stderr)
        for e in erros:
            print(" -", e, file=sys.stderr)
        return 1
    print(f"Painel gravado: {saida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
