#!/usr/bin/env python3
"""Gera a página Visão Geral › Glossário a partir do CONTEXT.md.

O CONTEXT.md é a fonte única da linguagem do domínio. Esta página publica os termos (com o que
evitar), as ambiguidades sinalizadas e o diálogo de exemplo, mais um apêndice de termos técnicos
gerais mantido em scripts/glossario_tecnico.md.

Uso:
  python3 scripts/glossario.py      # gera docs/visao-geral/glossario.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTEXT = ROOT / "CONTEXT.md"
TECNICO = ROOT / "scripts" / "glossario_tecnico.md"
DEST = ROOT / "docs" / "visao-geral" / "glossario.md"


def section(text: str, title: str) -> str:
    m = re.search(rf"^## {re.escape(title)}\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        sys.exit(f"Seção '## {title}' não encontrada no CONTEXT.md")
    return m.group(1).strip()


def parse_terms(language: str) -> list[tuple[str, list[tuple[str, str, str]]]]:
    """Lista de (grupo, [(termo, definição, evitar)])."""
    groups: list[tuple[str, list]] = []
    current = ("", [])
    for block in re.split(r"\n\s*\n", language):
        block = block.strip()
        if not block:
            continue
        if block.startswith("### "):
            if current[1]:
                groups.append(current)
            current = (block[4:].strip(), [])
            continue
        m = re.match(r"\*\*(.+?)\*\*:\n(.+?)(?:\n_Avoid_: (.+))?$", block, re.S)
        if not m:
            sys.exit(f"Termo fora do formato no CONTEXT.md:\n{block}")
        current[1].append((m.group(1).strip(), " ".join(m.group(2).split()), (m.group(3) or "").strip()))
    if current[1]:
        groups.append(current)
    return groups


def main() -> int:
    ctx = CONTEXT.read_text(encoding="utf-8")
    groups = parse_terms(section(ctx, "Language"))
    ambiguities = [p.strip() for p in re.split(r"\n\s*\n", section(ctx, "Flagged ambiguities")) if p.strip()]
    dialogue = section(ctx, "Example dialogue")
    tecnico = TECNICO.read_text(encoding="utf-8").strip()

    total = sum(len(items) for _, items in groups)
    out = [
        "---\ntitle: Glossário\n---\n",
        "<!-- Gerado por scripts/glossario.py a partir do CONTEXT.md. Não edite à mão: edite o CONTEXT.md. -->\n",
        "# Glossário\n",
        f"Linguagem oficial do Brasil Participativo SaaS e desta documentação: {total} termos, com as palavras a evitar "
        "e as ambiguidades já resolvidas. Use estes termos em textos, telas e código.\n",
        '!!! info "Fonte única"\n'
        "    Esta página é gerada a partir do `CONTEXT.md` do repositório. Para mudar um termo, edite o "
        "`CONTEXT.md` e rode `python3 scripts/glossario.py`.\n",
    ]
    for group, items in groups:
        out.append(f"## {group}\n")
        for term, definition, avoid in items:
            out.append(term)
            out.append(f":   {definition}")
            if avoid:
                out.append(f"\n    *Evite:* {avoid}")
            out.append("")
    out.append("## Ambiguidades resolvidas\n")
    out.append("Palavras que aparecem com mais de um sentido no projeto, e o sentido que vale.\n")
    for amb in ambiguities:
        out.append(f"- {' '.join(amb.split())}")
    out.append("")
    out.append('??? example "Diálogo de exemplo"\n')
    out += ["    " + line if line else "" for line in dialogue.splitlines()]
    out.append("")
    out.append("## Termos técnicos\n")
    out.append("Conceitos gerais de tecnologia usados nesta documentação.\n")
    out.append(tecnico)
    DEST.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{total} termos, {len(ambiguities)} ambiguidades → {DEST.relative_to(ROOT)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
