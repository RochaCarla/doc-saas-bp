---
icon: material/lightbulb-on
---

# Inovação

O que o Brasil Participativo SaaS traz de novo em relação ao Brasil Participativo e ao Decidim. Cada afirmação aponta a evidência no código. Afirmações de desempenho são marcadas como **medidas** (com número publicado) ou **inferidas** (conclusão da leitura do código).

<div class="grid cards" markdown>

-   :material-domain:{ .lg .middle } **[Participa](participa.md)**

    ---

    Várias organizações numa instalação, Decidim atual, 31 sobrescritas em vez de 492, órgãos e setores, participação efêmera e chatbot.

-   :material-message-processing:{ .lg .middle } **[Participação multicanal](multicanal.md)**

    ---

    Identificação progressiva, roteiros de conversa editáveis sem reinício, desenho para alta escala e anonimização.

-   :material-format-list-checks:{ .lg .middle } **[Funcionalidades do Participa](funcionalidades-participa.md)**

    ---

    Catálogo completo, por tema, de tudo o que o Participa implementou além do Decidim, com data e evidência.

-   :material-format-list-checks:{ .lg .middle } **[Funcionalidades da participação multicanal](funcionalidades-multicanal.md)**

    ---

    Catálogo completo da API OP-BP, do painel e do app, com data e evidência.

</div>

## Em números

| Indicador | Brasil Participativo | Participa | Fonte |
|-----------|---------------------:|----------:|-------|
| Versão do Decidim | 0.27.2 | 0.32.1 (atual) | `Gemfile.lock` |
| Arquivos do Decidim sobrescritos | 492 | 31 | Inventários gerados pelos dois sites |
| Linhas diferentes do original | cerca de 21 mil | cerca de 2 mil | Idem |
| Organizações por instalação | 1 | Várias | Multi-organização |
| Gems próprias e de terceiros por git | 5 componentes LabLivre | 14 | `Gemfile` |

| Indicador | API OP-BP | Fonte |
|-----------|----------:|-------|
| Participantes por segundo com boa experiência | 150 durante 6 h (**medido**) | `api/tests/load_tests/results/REPORT.md` |
| Capacidade diária estimada pelo relatório | cerca de 1 milhão de participantes | Idem |
| Municípios e propostas no catálogo do Orçamento do Povo | 420 e 4.173 | `api/app/data/decidim_proposals_components.json` |

As medições da API OP-BP são do relatório do próprio repositório, num servidor de 4 CPUs e 32 GB, e não foram reproduzidas nesta documentação.
