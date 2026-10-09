# Uso de inteligência artificial

Esta documentação foi produzida com apoio de **inteligência artificial generativa**, sob direção e responsabilidade da equipe do LabLivre/UnB. Esta página declara como a IA foi usada, que cuidados foram tomados e quais limites o leitor deve considerar.

!!! info "Resumo"
    - **Ferramenta:** Claude Code (Anthropic), com o modelo **Claude Opus 5.5**, em outubro de 2026.
    - **Papel da IA:** levantar informações no código, redigir as páginas, adaptar os scripts geradores e o tema visual da [documentação do Brasil Participativo](https://lablivre-unb.github.io/doc-bp/), e montar o e-book.
    - **Papel humano:** pedir a documentação, definir nome, endereço e licença, e decidir o que publicar.
    - **Responsabilidade:** o conteúdo é de responsabilidade da equipe do LabLivre/UnB, não da ferramenta.

## Ferramentas

| Ferramenta | Uso |
|------------|-----|
| Claude Code (Anthropic), modelo Claude Opus 5.5 | Agente de programação e redação, operado no repositório desta documentação |
| Subagentes de pesquisa do Claude Code | Três levantamentos com evidência por arquivo e linha: plataforma do Participa, funcionalidades e banco do Participa, e participação multicanal |
| Scripts determinísticos (Python e Node) | Estatísticas, dicionário de dados, inventário de sobrescritas, Glossário e e-book. **Os números vêm dos scripts, não do modelo** |

## O que a IA fez e o que ficou com pessoas

| Conteúdo | Papel da IA | Papel humano | Como foi verificado |
|----------|-------------|--------------|---------------------|
| Estrutura do site | Cópia e adaptação da estrutura do site do Brasil Participativo | Pedido e decisões de nome, endereço e licença | Build estrito |
| Participa e participação multicanal | Leitura do código e redação | Escolha dos repositórios | Cada fato com arquivo ou commit de origem; o que não tinha fonte ficou **a confirmar** |
| Banco, estatísticas, sobrescritas | Adaptação dos geradores para os dois projetos | — | Saídas reproduzíveis; colunas usadas nas consultas conferidas no `schema.rb` |
| Inovação | Comparação com a documentação do Brasil Participativo | — | Números dos inventários gerados; desempenho rotulado **medido** ou **inferido** |
| Glossário | Proposta de termos canônicos e ambiguidades no `CONTEXT.md` | — | Gerado do `CONTEXT.md` |

## Salvaguardas

- **Fonte verificável:** toda afirmação técnica aponta para arquivo, commit ou página pública.
- **Nada inventado:** o que não estava no código aparece como **a confirmar**.
- **Rótulos:** desempenho aparece como **medido** ou **inferido**.
- **Números por script:** estatísticas e contagens vêm de programas reproduzíveis.
- **Divulgação responsável:** pendências de segurança encontradas na leitura do código ficaram fora do site e foram preparadas como issues confidenciais para os repositórios.
- **Histórico:** commits feitos com a IA têm a linha `Co-Authored-By: Claude`.

## Dados tratados

| Dado | Tratamento |
|------|------------|
| Código público dos repositórios e do Decidim | Lido pela IA |
| API pública do GitLab, rubygems, PyPI e endoflife.date | Lidas pelos scripts |
| Nomes e e-mails do histórico do git | Processados pelo script de estatísticas; **e-mails não são publicados** |
| Credenciais cifradas dos repositórios | Não decifradas; só os nomes de variáveis foram publicados |
| Segredos de produção e dados pessoais | **Não** foram fornecidos à IA nem publicados |

## Limitações

- O texto pode conter imprecisões que escaparam à verificação, principalmente onde o comportamento depende de configuração de produção não versionada.
- Partes da implantação de produção estão fora dos repositórios lidos.
- O conteúdo reflete o código em outubro de 2026.

## Registro de revisão humana

| Seção | Revisada por | Data | Observações |
|-------|--------------|------|-------------|
| Visão Geral | | | |
| Participa | | | |
| Participação multicanal | | | |
| Transferência | | | |
| Inovação | | | |
| Estatísticas | | | |

## Contribuições futuras com IA

1. **Declare:** mantenha a linha `Co-Authored-By` nos commits feitos com apoio de IA.
2. **Verifique:** todo fato novo precisa de fonte. O que não tiver fonte fica **a confirmar**.
3. **Não exponha:** não forneça à IA segredos, dados pessoais ou documentos sem autorização.
4. **Prefira scripts:** números e listas extensas devem vir dos geradores em `scripts/`.
5. **Cheque o resultado:** rode o build estrito antes do merge.
6. **Revise:** uma pessoa da equipe revisa e aprova a mudança.
