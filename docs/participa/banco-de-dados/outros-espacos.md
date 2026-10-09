---
title: Conferências, iniciativas e eleições
icon: material/account-group
---

<!-- Gerado por scripts/banco_de_dados.py em 2026-10-09T16:34:04+00:00. Não edite à mão. -->

# Conferências, iniciativas e eleições

Espaços e módulos do Decidim instalados explicitamente no Participa: conferências, iniciativas e eleições.

**21 tabelas.** Schema versão `20260924162404`. Legenda da coluna **Referência**: *FK* = chave estrangeira declarada no banco; *→* = referência por convenção de nome (sem restrição no banco).

## Relacionamentos

Cada seta vai da tabela referenciada para a tabela que guarda a referência. Referências para outros domínios aparecem na coluna **Referência** das tabelas abaixo.

**A partir de `decidim_conferences`**

```mermaid
flowchart LR
    decidim_conference_speaker_conference_meetings["conference_<br/>speaker_<br/>conference_<br/>meetings"]
    decidim_conference_speakers["conference_<br/>speakers"]
    decidim_conference_user_roles["conference_<br/>user_roles"]
    decidim_conferences["conferences"]
    decidim_conferences_conference_invites["conferences_<br/>conference_<br/>invites"]
    decidim_conferences_conference_meeting_registration_types["conferences_<br/>conference_<br/>meeting_<br/>registration_<br/>types"]
    decidim_conferences_conference_registrations["conferences_<br/>conference_<br/>registrations"]
    decidim_conferences_media_links["conferences_<br/>media_links"]
    decidim_conferences_partners["conferences_<br/>partners"]
    decidim_conferences_registration_types["conferences_<br/>registration_<br/>types"]
    decidim_conference_speaker_conference_meetings --> decidim_conferences_conference_meeting_registration_types
    decidim_conference_speakers --> decidim_conference_speaker_conference_meetings
    decidim_conferences --> decidim_conference_speakers
    decidim_conferences --> decidim_conference_user_roles
    decidim_conferences --> decidim_conferences_conference_invites
    decidim_conferences --> decidim_conferences_conference_registrations
    decidim_conferences --> decidim_conferences_media_links
    decidim_conferences --> decidim_conferences_partners
    decidim_conferences --> decidim_conferences_registration_types
```

**A partir de `decidim_elections_elections`**

```mermaid
flowchart TB
    decidim_elections_elections["elections_<br/>elections"]
    decidim_elections_questions["elections_<br/>questions"]
    decidim_elections_response_options["elections_<br/>response_<br/>options"]
    decidim_elections_voters["elections_<br/>voters"]
    decidim_elections_votes["elections_<br/>votes"]
    decidim_elections_elections --> decidim_elections_questions
    decidim_elections_elections --> decidim_elections_voters
    decidim_elections_questions --> decidim_elections_response_options
    decidim_elections_questions --> decidim_elections_votes
    decidim_elections_response_options --> decidim_elections_votes
```

**Outras relações**

```mermaid
flowchart LR
    decidim_initiatives["initiatives"]
    decidim_initiatives_votes["initiatives_<br/>votes"]
    decidim_initiatives --> decidim_initiatives_votes
```

## Tabelas

| Tabela | Descrição | Colunas | Origem |
|---|---|---:|---|
| [`decidim_conference_speaker_conference_meetings`](#decidim-conference-speaker-conference-meetings) | — | 3 | Decidim |
| [`decidim_conference_speakers`](#decidim-conference-speakers) | — | 12 | Decidim |
| [`decidim_conference_user_roles`](#decidim-conference-user-roles) | — | 6 | Decidim |
| [`decidim_conferences`](#decidim-conferences) | — | 28 | Decidim |
| [`decidim_conferences_conference_invites`](#decidim-conferences-conference-invites) | — | 9 | Decidim |
| [`decidim_conferences_conference_meeting_registration_types`](#decidim-conferences-conference-meeting-registration-types) | — | 3 | Decidim |
| [`decidim_conferences_conference_registrations`](#decidim-conferences-conference-registrations) | — | 7 | Decidim |
| [`decidim_conferences_media_links`](#decidim-conferences-media-links) | — | 8 | Decidim |
| [`decidim_conferences_partners`](#decidim-conferences-partners) | — | 8 | Decidim |
| [`decidim_conferences_registration_types`](#decidim-conferences-registration-types) | — | 9 | Decidim |
| [`decidim_elections_elections`](#decidim-elections-elections) | — | 17 | Decidim |
| [`decidim_elections_questions`](#decidim-elections-questions) | — | 14 | Decidim |
| [`decidim_elections_response_options`](#decidim-elections-response-options) | — | 6 | Decidim |
| [`decidim_elections_voters`](#decidim-elections-voters) | — | 5 | Decidim |
| [`decidim_elections_votes`](#decidim-elections-votes) | — | 6 | Decidim |
| [`decidim_initiatives`](#decidim-initiatives) | — | 25 | Decidim |
| [`decidim_initiatives_committee_members`](#decidim-initiatives-committee-members) | — | 6 | Decidim |
| [`decidim_initiatives_settings`](#decidim-initiatives-settings) | — | 3 | Decidim |
| [`decidim_initiatives_type_scopes`](#decidim-initiatives-type-scopes) | — | 7 | Decidim |
| [`decidim_initiatives_types`](#decidim-initiatives-types) | — | 20 | Decidim |
| [`decidim_initiatives_votes`](#decidim-initiatives-votes) | — | 9 | Decidim |

### `decidim_conference_speaker_conference_meetings` { #decidim-conference-speaker-conference-meetings }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `conference_meeting_id` | `bigint` | não |  | → [`decidim_conference_speaker_conference_meetings`](outros-espacos.md#decidim-conference-speaker-conference-meetings) |  |
| `conference_speaker_id` | `bigint` | não |  | → [`decidim_conference_speakers`](outros-espacos.md#decidim-conference-speakers) |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_meetings_on_decidim_conference_meeting_id` | `conference_meeting_id` |  | btree |
    | `index_meetings_on_decidim_conference_speaker_id` | `conference_speaker_id` |  | btree |

### `decidim_conference_speakers` { #decidim-conference-speakers }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `affiliation` | `jsonb` | sim |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_conference_id` | `bigint` | sim |  | → [`decidim_conferences`](outros-espacos.md#decidim-conferences) |  |
| `decidim_user_id` | `bigint` | sim |  | → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `full_name` | `string` | sim |  |  |  |
| `personal_url` | `string` | sim |  |  |  |
| `position` | `jsonb` | sim |  |  |  |
| `published_at` | `datetime` | sim |  |  |  |
| `short_bio` | `jsonb` | sim |  |  |  |
| `twitter_handle` | `string` | sim |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_conference_speakers_on_decidim_conference_id` | `decidim_conference_id` |  | btree |
    | `index_decidim_conference_speaker_on_decidim_user_id` | `decidim_user_id` |  | btree |

### `decidim_conference_user_roles` { #decidim-conference-user-roles }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_conference_id` | `integer` | sim |  | → [`decidim_conferences`](outros-espacos.md#decidim-conferences) |  |
| `decidim_user_id` | `integer` | sim |  | → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `role` | `string` | sim |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_unique_user_and_conference_role` | `decidim_conference_id`, `decidim_user_id`, `role` | sim | btree |

### `decidim_conferences` { #decidim-conferences }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `available_slots` | `integer` | não | `0` |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_organization_id` | `integer` | sim |  | → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `decidim_scope_id` | `integer` | sim |  | → [`decidim_scopes`](componentes-conteudo.md#decidim-scopes) |  |
| `deleted_at` | `datetime` | sim |  |  |  |
| `description` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `diploma_sent_at` | `datetime` | sim |  |  |  |
| `end_date` | `date` | sim |  |  |  |
| `follows_count` | `integer` | não | `0` | contador em cache |  |
| `location` | `string` | sim |  |  |  |
| `objectives` | `jsonb` | não |  |  |  |
| `promoted` | `boolean` | sim | `false` |  |  |
| `published_at` | `datetime` | sim |  |  |  |
| `reference` | `string` | sim |  |  |  |
| `registration_terms` | `jsonb` | sim |  |  |  |
| `registrations_enabled` | `boolean` | não | `false` |  |  |
| `scopes_enabled` | `boolean` | não | `true` |  |  |
| `short_description` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `show_statistics` | `boolean` | sim | `false` |  |  |
| `sign_date` | `date` | sim |  |  |  |
| `signature_name` | `string` | sim |  |  |  |
| `slogan` | `jsonb` | não |  |  |  |
| `slug` | `string` | não |  |  |  |
| `start_date` | `date` | sim |  |  |  |
| `title` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `updated_at` | `datetime` | não |  |  |  |
| `weight` | `integer` | não | `0` |  |  |

??? note "Índices (4)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_unique_conference_slug_and_organization` | `decidim_organization_id`, `slug` | sim | btree |
    | `index_decidim_conferences_on_decidim_organization_id` | `decidim_organization_id` |  | btree |
    | `index_decidim_conferences_on_decidim_scope_id` | `decidim_scope_id` |  | btree |
    | `index_decidim_conferences_on_deleted_at` | `deleted_at` |  | btree |

### `decidim_conferences_conference_invites` { #decidim-conferences-conference-invites }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `accepted_at` | `datetime` | sim |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_conference_id` | `bigint` | não |  | → [`decidim_conferences`](outros-espacos.md#decidim-conferences) |  |
| `decidim_conference_registration_type_id` | `integer` | sim |  |  |  |
| `decidim_user_id` | `bigint` | não |  | → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `rejected_at` | `datetime` | sim |  |  |  |
| `sent_at` | `datetime` | sim |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `idx_decidim_conferences_invites_on_conference_id` | `decidim_conference_id` |  | btree |
    | `ixd_conferences_on_registration_type_id` | `decidim_conference_registration_type_id` |  | btree |
    | `index_decidim_conferences_conference_invites_on_decidim_user_id` | `decidim_user_id` |  | btree |

### `decidim_conferences_conference_meeting_registration_types` { #decidim-conferences-conference-meeting-registration-types }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `conference_meeting_id` | `bigint` | não |  | → [`decidim_conference_speaker_conference_meetings`](outros-espacos.md#decidim-conference-speaker-conference-meetings) |  |
| `registration_type_id` | `bigint` | não |  |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_registrations_on_decidim_conference_meeting_id` | `conference_meeting_id` |  | btree |
    | `index_meetings_on_decidim_registration_type_id` | `registration_type_id` |  | btree |

### `decidim_conferences_conference_registrations` { #decidim-conferences-conference-registrations }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `confirmed_at` | `datetime` | sim |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_conference_id` | `bigint` | não |  | → [`decidim_conferences`](outros-espacos.md#decidim-conferences) |  |
| `decidim_conference_registration_type_id` | `integer` | sim |  |  |  |
| `decidim_user_id` | `bigint` | não |  | → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (4)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_conferences_registrations_on_decidim_conference` | `decidim_conference_id` |  | btree |
    | `idx_conferences_registrations_on_registration_type_id` | `decidim_conference_registration_type_id` |  | btree |
    | `decidim_conferences_registrations_user_conference_unique` | `decidim_user_id`, `decidim_conference_id` | sim | btree |
    | `index_decidim_conferences_registrations_on_decidim_user_id` | `decidim_user_id` |  | btree |

### `decidim_conferences_media_links` { #decidim-conferences-media-links }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `date` | `date` | sim |  |  |  |
| `decidim_conference_id` | `bigint` | sim |  | → [`decidim_conferences`](outros-espacos.md#decidim-conferences) |  |
| `link` | `string` | não |  |  |  |
| `title` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `updated_at` | `datetime` | não |  |  |  |
| `weight` | `integer` | não | `0` |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_conferences_media_links_on_decidim_conference_id` | `decidim_conference_id` |  | btree |

### `decidim_conferences_partners` { #decidim-conferences-partners }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_conference_id` | `bigint` | sim |  | → [`decidim_conferences`](outros-espacos.md#decidim-conferences) |  |
| `link` | `string` | sim |  |  |  |
| `name` | `string` | não |  |  |  |
| `partner_type` | `string` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `weight` | `integer` | não | `0` |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_conferences_partners_on_decidim_conference_id` | `decidim_conference_id` |  | btree |
    | `index_decidim_conferences_partners_on_weight_and_partner_type` | `weight`, `partner_type` |  | btree |

### `decidim_conferences_registration_types` { #decidim-conferences-registration-types }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_conference_id` | `bigint` | sim |  | → [`decidim_conferences`](outros-espacos.md#decidim-conferences) |  |
| `description` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `price` | `decimal` | sim | `"0.0"` |  |  |
| `published_at` | `datetime` | sim |  |  |  |
| `title` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `updated_at` | `datetime` | não |  |  |  |
| `weight` | `integer` | não | `0` |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `idx_registration_types_on_decidim_conference_id` | `decidim_conference_id` |  | btree |
    | `index_decidim_conferences_registration_types_on_published_at` | `published_at` |  | btree |

### `decidim_elections_elections` { #decidim-elections-elections }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `allow_census_check_before_start` | `boolean` | não | `false` |  |  |
| `announcement` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `census_manifest` | `string` | sim |  |  |  |
| `census_settings` | `jsonb` | não | `{}` |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_component_id` | `integer` | sim |  | → [`decidim_components`](componentes-conteudo.md#decidim-components) |  |
| `deleted_at` | `datetime` | sim |  |  |  |
| `description` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `end_at` | `datetime` | sim |  |  |  |
| `published_at` | `datetime` | sim |  |  |  |
| `published_results_at` | `datetime` | sim |  |  |  |
| `results_availability` | `string` | não | `"after_end"` |  |  |
| `start_at` | `datetime` | sim |  |  |  |
| `title` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `updated_at` | `datetime` | não |  |  |  |
| `votes_count` | `integer` | não | `0` | contador em cache |  |

??? note "Índices (5)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_elections_elections_on_census_manifest` | `census_manifest` |  | btree |
    | `index_decidim_elections_elections_on_deleted_at` | `deleted_at` |  | btree |
    | `index_decidim_elections_elections_on_end_at` | `end_at` |  | btree |
    | `index_decidim_elections_elections_on_published_at` | `published_at` |  | btree |
    | `index_decidim_elections_elections_on_start_at` | `start_at` |  | btree |

### `decidim_elections_questions` { #decidim-elections-questions }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `body` | `jsonb` | não | `{}` | traduzível (`{"pt-BR": …}`) |  |
| `created_at` | `datetime` | não |  |  |  |
| `description` | `jsonb` | sim | `{}` | traduzível (`{"pt-BR": …}`) |  |
| `election_id` | `bigint` | não |  | FK → [`decidim_elections_elections`](outros-espacos.md#decidim-elections-elections) |  |
| `mandatory` | `boolean` | não | `false` |  |  |
| `max_choices` | `integer` | sim |  |  |  |
| `position` | `integer` | sim |  |  |  |
| `published_results_at` | `datetime` | sim |  |  |  |
| `question_type` | `string` | não | `"multiple_option"` |  |  |
| `response_options_count` | `integer` | não | `0` | contador em cache |  |
| `updated_at` | `datetime` | não |  |  |  |
| `votes_count` | `integer` | não | `0` | contador em cache |  |
| `voting_enabled_at` | `datetime` | sim |  |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_questions_on_election_id` | `election_id` |  | btree |

### `decidim_elections_response_options` { #decidim-elections-response-options }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `body` | `jsonb` | não | `{}` | traduzível (`{"pt-BR": …}`) |  |
| `created_at` | `datetime` | não |  |  |  |
| `question_id` | `bigint` | não |  | FK → [`decidim_elections_questions`](outros-espacos.md#decidim-elections-questions) |  |
| `updated_at` | `datetime` | não |  |  |  |
| `votes_count` | `integer` | não | `0` | contador em cache |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_response_options_on_question_id` | `question_id` |  | btree |

### `decidim_elections_voters` { #decidim-elections-voters }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `data` | `jsonb` | não |  |  |  |
| `election_id` | `bigint` | não |  | FK → [`decidim_elections_elections`](outros-espacos.md#decidim-elections-elections) |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_elections_voters_on_election_id` | `election_id` |  | btree |

### `decidim_elections_votes` { #decidim-elections-votes }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `question_id` | `bigint` | não |  | FK → [`decidim_elections_questions`](outros-espacos.md#decidim-elections-questions) |  |
| `response_option_id` | `bigint` | não |  | FK → [`decidim_elections_response_options`](outros-espacos.md#decidim-elections-response-options) |  |
| `updated_at` | `datetime` | não |  |  |  |
| `voter_uid` | `string` | não |  |  |  |

??? note "Índices (4)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_elections_votes_on__voter_uid_and_response` | `question_id`, `voter_uid`, `response_option_id` | sim | btree |
    | `index_decidim_elections_votes_on_question_id` | `question_id` |  | btree |
    | `index_decidim_elections_votes_on_response_option_id` | `response_option_id` |  | btree |
    | `index_decidim_elections_votes_on_voter_uid` | `voter_uid` |  | btree |

### `decidim_initiatives` { #decidim-initiatives }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `answer` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `answer_url` | `string` | sim |  |  |  |
| `answered_at` | `datetime` | sim |  |  |  |
| `comments_count` | `integer` | não | `0` | contador em cache |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_area_id` | `bigint` | sim |  | → [`decidim_areas`](componentes-conteudo.md#decidim-areas) |  |
| `decidim_author_id` | `bigint` | não |  | polimórfico (tipo em `decidim_author_type`) |  |
| `decidim_author_type` | `string` | não |  |  |  |
| `decidim_organization_id` | `integer` | sim |  | → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `description` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `first_progress_notification_at` | `datetime` | sim |  |  | — |
| `follows_count` | `integer` | não | `0` | contador em cache |  |
| `offline_votes` | `jsonb` | sim | `{}` |  |  |
| `online_votes` | `jsonb` | sim | `{}` |  |  |
| `published_at` | `datetime` | sim |  |  |  |
| `reference` | `string` | sim |  |  |  |
| `scoped_type_id` | `integer` | sim |  |  | — |
| `second_progress_notification_at` | `datetime` | sim |  |  | — |
| `signature_end_date` | `date` | sim |  |  |  |
| `signature_start_date` | `date` | sim |  |  |  |
| `signature_type` | `integer` | não | `0` |  |  |
| `state` | `integer` | não | `0` |  |  |
| `title` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (8)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `decidim_initiatives_description_search` | `md5((description)::text)` |  | btree |
    | `index_decidim_initiatives_on_answered_at` | `answered_at` |  | btree |
    | `index_decidim_initiatives_on_decidim_area_id` | `decidim_area_id` |  | btree |
    | `index_decidim_initiatives_on_decidim_author` | `decidim_author_id`, `decidim_author_type` |  | btree |
    | `index_decidim_initiatives_on_decidim_organization_id` | `decidim_organization_id` |  | btree |
    | `index_decidim_initiatives_on_published_at` | `published_at` |  | btree |
    | `index_decidim_initiatives_on_scoped_type_id` | `scoped_type_id` |  | btree |
    | `decidim_initiatives_title_search` | `title` |  | btree |

### `decidim_initiatives_committee_members` { #decidim-initiatives-committee-members }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_initiatives_id` | `bigint` | sim |  |  |  |
| `decidim_users_id` | `bigint` | sim |  |  |  |
| `state` | `integer` | não | `0` |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_committee_members_initiative` | `decidim_initiatives_id` |  | btree |
    | `index_decidim_committee_members_user` | `decidim_users_id` |  | btree |
    | `index_decidim_initiatives_committee_members_on_state` | `state` |  | btree |

### `decidim_initiatives_settings` { #decidim-initiatives-settings }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `decidim_organization_id` | `bigint` | sim |  | FK → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `initiatives_order` | `string` | sim | `"random"` |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_initiatives_settings_on_decidim_organization_id` | `decidim_organization_id` |  | btree |

### `decidim_initiatives_type_scopes` { #decidim-initiatives-type-scopes }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_initiatives_types_id` | `bigint` | sim |  |  |  |
| `decidim_scopes_id` | `bigint` | sim |  |  |  |
| `decidim_taxonomy_id` | `bigint` | sim |  |  |  |
| `supports_required` | `integer` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `idx_scoped_initiative_type_type` | `decidim_initiatives_types_id` |  | btree |
    | `idx_scoped_initiative_type_scope` | `decidim_scopes_id` |  | btree |
    | `index_decidim_initiatives_type_scopes_on_decidim_taxonomy_id` | `decidim_taxonomy_id` |  | btree |

### `decidim_initiatives_types` { #decidim-initiatives-types }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `area_enabled` | `boolean` | não | `false` |  |  |
| `attachments_enabled` | `boolean` | não | `false` |  |  |
| `child_scope_threshold_enabled` | `boolean` | não | `false` |  |  |
| `collect_user_extra_fields` | `boolean` | sim | `false` |  |  |
| `comments_enabled` | `boolean` | não | `true` |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `custom_signature_end_date_enabled` | `boolean` | não | `false` |  |  |
| `decidim_organization_id` | `integer` | sim |  | → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `description` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `document_number_authorization_handler` | `string` | sim |  |  |  |
| `extra_fields_legal_information` | `jsonb` | sim |  |  |  |
| `minimum_committee_members` | `integer` | sim |  |  |  |
| `only_global_scope_enabled` | `boolean` | não | `false` |  |  |
| `promoting_committee_enabled` | `boolean` | não | `true` |  |  |
| `signature_type` | `integer` | não | `0` |  |  |
| `title` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `undo_online_signatures_enabled` | `boolean` | não | `true` |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `validate_sms_code_on_votes` | `boolean` | sim | `false` |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_initiative_types_on_decidim_organization_id` | `decidim_organization_id` |  | btree |

### `decidim_initiatives_votes` { #decidim-initiatives-votes }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_author_id` | `bigint` | não |  |  |  |
| `decidim_initiative_id` | `bigint` | não |  | → [`decidim_initiatives`](outros-espacos.md#decidim-initiatives) |  |
| `decidim_scope_id` | `integer` | sim |  | → [`decidim_scopes`](componentes-conteudo.md#decidim-scopes) |  |
| `encrypted_metadata` | `text` | sim |  |  |  |
| `hash_id` | `string` | sim |  |  |  |
| `timestamp` | `string` | sim |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_initiatives_votes_on_decidim_author_id` | `decidim_author_id` |  | btree |
    | `index_decidim_initiatives_votes_on_decidim_initiative_id` | `decidim_initiative_id` |  | btree |
    | `index_decidim_initiatives_votes_on_hash_id` | `hash_id` |  | btree |

