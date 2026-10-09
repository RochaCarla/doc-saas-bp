# Configuração

A API OP-BP lê a configuração de variáveis de ambiente pela classe `Settings` (`api/app/config.py`). O modelo está em `api/.env.example`. Os valores não estão nesta documentação.

## Variáveis da API

### Infraestrutura

| Variável | Uso |
|----------|-----|
| `APP_ENV` | `development` ou `production`. Em produção, liga as [validações estritas](#validacoes-de-producao) |
| `LOG_LEVEL` | Nível de log |
| `POSTGRES_HOST`, `POSTGRES_PORT`, `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD` | Banco, pelo PgBouncer |
| `VALKEY_CACHE_HOST`, `VALKEY_CACHE_PORT`, `VALKEY_CACHE_PASSWORD` | Valkey de cache, sessões e limites |
| `VALKEY_BROKER_HOST`, `VALKEY_BROKER_PORT`, `VALKEY_BROKER_PASSWORD` | Valkey das filas do Dramatiq |
| `CORS_ALLOW_ORIGINS` | Origens permitidas (lista separada por vírgula) |
| `RATE_LIMIT_ENABLED` | Liga os limites de requisição (desligado só em testes de carga) |
| `APP_VERSION`, `GIT_COMMIT`, `BUILD_TIME` | Identificação do build exibida em `/health` |
| `OTEL_ENABLED`, `OTEL_SERVICE_NAME`, `OTEL_EXPORTER_OTLP_ENDPOINT` | Rastreamento OpenTelemetry |

### Acesso e criptografia

| Variável | Uso |
|----------|-----|
| `API_KEY` | Chave de acesso às rotas REST |
| `ADMIN_API_KEY` | Chave do painel (32 caracteres ou mais em produção) |
| `ADMIN_JWT_SECRET`, `ADMIN_JWT_EXPIRY_SECONDS` | Tokens do painel (padrão de 3.600 s) |
| `CPF_HASH_SALT` | Sal do hash do CPF |
| `CPF_ENCRYPTION_KEY`, `CPF_ENCRYPTION_KEY_PREVIOUS` | Chave Fernet do CPF e a anterior, para rotação |
| `CONFIG_ENCRYPTION_KEY` | Chave Fernet dos segredos por processo (WhatsApp, catálogo) |
| `ANONYMIZATION_SECRET` | Chave Fernet dos backups de anonimização |

### Integrações

| Variável | Uso |
|----------|-----|
| `BP_API_URL`, `BP_API_KEY` | API GraphQL do Brasil Participativo e chave compartilhada |
| `GOVBR_JWT_SECRET` | Segredo do login externo (igual ao `EXTERNAL_AUTH_SECRET` do Decidim) |
| `GOVBR_AUTH_BASE_URL` | Endereço do `/external_auth/link` |
| `GOVBR_CALLBACK_URL` | Endereço público do callback (HTTPS) |
| `GOVBR_CALLBACK_API_KEY` | Chave do callback (igual a `BP_API_KEY`) |
| `SERPRO_API_URL`, `SERPRO_TOKEN_URL`, `SERPRO_CONSUMER_KEY`, `SERPRO_CONSUMER_SECRET`, `SERPRO_USE_REAL_API` | Consulta CPF do SERPRO |
| `WHATSAPP_SERPRO_BASE_URL`, `WHATSAPP_SERPRO_CLIENT_ID`, `WHATSAPP_SERPRO_CLIENT_SECRET`, `WHATSAPP_SERPRO_FROM_PHONE_NUMBER_ID` | Valores padrão do WhatsApp do SERPRO |
| `WHATSAPP_APP_SECRET`, `WHATSAPP_SIGNATURE_VALIDATION`, `WHATSAPP_SKIP_SIGNATURE` | Verificação das mensagens do WhatsApp |
| `WHATSAPP_FLOW_PRIVATE_KEY_PATH`, `WHATSAPP_FLOW_PRIVATE_KEY_PASSPHRASE` | Chave privada do WhatsApp Flows |
| `TELEGRAM_WEBHOOK_SECRET` | Segredo do webhook do Telegram |
| `PROCESSES_API_URL`, `PROCESSES_API_KEY`, `PROCESSES_USE_REAL_API`, `PROCESSES_API_TIMEOUT`, `PROCESSES_TIMEZONE` | Catálogo de processos do concierge |
| `BP_DATA_PATH` | Caminho alternativo do JSON de propostas |

### Sessões

| Variável | Uso |
|----------|-----|
| `CONV_SESSION_TTL` | Duração da sessão do roteiro (padrão de 24 h) |
| `FLOW_CHAT_TTL` | Duração da sessão do WhatsApp Flows |

### Workers e ferramentas

| Variável | Uso |
|----------|-----|
| `WORKER_*_PROCESSES`, `WORKER_*_THREADS` | Processos e threads de cada worker no Docker Compose |
| `SKIP_MIGRATIONS` | Pula as migrações no início do contêiner (workers) |
| `DASHBOARD_PORT` | Porta do Dramatiq Dashboard (perfil `tools`) |
| `OPBP_ADMIN_KEY` | Chave usada pelo script de provisionamento do concierge |

## Validações de produção

Com `APP_ENV=production`, a API **não inicia** se faltar algum destes requisitos (`api/app/config.py`):

- segredo e validação de assinatura do WhatsApp ligados, sem pular a verificação;
- Consulta CPF real (`SERPRO_USE_REAL_API=true`);
- `GOVBR_JWT_SECRET` e `ADMIN_API_KEY` com 32 caracteres ou mais; `GOVBR_CALLBACK_API_KEY` com 16 ou mais;
- `BP_API_KEY` definida e igual a `GOVBR_CALLBACK_API_KEY`;
- `CPF_HASH_SALT` diferente do padrão e `CPF_ENCRYPTION_KEY` definida;
- `API_KEY` e `TELEGRAM_WEBHOOK_SECRET` definidos;
- callback gov.br em HTTPS.

A falta de senha do Valkey gera só um aviso.

## Variáveis do front-end

| App | Variáveis |
|-----|-----------|
| Painel | `VITE_API_URL` (origem da API, sem `/api/v1`) |
| App de participação | `NEXT_PUBLIC_API_URL`, `NEXT_PUBLIC_PLATFORM`, `NEXT_PUBLIC_PROCESS_ID`, `NEXT_PUBLIC_DECIDIM_URL` e a credencial de acesso à API |

Os arquivos `front/.env.example` e `front/.env.prod.sample` trazem variáveis que o código atual não usa (por exemplo, `NEXT_PUBLIC_BP_URL`, `NEXT_PUBLIC_DECIDIM_PROCESS_SLUG` e as do SERPRO). Remova-as na transferência para evitar confusão.

## Configuração por processo

Parte da configuração fica no banco, por processo, e é editada no [painel](painel.md): regras de voto, credenciais do WhatsApp, catálogo de processos, roteiro, provedores por canal e endereços de webhook, compartilhamento e retorno. Valores vazios nas credenciais por processo usam as variáveis globais.
