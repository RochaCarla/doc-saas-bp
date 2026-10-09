---
title: Glossário
---

<!-- Gerado por scripts/glossario.py a partir do CONTEXT.md. Não edite à mão: edite o CONTEXT.md. -->

# Glossário

Linguagem oficial do Brasil Participativo SaaS e desta documentação: 62 termos, com as palavras a evitar e as ambiguidades já resolvidas. Use estes termos em textos, telas e código.

!!! info "Fonte única"
    Esta página é gerada a partir do `CONTEXT.md` do repositório. Para mudar um termo, edite o `CONTEXT.md` e rode `python3 scripts/glossario.py`.

## Instituições

Brasil Participativo
:   Plataforma nacional de participação digital do governo federal, construída sobre o **Decidim** e mantida no **core** do Brasil Participativo.

    *Evite:* BP (só em nomes técnicos, como OP-BP)

Brasil Participativo SaaS
:   Oferta da plataforma de participação como serviço para outras **organizações**, como estados, municípios e órgãos. É formada pelo **Participa** e pela **participação multicanal**.

    *Evite:* SaaS (sozinho), BP SaaS, "novo Brasil Participativo"

Secretaria Nacional de Participação Social (SNPS)
:   Unidade da Secretaria-Geral da Presidência da República que administra o **Brasil Participativo** e é parte do **TED**.

    *Evite:* "a Secretaria" sem o nome completo na primeira menção

LabLivre/UnB
:   Laboratório de Competência em Software Livre da Universidade de Brasília, que desenvolve as plataformas e esta documentação.

    *Evite:* LAPPIS (nome antigo)

TED
:   Termo de Execução Descentralizada entre a UnB e a **SNPS**, que viabiliza o desenvolvimento, a manutenção e a documentação das plataformas.

    *Evite:* convênio, contrato

Dataprev
:   Empresa pública que hospeda o **Brasil Participativo** em **produção** e cuja infraestrutura aparece nos testes de carga da **API OP-BP**.

SERPRO
:   Empresa pública que fornece a **Consulta CPF** e o **WhatsApp do SERPRO**.

Octree
:   Empresa da comunidade **Decidim** que mantém módulos usados no **Participa**, como a participação efêmera e as abas de configuração da organização, e que participou da construção da **multi-organização**.

## Pessoas e papéis

Participante
:   Pessoa que participa de um **espaço participativo** ou de um processo da **API OP-BP**: propõe, vota, comenta ou responde formulários.

    *Evite:* usuário (só ao contar contas, em rótulos da interface e ao falar do código ou do banco), cidadão (só em nomes oficiais e para o público em geral)

Gestor de processo
:   Servidor de uma **organização** que cria, publica e acompanha **espaços participativos** pelo painel.

    *Evite:* administrador (é o **papel**, não a pessoa), admin

Equipe de operação
:   Equipe técnica que implanta, configura, monitora e recupera as plataformas.

    *Evite:* operador (na LGPD é outro conceito), sysadmin

Equipe receptora
:   Equipe que assume a manutenção e a operação das plataformas ao fim da **transferência de tecnologia**.

    *Evite:* "governo" (genérico), cliente

Papel
:   Nível de acesso de uma pessoa aos painéis: administrador de sistema, administrador da organização, administrador de espaço, **administrador com escopo**, moderador, avaliador ou colaborador.

    *Evite:* perfil (é a página pública do participante)

Administrador com escopo
:   **Papel** do **Participa** que administra os processos de um **órgão** ou **setor**, sem poder excluí-los.

    *Evite:* administrador do órgão (sem dizer que é um papel), admin setorial

## Plataforma e código

Decidim
:   Software livre de democracia participativa, base do **Brasil Participativo** e do **Participa**.

    *Evite:* upstream (só ao comparar código), plataforma base

Core do Brasil Participativo
:   Repositório `decidim-govbr` do **Brasil Participativo**, sobre o Decidim 0.27, que altera o Decidim por **sobrescritas**.

    *Evite:* "o decidim-govbr" sem qualificar (veja as ambiguidades)

Participa
:   Plataforma do **Brasil Participativo SaaS** sobre o Decidim 0.32, que atende várias **organizações** numa só **instalação**. Foi criada do zero, sem histórico em comum com o **core do Brasil Participativo**.

    *Evite:* fork do decidim-govbr, versão nova do Brasil Participativo, SaaS (sozinho)

Organização
:   Unidade atendida pelo **Participa**, identificada por um endereço, com participantes, **espaços participativos** e configurações próprios. Cada organização tem um schema próprio no banco.

    *Evite:* tenant (só no código), cliente, instância (é outro conceito)

Multi-organização
:   Capacidade do **Participa** de atender várias **organizações** numa só **instalação**, isolando os dados de cada uma.

    *Evite:* multi-tenant, multitenancy (só em texto técnico), "um banco por cliente"

Instalação
:   Um conjunto implantado do **Participa** ou da **API OP-BP**, com seu endereço, banco e configuração, como a instalação de desenvolvimento do Participa do Acre.

    *Evite:* instância (é um **espaço participativo**), deploy

Sobrescrita
:   Arquivo que substitui o arquivo de mesmo caminho numa gem do **Decidim**; é o principal custo de atualização.

    *Evite:* patch, override, customização (genérico)

Módulo Decidim
:   Funcionalidade nativa do **Decidim**, como propostas, reuniões e formulários.

    *Evite:* plugin, componente customizado

Gem do Brasil Participativo
:   Extensão do **Decidim** desenvolvida pelo **LabLivre/UnB** em repositório próprio e instalada no **Participa**, como as regras por **etapa** de propostas e reuniões.

    *Evite:* plugin, módulo BP

Engine do repositório
:   Extensão do **Decidim** versionada dentro do próprio repositório do **Participa**: a engine gov.br e o **chatbot**.

    *Evite:* componente, plugin

Componente
:   Funcionalidade adicionada pelo painel a um **espaço participativo**, como um conjunto de propostas ou um **texto participativo**.

    *Evite:* módulo, gem

Produção
:   A **instalação** que atende o público de verdade.

    *Evite:* "a main" como sinônimo de produção

Homologação
:   **Instalação** em que uma **versão candidata** é validada antes de ir para **produção**.

    *Evite:* laboratório (é o LabLivre), lab, staging

Versão candidata
:   Versão em **homologação** antes de se tornar **versão estável**.

    *Evite:* beta, build

Versão estável
:   Versão liberada para **produção**. No **Participa**, o nome junta a versão do Decidim e a do Participa, como `0.32.1-v1.0.1`.

    *Evite:* release (sem qualificar)

## Participação

Espaço participativo
:   Lugar onde a participação acontece: um **processo participativo** ou uma **instância**. Um espaço tem muitos **componentes**.

    *Evite:* espaço (sozinho), página

Processo participativo
:   Mecanismo institucional de interlocução entre a administração pública e os cidadãos para elaborar, executar, monitorar ou avaliar leis, projetos e políticas públicas. Tem **etapas**.

    *Evite:* campanha, consulta (quando não for Consulta Pública)

Instância
:   **Espaço participativo** permanente, como um conselho, colegiado ou fórum.

    *Evite:* assembleia (só ao falar do código ou do banco)

Etapa
:   Fase de um **processo participativo**, com período definido. No **Participa**, a troca de etapa pode ser automática pelas datas.

    *Evite:* step (só no código), fase (no texto da interface)

Órgão
:   Primeiro nível da hierarquia de governo de uma **organização** no **Participa**, como uma secretaria. Tem **setores**.

    *Evite:* escopo (é outro mecanismo do Decidim), public body

Setor
:   Unidade de um **órgão** no **Participa**, responsável por **processos participativos**.

    *Evite:* subescopo, sub-instância (é do Brasil Participativo)

Proposta
:   Contribuição de um participante, que pode ser votada, comentada e moderada.

Texto participativo
:   Documento dividido em parágrafos, cada um aberto a comentários. No **Participa**, é um **componente** próprio, com **devolutiva** por comentário.

    *Evite:* minuta (só quando o documento de fato for uma minuta)

Devolutiva
:   Retorno do poder público aos participantes sobre o que foi feito com a participação. No **texto participativo** do Participa, cada comentário recebe uma devolutiva.

    *Evite:* feedback

Participação efêmera
:   Forma de participar no **Participa** sem cadastro completo, informando CPF e nome. Quem participa assim é um **participante efêmero**.

    *Evite:* participação anônima (o CPF é informado), login efêmero

Modelo de processo
:   Processo de partida, com etapas, componentes e conteúdo, guardado num catálogo compartilhado e usado para criar novos processos no **Participa**.

    *Evite:* template (só no código)

Orçamento do Povo
:   Orçamento participativo federal, com participação pela web, por mensageria e presencial. Foi o primeiro processo atendido pela **API OP-BP**.

    *Evite:* "OP" em texto corrido

## Mensageria

Participação multicanal
:   Projeto que leva a participação para o WhatsApp, o Telegram e um **app de participação**; repositório `multi-channel-participation`. Formado pela **API OP-BP**, pelo **painel administrativo** e pelo **app de participação**.

    *Evite:* multicanal (sozinho como substantivo), bot

API OP-BP
:   Sistema da **participação multicanal** que recebe as mensagens dos canais, conduz o **roteiro de conversa**, valida a identidade e registra os votos no **Decidim**.

    *Evite:* BPAPI (é o nome do painel), bot, N8N (implementação anterior)

Painel administrativo
:   Interface da **participação multicanal** em que se configuram processos, **roteiros de conversa**, propostas e a operação da **API OP-BP**.

    *Evite:* BPAPI (só ao citar a tela), admin

App de participação
:   Aplicação de votação do **Orçamento do Povo** que roda como Telegram Mini App ou página web.

    *Evite:* front (genérico), mini app (sozinho)

Roteiro de conversa
:   Máquina de estados em YAML que define a conversa da **API OP-BP** num processo, editável e versionada pelo **painel administrativo**.

    *Evite:* fluxo (sozinho), flow, script

Chatbot
:   Módulo do **Participa** que atende participantes por WhatsApp com um roteiro fixo, de termos editáveis, e registra votos em propostas.

    *Evite:* API OP-BP (é outro sistema), bot (sozinho)

WhatsApp do SERPRO
:   Serviço do **SERPRO** para enviar e receber mensagens de WhatsApp, usado pela **API OP-BP** e pelo **chatbot**.

    *Evite:* API da Meta, WhatsApp Business (sem qualificar)

Consulta CPF
:   Serviço do **SERPRO** que confere CPF, nome e data de nascimento.

    *Evite:* validação na Receita

Identificação progressiva
:   Sequência de níveis de um participante na **API OP-BP**: anônimo (só o identificador do canal), identificado (CPF conferido na **Consulta CPF**) e autenticado (login **gov.br**).

    *Evite:* cadastro, onboarding

gov.br
:   Login Único do governo federal.

Login externo
:   Vínculo entre a conta **gov.br** e o participante que chegou por um canal de mensagens, feito pelo **Brasil Participativo** a pedido da **API OP-BP**.

    *Evite:* login social, SSO

Impersonação
:   Acesso pelo qual a **API OP-BP** age no **Decidim** em nome de um participante já vinculado.

    *Evite:* login por API

## Documentação

Página gerada
:   Página da documentação produzida automaticamente a partir do código e de fontes públicas, e que não se edita à mão.

    *Evite:* página automática, relatório

Série analisada
:   Período coberto pelas estatísticas de um projeto, a partir do mês do primeiro commit.

    *Evite:* histórico completo

Fator de ausência
:   Menor número de pessoas que somam metade das contribuições de código.

    *Evite:* bus factor (em texto corrido)

A confirmar
:   Marca de informação sem fonte verificável, que precisa ser levantada com a equipe atual.

    *Evite:* TBD, a definir

Medido / inferido
:   Qualificação de uma afirmação de desempenho: *medido* quando há número publicado; *inferido* quando é conclusão da leitura do código.

Canal restrito
:   Issue confidencial no repositório do projeto, onde ficam as pendências de segurança ainda não corrigidas.

    *Evite:* "relatado à equipe" sem dizer onde

Transferência de tecnologia
:   Passagem das plataformas do **LabLivre/UnB** para a **equipe receptora**, em fases, com critérios de aceite.

    *Evite:* handover, repasse (repasse é só a fase de capacitação)

E-book
:   Versão em PDF, autônoma, de todo o conteúdo da documentação.

    *Evite:* exportação, impressão

Rodapé institucional
:   Faixa no fim de toda página que identifica quem realiza a documentação e quem é parceiro.

    *Evite:* rodapé (sozinho)

## Ambiguidades resolvidas

Palavras que aparecem com mais de um sentido no projeto, e o sentido que vale.

- **"decidim-govbr"**: é o nome do repositório do **core do Brasil Participativo** (Decidim 0.27) e também o de uma **engine do repositório** do **Participa**, criada do zero, com código diferente. Termo canônico: **core do Brasil Participativo** para o repositório; **engine gov.br do Participa** para a engine.
- **"Órgão" e "setor"**: no **Brasil Participativo**, órgãos são escopos do Decidim e geram **instâncias** automaticamente, com sub-instâncias por setor. No **Participa**, **órgão** e **setor** são uma hierarquia própria de governo, que organiza **processos participativos** e **administradores com escopo**, sem criar instâncias. Diga sempre de qual plataforma se trata.
- **"Efêmero"**: o **participante efêmero** do **Participa** informa CPF e nome para participar sem cadastro. O usuário efêmero que a **API OP-BP** cria no **Brasil Participativo** é uma conta técnica para registrar votos de quem validou o CPF. Termo canônico: **participação efêmera** para o Participa; "usuário efêmero da API OP-BP" para o outro caso.
- **"Chatbot" × "API OP-BP"**: as duas atendem participantes pelo WhatsApp do SERPRO, mas são sistemas diferentes. O **chatbot** está dentro do **Participa**; a **API OP-BP** é um sistema à parte, que registra votos no **Brasil Participativo**. Termo canônico: **chatbot** só para o módulo do Participa.
- **"Roteiro"**: o **roteiro de conversa** da **API OP-BP** é uma máquina de estados inteira, editável pelo painel. O roteiro do **chatbot** é fixo; só os termos são editáveis. Qualifique sempre.
- **"Processo" na API OP-BP**: o painel da **API OP-BP** chama de processo a configuração de um canal com seu **roteiro de conversa**, regras de voto e propostas. Ele pode apontar para um **processo participativo** do Decidim, mas não é o mesmo objeto. Termo canônico: "processo da API OP-BP".
- **"Instância"**: no Decidim, é um **espaço participativo** permanente. Em infraestrutura, a palavra aparece para um conjunto implantado, como no nome do chart Helm do Participa. Termo canônico: **instância** só para o espaço participativo; **instalação** para o conjunto implantado.
- **"Orçamento Participativo"**: é um dos tipos de processo criados como taxonomia no **Participa**, o nome do primeiro processo da **API OP-BP** e o assunto do módulo Orçamentos do Decidim. O programa federal é o **Orçamento do Povo**. Diga qual dos três.
- **"Modelo"**: o **modelo de processo** do **Participa** vem de um catálogo compartilhado. O Decidim tem um módulo próprio de modelos, que não está instalado. Termo canônico: **modelo de processo**.

??? example "Diálogo de exemplo"

    > **Equipe receptora**: O município X quer usar a plataforma. Instalamos um Decidim novo para ele?
    >
    > **Especialista**: Não. O **Participa** é **multi-organização**: criamos uma **organização** nova no painel de sistema, e ela ganha um schema próprio no banco. Falta só o endereço, o certificado e a rota de entrada, que ficam fora do chart.
    >
    > **Equipe receptora**: E as secretarias do município?
    >
    > **Especialista**: Cada secretaria é um **órgão**, com seus **setores**. O **gestor de processo** de um setor recebe o papel de **administrador com escopo** e só vê os processos do setor. Não confunda com os órgãos do **Brasil Participativo**, que viram **instâncias**.
    >
    > **Equipe receptora**: Eles também querem votação pelo WhatsApp. Usamos a **API OP-BP**?
    >
    > **Especialista**: Depende. O Participa já tem o **chatbot**, que vota direto nas propostas com **participação efêmera** ou gov.br. A **API OP-BP** é outro sistema, com **roteiros de conversa** editáveis, e hoje registra votos no **Brasil Participativo**. A escolha entre os dois ainda está **a confirmar**.

## Termos técnicos

Conceitos gerais de tecnologia usados nesta documentação.

Rails Engine
:   Mini-aplicação Rails empacotada como gem. O Decidim, seus módulos e as engines do Participa são engines.

Command, Form, Cell, Permission
:   Padrões de código do Decidim: regra de negócio, validação de entrada, componente de interface e regra de acesso.

`prepend`
:   Recurso do Ruby que insere um módulo antes de uma classe, para alterar só alguns métodos dela. É a forma preferida de customizar o Decidim no Participa.

Deface
:   Gem que altera trechos de views Rails sem copiá-las.

Apartment
:   Gem (`ros-apartment`) que separa os dados de cada organização num schema PostgreSQL. A `decidim-apartment` a integra ao Decidim. Veja [Multi-organização](../participa/multi-organizacao.md).

Sidekiq
:   Processador de tarefas em segundo plano do Participa, que usa o Redis como fila.

Helm
:   Gerenciador de pacotes (*charts*) do Kubernetes, usado para implantar o Participa.

CloudNativePG
:   Operador Kubernetes que cria e mantém clusters PostgreSQL.

FastAPI
:   Framework web em Python usado pela API OP-BP.

Dramatiq
:   Processador de tarefas em segundo plano da API OP-BP.

Valkey
:   Banco em memória compatível com o Redis, usado pela API OP-BP para cache e filas.

PgBouncer
:   Intermediário que agrupa conexões ao PostgreSQL.

Alembic
:   Ferramenta de migrações de banco da API OP-BP.

Design System gov.br
:   Padrão visual do governo federal. No Participa, seus tokens, fonte e cores são usados pela engine gov.br.

Mermaid
:   Linguagem de diagramas em texto usada nesta documentação.
