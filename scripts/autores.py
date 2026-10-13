#!/usr/bin/env python3
"""Preenche a página "Autoria e equipe" do e-book (overrides/print/capa.tpl) com a lista da equipe.

A lista vem da página Equipe do portal de conhecimento (gitlab.com/lappis-unb/decidimbr/docs), que junta a base
Integrantes da Equipe do Notion e quem tem commits nos repositórios do grupo lappis-unb/decidimbr. Para atualizar,
copie de lá o arquivo scripts/portal/equipe/autores.json para scripts/autores.json e rode:

  python3 scripts/autores.py

Só usa a biblioteca padrão do Python.
"""

from __future__ import annotations

import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FONTE = ROOT / "scripts" / "autores.json"
TPL = ROOT / "overrides" / "print" / "capa.tpl"
INI = "{#- >>> autoria (gerado por scripts/autores.py; não edite à mão) -#}"
FIM = "{#- <<< autoria -#}"
ANTES_DE = '<div class="bp-front bp-front--apresentacao">'


def main() -> int:
    dados = json.loads(FONTE.read_text(encoding="utf-8"))
    nomes = dados["autores"]
    itens = "\n".join(f"    <li>{html.escape(n)}</li>" for n in nomes)
    bloco = f"""{INI}
<div class="bp-front bp-front--autoria">
  <h2 class="bp-rosto__heading">Autoria e equipe</h2>
  <p>A autoria institucional é do Laboratório de Competência em Software Livre (LabLivre) da Universidade de Brasília. Esta é a equipe que faz o Brasil Participativo, em ordem alfabética: {len(nomes)} pessoas, entre as registradas na base Integrantes da Equipe, no Notion, e as que contribuíram com código nos repositórios do grupo <code>lappis-unb/decidimbr</code>, no GitLab.</p>
  <ul class="bp-autoria">
{itens}
  </ul>
</div>
{FIM}
"""
    tpl = TPL.read_text(encoding="utf-8")
    if INI in tpl:
        ini, fim = tpl.index(INI), tpl.index(FIM) + len(FIM) + 1
        tpl = tpl[:ini] + bloco + tpl[fim:]
    elif ANTES_DE in tpl:
        tpl = tpl.replace(ANTES_DE, bloco + "\n" + ANTES_DE, 1)
    else:
        sys.exit(f"não achei onde inserir a autoria em {TPL}")
    TPL.write_text(tpl, encoding="utf-8")
    print(f"{len(nomes)} nomes na página de autoria → {TPL.relative_to(ROOT)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
