# Desenvolvimento

O README do `participa` remete a `docs/development.md`, que não existe no repositório. Este guia reúne o que está no README, no `CONTRIBUTING.md`, no `docker-compose.yml` e no `bin/dev`.

## Com Docker Compose (recomendado)

```bash
git clone https://gitlab.com/lappis-unb/decidimbr/participa.git
cd participa
cp .env.sample .env
docker compose up --build        # o primeiro início leva vários minutos
```

O contêiner `decidim` instala as dependências, roda `db:create` e `db:migrate` e sobe o Rails (porta 3000) e o servidor de desenvolvimento do Shakapacker. Também sobem `postgres`, `redis` (filas), `redis-cache` e `sidekiq`.

Quando o log mostrar `Listening on http://0.0.0.0:3000`, em outro terminal:

```bash
# 1. administrador de sistema
docker compose exec decidim bin/rails runner '
  Decidim::System::Admin.new(email: "admin@example.com",
                             password: "<senha forte>",
                             password_confirmation: "<senha forte>").save!(validate: false)'
```

2. Entre em <http://localhost:3000/system> e crie uma organização com host `localhost`.
3. Crie o administrador da organização e, se quiser, o conteúdo de exemplo:

```bash
docker compose exec decidim bin/rails "decidim_admin:create_admin[Nome,email@example.com,<senha>,localhost]"
docker compose exec decidim bin/rails "decidim_admin:seed_organization[localhost]"
```

E-mails enviados em desenvolvimento aparecem em <http://localhost:3000/letter_opener>.

## Sem Docker

Requisitos: Ruby 3.4.7 e Node 22.14.0 (`.tool-versions`, para asdf ou mise), PostgreSQL com permissão para criar extensões, e Redis.

```bash
bin/dev    # bundle install, decidim:upgrade, db:migrate e Procfile.dev (web, Shakapacker, Sidekiq)
```

As extensões ficam no schema `shared_extensions`. Se o banco não as tiver, rode `bin/rails decidim_apartment:install_pg_extension`.

## Variáveis úteis em desenvolvimento

| Variável | Efeito |
|----------|--------|
| `OMNIAUTH_GOVBR_FAKE=true` | Formulário local no lugar do SSO do gov.br |
| `GOVBR_LAYOUT_HOSTS=localhost` | Liga o layout gov.br para `localhost` |
| `CHATBOT_RESET_COMMAND=true` | Comando de reinício da conversa do chatbot |
| `RAILS_BOOST_PERFORMANCE=true` | Carregamento antecipado de classes, para medir desempenho |
| `REDIS_CACHE_URL` | Cache compartilhado entre web e Sidekiq (evita recriar a demo de modelos a cada início) |

## Testes

| Suíte | Arquivos de spec | Como rodar |
|-------|-----------------:|------------|
| Aplicação (`spec/`) | 23 | `docker compose exec -e RAILS_ENV=test -e RAILS_MASTER_KEY= -e DISABLE_SPRING=1 -e TEMPLATE_GIT_URL= decidim bundle exec rspec spec/<arquivo>_spec.rb` |
| Chatbot (`decidim-chatbot/spec/`) | 61 | Roda contra a aplicação, com multi-organização e sobrescritas carregadas |
| Engine gov.br (`decidim-govbr/spec/`) | 23 | `cd decidim-govbr && bin/test rspec` (aplicação de teste própria) |

Os testes **não rodam no CI**. Rode-os localmente antes de abrir o merge request. O lint usa a configuração RuboCop do Decidim (`.rubocop.yml`).

## Contribuição

Segundo o `CONTRIBUTING.md`:

- branches a partir da `main`, com prefixo `feat/`, `fix/`, `chore/`, `core/` ou `docs/`;
- mensagens no padrão Conventional Commits, em português;
- merge request para a `main`.

A branch `develop` está parada desde agosto de 2026, 165 commits atrás da `main`.

## Ferramentas do chatbot

```bash
bin/rails chatbot:validate                          # estrutura do roteiro e limites do WhatsApp
PHONE=<telefone> HOST=localhost bin/rails chatbot:simulate      # conversa no terminal
bin/rails chatbot:render_payload KIND=... TO=...    # payload de uma mensagem
```
