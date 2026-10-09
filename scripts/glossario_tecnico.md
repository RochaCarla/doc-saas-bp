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
