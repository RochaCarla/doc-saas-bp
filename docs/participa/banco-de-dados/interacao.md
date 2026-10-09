---
title: Comentários e interação
icon: material/comment-multiple
---

<!-- Gerado por scripts/banco_de_dados.py em 2026-10-09T16:34:04+00:00. Não edite à mão. -->

# Comentários e interação

Comentários, curtidas, seguidores, notificações, mensagens privadas, lembretes e conquistas.

**13 tabelas.** Schema versão `20260924162404`. Legenda da coluna **Referência**: *FK* = chave estrangeira declarada no banco; *→* = referência por convenção de nome (sem restrição no banco).

## Relacionamentos

Cada seta vai da tabela referenciada para a tabela que guarda a referência. Referências para outros domínios aparecem na coluna **Referência** das tabelas abaixo.

**A partir de `decidim_messaging_conversations`**

```mermaid
flowchart TB
    decidim_messaging_conversations["messaging_<br/>conversations"]
    decidim_messaging_messages["messaging_<br/>messages"]
    decidim_messaging_participations["messaging_<br/>participations"]
    decidim_messaging_receipts["messaging_<br/>receipts"]
    decidim_messaging_conversations --> decidim_messaging_messages
    decidim_messaging_conversations --> decidim_messaging_participations
    decidim_messaging_messages --> decidim_messaging_receipts
```

**A partir de `decidim_reminders`**

```mermaid
flowchart TB
    decidim_reminder_deliveries["reminder_<br/>deliveries"]
    decidim_reminder_records["reminder_<br/>records"]
    decidim_reminders["reminders"]
    decidim_reminders --> decidim_reminder_deliveries
    decidim_reminders --> decidim_reminder_records
```

**Outras relações**

```mermaid
flowchart LR
    decidim_comments_comment_votes["comments_<br/>comment_votes"]
    decidim_comments_comments["comments_<br/>comments"]
    decidim_comments_comments --> decidim_comments_comment_votes
```

## Tabelas

| Tabela | Descrição | Colunas | Origem |
|---|---|---:|---|
| [`decidim_comments_comment_votes`](#decidim-comments-comment-votes) | Votos (positivo/negativo) em comentários. | 7 | Decidim |
| [`decidim_comments_comments`](#decidim-comments-comments) | Comentários. `decidim_commentable_*` aponta para o recurso e `decidim_root_commentable_*` para a raiz da conversa. | 18 | Decidim |
| [`decidim_follows`](#decidim-follows) | Usuários que seguem recursos. | 6 | Decidim |
| [`decidim_gamification_badge_scores`](#decidim-gamification-badge-scores) | — | 4 | Decidim |
| [`decidim_likes`](#decidim-likes) | Curtidas em recursos (chamadas de apoios antes do Decidim 0.32). | 7 | Decidim |
| [`decidim_messaging_conversations`](#decidim-messaging-conversations) | — | 3 | Decidim |
| [`decidim_messaging_messages`](#decidim-messaging-messages) | — | 6 | Decidim |
| [`decidim_messaging_participations`](#decidim-messaging-participations) | — | 5 | Decidim |
| [`decidim_messaging_receipts`](#decidim-messaging-receipts) | — | 6 | Decidim |
| [`decidim_notifications`](#decidim-notifications) | Notificações dos usuários. | 9 | Decidim |
| [`decidim_reminder_deliveries`](#decidim-reminder-deliveries) | — | 4 | Decidim |
| [`decidim_reminder_records`](#decidim-reminder-records) | — | 6 | Decidim |
| [`decidim_reminders`](#decidim-reminders) | — | 5 | Decidim |

### `decidim_comments_comment_votes` { #decidim-comments-comment-votes }

Votos (positivo/negativo) em comentários.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_author_id` | `integer` | não |  | polimórfico (tipo em `decidim_author_type`) |  |
| `decidim_author_type` | `string` | não |  |  |  |
| `decidim_comment_id` | `integer` | não |  | → [`decidim_comments_comments`](interacao.md#decidim-comments-comments) |  |
| `updated_at` | `datetime` | não |  |  |  |
| `weight` | `integer` | não |  |  |  |

??? note "Índices (4)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_comments_comment_votes_on_decidim_author` | `decidim_author_id`, `decidim_author_type` |  | btree |
    | `decidim_comments_comment_vote_author` | `decidim_author_id` |  | btree |
    | `decidim_comments_comment_vote_comment_author_unique` | `decidim_comment_id`, `decidim_author_id` | sim | btree |
    | `decidim_comments_comment_vote_comment` | `decidim_comment_id` |  | btree |

### `decidim_comments_comments` { #decidim-comments-comments }

Comentários. `decidim_commentable_*` aponta para o recurso e `decidim_root_commentable_*` para a raiz da conversa.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `alignment` | `integer` | não | `0` |  |  |
| `body` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `comments_count` | `integer` | não | `0` | contador em cache |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_author_id` | `integer` | não |  | polimórfico (tipo em `decidim_author_type`) |  |
| `decidim_author_type` | `string` | não |  |  |  |
| `decidim_commentable_id` | `integer` | não |  | polimórfico (tipo em `decidim_commentable_type`) |  |
| `decidim_commentable_type` | `string` | não |  |  |  |
| `decidim_participatory_space_id` | `integer` | sim |  | polimórfico (tipo em `decidim_participatory_space_type`) |  |
| `decidim_participatory_space_type` | `string` | sim |  |  |  |
| `decidim_root_commentable_id` | `integer` | não |  | polimórfico (tipo em `decidim_root_commentable_type`) |  |
| `decidim_root_commentable_type` | `string` | não |  |  |  |
| `deleted_at` | `datetime` | sim |  |  |  |
| `depth` | `integer` | não | `0` |  |  |
| `down_votes_count` | `integer` | não | `0` | contador em cache |  |
| `up_votes_count` | `integer` | não | `0` | contador em cache |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (6)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_comments_comments_on_created_at` | `created_at` |  | btree |
    | `index_decidim_comments_comments_on_decidim_author` | `decidim_author_id`, `decidim_author_type` |  | btree |
    | `decidim_comments_comment_author` | `decidim_author_id` |  | btree |
    | `decidim_comments_comment_commentable` | `decidim_commentable_type`, `decidim_commentable_id` |  | btree |
    | `index_decidim_comments_on_decidim_participatory_space` | `decidim_participatory_space_id`, `decidim_participatory_space_type` |  | btree |
    | `decidim_comments_comment_root_commentable` | `decidim_root_commentable_type`, `decidim_root_commentable_id` |  | btree |

### `decidim_follows` { #decidim-follows }

Usuários que seguem recursos.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_followable_id` | `bigint` | sim |  | polimórfico (tipo em `decidim_followable_type`) |  |
| `decidim_followable_type` | `string` | sim |  |  |  |
| `decidim_user_id` | `bigint` | não |  | → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_follows_followable_id_and_type` | `decidim_followable_id`, `decidim_followable_type` |  | btree |
    | `index_uniq_on_follows_user_and_followable` | `decidim_user_id`, `decidim_followable_id`, `decidim_followable_type` | sim | btree |
    | `index_decidim_follows_on_decidim_user_id` | `decidim_user_id` |  | btree |

### `decidim_gamification_badge_scores` { #decidim-gamification-badge-scores }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `badge_name` | `string` | não |  |  |  |
| `user_id` | `bigint` | não |  | → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `value` | `integer` | não | `0` |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_gamification_badge_scores_on_user_id` | `user_id` |  | btree |

### `decidim_likes` { #decidim-likes }

Curtidas em recursos (chamadas de apoios antes do Decidim 0.32).

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_author_id` | `bigint` | sim |  | polimórfico (tipo em `decidim_author_type`) |  |
| `decidim_author_type` | `string` | sim |  |  |  |
| `resource_id` | `bigint` | sim |  | polimórfico (tipo em `resource_type`) |  |
| `resource_type` | `string` | sim |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `idx_likes_authors` | `decidim_author_type`, `decidim_author_id` |  | btree |
    | `index_decidim_likes_on_resource_type_and_resource_id` | `resource_type`, `resource_id` |  | btree |

### `decidim_messaging_conversations` { #decidim-messaging-conversations }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  | — |
| `updated_at` | `datetime` | não |  |  | — |

### `decidim_messaging_messages` { #decidim-messaging-messages }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `body` | `text` | não |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_conversation_id` | `bigint` | não |  | → [`decidim_messaging_conversations`](interacao.md#decidim-messaging-conversations) |  |
| `decidim_sender_id` | `bigint` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_messaging_messages_on_decidim_conversation_id` | `decidim_conversation_id` |  | btree |
    | `index_decidim_messaging_messages_on_decidim_sender_id` | `decidim_sender_id` |  | btree |

### `decidim_messaging_participations` { #decidim-messaging-participations }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_conversation_id` | `bigint` | não |  | → [`decidim_messaging_conversations`](interacao.md#decidim-messaging-conversations) |  |
| `decidim_participant_id` | `bigint` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_conversation_participations_on_conversation_id` | `decidim_conversation_id` |  | btree |
    | `index_conversation_participations_on_participant_id` | `decidim_participant_id` |  | btree |

### `decidim_messaging_receipts` { #decidim-messaging-receipts }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_message_id` | `bigint` | não |  | → [`decidim_messaging_messages`](interacao.md#decidim-messaging-messages) |  |
| `decidim_recipient_id` | `bigint` | não |  |  |  |
| `read_at` | `datetime` | sim |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_messaging_receipts_on_decidim_message_id` | `decidim_message_id` |  | btree |
    | `index_decidim_messaging_receipts_on_decidim_recipient_id` | `decidim_recipient_id` |  | btree |

### `decidim_notifications` { #decidim-notifications }

Notificações dos usuários.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_resource_id` | `bigint` | não |  | polimórfico (tipo em `decidim_resource_type`) |  |
| `decidim_resource_type` | `string` | não |  |  |  |
| `decidim_user_id` | `bigint` | não |  | → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `event_class` | `string` | não |  |  |  |
| `event_name` | `string` | não |  |  |  |
| `extra` | `jsonb` | sim |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_notifications_on_decidim_resource_id` | `decidim_resource_id` |  | btree |
    | `index_decidim_notifications_on_decidim_user_id` | `decidim_user_id` |  | btree |

### `decidim_reminder_deliveries` { #decidim-reminder-deliveries }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_reminder_id` | `bigint` | sim |  | FK → [`decidim_reminders`](interacao.md#decidim-reminders) |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_reminder_deliveries_on_decidim_reminder_id` | `decidim_reminder_id` |  | btree |

### `decidim_reminder_records` { #decidim-reminder-records }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `decidim_reminder_id` | `bigint` | sim |  | FK → [`decidim_reminders`](interacao.md#decidim-reminders) |  |
| `remindable_id` | `bigint` | não |  | polimórfico (tipo em `remindable_type`) |  |
| `remindable_type` | `string` | não |  |  |  |
| `state` | `integer` | não | `0` |  |  |
| `string` | `string` | sim | `"active"` |  | — |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_reminder_records_on_decidim_reminder_id` | `decidim_reminder_id` |  | btree |
    | `index_decidim_reminder_records_remindable` | `remindable_type`, `remindable_id` |  | btree |
    | `index_decidim_reminder_records_on_string` | `string` |  | btree |

### `decidim_reminders` { #decidim-reminders }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_component_id` | `bigint` | sim |  | FK → [`decidim_components`](componentes-conteudo.md#decidim-components) |  |
| `decidim_user_id` | `bigint` | não |  | FK → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_reminders_on_decidim_component_id` | `decidim_component_id` |  | btree |
    | `index_decidim_reminders_on_decidim_user_id` | `decidim_user_id` |  | btree |

