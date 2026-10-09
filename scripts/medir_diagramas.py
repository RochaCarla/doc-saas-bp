#!/usr/bin/env python3
"""Mede a legibilidade dos diagramas Mermaid da documentação (SPEC.md, RNF03).

Renderiza cada bloco ```mermaid de docs/ com o Mermaid 11 (o mesmo do site) no Google Chrome
em modo headless, lê a largura natural de cada SVG e calcula a escala com que ele aparece na
coluna de conteúdo do site (cerca de 690 px). Termina com código 1 se algum diagrama ficar
abaixo da escala mínima.

Uso:
  python3 scripts/medir_diagramas.py            # todos os diagramas
  python3 scripts/medir_diagramas.py --min 0.9  # escala mínima diferente

Requer o Google Chrome (CHROME=/caminho/do/chrome para outro executável) e acesso à internet
(o Mermaid é carregado do jsDelivr).
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import subprocess
import sys
import tempfile
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COLUMN = 690
CHROME_CANDIDATES = [
    os.environ.get("CHROME", ""),
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "google-chrome", "google-chrome-stable", "chromium", "chromium-browser",
]

PAGE = """<!doctype html><html><head><meta charset="utf-8">
<style>body{{font-family:Raleway,sans-serif;width:3000px}}</style></head><body>
{blocks}
<pre id="result">PENDING</pre>
<script type="module">
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
mermaid.initialize({{startOnLoad:false, securityLevel:'loose', fontFamily:'Raleway, sans-serif'}});
const res = {{}};
let n = 0;
for (const el of document.querySelectorAll('pre.mermaid')) {{
  try {{
    const {{svg}} = await mermaid.render('r' + (n++), el.textContent);
    const m = svg.match(/viewBox="([-\\d.]+) ([-\\d.]+) ([\\d.]+) ([\\d.]+)"/);
    res[el.id] = m ? {{w: Math.round(+m[3]), h: Math.round(+m[4])}} : {{err: 'sem viewBox'}};
  }} catch (e) {{ res[el.id] = {{err: String(e).slice(0, 160)}}; }}
}}
document.getElementById('result').textContent = JSON.stringify(res);
</script></body></html>"""


def find_chrome() -> str:
    for c in CHROME_CANDIDATES:
        if c and (Path(c).exists() or subprocess.run(["which", c], capture_output=True).returncode == 0):
            return c
    sys.exit("Google Chrome não encontrado. Defina CHROME=/caminho/do/chrome.")


def collect() -> list[dict]:
    items = []
    for f in sorted((ROOT / "docs").rglob("*.md")):
        for i, m in enumerate(re.finditer(r"```mermaid\n(.*?)```", f.read_text(encoding="utf-8"), re.S)):
            items.append({"id": f"d{len(items)}", "file": str(f.relative_to(ROOT)), "idx": i, "src": m.group(1)})
    return items


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--min", type=float, default=0.85, help="escala mínima aceita (padrão 0,85)")
    args = parser.parse_args()

    items = collect()
    chrome = find_chrome()
    with tempfile.TemporaryDirectory() as tmp:
        blocks = "\n".join(f'<pre class="mermaid" id="{it["id"]}">{html.escape(it["src"])}</pre>' for it in items)
        Path(tmp, "page.html").write_text(PAGE.format(blocks=blocks), encoding="utf-8")
        server = ThreadingHTTPServer(("127.0.0.1", 0), partial(SimpleHTTPRequestHandler, directory=tmp))
        threading.Thread(target=server.serve_forever, daemon=True).start()
        try:
            dom = subprocess.run(
                [chrome, "--headless=new", "--disable-gpu", f"--user-data-dir={tmp}/profile",
                 "--virtual-time-budget=120000", "--dump-dom",
                 f"http://127.0.0.1:{server.server_address[1]}/page.html"],
                capture_output=True, text=True, timeout=300).stdout
        finally:
            server.shutdown()

    found = re.search(r'<pre id="result">([^<]*)', dom)
    if not found or found.group(1) == "PENDING":
        sys.exit("Não foi possível renderizar os diagramas (Chrome ou rede indisponível).")
    result = json.loads(html.unescape(found.group(1)))

    failures = 0
    for it in items:
        r = result.get(it["id"], {"err": "sem resultado"})
        if "err" in r:
            failures += 1
            print(f"ERRO    {it['file']} #{it['idx']}: {r['err']}")
            continue
        scale = min(1.0, COLUMN / r["w"]) if r["w"] else 0.0
        ok = scale >= args.min
        failures += not ok
        print(f"{'ok  ' if ok else 'LARGO'}   {scale:4.2f}  {r['w']:>5}×{r['h']:<5} {it['file']} #{it['idx']}")
    print(f"\n{len(items)} diagramas; {failures} abaixo da escala mínima {args.min:.2f} ou com erro.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
