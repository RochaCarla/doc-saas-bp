# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Documentation site for **Brasil Participativo SaaS**, made of two LabLivre/UnB projects:

- **Participa** — multi-organization (one PostgreSQL schema per organization) platform on Decidim 0.32.1: [gitlab.com/lappis-unb/decidimbr/participa](https://gitlab.com/lappis-unb/decidimbr/participa)
- **Participação multicanal** — API OP-BP (FastAPI), admin panel and participation app for WhatsApp and Telegram: [gitlab.com/lappis-unb/decidimbr/multi-channel-participation](https://gitlab.com/lappis-unb/decidimbr/multi-channel-participation)

Sister site of the Brasil Participativo documentation ([lablivre-unb/doc-bp](https://github.com/lablivre-unb/doc-bp)), with the same structure, theme, generators and e-book.

## Spec and domain language

- `SPEC.md`: as-built specification (scope, sources, generators, e-book, requirements with acceptance criteria). Update it when scope or requirements change.
- `CONTEXT.md`: domain glossary, the single source for the site's Glossário. Use its terms in every page; after editing it, run `python3 scripts/glossario.py`. Several terms differ from doc-bp (órgão, setor, efêmero, `decidim-govbr`); check the flagged ambiguities.
- `docs/sobre/uso-de-ia.md`: AI usage statement and rules for AI-assisted contributions.
- `docs/adr/`: decisions about this documentation (excluded from the site).

## Build & Development Commands

```bash
# Local dev server with Docker (hot-reload) → http://localhost:8000/doc-saas-bp/
docker compose up

# Strict build (same check as CI)
docker compose run --rm docs build --strict

# Without Docker
pip install "mkdocs>=1.6,<2" "mkdocs-material==9.7.7" "mkdocs-print-site-plugin==2.9" && mkdocs serve

# E-book PDF (print_page + Puppeteer) → dist/
./scripts/pdf.sh

# Regenerate generated sections (stdlib-only Python; clones repos into .cache/)
python3 scripts/estatisticas.py                                   # docs/estatisticas/ (both projects; --projeto to pick one)
python3 scripts/banco_de_dados.py --out docs/participa/banco-de-dados   # Participa data dictionary (except consultas.md)
python3 scripts/sobrescritas.py                                   # docs/transferencia/sobrescritas.md (vs Decidim v0.32.1)
python3 scripts/glossario.py                                      # docs/visao-geral/glossario.md (from CONTEXT.md)
```

No tests or linter configured in this repo. CI runs `mkdocs build --strict` (versions pinned in `.github/workflows/deploy.yml`, MkDocs < 2) on push to main and deploys to GitHub Pages.

## Architecture

- **Config**: `mkdocs.yml` — nav, theme, plugins, `extra.institucional` (footer)
- **Content**: `docs/` — `visao-geral/`, `participa/`, `multicanal/`, `transferencia/`, `inovacao/`, `estatisticas/`, `sobre/`
- **Generated pages** (never edit by hand): `docs/estatisticas/**`, `docs/participa/banco-de-dados/*` (except `consultas.md`), `docs/transferencia/sobrescritas.md`, `docs/visao-geral/glossario.md`
- **Theme**: gov.br Design System tokens in `docs/stylesheets/custom.css`; `overrides/` for announcement, page footer, institutional footer and e-book cover/back cover
- **Deploy**: GitHub Actions → GitHub Pages at `rochacarla.github.io/doc-saas-bp`

## Conventions

- **Language**: all content in Brazilian Portuguese (pt-BR)
- **Commit messages**: Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`)
- **Navigation**: any new page must be added to `nav:` in `mkdocs.yml`. Top tabs: Início, Documentação, Transferência, Inovação, Estatísticas, Sobre
- **Evidence**: technical claims must cite a file, line or commit in the two repos; mark unknowns **a confirmar**; label performance claims measured or inferred
- **Security**: never describe unfixed vulnerabilities on the site (ADR 0001); confidential issue drafts live in `dist/` (gitignored) and must never be committed
- **Diagrams**: Mermaid, preferably vertical (`flowchart TB`)
