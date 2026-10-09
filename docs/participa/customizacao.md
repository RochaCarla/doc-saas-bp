# Customização do Decidim

O Participa altera o Decidim de quatro formas. A escolha entre elas define quanto trabalho cada atualização do Decidim vai custar.

| Forma | Quantidade | Custo na atualização |
|-------|-----------:|----------------------|
| **Gem própria** (`decidim-bp_*`, `decidim-categories`, `decidim-government_spaces`…) | 14 gems | Atualizar e testar cada gem |
| **`prepend`** de módulo sobre uma classe do Decidim | 18 na aplicação, mais os das engines e gems | Revisar só os métodos alterados |
| **Deface** (troca de trecho de view) | 10, na engine `decidim-govbr` | Revisar os seletores quando a view muda |
| **Sobrescrita** de arquivo de mesmo caminho | 31 ([inventário](../transferencia/sobrescritas.md)) | Comparar o arquivo inteiro com a versão nova |

No Brasil Participativo (`decidim-govbr`, 0.27.2) eram 492 sobrescritas e 21 mil linhas diferentes do original. A mudança de estratégia é o principal ganho de manutenção do Participa ([Inovação](../inovacao/index.md)).

## Sobrescritas na aplicação

| Tipo | Arquivos |
|------|----------|
| Cells de orçamentos e comentários | Modal de informações do orçamento; formulário e edição de comentário |
| Views de orçamentos | Resumo do progresso do voto |
| Views de comentários e reuniões | Erro de atualização de comentário; pauta de reunião no painel |
| Layout e e-mail | `_head_extra` (scripts de análise), cabeçalho do painel, links do rodapé, boletim |
| JavaScript | Seletores de data e hora |

`app/packs/src/decidim/decidim_application.js` e os dois `decidim_application.scss` coincidem com arquivos do Decidim, mas são **pontos de extensão oficiais**, não sobrescritas.

## Módulos por `prepend`

Aplicados em `config/initializers/decidim_*_overrides.rb`:

| Área | O que mudam |
|------|-------------|
| Comentários | Quem edita e quando (5 minutos para autores comuns), papel administrativo no formulário, link do comentário denunciado |
| Moderação | Só papéis administrativos denunciam; mensagem correta quando a denúncia já ocultou o conteúdo |
| Orçamentos | Regras de conclusão do voto com mínimo de projetos ou orçamento zerado; correção da permissão de voto do 0.32.1 |
| Propostas | Imagem maior no card |
| Processos | Atualizar as datas do processo na tela de etapas |
| Autorizações | Transferir votos sem quebrar o índice único nem o limite de votos |
| E-mail | URLs absolutas de imagens (o 0.32 prefixa o idioma) |
| Reuniões | Aceita mais formatos de link do YouTube na incorporação |

Há ainda um `class_eval` em `ActiveStorage::BaseController` para trocar de organização ao servir arquivos (`config/initializers/active_storage_apartment_patch.rb`).

## Deface

A `config/application.rb` manda o Zeitwerk ignorar a pasta `app/overrides` de todas as engines, porque declarações Deface não definem constante e derrubavam o boot. Em produção, as views são pré-compiladas na imagem e o Deface fica desligado.

## Boas práticas para novas customizações

| Em vez de | Prefira |
|-----------|---------|
| Copiar uma view inteira | Deface sobre o trecho, ou um bloco de conteúdo |
| Sobrescrever uma classe | `prepend` só nos métodos alterados |
| Mudar comportamento na aplicação | Uma gem `decidim-*` própria, com testes |
| Manter a melhoria só no Participa | Contribuir com o Decidim, se servir a outras instalações |
