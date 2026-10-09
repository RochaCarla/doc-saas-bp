---
hide:
  - navigation
  - toc
hide_feedback: true
---

<div class="bp-hero" markdown>

# Documentação do Brasil Participativo SaaS

A plataforma de participação do governo federal como serviço para estados, municípios e órgãos, e a participação por WhatsApp e Telegram, construídas com software livre sobre o [Decidim](https://decidim.org/).

[Comece por aqui](visao-geral/trilhas.md){ .md-button .md-button--primary }
[Participa](participa/index.md){ .md-button }
[Participação multicanal](multicanal/index.md){ .md-button }
[:material-file-pdf-box: Baixar PDF](https://rochacarla.github.io/doc-saas-bp/documentacao-brasil-participativo-saas.pdf){ .md-button }

</div>

## Novo por aqui?

Entenda [o que é o Brasil Participativo SaaS](visao-geral/sobre.md), veja [como as peças se ligam](visao-geral/arquitetura.md) e siga a [trilha de aprendizado](visao-geral/trilhas.md) do seu perfil.

<div class="grid cards" markdown>

-   :material-domain:{ .lg .middle } **Participa**

    ---

    Plataforma multi-organização sobre o Decidim 0.32.1: um schema por organização, órgãos e setores, participação efêmera, chatbot de WhatsApp.

    [:octicons-arrow-right-24: Participa](participa/index.md)

-   :material-message-processing:{ .lg .middle } **Participação multicanal**

    ---

    API OP-BP, painel e app: WhatsApp, Telegram, roteiros de conversa editáveis e identificação progressiva por CPF e gov.br.

    [:octicons-arrow-right-24: Participação multicanal](multicanal/index.md)

-   :material-transfer:{ .lg .middle } **Transferência**

    ---

    Inventário, operação, segurança, APIs, versões, testes, decisões pendentes e plano de repasse.

    [:octicons-arrow-right-24: Transferência](transferencia/index.md)

-   :material-chart-line:{ .lg .middle } **Gestão e pesquisa**

    ---

    O que mudou em relação ao Brasil Participativo e indicadores de qualidade dos dois projetos.

    [:octicons-arrow-right-24: Inovação](inovacao/index.md)

</div>

## Documentos em destaque

<div class="grid cards" markdown>

-   **[Arquitetura do sistema](visao-geral/arquitetura.md)**

    ---

    Participa, API OP-BP, Brasil Participativo, gov.br e SERPRO num só diagrama.

-   **[Multi-organização](participa/multi-organizacao.md)**

    ---

    Como o Participa separa cada organização num schema PostgreSQL próprio.

-   **[Roteiros de conversa](multicanal/roteiros.md)**

    ---

    Máquinas de estados em YAML que o gestor de processo edita no painel.

-   **[Banco de Dados do Participa](participa/banco-de-dados/index.md)**

    ---

    Dicionário das 153 tabelas, gerado do `schema.rb`, com o que não vem do Decidim.

-   **[Decisões pendentes](transferencia/decisoes.md#decisoes-pendentes)**

    ---

    Uma ou duas soluções de WhatsApp, futuro do Brasil Participativo e manifestos de produção.

-   **[Glossário](visao-geral/glossario.md)**

    ---

    Organização, órgão, setor, participação efêmera, chatbot, API OP-BP e as palavras que mudam de sentido entre as plataformas.

</div>

## Em números

<div class="bp-stats" markdown>
<div><strong>0.32.1</strong><span>versão do Decidim no Participa</span></div>
<div><strong>31</strong><span>sobrescritas do Decidim (eram 492)</span></div>
<div><strong>153</strong><span>tabelas por organização</span></div>
<div><strong>688</strong><span>commits nos dois projetos</span></div>
<div><strong>19</strong><span>tabelas da API OP-BP</span></div>
</div>

Sobrescritas e tabelas: páginas geradas do código. Commits: [Estatísticas](estatisticas/index.md).

## Links úteis

| | |
|---|---|
| Código do Participa | [gitlab.com/lappis-unb/decidimbr/participa](https://gitlab.com/lappis-unb/decidimbr/participa) |
| Código da participação multicanal | [gitlab.com/lappis-unb/decidimbr/multi-channel-participation](https://gitlab.com/lappis-unb/decidimbr/multi-channel-participation) |
| Gems do Brasil Participativo | [components-brasil-participativo](https://gitlab.com/lappis-unb/decidimbr/components-brasil-participativo) |
| Documentação do Brasil Participativo | [lablivre-unb.github.io/doc-bp](https://lablivre-unb.github.io/doc-bp/) |
| Decidim | [decidim.org](https://decidim.org/) · [documentação oficial](https://docs.decidim.org/) |
| Sobre esta documentação | [LabLivre/UnB e TED com a Secretaria](sobre/index.md) |
