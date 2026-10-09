# Módulos e gems

O Participa monta a plataforma com três tipos de peça: módulos oficiais do Decidim, gems do Brasil Participativo e de terceiros (instaladas a partir de repositórios git) e duas engines versionadas no próprio repositório.

## Módulos do Decidim (0.32.1)

| Módulo | Como entra | Para quê |
|--------|-----------|----------|
| `core`, `admin`, `system`, `api`, `verifications`, `generators` | Gem `decidim` | Núcleo, painéis, API GraphQL, verificações |
| `participatory_processes`, `assemblies` | Gem `decidim` | Processos participativos e instâncias |
| `proposals`, `meetings`, `comments`, `forms`, `surveys`, `budgets`, `accountability`, `debates`, `blogs`, `pages` | Gem `decidim` | Componentes |
| `initiatives` | `Gemfile` | Iniciativas |
| `conferences` | `Gemfile` | Espaço de conferências do Decidim (diferente do tipo de processo Conferência) |
| `elections` | `Gemfile` | Eleições, reescritas no Decidim 0.32; entraram na versão `0.32.1-v1.0.0` |

Não estão instalados: `decidim-ai`, `decidim-collaborative_texts`, `decidim-demographics`, `decidim-design` e `decidim-templates`. O banco ainda guarda uma tabela de sorteios, módulo que não existe mais no Decidim 0.32.

## Gems instaladas a partir de git

Todas seguem uma **branch**, não uma tag: um `bundle update` pode trazer código novo sem mudança no `Gemfile`. O que vale é o commit travado no `Gemfile.lock`.

| Gem | Origem | Branch | O que faz |
|-----|--------|--------|-----------|
| `decidim-bp_proposals` | LabLivre | `main` | Comentários em propostas controlados por etapa |
| `decidim-bp_meetings` | LabLivre | `main` | Criação, comentários e anexos de reuniões controlados por etapa; participante pode anexar arquivos à própria reunião |
| `decidim-bp_comments` | LabLivre | `main` | Respostas oficiais, árvore de dois níveis, edição em até 5 minutos, denúncia restrita, anexos em comentários |
| `decidim-questionnaires` | LabLivre | `main` | Extensões de formulários: perguntas obrigatórias, duplicar, exportar e importar perguntas, limite de arquivos, e-mail de confirmação, exportação em CSV em lotes |
| `decidim-participatory_texts` | LabLivre | `main` | Componente [Texto participativo](texto-participativo.md) |
| `decidim-community_templates` | Fork LabLivre de `decidim-ice/decidim-module-community_templates` | `core/bump-32` | [Modelos de processo](modelos.md) |
| `decidim-government_spaces` | LabLivre | `main` | [Órgãos e setores](orgaos-setores.md) |
| `decidim-categories` | LabLivre | `main` | Categorias hierárquicas por espaço, obrigatórias em propostas e reuniões |
| `decidim-extra_home_blocks` | LabLivre | `main` | Melhorias nos blocos de conteúdo do Decidim (linha do tempo de etapas, banner gov.br 1920×280, estatísticas configuráveis) |
| `decidim-extra_blocks` | LabLivre (cópia de módulo da Octree, **inferido**) | `main` | Galeria de 22 layouts de bloco para páginas iniciais |
| `decidim-toggle` | Octree | `main` | Abas de configuração da organização no `/system` |
| `decidim-ephemeral_participation` | Octree | `main` | [Participação efêmera](participacao-efemera.md) |
| `decidim-apartment` | LabLivre (`infra/participa-gem`) | `v0.1.0-rc` | [Multi-organização](multi-organizacao.md) |
| `omniauth-govbr` | Repositório pessoal no GitHub | `main` | Estratégia OmniAuth do Login Único gov.br, com PKCE |

Fontes: `Gemfile`, seções `GIT` do `Gemfile.lock` e o código de cada gem na revisão travada.

!!! warning "Dependências a fixar"
    Antes da transferência, fixe cada gem numa tag ou commit no `Gemfile` e decida onde fica o `omniauth-govbr`, hoje num repositório pessoal. Veja [Plano de atualização](../transferencia/atualizacao.md).

## Engines do repositório

| Engine | O que faz |
|--------|-----------|
| [`decidim-govbr`](govbr.md) | Login gov.br e CPF, participação efêmera por CPF e nome, layout e cores gov.br, blocos da página inicial, notícias, troca automática de etapa, formulário de processo simplificado |
| [`decidim-chatbot`](chatbot.md) | Chatbot de WhatsApp para votação em propostas |

## Ausentes em relação ao Brasil Participativo

O `decidim-govbr` (0.27.2) instala componentes que o Participa não tem: `decidim-homes` (substituído por blocos de conteúdo), `decidim-ej` (Empurrando Juntas), `decidim-extra_user_fields`, `decidim-module-mobile`, `decidim-enhanced_process_groups_and_scopes` e `decidim-decidim_awesome` (instalado e removido em maio de 2025 por erro de compilação).
