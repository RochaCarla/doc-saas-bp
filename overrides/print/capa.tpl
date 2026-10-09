{#- Elementos pré-textuais do e-book. O gerador de PDF (scripts/gerar_pdf.cjs) imprime cada bloco em separado. -#}

<div class="bp-front bp-front--capa">
  <div class="bp-capa">
    <p class="bp-capa__brand">Universidade de Brasília · LabLivre</p>
    <div class="bp-capa__main">
      <p class="bp-capa__kicker">Documentação técnica</p>
      <h1 class="bp-capa__title">Brasil<br>Participativo<br>SaaS</h1>
      <p class="bp-capa__subtitle">Participa, plataforma multi-organização sobre o Decidim, e participação multicanal por WhatsApp e Telegram</p>
    </div>
    <div class="bp-capa__footer">
      <p>Secretaria Nacional de Participação Social<br>Secretaria-Geral da Presidência da República</p>
      <p class="bp-capa__edition">Edição de <span class="bp-edition">2026</span></p>
    </div>
  </div>
</div>

<div class="bp-front bp-front--rosto">
  <p class="bp-rosto__inst">Universidade de Brasília<br>Laboratório de Competência em Software Livre (LabLivre)</p>

  <h1 class="bp-rosto__title">Brasil Participativo SaaS</h1>
  <p class="bp-rosto__subtitle">Documentação técnica do Participa e da participação multicanal</p>

  <p class="bp-rosto__inst">Produzido no âmbito do Termo de Execução Descentralizada (TED) entre a Universidade de Brasília e a Secretaria Nacional de Participação Social, da Secretaria-Geral da Presidência da República.</p>

  <h2 class="bp-rosto__heading">Informações gerais</h2>
  <table class="bp-ficha">
    <tr><th>Título</th><td>Brasil Participativo SaaS: documentação técnica do Participa e da participação multicanal</td></tr>
    <tr><th>Edição</th><td><span class="bp-edition">2026</span></td></tr>
    <tr><th>Versão do conteúdo</th><td><span class="bp-version">—</span>, gerada em <span class="bp-generated">—</span></td></tr>
    <tr><th>Realização</th><td>Laboratório de Competência em Software Livre (LabLivre), Universidade de Brasília (UnB)</td></tr>
    <tr><th>Parceria</th><td>Secretaria Nacional de Participação Social (SNPS), Secretaria-Geral da Presidência da República, por meio de Termo de Execução Descentralizada</td></tr>
    <tr><th>Projetos</th><td>Participa (plataforma multi-organização) e participação multicanal (API OP-BP, painel e app de participação)</td></tr>
    <tr><th>Base tecnológica</th><td>Participa: Decidim 0.32.1, Rails 8.1, AGPLv3. Participação multicanal: Python, FastAPI, Next.js</td></tr>
    <tr><th>Código-fonte</th><td>gitlab.com/lappis-unb/decidimbr/participa · gitlab.com/lappis-unb/decidimbr/multi-channel-participation</td></tr>
    <tr><th>Fontes do conteúdo</th><td>Código dos repositórios <code>participa</code>, <code>multi-channel-participation</code> e das gems do Brasil Participativo, código do Decidim 0.32.1 e API pública do GitLab</td></tr>
    <tr><th>Uso de IA</th><td>Produzido com apoio de IA generativa (Claude Code, modelo Claude Opus 5.5), sob direção e revisão da equipe. Ver Sobre › Uso de IA</td></tr>
    <tr><th>Licença</th><td>Conteúdo sob Creative Commons Atribuição 4.0 Internacional (CC BY 4.0), exceto logos e marcas institucionais. Código desta documentação e software Participa: AGPLv3</td></tr>
    <tr><th>Versão on-line</th><td>{{ config.site_url }}</td></tr>
    <tr><th>Contato</th><td>brasilparticipativo@presidencia.gov.br · decidim@unb.br</td></tr>
  </table>

  <h2 class="bp-rosto__heading">Como citar</h2>
  <p class="bp-rosto__cite">LABLIVRE. <strong>Brasil Participativo SaaS</strong>: documentação técnica do Participa e da participação multicanal. Brasília: Universidade de Brasília, <span class="bp-year">2026</span>. Disponível em: {{ config.site_url }}. Acesso em: <span class="bp-access">—</span>.</p>
</div>

<div class="bp-front bp-front--apresentacao">
  <h1 class="bp-apresentacao__title">Apresentação</h1>

  <p>O Brasil Participativo SaaS oferece a plataforma de participação do governo federal a estados, municípios e órgãos, e leva a participação para o WhatsApp e o Telegram. É formado por dois projetos de software livre do LabLivre/UnB: o Participa, plataforma multi-organização sobre o Decidim 0.32.1, e a participação multicanal, cujo núcleo é a API OP-BP.</p>

  <p>Este documento reúne, em português, o conhecimento técnico e operacional sobre os dois projetos. Ele é gerado a partir da versão on-line da documentação, que é atualizada continuamente com base no código-fonte. Em caso de divergência, vale a versão on-line.</p>

  <h2 class="bp-rosto__heading">Organização</h2>
  <table class="bp-ficha">
    <tr><th>Trilhas e novidades</th><td>Por onde começar em cada perfil e mudanças recentes</td></tr>
    <tr><th>Documentação</th><td>Visão geral, Participa e participação multicanal: arquitetura, módulos, implantação, configuração e banco de dados</td></tr>
    <tr><th>Transferência</th><td>Plano de transferência, inventário, operação, segurança, APIs, release, testes, atualização e decisões</td></tr>
    <tr><th>Inovação</th><td>O que mudou em relação ao Brasil Participativo e ao Decidim</td></tr>
    <tr><th>Estatísticas</th><td>Indicadores dos dois projetos de software livre</td></tr>
    <tr><th>Sobre</th><td>Origem e manutenção desta documentação</td></tr>
  </table>

  <h2 class="bp-rosto__heading">Para quem</h2>
  <table class="bp-ficha">
    <tr><th>Desenvolvedores</th><td>Participa, Participação multicanal e Banco de Dados</td></tr>
    <tr><th>Equipe receptora</th><td>Transferência e Documentação</td></tr>
    <tr><th>Equipes de operação</th><td>Implantação, Configuração e Operação e continuidade</td></tr>
    <tr><th>Gestores de processos</th><td>Órgãos e setores, Participação efêmera, Chatbot, Roteiros de conversa e Painel</td></tr>
    <tr><th>Gestão e pesquisa</th><td>Inovação e Estatísticas</td></tr>
  </table>

  <h2 class="bp-rosto__heading">Convenções</h2>
  <ul>
    <li>Caixas azuis trazem informações; verdes, dicas; amarelas, cuidados; vermelhas, riscos.</li>
    <li>Nomes de arquivos, tabelas, variáveis e comandos aparecem em <code>fonte monoespaçada</code>.</li>
    <li>Afirmações de desempenho são marcadas como <strong>medidas</strong> ou <strong>inferidas</strong>; o que não tem fonte é marcado <strong>a confirmar</strong>.</li>
    <li>Conteúdos em abas na versão on-line aparecem aqui em sequência, cada um com seu título.</li>
  </ul>
</div>
