# Inovações da participação multicanal

## Identificação progressiva

A participação começa sem nenhuma barreira: basta escrever no WhatsApp ou no Telegram. O participante pode votar anônimo e, depois, subir de nível, informando o CPF (conferido na Consulta CPF do SERPRO) ou entrando com o gov.br. O voto acompanha o nível: só votos identificados ou autenticados vão para o Brasil Participativo ([Votação e identificação](../multicanal/votacao.md)).

Esse desenho permite medir onde as pessoas desistem, uma pergunta central em participação por mensagens.

## Roteiros de conversa editáveis sem reinício

Os roteiros são máquinas de estados em YAML, guardadas no banco, com editor visual no painel (grafo, simulador e editores de estado, mensagem, condição e ação), versões imutáveis e publicação. O motor compila os roteiros em memória pela data de atualização, então uma mudança publicada vale na mensagem seguinte ([Roteiros de conversa](../multicanal/roteiros.md)).

Com isso, o gestor de processo cria uma consulta nova, como a da Vila Carioca, sem escrever código.

## Desenhada para escala

| Escolha | Efeito |
|---------|--------|
| Webhook responde rápido; votos e chamadas externas vão para filas | A API não espera o Decidim nem o SERPRO |
| Quatro filas com prioridades (`critical` a `low-priority`) | Votos não esperam tarefas de manutenção |
| Registro de cada tarefa antes do envio à fila e reenvio de tarefas presas | Nenhum voto se perde se a fila falhar |
| Marca de voto no Valkey que falha fechada | Sem voto duplo, mesmo com o cache fora do ar |
| Circuit breakers para SERPRO, WhatsApp e catálogo | Uma integração lenta não derruba as outras |
| PgBouncer em modo transação e Valkey separado para filas | Conexões e memória sob controle |

Resultados **medidos** do relatório de carga do repositório (`api/tests/load_tests/results/REPORT.md`, servidor de 4 CPUs e 32 GB):

- 150 participantes por segundo durante 6 horas (350 a 400 mil participantes) com boa experiência;
- a 300 e 350 participantes por segundo, perda considerável e sobrecarga do banco;
- conclusão do relatório: até cerca de 1 milhão de participantes por dia.

## Um processo, vários canais e provedores

Cada processo declara o provedor de cada canal, com credenciais próprias de WhatsApp do SERPRO cifradas no banco. Uma única instalação da API atende processos de órgãos diferentes, cada um com seu número de WhatsApp ([Canais](../multicanal/canais.md)).

## Catálogo compatível com várias versões do Decidim

O concierge lista processos abertos de qualquer Decidim entre 0.27 e 0.32: a consulta GraphQL remove os campos que a instância não conhece e se adapta aos tipos de processo das versões antigas ([Integração com o Decidim](../multicanal/integracao.md#catalogo-de-processos)).

## LGPD no desenho

- CPF cifrado com chave rotacionável; só hash e máscara nas auditorias; CPF sempre mascarado no painel.
- Anonimização por processo em duas etapas, com prova de participação desvinculada do voto e reversão por 7 dias.
- Validações que impedem a API de iniciar em produção sem os segredos obrigatórios.

O que ainda falta (retenção e expurgo de dados) está em [Segurança e LGPD](../transferencia/seguranca.md).
