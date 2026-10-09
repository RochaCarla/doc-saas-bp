# Texto participativo

O Participa tem um componente próprio de texto participativo, da gem `decidim-participatory_texts` (`Decidim.register_component(:participatory_texts)`, nome "Texto Participativo"). Ele é diferente do texto participativo que o Decidim oferece dentro do componente de propostas, usado no Brasil Participativo.

## O que faz

| Quem | O que pode fazer |
|------|------------------|
| Administrador | Criar o texto colando o conteúdo; mover, unir, ocultar e tornar interativos os parágrafos; registrar a **devolutiva** de cada comentário |
| Participante | Comentar parágrafos interativos, quando a etapa permite (`comments_enabled`, desligado por padrão) |

A edição usa Hotwire (Turbo e Stimulus) e o editor Jodit.

## Devolutiva por comentário

Cada comentário de parágrafo pode receber uma devolutiva com situação e texto (`decidim_participatory_texts_comment_feedbacks`):

| Situação | Significado |
|----------|-------------|
| `awaiting_review` | Aguardando análise (padrão) |
| `incorporated` | Incorporado ao texto |
| `partially_incorporated` | Incorporado em parte |
| `not_incorporated` | Não incorporado |

## Dados e API

| Item | Onde |
|------|------|
| Parágrafos | `decidim_participatory_texts_paragraphs` (título, corpo, nível, posição, oculto, interativo, contagem de comentários) |
| Devolutivas | `decidim_participatory_texts_comment_feedbacks` |
| GraphQL | Tipo `Paragraph` (`lib/decidim/api/paragraph_type.rb` da gem) |
| Dados abertos | Exporta os comentários dos parágrafos |

As migrações da gem não são copiadas para `db/migrate`: a gem acrescenta o próprio `db/migrate` em tempo de execução.

A gem não tem README. Esta página foi escrita a partir do código na revisão travada no `Gemfile.lock`.
