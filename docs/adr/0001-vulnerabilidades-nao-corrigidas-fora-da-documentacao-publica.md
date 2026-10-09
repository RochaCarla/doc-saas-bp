# Vulnerabilidades não corrigidas ficam fora da documentação pública

A documentação é pública (site e e-book) e descreve o Participa e a participação multicanal com detalhe de código. Seguimos a mesma regra da documentação do Brasil Participativo: vulnerabilidades ainda não corrigidas são registradas apenas em issues confidenciais nos repositórios do GitLab (`participa` e `multi-channel-participation`), e o site e o e-book trazem só um aviso neutro, porque detalhar uma falha explorável antes da correção entrega o caminho do ataque, e o que é publicado não pode ser "despublicado". Depois de corrigida e implantada, a vulnerabilidade entra na documentação como risco resolvido, com a versão da correção.

## Consequences

- Os rascunhos das issues ficam em `dist/` (ignorado pelo git) até serem abertos no GitLab.
- Também ficam fora do site detalhes de configuração que apontam diretamente para uma falha, mesmo quando o nome da variável é público.
- A transferência de tecnologia precisa incluir o acesso da equipe receptora às issues confidenciais.
