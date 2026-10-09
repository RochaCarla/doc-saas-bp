# Decisões de arquitetura

Decisões que explicam por que os sistemas são como são, reconstruídas do código, do histórico e da documentação dos repositórios. Cada uma traz a evidência. Ao final, as decisões que **ainda precisam ser tomadas**.

## ADR 1 · Nova base sobre o Decidim atual, em vez de evoluir o core

- **Contexto:** o core do Brasil Participativo está no Decidim 0.27.2, com 492 sobrescritas, e atende uma só organização.
- **Decisão:** criar o Participa do zero sobre o Decidim (0.29.1 em maio de 2025, depois 0.30 e 0.32.1) e trazer as customizações de novo.
- **Consequências:** plataforma atual e com poucas sobrescritas; nenhuma migração de dados prevista a partir do Brasil Participativo.
- **Evidência:** primeiro commit `331679f`; nenhum commit em comum com o `decidim-govbr`.

## ADR 2 · Um schema PostgreSQL por organização

- **Contexto:** oferecer a plataforma a muitas organizações sem uma instalação por organização.
- **Decisão:** `ros-apartment` integrado ao Decidim pela `decidim-apartment`, com um schema por organização e o host escolhendo o schema.
- **Consequências:** isolamento por schema; jobs, cache e arquivos precisam conhecer a organização; migrações rodam em todos os schemas; não há conversão de um Decidim tradicional.
- **Evidência:** merge `feat/one-decidim-one-db` (agosto de 2025); participa-gem.

## ADR 3 · Customizar por gems, `prepend` e Deface

- **Contexto:** o custo de atualização do core do Brasil Participativo vem das sobrescritas.
- **Decisão:** cada funcionalidade do Brasil Participativo vira uma gem; alterações pontuais usam `prepend` e Deface.
- **Consequências:** 31 sobrescritas no lugar de 492; 14 gems externas para manter e versionar.
- **Evidência:** `Gemfile`; [Customização do Decidim](../participa/customizacao.md).

## ADR 4 · Hierarquia própria de órgãos e setores

- **Contexto:** gestores de uma secretaria precisam ver só os processos dela.
- **Decisão:** gem `decidim-government_spaces` com Órgão → Setor e administradores com escopo, sem criar instâncias.
- **Evidência:** especificação na branch `feat/govspace`.

## ADR 5 · Participação efêmera por CPF e nome

- **Contexto:** reduzir a barreira de entrada para votar.
- **Decisão:** verificação efêmera por CPF e nome, transferida para a conta no login gov.br.
- **Consequências:** participação mais simples, sem prova de posse do CPF.
- **Evidência:** `decidim-ephemeral_participation`; `GovbrAuthorizationHandler`.

## ADR 6 · Implantação em Kubernetes com CloudNativePG

- **Decisão:** chart Helm com PostgreSQL gerenciado pelo CloudNativePG, Redis da Bitnami, migrações e assets por hooks.
- **Consequências:** criação de organizações e Ingress fora do chart de instância.
- **Evidência:** `deploy/decidim-instance-chart/`; commit `5879315`.

## ADR 7 · Participação por mensagens num serviço separado (API OP-BP)

- **Contexto:** o Orçamento do Povo previa milhões de participantes por WhatsApp.
- **Decisão:** um serviço em Python, com filas e cache próprios, que conduz a conversa e registra os votos no Brasil Participativo por GraphQL e impersonação.
- **Consequências:** escala independente do Decidim (testes de carga de até cerca de 1 milhão de participantes por dia, segundo o relatório do repositório); dependência do login externo e da impersonação do core.
- **Evidência:** `api/`; `api/tests/load_tests/results/REPORT.md`.

## ADR 8 · Roteiros de conversa em YAML editáveis

- **Decisão:** máquina de estados declarada em YAML, guardada no banco, versionada e editada pelo painel, com troca sem reinício.
- **Evidência:** `api/scripts/flow_engine.py`; `conversation_scripts`.

## ADR 9 · Identificação progressiva

- **Decisão:** votar anônimo e subir de nível (CPF conferido no SERPRO, depois gov.br), com o voto acompanhando o nível.
- **Evidência:** `api/app/workers/tasks/vote_identify.py`.

## ADR 10 · Chatbot dentro do Participa

- **Contexto:** organizações do Participa também querem votação por WhatsApp.
- **Decisão:** um módulo dentro do Participa, com roteiro fixo, que vota direto nas propostas.
- **Consequências:** duas soluções de WhatsApp com modelos diferentes.
- **Evidência:** `decidim-chatbot/`; merge `9253a99`.

## Decisões pendentes

| Decisão | Opções | Impacto |
|---------|--------|---------|
| **Uma ou duas soluções de WhatsApp** | Manter o chatbot no Participa e a API OP-BP no Brasil Participativo; ligar a API OP-BP ao Participa (exige login externo e impersonação no Participa); ficar só com uma | Equipe, custos de SERPRO e Meta, experiência do participante |
| **Futuro do Brasil Participativo** | Manter o core 0.27 e atualizá-lo; levar o Brasil Participativo para o Participa (sem conversão de dados pronta) | Maior item do roadmap |
| **Onde ficam os manifestos de produção** | Trazer para os repositórios; manter em `infra/decidim-saas` e documentar | Condição para a operação autônoma |
| **Licença da participação multicanal** | AGPLv3, como o Participa; outra | Condição para publicar como software livre |
| **Custódia das chaves de CPF** | Cofre de segredos do receptor | Perda torna dados ilegíveis |

## Como registrar novas decisões

Registre cada decisão nova como um ADR curto (contexto, decisão, consequências, evidência) e acrescente-a a esta página.
