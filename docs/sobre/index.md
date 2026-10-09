# Sobre esta documentação

Esta documentação é resultado do trabalho do **Laboratório de Competência em Software Livre (LabLivre) da Universidade de Brasília (UnB)**, realizado no âmbito de um **Termo de Execução Descentralizada (TED)** firmado com a **Secretaria Nacional de Participação Social**, da Secretaria-Geral da Presidência da República.

## Objetivo

Reunir, em um só lugar e em português, o conhecimento técnico sobre o Brasil Participativo SaaS (o Participa e a participação multicanal), para que:

- **desenvolvedores** consigam entender, executar e evoluir os dois projetos;
- **equipes de operação** consigam implantar, configurar e manter as plataformas;
- **gestores de processos participativos** entendam órgãos e setores, participação efêmera, chatbot e roteiros de conversa;
- a **equipe receptora** tenha o que precisa para a transferência de tecnologia.

É uma documentação irmã da [documentação do Brasil Participativo](https://lablivre-unb.github.io/doc-bp/), com a mesma estrutura e as mesmas regras.

## O que é o TED

O **Termo de Execução Descentralizada** é o instrumento pelo qual um órgão da administração pública federal transfere crédito orçamentário a outro órgão ou entidade federal, como uma universidade, para a execução de ações de interesse comum. Neste caso, a parceria entre a Secretaria e a UnB viabiliza o desenvolvimento, a manutenção e a documentação das plataformas pelo LabLivre.

## Como esta documentação foi produzida

| Fonte | Uso |
|-------|-----|
| Código do [`participa`](https://gitlab.com/lappis-unb/decidimbr/participa) (branch `main`, commit `9253a99`) | Participa, banco de dados, sobrescritas |
| Código do [`multi-channel-participation`](https://gitlab.com/lappis-unb/decidimbr/multi-channel-participation) (branch `main`, commit `cad204d`) | Participação multicanal |
| Gems do Brasil Participativo e `participa-gem`, nas revisões travadas no `Gemfile.lock` | Módulos, multi-organização |
| Código do Decidim 0.32.1 | Inventário de sobrescritas e comportamento padrão |
| API pública do GitLab | [Estatísticas](../estatisticas/index.md) |
| [Documentação do Brasil Participativo](https://lablivre-unb.github.io/doc-bp/) | Comparações em [Inovação](../inovacao/index.md) |

As informações refletem o código na data da coleta, outubro de 2026.

## Versão em PDF

Todo o conteúdo deste site também está disponível como e-book, com capa, folha de rosto, ficha técnica, sumário e contracapa, gerado a cada atualização.

[:material-file-pdf-box: Baixar a documentação completa em PDF](https://rochacarla.github.io/doc-saas-bp/documentacao-brasil-participativo-saas.pdf){ .md-button .md-button--primary }

Para gerar localmente: `./scripts/pdf.sh` (resultado em `dist/`).

## Uso de inteligência artificial

Esta documentação foi produzida com apoio de IA generativa (Claude Code, modelo Claude Opus 5.5), sob direção e responsabilidade da equipe do LabLivre/UnB. Ferramentas, papéis, salvaguardas e limites estão em [Uso de IA](uso-de-ia.md).

## Licenças

| O quê | Licença |
|-------|---------|
| Conteúdo desta documentação (textos, diagramas, e-book) | [Creative Commons Atribuição 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.pt-br) |
| Logos e marcas da UnB, do LabLivre e do governo federal | Não incluídos na licença; uso sujeito às regras de cada instituição |
| Código desta documentação (geradores em `scripts/`, tema e templates) | GNU Affero General Public License v3 (AGPLv3) |
| Participa e Decidim | GNU Affero General Public License v3 (AGPLv3) |
| Participação multicanal | Sem arquivo de licença no repositório (**a definir**) |

Com a CC BY 4.0, qualquer pessoa pode copiar, adaptar e redistribuir o conteúdo, inclusive para fins comerciais, desde que cite a autoria (LabLivre/UnB) e indique se houve modificações.

## Contribua com a documentação

O código-fonte desta documentação está em [github.com/RochaCarla/doc-saas-bp](https://github.com/RochaCarla/doc-saas-bp). Para corrigir ou sugerir algo, use o botão de edição :material-file-edit-outline: no topo de cada página ou abra uma [issue](https://github.com/RochaCarla/doc-saas-bp/issues/new).

O site é gerado com [MkDocs](https://www.mkdocs.org/) e [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/), com visual baseado no [Design System gov.br](https://www.gov.br/ds/).

## Contato

- **Equipe de desenvolvimento**: decidim@unb.br
- **Brasil Participativo**: brasilparticipativo@presidencia.gov.br
