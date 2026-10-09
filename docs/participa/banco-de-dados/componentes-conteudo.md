---
title: Componentes, taxonomia, conteúdo e arquivos
icon: material/puzzle
---

<!-- Gerado por scripts/banco_de_dados.py em 2026-10-09T16:34:04+00:00. Não edite à mão. -->

# Componentes, taxonomia, conteúdo e arquivos

Componentes de cada espaço, taxonomias, categorias, escopos, áreas, anexos, blocos de conteúdo, páginas estáticas, modelos de processo, newsletters e arquivos do ActiveStorage.

**32 tabelas.** Schema versão `20260924162404`. Legenda da coluna **Referência**: *FK* = chave estrangeira declarada no banco; *→* = referência por convenção de nome (sem restrição no banco).

## Relacionamentos

Cada seta vai da tabela referenciada para a tabela que guarda a referência. Referências para outros domínios aparecem na coluna **Referência** das tabelas abaixo.

**A partir de `active_storage_blobs`**

```mermaid
flowchart TB
    active_storage_attachments["active_<br/>storage_<br/>attachments"]
    active_storage_blobs["active_<br/>storage_blobs"]
    active_storage_variant_records["active_<br/>storage_<br/>variant_<br/>records"]
    active_storage_blobs --> active_storage_attachments
    active_storage_blobs --> active_storage_variant_records
```

**A partir de `decidim_scope_types`**

```mermaid
flowchart TB
    decidim_scope_types["scope_types"]
    decidim_scopes["scopes"]
    decidim_searchable_resources["searchable_<br/>resources"]
    decidim_scope_types --> decidim_scopes
    decidim_scopes --> decidim_searchable_resources
```

**A partir de `decidim_taxonomies`**

```mermaid
flowchart TB
    decidim_taxonomies["taxonomies"]
    decidim_taxonomy_filter_items["taxonomy_<br/>filter_items"]
    decidim_taxonomy_filters["taxonomy_<br/>filters"]
    decidim_taxonomies --> decidim_taxonomy_filter_items
    decidim_taxonomies --> decidim_taxonomy_filters
    decidim_taxonomy_filters --> decidim_taxonomy_filter_items
```

**Outras relações**

```mermaid
flowchart LR
    decidim_area_types["area_types"]
    decidim_areas["areas"]
    decidim_attachment_collections["attachment_<br/>collections"]
    decidim_attachments["attachments"]
    decidim_categories["categories"]
    decidim_categorizations["categorizations"]
    decidim_content_block_attachments["content_block_<br/>attachments"]
    decidim_content_blocks["content_<br/>blocks"]
    decidim_static_page_topics["static_page_<br/>topics"]
    decidim_static_pages["static_pages"]
    decidim_area_types --> decidim_areas
    decidim_attachment_collections --> decidim_attachments
    decidim_categories --> decidim_categorizations
    decidim_content_blocks --> decidim_content_block_attachments
    decidim_static_page_topics --> decidim_static_pages
```

## Tabelas

| Tabela | Descrição | Colunas | Origem |
|---|---|---:|---|
| [`active_storage_attachments`](#active-storage-attachments) | Associação polimórfica entre registros e arquivos. | 6 | Decidim |
| [`active_storage_blobs`](#active-storage-blobs) | Metadados dos arquivos enviados (o conteúdo fica no storage). | 9 | Decidim |
| [`active_storage_variant_records`](#active-storage-variant-records) | — | 3 | Decidim |
| [`community_template_sources`](#community-template-sources) | Origem dos modelos de processo usados ou publicados pela organização (gem decidim-community_templates). | 7 | `decidim-community_templates` (LabLivre) |
| [`community_template_uses`](#community-template-uses) | Recursos criados a partir de um modelo de processo. | 7 | `decidim-community_templates` (LabLivre) |
| [`decidim_area_types`](#decidim-area-types) | — | 4 | Decidim |
| [`decidim_areas`](#decidim-areas) | Áreas. | 6 | Decidim |
| [`decidim_attachment_collections`](#decidim-attachment-collections) | Pastas (coleções) de anexos. | 6 | Decidim |
| [`decidim_attachments`](#decidim-attachments) | Anexos de espaços e recursos. | 12 | Decidim |
| [`decidim_categories`](#decidim-categories) | Categorias legadas do Decidim. O Participa usa as da gem decidim-categories. | 7 | Decidim |
| [`decidim_categories_categories`](#decidim-categories-categories) | Categorias hierárquicas por espaço participativo, com lixeira (gem decidim-categories). | 9 | `decidim-categories` (LabLivre) |
| [`decidim_categories_categorizations`](#decidim-categories-categorizations) | Associação entre recursos e categorias da gem decidim-categories. | 6 | `decidim-categories` (LabLivre) |
| [`decidim_categorizations`](#decidim-categorizations) | Associação legada entre recursos e categorias do Decidim. | 6 | Decidim |
| [`decidim_components`](#decidim-components) | Componentes de cada espaço (`manifest_name`: proposals, meetings, surveys, participatory_texts…). Polimórfico em `participatory_space`. | 13 | Decidim |
| [`decidim_content_block_attachments`](#decidim-content-block-attachments) | — | 3 | Decidim |
| [`decidim_content_blocks`](#decidim-content-blocks) | Blocos de conteúdo de páginas (home da organização e de espaços). | 11 | Decidim |
| [`decidim_contextual_help_sections`](#decidim-contextual-help-sections) | — | 4 | Decidim |
| [`decidim_editor_images`](#decidim-editor-images) | — | 5 | Decidim |
| [`decidim_newsletters`](#decidim-newsletters) | Newsletters. | 10 | Decidim |
| [`decidim_resource_links`](#decidim-resource-links) | Ligações entre recursos (ex.: proposta ↔ reunião). | 7 | Decidim |
| [`decidim_resource_permissions`](#decidim-resource-permissions) | — | 6 | Decidim |
| [`decidim_scope_types`](#decidim-scope-types) | Tipos de escopo. | 4 | Decidim |
| [`decidim_scopes`](#decidim-scopes) | Escopos (territoriais ou temáticos). | 9 | Decidim |
| [`decidim_searchable_resources`](#decidim-searchable-resources) | Índice de busca global. | 15 | Decidim |
| [`decidim_share_tokens`](#decidim-share-tokens) | — | 11 | Decidim |
| [`decidim_short_links`](#decidim-short-links) | — | 10 | Decidim |
| [`decidim_static_page_topics`](#decidim-static-page-topics) | Tópicos que agrupam páginas estáticas. | 6 | Decidim |
| [`decidim_static_pages`](#decidim-static-pages) | Páginas estáticas (`/pages`), como termos de uso e tutoriais. | 10 | Decidim |
| [`decidim_taxonomies`](#decidim-taxonomies) | Taxonomias do Decidim 0.32. A raiz "Categorias" e os tipos de processo são criados pela decidim-govbr. | 12 | Decidim |
| [`decidim_taxonomizations`](#decidim-taxonomizations) | Associação entre recursos e taxonomias. | 6 | Decidim |
| [`decidim_taxonomy_filter_items`](#decidim-taxonomy-filter-items) | — | 5 | Decidim |
| [`decidim_taxonomy_filters`](#decidim-taxonomy-filters) | — | 9 | Decidim |

### `active_storage_attachments` { #active-storage-attachments }

Associação polimórfica entre registros e arquivos.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `blob_id` | `bigint` | não |  | FK → [`active_storage_blobs`](componentes-conteudo.md#active-storage-blobs) |  |
| `created_at` | `datetime` | não |  |  |  |
| `name` | `string` | não |  |  |  |
| `record_id` | `bigint` | não |  | polimórfico (tipo em `record_type`) |  |
| `record_type` | `string` | não |  |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_active_storage_attachments_on_blob_id` | `blob_id` |  | btree |
    | `index_active_storage_attachments_uniqueness` | `record_type`, `record_id`, `name`, `blob_id` | sim | btree |

### `active_storage_blobs` { #active-storage-blobs }

Metadados dos arquivos enviados (o conteúdo fica no storage).

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `byte_size` | `bigint` | não |  |  |  |
| `checksum` | `string` | sim |  |  |  |
| `content_type` | `string` | sim |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `filename` | `string` | não |  |  |  |
| `key` | `string` | não |  |  |  |
| `metadata` | `text` | sim |  |  |  |
| `service_name` | `string` | não |  |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_active_storage_blobs_on_key` | `key` | sim | btree |

### `active_storage_variant_records` { #active-storage-variant-records }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `blob_id` | `bigint` | não |  | FK → [`active_storage_blobs`](componentes-conteudo.md#active-storage-blobs) |  |
| `variation_digest` | `string` | não |  |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_active_storage_variant_records_uniqueness` | `blob_id`, `variation_digest` | sim | btree |

### `community_template_sources` { #community-template-sources }

Origem dos modelos de processo usados ou publicados pela organização (gem decidim-community_templates).

Origem: `decidim-community_templates` (LabLivre).

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_organization_id` | `integer` | sim |  | → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `source_id` | `integer` | sim |  | polimórfico (tipo em `source_type`) |  |
| `source_type` | `string` | sim |  |  |  |
| `template_id` | `string` | sim |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_community_template_sources_on_decidim_organization_id` | `decidim_organization_id` |  | btree |
    | `unique_community_template_sources_on_organization` | `source_type`, `source_id`, `decidim_organization_id` | sim | btree |
    | `index_community_template_sources_on_template_id` | `template_id` |  | btree |

### `community_template_uses` { #community-template-uses }

Recursos criados a partir de um modelo de processo.

Origem: `decidim-community_templates` (LabLivre).

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_organization_id` | `integer` | sim |  | → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `resource_id` | `integer` | sim |  | polimórfico (tipo em `resource_type`) |  |
| `resource_type` | `string` | sim |  |  |  |
| `template_id` | `string` | sim |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_community_template_uses_on_decidim_organization_id` | `decidim_organization_id` |  | btree |
    | `unique_community_template_uses_on_organization` | `resource_type`, `resource_id`, `decidim_organization_id` | sim | btree |
    | `index_community_template_uses_on_template_id` | `template_id` |  | btree |

### `decidim_area_types` { #decidim-area-types }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `decidim_organization_id` | `bigint` | sim |  | FK → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `name` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `plural` | `jsonb` | não |  |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_area_types_on_decidim_organization_id` | `decidim_organization_id` |  | btree |

### `decidim_areas` { #decidim-areas }

Áreas.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `area_type_id` | `bigint` | sim |  | FK → [`decidim_area_types`](componentes-conteudo.md#decidim-area-types) |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_organization_id` | `bigint` | sim |  | FK → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `name` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_areas_on_area_type_id` | `area_type_id` |  | btree |
    | `index_decidim_areas_on_decidim_organization_id` | `decidim_organization_id` |  | btree |

### `decidim_attachment_collections` { #decidim-attachment-collections }

Pastas (coleções) de anexos.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `collection_for_id` | `bigint` | não |  | polimórfico (tipo em `collection_for_type`) |  |
| `collection_for_type` | `string` | não |  |  |  |
| `description` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `name` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `weight` | `integer` | não | `0` |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `decidim_attachment_collections_collection_for_id_and_type` | `collection_for_type`, `collection_for_id` |  | btree |

### `decidim_attachments` { #decidim-attachments }

Anexos de espaços e recursos.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `attached_to_id` | `integer` | não |  | polimórfico (tipo em `attached_to_type`) |  |
| `attached_to_type` | `string` | não |  |  |  |
| `attachment_collection_id` | `integer` | sim |  | FK → [`decidim_attachment_collections`](componentes-conteudo.md#decidim-attachment-collections) |  |
| `content_type` | `string` | não |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `description` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `file_size` | `string` | não |  |  |  |
| `link` | `string` | sim |  |  |  |
| `title` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `updated_at` | `datetime` | não |  |  |  |
| `weight` | `integer` | não | `0` |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_attachments_on_attached_to` | `attached_to_id`, `attached_to_type` |  | btree |
    | `index_decidim_attachments_on_attachment_collection_id` | `attachment_collection_id` |  | btree |

### `decidim_categories` { #decidim-categories }

Categorias legadas do Decidim. O Participa usa as da gem decidim-categories.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `decidim_participatory_space_id` | `integer` | sim |  | polimórfico (tipo em `decidim_participatory_space_type`) | — |
| `decidim_participatory_space_type` | `string` | sim |  |  |  |
| `description` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `name` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `parent_id` | `integer` | sim |  | → [`decidim_categories`](componentes-conteudo.md#decidim-categories) |  |
| `weight` | `integer` | não | `0` |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_categories_on_decidim_participatory_space` | `decidim_participatory_space_id`, `decidim_participatory_space_type` |  | btree |
    | `index_decidim_categories_on_parent_id` | `parent_id` |  | btree |

### `decidim_categories_categories` { #decidim-categories-categories }

Categorias hierárquicas por espaço participativo, com lixeira (gem decidim-categories).

Origem: `decidim-categories` (LabLivre).

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_participatory_space_id` | `bigint` | não |  | polimórfico (tipo em `decidim_participatory_space_type`) |  |
| `decidim_participatory_space_type` | `string` | não |  |  |  |
| `deleted_at` | `datetime` | sim |  |  |  |
| `name` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `parent_id` | `integer` | sim |  | → [`decidim_categories_categories`](componentes-conteudo.md#decidim-categories-categories) |  |
| `updated_at` | `datetime` | não |  |  |  |
| `weight` | `integer` | sim |  |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `idx_cat_categories_on_ps` | `decidim_participatory_space_id`, `decidim_participatory_space_type` |  | btree |
    | `idx_categories_on_participatory_space` | `decidim_participatory_space_id`, `decidim_participatory_space_type` |  | btree |

### `decidim_categories_categorizations` { #decidim-categories-categorizations }

Associação entre recursos e categorias da gem decidim-categories.

Origem: `decidim-categories` (LabLivre).

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `categorizable_id` | `bigint` | não |  | polimórfico (tipo em `categorizable_type`) |  |
| `categorizable_type` | `string` | não |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_categories_category_id` | `bigint` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `idx_decidim_categories_categorizations_on_categorizable` | `categorizable_id`, `categorizable_type` |  | btree |
    | `idx_unique_decidim_categories_categorizations` | `decidim_categories_category_id`, `categorizable_id`, `categorizable_type` | sim | btree |
    | `idx_decidim_categories_categorizations_on_category_id` | `decidim_categories_category_id` |  | btree |

### `decidim_categorizations` { #decidim-categorizations }

Associação legada entre recursos e categorias do Decidim.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `categorizable_id` | `bigint` | não |  | polimórfico (tipo em `categorizable_type`) |  |
| `categorizable_type` | `string` | não |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_category_id` | `bigint` | não |  | → [`decidim_categories`](componentes-conteudo.md#decidim-categories) |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `decidim_categorizations_categorizable_id_and_type` | `categorizable_type`, `categorizable_id` |  | btree |
    | `index_decidim_categorizations_on_decidim_category_id` | `decidim_category_id` |  | btree |

### `decidim_components` { #decidim-components }

Componentes de cada espaço (`manifest_name`: proposals, meetings, surveys, participatory_texts…). Polimórfico em `participatory_space`.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `deleted_at` | `datetime` | sim |  |  |  |
| `manifest_name` | `string` | sim |  |  |  |
| `name` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `participatory_space_id` | `integer` | não |  | polimórfico (tipo em `participatory_space_type`) |  |
| `participatory_space_type` | `string` | não |  |  |  |
| `permissions` | `jsonb` | sim |  |  |  |
| `published_at` | `datetime` | sim |  |  |  |
| `settings` | `jsonb` | sim | `{}` |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `visible` | `boolean` | sim | `true` |  |  |
| `weight` | `integer` | sim | `0` |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_components_on_deleted_at` | `deleted_at` |  | btree |
    | `index_decidim_components_on_decidim_participatory_space` | `participatory_space_id`, `participatory_space_type` |  | btree |

### `decidim_content_block_attachments` { #decidim-content-block-attachments }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `decidim_content_block_id` | `bigint` | não |  | → [`decidim_content_blocks`](componentes-conteudo.md#decidim-content-blocks) |  |
| `name` | `string` | sim |  |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `decidim_content_block_attachments_on_content_block` | `decidim_content_block_id` |  | btree |

### `decidim_content_blocks` { #decidim-content-blocks }

Blocos de conteúdo de páginas (home da organização e de espaços).

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_organization_id` | `integer` | não |  | → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `images` | `jsonb` | sim | `{}` |  |  |
| `manifest_name` | `string` | não |  |  |  |
| `published_at` | `datetime` | sim |  |  |  |
| `scope_name` | `string` | não |  |  |  |
| `scoped_resource_id` | `integer` | sim |  |  |  |
| `settings` | `jsonb` | sim |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `weight` | `integer` | sim |  |  |  |

??? note "Índices (5)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `idx_decidim_content_blocks_org_id_scope_scope_id_manifest` | `decidim_organization_id`, `scope_name`, `scoped_resource_id`, `manifest_name` |  | btree |
    | `index_decidim_content_blocks_on_decidim_organization_id` | `decidim_organization_id` |  | btree |
    | `index_decidim_content_blocks_on_manifest_name` | `manifest_name` |  | btree |
    | `index_decidim_content_blocks_on_published_at` | `published_at` |  | btree |
    | `index_decidim_content_blocks_on_scope_name` | `scope_name` |  | btree |

### `decidim_contextual_help_sections` { #decidim-contextual-help-sections }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `content` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `organization_id` | `bigint` | não |  | → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `section_id` | `string` | não |  | → [`decidim_contextual_help_sections`](componentes-conteudo.md#decidim-contextual-help-sections) |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_contextual_help_sections_on_organization_id` | `organization_id` |  | btree |
    | `index_decidim_contextual_help_sections_on_section_id` | `section_id` |  | btree |

### `decidim_editor_images` { #decidim-editor-images }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_author_id` | `bigint` | não |  | FK → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `decidim_organization_id` | `bigint` | não |  | FK → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `decidim_editor_images_author` | `decidim_author_id` |  | btree |
    | `decidim_editor_images_constraint_organization` | `decidim_organization_id` |  | btree |

### `decidim_newsletters` { #decidim-newsletters }

Newsletters.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `author_id` | `integer` | sim |  | FK → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `created_at` | `datetime` | não |  |  |  |
| `extended_data` | `jsonb` | sim | `{}` |  |  |
| `organization_id` | `integer` | sim |  | → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `sent_at` | `datetime` | sim |  |  |  |
| `subject` | `jsonb` | sim |  |  |  |
| `total_deliveries` | `integer` | sim |  |  |  |
| `total_recipients` | `integer` | sim |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_newsletters_on_author_id` | `author_id` |  | btree |
    | `index_decidim_newsletters_on_organization_id` | `organization_id` |  | btree |

### `decidim_resource_links` { #decidim-resource-links }

Ligações entre recursos (ex.: proposta ↔ reunião).

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `data` | `jsonb` | sim |  |  |  |
| `from_id` | `integer` | não |  | polimórfico (tipo em `from_type`) |  |
| `from_type` | `string` | não |  |  |  |
| `name` | `string` | não |  |  |  |
| `to_id` | `integer` | não |  | polimórfico (tipo em `to_type`) |  |
| `to_type` | `string` | não |  |  |  |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_resource_links_on_from_type_and_from_id` | `from_type`, `from_id` |  | btree |
    | `index_decidim_resource_links_on_name` | `name` |  | btree |
    | `index_decidim_resource_links_on_to_type_and_to_id` | `to_type`, `to_id` |  | btree |

### `decidim_resource_permissions` { #decidim-resource-permissions }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `permissions` | `jsonb` | sim | `{}` |  |  |
| `resource_id` | `bigint` | sim |  | polimórfico (tipo em `resource_type`) |  |
| `resource_type` | `string` | sim |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_resource_permissions_on_r_type_and_r_id` | `resource_type`, `resource_id` | sim | btree |

### `decidim_scope_types` { #decidim-scope-types }

Tipos de escopo.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `decidim_organization_id` | `integer` | sim |  | FK → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `name` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `plural` | `jsonb` | não |  |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_scope_types_on_decidim_organization_id` | `decidim_organization_id` |  | btree |

### `decidim_scopes` { #decidim-scopes }

Escopos (territoriais ou temáticos).

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `code` | `string` | não |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_organization_id` | `integer` | sim |  | FK → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `name` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `parent_id` | `integer` | sim |  | FK → [`decidim_scopes`](componentes-conteudo.md#decidim-scopes) |  |
| `part_of` | `integer[]` | não | `[]` |  |  |
| `scope_type_id` | `integer` | sim |  | FK → [`decidim_scope_types`](componentes-conteudo.md#decidim-scope-types) |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (5)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_scopes_on_decidim_organization_id_and_code` | `decidim_organization_id`, `code` | sim | btree |
    | `index_decidim_scopes_on_decidim_organization_id` | `decidim_organization_id` |  | btree |
    | `index_decidim_scopes_on_parent_id` | `parent_id` |  | btree |
    | `index_decidim_scopes_on_part_of` | `part_of` |  | gin |
    | `index_decidim_scopes_on_scope_type_id` | `scope_type_id` |  | btree |

### `decidim_searchable_resources` { #decidim-searchable-resources }

Índice de busca global.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `content_a` | `text` | sim |  |  |  |
| `content_b` | `text` | sim |  |  |  |
| `content_c` | `text` | sim |  |  |  |
| `content_d` | `text` | sim |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `datetime` | `datetime` | sim |  |  |  |
| `decidim_organization_id` | `bigint` | sim |  | → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `decidim_participatory_space_id` | `bigint` | sim |  | polimórfico (tipo em `decidim_participatory_space_type`) |  |
| `decidim_participatory_space_type` | `string` | sim |  |  |  |
| `decidim_scope_id` | `bigint` | sim |  | → [`decidim_scopes`](componentes-conteudo.md#decidim-scopes) |  |
| `locale` | `string` | não |  |  |  |
| `resource_id` | `bigint` | sim |  | polimórfico (tipo em `resource_type`) |  |
| `resource_type` | `string` | sim |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (4)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_searchable_resources_on_decidim_organization_id` | `decidim_organization_id` |  | btree |
    | `index_decidim_searchable_resource_on_pspace_type_and_pspace_id` | `decidim_participatory_space_type`, `decidim_participatory_space_id` |  | btree |
    | `index_decidim_searchable_resources_on_decidim_scope_id` | `decidim_scope_id` |  | btree |
    | `index_decidim_searchable_rsrcs_on_s_type_and_s_id` | `resource_type`, `resource_id` |  | btree |

### `decidim_share_tokens` { #decidim-share-tokens }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | sim |  |  |  |
| `decidim_organization_id` | `bigint` | não |  | → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `decidim_user_id` | `bigint` | não |  | → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `expires_at` | `datetime` | sim |  |  |  |
| `last_used_at` | `datetime` | sim |  |  |  |
| `registered_only` | `boolean` | sim |  |  |  |
| `times_used` | `integer` | sim | `0` |  |  |
| `token` | `string` | não |  |  |  |
| `token_for_id` | `bigint` | não |  | polimórfico (tipo em `token_for_type`) |  |
| `token_for_type` | `string` | não |  |  |  |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_share_tokens_on_decidim_organization_id` | `decidim_organization_id` |  | btree |
    | `index_decidim_share_tokens_on_decidim_user_id` | `decidim_user_id` |  | btree |
    | `decidim_share_tokens_token_for` | `token_for_type`, `token_for_id` |  | btree |

### `decidim_short_links` { #decidim-short-links }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_organization_id` | `bigint` | não |  | → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `identifier` | `string` | não |  |  |  |
| `mounted_engine_name` | `string` | sim |  |  |  |
| `params` | `jsonb` | sim |  |  |  |
| `route_name` | `string` | sim |  |  |  |
| `target_id` | `bigint` | não |  | polimórfico (tipo em `target_type`) |  |
| `target_type` | `string` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (5)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `idx_decidim_short_links_organization_id_identifier` | `decidim_organization_id`, `identifier` | sim | btree |
    | `index_decidim_short_links_on_decidim_organization_id` | `decidim_organization_id` |  | btree |
    | `index_decidim_short_links_on_mounted_engine_name` | `mounted_engine_name` |  | btree |
    | `index_decidim_short_links_on_route_name` | `route_name` |  | btree |
    | `index_decidim_short_links_on_target` | `target_type`, `target_id` |  | btree |

### `decidim_static_page_topics` { #decidim-static-page-topics }

Tópicos que agrupam páginas estáticas.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `description` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `organization_id` | `bigint` | não |  | → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `show_in_footer` | `boolean` | não | `false` |  |  |
| `title` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `weight` | `integer` | sim |  |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_static_page_topics_on_organization_id` | `organization_id` |  | btree |

### `decidim_static_pages` { #decidim-static-pages }

Páginas estáticas (`/pages`), como termos de uso e tutoriais.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `allow_public_access` | `boolean` | não | `false` |  |  |
| `content` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_organization_id` | `integer` | sim |  | FK → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `slug` | `string` | não |  |  |  |
| `title` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `topic_id` | `bigint` | sim |  | → [`decidim_static_page_topics`](componentes-conteudo.md#decidim-static-page-topics) |  |
| `updated_at` | `datetime` | não |  |  |  |
| `weight` | `integer` | sim |  |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_static_pages_on_decidim_organization_id` | `decidim_organization_id` |  | btree |
    | `index_decidim_static_pages_on_topic_id` | `topic_id` |  | btree |

### `decidim_taxonomies` { #decidim-taxonomies }

Taxonomias do Decidim 0.32. A raiz "Categorias" e os tipos de processo são criados pela decidim-govbr.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `children_count` | `integer` | não | `0` | contador em cache |  |
| `created_at` | `datetime` | não |  |  |  |
| `decidim_organization_id` | `bigint` | não |  | → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `filter_items_count` | `integer` | não | `0` | contador em cache |  |
| `filters_count` | `integer` | não | `0` | contador em cache |  |
| `name` | `jsonb` | não | `{}` | traduzível (`{"pt-BR": …}`) |  |
| `parent_id` | `bigint` | sim |  | → [`decidim_taxonomies`](componentes-conteudo.md#decidim-taxonomies) |  |
| `part_of` | `integer[]` | não | `[]` |  |  |
| `taxonomizations_count` | `integer` | não | `0` | contador em cache |  |
| `updated_at` | `datetime` | não |  |  |  |
| `weight` | `integer` | sim |  |  |  |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_taxonomies_on_decidim_organization_id` | `decidim_organization_id` |  | btree |
    | `index_decidim_taxonomies_on_parent_id` | `parent_id` |  | btree |
    | `index_decidim_taxonomies_on_part_of` | `part_of` |  | gin |

### `decidim_taxonomizations` { #decidim-taxonomizations }

Associação entre recursos e taxonomias.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `taxonomizable_id` | `bigint` | não |  | polimórfico (tipo em `taxonomizable_type`) |  |
| `taxonomizable_type` | `string` | não |  |  |  |
| `taxonomy_id` | `bigint` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_taxonomizations_on_taxonomizable` | `taxonomizable_type`, `taxonomizable_id` |  | btree |
    | `index_taxonomizations_on_id_tid_and_ttype` | `taxonomy_id`, `taxonomizable_id`, `taxonomizable_type` | sim | btree |
    | `index_decidim_taxonomizations_on_taxonomy_id` | `taxonomy_id` |  | btree |

### `decidim_taxonomy_filter_items` { #decidim-taxonomy-filter-items }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `created_at` | `datetime` | não |  |  |  |
| `taxonomy_filter_id` | `bigint` | não |  | → [`decidim_taxonomy_filters`](componentes-conteudo.md#decidim-taxonomy-filters) |  |
| `taxonomy_item_id` | `bigint` | não |  | FK → [`decidim_taxonomies`](componentes-conteudo.md#decidim-taxonomies) |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_taxonomy_filter_items_on_filter_id_and_item_id` | `taxonomy_filter_id`, `taxonomy_item_id` | sim | btree |
    | `index_decidim_taxonomy_filter_items_on_taxonomy_filter_id` | `taxonomy_filter_id` |  | btree |
    | `index_decidim_taxonomy_filter_items_on_taxonomy_item_id` | `taxonomy_item_id` |  | btree |

### `decidim_taxonomy_filters` { #decidim-taxonomy-filters }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `components_count` | `integer` | não | `0` | contador em cache |  |
| `created_at` | `datetime` | não |  |  |  |
| `filter_items_count` | `integer` | não | `0` | contador em cache |  |
| `internal_name` | `jsonb` | sim | `{}` |  |  |
| `name` | `jsonb` | sim | `{}` | traduzível (`{"pt-BR": …}`) |  |
| `participatory_space_manifests` | `string[]` | não | `[]` |  |  |
| `root_taxonomy_id` | `bigint` | não |  | FK → [`decidim_taxonomies`](componentes-conteudo.md#decidim-taxonomies) |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_taxonomy_filters_on_root_taxonomy_id` | `root_taxonomy_id` |  | btree |

