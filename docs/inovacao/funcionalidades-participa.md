# Funcionalidades do Participa

Catálogo de tudo o que o projeto implementou além do Decidim 0.32.1, na branch `main` (commit `9253a99`, 7 de outubro de 2026). Cada linha traz onde a funcionalidade está e quando entrou: a data do merge ou do commit. Funcionalidades que o Decidim já oferece só aparecem quando o Participa as alterou.

Legenda da coluna **Onde**: *app* = aplicação (`app/`, `config/`, `lib/`); *govbr* = engine `decidim-govbr/`; *chatbot* = engine `decidim-chatbot/`; o nome de uma gem indica uma [gem instalada](../participa/modulos.md).

## Plataforma e multi-organização

| Funcionalidade | O que faz | Onde | Desde |
|----------------|-----------|------|-------|
| Um schema por organização | Cada organização num schema PostgreSQL próprio, escolhido pelo host ([Multi-organização](../participa/multi-organizacao.md)) | `decidim-apartment` | ago. 2025 (`feat/one-decidim-one-db`) |
| Criação de organização com o schema | O `/system` cria chave, schema e organização, e desfaz tudo em caso de erro | `decidim-apartment` | ago. 2025 |
| Jobs, cache e arquivos por organização | Jobs levam a organização; cache Redis e pastas S3 separados por organização | `decidim-apartment`, app | ago. 2025 |
| Auditoria de schemas | `apartment:check_column`, `apartment:schema_drift` e `apartment:repair_plan` | app (`lib/tasks/apartment_*.rake`) | set. 2026 |
| Administrador por organização via tarefa | `decidim_admin:create_admin[NOME,EMAIL,SENHA,HOST]` | app (`lib/tasks/seeds.rake`) | mai. 2025 |
| Conteúdo de partida por organização | `decidim_admin:seed_organization[HOST]`: banner, blocos da página inicial, 18 grupos de secretarias, páginas e 4 processos de exemplo | app (`lib/tasks/seeds/seed_rake.json`) | out. 2025 (`rake_organization`) |
| Taxonomias padrão | Raiz "Categorias" e os tipos Plano Participativo, Consulta Pública, Orçamento Participativo, Conselhos e Colegiados e Audiência Pública | govbr (`lib/tasks/taxonomies.rake`) | out. 2025 |
| Abas de configuração da organização | OmniAuth, e-mails, idioma, segurança, upload e autorizações em abas no `/system` | `decidim-toggle` | set. 2026 (`0.32.1-v1.0.1`) |
| Fila e cache em Redis separados | Um Redis para o Sidekiq, outro para o cache | app, Helm | set. 2025 |
| Tarefas em segundo plano | Sidekiq com filas ponderadas | app (`config/sidekiq.yml`) | mai. 2025 |
| Agendamento no Sidekiq | `sidekiq-cron` lendo `config/sidekiq_cron_schedule.yml`, com fuso da aplicação | app | out. 2026 (`release/0.32.1-v1.0.2`) |
| Implantação em Kubernetes | Chart Helm com Puma, Sidekiq, CloudNativePG, Redis e cert-manager ([Implantação](../participa/implantacao.md)) | `deploy/decidim-instance-chart/` | set. a out. 2025 |
| Assets fora da imagem | Job do Helm compila os assets num volume servido por nginx | Helm | **a confirmar** |
| Armazenamento S3/MinIO | Active Storage em S3, uma pasta por organização | app, `decidim-apartment` | mai. 2026 (`fix/add-aws-sdk-s3`) |
| Views pré-compiladas | Deface pré-compilado na imagem e desligado em produção | app (`Dockerfile`) | ago. 2025 (`chore/install-deface`) |
| Análise de desempenho | Pyroscope em produção, inclusive nos jobs do Sidekiq | app (`config/initializers/pyroscope.rb`) | jul. 2026 |
| Análise de uso | Matomo (Tag Manager, condicionado ao consentimento de análise nas páginas públicas) e PostHog | app | set. 2026 |
| Pipeline de imagens e versões | Imagens `dev`, `bump` e de produção; Release no GitLab a cada tag | `.gitlab-ci.yml` | out. 2025 |
| Análises de segurança no CI | Gitleaks, Hadolint, Brakeman, Syft e Grype, com relatório consolidado | `.gitlab-ci.yml` | out. 2025 |

## Login, identidade e participação efêmera

| Funcionalidade | O que faz | Onde | Desde |
|----------------|-----------|------|-------|
| Login gov.br | OAuth2/OpenID Connect com PKCE; CPF vem do `sub` | `omniauth-govbr`, app (`config/initializers/omniauth_govbr.rb`) | ago. 2025 (`add-omniaut-govbr`) |
| Login gov.br por organização | Cliente, segredo, SSO e retorno lidos da configuração da organização a cada requisição | app | ago. 2025 |
| Botão gov.br na tela de login | Botão no topo e título "Conecte-se" | govbr (`app/views/decidim/devise/`) | out. 2025 |
| Participação efêmera | Participar com CPF e nome, sem cadastro completo ([Participação efêmera](../participa/participacao-efemera.md)) | `decidim-ephemeral_participation`, govbr | set. 2025 (`feat/ephemeral`); gem em set. 2026 |
| Validação de CPF e nome | Dígitos verificadores do CPF, nome com duas palavras, e-mail opcional | govbr (`GovbrAuthorizationHandler`) | set. 2026 |
| Retomada só com o mesmo nome | O participante efêmero só é retomado se o nome conferir | govbr (`IdentifyEphemeralParticipant`) | set. 2026 |
| Login gov.br concede a verificação de CPF | Quem entra com o gov.br recebe a verificação atestada pelo gov.br | govbr (`GrantGovbrLoginAuthorization`) | set. 2026 |
| Votos efêmeros passam para a conta | Ao entrar com o gov.br, os votos do participante efêmero vão para a conta, sem quebrar limite nem índice | govbr; app (`authorization_transfer_override.rb`) | set. 2026 |
| Tempo de sessão efêmera no rodapé | Mostra quanto resta e o link para completar o cadastro | app (`footer/_main_links.html.erb`) | set. 2026 |
| Onboarding sem "pular verificação" | Remove o link que deixava pular a verificação | govbr | set. 2026 |
| SSO falso em desenvolvimento | `OMNIAUTH_GOVBR_FAKE=true` troca o gov.br por um formulário local | app | set. 2026 |
| CPF fora dos logs | `cpf`, `document_number`, nome da identidade e payloads de webhook filtrados | app (`filter_parameter_logging.rb`) | set. 2026 |

## Órgãos, setores e gestão

| Funcionalidade | O que faz | Onde | Desde |
|----------------|-----------|------|-------|
| Hierarquia Órgão → Setor | Órgãos, setores e tipos de órgão por organização ([Órgãos e setores](../participa/orgaos-setores.md)) | `decidim-government_spaces` | jun. 2026 (`bump/govspace`) |
| Administradores com escopo | Convite para administrar um órgão ou setor; acesso aos processos da hierarquia, sem excluir | `decidim-government_spaces` | jun. 2026 |
| Setor do processo | Campo de setor no formulário do processo (um setor por processo) | `decidim-government_spaces` | jun. 2026 |
| Páginas públicas de órgãos | `/orgaos` e `/orgaos/setores/:id`; item "Órgãos Públicos" no menu | `decidim-government_spaces`; app (`decidim_home_menu.rb`) | jun. 2026 |
| Categorias hierárquicas | Categorias por espaço, com lixeira; obrigatórias e só em folhas nas propostas e reuniões | `decidim-categories` | jun. 2026 (`bump/categories-govspace`) |

## Processos participativos

| Funcionalidade | O que faz | Onde | Desde |
|----------------|-----------|------|-------|
| Formulário de processo simplificado | Menos campos, descrição curta até 300 caracteres e descrição até 5.000 | govbr | abr. 2026 (`melhoria/formulario-simplificado`) |
| Campos institucionais obrigatórios | "Setor" e contato institucional obrigatórios | govbr | jul. 2026 (`mudanca-de-campos`) |
| Datas do processo na tela de etapas | Edita início e fim do processo junto das etapas | govbr; app (`participatory_process_steps_controller_override.rb`) | jun. 2026 (`refactor-process-date`) |
| Troca automática de etapa | Ativa, de hora em hora, a etapa cujas datas cobrem o momento atual, em todas as organizações | govbr (`step_auto_activation.rb`) | out. 2026 |
| Ordenação de componentes | Componentes do processo em ordem definida | app | mai. 2026 (`ordenacao-componentes`) |
| Menu do painel reordenado | Processos → Grupos → Modelos | govbr (`menu_reorder.rb`) | jul. 2026 |
| Nomes e rótulos de processo | Nomenclatura e rótulos de metadados em português | govbr, app | ago. 2026 |
| Modelos de processo | Catálogo em repositório Git, criação a partir de modelo, publicação de modelos e organização de demonstração ([Modelos](../participa/modelos.md)) | `decidim-community_templates` | nov. 2025 (`feat/install_template`) |
| Cards de modelos | Visual dos cards do catálogo | `decidim-community_templates` | mar. 2026 |
| Importação resiliente de modelos | Peso nulo vira 0; um modelo com erro não aborta os outros; demonstração não é recriada a cada expiração de cache | app (`community_templates_*.rb`) | jul. a set. 2026 |

## Componentes e participação

| Funcionalidade | O que faz | Onde | Desde |
|----------------|-----------|------|-------|
| Texto participativo | Componente próprio: texto colado, parágrafos que se movem, unem, ocultam e se tornam interativos ([Texto participativo](../participa/texto-participativo.md)) | `decidim-participatory_texts` | mai. 2026 |
| Devolutiva por comentário | Cada comentário de parágrafo recebe situação (incorporado, em parte, não) e texto | `decidim-participatory_texts` | jun. 2026 (`bump/participatory_text`) |
| Comentários por etapa | Comentários em propostas e reuniões ligados ou desligados em cada etapa | `decidim-bp_proposals`, `decidim-bp_meetings` | jun. 2026 (`feat/adding_modules`) |
| Criação de reuniões por etapa | Participantes criam reuniões só nas etapas permitidas | `decidim-bp_meetings` | jun. 2026 |
| Anexos em reuniões por etapa | Administrador anexa e público vê; participante anexa à própria reunião | `decidim-bp_meetings` | jun. 2026 |
| Respostas oficiais | Só papéis administrativos respondem comentários; resposta com a etiqueta "Resposta Oficial"; árvore de dois níveis | `decidim-bp_comments` | jun. 2026 |
| Edição de comentários em 5 minutos | Autores comuns editam ou excluem só nos primeiros 5 minutos; administradores sem limite | `decidim-bp_comments`; app | set. 2026 (`feat/edicao-comentarios-tempo-limite-admin`) |
| Anexos em comentários | Configuração de anexos nos componentes com comentário | `decidim-bp_comments` | jun. 2026 |
| Denúncia restrita | Uma denúncia oculta o conteúdo, por isso só papéis administrativos denunciam | `decidim-bp_comments`; app (`report_authorization.rb`) | ago. 2026 |
| Link de comentário moderado | Link correto para o comentário oculto, inclusive em parágrafo de texto participativo | app (`comment_override.rb`) | ago. 2026 (`fix/moderation-hidden-comment-link`) |
| Formulários ampliados | Perguntas obrigatórias em modal, duplicar, exportar e importar perguntas, numeração, contador de respostas | `decidim-questionnaires` | jun. 2026 |
| Limite de arquivos por pergunta | Coluna `max_files` | `decidim-questionnaires` | jun. 2026 |
| E-mail de confirmação de resposta | Participante recebe e-mail ao responder | `decidim-questionnaires` | jun. 2026 |
| Exportação de respostas em lotes | CSV por *streaming* e consultas em lotes | `decidim-questionnaires` | jun. 2026 |
| Download de anexos de formulários | Correção do download de anexos das respostas | app | ago. 2026 (`fix/form-attachments-download`) |
| Orçamentos: conclusão do voto | Regras de conclusão com mínimo de projetos ou orçamento zerado; correção da permissão de voto do 0.32.1 | app (`budgets/*_override.rb`) | set. 2026 (`fix/conclusao-votacao-orcamento-op`) |
| Orçamentos: modal e botão de voto | Modal de informações após votar, botão de voto próprio e contraste WCAG no resumo | app | ago. 2026 (`fix/orcamentos-pos-votacao-modal`) |
| Vídeos em reuniões | Aceita `youtu.be` e `youtube.com` sem `www` na incorporação | app (`meeting_iframe_embedder_override.rb`) | jul. 2026 |
| Seletor de data e hora | Seletores com tradução e botões que não se sobrepõem ao rodapé | app (`generate_*picker.js`) | ago. a set. 2026 |
| Iniciativas | Módulo de iniciativas do Decidim habilitado | `decidim-initiatives` | jul. 2026 |
| Conferências | Espaço de conferências do Decidim habilitado | `decidim-conferences` | ago. 2026 |
| Eleições | Módulo de eleições do Decidim 0.32 habilitado | `decidim-elections` | set. 2026 (`0.32.1-v1.0.1`) |

## Página inicial e conteúdo

| Funcionalidade | O que faz | Onde | Desde |
|----------------|-----------|------|-------|
| Página inicial com blocos próprios | Subcomponentes da página inicial e conteúdo de partida | govbr, app | out. 2025 (`feat/homepage`) |
| Bloco de estatísticas | Estatísticas com título configurável e itens ocultáveis | govbr; `decidim-extra_home_blocks` | nov. 2025 (`feat/stats_design`) |
| Bloco de processos abertos | Abas por tipo de processo, 6 por aba; estado vazio e acessibilidade nas abas acrescentados em ago. 2026 | govbr (`open_processes`) | out. 2025 |
| Bloco de notícias | Notícias de um blog com post em destaque; botão "ver mais" e título em destaque acrescentados em ago. e set. 2026 | govbr (`blog_news`) | out. 2025 |
| Página global de notícias | `/:locale/news` com posts de todos os blogs e seletor de destaque | govbr (`news_controller.rb`) | out. 2026 |
| Banner na proporção gov.br | Banner da página inicial recortado em 1920×280 | `decidim-extra_home_blocks` | jun. 2026 (`design/change_banner_width`) |
| Bloco hero configurável | Esconder texto de boas-vindas e botão | govbr | set. 2026 |
| Linha do tempo de etapas | Bloco "Etapa e duração" com a linha do tempo das etapas | `decidim-extra_home_blocks` | jun. 2026 |
| Galeria de layouts | 22 layouts de bloco (CTA, Hero, Proposta rápida, Vídeo, Roadmap, Logos…) para páginas iniciais | `decidim-extra_blocks` | set. 2026 |
| Reuniões sem mapa no destaque | Bloco de reuniões em destaque sem o mapa | govbr | ago. 2026 |

## Aparência e Design System gov.br

| Funcionalidade | O que faz | Onde | Desde |
|----------------|-----------|------|-------|
| Tema gov.br | Tokens do Design System em SCSS, sobre o Tailwind do Decidim 0.32 | govbr | jun. 2026 (`feat/govbr-ds-poc`) |
| Painel adaptado | Estilo do Design System também no painel administrativo | govbr | jun. 2026 |
| Barra de navegação gov.br | Busca recolhível, seletor de idiomas e menu do usuário (Stimulus) | govbr | jun. 2026 (`feat/govbr-navbar`) |
| Layout gov.br por host | Só nos hosts de `GOVBR_LAYOUT_HOSTS` | govbr | set. 2026 (`feat/govbr-colors-and-layout`) |
| Cores da organização | 15 cores extras com padrão na paleta gov.br, editáveis no painel | govbr (`colors.rb`) | ago. a set. 2026 |
| Fonte Rawline | Fonte do Design System gov.br | govbr | out. 2025 |
| Tela de verificação gov.br | Botão "Entrar com gov.br" e textos próprios | govbr (Deface) | out. 2025 |
| Login responsivo | Tela de login ajustada para celular | govbr | jul. 2026 |

## Chatbot de WhatsApp

| Funcionalidade | O que faz | Onde | Desde |
|----------------|-----------|------|-------|
| Módulo de chatbot | Entrada no painel acima de "Moderações globais", só para administradores da organização ([Chatbot](../participa/chatbot.md)) | chatbot | out. 2026 (`feat/chatbot-admin-module`) |
| Provedores de mensageria | Provedores declarados em código, com configuração cifrada, ligar, desligar e testar | chatbot | set. 2026 |
| WhatsApp do SERPRO | Autenticação OAuth e quatro tipos de mensagem: texto, botões, lista e link | chatbot | set. 2026 |
| Registro do webhook | Registrar no SERPRO pelo painel e listar os últimos eventos | chatbot | set. 2026 |
| Recebimento seguro | Webhook com Basic Auth, descarte de repetidas, limite por telefone e fora do limite por IP | chatbot | set. 2026 |
| Uma conversa por pessoa | Máquina de estados do roteiro de 15 estados, uma pessoa por vez | chatbot | set. 2026 |
| Lembrete e silêncio | Relembra o passo sem resposta e silencia após três tentativas; trata mídia | chatbot | set. 2026 |
| Propostas como opções de voto | Escolha do componente e lista das propostas no WhatsApp | chatbot | set. 2026 |
| Identificação por CPF e nome | Página de identificação de uso único que cria ou retoma o participante efêmero | chatbot | set. 2026 |
| Identificação por gov.br | Link para o login gov.br e voto como a conta atestada, logo após o login | chatbot | set. a out. 2026 |
| Voto real no Decidim | Mesmo comando e permissões do site; um voto por participante | chatbot | set. 2026 |
| "Já participou" | Responde após o encerramento e trava o voto | chatbot | set. 2026 |
| Ranking pelos votos do Decidim | Ranking e contagem de votos do chat na visão geral | chatbot | set. 2026 |
| Assistente de textos | Quatro passos (geral, propostas, suporte, publicar), prévia num celular simulado, caminhos de exemplo e simulação | chatbot | set. 2026 |
| Rascunho e publicação | Rascunho do roteiro e publicação aos participantes; restaurar textos padrão | chatbot | set. 2026 |
| Visão geral | Números em cache, situação ligado ou desligado e lista "Para colocar no ar" com 9 itens | chatbot | set. 2026 |
| Simulador no terminal | `chatbot:simulate` imita o WhatsApp | chatbot | set. 2026 |
| Comando de reinício para testes | Reinicia a conversa e desfaz o voto, só fora de produção | chatbot | set. 2026 |

## E-mail, mapas e dados

| Funcionalidade | O que faz | Onde | Desde |
|----------------|-----------|------|-------|
| Boletim com mídia | Imagens com URL absoluta e vídeos trocados por link com miniatura | app (`newsletter_email_body.rb`, `mailer_helper_override.rb`) | out. 2026 |
| Mapas HERE e OSM | Geocodificação e autocompletar com HERE; mapa estático HERE; blocos OSM; Photon sem chave | app (`config/initializers/geocoder.rb`) | ago. a set. 2026 |
| Dados abertos | Correção da página de dados abertos; exportação por organização | app; `decidim-apartment` | set. 2026 |
| Imagem maior nos cards de proposta | Card usa a variante `:big` | app (`proposal_g_cell_override.rb`) | set. 2026 |
| Traduções pt-BR | Painel, processos, formulários, modelos e chaves sem tradução no Decidim | app (`config/locales/`) | contínuo |

## Removidas ou movidas

| Funcionalidade | O que aconteceu |
|----------------|-----------------|
| Decidim Awesome | Instalado em maio de 2025 e removido por erro de compilação |
| OpenTelemetry | Configurado em dezembro de 2025 e substituído pelo Pyroscope em julho de 2026 |
| Demonstração SaaS e chart de organizações | Formulário que criava organizações e chart com Ingress, seed e Airflow; movidos para `infra/decidim-saas` em maio de 2026 |
| Componente `govbr` | Removido em novembro de 2025; hoje só com `ENABLE_GOVBR_COMPONENT=true` |
| Proxy de imagens | Removido em junho de 2026 |
| API `createEphemeralSession` e scripts de voto | Criados para o chatbot em setembro de 2026 e retirados antes do merge |
| Convite de administrador por CPF | Só na branch `release/0.32.1-v1.0.0-cpf-invite`; deixou rastros no `schema.rb` ([divergências](../participa/banco-de-dados/index.md#divergencias-entre-o-schemarb-e-as-migracoes)) |

Fontes: `git log --merges main`, commits `feat` da `main`, `Gemfile` e o código de cada gem na revisão travada. Itens com data de gem indicam quando a gem entrou ou mudou no `Gemfile.lock` do Participa.
