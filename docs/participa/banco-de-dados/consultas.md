---
title: Consultas úteis
icon: material/database-search
---

# Consultas úteis

Exemplos de SQL para investigar dados do Participa. Rode em uma réplica ou cópia, nunca direto no primário de produção.

## Escolher a organização

Cada organização tem um schema próprio. Antes de qualquer consulta, descubra o schema pelo host e ajuste o `search_path`:

```sql
-- no schema public
SELECT host, key FROM public.apartment_distribution_keys ORDER BY host;

-- entra na organização (troque pela chave UUID do host)
SET search_path TO "<chave-uuid>", shared_extensions;
SELECT id, host, name->>'pt-BR' AS nome FROM decidim_organizations;
```

Para comparar organizações, repita a consulta em cada schema ou monte uma união:

```sql
SELECT 'org-a' AS org, count(*) FROM "<chave-a>".decidim_users WHERE deleted_at IS NULL
UNION ALL
SELECT 'org-b', count(*) FROM "<chave-b>".decidim_users WHERE deleted_at IS NULL;
```

## Participantes

```sql
-- participantes por forma de verificação
SELECT a.name AS verificacao, count(DISTINCT a.decidim_user_id) AS participantes
FROM decidim_authorizations a
GROUP BY a.name
ORDER BY participantes DESC;

-- logins pelo gov.br
SELECT count(*) FROM decidim_identities WHERE provider = 'govbr';
```

## Processos e etapas

```sql
-- processos publicados com a etapa ativa
SELECT p.slug, p.title->>'pt-BR' AS titulo, s.title->>'pt-BR' AS etapa_ativa,
       p.automatic_step_activation AS troca_automatica
FROM decidim_participatory_processes p
LEFT JOIN decidim_participatory_process_steps s
  ON s.decidim_participatory_process_id = p.id AND s.active
WHERE p.published_at IS NOT NULL
ORDER BY p.published_at DESC;

-- processos por setor (decidim-government_spaces)
SELECT gs.title->>'pt-BR' AS setor, count(*) AS processos
FROM decidim_government_spaces_process_assignments pa
JOIN decidim_government_spaces gs ON gs.id = pa.government_space_id
GROUP BY setor
ORDER BY processos DESC;
```

## Propostas e votos

```sql
-- propostas mais votadas de um componente
SELECT p.id, p.title->>'pt-BR' AS titulo, p.proposal_votes_count AS votos
FROM decidim_proposals_proposals p
WHERE p.decidim_component_id = :componente
  AND p.published_at IS NOT NULL
  AND p.withdrawn_at IS NULL
ORDER BY votos DESC
LIMIT 20;
```

## Texto participativo

```sql
-- devolutivas por situação num componente de texto participativo
SELECT f.status, count(*)
FROM decidim_participatory_texts_comment_feedbacks f
JOIN decidim_participatory_texts_paragraphs pg ON pg.id = f.decidim_paragraph_id
WHERE pg.decidim_component_id = :componente
GROUP BY f.status;
```

## Chatbot

```sql
-- conversas e votos confirmados pelo chatbot
SELECT broker, count(*) AS conversas, count(confirmed_at) AS votos_confirmados
FROM decidim_chatbot_conversations
GROUP BY broker;

-- mensagens com falha nas últimas 24 horas
SELECT direction, kind, count(*)
FROM decidim_chatbot_events
WHERE status = 'failed' AND occurred_at > now() - interval '24 hours'
GROUP BY direction, kind;
```

## Conferir a estrutura dos schemas

Prefira as tarefas do repositório, que percorrem todos os schemas:

```bash
bin/rails apartment:schema_drift
bin/rails "apartment:check_column[decidim_users,document_number]"
```

!!! note "Colunas citadas"
    As consultas usam as colunas do `schema.rb` da `main`. Confira o [dicionário](index.md) se a versão do banco for outra.
