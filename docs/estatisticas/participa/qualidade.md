---
title: "Qualidade e Boas Práticas: Participa"
---

<!-- Gerado por scripts/estatisticas.py em 2026-10-10T19:18:25+00:00. Não edite à mão. -->

# Qualidade e Boas Práticas: Participa

!!! info "Coleta de 10/10/2026"
    Branches `main` e `develop` do [participa](https://gitlab.com/lappis-unb/decidimbr/participa) e API pública do GitLab. Série a partir de 01/05/2025, mês do primeiro commit. "Últimos 12 meses" = 10/10/2025 a 10/10/2026. Para atualizar, rode `python3 scripts/estatisticas.py --projeto participa`.


Indicadores de saúde de projeto de software livre, inspirados nas métricas da [CHAOSS](https://chaoss.community/) e nos critérios do [selo de boas práticas da OpenSSF](https://www.bestpractices.dev/pt-BR/criteria/0).

## Indicadores

|  | Indicador | Valor |
| --- | --- | --- |
| :yellow_circle: | Fator de ausência (pessoas que somam 50% dos commits) | 2 |
| :green_circle: | Contribuidores ativos | 16 |
| :green_circle: | Sucesso de pipelines na `develop` | 100% |
| :green_circle: | Mediana de tempo até o merge | 1,1 dias |
| :red_circle: | MRs com ao menos um comentário | 15% |
| :red_circle: | MRs integrados pelo próprio autor | 44% |
| :white_circle: | Mediana de tempo para fechar issues | — |
| :green_circle: | Commits no padrão Conventional Commits | 83% |
| :yellow_circle: | Issues abertas há mais de 1 ano | 22% |
| :green_circle: | Versões estáveis publicadas | 6 |
| :green_circle: | Ruby com suporte | 3.4.7 (fim do suporte: 31/03/2028) |
| :green_circle: | Rails com suporte | 8.1.4 (fim do suporte: 10/10/2027) |
| :green_circle: | Defasagem do Decidim (versões menores) | 0.32.1 → 0.32.1 (0 atrás) |

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
| Ruby e Rails | com suporte | — | sem suporte |
| Defasagem do Decidim | versão atual | 1 a 2 versões menores | 3 ou mais |

## Integração contínua

| Job | Estágio | Bloqueia o pipeline? |
| --- | --- | --- |
| `gitleaks-scan` | `security` | Não (`allow_failure`) |
| `hadolint-scan` | `security` | Não (`allow_failure`) |
| `brakeman-scan` | `security` | Não (`allow_failure`) |
| `sca-scan` | `security` | Não (`allow_failure`) |
| `consolidate-reports` | `reports` | Sim |
| `build_dev_image` | `build_dev_image` | Sim |
| `build_bump_image` | `build_bump_image` | Sim |
| `build_prod_image` | `build_prod_image` | Sim |
| `release` | `release` | Sim |

### Pipelines nos últimos 12 meses

| Branch | Pipelines | Sucesso | Falha | Cancelados | Outros | Taxa de sucesso |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `develop` | 1 | 1 | 0 | 0 | 0 | 100% |
| `main` | 104 | 101 | 1 | 2 | 0 | 99% |
| todas as branches | 497 | 478 | 14 | 5 | 0 | 97% |

Taxa de sucesso = sucesso ÷ (sucesso + falha). Jobs com `allow_failure` não derrubam o pipeline.

## Testes e análise estática

| Item | Valor |
| --- | ---: |
| Arquivos Ruby em `app/` (aplicação e engines) | 96 |
| Arquivos de teste RSpec (`*_spec.rb`) | 107 |
| Arquivos de teste Minitest (`test/`) | 2 |
| Regras RuboCop desativadas em `.rubocop_todo.yml` | 0 |
| Ocorrências pendentes no `.rubocop_todo.yml` | 0 |
| Arquivos de teste por arquivo de código | 1,14 |
| Cobertura publicada no CI | Não (SimpleCov instalado, sem relatório no CI) |

## Dependências e plataforma

| Item | Versão em uso | Situação |
| --- | --- | --- |
| Ruby | 3.4.7 | fim do suporte em 31/03/2028; ciclo atual 4.0 |
| Rails | 8.1.4 | fim do suporte em 10/10/2027; ciclo atual 8.1 |
| Decidim | 0.32.1 | versão mais recente: 0.32.1 |
| Lockfiles | `Gemfile.lock`, `package-lock.json` | Versões de dependências travadas |

### Gems instaladas direto de repositórios git

Gems apontadas para uma branch mudam a cada `bundle update`. A versão efetiva fica só no `Gemfile.lock`.

| Gem | Branch | Tag ou commit fixo? |
| --- | --- | --- |
| `omniauth-govbr` | `main` | :x: |

## Checklist de boas práticas

|  | Prática | Observação |
| --- | --- | --- |
| :white_check_mark: | Licença de software livre | O nome do arquivo não é o padrão (`LICENSE`), por isso o GitLab pode não detectar a licença |
| :white_check_mark: | README na raiz |  |
| :white_check_mark: | Guia de contribuição |  |
| :white_check_mark: | Código de conduta |  |
| :x: | Política de segurança (`SECURITY.md`) | Sem canal documentado para relatar vulnerabilidades |
| :x: | Registro de mudanças (`CHANGELOG`) | 7 tags, sem notas de versão |
| :x: | Template de merge request |  |
| :x: | Template de issue |  |
| :x: | Lint de código no CI |  |
| :x: | Testes automatizados no CI |  |
| :white_check_mark: | Análise estática de segurança (SAST) | Não bloqueia o pipeline |
| :white_check_mark: | Análise de dependências (SCA) | Não bloqueia o pipeline |
| :white_check_mark: | Varredura de segredos |  |
| :white_check_mark: | Sem relatórios gerados versionados |  |

## Limitações

- **Diversidade de organizações** (*Elephant Factor*, CHAOSS) não é calculada: quase todos os commits usam e-mails pessoais, que não indicam a instituição.
- **Revisão de código** é estimada pelo número de comentários do MR, que inclui comentários do próprio autor. Aprovações não estão disponíveis sem autenticação.
- **Issues confidenciais** não aparecem na API pública.
- **Razão entre arquivos de teste e de código** é só um indicativo; não mede cobertura.

