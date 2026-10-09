# Imagem da documentação: Material for MkDocs + plugin que monta a página única para o PDF.
FROM squidfunk/mkdocs-material:9.7.7

RUN pip install --no-cache-dir "mkdocs-print-site-plugin==2.9"
