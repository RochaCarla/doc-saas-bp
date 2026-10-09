# Inovações do Participa

## Uma instalação, muitas organizações

O Decidim já permite várias organizações num banco, separadas por coluna. O Participa vai além e dá a cada organização um **schema PostgreSQL próprio**, escolhido pelo host da requisição, com cache, arquivos e jobs também separados ([Multi-organização](../participa/multi-organizacao.md)).

| Ganho | Como |
|-------|------|
| Organização nova sem nova instalação | Criação pelo `/system`, com schema criado e desfeito em caso de erro |
| Isolamento de dados mais forte que a coluna `decidim_organization_id` | `search_path` por requisição |
| Manutenção única | Uma imagem, um chart e uma migração para todas as organizações |

O custo: tarefas periódicas e jobs agendados precisam percorrer os schemas, e não há conversão pronta de um Decidim tradicional.

## Customizar sem sobrescrever

| | Brasil Participativo | Participa |
|--|---------------------:|----------:|
| Arquivos sobrescritos | 492 | 31 |
| Linhas diferentes do Decidim | cerca de 21 mil | cerca de 2 mil |
| Sobrescritas idênticas ao original | 26 | 0 |

Fonte: [inventário do Participa](../transferencia/sobrescritas.md) e inventário publicado do core do Brasil Participativo.

A redução veio de levar as funcionalidades para **gems** e de usar **`prepend`** e **Deface** nos pontos que restaram ([Customização](../participa/customizacao.md)). O resultado é visível no histórico: o Participa passou do Decidim 0.30.9 ao 0.32.1 (que trocou o Rails 7.0 pelo 8.1) em setembro de 2026, enquanto o core do Brasil Participativo segue no 0.27.2.

## Regras por etapa

As gems `decidim-bp_proposals` e `decidim-bp_meetings` levam para a **etapa** decisões que o Decidim toma para o componente inteiro:

- quem pode comentar propostas e reuniões;
- se participantes podem criar reuniões;
- se o administrador e o participante podem anexar arquivos à reunião (o participante anexar à própria reunião não existe no Decidim).

Assim, um processo pode abrir comentários só na etapa de consulta e fechá-los na de sistematização sem reconfigurar componentes.

## Comentários com resposta oficial

A gem `decidim-bp_comments` organiza a conversa em dois níveis: participantes comentam, e só papéis administrativos respondem, com a etiqueta "Resposta Oficial". Autores comuns editam ou excluem o próprio comentário nos primeiros 5 minutos.

## Órgãos, setores e administradores com escopo

Em vez de usar escopos e criar instâncias automaticamente, como o Brasil Participativo, o Participa modela a estrutura de governo (Órgão → Setor) e dá acesso por ela: quem administra um setor vê só os processos do setor, sem poder excluí-los ([Órgãos e setores](../participa/orgaos-setores.md)). A funcionalidade foi especificada antes de implementada (OpenSpec, branch `feat/govspace`).

## Participar sem cadastro, sem perder o voto depois

A [participação efêmera](../participa/participacao-efemera.md) permite votar com CPF e nome. Se a pessoa entrar depois com o gov.br, os votos passam para a conta, sem quebrar o limite de votos nem o índice único (sobrescrita de `AuthorizationTransfer`).

## Texto participativo com devolutiva por comentário

O componente próprio registra, para cada comentário de parágrafo, se a sugestão foi incorporada, incorporada em parte ou não incorporada ([Texto participativo](../participa/texto-participativo.md)). A devolutiva deixa de ser só um relatório no fim do processo.

## Modelos de processo compartilhados

Um catálogo em repositório Git permite criar processos a partir de modelos e publicar novos modelos, com uma organização de demonstração para prévia ([Modelos de processo](../participa/modelos.md)). Uma secretaria municipal pode partir de um processo pronto de outra organização.

## Troca automática de etapa

Por processo, um job de hora em hora ativa a etapa cujas datas cobrem o momento atual, em todas as organizações. Remove um passo manual que, esquecido, deixava processos na etapa errada.

## Chatbot com identificação forte

O [chatbot](../participa/chatbot.md) leva a votação ao WhatsApp sem sair do Participa: o voto usa o mesmo comando e as mesmas permissões do site. A identificação é feita por um link de uso único, válido por 1 hora, por CPF e nome ou pelo gov.br, e o painel tem uma lista de verificação de 9 itens antes de colocar no ar.

## Desempenho

Não há medições de desempenho do Participa publicadas no repositório. Pontos do desenho que favorecem o desempenho (**inferido**):

- cache Redis separado da fila, com namespace por organização;
- assets compilados uma vez por versão e servidos por nginx, fora do Puma;
- exportação de respostas de formulário em CSV por *streaming* e em lotes (`decidim-questionnaires`).
