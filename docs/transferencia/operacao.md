# Operação e continuidade

## Rotinas

### Participa

| Rotina | Frequência | Como |
|--------|-----------|------|
| Troca automática de etapa | De hora em hora | `sidekiq-cron` (`PROCESS_STEP_AUTO_ACTIVATION_CRON`) |
| Tarefas periódicas do Decidim (resumos, lembretes, dados abertos, limpezas, inativos) | Diária ou semanal | **Não agendadas no repositório.** Agende as versões por organização da participa-gem (por exemplo, `decidim:reminders:all`, que dispara `decidim_apartment:reminders:all`) |
| Conferir a estrutura dos schemas | Antes de cada versão com migração | `bin/rails apartment:schema_drift` |
| Criar organização | Sob demanda | Painel `/system`, DNS, Ingress e certificado ([Implantação](../participa/implantacao.md#criar-uma-organizacao-no-cluster)) |
| Revisar filas | Contínua | Painel do Sidekiq |

### API OP-BP

| Rotina | Frequência | Como |
|--------|-----------|------|
| Reenviar tarefas presas | A cada 5 minutos | Cron externo com `api/scripts/recover-orphan-tasks.sh` |
| Reconciliar votos entre cache e banco | Após incidentes com o Valkey | Painel › Operação › Reconciliação |
| Repetir tarefas com falha | Contínua | Painel › Operação › Task logs |
| Anonimizar processos encerrados | Ao fim de cada processo, se aplicável | Painel › Processo › LGPD |
| Limpar backups de anonimização expirados | Diária | O ator existe, mas não é registrado pelo worker: ligue-o antes de depender da anonimização |

## Monitoramento recomendado

| Sinal | Participa | API OP-BP |
|-------|-----------|-----------|
| Disponibilidade | Probes TCP do Kubernetes na porta 3000 | `GET /health` (banco, Valkey, versão) |
| Métricas | Redis e CloudNativePG pelo Prometheus Operator | `/metrics` (Prometheus): links e callbacks gov.br, votos, workers, tempo por passo do roteiro |
| Desempenho | Pyroscope | OpenTelemetry com Jaeger |
| Filas | Painel do Sidekiq | Dramatiq Dashboard e tabela `task_logs` |
| Erros | Logs dos pods; PostHog recebe erros do Rails quando configurado | Logs JSON com `request_id` |

## Incidentes comuns

??? question "Uma organização do Participa responde com erro depois de uma versão"
    Rode `bin/rails apartment:schema_drift`. Se o schema dela estiver atrás do `public`, use `apartment:repair_plan[schema]` para ver quais migrações estão registradas sem ter sido aplicadas e rode-as de novo naquele schema.

??? question "Host novo do Participa abre a página errada ou erro 404"
    O host precisa estar em `apartment_distribution_keys` (criado pelo `/system`) e ter Ingress e certificado. Host desconhecido cai no schema `public`.

??? question "Assets do Participa não carregam depois de uma versão"
    Verifique o job `compile-assets-job` do Helm e o volume `assets`. O nginx ao lado do Puma serve `/decidim-packs` desse volume.

??? question "Votos da API OP-BP não aparecem no Brasil Participativo"
    Veja Painel › Operação › Task logs, filtrando `bp_register_votes`. Erros de chave são permanentes: confira se `BP_API_KEY` é igual ao `N8N_SECRET_KEY` do Brasil Participativo. Verifique também `register_votes_on_bp` no processo.

??? question "Participante volta do gov.br e a conversa não continua"
    Confira se o callback chegou (`POST /api/v1/identity/govbr/callback`), se `GOVBR_CALLBACK_API_KEY` confere e se o worker `process_govbr_auth` recebeu CPF e e-mail.

??? question "O WhatsApp parou de responder num processo"
    Confira as credenciais do processo (aba WhatsApp), o provedor declarado em `channel_providers`, o período do processo e o registro do webhook no SERPRO.

## Backup e recuperação

| Projeto | Situação | Recomendação |
|---------|----------|--------------|
| Participa | O backup do CloudNativePG em S3 (barman) e o `ScheduledBackup` estão só como TODO no chart | Configurar backup contínuo e testar restauração de **todos os schemas** juntos |
| Participa (arquivos) | S3/MinIO, uma pasta por organização | Versionamento ou réplica do bucket |
| API OP-BP | Nenhuma rotina no repositório | `pg_dump` agendado; o broker Valkey usa AOF |

!!! warning "Backups contêm dados pessoais"
    Os dois bancos guardam CPF (cifrado ou em hash), nomes, e-mails e telefones. Cifre os backups e restrinja o acesso.

## Continuidade

- Os dois projetos dependem de poucas pessoas: o fator de ausência é 2 no Participa e 1 na participação multicanal ([Estatísticas](../estatisticas/index.md)).
- Partes da implantação de produção estão fora dos repositórios analisados. Recuperar esses manifestos é condição para a operação autônoma.
