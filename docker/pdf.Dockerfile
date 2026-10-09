# Imagem para gerar o e-book: Puppeteer (com Chrome) + pdf-lib.
FROM ghcr.io/puppeteer/puppeteer:25.12.0

RUN npm install --no-save pdf-lib@1.17.1
