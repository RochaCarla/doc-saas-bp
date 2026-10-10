# Funcionalidades da participação multicanal

Catálogo de tudo o que a API OP-BP, o painel administrativo e o app de participação implementam na branch `main` (commit `cad204d`, 14 de setembro de 2026). A coluna **Desde** traz a data do commit `feat` correspondente. "Versão inicial" indica o que veio no primeiro commit da `main` (17 de março de 2026), que importou o projeto já pronto.

## Canais

| Funcionalidade | O que faz | Onde | Desde |
|----------------|-----------|------|-------|
| WhatsApp Flows | Formulário de várias telas no WhatsApp, com payload cifrado, para votar no Orçamento do Povo ([Canais](../multicanal/canais.md#whatsapp-flows)) | `api/app/whatsapp_flows/` | versão inicial |
| WhatsApp do SERPRO | Recebe e envia texto, botões, lista e botão com link pela API do SERPRO | `api/app/services/channel_providers/whatsapp_serpro.py`, `api/app/integrations/whatsapp_serpro_client.py` | mai. 2026 |
| Telegram | Bot de texto com mensagens e cliques em botões | `api/app/services/channel_providers/telegram.py` | mai. 2026 |
| Webhook único por provedor | `/api/v1/conversations/{provedor}/webhook` no lugar de rotas fixas por canal | `api/app/routes/conversations.py` | mai. 2026 |
| Uma bolha por resposta | Cada resposta do roteiro vira uma mensagem, enviada em ordem | `api/app/routes/conversations.py` | mai. 2026 |
| Descarte de repetidas e limite por participante | Eventos repetidos descartados por 24 h; até 20 mensagens por minuto por identificador | `api/app/routes/conversations.py`, `api/app/core/constants.py` | mai. 2026 |
| Provedor por processo | Cada processo declara o provedor de cada canal; WhatsApp Flows e SERPRO não atendem o mesmo processo | `api/app/services/provider_gate.py` | jun. 2026 |
| Credenciais do WhatsApp por processo | `client_id`, segredo (cifrado) e número de origem por processo, com valores globais como reserva | `process_whatsapp_serpro_config` | jun. 2026 |
| Token OAuth por cliente | Cache do token do SERPRO separado por `client_id`, para isolar processos | `api/app/integrations/whatsapp_serpro_client.py` | jun. 2026 |
| Registro do webhook no SERPRO | Registrar e ativar o webhook do processo pelo painel, de forma idempotente | `api/app/services/process_webhook_service.py` | mai. a jun. 2026 |
| Voltar ao canal | Botão "Voltar para o WhatsApp/Telegram" depois do login gov.br, por processo | `channel_return_urls` | jun. 2026 |
| App de participação | Votação como Telegram Mini App ou página web, com adaptadores por plataforma | `front/apps/participation/` | mar. 2026 |

## Roteiros de conversa

| Funcionalidade | O que faz | Onde | Desde |
|----------------|-----------|------|-------|
| Motor de roteiros em YAML | Carregador com validação, verificador de condições, executor de ações e modelos Jinja2 ([Roteiros](../multicanal/roteiros.md)) | `api/scripts/flow_engine.py` | mai. 2026 |
| Orquestrador de conversa | Uma rodada do roteiro por mensagem, sessão no Valkey e eventos de negócio fora do motor | `api/app/services/conversation_orchestrator.py`, `business_event_handler.py` | mai. 2026 |
| Coleções no próprio YAML | Menus e listas declarados no roteiro, sem depender de código | `flow_engine.py` | mai. 2026 |
| Predicado `se` | Condições booleanas sobre a sessão em botões e transições | `flow_engine.py` | jun. 2026 |
| Ações de dados | `carregar_propostas`, `votar`, `criar_proposta` | `flow_engine.py` | mai. 2026 |
| Ranking preliminar | `carregar_ranking` com os votos reais, em cache de 15 s | `api/app/repositories/` | mai. 2026 |
| Link gov.br no roteiro | Ação `gerar_link_govbr` | `flow_engine.py` | jun. 2026 |
| Alterar voto no roteiro | Botão e caminho de troca de voto | `flow_engine.py`, `vila-carioca.yml` | jun. 2026 |
| Processos abertos no roteiro | `carregar_processos` e `buscar_processos` para o concierge | `flow_engine.py` | ago. a set. 2026 |
| Roteiros no banco | Cadastro de roteiros validados pelo motor; troca sem reinício | `conversation_scripts` | mai. 2026 |
| Versões de roteiro | Publicação em versões imutáveis e restauração | `conversation_script_versions` | jun. 2026 |
| Tempo por passo | Registro das transições e painel de tempo por passo do roteiro | `flow_step_events` | jun. 2026 |
| Comando de reinício por processo | Comando de depuração liberado em produção só com a opção do processo | `process_settings.allow_reset_command` | jul. 2026 |

### Roteiros prontos

| Roteiro | O que faz | Desde |
|---------|-----------|-------|
| Vila Carioca | Consulta de bairro: tema prioritário, login gov.br, ranking, compartilhamento, "saber mais", recomeçar e troca de voto | mai. a jul. 2026 |
| Concierge do Brasil Participativo | Saudação, dúvidas frequentes, processos abertos pelo GraphQL do Decidim, destaques, total de processos e busca por texto | ago. a set. 2026 |
| Consulta com votação | Carrega as propostas reais do processo e registra o voto | mai. 2026 |

## Votação e propostas

| Funcionalidade | O que faz | Onde | Desde |
|----------------|-----------|------|-------|
| Votação assíncrona | Envio responde 202 com `tracking_id`; votos gravados por worker | `api/app/routes/votes.py` | versão inicial |
| Limite de votos | Até 3 propostas por participante e processo (configurável) | `process_settings` | versão inicial |
| Sem voto duplo | Marca no Valkey por 90 dias que falha fechada | `api/app/services/vote_submit_service.py` | versão inicial |
| Municípios e CEP | Busca de município por nome, código IBGE ou CEP (ViaCEP com BrasilAPI de reserva) | `api/app/integrations/cep_client.py` | versão inicial; por processo em mai. 2026 |
| Propostas por processo | Fonte das propostas por processo: banco ou JSON, com cache | `api/app/services/proposals/` | mai. 2026 |
| Cadastro e importação de propostas | Criar, editar, excluir e importar em lote pelo painel | `api/app/routes/admin.py` | mai. 2026 |
| Etiquetas em propostas | Filtro de propostas por etiquetas (JSONB) | `proposals.tags` | mai. 2026 |
| Propostas sem dados pessoais | Propostas de vários processos com dados pessoais removidos | `api/app/services/proposals/` | jun. 2026 |
| Listas dinâmicas no WhatsApp | Lista de propostas votáveis com ids e corpo; propostas já votadas travadas | `api/app/services/` | jun. 2026 |
| Troca de voto só na API | Por processo; o registro no Brasil Participativo não muda | `process_settings.allow_vote_change` | jun. 2026 |
| Registro opcional no Brasil Participativo | Por processo, o voto pode ficar só na API | `process_settings.register_votes_on_bp` | jun. 2026 |
| Proposta enviada pelo canal | O participante cria uma proposta na conversa | ação `criar_proposta` | mai. 2026 |

## Identificação

| Funcionalidade | O que faz | Onde | Desde |
|----------------|-----------|------|-------|
| Identificação progressiva | Anônimo, identificado por CPF e autenticado pelo gov.br ([Votação e identificação](../multicanal/votacao.md)) | `api/app/workers/tasks/vote_identify.py` | versão inicial |
| Consulta CPF | Confere situação, nascimento, nome e idade mínima no SERPRO | `api/app/integrations/serpro_client.py` | versão inicial |
| Proteções da validação de CPF | Limites de tentativa, bloqueio, cache da resposta (desde mar. 2026), tempo mínimo de resposta e token de uso único | `api/app/services/cpf_validate_service.py` | versão inicial |
| Login gov.br pelo Brasil Participativo | Link de login externo assinado e retorno com CPF, nome e e-mail | `api/app/services/govbr_identity_service.py` | versão inicial |
| Retorno idempotente | Callback repetido só reenvia a mensagem de compartilhamento | `govbr_identity_service.py` | jun. 2026 |
| Canal e volta no token | O link gov.br leva o canal e o endereço de volta | `govbr_identity_service.py` | jun. 2026 |
| Callback só em HTTPS em produção | Validação da configuração | `api/app/config.py` | jun. 2026 |
| Mensagem pós-login | Push pelo WhatsApp com sucesso, ranking e botões de compartilhar ou encerrar | `api/app/services/post_auth_notification.py` | jun. 2026 |
| Uma pessoa por CPF | Reaproveita a pessoa pelo hash do CPF ao autenticar | `api/app/workers/tasks/govbr_auth_callback.py` | jun. 2026 |
| Id numérico na impersonação | Envia o id numérico da conta gov.br no Decidim | `api/app/integrations/bp_client.py` | set. 2026 |

## Integração com o Decidim

| Funcionalidade | O que faz | Onde | Desde |
|----------------|-----------|------|-------|
| Usuário efêmero e voto no Brasil Participativo | `ephemeral.create(cpf)` e `voteProposal` com impersonação, em lote | `api/app/integrations/bp_client.py` | versão inicial |
| Catálogo de processos por GraphQL | Processos abertos de qualquer Decidim entre 0.27 e 0.32, com fuso, ordenação, destaques e busca | `api/app/integrations/processes_catalog_client.py` | ago. a set. 2026 |
| Catálogo por processo | Cada processo aponta para a instalação Decidim do seu catálogo | `process_catalog_config` | ago. 2026 |
| TLS compatível com o Brasil Participativo | Suítes RSA readmitidas para o host do Decidim 0.27 | `api/app/core/http_client.py` | set. 2026 |

## Painel administrativo

| Funcionalidade | O que faz | Onde | Desde |
|----------------|-----------|------|-------|
| Painel em Vite | Painel reescrito como SPA Vite + React, com cadastro de processos | `front/apps/admin/` | jun. 2026 |
| Kit de interface | Botões, campos, seleção, menus, dicas, avisos e página de demonstração | `front/apps/admin/src/` | jun. 2026 |
| Processo em abas | Visão geral, resumo, configurações, propostas, participantes, votos, roteiro e LGPD ([Painel](../multicanal/painel.md)) | `routes/ProcessDetail.tsx` | jun. 2026 |
| Estatísticas por processo | Painel de participação e contagem de votos por tipo, com cache | `/api/v1/admin/stats`, `/votes/stats` | jun. 2026 |
| Participantes por processo | Lista e detalhe, com CPF mascarado | `/api/v1/admin/participants` | jun. 2026 |
| Editor visual de roteiros | Grafo, simulador e editores de estado, mensagem, condição e ação; três visões e versões | `routes/flow/` | jun. 2026 |
| Navegação | Barra lateral recolhível, trilha de navegação e nome BPAPI | `front/apps/admin/` | jun. 2026 |
| Operação | Task logs com nova tentativa, reconciliação de votos e saúde do sistema | `routes/Operations.tsx` | versão inicial e jun. 2026 |
| Acesso ao painel | Chave de administrador ou token JWT revogável | `api/app/core/admin_auth.py`, `admin_jwt.py` | versão inicial |

## LGPD e segurança

| Funcionalidade | O que faz | Onde | Desde |
|----------------|-----------|------|-------|
| CPF cifrado | Fernet com rotação de chave; hash para busca; máscara nas auditorias | `api/app/validators/cpf_validator.py` | mar. 2026 |
| Anonimização | Por processo, em duas etapas, com prova de participação e reversão por 7 dias | `api/app/services/anonymization_service.py` | mar. 2026 |
| Segredos por processo cifrados | Cifra Fernet genérica para credenciais de WhatsApp e catálogo | `api/app/core/secret_cipher.py` | jun. 2026 |
| Validações de produção | A API não inicia em produção sem os segredos e verificações obrigatórios | `api/app/config.py` | versão inicial |
| Filtro de dados sensíveis nos logs | CPF, tokens e senhas mascarados | `api/app/core/logging_config.py` | versão inicial |
| Cabeçalhos de segurança | CSP, `X-Frame-Options`, `no-store` e HSTS em produção | `api/app/main.py` | versão inicial |
| Análises no CI | Ruff, mypy, Bandit, pip-audit, Trivy, Gitleaks e Semgrep | `.gitlab-ci.yml` | versão inicial |

## Operação e escala

| Funcionalidade | O que faz | Onde | Desde |
|----------------|-----------|------|-------|
| Filas com prioridade | Quatro filas Dramatiq, de `critical` a `low-priority` | `api/app/workers/` | versão inicial |
| Nenhuma tarefa perdida | Registro da tarefa antes do envio à fila e reenvio de tarefas presas | `api/app/services/task_dispatch.py`, `workers/tasks/recovery.py` | versão inicial |
| Reconciliação de votos | Corrige divergências entre cache e banco | `workers/tasks/` | versão inicial |
| Circuit breakers | Para SERPRO, WhatsApp e catálogo | `api/app/core/circuit_breaker.py` | versão inicial |
| Cache e filas separados | Dois Valkey, um sem persistência e outro com AOF | `api/docker-compose.yml` | mar. 2026 |
| PgBouncer | Agrupamento de conexões em modo transação | `api/docker-compose.yml` | versão inicial |
| Métricas e rastreamento | Prometheus e OpenTelemetry com Jaeger | `api/app/core/metrics.py`, `tracing.py` | mar. 2026 |
| Versão no `/health` | Versão, commit e data do build | `api/app/routes/health.py` | jun. 2026 |
| Logs silenciosos de saúde | Acesso a `/health` e `/metrics` fora dos logs | `api/app/core/logging_config.py` | jun. 2026 |
| Testes de carga | Cenários k6 para chats, gov.br e votos | `api/tests/load_tests/` | mar. 2026 |
| Dados de demonstração | Seed com dados realistas e da Vila Carioca | `api/scripts/` | mar. e mai. 2026 |
| Limites desligáveis | `RATE_LIMIT_ENABLED` para testes de carga | `api/app/config.py` | abr. 2026 |
| Simulação do CI | `scripts/ci-check.sh` roda os estágios localmente, inclusive verificações do front-end | `scripts/ci-check.sh` | mar. 2026 |

Fontes: commits `feat` da `main` (`git log main`), código da `main` e `api/tests/load_tests/results/REPORT.md`.
