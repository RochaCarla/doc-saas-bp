# Testes e qualidade

## Suítes

| Projeto | Suíte | Arquivos | Ferramentas |
|---------|-------|---------:|-------------|
| Participa | Aplicação (`spec/`) | 23 | RSpec, FactoryBot, factories do Decidim |
| Participa | Chatbot (`decidim-chatbot/spec/`) | 61 | RSpec, WebMock, Wisper |
| Participa | Engine gov.br (`decidim-govbr/spec/`) | 23 | RSpec, aplicação de teste própria |
| API OP-BP | `api/tests/` | 117 | pytest, pytest-asyncio, pytest-cov; cerca de 1.200 funções de teste |
| API OP-BP | `api/tests/e2e/` | 7 | Fluxos anônimo, CPF, gov.br e erros contra uma API real |
| API OP-BP | `api/tests/load_tests/` | — | k6: chats, link e callback gov.br, votos |
| Painel | `front/apps/admin` | 1 | Vitest |

Comandos em [Participa › Desenvolvimento](../participa/desenvolvimento.md#testes) e [Participação multicanal › Implantação](../multicanal/implantacao.md#ambiente-local).

## Integração contínua

| Verificação | Participa | API OP-BP |
|-------------|-----------|-----------|
| Testes | :x: não rodam | :white_check_mark: `api:pytest`, com cobertura |
| Lint | :x: não roda | :white_check_mark: Ruff (lint e formato), mypy |
| Segredos | Gitleaks (não bloqueia) | Gitleaks (bloqueia) |
| Análise estática de segurança | Brakeman (não bloqueia) | Bandit (bloqueia), Semgrep (não bloqueia) |
| Dependências | Syft + Grype (não bloqueia) | pip-audit (não bloqueia), Trivy (bloqueia) |
| Dockerfile | Hadolint (não bloqueia) | — |
| Front-end | — | :x: nenhum job (o `scripts/ci-check.sh` local tem) |

Indicadores detalhados em [Estatísticas](../estatisticas/index.md).

## Regras para a equipe

- Todo merge request com mudança de comportamento traz teste.
- No Participa, rode as três suítes localmente até que o CI as rode.
- Nos roteiros de conversa, teste no simulador do painel antes de publicar.
- Mudanças de banco no Participa: confira `apartment:schema_drift` num ambiente com mais de uma organização.

## Lacunas

1. **Participa sem testes no CI.** Primeira melhoria a fazer: incluir RSpec e RuboCop no pipeline, com PostgreSQL e Redis como serviços.
2. **Multi-organização sem teste de ponta a ponta.** Não há teste que crie duas organizações e verifique o isolamento.
3. **Front-ends da participação multicanal quase sem testes** e sem CI.
4. **Testes de carga só da API OP-BP.** O Participa não tem medição de capacidade publicada.
