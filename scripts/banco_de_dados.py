#!/usr/bin/env python3
"""Gera a seção "Participa › Banco de Dados" (dicionário de dados) a partir do db/schema.rb do participa.

Lê o schema e as migrações da branch main (mesmo clone usado por scripts/estatisticas.py) e:
  - agrupa as tabelas por domínio;
  - lista colunas, tipos, nulidade, padrões, índices e referências;
  - infere referências por convenção (decidim_<entidade>_id) além das chaves estrangeiras declaradas;
  - identifica a origem de cada tabela e coluna (Decidim, engines do Participa ou gems) pelas migrações;
  - aponta tabelas e colunas do schema.rb que nenhuma migração cria.

Uso:
  python3 scripts/banco_de_dados.py
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from estatisticas import P, PROJETOS, ROOT, git, sync_repo  # noqa: E402

BRANCH = "main"
CORE_URL = "https://gitlab.com/lappis-unb/decidimbr/participa/-/blob/main"

# --------------------------------------------------------------------------- domínios

DOMAINS = [
    ("organizacao-usuarios", "Organização, usuários e autenticação", "material/account-key",
     "Organizações, usuários, administradores de sistema, identidades de login (gov.br), autorizações, "
     "tokens de API e o mapa de schemas do multi-organização.",
     [r"^decidim_organizations$", r"^decidim_system_admins$", r"^decidim_users$", r"^decidim_identities$",
      r"^decidim_authorization", r"^decidim_user_group_memberships$", r"^decidim_impersonation_logs$",
      r"^decidim_verifications_", r"^decidim_api_", r"^oauth_", r"^apartment_", r"^decidim_toggle_",
      r"^decidim_private_exports$", r"^decidim_members$"]),
    ("processos-instancias", "Processos participativos e instâncias", "material/sitemap",
     "Processos participativos, etapas, grupos e assembleias, chamadas de instâncias na interface.",
     [r"^decidim_participatory_process", r"^decidim_participatory_space_", r"^decidim_assembl"]),
    ("orgaos-setores", "Órgãos e setores", "material/domain",
     "Hierarquia de governo Órgão → Setor da gem decidim-government_spaces: tipos de órgão, membros, "
     "convites e atribuição de processos a setores.",
     [r"^decidim_government_spaces"]),
    ("outros-espacos", "Conferências, iniciativas e eleições", "material/account-group",
     "Espaços e módulos do Decidim instalados explicitamente no Participa: conferências, iniciativas e eleições.",
     [r"^decidim_conference", r"^decidim_initiatives", r"^decidim_elections_"]),
    ("componentes-conteudo", "Componentes, taxonomia, conteúdo e arquivos", "material/puzzle",
     "Componentes de cada espaço, taxonomias, categorias, escopos, áreas, anexos, blocos de conteúdo, páginas "
     "estáticas, modelos de processo, newsletters e arquivos do ActiveStorage.",
     [r"^decidim_components$", r"^decidim_categor", r"^decidim_taxonom", r"^decidim_scope", r"^decidim_area",
      r"^decidim_resource_", r"^decidim_attachment", r"^decidim_content_block", r"^decidim_hashtags$",
      r"^decidim_share_tokens$", r"^decidim_short_links$", r"^decidim_searchable_resources$",
      r"^decidim_static_page", r"^decidim_contextual_help_sections$", r"^decidim_editor_images$",
      r"^decidim_newsletters$", r"^active_storage_", r"^community_template_"]),
    ("propostas", "Propostas e texto participativo", "material/lightbulb-on",
     "Propostas, votos, emendas, coautorias, rascunhos colaborativos, avaliação e o componente de texto "
     "participativo (parágrafos e devolutivas).",
     [r"^decidim_proposals_", r"^decidim_amendments$", r"^decidim_coauthorships$", r"^decidim_participatory_texts_"]),
    ("reunioes", "Reuniões e eventos", "material/calendar",
     "Reuniões, inscrições, convites, pautas e enquetes ao vivo.",
     [r"^decidim_meetings_"]),
    ("formularios", "Formulários", "material/form-select",
     "Questionários, perguntas, condições de exibição e respostas dos componentes de formulário.",
     [r"^decidim_forms_", r"^decidim_surveys_"]),
    ("interacao", "Comentários e interação", "material/comment-multiple",
     "Comentários, curtidas, seguidores, notificações, mensagens privadas, lembretes e conquistas.",
     [r"^decidim_comments_", r"^decidim_likes$", r"^decidim_endorsements$", r"^decidim_follows$",
      r"^decidim_notifications$", r"^decidim_messaging_", r"^decidim_reminder", r"^decidim_gamification_"]),
    ("moderacao-auditoria", "Moderação, auditoria e métricas", "material/shield-search",
     "Denúncias, moderações, bloqueios de usuários, log de ações administrativas, versões (PaperTrail) "
     "e métricas agregadas.",
     [r"^decidim_moderations$", r"^decidim_reports$", r"^decidim_user_moderations$", r"^decidim_user_reports$",
      r"^decidim_user_blocks$", r"^decidim_action_logs$", r"^versions$", r"^decidim_metrics$"]),
    ("outros-modulos", "Orçamentos, debates, blog e outros módulos", "material/view-grid-plus",
     "Demais módulos nativos do Decidim: orçamentos, prestação de contas, debates, blog e páginas, "
     "mais a tabela legada de sorteios.",
     [r"^decidim_budgets_", r"^decidim_accountability_", r"^decidim_debates_", r"^decidim_blogs_",
      r"^decidim_pages_", r"^decidim_sortitions_"]),
    ("chatbot", "Chatbot", "material/whatsapp",
     "Tabelas do módulo decidim-chatbot: provedores de mensageria, conversas, eventos, roteiro e links de "
     "identificação.",
     [r"^decidim_chatbot_"]),
]
MAP_MIN_REFS = 4
MAP_LABELS = {
    "organizacao-usuarios": "Organização<br/>e usuários", "processos-instancias": "Processos<br/>e instâncias",
    "orgaos-setores": "Órgãos<br/>e setores", "outros-espacos": "Conferências,<br/>iniciativas, eleições",
    "componentes-conteudo": "Componentes<br/>e conteúdo", "propostas": "Propostas", "reunioes": "Reuniões",
    "formularios": "Formulários", "interacao": "Interação", "moderacao-auditoria": "Moderação<br/>e auditoria",
    "outros-modulos": "Outros<br/>módulos", "chatbot": "Chatbot",
}
OTHER_DOMAIN = ("outras", "Outras tabelas", "material/table", "Tabelas que não se encaixam nos demais domínios.", [])

TABLE_DOCS = {
    "decidim_organizations": "Organização. Cada host atende uma organização; no Participa, cada schema guarda uma única linha desta tabela.",
    "decidim_users": "Participantes e grupos de usuários (coluna `type`). Guarda perfil, preferências de notificação e `extended_data`.",
    "decidim_identities": "Identidades de login externo (OmniAuth). Para o gov.br, `provider = 'govbr'` e `uid` é o CPF.",
    "decidim_authorizations": "Autorizações (verificações) concedidas a usuários.",
    "decidim_system_admins": "Administradores do painel `/system`.",
    "decidim_participatory_processes": "Processos participativos. `automatic_step_activation` liga a troca automática de etapa (decidim-govbr).",
    "decidim_participatory_process_steps": "Etapas (fases) de cada processo.",
    "decidim_participatory_process_groups": "Grupos de processos.",
    "decidim_participatory_process_user_roles": "Papéis de usuários em processos (admin, moderador, avaliador, colaborador).",
    "decidim_assemblies": "Assembleias, chamadas de instâncias na interface. `parent_id` forma a hierarquia de sub-instâncias.",
    "decidim_assemblies_types": "Tipos de assembleia.",
    "decidim_assembly_members": "Membros de uma assembleia.",
    "decidim_assembly_user_roles": "Papéis de usuários em assembleias.",
    "decidim_components": "Componentes de cada espaço (`manifest_name`: proposals, meetings, surveys, participatory_texts…). Polimórfico em `participatory_space`.",
    "decidim_scopes": "Escopos (territoriais ou temáticos).",
    "decidim_scope_types": "Tipos de escopo.",
    "decidim_areas": "Áreas.",
    "decidim_categories": "Categorias legadas do Decidim. O Participa usa as da gem decidim-categories.",
    "decidim_categorizations": "Associação legada entre recursos e categorias do Decidim.",
    "decidim_categories_categories": "Categorias hierárquicas por espaço participativo, com lixeira (gem decidim-categories).",
    "decidim_categories_categorizations": "Associação entre recursos e categorias da gem decidim-categories.",
    "decidim_taxonomies": "Taxonomias do Decidim 0.32. A raiz \"Categorias\" e os tipos de processo são criados pela decidim-govbr.",
    "decidim_taxonomizations": "Associação entre recursos e taxonomias.",
    "decidim_attachments": "Anexos de espaços e recursos.",
    "decidim_attachment_collections": "Pastas (coleções) de anexos.",
    "decidim_content_blocks": "Blocos de conteúdo de páginas (home da organização e de espaços).",
    "decidim_static_pages": "Páginas estáticas (`/pages`), como termos de uso e tutoriais.",
    "decidim_static_page_topics": "Tópicos que agrupam páginas estáticas.",
    "decidim_newsletters": "Newsletters.",
    "decidim_resource_links": "Ligações entre recursos (ex.: proposta ↔ reunião).",
    "decidim_searchable_resources": "Índice de busca global.",
    "decidim_proposals_proposals": "Propostas. No Decidim, também representam parágrafos do texto participativo do componente de propostas.",
    "decidim_proposals_proposal_votes": "Votos em propostas.",
    "decidim_proposals_participatory_texts": "Texto participativo do componente de propostas do Decidim (o Participa usa o componente próprio).",
    "decidim_participatory_texts_paragraphs": "Parágrafos do componente Texto participativo (gem decidim-participatory_texts).",
    "decidim_participatory_texts_comment_feedbacks": "Devolutiva a um comentário de parágrafo: incorporado, parcialmente, não incorporado ou aguardando análise.",
    "decidim_proposals_proposal_notes": "Notas privadas de administradores sobre propostas.",
    "decidim_proposals_collaborative_drafts": "Rascunhos colaborativos de propostas.",
    "decidim_proposals_valuation_assignments": "Atribuição de propostas a avaliadores.",
    "decidim_amendments": "Emendas entre recursos emendáveis (propostas).",
    "decidim_coauthorships": "Coautoria polimórfica de recursos.",
    "decidim_meetings_meetings": "Reuniões e eventos.",
    "decidim_meetings_registrations": "Inscrições em reuniões.",
    "decidim_forms_questionnaires": "Questionários. Polimórfico em `questionnaire_for` (formulário, reunião…).",
    "decidim_forms_questions": "Perguntas de um questionário.",
    "decidim_forms_responses": "Respostas a perguntas (chamadas de `answers` antes do Decidim 0.32).",
    "decidim_forms_response_options": "Opções de resposta.",
    "decidim_forms_response_choices": "Opções escolhidas em uma resposta.",
    "decidim_forms_display_conditions": "Condições de exibição entre perguntas.",
    "decidim_surveys_surveys": "Componente de formulário (enquete).",
    "decidim_comments_comments": "Comentários. `decidim_commentable_*` aponta para o recurso e `decidim_root_commentable_*` para a raiz da conversa.",
    "decidim_comments_comment_votes": "Votos (positivo/negativo) em comentários.",
    "decidim_likes": "Curtidas em recursos (chamadas de apoios antes do Decidim 0.32).",
    "decidim_follows": "Usuários que seguem recursos.",
    "decidim_notifications": "Notificações dos usuários.",
    "decidim_moderations": "Moderação de um recurso denunciado (contagem de denúncias, data de ocultação).",
    "decidim_reports": "Denúncias individuais ligadas a uma moderação.",
    "decidim_action_logs": "Log de ações administrativas e de participantes.",
    "versions": "Histórico de versões (PaperTrail).",
    "decidim_metrics": "Métricas agregadas por dia.",
    "apartment_distribution_keys": "Mapa entre host e schema: cada organização tem um schema PostgreSQL com nome UUID. Única tabela que fica no schema `public`.",
    "decidim_toggle_organization_module_configs": "Configurações de módulos por organização, editadas em abas do painel `/system` (gem decidim-toggle).",
    "community_template_sources": "Origem dos modelos de processo usados ou publicados pela organização (gem decidim-community_templates).",
    "community_template_uses": "Recursos criados a partir de um modelo de processo.",
    "decidim_government_spaces": "Órgãos e setores (herança por `type`: Organ, Sector); `parent_id` liga o setor ao órgão.",
    "decidim_government_spaces_organ_types": "Tipos de órgão.",
    "decidim_government_spaces_memberships": "Administradores com escopo de um órgão ou setor.",
    "decidim_government_spaces_pending_invitations": "Convites pendentes para administrar um órgão ou setor. Nenhuma migração de `main` cria esta tabela.",
    "decidim_government_spaces_process_assignments": "Setor responsável por cada processo participativo (um por processo).",
    "decidim_chatbot_broker_configs": "Provedor de mensageria da organização (hoje só o WhatsApp do SERPRO), com segredos cifrados e dados do webhook.",
    "decidim_chatbot_conversations": "Conversa de uma pessoa (telefone) com o chatbot: estado do roteiro, participante vinculado e voto confirmado.",
    "decidim_chatbot_events": "Mensagens recebidas e enviadas, com situação (pendente, processada, ignorada, falha, enviada).",
    "decidim_chatbot_flow_settings": "Roteiro da organização: textos editáveis, componente de propostas, modo de identificação, rascunho e versão publicada.",
    "decidim_chatbot_identity_links": "Links de identificação enviados na conversa: só o resumo do token, validade de 1 hora, uso único.",
    "active_storage_blobs": "Metadados dos arquivos enviados (o conteúdo fica no storage).",
    "active_storage_attachments": "Associação polimórfica entre registros e arquivos.",
    "decidim_budgets_budgets": "Orçamentos de um componente.",
    "decidim_budgets_projects": "Projetos votáveis de um orçamento.",
    "decidim_budgets_orders": "Votos (carrinhos) de participantes num orçamento.",
    "decidim_debates_debates": "Debates.",
    "decidim_blogs_posts": "Posts do blog (notícias).",
    "decidim_pages_pages": "Conteúdo do componente Páginas.",
    "decidim_accountability_results": "Resultados acompanhados na prestação de contas.",
    "decidim_sortitions_sortitions": "Sorteios de propostas (tabela legada; o módulo não existe no Decidim 0.32).",
}

# Engines versionadas no próprio repositório (sufixo da migração copiada).
REPO_ENGINES = {"decidim_govbr", "decidim_chatbot"}
LABLIVRE_GEMS = {"decidim_government_spaces", "decidim_categories", "decidim_community_templates", "decidim_apartment",
                 "decidim_participatory_texts", "decidim_questionnaires"}
COMMUNITY_GEMS = {"decidim_toggle": "decidim-toggle", "decidim_ephemeral_participation": "decidim-ephemeral_participation"}
# Gems que acrescentam o próprio db/migrate em tempo de boot: as migrações não estão copiadas no app.
GEM_TABLES = {r"^decidim_participatory_texts_": "lablivre:decidim-participatory_texts"}
GEM_COLUMNS = {("decidim_forms_questions", "max_files"): "lablivre:decidim-questionnaires"}
# Texto de todas as migrações lidas: um nome que não aparece em nenhuma é divergência do schema.rb.
MIGRATION_TEXT: list[str] = []


# --------------------------------------------------------------------------- schema.rb

def parse_schema(text: str) -> dict:
    version = re.search(r"define\(version: ([\d_]+)\)", text)
    extensions = re.findall(r'enable_extension "([^"]+)"', text)
    tables: dict[str, dict] = {}
    current = None
    for line in text.splitlines():
        m = re.match(r'\s*create_table "([^"]+)"(.*) do \|t\|', line)
        if m:
            opts = m.group(2)
            pk = "não" if "id: false" in opts else ("serial" if "id: :serial" in opts else "bigint")
            current = {"name": m.group(1), "pk": pk, "columns": [], "indexes": []}
            if pk != "não":
                current["columns"].append({"name": "id", "type": "serial" if pk == "serial" else "bigint",
                                           "null": False, "default": None, "pk": True, "array": False})
            tables[current["name"]] = current
            continue
        if current is None:
            fk = re.match(r'\s*add_foreign_key "([^"]+)", "([^"]+)"(.*)', line)
            if fk:
                col = re.search(r'column: "([^"]+)"', fk.group(3))
                singular = fk.group(2).rsplit("_", 1)
                tables.setdefault(fk.group(1), {"fks": []})
                tables[fk.group(1)].setdefault("fks", []).append(
                    {"to": fk.group(2), "column": col.group(1) if col else f"{fk.group(2).rstrip('s')}_id"})
            continue
        if re.match(r"\s*end\s*$", line):
            current = None
            continue
        idx = re.match(r'\s*t\.index (\[[^\]]*\]|"[^"]*"), name: "([^"]+)"(.*)', line)
        if idx:
            cols = re.findall(r'"([^"]+)"', idx.group(1)) if idx.group(1).startswith("[") else [idx.group(1).strip('"')]
            current["indexes"].append({"name": idx.group(2), "columns": cols, "unique": "unique: true" in idx.group(3),
                                       "using": (re.search(r"using: :(\w+)", idx.group(3)) or [None, None])[1],
                                       "where": (re.search(r'where: "([^"]+)"', idx.group(3)) or [None, None])[1]})
            continue
        col = re.match(r'\s*t\.(\w+) "([^"]+)"(.*)', line)
        if col:
            rest = col.group(3)
            default = re.search(r"default: (\{\}|\[\]|-?[\d.]+|true|false|\"[^\"]*\"|-> \{[^}]*\})", rest)
            current["columns"].append({
                "name": col.group(2), "type": col.group(1), "null": "null: false" not in rest,
                "default": default.group(1) if default else None, "pk": False, "array": "array: true" in rest,
            })
    # tabelas criadas pelo setdefault de FKs antes de create_table: mescla
    fks = defaultdict(list)
    for name, t in list(tables.items()):
        if "fks" in t:
            fks[name].extend(t.pop("fks"))
        if "columns" not in t:
            del tables[name]
    return {"version": version.group(1) if version else None, "extensions": extensions, "tables": tables, "fks": fks}


# --------------------------------------------------------------------------- origem pelas migrações

def migration_origin(filename: str) -> tuple[str, str]:
    m = re.match(r"^(\d+)_([a-z0-9_]+?)(?:\.([a-z0-9_]+))?\.rb$", filename)
    if not m:
        return ("?", filename)
    engine = m.group(3)
    if engine is None or engine in REPO_ENGINES:
        return ("participa", m.group(2))
    if engine in LABLIVRE_GEMS:
        return ("lablivre:" + engine.replace("decidim_", "decidim-"), m.group(2))
    if engine in COMMUNITY_GEMS:
        return ("comunidade:" + COMMUNITY_GEMS[engine], m.group(2))
    return ("decidim", m.group(2))


def trace_origins(repo: Path) -> tuple[dict, dict, Counter]:
    """Retorna origem de tabelas e colunas: {(tabela, coluna): (origem, arquivo)}."""
    files = sorted(f.split("/")[-1] for f in git(repo, "ls-tree", "--name-only", f"{BRANCH}:db/migrate").splitlines())
    col_origin: dict[tuple[str, str], tuple[str, str]] = {}
    table_origin: dict[str, tuple[str, str]] = {}
    per_origin = Counter()
    sym = r"[:\"']?([a-z0-9_]+)[\"']?"
    for f in files:
        origin, _ = migration_origin(f)
        per_origin[origin.split(":")[0]] += 1
        src = git(repo, "show", f"{BRANCH}:db/migrate/{f}")
        MIGRATION_TEXT.append(src)
        block_table = None
        for line in src.splitlines():
            s = line.strip()
            m = re.match(rf"create_table {sym}", s)
            if m:
                block_table = m.group(1)
                table_origin.setdefault(block_table, (origin, f))
                col_origin.setdefault((block_table, "id"), (origin, f))
                continue
            m = re.match(rf"change_table {sym}", s)
            if m:
                block_table = m.group(1)
                continue
            m = re.match(rf"rename_table {sym},\s*{sym}", s)
            if m:
                old, new = m.group(1), m.group(2)
                if old in table_origin:
                    table_origin[new] = table_origin[old]
                for (t, c), v in list(col_origin.items()):
                    if t == old:
                        col_origin[(new, c)] = v
                continue
            if block_table:
                m = re.match(rf"t\.(?:references|belongs_to) {sym}(.*)", s)
                if m:
                    col_origin.setdefault((block_table, m.group(1) + "_id"), (origin, f))
                    if "polymorphic" in m.group(2):
                        col_origin.setdefault((block_table, m.group(1) + "_type"), (origin, f))
                    continue
                if s.startswith("t.timestamps"):
                    for c in ("created_at", "updated_at"):
                        col_origin.setdefault((block_table, c), (origin, f))
                    continue
                m = re.match(rf"t\.rename {sym},\s*{sym}", s)
                if m and (block_table, m.group(1)) in col_origin:
                    col_origin[(block_table, m.group(2))] = col_origin[(block_table, m.group(1))]
                    continue
                m = re.match(rf"t\.(?!index|remove|rename)\w+ {sym}", s)
                if m:
                    col_origin.setdefault((block_table, m.group(1)), (origin, f))
                    continue
                if s == "end":
                    block_table = None
                    continue
            m = re.match(rf"add_column {sym},\s*{sym}", s)
            if m:
                col_origin.setdefault((m.group(1), m.group(2)), (origin, f))
                continue
            m = re.match(rf"add_(?:reference|belongs_to) {sym},\s*{sym}(.*)", s)
            if m:
                col_origin.setdefault((m.group(1), m.group(2) + "_id"), (origin, f))
                if "polymorphic" in m.group(3):
                    col_origin.setdefault((m.group(1), m.group(2) + "_type"), (origin, f))
                continue
            m = re.match(rf"add_timestamps {sym}", s)
            if m:
                for c in ("created_at", "updated_at"):
                    col_origin.setdefault((m.group(1), c), (origin, f))
                continue
            m = re.match(rf"rename_column {sym},\s*{sym},\s*{sym}", s)
            if m and (m.group(1), m.group(2)) in col_origin:
                col_origin[(m.group(1), m.group(3))] = col_origin[(m.group(1), m.group(2))]
    return table_origin, col_origin, per_origin


def origin_label(origin: str | None) -> str:
    if not origin:
        return "—"
    if origin == "participa":
        return ":flag_br: Participa"
    if origin == "decidim":
        return "Decidim"
    kind, gem = origin.split(":", 1)
    return f"`{gem}` (LabLivre)" if kind == "lablivre" else f"`{gem}`"


# --------------------------------------------------------------------------- referências

def domain_of(table: str) -> tuple:
    for d in DOMAINS:
        if any(re.search(p, table) for p in d[4]):
            return d
    return OTHER_DOMAIN


def module_prefix(table: str) -> str:
    parts = table.split("_")
    return "_".join(parts[:2]) if table.startswith("decidim_") else parts[0]


def infer_references(schema: dict) -> dict:
    tables = schema["tables"]
    names = set(tables)
    refs: dict[tuple[str, str], tuple[str, str]] = {}
    for src, fks in schema["fks"].items():
        for fk in fks:
            refs[(src, fk["column"])] = (fk["to"], "fk")
    special = {
        "decidim_organization_id": "decidim_organizations", "decidim_user_id": "decidim_users",
        "decidim_user_group_id": "decidim_users", "decidim_component_id": "decidim_components",
        "decidim_scope_id": "decidim_scopes", "decidim_area_id": "decidim_areas",
        "decidim_category_id": "decidim_categories", "decidim_scope_type_id": "decidim_scope_types",
        "decidim_participatory_process_id": "decidim_participatory_processes",
        "decidim_participatory_process_type_id": "decidim_participatory_process_types",
        "decidim_participatory_process_group_id": "decidim_participatory_process_groups",
        "decidim_assembly_id": "decidim_assemblies", "decidim_assemblies_type_id": "decidim_assemblies_types",
        "decidim_conference_id": "decidim_conferences", "blob_id": "active_storage_blobs",
        "decidim_proposal_id": "decidim_proposals_proposals", "decidim_meeting_id": "decidim_meetings_meetings",
        "decidim_questionnaire_id": "decidim_forms_questionnaires", "decidim_question_id": "decidim_forms_questions",
        "decidim_moderation_id": "decidim_moderations", "decidim_budgets_budget_id": "decidim_budgets_budgets",
        "decidim_project_id": "decidim_budgets_projects", "decidim_order_id": "decidim_budgets_orders",
        "decidim_answer_id": "decidim_forms_answers", "decidim_answer_option_id": "decidim_forms_answer_options",
        "invited_by_id": "decidim_users", "decidim_reminder_id": "decidim_reminders",
        "attachment_collection_id": "decidim_attachment_collections", "decidim_initiative_id": "decidim_initiatives",
        "decidim_consultation_id": "decidim_consultations", "decidim_consultations_question_id": "decidim_consultations_questions",
        "decidim_homes_home_id": "decidim_homes_homes", "decidim_comment_id": "decidim_comments_comments",
    }
    for t, info in tables.items():
        cols = {c["name"] for c in info["columns"]}
        for c in info["columns"]:
            name = c["name"]
            if not name.endswith("_id") or name == "id" or (t, name) in refs:
                continue
            base = name[:-3]
            if base + "_type" in cols:
                refs[(t, name)] = (base + "_type", "poly")
                continue
            if name == "parent_id":
                refs[(t, name)] = (t, "conv")
                continue
            target = special.get(name)
            if not target:
                stem = base.replace("decidim_", "", 1)
                cands = [n for n in names if n in (f"decidim_{stem}s", f"decidim_{stem}es") or
                         n.endswith(f"_{stem}s") or n.endswith(f"_{stem}es")]
                same = [n for n in cands if module_prefix(n) == module_prefix(t)]
                pick = same if len(same) == 1 else cands if len(cands) == 1 else []
                target = pick[0] if pick else None
            if target and target in names:
                refs[(t, name)] = (target, "conv")
    return refs


# --------------------------------------------------------------------------- renderização

def esc(text: str) -> str:
    return str(text).replace("|", "\\|")


def anchor(table: str) -> str:
    return table.replace("_", "-")


def col_type(c: dict) -> str:
    t = c["type"]
    if c["array"]:
        t += "[]"
    return f"`{t}`"


def note_for(table: str, c: dict, refs: dict, page_of: dict) -> str:
    notes = []
    if c["pk"]:
        notes.append("chave primária")
    ref = refs.get((table, c["name"]))
    if ref:
        target, kind = ref
        if kind == "poly":
            notes.append(f"polimórfico (tipo em `{target}`)")
        else:
            link = f"[`{target}`]({page_of[target]}#{anchor(target)})" if target in page_of else f"`{target}`"
            notes.append(("FK → " if kind == "fk" else "→ ") + link)
    if c["type"] == "jsonb" and c["name"] in ("title", "description", "body", "name", "subtitle", "short_description",
                                               "announcement", "answer", "summary", "about", "content"):
        notes.append("traduzível (`{\"pt-BR\": …}`)")
    if c["name"].endswith("_count"):
        notes.append("contador em cache")
    return "; ".join(notes)


def wrap_label(name: str, width: int = 13) -> str:
    """Quebra o nome da tabela em linhas curtas, nos sublinhados."""
    lines, cur = [], ""
    for part in name.split("_"):
        cand = f"{cur}_{part}" if cur else part
        if len(cand) > width and cur:
            lines.append(cur + "_")
            cur = part
        else:
            cur = cand
    lines.append(cur)
    return "<br/>".join(lines)


def node_label(table: str) -> str:
    return wrap_label(re.sub(r"^decidim_", "", table))


def components_of(edges: set) -> list[set]:
    adj = defaultdict(set)
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    seen, comps = set(), []
    for n in sorted(adj):
        if n in seen:
            continue
        stack, comp = [n], set()
        while stack:
            x = stack.pop()
            if x not in comp:
                comp.add(x)
                stack.extend(adj[x])
        seen |= comp
        comps.append(comp)
    return comps


def pick_direction(nodes: set, edges: set) -> str:
    """Escolhe LR ou TB pela menor largura estimada (o diagrama cresce na vertical)."""
    children = defaultdict(set)
    parents = defaultdict(set)
    for a, b in edges:
        children[a].add(b)
        parents[b].add(a)
    level = {n: 0 for n in nodes if not parents[n]} or {min(nodes): 0}
    frontier = list(level)
    for _ in range(len(nodes)):
        nxt = []
        for n in frontier:
            for c in children[n]:
                if level.get(c, -1) < level[n] + 1 and level[n] + 1 < len(nodes):
                    level[c] = level[n] + 1
                    nxt.append(c)
        frontier = nxt
    for n in nodes:
        level.setdefault(n, 0)
    per_level = Counter(level.values())
    longest = max(len(line) for n in nodes for line in node_label(n).split("<br/>"))
    node_w = longest * 7.5 + 50
    width_lr = (max(level.values()) + 1) * (node_w + 40)
    width_tb = max(per_level.values()) * (node_w + 20)
    return "LR" if width_lr <= width_tb else "TB"


def relationship_diagrams(tables: list[str], refs: dict) -> list[tuple[str, str]]:
    """Um diagrama por grupo de tabelas conectadas; pares soltos vão juntos num diagrama empilhado."""
    tset = set(tables)
    edges = set()
    for (src, _), (dst, kind) in refs.items():
        if kind != "poly" and src in tset and dst in tset and src != dst:
            edges.add((dst, src))
    if not edges:
        return []
    diagrams, pairs = [], []
    comps = sorted(components_of(edges), key=lambda c: (-len(c), min(c)))
    for comp in comps:
        comp_edges = sorted((a, b) for a, b in edges if a in comp)
        if len(comp) <= 2:
            pairs.extend(comp_edges)
            continue
        roots = sorted({a for a, _ in comp_edges} - {b for _, b in comp_edges}) or [min(comp)]
        title = ", ".join(f"`{r}`" for r in roots)
        lines = ["```mermaid", f"flowchart {pick_direction(comp, set(comp_edges))}"]
        lines += [f'    {n}["{node_label(n)}"]' for n in sorted(comp)]
        lines += [f"    {a} --> {b}" for a, b in comp_edges]
        lines.append("```")
        diagrams.append((f"A partir de {title}", "\n".join(lines)))
    if pairs:
        nodes = sorted({n for e in pairs for n in e})
        lines = ["```mermaid", "flowchart LR"]
        lines += [f'    {n}["{node_label(n)}"]' for n in nodes]
        lines += [f"    {a} --> {b}" for a, b in pairs]
        lines.append("```")
        diagrams.append(("Outras relações", "\n".join(lines)))
    return diagrams


def render_domain(domain: tuple, tables: list[str], schema: dict, refs: dict, page_of: dict,
                  table_origin: dict, col_origin: dict, meta: dict) -> str:
    slug, title, icon, desc, _ = domain
    out = [f"---\ntitle: {title}\nicon: {icon}\n---\n",
           f"<!-- Gerado por scripts/banco_de_dados.py em {meta['generated']}. Não edite à mão. -->\n",
           f"# {title}\n", desc + "\n"]
    out.append(f"**{len(tables)} tabelas.** Schema versão `{meta['version']}`. "
               "Legenda da coluna **Referência**: *FK* = chave estrangeira declarada no banco; "
               "*→* = referência por convenção de nome (sem restrição no banco).\n")
    diagrams = relationship_diagrams(tables, refs)
    if diagrams:
        out.append("## Relacionamentos\n")
        out.append("Cada seta vai da tabela referenciada para a tabela que guarda a referência. Referências para "
                   "outros domínios aparecem na coluna **Referência** das tabelas abaixo.\n")
        for title, diagram in diagrams:
            if len(diagrams) > 1:
                out.append(f"**{title}**\n")
            out.append(diagram + "\n")
    out.append("## Tabelas\n")
    out.append("| Tabela | Descrição | Colunas | Origem |\n|---|---|---:|---|")
    for t in tables:
        o = table_origin.get(t, (None, None))[0]
        out.append(f"| [`{t}`](#{anchor(t)}) | {esc(TABLE_DOCS.get(t, '—'))} | {len(schema['tables'][t]['columns'])} | {origin_label(o)} |")
    out.append("")
    for t in tables:
        info = schema["tables"][t]
        o_table = table_origin.get(t, (None, None))[0]
        out.append(f"### `{t}` {{ #{anchor(t)} }}\n")
        if t in TABLE_DOCS:
            out.append(TABLE_DOCS[t] + "\n")
        out.append(f"Origem: {origin_label(o_table)}.\n")
        out.append("| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |\n|---|---|:---:|---|---|---|")
        for c in info["columns"]:
            o, f = col_origin.get((t, c["name"]), (None, None))
            origin = origin_label(o) if o != o_table else ""
            if o == "participa" and f:
                origin = f"[:flag_br: Participa]({CORE_URL}/db/migrate/{f} \"{f}\")"
            out.append(f"| `{c['name']}` | {col_type(c)} | {'sim' if c['null'] else 'não'} | "
                       f"{('`' + esc(c['default']) + '`') if c['default'] is not None else ''} | "
                       f"{note_for(t, c, refs, page_of)} | {origin} |")
        if info["indexes"]:
            out.append(f"\n??? note \"Índices ({len(info['indexes'])})\"\n")
            out.append("    | Nome | Colunas | Único | Tipo |\n    |---|---|:---:|---|")
            for i in info["indexes"]:
                cols = ", ".join(f"`{esc(c)}`" for c in i["columns"])
                extra = (i["using"] or "btree") + (f" (parcial: `{esc(i['where'])}`)" if i["where"] else "")
                out.append(f"    | `{i['name']}` | {cols} | {'sim' if i['unique'] else ''} | {extra} |")
        out.append("")
    return "\n".join(out) + "\n"


def render_index(schema: dict, groups: dict, refs: dict, page_of: dict, table_origin: dict, col_origin: dict,
                 per_origin: Counter, meta: dict) -> str:
    tables = schema["tables"]
    n_cols = sum(len(t["columns"]) for t in tables.values())
    n_idx = sum(len(t["indexes"]) for t in tables.values())
    n_fk = sum(len(v) for v in schema["fks"].values())
    n_conv = sum(1 for v in refs.values() if v[1] == "conv")
    n_poly = sum(1 for v in refs.values() if v[1] == "poly")
    types = Counter(c["type"] for t in tables.values() for c in t["columns"])
    out = ["---\ntitle: Banco de Dados\nicon: material/database\n---\n",
           f"<!-- Gerado por scripts/banco_de_dados.py em {meta['generated']}. Não edite à mão. -->\n",
           "# Banco de Dados\n",
           "Dicionário de dados do PostgreSQL do Participa, gerado a partir do `db/schema.rb` e das "
           f"migrações da branch `main` do [participa]({CORE_URL.rsplit('/-/', 1)[0]}).\n",
           '!!! note "Um schema por organização"\n'
           "    O `schema.rb` descreve o schema `public`, que serve de modelo. Cada organização ganha um schema "
           "PostgreSQL próprio, com nome UUID, contendo todas estas tabelas. Só `apartment_distribution_keys` fica "
           "no `public`, e as extensões ficam no schema `shared_extensions`. "
           "Veja [Multi-organização](../multi-organizacao.md).\n",
           f'!!! info "Versão do schema: `{meta["version"]}`"\n    Gerado em {meta["generated_date"]}. '
           "Para atualizar, rode `python3 scripts/banco_de_dados.py`.\n"]
    out.append("## Em números\n")
    out.append("| Item | Quantidade |\n|---|---:|")
    out += [f"| Tabelas | {len(tables)} |", f"| Colunas | {n_cols} |", f"| Índices | {n_idx} |",
            f"| Chaves estrangeiras declaradas | {n_fk} |", f"| Referências por convenção (sem FK) | {n_conv} |",
            f"| Associações polimórficas | {n_poly} |",
            f"| Migrações em `db/migrate` | {sum(per_origin.values())} ({per_origin.get('participa', 0)} das engines do "
            f"repositório, {per_origin.get('lablivre', 0)} de gems do LabLivre, {per_origin.get('comunidade', 0)} de "
            "outras gems) |",
            f"| Extensões do PostgreSQL | {', '.join(f'`{e}`' for e in schema['extensions'])} |"]
    out.append("\n## Domínios\n")
    out.append('<div class="grid cards" markdown>\n')
    for d in DOMAINS + [OTHER_DOMAIN]:
        if d[0] not in groups:
            continue
        out.append(f"-   :{d[2].replace('/', '-')}:{{ .lg .middle }} **[{d[1]}]({d[0]}.md)**\n\n    ---\n\n"
                   f"    {d[3]}\n\n    {len(groups[d[0]])} tabelas\n")
    out.append("</div>\n")

    out.append("## Mapa entre domínios\n")
    out.append("Cada seta indica que tabelas de um domínio referenciam tabelas de outro. O número é a quantidade "
               "de colunas de referência.\n")
    flows = Counter()
    for (src, _), (dst, kind) in refs.items():
        if kind == "poly" or dst not in tables:
            continue
        a, b = domain_of(src)[0], domain_of(dst)[0]
        if a != b:
            flows[(a, b)] += 1
    titles = {d[0]: d[1] for d in DOMAINS + [OTHER_DOMAIN]}
    ids = {d[0]: f"D{i}" for i, d in enumerate(DOMAINS + [OTHER_DOMAIN])}
    strong = {k: n for k, n in flows.items() if n >= MAP_MIN_REFS}
    used = sorted({x for k in strong for x in k}, key=lambda d: [x[0] for x in DOMAINS + [OTHER_DOMAIN]].index(d))
    lines = ["```mermaid", "flowchart LR"]
    lines += [f'    {ids[d]}["{MAP_LABELS.get(d, titles[d])}"]' for d in used]
    lines += [f"    {ids[a]} -->|{n}| {ids[b]}" for (a, b), n in sorted(strong.items(), key=lambda x: -x[1])]
    lines.append("```")
    out.append("\n".join(lines) + "\n")
    out.append(f"O diagrama mostra só as ligações com {MAP_MIN_REFS} ou mais referências. A tabela abaixo traz todas.\n")
    out.append('??? note "Todas as referências entre domínios"\n')
    out.append("    | De | Para | Referências |\n    |---|---|---:|")
    out += [f"    | {titles[a]} | {titles[b]} | {n} |" for (a, b), n in sorted(flows.items(), key=lambda x: -x[1])]
    out.append("")

    out.append("## Convenções do Decidim\n")
    out.append(
        "| Convenção | Exemplo | Significado |\n|---|---|---|\n"
        "| Prefixo por módulo | `decidim_proposals_proposals` | `decidim_<módulo>_<entidade>`. Tabelas do núcleo usam só `decidim_<entidade>` |\n"
        "| Organização em tudo | `decidim_organization_id` | Ligação com a organização. No Participa, o isolamento entre organizações é feito por schema, e a coluna continua existindo |\n"
        "| Textos traduzíveis em JSONB | `title = {\"pt-BR\": \"…\", \"en\": \"…\"}` | Campos de texto exibidos ficam em `jsonb`, um valor por idioma. Consulta: `title->>'pt-BR'` |\n"
        "| Polimorfismo | `participatory_space_type` + `participatory_space_id` | A linha aponta para tabelas diferentes conforme o tipo (nome da classe Ruby) |\n"
        "| Referência sem FK | `decidim_component_id` | A maioria das relações não tem restrição no banco; a integridade é garantida pela aplicação |\n"
        "| Contadores em cache | `comments_count`, `proposal_votes_count` | Atualizados pela aplicação para evitar `COUNT(*)` |\n"
        "| Publicação | `published_at` | Nulo = rascunho / não publicado |\n"
        "| Ocultação por moderação | `decidim_moderations.hidden_at` | Recurso oculto continua no banco |\n"
        "| Configurações em JSONB | `decidim_components.settings` | Configurações globais e por etapa do componente |\n")

    out.append("## Tipos de coluna\n")
    out.append("| Tipo | Colunas |\n|---|---:|")
    out += [f"| `{k}` | {v} |" for k, v in types.most_common()]

    out.append("\n## O que não vem do Decidim\n")
    own_tables = sorted(t for t, (o, _) in table_origin.items() if o != "decidim" and t in tables)
    out.append(f"### Tabelas ({len(own_tables)})\n")
    out.append("| Tabela | Origem | Domínio |\n|---|---|---|")
    out += [f"| [`{t}`]({page_of[t]}#{anchor(t)}) | {origin_label(table_origin[t][0])} | {domain_of(t)[1]} |"
            for t in own_tables]
    own_cols = sorted(((t, c), o, f) for (t, c), (o, f) in col_origin.items()
                      if o != "decidim" and t in tables and t not in own_tables
                      and any(col["name"] == c for col in tables[t]["columns"]))
    out.append(f"\n### Colunas adicionadas a tabelas do Decidim ({len(own_cols)})\n")
    out.append("| Tabela | Coluna | Tipo | Origem |\n|---|---|---|---|")
    for (t, c), o, f in own_cols:
        col = next(col for col in tables[t]["columns"] if col["name"] == c)
        link = f" ([`{f}`]({CORE_URL}/db/migrate/{f}))" if f else ""
        out.append(f"| [`{t}`]({page_of[t]}#{anchor(t)}) | `{c}` | {col_type(col)} | {origin_label(o)}{link} |")

    corpus = "\n".join(MIGRATION_TEXT)
    orphan_tables = sorted(t for t in tables if t not in table_origin and t not in corpus)
    orphan_cols = sorted((t, c["name"]) for t, info in tables.items() if t in table_origin
                         for c in info["columns"] if (t, c["name"]) not in col_origin and c["name"] not in corpus)
    if orphan_tables or orphan_cols:
        out.append("\n## Divergências entre o `schema.rb` e as migrações\n")
        out.append("Itens do `schema.rb` cujo nome não aparece em nenhuma migração de `main` nem nas gems que trazem "
                   "as próprias migrações. Uma instalação nova com `db:schema:load` os cria; uma com `db:migrate`, não. "
                   "Confirme a origem antes da transferência.\n")
        out.append("| Tabela | Coluna |\n|---|---|")
        out += [f"| [`{t}`]({page_of[t]}#{anchor(t)}) | (tabela inteira) |" for t in orphan_tables]
        out += [f"| [`{t}`]({page_of[t]}#{anchor(t)}) | `{c}` |" for t, c in orphan_cols]
    out.append("\n## Como usar este dicionário\n")
    out.append("- Cada página de domínio lista as tabelas com colunas, tipos, padrões, referências e índices.\n"
               "- A coluna **Origem** mostra quando uma tabela ou coluna foi criada por uma engine do repositório "
               "(:flag_br: Participa) ou por uma gem, com link para a migração.\n"
               "- Exemplos de SQL estão em [Consultas úteis](consultas.md).\n")
    return "\n".join(out) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default=str(ROOT / "docs" / "banco-de-dados"))
    parser.add_argument("--cache", default=str(ROOT / ".cache" / "estatisticas"))
    args = parser.parse_args()

    P.update(PROJETOS["participa"], slug="participa")
    repo = sync_repo(Path(args.cache))
    schema = parse_schema(git(repo, "show", f"{BRANCH}:db/schema.rb"))
    table_origin, col_origin, per_origin = trace_origins(repo)
    for table, info in schema["tables"].items():
        gem = next((g for rx, g in GEM_TABLES.items() if re.search(rx, table)), None)
        if gem and table not in table_origin:
            table_origin[table] = (gem, None)
            for c in info["columns"]:
                col_origin.setdefault((table, c["name"]), (gem, None))
    for key, gem in GEM_COLUMNS.items():
        col_origin.setdefault(key, (gem, None))
    refs = infer_references(schema)

    groups: dict[str, list[str]] = defaultdict(list)
    for t in sorted(schema["tables"]):
        groups[domain_of(t)[0]].append(t)
    page_of = {t: f"{domain_of(t)[0]}.md" for t in schema["tables"]}

    now = datetime.now(timezone.utc).replace(microsecond=0)
    v = schema["version"] or ""
    meta = {"generated": now.isoformat(), "generated_date": now.strftime("%d/%m/%Y"),
            "version": v.replace("_", "")}
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.md").write_text(render_index(schema, groups, refs, page_of, table_origin, col_origin,
                                               per_origin, meta), encoding="utf-8")
    for d in DOMAINS + [OTHER_DOMAIN]:
        if d[0] in groups:
            (out / f"{d[0]}.md").write_text(render_domain(d, groups[d[0]], schema, refs, page_of, table_origin,
                                                          col_origin, meta), encoding="utf-8")
    print("Domínios:", {k: len(v) for k, v in groups.items()}, file=sys.stderr)
    unknown = [(t, c["name"]) for t, info in schema["tables"].items() for c in info["columns"]
               if (t, c["name"]) not in col_origin]
    print(f"Colunas sem origem identificada: {len(unknown)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
