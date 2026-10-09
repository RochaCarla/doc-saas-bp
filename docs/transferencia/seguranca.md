# Segurança e LGPD

## Riscos conhecidos

!!! warning "Pendências em canal restrito"
    A leitura do código para esta documentação encontrou pendências de segurança nos dois projetos. Os detalhes estão em **issues confidenciais** nos repositórios do GitLab, e não nesta página, até que sejam corrigidas ou avaliadas (decisão registrada em `docs/adr/0001` deste repositório). A equipe receptora deve pedir acesso a essas issues na fase de preparação.

Riscos que podem ser discutidos publicamente:

| Risco | Projeto | Recomendação |
|-------|---------|--------------|
| Testes e lint não rodam no CI; os jobs de segurança não bloqueiam | Participa | Incluir RSpec e RuboCop no CI e tornar bloqueantes as análises de severidade alta |
| Gems instaladas por branch, uma delas em repositório pessoal | Participa | Fixar tags ou commits e migrar `omniauth-govbr` para um grupo institucional |
| Configuração dependente de credenciais cifradas não revisadas | Participa | Revisar o conteúdo das credenciais com a equipe atual ([Configuração](../participa/configuracao.md)) |
| Identificação efêmera sem prova de posse do CPF | Participa | Avaliar, por processo, se CPF e nome bastam para o risco da participação |
| Sem arquivo de licença, política de segurança ou versões publicadas | Participação multicanal | Definir licença, `SECURITY.md` e numeração de versões |
| Segredos compartilhados com o Brasil Participativo | Participação multicanal | Rotacionar em conjunto e documentar o procedimento ([Integração](../multicanal/integracao.md#segredos-compartilhados-com-o-decidim)) |
| Sem rotina de retenção de dados pessoais | Participação multicanal | Definir prazos com a SNPS e implementar o expurgo |

## Controles existentes

### Participa

| Controle | Como |
|----------|------|
| Isolamento entre organizações | Schema PostgreSQL por organização; cache Redis, arquivos e jobs separados por organização |
| Login gov.br | OAuth2/OpenID Connect com PKCE; formulário falso só em desenvolvimento |
| Limites de requisição | Rack::Attack do Decidim; limites por telefone no chatbot |
| Senha de administradores | Forte, com 15 caracteres ou mais e expiração em 90 dias |
| Logs | Parâmetros filtrados incluem senhas, tokens, CPF, `document_number` e o conteúdo dos webhooks; logs do chatbot sem telefones e mensagens |
| Segredos | Credenciais Rails cifradas no repositório, chaves fora do Git; segredos do chatbot cifrados no banco |
| Webhook do chatbot | Basic Auth por token, comparado em tempo constante; links de identificação de uso único, válidos por 1 hora |
| Análises no CI | Gitleaks, Hadolint, Brakeman, Syft e Grype |

### API OP-BP

| Controle | Como |
|----------|------|
| CPF | Cifrado (Fernet) em `users`, com rotação de chave; só hash e máscara nas tabelas de auditoria; sempre mascarado no painel |
| Validação de CPF | Limites de tentativa por participante e por CPF, token de uso único, tempo mínimo de resposta |
| Segredos por processo | Cifrados no banco e nunca devolvidos pela API |
| Acesso | Chave de API nas rotas REST; chave ou token revogável no painel |
| Webhooks | Segredo do Telegram e assinatura HMAC do WhatsApp; descarte de eventos repetidos |
| Validações de produção | A API não inicia em produção sem os segredos e as verificações obrigatórios ([Configuração](../multicanal/configuracao.md#validacoes-de-producao)) |
| Logs | JSON com filtro de CPF, tokens e senhas |
| Contêiner | Usuário sem privilégios; `no-new-privileges` e rede interna no Compose de produção |
| Análises no CI | Ruff, mypy, Bandit, pip-audit, Trivy, Gitleaks e Semgrep |
| Testes de invasão | Relatório parcial das rotas do painel (março de 2026), na branch `docs/security`; os achados parecem tratados na `main` |

## Gestão de vulnerabilidades

1. Relatos de vulnerabilidade entram como **issue confidencial** no repositório do projeto.
2. A correção segue o fluxo normal, sem detalhar o problema no título do merge request até a publicação.
3. Depois da correção em produção, o risco pode ser descrito nesta documentação.

O `CONTRIBUTING.md` do Participa indica um e-mail institucional para assuntos de segurança. A participação multicanal não tem canal declarado.

## Dados pessoais (LGPD)

### Inventário

| Dado | Participa | API OP-BP |
|------|-----------|-----------|
| CPF | Hash na verificação; coluna `document_number` em `decidim_users` | Cifrado em `users`; hash e máscara nas auditorias |
| Nome | Conta e participante efêmero | `users`, tentativas de validação de CPF |
| E-mail | Conta | `users` (após login gov.br) |
| Data de nascimento | — | `users`, tentativas de validação de CPF |
| Telefone ou id do Telegram | Conversas do chatbot | `chats`, `participants` |
| Mensagens trocadas | Eventos do chatbot (corpo de saída apagado após o envio) | `messages` |
| Votos | Votos em propostas | `votes`, com vínculo à pessoa até a anonimização |

### Tratamentos

- **Compartilhamento**: o Brasil Participativo envia CPF, nome e e-mail à API OP-BP no retorno do login gov.br; a API OP-BP envia o CPF ao SERPRO e ao Brasil Participativo.
- **Análise de uso**: o Participa pode carregar Matomo e PostHog. Revise a política de consentimento e a localização dos dados de cada ferramenta.
- **Anonimização**: só na API OP-BP, por processo e opcional; desfaz o vínculo entre voto e pessoa, mas mantém os dados da pessoa.
- **Retenção**: nenhum dos dois projetos tem rotina de expurgo de dados pessoais.

### Encarregado e bases legais

**A confirmar com a SNPS e com cada organização atendida**: quem é o controlador em cada organização do Participa, encarregado de dados, bases legais por finalidade, prazos de retenção e acordos com o SERPRO e a Meta.
