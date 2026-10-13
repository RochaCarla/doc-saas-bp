#!/usr/bin/env python3
"""Gera a aba Equipe (docs/equipe/index.md) e a página "Autoria e equipe" do e-book (overrides/print/capa.tpl).

A lista vem da página Equipe do portal de conhecimento (gitlab.com/lappis-unb/decidimbr/docs), que junta a base
Integrantes da Equipe do Notion e quem tem commits nos repositórios do grupo lappis-unb/decidimbr. Para atualizar,
copie de lá scripts/portal/equipe/equipe.json para scripts/equipe.json e as fotos de docs/portal/equipe/fotos/
para docs/assets/equipe/, e rode:

  python3 scripts/equipe.py

Só usa a biblioteca padrão do Python.
"""

from __future__ import annotations

import html
import json
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FONTE = ROOT / "scripts" / "equipe.json"
FOTOS = ROOT / "docs" / "assets" / "equipe"
PAGINA = ROOT / "docs" / "equipe" / "index.md"
TPL = ROOT / "overrides" / "print" / "capa.tpl"
INI = "{#- >>> autoria (gerado por scripts/equipe.py; não edite à mão) -#}"
FIM = "{#- <<< autoria -#}"
INI_ANTIGO = "{#- >>> autoria (gerado por scripts/autores.py; não edite à mão) -#}"
ANTES_DE = '<div class="bp-front bp-front--apresentacao">'


def foto(p: dict) -> str:
    f = p.get("foto")
    if f and f.startswith("http"):
        src = html.escape(f)
    elif f and (FOTOS / f).exists():
        src = f"../assets/equipe/{f}"
    else:
        ini = "".join(w[0] for w in p["nome"].split()[:2]).upper() or "?"
        return f'<span class="bp-avatar bp-avatar--iniciais" aria-hidden="true">{html.escape(ini)}</span>'
    return f'<img class="bp-avatar" src="{src}" alt="" width="32" height="32" loading="lazy">'


def pagina(pessoas: list[dict], gerado: str) -> str:
    out = ["---\ntitle: Equipe\n---\n",
           "<!-- Gerado por scripts/equipe.py a partir de scripts/equipe.json. Não edite à mão. -->\n",
           "# Equipe\n",
           f"Quem faz o Brasil Participativo, em ordem alfabética: {len(pessoas)} pessoas, entre as registradas na base "
           "Integrantes da Equipe, no Notion, e as que contribuíram com código nos repositórios do grupo "
           "[`lappis-unb/decidimbr`](https://gitlab.com/lappis-unb/decidimbr), no GitLab. A autoria institucional "
           "é do LabLivre/UnB.\n",
           "A foto vem do GitLab e, quando não há, do Notion. Contatos e outros dados pessoais não são publicados. "
           f"Lista da página Equipe do portal de conhecimento, gerada em {gerado[8:10]}/{gerado[5:7]}/{gerado[:4]}.\n",
           "| | Nome | GitLab |\n|---|---|---|"]
    for p in pessoas:
        user = f"[@{p['usuario']}]({p['perfil']})" if p.get("usuario") and p.get("perfil") else "—"
        out.append(f"| {foto(p)} | {html.escape(p['nome'])} | {user} |")
    return "\n".join(out) + "\n"


def autoria(nomes: list[str]) -> str:
    itens = "\n".join(f"    <li>{html.escape(n)}</li>" for n in nomes)
    return f"""{INI}
<div class="bp-front bp-front--autoria">
  <h2 class="bp-rosto__heading">Autoria e equipe</h2>
  <p>A autoria institucional é do Laboratório de Competência em Software Livre (LabLivre) da Universidade de Brasília. Esta é a equipe que faz o Brasil Participativo, em ordem alfabética: {len(nomes)} pessoas, entre as registradas na base Integrantes da Equipe, no Notion, e as que contribuíram com código nos repositórios do grupo <code>lappis-unb/decidimbr</code>, no GitLab.</p>
  <ul class="bp-autoria">
{itens}
  </ul>
</div>
{FIM}
"""


def main() -> int:
    dados = json.loads(FONTE.read_text(encoding="utf-8"))
    pessoas = dados["pessoas"]
    PAGINA.parent.mkdir(parents=True, exist_ok=True)
    PAGINA.write_text(pagina(pessoas, dados["gerado"]), encoding="utf-8")

    nomes = sorted({p["nome"] for p in pessoas},
                   key=lambda n: unicodedata.normalize("NFKD", n).encode("ascii", "ignore").decode().casefold())
    tpl = TPL.read_text(encoding="utf-8")
    for ini in (INI, INI_ANTIGO):
        if ini in tpl:
            tpl = tpl[:tpl.index(ini)] + autoria(nomes) + tpl[tpl.index(FIM) + len(FIM) + 1:]
            break
    else:
        if ANTES_DE not in tpl:
            sys.exit(f"não achei onde inserir a autoria em {TPL}")
        tpl = tpl.replace(ANTES_DE, autoria(nomes) + "\n" + ANTES_DE, 1)
    TPL.write_text(tpl, encoding="utf-8")
    sem_foto = [p["foto"] for p in pessoas if p.get("foto") and not p["foto"].startswith("http") and not (FOTOS / p["foto"]).exists()]
    if sem_foto:
        print(f"aviso: fotos ausentes em {FOTOS.relative_to(ROOT)}: {', '.join(sem_foto)}", file=sys.stderr)
    print(f"{len(pessoas)} pessoas na aba Equipe e {len(nomes)} nomes na autoria do e-book", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
