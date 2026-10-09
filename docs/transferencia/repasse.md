# Plano de repasse de conhecimento

## Perfis da equipe receptora

| Perfil | Precisa dominar |
|--------|-----------------|
| Desenvolvimento Ruby/Decidim | Participa, gems do Brasil Participativo, multi-organização, customização |
| Desenvolvimento Python | API OP-BP, workers, roteiros de conversa, integrações |
| Front-end | Painel administrativo e app de participação |
| Operação | Kubernetes, Helm, CloudNativePG, Docker Compose da API OP-BP, monitoramento |
| Gestão | Órgãos e setores, modelos de processo, chatbot, roteiros e LGPD |

## Trilha de sessões

| # | Tema | Leitura | Exercício |
|---|------|---------|-----------|
| 1 | O produto e as duas plataformas | [Sobre](../visao-geral/sobre.md), [Arquitetura do sistema](../visao-geral/arquitetura.md), [Glossário](../visao-geral/glossario.md) | Explicar com as próprias palavras a diferença entre chatbot e API OP-BP |
| 2 | Participa: código e multi-organização | [Arquitetura](../participa/arquitetura.md), [Multi-organização](../participa/multi-organizacao.md) | Subir o ambiente local e criar duas organizações |
| 3 | Participa: módulos e customização | [Módulos e gems](../participa/modulos.md), [Customização](../participa/customizacao.md) | Alterar um texto por Deface e um comportamento por `prepend`, com teste |
| 4 | Participa: governo e participação | [Órgãos e setores](../participa/orgaos-setores.md), [Participação efêmera](../participa/participacao-efemera.md), [Chatbot](../participa/chatbot.md) | Montar órgão, setor e administrador com escopo; votar como participante efêmero |
| 5 | Participa: implantação | [Implantação](../participa/implantacao.md), [Configuração](../participa/configuracao.md) | Instalar o chart num cluster de teste e criar uma organização com endereço próprio |
| 6 | API OP-BP: arquitetura e canais | [Arquitetura](../multicanal/arquitetura.md), [Canais](../multicanal/canais.md) | Subir a API local e simular uma conversa pelo webhook do Telegram |
| 7 | API OP-BP: roteiros e votação | [Roteiros](../multicanal/roteiros.md), [Votação](../multicanal/votacao.md), [Integração](../multicanal/integracao.md) | Alterar e publicar um roteiro; registrar um voto num Decidim de teste |
| 8 | Operação e incidentes | [Operação](operacao.md), [Segurança](seguranca.md) | Restaurar backups; reprocessar tarefas com falha; rotacionar um segredo |
| 9 | Versões e atualização | [Release](release.md), [Atualização](atualizacao.md) | Gerar uma versão do Participa e implantá-la em homologação |

## Operação assistida

Durante pelo menos um ciclo completo de versão de cada projeto, a equipe receptora executa e o LabLivre acompanha: criação de organização, versão, implantação, incidente simulado e restauração.

## Matriz de responsabilidades

R = executa, A = aprova, C = consultado, I = informado.

| Atividade | LabLivre | Receptor | SNPS | Organizações |
|-----------|:--------:|:--------:|:----:|:------------:|
| Manter o código e as gems | R → C | A → R | I | — |
| Versões e implantação | R → C | A → R | I | I |
| Criar organizações no Participa | R → C | R | A | C |
| Gestão de processos e roteiros | C | C | A | R |
| Segurança e pendências restritas | R | R | A | I |
| LGPD (controlador, retenção) | C | C | R | R |

A seta indica a mudança ao longo das fases.

## Encerramento

1. Critérios de aceite da [Transferência](index.md#criterios-de-aceite) cumpridos.
2. Contas e acessos do [Inventário](inventario.md) transferidos ou com acesso de administração da equipe receptora.
3. Acessos do LabLivre revogados ou reduzidos ao combinado.
4. Termo de aceite assinado pela SNPS.
