# Inventário de ativos

Tudo o que precisa mudar de mãos. Os itens marcados **a confirmar** não estão registrados nos repositórios e devem ser levantados com a equipe atual.

## Repositórios de código

| Repositório | Conteúdo |
|-------------|----------|
| [`lappis-unb/decidimbr/participa`](https://gitlab.com/lappis-unb/decidimbr/participa) | Participa: aplicação, engines `decidim-govbr` e `decidim-chatbot`, chart Helm |
| [`lappis-unb/decidimbr/infra/participa-gem`](https://gitlab.com/lappis-unb/decidimbr/infra/participa-gem) | `decidim-apartment` (multi-organização) |
| `lappis-unb/decidimbr/components-brasil-participativo/*` | Gems do Brasil Participativo: `decidim-bp_proposals`, `decidim-bp_meetings`, `decidim-bp_comments`, `decidim-module-questionnaires`, `decidim-participatory_text`, `decidim-bp_templates`, `decidim-government-spaces`, `decidim-categories`, `decidim-extra_home_blocks`, `decidim-extra-blocks` |
| `infra/decidim-saas` | Chart de criação de organizações e demonstração SaaS, movidos do `participa` em maio de 2026 (**a confirmar**) |
| Repositório do catálogo de modelos de processo | Endereço em `TEMPLATE_GIT_URL` (**a confirmar**) |
| [`lappis-unb/decidimbr/multi-channel-participation`](https://gitlab.com/lappis-unb/decidimbr/multi-channel-participation) | API OP-BP, painel administrativo e app de participação |

O grupo `lappis-unb/decidimbr` pertence ao laboratório. A transferência deve definir se os repositórios migram para um grupo do órgão receptor ou se o receptor recebe permissão de manutenção.

## Dependências de terceiros

| Dependência | Origem | Risco |
|-------------|--------|-------|
| `decidim-toggle`, `decidim-ephemeral_participation` | `git.octree.ch` (Octree) | Repositório externo, seguido por branch |
| `omniauth-govbr` | Repositório pessoal no GitHub | Depende de uma pessoa; migrar para um grupo institucional |
| Imagens Bitnami `redis` | Docker Hub / Bitnami | Mudanças de licença e de distribuição das imagens Bitnami devem ser acompanhadas |

## Imagens e artefatos

| Artefato | Onde |
|----------|------|
| Imagens do Participa (`dev`, `bump`, produção) | `registry.gitlab.com/lappis-unb/decidimbr/participa` |
| Imagem da API OP-BP | Registro do GitLab do projeto (`api:<sha>`, `api:latest`) |
| Releases do Participa | GitLab Releases, geradas pelas tags |

## Ambientes

| Ambiente | Projeto | Endereço | Situação |
|----------|---------|----------|----------|
| Desenvolvimento do Participa do Acre | Participa | `acre.dev.participa.lappis.rocks` | Citado como padrão do catálogo da API OP-BP |
| Homologação do Participa | Participa | Host de homologação da Dataprev no `values.yaml` e no `docker-compose.proxy.yml` | **a confirmar** |
| Produção do Participa | Participa | **a confirmar** | |
| API OP-BP | Participação multicanal | `api-opbp.lablivre.rocks` (padrão de script) e `api.bp.lappis.rocks` (padrão do app) | **a confirmar** qual é produção |
| Painel e app de participação | Participação multicanal | **a confirmar** | |

## Serviços externos e contas

| Serviço | Uso | Credenciais (nomes) | Responsável |
|---------|-----|---------------------|-------------|
| gov.br (Login Único) | Login no Participa | `OMNIAUTH_GOVBR_*` e configuração por organização | **a confirmar** (um cliente por organização?) |
| WhatsApp do SERPRO | Chatbot e API OP-BP | Por organização (chatbot) e por processo (API OP-BP); `WHATSAPP_SERPRO_*` | **a confirmar** |
| Consulta CPF do SERPRO | API OP-BP | `SERPRO_*` | **a confirmar** |
| WhatsApp Flows (Meta) | API OP-BP | `WHATSAPP_APP_SECRET`, `WHATSAPP_FLOW_PRIVATE_KEY_*` | **a confirmar** |
| Bot do Telegram | API OP-BP | `TELEGRAM_WEBHOOK_SECRET` | **a confirmar** |
| Brasil Participativo (API) | Votos da API OP-BP | `BP_API_KEY`, `GOVBR_JWT_SECRET` (compartilhados com o core do Brasil Participativo) | SNPS e Dataprev |
| S3/MinIO | Arquivos do Participa | `AWS_*` | **a confirmar** |
| SMTP | E-mails do Participa | Por organização e `SMTP_*` | **a confirmar** |
| HERE e servidores OSM/Photon | Mapas do Participa | `MAPS_HERE_API_KEY`, `OSM_URL`, `MAPS_GEOCODING_HOST` | Servidores OSM e Photon do LAPPIS (**a migrar**) |
| Matomo, PostHog, Pyroscope | Análise de uso e desempenho | `MATOMO_*`, `POSTHOG_*`, `PYROSCOPE_*` | **a confirmar** |
| Airflow | Ingestão de dados do Participa (papel `airflow` no banco) | Papel no CloudNativePG | **a confirmar** |
| Let's Encrypt | Certificados do Participa | cert-manager | Equipe de operação |

## Segredos da aplicação

| Projeto | Segredos | Onde ficam |
|---------|----------|------------|
| Participa | `SECRET_KEY_BASE`, `RAILS_MASTER_KEY` e as chaves das credenciais Rails | Secrets do Kubernetes criados à mão |
| Participa | Segredos de provedores do chatbot | Banco, cifrados |
| API OP-BP | `API_KEY`, `ADMIN_API_KEY`, `ADMIN_JWT_SECRET`, `CPF_HASH_SALT`, `CPF_ENCRYPTION_KEY`, `CONFIG_ENCRYPTION_KEY`, `ANONYMIZATION_SECRET` | Variáveis de ambiente (**a confirmar** onde são guardadas em produção) |

!!! danger "Chaves de cifragem do CPF"
    Perder `CPF_ENCRYPTION_KEY` ou `CPF_HASH_SALT` torna os CPFs guardados pela API OP-BP ilegíveis ou impossíveis de encontrar. Trocar `SECRET_KEY_BASE` no Participa muda o identificador das verificações por CPF. Planeje a custódia dessas chaves antes da transferência.

## Domínios

| Domínio | Uso |
|---------|-----|
| `*.participa.lappis.rocks` | Instalações de desenvolvimento do Participa (**a migrar**) |
| `api-opbp.lablivre.rocks`, `api.bp.lappis.rocks` | API OP-BP (**a migrar**) |
| `rochacarla.github.io/doc-saas-bp` | Esta documentação |
