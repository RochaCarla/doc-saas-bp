# Engine decidim-govbr

A engine `decidim-govbr/` reúne as customizações de governo do Participa. Ela foi **gerada do zero** em setembro de 2025 com o gerador de módulos do Decidim (commit `b0ad8c3`). Só o nome coincide com o repositório `decidim-govbr` do Brasil Participativo; o código é outro.

Ela depende de `decidim-core`, `decidim-participatory_processes` e `deface`, não cria tabelas e tem 23 arquivos de teste com aplicação de teste própria.

## O que acrescenta

### Identidade e CPF

| Funcionalidade | Como funciona | Onde |
|----------------|---------------|------|
| Login gov.br concede a verificação de CPF | Ao entrar com o gov.br, o participante recebe a verificação por CPF (`verified_by: "govbr"`). Se o CPF era de um participante efêmero, os votos passam para a conta. Se pertence a outra conta ativa, a concessão é recusada | `app/commands/decidim/govbr/grant_govbr_login_authorization.rb` |
| Verificação por CPF e nome | `GovbrAuthorizationHandler`: CPF com dígitos verificadores, nome com ao menos duas palavras e e-mail opcional. O identificador único é um hash do CPF com o segredo da aplicação | `app/services/govbr_authorization_handler.rb` |
| Participante efêmero por CPF | Retoma, cria ou recusa o participante efêmero; exige que o nome confira para retomar | `app/commands/decidim/govbr/identify_ephemeral_participant.rb` |
| Telas de login e verificação | Botão "Entrar com gov.br" no topo e título "Conecte-se" | `app/views/decidim/devise/` e overrides de `verifications/` |

Veja [Participação efêmera](participacao-efemera.md).

### Aparência

| Funcionalidade | Como funciona |
|----------------|---------------|
| Layout gov.br por host | Barra de navegação e rodapé gov.br só nos hosts listados em `GOVBR_LAYOUT_HOSTS`, com busca recolhível, seletor de idiomas e menu do usuário (controladores Stimulus) |
| Cores da organização | 15 cores extras (semânticas, cinzas e fundos) além das 3 do Decidim, com padrão na paleta do Design System gov.br (`lib/decidim/govbr/colors.rb`) |
| Fonte Rawline | Fonte do Design System gov.br (`app/packs/fonts/rawline/`) |
| Tokens do Design System | Copiados em SCSS (`_design_system.scss`). O pacote `@govbr-ds/core` está declarado, mas nenhum JavaScript o importa |

### Página inicial e notícias

| Bloco ou página | O que mostra |
|-----------------|--------------|
| `blog_news` | Notícias de um componente de blog, com post em destaque |
| `open_processes` | Processos abertos em abas por taxonomia, 6 por aba |
| Bloco `hero` | Ganha as opções de esconder o texto de boas-vindas e o botão |
| `/:locale/news` | Página global com os posts de todos os blogs |

### Processos participativos

| Funcionalidade | Como funciona |
|----------------|---------------|
| Troca automática de etapa | Opção por processo (`automatic_step_activation`). Um job de hora em hora percorre todas as organizações e ativa a etapa cujas datas cobrem o momento atual, pelo mesmo comando do botão "Ativar" |
| Formulário simplificado | Descrição curta até 300 caracteres e descrição até 5.000; "Setor" e contato institucional obrigatórios; datas do processo editáveis na tela de etapas |
| Menu do painel | Processos → Grupos → Modelos |
| Taxonomias padrão | `bin/rails "decidim_govbr:taxonomies:participatory_process[HOST]"` cria a raiz "Categorias" e os tipos Plano Participativo, Consulta Pública, Orçamento Participativo, Conselhos e Colegiados e Audiência Pública |

## Como ela altera o Decidim

- **12 sobrescritas** de mesmo caminho (11 views e 1 cell), entre elas o formulário de processo (244 linhas diferentes do Decidim) e a tela de login.
- **10 overrides Deface**, que trocam trechos de views sem copiá-las (cores da organização, cabeçalho e etapas do processo, telas de verificação, classe do `body` e barra de navegação).
- **Extensões por `prepend`** em formulários e comandos de organização e de processo.
- As views da engine têm prioridade sobre as do Decidim (`prepend_view_path` em `lib/decidim/govbr/engine.rb`).

!!! note "A confirmar"
    - `ParticipatoryProcessFormExtensions` e `TaxonomyFormExtensions` são carregados, mas nenhum `include` os aplica: podem ser código morto.
    - O componente `govbr` só é registrado com `ENABLE_GOVBR_COMPONENT=true`, e suas rotas estão vazias. O README da engine ainda o descreve como componente.
    - `layouts/decidim/_head_extra.html.erb` existe na aplicação e na engine; qual dos dois é renderizado nas páginas públicas precisa ser verificado em execução.
