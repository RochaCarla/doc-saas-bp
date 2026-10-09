# Novidades

Mudanças recentes nos dois projetos, a partir do histórico das branches `main`.

## Participa

### Outubro de 2026

- **Chatbot de WhatsApp** integrado à `main` (merge `9253a99`): votação em propostas com identificação por CPF e nome ou gov.br, painel com visão geral, provedores e textos do roteiro. [Chatbot](participa/chatbot.md)
- **Versão "0.32.1 v1.0.2"** (sem tag): troca automática de etapa com `sidekiq-cron`, URLs absolutas de imagens nos e-mails, `CONTRIBUTING.md` e código de conduta.
- **Página global de notícias** e seletor de post em destaque na página inicial.

### Setembro de 2026

- **Atualização para o Decidim 0.32.1**, com Rails 8.1 e Ruby 3.4.7 (`0.32.1-v1.0.0`).
- **`0.32.1-v1.0.1`**: eleições, participação efêmera, abas de configuração da organização, blocos extras de página inicial, mapas HERE e OSM, PostHog.
- **Layout gov.br por host** (`GOVBR_LAYOUT_HOSTS`) e cores da organização com padrão do Design System gov.br.
- **Comentários**: edição limitada a 5 minutos e respostas oficiais.

### Junho a agosto de 2026

- Módulos do Brasil Participativo como gems: formulários, regras por etapa em propostas e reuniões, categorias, órgãos e setores.
- Iniciativas e conferências instaladas.
- Pyroscope para análise de desempenho.

## Participação multicanal

### Setembro de 2026

- **Concierge do Brasil Participativo**: lista de processos abertos pelo GraphQL do Decidim, destaques e busca por texto. [Integração](multicanal/integracao.md#catalogo-de-processos)
- Envio do id numérico do usuário gov.br na impersonação e ajuste de TLS para o host do Brasil Participativo.

### Julho e agosto de 2026

- Opção por processo para permitir o comando de reinício em produção. [Roteiros](multicanal/roteiros.md#comando-de-reinicio-para-testes)
- Configuração do catálogo de processos por processo.

### Junho de 2026

- **Painel**: dados por processo, editor visual de roteiros com grafo e simulador, versões, tempo por passo.
- **Alteração de voto** por processo e provedor de canal por processo.
- Credenciais do WhatsApp do SERPRO por processo.

## Esta documentação

- Primeira versão, em outubro de 2026, com o Participa, a participação multicanal, a Transferência, a Inovação e as Estatísticas dos dois projetos.
