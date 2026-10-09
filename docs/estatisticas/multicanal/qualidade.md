---
title: "Qualidade e Boas Práticas: Participação multicanal"
---

<!-- Gerado por scripts/estatisticas.py em 2026-10-08T14:14:52+00:00. Não edite à mão. -->

# Qualidade e Boas Práticas: Participação multicanal

!!! info "Coleta de 08/10/2026"
    Branch `main` do [multi-channel-participation](https://gitlab.com/lappis-unb/decidimbr/multi-channel-participation) e API pública do GitLab. Série a partir de 01/03/2026, mês do primeiro commit. "Últimos 12 meses" = 08/10/2025 a 08/10/2026. Para atualizar, rode `python3 scripts/estatisticas.py --projeto multicanal`.


Indicadores de saúde de projeto de software livre, inspirados nas métricas da [CHAOSS](https://chaoss.community/) e nos critérios do [selo de boas práticas da OpenSSF](https://www.bestpractices.dev/pt-BR/criteria/0).

## Indicadores

|  | Indicador | Valor |
| --- | --- | --- |
| :red_circle: | Fator de ausência (pessoas que somam 50% dos commits) | 1 |
| :red_circle: | Contribuidores ativos | 3 |
| :yellow_circle: | Sucesso de pipelines na `main` | 70% |
| :green_circle: | Mediana de tempo até o merge | 0 h |
| :red_circle: | MRs com ao menos um comentário | 0% |
| :red_circle: | MRs integrados pelo próprio autor | 56% |
| :white_circle: | Mediana de tempo para fechar issues | — |
| :green_circle: | Commits no padrão Conventional Commits | 99% |
| :green_circle: | Issues abertas há mais de 1 ano | 0% |
| :red_circle: | Versões estáveis publicadas | 0 |
| :green_circle: | Python com suporte | 3.14 (fim do suporte: 31/10/2030) |

### Como ler os indicadores

As faixas abaixo são referências adotadas nesta documentação para orientar a leitura. A CHAOSS define as métricas, mas não estabelece faixas.

| Indicador | :green_circle: | :yellow_circle: | :red_circle: |
| --- | --- | --- | --- |
| Fator de ausência | 4 ou mais | 2 a 3 | 1 |
| Contribuidores ativos (12 meses) | 10 ou mais | 5 a 9 | menos de 5 |
| Sucesso de pipelines | 90% ou mais | 70% a 89% | menos de 70% |
| Mediana até o merge | até 3 dias | até 10 dias | mais de 10 dias |
| MRs com comentário | 70% ou mais | 40% a 69% | menos de 40% |
| MRs integrados pelo autor | até 10% | até 30% | mais de 30% |
| Mediana para fechar issues | até 30 dias | até 90 dias | mais de 90 dias |
| Conventional Commits | 80% ou mais | 50% a 79% | menos de 50% |
| Issues abertas há mais de 1 ano | até 20% | até 50% | mais de 50% |
| Versões estáveis em 12 meses | 4 ou mais | 1 a 3 | nenhuma |
| Python e Node.js | com suporte | — | sem suporte |

## Integração contínua

| Job | Estágio | Bloqueia o pipeline? |
| --- | --- | --- |
| `api:ruff-lint` | `quality` | Sim |
| `api:ruff-format` | `quality` | Sim |
| `api:mypy` | `quality` | Sim |
| `api:bandit` | `security` | Sim |
| `api:pip-audit` | `security` | Não (`allow_failure`) |
| `api:trivy` | `security` | Sim |
| `gitleaks` | `security` | Sim |
| `api:semgrep` | `security` | Não (`allow_failure`) |
| `api:pytest` | `test` | Sim |
| `api:build` | `build` | Sim |

### Pipelines nos últimos 12 meses

| Branch | Pipelines | Sucesso | Falha | Cancelados | Outros | Taxa de sucesso |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `main` | 47 | 33 | 14 | 0 | 0 | 70% |
| todas as branches | 61 | 38 | 23 | 0 | 0 | 62% |

Taxa de sucesso = sucesso ÷ (sucesso + falha). Jobs com `allow_failure` não derrubam o pipeline.

## Testes e análise estática

| Item | Valor |
| --- | ---: |
| Arquivos Python em `api/app/` | 163 |
| Arquivos de teste pytest (`api/tests/`) | 117 |
| Arquivos TypeScript em `front/apps/*/src/` | 103 |
| Arquivos de teste do front-end (`*.test.ts`, `*.spec.ts`) | 1 |
| Ferramentas de análise configuradas no `pyproject.toml` | Ruff, mypy, Bandit, pip-audit |
| Arquivos de teste por arquivo de código | 0,44 |
| Cobertura publicada no CI | Sim (pytest-cov) |

## Dependências e plataforma

| Item | Versão em uso | Situação |
| --- | --- | --- |
| Python | 3.14 (exige >=3.13) | fim do suporte em 31/10/2030; ciclo atual 3.14 |
| FastAPI | 0.137.1 | versão mais recente: 0.143.0 |
| Lockfiles | `api/uv.lock`, `front/pnpm-lock.yaml` | Versões de dependências travadas |

## Checklist de boas práticas

|  | Prática | Observação |
| --- | --- | --- |
| :x: | Licença de software livre | Sem arquivo de licença no repositório |
| :x: | README na raiz | Só em subpastas: `api/README.md`, `front/README.md` |
| :x: | Guia de contribuição |  |
| :x: | Código de conduta |  |
| :x: | Política de segurança (`SECURITY.md`) | Sem canal documentado para relatar vulnerabilidades |
| :x: | Registro de mudanças (`CHANGELOG`) | 0 tags, sem notas de versão |
| :x: | Template de merge request |  |
| :x: | Template de issue |  |
| :white_check_mark: | Lint de código no CI |  |
| :white_check_mark: | Testes automatizados no CI |  |
| :white_check_mark: | Análise estática de segurança (SAST) |  |
| :white_check_mark: | Análise de dependências (SCA) |  |
| :white_check_mark: | Varredura de segredos |  |
| :white_check_mark: | Sem relatórios gerados versionados |  |

## Limitações

- **Diversidade de organizações** (*Elephant Factor*, CHAOSS) não é calculada: quase todos os commits usam e-mails pessoais, que não indicam a instituição.
- **Revisão de código** é estimada pelo número de comentários do MR, que inclui comentários do próprio autor. Aprovações não estão disponíveis sem autenticação.
- **Issues confidenciais** não aparecem na API pública.
- **Razão entre arquivos de teste e de código** é só um indicativo; não mede cobertura.

