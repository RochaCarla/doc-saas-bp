# Especificação — Documentação técnica do Brasil Participativo SaaS

Especificação "como construída" desta documentação: escopo, fontes, geradores, e-book e requisitos com critérios de aceitação. A linguagem do domínio está no [CONTEXT.md](./CONTEXT.md). Esta documentação replica a estrutura da [documentação do Brasil Participativo](https://github.com/lablivre-unb/doc-bp), com as adaptações listadas na § 10.

Atualize este arquivo quando o escopo ou os requisitos mudarem.

## 1. Escopo

Documentar, em português, dois projetos do LabLivre/UnB que formam o Brasil Participativo SaaS:

| Projeto | Repositório | Foco |
|---------|-------------|------|
| Participa | `gitlab.com/lappis-unb/decidimbr/participa` | Plataforma multi-organização sobre o Decidim 0.32.1 |
| Participação multicanal | `gitlab.com/lappis-unb/decidimbr/multi-channel-participation` | API OP-BP, painel administrativo e app de participação |

Fora do escopo: o core do Brasil Participativo (`decidim-govbr`, documentado no `doc-bp`), o repositório `infra/decidim-saas` (não analisado) e manuais de uso para participantes.

## 2. Personas e uso dominante

| Persona | Uso dominante | Ponto de entrada |
|---|---|---|
| Desenvolvedor do Participa | "Como subo o ambiente e onde mudo este comportamento sem sobrescrever o Decidim?" | Trilhas, Participa |
| Desenvolvedor da participação multicanal | "Como funciona a API e como altero um roteiro?" | Trilhas, Participação multicanal |
| Equipe de operação | "Como implanto, crio uma organização e recupero as plataformas?" | Participa › Implantação, Transferência › Operação |
| Gestor de processo | "Como uso órgãos e setores, participação efêmera, chatbot e roteiros?" | Trilhas › Gestor de processo |
| **Equipe receptora** | "O que preciso receber, decidir e saber para assumir as plataformas?" | Transferência |
| Gestão e pesquisa | "O que mudou em relação ao Brasil Participativo e como estão os projetos?" | Inovação, Estatísticas |

## 3. Fontes de conteúdo

| Fonte | Uso |
|---|---|
| `participa`, branch `main` (commit `9253a99`, 2026-10-07) | Participa, banco, sobrescritas, estatísticas |
| `multi-channel-participation`, branch `main` (commit `cad204d`, 2026-09-14) | Participação multicanal, estatísticas |
| Gems do `Gemfile` do Participa, nas revisões travadas no `Gemfile.lock` | Módulos, multi-organização |
| Decidim, tag `v0.32.1` | Inventário de sobrescritas |
| API pública do GitLab, rubygems.org, pypi.org, endoflife.date | Estatísticas e qualidade |
| Documentação do Brasil Participativo (`doc-bp`) | Comparações em Inovação |

Toda afirmação técnica cita arquivo, linha ou commit. O que não tem fonte é marcado **a confirmar**.

## 4. Arquitetura da informação

| Aba | Conteúdo |
|---|---|
| Início | Home, trilhas por perfil, novidades |
| Documentação | Visão Geral (sobre, arquitetura do sistema, glossário), Participa (14 páginas e Banco de Dados), Participação multicanal (10 páginas) |
| Transferência | Pacote de transferência: índice, inventário, operação, segurança, APIs, release, testes, atualização, sobrescritas (gerada), decisões, repasse |
| Inovação | Índice, Participa, Participação multicanal |
| Estatísticas | Resumo e cinco páginas por projeto (geradas) |
| Sobre | Origem, licenças, uso de IA |

## 5. Geradores

Scripts em `scripts/`, só com a biblioteca padrão do Python. Clonam os repositórios em `.cache/`.

| Script | Entrada | Saída |
|---|---|---|
| `estatisticas.py` | Git e API do GitLab de cada projeto em `PROJETOS` (`--projeto` para um só) | `docs/estatisticas/index.md` e `docs/estatisticas/<projeto>/*.md` |
| `banco_de_dados.py` | `db/schema.rb` e `db/migrate/` do Participa | `docs/participa/banco-de-dados/*.md`, exceto `consultas.md` (rode com `--out docs/participa/banco-de-dados`) |
| `sobrescritas.py` | Participa (aplicação e engines) × Decidim `v0.32.1` | `docs/transferencia/sobrescritas.md` |
| `glossario.py` | `CONTEXT.md` e `scripts/glossario_tecnico.md` | `docs/visao-geral/glossario.md` |
| `gerar_pdf.cjs` | Site construído | E-book em PDF |
| `medir_diagramas.py` | Site construído | Verificação da largura dos diagramas |

As verificações de qualidade das estatísticas têm duas pilhas: `decidim` (Ruby, Rails, Decidim, RuboCop) e `python` (Python, Node, FastAPI, Ruff e mypy).

## 6. Interface

Mesmo tema do `doc-bp`: tokens do Design System gov.br (`docs/stylesheets/custom.css`), aviso no topo e rodapé de página (`overrides/main.html`), rodapé institucional (`overrides/partials/bp-institucional.html`, configurado em `extra.institucional`).

## 7. E-book

Gerado do `/print_page/` pelo `scripts/gerar_pdf.cjs`: capa, folha de rosto com ficha técnica e "Como citar", apresentação, sumário, miolo numerado e contracapa (`overrides/print/`). Publicado como `documentacao-brasil-participativo-saas.pdf`.

## 8. Build e publicação

MkDocs `>=1.6,<2`, Material 9.7.7 e `mkdocs-print-site-plugin` 2.9, fixos no `Dockerfile`, no `pyproject.toml` e no `.github/workflows/deploy.yml`. O CI roda `mkdocs build --strict`, gera o PDF (sem bloquear o deploy) e publica no GitHub Pages em `rochacarla.github.io/doc-saas-bp`.

## 9. Requisitos

**Funcionais**

| ID | Requisito |
|---|---|
| RF01 | O site DEVE organizar o conteúdo nas seis abas da § 4. |
| RF02 | O site DEVE oferecer busca em português em todo o conteúdo. |
| RF03 | Toda página, exceto a home, DEVE ter o rodapé de página com reportar problema, baixar PDF e sugerir edição. |
| RF04 | O e-book DEVE conter todas as páginas do site, exceto a home, na estrutura da § 7. |
| RF05 | Toda página gerada DEVE ser reproduzível pelo seu script, sem edição manual. |
| RF06 | As Estatísticas DEVEM cobrir cada projeto desde o mês do primeiro commit e informar a data da coleta. |
| RF07 | O Banco de Dados DEVE documentar todas as tabelas do `db/schema.rb` do Participa, com origem e divergências em relação às migrações. |
| RF08 | A Transferência DEVE listar cada documento exigido e sua situação, e as decisões pendentes. |
| RF09 | O Glossário publicado DEVE ser gerado do `CONTEXT.md`. |
| RF10 | O rodapé institucional DEVE exibir Realização e Parceria a partir de `extra.institucional`. |

**Não funcionais**

| ID | Requisito |
|---|---|
| RNF01 | Todo o conteúdo DEVE estar em português do Brasil. |
| RNF02 | O build estrito NÃO PODE emitir avisos. |
| RNF03 | Nenhum diagrama PODE ser reduzido a menos de 85% do tamanho natural na coluna de conteúdo. |
| RNF04 | Afirmações técnicas DEVEM ter fonte verificável; desempenho DEVE ser rotulado como medido ou inferido. |
| RNF05 | O repositório NÃO PODE conter valores de segredos, e-mails de contribuidores ou dados pessoais. |
| RNF06 | As versões de ferramentas DEVEM ser fixas e iguais no Docker e no CI. |
| RNF07 | O site DEVE ser servido inteiramente pelo GitHub Pages. |
| RNF08 | O site e o e-book NÃO PODEM detalhar vulnerabilidades ainda não corrigidas; exibem só um aviso neutro que aponta para o canal restrito (ADR 0001). |

**Critérios de aceitação**

| ID | Critério verificável |
|---|---|
| RF01 | O `nav:` do `mkdocs.yml` tem exatamente as seis abas da § 4. |
| RF02 | Buscar "organização" retorna o Glossário e Multi-organização. |
| RF03 | O HTML de qualquer página, exceto `/`, contém `bp-page-footer` com os três links. |
| RF04 | `./scripts/pdf.sh` termina com "PDF gerado"; a primeira página é a capa e a última, a contracapa. |
| RF05 | Rodar os quatro scripts Python não produz diferença no `git diff`, salvo datas de coleta e números que mudaram na fonte. |
| RF06 | `docs/estatisticas/index.md` mostra o início da série de cada projeto. |
| RF07 | O número de tabelas em `docs/participa/banco-de-dados/index.md` é igual ao de `create_table` no `db/schema.rb`. |
| RF08 | `docs/transferencia/decisoes.md` tem a seção "Decisões pendentes". |
| RF09 | `python3 scripts/glossario.py` não produz diferença em `docs/visao-geral/glossario.md`. |
| RNF02 | `docker compose run --rm docs build --strict` termina sem `WARNING`. |
| RNF05 | `grep -rE "@(gmail|hotmail|protonmail)\.com" docs` não retorna nada. |
| RNF08 | `docs/transferencia/seguranca.md` tem o aviso de canal restrito, e nenhuma página descreve como explorar uma falha aberta. |

## 10. Decisões

| Decisão | Motivo |
|---|---|
| Replicar a estrutura do `doc-bp` (tema, rodapé, e-book, geradores, SPEC, CONTEXT) | Pedido da equipe; mesma experiência nas duas documentações |
| Nome "Brasil Participativo SaaS" | Escolha da equipe; o primeiro parágrafo explica Participa e participação multicanal |
| Publicar em `rochacarla.github.io/doc-saas-bp` | Escolha da equipe; trocar o endereço exige atualizar `site_url`, os links absolutos e o e-book |
| Conteúdo sob CC BY 4.0 e código sob AGPLv3 (no lugar do MIT inicial) | Mesmo licenciamento do `doc-bp` |
| Sem abas Manual de Uso, Design System e Estudos | Não há guias públicos nem estudos sobre os dois projetos; o Design System está na engine gov.br |
| Estatísticas por projeto, com série desde o primeiro commit | Projetos recentes (2025 e 2026), sem fase anterior a excluir |
| Vulnerabilidades em issues confidenciais (ADR 0001) | Mesma regra do `doc-bp` |

## 11. Regras editoriais

- Termos do `CONTEXT.md` em todas as páginas; depois de editá-lo, rode `python3 scripts/glossario.py`.
- Diga sempre de qual plataforma se trata quando o termo muda de sentido (órgão, setor, efêmero, `decidim-govbr`).
- Commits com IA levam `Co-Authored-By`; veja `docs/sobre/uso-de-ia.md`.

## 12. Riscos

| Risco | Mitigação |
|---|---|
| Código muda depressa (chatbot entrou na `main` às vésperas da coleta) | Commits de coleta citados em Sobre; geradores reexecutáveis |
| Partes da produção fora dos repositórios | Marcadas **a confirmar** no Inventário e na Implantação |
| Endereço do site muda se o repositório for transferido | Endereço concentrado em `site_url`, links da home, de Sobre e do rodapé |

## 13. Questões em aberto

- Uma ou duas soluções de WhatsApp (chatbot × API OP-BP).
- Conteúdo do repositório `infra/decidim-saas` e manifestos de produção da API OP-BP e dos front-ends.
- Licença da participação multicanal.
- Transferência deste repositório para a organização `lablivre-unb`, como no `doc-bp`.

## 14. Verificação

```bash
docker compose run --rm docs build --strict
python3 scripts/estatisticas.py
python3 scripts/banco_de_dados.py --out docs/participa/banco-de-dados
python3 scripts/sobrescritas.py
python3 scripts/glossario.py
./scripts/pdf.sh
```
