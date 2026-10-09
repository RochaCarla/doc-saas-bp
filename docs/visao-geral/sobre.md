# Sobre o Brasil Participativo SaaS

O **Brasil Participativo SaaS** leva a plataforma de participação do governo federal a outras **organizações**, como estados, municípios e órgãos, e a novos canais. Ele é formado por dois projetos de software livre, desenvolvidos pelo LabLivre/UnB:

| Projeto | O que é | Repositório |
|---------|---------|-------------|
| **[Participa](../participa/index.md)** | Plataforma de participação sobre o Decidim 0.32.1 que atende várias organizações numa só instalação | [`participa`](https://gitlab.com/lappis-unb/decidimbr/participa) |
| **[Participação multicanal](../multicanal/index.md)** | API OP-BP, painel e app que levam a participação ao WhatsApp, ao Telegram e a um app web | [`multi-channel-participation`](https://gitlab.com/lappis-unb/decidimbr/multi-channel-participation) |

## Relação com o Brasil Participativo

O [Brasil Participativo](https://brasilparticipativo.presidencia.gov.br/) é a plataforma nacional, mantida no core `decidim-govbr` (Decidim 0.27.2) e documentada em [lablivre-unb.github.io/doc-bp](https://lablivre-unb.github.io/doc-bp/).

| | Brasil Participativo | Participa | Participação multicanal |
|--|---------------------|-----------|------------------------|
| Público | Governo federal | Estados, municípios e órgãos | Processos com participação por mensagens |
| Base | Decidim 0.27.2 | Decidim 0.32.1 | Python (FastAPI) |
| Organizações por instalação | Uma | Várias | Não se aplica |
| Início do repositório | Set. 2021 | Mai. 2025 | Mar. 2026 |
| Relação de código | — | Criado do zero; nenhum commit em comum com o core | Registra votos no Brasil Participativo |

O Participa não é um fork do core do Brasil Participativo: os dois repositórios não compartilham commits. As customizações do Brasil Participativo foram trazidas de novo, como gems e engines, e uma engine do Participa recebeu o mesmo nome, `decidim-govbr` (veja o [Glossário](glossario.md)).

## Quem usa

| Perfil | O que encontra aqui |
|--------|---------------------|
| **Gestor de processo** | Como funcionam órgãos e setores, participação efêmera, texto participativo, modelos de processo e o chatbot |
| **Equipe de operação** | Implantação em Kubernetes, configuração, multi-organização e rotinas da API OP-BP |
| **Pessoa desenvolvedora** | Ambiente local, módulos, customização do Decidim, banco de dados e roteiros de conversa |
| **Equipe receptora** | Inventário, segurança, decisões e plano de atualização na aba [Transferência](../transferencia/index.md) |

## Situação em outubro de 2026

- O **Participa** está em Decidim 0.32.1, a versão mais recente do Decidim, com a versão `0.32.1-v1.0.1` publicada e a `v1.0.2` integrada à `main` sem tag.
- A **participação multicanal** não tem versões publicadas; a API está em `0.1.0`.
- Há duas soluções de WhatsApp: o **chatbot** dentro do Participa e a **API OP-BP**. Qual será o caminho está **a confirmar**.
- A instalação de desenvolvimento do Participa do Acre é a referência citada no código da API OP-BP para o catálogo de processos.

Números de atividade e qualidade em [Estatísticas](../estatisticas/index.md).
