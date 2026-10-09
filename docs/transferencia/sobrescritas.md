---
title: Inventário de sobrescritas
---

<!-- Gerado por scripts/sobrescritas.py em 2026-10-08T14:15:31+00:00. Não edite à mão. -->

# Inventário de sobrescritas

Arquivos do `participa` (branch `main`) que **substituem** arquivos do Decidim 0.32.1. O Rails carrega a versão da aplicação no lugar da versão da gem, então cada um deles precisa ser revisado ao atualizar o Decidim. Veja o [Plano de atualização tecnológica](atualizacao.md).

!!! note "Engines do próprio repositório"
    Arquivos de mesmo caminho dentro de `decidim-govbr`, `decidim-chatbot` também competem com os do Decidim. Para eles, a precedência depende da ordem de carregamento das engines; a coluna **Origem** indica onde cada arquivo está.

!!! info "Gerado em 08/10/2026"
    Comparação de `app/`, `lib/`, `config/initializers/` (da aplicação e das engines) com as gems do Decidim na tag `v0.32.1`. Para atualizar, rode `python3 scripts/sobrescritas.py`.

## Resumo

| Item | Quantidade |
|---|---:|
| Arquivos sobrescritos | 31 |
| Linhas diferentes do original (adicionadas + removidas) | 1.980 |
| Sobrescritas idênticas ao original (podem ser removidas) | 0 |
| Arquivos próprios, sem equivalente no Decidim | 301 |

## Por gem do Decidim

Quanto mais linhas diferentes, maior o esforço de atualização.

| Gem | Arquivos sobrescritos | Linhas diferentes |
|---|---:|---:|
| `decidim-core` | 10 | 1.179 |
| `decidim-participatory_processes` | 3 | 334 |
| `decidim-admin` | 7 | 233 |
| `decidim-budgets` | 5 | 110 |
| `decidim-comments` | 3 | 105 |
| `decidim-meetings` | 2 | 12 |
| `decidim-accountability` | 1 | 7 |

## Por tipo de arquivo

| Tipo | Arquivos | Linhas diferentes |
|---|---:|---:|
| `packs` | 5 | 942 |
| `views` | 20 | 873 |
| `cells` | 5 | 158 |
| `jobs` | 1 | 7 |

## As 40 sobrescritas mais alteradas

| Arquivo | Origem | Gem | + | − | Linhas no Participa |
|---|---|---|---:|---:|---:|
| [`app/packs/stylesheets/decidim/decidim_application.scss`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/app/packs/stylesheets/decidim/decidim_application.scss) | aplicação | `decidim-core` | 651 | 5 | 655 |
| [`app/views/decidim/participatory_processes/admin/participatory_processes/_form.html.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/decidim-govbr/app/views/decidim/participatory_processes/admin/participatory_processes/_form.html.erb) | decidim-govbr | `decidim-participatory_processes` | 158 | 154 | 236 |
| [`app/packs/src/decidim/decidim_application.js`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/app/packs/src/decidim/decidim_application.js) | aplicação | `decidim-core` | 232 | 1 | 232 |
| [`app/views/layouts/decidim/footer/_main_links.html.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/app/views/layouts/decidim/footer/_main_links.html.erb) | aplicação | `decidim-core` | 38 | 55 | 42 |
| [`app/views/decidim/admin/attachments/_form.html.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/decidim-govbr/app/views/decidim/admin/attachments/_form.html.erb) | decidim-govbr | `decidim-admin` | 56 | 36 | 64 |
| [`app/views/decidim/devise/sessions/new.html.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/decidim-govbr/app/views/decidim/devise/sessions/new.html.erb) | decidim-govbr | `decidim-core` | 44 | 47 | 49 |
| [`app/views/decidim/admin/attachments/index.html.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/decidim-govbr/app/views/decidim/admin/attachments/index.html.erb) | decidim-govbr | `decidim-admin` | 24 | 36 | 62 |
| [`app/cells/decidim/comments/comment_form/show.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/app/cells/decidim/comments/comment_form/show.erb) | aplicação | `decidim-comments` | 37 | 4 | 76 |
| [`app/cells/decidim/budgets/budget_information_modal_cell.rb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/app/cells/decidim/budgets/budget_information_modal_cell.rb) | aplicação | `decidim-budgets` | 35 | 2 | 55 |
| [`app/cells/decidim/comments/edit_comment_modal_form/show.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/app/cells/decidim/comments/edit_comment_modal_form/show.erb) | aplicação | `decidim-comments` | 32 | 5 | 61 |
| [`app/views/decidim/admin/dashboard/show.html.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/decidim-govbr/app/views/decidim/admin/dashboard/show.html.erb) | decidim-govbr | `decidim-admin` | 25 | 11 | 65 |
| [`app/cells/decidim/budgets/budget_information_modal/show.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/app/cells/decidim/budgets/budget_information_modal/show.erb) | aplicação | `decidim-budgets` | 30 | 5 | 41 |
| [`app/views/decidim/comments/comments/update_error.js.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/app/views/decidim/comments/comments/update_error.js.erb) | aplicação | `decidim-comments` | 26 | 1 | 26 |
| [`app/views/decidim/devise/shared/_omniauth_buttons.html.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/decidim-govbr/app/views/decidim/devise/shared/_omniauth_buttons.html.erb) | decidim-govbr | `decidim-core` | 15 | 11 | 19 |
| [`app/views/layouts/decidim/_head_extra.html.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/decidim-govbr/app/views/layouts/decidim/_head_extra.html.erb) | decidim-govbr | `decidim-core` | 11 | 13 | 12 |
| [`app/packs/stylesheets/decidim/admin/decidim_application.scss`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/app/packs/stylesheets/decidim/admin/decidim_application.scss) | aplicação | `decidim-admin` | 17 | 5 | 17 |
| [`app/views/decidim/participatory_processes/admin/participatory_process_steps/_form.html.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/decidim-govbr/app/views/decidim/participatory_processes/admin/participatory_process_steps/_form.html.erb) | decidim-govbr | `decidim-participatory_processes` | 13 | 7 | 27 |
| [`app/views/layouts/decidim/_head_extra.html.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/app/views/layouts/decidim/_head_extra.html.erb) | aplicação | `decidim-core` | 5 | 14 | 5 |
| [`app/packs/src/decidim/datepicker/generate_datepicker.js`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/app/packs/src/decidim/datepicker/generate_datepicker.js) | aplicação | `decidim-core` | 15 | 2 | 158 |
| [`app/packs/src/decidim/datepicker/generate_timepicker.js`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/app/packs/src/decidim/datepicker/generate_timepicker.js) | aplicação | `decidim-core` | 8 | 6 | 312 |
| [`app/views/decidim/budgets/projects/order_progress_summary/_content.html.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/app/views/decidim/budgets/projects/order_progress_summary/_content.html.erb) | aplicação | `decidim-budgets` | 2 | 12 | 22 |
| [`app/views/decidim/budgets/projects/order_progress_summary/_content_responsive.html.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/app/views/decidim/budgets/projects/order_progress_summary/_content_responsive.html.erb) | aplicação | `decidim-budgets` | 2 | 11 | 47 |
| [`app/views/decidim/budgets/projects/order_progress_summary/_progress_box_buttons.html.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/app/views/decidim/budgets/projects/order_progress_summary/_progress_box_buttons.html.erb) | aplicação | `decidim-budgets` | 1 | 10 | 3 |
| [`app/views/decidim/admin/help_sections/_form.html.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/decidim-govbr/app/views/decidim/admin/help_sections/_form.html.erb) | decidim-govbr | `decidim-admin` | 9 | 0 | 46 |
| [`app/views/decidim/admin/logs/_filters.html.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/decidim-govbr/app/views/decidim/admin/logs/_filters.html.erb) | decidim-govbr | `decidim-admin` | 6 | 3 | 40 |
| [`app/cells/decidim/meetings/highlighted_meetings_for_component/show.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/decidim-govbr/app/cells/decidim/meetings/highlighted_meetings_for_component/show.erb) | decidim-govbr | `decidim-meetings` | 2 | 6 | 25 |
| [`app/jobs/application_job.rb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/app/jobs/application_job.rb) | aplicação | `decidim-accountability` | 5 | 2 | 7 |
| [`app/views/decidim/newsletter_mailer/newsletter.html.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/app/views/decidim/newsletter_mailer/newsletter.html.erb) | aplicação | `decidim-core` | 5 | 1 | 20 |
| [`app/views/layouts/decidim/admin/_header.html.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/app/views/layouts/decidim/admin/_header.html.erb) | aplicação | `decidim-admin` | 5 | 0 | 16 |
| [`app/views/decidim/meetings/admin/agenda/_form.html.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/app/views/decidim/meetings/admin/agenda/_form.html.erb) | aplicação | `decidim-meetings` | 2 | 2 | 72 |
| [`app/views/decidim/participatory_processes/admin/participatory_processes/_processes_thead.html.erb`](https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main/decidim-govbr/app/views/decidim/participatory_processes/admin/participatory_processes/_processes_thead.html.erb) | decidim-govbr | `decidim-participatory_processes` | 1 | 1 | 19 |

## Lista completa por gem

??? note "`decidim-accountability` — 1 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/jobs/application_job.rb` | 5 | 2 |

??? note "`decidim-admin` — 7 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/packs/stylesheets/decidim/admin/decidim_application.scss` | 17 | 5 |
    | `app/views/layouts/decidim/admin/_header.html.erb` | 5 | 0 |
    | `decidim-govbr/app/views/decidim/admin/attachments/_form.html.erb` | 56 | 36 |
    | `decidim-govbr/app/views/decidim/admin/attachments/index.html.erb` | 24 | 36 |
    | `decidim-govbr/app/views/decidim/admin/dashboard/show.html.erb` | 25 | 11 |
    | `decidim-govbr/app/views/decidim/admin/help_sections/_form.html.erb` | 9 | 0 |
    | `decidim-govbr/app/views/decidim/admin/logs/_filters.html.erb` | 6 | 3 |

??? note "`decidim-budgets` — 5 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/cells/decidim/budgets/budget_information_modal/show.erb` | 30 | 5 |
    | `app/cells/decidim/budgets/budget_information_modal_cell.rb` | 35 | 2 |
    | `app/views/decidim/budgets/projects/order_progress_summary/_content.html.erb` | 2 | 12 |
    | `app/views/decidim/budgets/projects/order_progress_summary/_content_responsive.html.erb` | 2 | 11 |
    | `app/views/decidim/budgets/projects/order_progress_summary/_progress_box_buttons.html.erb` | 1 | 10 |

??? note "`decidim-comments` — 3 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/cells/decidim/comments/comment_form/show.erb` | 37 | 4 |
    | `app/cells/decidim/comments/edit_comment_modal_form/show.erb` | 32 | 5 |
    | `app/views/decidim/comments/comments/update_error.js.erb` | 26 | 1 |

??? note "`decidim-core` — 10 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/packs/src/decidim/datepicker/generate_datepicker.js` | 15 | 2 |
    | `app/packs/src/decidim/datepicker/generate_timepicker.js` | 8 | 6 |
    | `app/packs/src/decidim/decidim_application.js` | 232 | 1 |
    | `app/packs/stylesheets/decidim/decidim_application.scss` | 651 | 5 |
    | `app/views/decidim/newsletter_mailer/newsletter.html.erb` | 5 | 1 |
    | `app/views/layouts/decidim/_head_extra.html.erb` | 5 | 14 |
    | `app/views/layouts/decidim/footer/_main_links.html.erb` | 38 | 55 |
    | `decidim-govbr/app/views/decidim/devise/sessions/new.html.erb` | 44 | 47 |
    | `decidim-govbr/app/views/decidim/devise/shared/_omniauth_buttons.html.erb` | 15 | 11 |
    | `decidim-govbr/app/views/layouts/decidim/_head_extra.html.erb` | 11 | 13 |

??? note "`decidim-meetings` — 2 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/views/decidim/meetings/admin/agenda/_form.html.erb` | 2 | 2 |
    | `decidim-govbr/app/cells/decidim/meetings/highlighted_meetings_for_component/show.erb` | 2 | 6 |

??? note "`decidim-participatory_processes` — 3 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `decidim-govbr/app/views/decidim/participatory_processes/admin/participatory_process_steps/_form.html.erb` | 13 | 7 |
    | `decidim-govbr/app/views/decidim/participatory_processes/admin/participatory_processes/_form.html.erb` | 158 | 154 |
    | `decidim-govbr/app/views/decidim/participatory_processes/admin/participatory_processes/_processes_thead.html.erb` | 1 | 1 |

## Arquivos próprios

Arquivos sem equivalente no Decidim (código exclusivo do Participa), por pasta:

| Pasta | Arquivos |
|---|---:|
| `decidim-govbr/packs` | 41 |
| `decidim-chatbot/lib` | 35 |
| `config` | 29 |
| `decidim-chatbot/views` | 27 |
| `decidim-govbr/lib` | 27 |
| `decidim-govbr/cells` | 15 |
| `decidim-govbr/views` | 13 |
| `decidim-govbr/overrides` | 10 |
| `decidim-chatbot/controllers` | 8 |
| `lib` | 8 |
| `controllers` | 7 |
| `services` | 7 |
| `decidim-chatbot/commands` | 7 |
| `decidim-chatbot/services` | 7 |
| `cells` | 5 |
| `models` | 5 |
| `decidim-chatbot/models` | 5 |
| `decidim-chatbot/forms` | 4 |
| `decidim-chatbot/packs` | 4 |
| `decidim-chatbot/presenters` | 4 |
| `commands` | 3 |
| `helpers` | 3 |
| `permissions` | 3 |
| `views` | 3 |
| `decidim-govbr/controllers` | 3 |
| `channels` | 2 |
| `decidim-chatbot/helpers` | 2 |
| `decidim-govbr/commands` | 2 |
| `decidim-govbr/services` | 2 |
| `forms` | 1 |
| `mailers` | 1 |
| `packs` | 1 |
| `decidim-chatbot/jobs` | 1 |
| `decidim-chatbot/permissions` | 1 |
| `decidim-govbr/helpers` | 1 |
| `decidim-govbr/jobs` | 1 |
| `decidim-govbr/models` | 1 |
| `decidim-govbr/permissions` | 1 |
| `decidim-govbr/validators` | 1 |
