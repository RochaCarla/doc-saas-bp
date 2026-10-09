# Documentação do Brasil Participativo SaaS

Documentação técnica do **Participa**, plataforma multi-organização sobre o Decidim 0.32.1, e da **participação multicanal** (API OP-BP, painel e app para WhatsApp e Telegram), produzida pelo LabLivre/UnB.

Site: <https://rochacarla.github.io/doc-saas-bp/> · E-book: [PDF](https://rochacarla.github.io/doc-saas-bp/documentacao-brasil-participativo-saas.pdf)

## Conteúdo

- **Documentação**: visão geral, arquitetura do sistema, glossário; Participa (multi-organização, módulos, chatbot, órgãos e setores, implantação, configuração, banco de dados); participação multicanal (canais, roteiros de conversa, votação, integração, painel, dados, implantação)
- **Transferência**: inventário, operação, segurança e LGPD, APIs, release, testes, atualização, sobrescritas, decisões e repasse
- **Inovação** e **Estatísticas** dos dois projetos

## Rodar localmente

```bash
docker compose up                              # http://localhost:8000/doc-saas-bp/
docker compose run --rm docs build --strict    # mesmo build do CI
./scripts/pdf.sh                               # e-book em dist/
```

Sem Docker: `pip install "mkdocs>=1.6,<2" "mkdocs-material==9.7.7" "mkdocs-print-site-plugin==2.9" && mkdocs serve`.

## Páginas geradas

| Script | Gera |
|--------|------|
| `scripts/estatisticas.py` | `docs/estatisticas/` (os dois projetos) |
| `scripts/banco_de_dados.py --out docs/participa/banco-de-dados` | Dicionário de dados do Participa |
| `scripts/sobrescritas.py` | `docs/transferencia/sobrescritas.md` |
| `scripts/glossario.py` | `docs/visao-geral/glossario.md`, a partir do `CONTEXT.md` |

Não edite essas páginas à mão.

## Especificação e linguagem

- [`SPEC.md`](SPEC.md): escopo, fontes, geradores, e-book e requisitos.
- [`CONTEXT.md`](CONTEXT.md): termos canônicos e ambiguidades; fonte do Glossário.

## Uso de IA

Produzida com apoio de IA generativa, sob direção e revisão da equipe. Veja [`docs/sobre/uso-de-ia.md`](docs/sobre/uso-de-ia.md).

## Licença

- Conteúdo: [CC BY 4.0](LICENSE-CONTEUDO.txt), exceto logos e marcas institucionais.
- Código desta documentação: [AGPLv3](LICENSE).
