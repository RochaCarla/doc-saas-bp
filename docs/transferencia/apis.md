# APIs

| API | Projeto | Para quem | Autenticação |
|-----|---------|-----------|--------------|
| GraphQL `/api` | Participa | Clientes externos e o concierge da API OP-BP | Sessão, ou JWT de `/api/sign_in` |
| Webhooks `/chatbot/webhooks/:token` | Participa | WhatsApp do SERPRO | Basic Auth por provedor |
| REST `/api/v1/*` | API OP-BP | App de participação e integrações | Chave de API |
| REST `/api/v1/admin/*` | API OP-BP | Painel administrativo | Chave de administrador ou JWT |
| Webhooks `/api/v1/conversations/{provedor}/webhook` | API OP-BP | WhatsApp do SERPRO e Telegram | Verificação do provedor |
| `/api/v1/whatsapp-flows` | API OP-BP | WhatsApp Flows (Meta) | Criptografia do protocolo Flows |
| Callback `/api/v1/identity/govbr/callback` | API OP-BP | Brasil Participativo | Chave compartilhada |

## Participa: GraphQL

A API do Decidim 0.32 em `/api`, com GraphiQL em `/api/graphiql`. Limites: 50 itens por página, complexidade 5.000, profundidade 15. CORS em `/api*` só para `ALLOWED_ORIGINS`. Cada organização responde no seu próprio host.

```bash
curl -s https://<host-da-organizacao>/api \
  -H 'Content-Type: application/json' \
  -d '{"query":"{ participatoryProcesses { id slug title { translation(locale: \"pt-BR\") } } }"}'
```

O componente de texto participativo acrescenta o tipo `Paragraph`. O Participa não tem a API REST própria nem a impersonação do core do Brasil Participativo.

## API OP-BP

A documentação interativa (`/docs`, `/redoc`) fica disponível fora de produção. Principais rotas:

| Método e caminho | Função | Limite por minuto |
|------------------|--------|------------------:|
| `GET /health` | Saúde e versão | 30 |
| `POST /api/v1/chats` | Cria ou recupera o chat de um canal | — |
| `POST /api/v1/participants` | Cria ou recupera o participante num processo | — |
| `GET /api/v1/proposals`, `GET /api/v1/proposals/municipalities` | Propostas por município e autocompletar | — |
| `GET /api/v1/cep/{cep}` | Município de um CEP e se ele participa | 30 |
| `POST /api/v1/votes/submit` | Envia votos (responde 202 com `tracking_id`) | 20 |
| `POST /api/v1/votes/identify` | Identificação posterior (CPF ou gov.br) | 20 |
| `GET /api/v1/votes/status/{tracking_id}` | Situação da tarefa | — |
| `POST /api/v1/identity/cpf/validate` | Valida CPF no SERPRO | 10 |
| `POST /api/v1/identity/govbr` | Gera o link de login gov.br | 15 |
| `POST /api/v1/identity/govbr/callback` | Retorno do Brasil Participativo após o login | 30 |
| `POST /api/v1/identity/govbr/status` | Participante já autenticado? | 30 |

As rotas do painel cobrem processos, propostas, participantes, votos, roteiros, operação e LGPD ([Painel](../multicanal/painel.md)).

### Exemplo: enviar votos

```bash
curl -s -X POST https://<api-op-bp>/api/v1/votes/submit \
  -H "Authorization: Bearer $API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"identifier_value":"<id-do-canal>","process_id":1,
       "proposals":[{"bp_proposal_id":"101","proposal_title":"Título"}],
       "identification":{"method":"anonymous"}}'
```

O corpo segue `VoteSubmitRequest` (`api/app/schemas/votes.py`). `identification.method` aceita `anonymous`, `cpf` (com `cpf`, `nome_completo`, `data_nascimento` ou um `validation_token`) e `govbr`. A resposta traz `status`, `message` e `tracking_id`.

## Entre os sistemas

| Chamada | Contrato |
|---------|----------|
| API OP-BP → Brasil Participativo | GraphQL `ephemeral.create(cpf)` com `authKey`; `voteProposal` com `X-API-KEY` e `X-USER-ID` ([Integração](../multicanal/integracao.md)) |
| API OP-BP → Brasil Participativo | Link de login externo assinado com `GOVBR_JWT_SECRET` |
| Brasil Participativo → API OP-BP | Callback com `source_id`, `external_id`, CPF, nome, e-mail e situação |
| API OP-BP → Participa | GraphQL `participatoryProcesses` (leitura) |

## Dados abertos

O Participa exporta os dados abertos do Decidim por organização; a versão da participa-gem é disparada pela tarefa `decidim:open_data:export`.
