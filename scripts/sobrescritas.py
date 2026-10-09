#!/usr/bin/env python3
"""Gera o inventário de sobrescritas do Decidim no Participa.

Compara cada arquivo de app/, lib/ e config/initializers/ da aplicação (branch main) e das engines do
próprio repositório (decidim-govbr/, decidim-chatbot/) com o arquivo de mesmo caminho nas gems do
Decidim 0.32.1. Quando o caminho existe numa gem, o arquivo do Participa a sobrescreve.
Mede a diferença em linhas para estimar o esforço de atualização do Decidim.

Uso:
  python3 scripts/sobrescritas.py      # gera docs/transferencia/sobrescritas.md
"""

from __future__ import annotations

import difflib
import io
import subprocess
import sys
import tarfile
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from estatisticas import P, PROJETOS, ROOT, git, sync_repo  # noqa: E402

DECIDIM_TAG = "v0.32.1"
UPSTREAM_URL = "https://github.com/decidim/decidim.git"
CORE_URL = "https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main"
SCOPES = ("app/", "lib/", "config/initializers/")
# Engines versionadas no próprio repositório: os caminhos abaixo delas também podem sobrescrever o Decidim.
ENGINES = ("decidim-govbr/", "decidim-chatbot/")


def relative(path: str) -> tuple[str, str]:
    """(caminho relativo à raiz da aplicação ou da engine, origem)."""
    for engine in ENGINES:
        if path.startswith(engine):
            return path[len(engine):], engine.rstrip("/")
    return path, "aplicação"


def core_files(repo: Path) -> dict[str, list[str]]:
    tree = set(git(repo, "ls-tree", "-r", "-d", "--name-only", "main").splitlines())
    paths = [prefix + s.rstrip("/") for prefix in ("", *ENGINES) for s in SCOPES if prefix + s.rstrip("/") in tree]
    data = subprocess.run(["git", "-C", str(repo), "archive", "main", *paths],
                          check=True, capture_output=True).stdout
    files = {}
    with tarfile.open(fileobj=io.BytesIO(data)) as tar:
        for member in tar.getmembers():
            if member.isfile():
                raw = tar.extractfile(member).read()
                files[member.name] = raw.decode("utf-8", errors="replace").splitlines()
    return files


def upstream_dir(cache: Path) -> Path:
    path = cache / f"decidim-{DECIDIM_TAG}"
    if not path.exists():
        subprocess.run(["git", "clone", "--quiet", "--depth", "1", "--branch", DECIDIM_TAG, UPSTREAM_URL, str(path)],
                       check=True)
    return path


def main() -> int:
    cache = ROOT / ".cache" / "estatisticas"
    P.update(PROJETOS["participa"], slug="participa")
    repo = sync_repo(cache)
    upstream = upstream_dir(ROOT / ".cache")
    gems = sorted(p for p in upstream.iterdir() if p.is_dir() and p.name.startswith("decidim-"))

    files = core_files(repo)
    overrides = []
    own = defaultdict(int)
    for path, lines in sorted(files.items()):
        rel, origin = relative(path)
        match = next((g for g in gems if (g / rel).is_file()), None)
        if not match:
            folder = rel.split("/")[1] if rel.startswith("app/") else rel.split("/")[0]
            own[folder if origin == "aplicação" else f"{origin}/{folder}"] += 1
            continue
        original = (match / rel).read_text(encoding="utf-8", errors="replace").splitlines()
        diff = list(difflib.unified_diff(original, lines, lineterm="", n=0))
        added = sum(1 for d in diff if d.startswith("+") and not d.startswith("+++"))
        removed = sum(1 for d in diff if d.startswith("-") and not d.startswith("---"))
        overrides.append({"path": path, "rel": rel, "origin": origin, "gem": match.name, "added": added, "removed": removed,
                          "core_lines": len(lines), "upstream_lines": len(original)})

    by_gem = defaultdict(list)
    for o in overrides:
        by_gem[o["gem"]].append(o)
    identical = [o for o in overrides if o["added"] == 0 and o["removed"] == 0]
    total_changed = sum(o["added"] + o["removed"] for o in overrides)

    def kind(path: str) -> str:
        parts = relative(path)[0].split("/")
        return parts[1] if parts[0] == "app" and len(parts) > 2 else parts[0] + ("/" + parts[1] if len(parts) > 2 else "")

    now = datetime.now(timezone.utc)
    out = [
        "---\ntitle: Inventário de sobrescritas\n---\n",
        f"<!-- Gerado por scripts/sobrescritas.py em {now.isoformat(timespec='seconds')}. Não edite à mão. -->\n",
        "# Inventário de sobrescritas\n",
        f"Arquivos do `participa` (branch `main`) que **substituem** arquivos do Decidim {DECIDIM_TAG[1:]}. "
        "O Rails carrega a versão da aplicação no lugar da versão da gem, então cada um deles precisa ser revisado ao "
        "atualizar o Decidim. Veja o [Plano de atualização tecnológica](atualizacao.md).\n",
        '!!! note "Engines do próprio repositório"\n'
        f"    Arquivos de mesmo caminho dentro de `{'`, `'.join(e.rstrip('/') for e in ENGINES)}` também competem com os do "
        "Decidim. Para eles, a precedência depende da ordem de carregamento das engines; a coluna **Origem** indica "
        "onde cada arquivo está.\n",
        f'!!! info "Gerado em {now.strftime("%d/%m/%Y")}"\n'
        f"    Comparação de `{'`, `'.join(SCOPES)}` (da aplicação e das engines) com as gems do Decidim na tag `{DECIDIM_TAG}`. "
        "Para atualizar, rode `python3 scripts/sobrescritas.py`.\n",
        "## Resumo\n",
        "| Item | Quantidade |\n|---|---:|",
        f"| Arquivos sobrescritos | {len(overrides)} |",
        f"| Linhas diferentes do original (adicionadas + removidas) | {total_changed:,} |".replace(",", "."),
        f"| Sobrescritas idênticas ao original (podem ser removidas) | {len(identical)} |",
        f"| Arquivos próprios, sem equivalente no Decidim | {sum(own.values())} |",
        "\n## Por gem do Decidim\n",
        "Quanto mais linhas diferentes, maior o esforço de atualização.\n",
        "| Gem | Arquivos sobrescritos | Linhas diferentes |\n|---|---:|---:|",
    ]
    for gem, items in sorted(by_gem.items(), key=lambda x: -sum(o["added"] + o["removed"] for o in x[1])):
        out.append(f"| `{gem}` | {len(items)} | {sum(o['added'] + o['removed'] for o in items):,} |".replace(",", "."))

    by_kind = defaultdict(lambda: [0, 0])
    for o in overrides:
        by_kind[kind(o["path"])][0] += 1
        by_kind[kind(o["path"])][1] += o["added"] + o["removed"]
    out.append("\n## Por tipo de arquivo\n")
    out.append("| Tipo | Arquivos | Linhas diferentes |\n|---|---:|---:|")
    for k, (n, c) in sorted(by_kind.items(), key=lambda x: -x[1][1]):
        out.append(f"| `{k}` | {n} | {c:,} |".replace(",", "."))

    out.append("\n## As 40 sobrescritas mais alteradas\n")
    out.append("| Arquivo | Origem | Gem | + | − | Linhas no Participa |\n|---|---|---|---:|---:|---:|")
    for o in sorted(overrides, key=lambda o: -(o["added"] + o["removed"]))[:40]:
        out.append(f"| [`{o['rel']}`]({CORE_URL}/{o['path']}) | {o['origin']} | `{o['gem']}` | {o['added']} | {o['removed']} | {o['core_lines']} |")

    if identical:
        out.append("\n## Sobrescritas idênticas ao original\n")
        out.append(f"Estes arquivos são iguais aos do Decidim {DECIDIM_TAG[1:]}. Podem ser removidos sem mudar o "
                   "comportamento, o que reduz o trabalho de atualização.\n")
        out += [f"- `{o['path']}` (`{o['gem']}`)" for o in identical]

    out.append("\n## Lista completa por gem\n")
    for gem, items in sorted(by_gem.items()):
        out.append(f'??? note "`{gem}` — {len(items)} arquivos"\n')
        out.append("    | Arquivo | + | − |\n    |---|---:|---:|")
        out += [f"    | `{o['path']}` | {o['added']} | {o['removed']} |" for o in sorted(items, key=lambda o: o["path"])]
        out.append("")

    out.append("## Arquivos próprios\n")
    out.append("Arquivos sem equivalente no Decidim (código exclusivo do Participa), por pasta:\n")
    out.append("| Pasta | Arquivos |\n|---|---:|")
    out += [f"| `{k}` | {v} |" for k, v in sorted(own.items(), key=lambda x: -x[1])]

    dest = ROOT / "docs" / "transferencia" / "sobrescritas.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{len(overrides)} sobrescritas, {len(identical)} idênticas, {total_changed} linhas diferentes → {dest}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
