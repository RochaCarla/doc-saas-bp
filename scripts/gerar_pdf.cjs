#!/usr/bin/env node
/**
 * Gera o e-book (PDF) da documentação a partir do site estático já construído.
 *
 * Uso:
 *   node scripts/gerar_pdf.cjs <pasta-do-site> <saida.pdf>
 *   DOC_VERSION=abc1234 node scripts/gerar_pdf.cjs site site/documentacao-brasil-participativo-saas.pdf
 *
 * Requer os pacotes "puppeteer" e "pdf-lib" (use NODE_PATH se estiverem fora do projeto).
 *
 * O e-book é montado em partes, impressas separadamente e unidas no fim:
 *   1. capa (página inteira, sem margens)
 *   2. folha de rosto e apresentação (sem numeração)
 *   3. miolo: sumário e conteúdo (numerado, com marcadores do PDF)
 *   4. contracapa (página inteira, sem margens)
 */
const fs = require("fs");
const http = require("http");
const path = require("path");
const puppeteer = require("puppeteer");
const { PDFDocument } = require("pdf-lib");

const [siteDir, output] = process.argv.slice(2);
if (!siteDir || !output) {
  console.error("Uso: node scripts/gerar_pdf.cjs <pasta-do-site> <saida.pdf>");
  process.exit(2);
}
const BASE = process.env.SITE_BASE || "/doc-saas-bp/";
const VERSION = process.env.DOC_VERSION || "versão local";
const ROOT = path.resolve(__dirname, "..");
const MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
  "agosto", "setembro", "outubro", "novembro", "dezembro"];
const MESES_ABREV = ["jan.", "fev.", "mar.", "abr.", "maio", "jun.", "jul.", "ago.", "set.", "out.", "nov.", "dez."];
const TYPES = {
  ".html": "text/html; charset=utf-8", ".css": "text/css", ".js": "application/javascript",
  ".json": "application/json", ".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg",
  ".woff2": "font/woff2", ".woff": "font/woff", ".ico": "image/x-icon", ".xml": "application/xml",
};

function serve(dir) {
  const root = path.resolve(dir);
  const server = http.createServer((req, res) => {
    let p = decodeURIComponent(req.url.split("?")[0]);
    if (!p.startsWith(BASE)) { res.writeHead(404); return res.end(); }
    p = path.join(root, p.slice(BASE.length));
    if (!p.startsWith(root)) { res.writeHead(403); return res.end(); }
    if (fs.existsSync(p) && fs.statSync(p).isDirectory()) p = path.join(p, "index.html");
    if (!fs.existsSync(p)) { res.writeHead(404); return res.end(); }
    res.writeHead(200, { "Content-Type": TYPES[path.extname(p)] || "application/octet-stream" });
    fs.createReadStream(p).pipe(res);
  });
  return new Promise((resolve) => server.listen(0, "127.0.0.1", () => resolve(server)));
}

const NO_BOXES = ["top-left", "top-center", "top-right", "bottom-left", "bottom-center", "bottom-right"]
  .map((b) => `@${b} { content: none; }`).join(" ");
const BOX_STYLE = "font-family: Raleway, Arial, sans-serif; font-size: 8pt; color: #636363;";
const pageRule = (margin, numbered) => numbered
  ? `@page { size: A4; margin: ${margin}; ${NO_BOXES}
       @bottom-left { content: "Brasil Participativo SaaS — Documentação técnica"; ${BOX_STYLE} }
       @bottom-right { content: counter(page); ${BOX_STYLE} } }`
  : `@page { size: A4; margin: ${margin}; ${NO_BOXES} }`;

async function renderPart(page, part, { margin, numbered = false, outline = false }) {
  await page.evaluate((part, rule) => {
    document.body.classList.remove("bp-part-capa", "bp-part-rosto", "bp-part-miolo", "bp-part-contracapa");
    document.body.classList.add(`bp-part-${part}`);
    let style = document.getElementById("bp-page-rule");
    if (!style) {
      style = document.createElement("style");
      style.id = "bp-page-rule";
      document.head.appendChild(style);
    }
    style.textContent = rule;
  }, part, pageRule(margin, numbered));
  return page.pdf({
    format: "A4",
    printBackground: true,
    preferCSSPageSize: true,
    displayHeaderFooter: false,
    outline,
    tagged: true,
    timeout: 600000,
  });
}

(async () => {
  const server = await serve(siteDir);
  const url = `http://127.0.0.1:${server.address().port}${BASE}print_page/`;
  const browser = await puppeteer.launch({
    headless: true,
    protocolTimeout: 1800000, // a página única tem centenas de páginas e dezenas de diagramas
    args: ["--no-sandbox", "--disable-dev-shm-usage", "--font-render-hinting=none"],
  });
  try {
    const page = await browser.newPage();
    await page.setViewport({ width: 1200, height: 1600 });
    console.log(`Abrindo ${url}`);
    await page.goto(url, { waitUntil: "load", timeout: 180000 });

    // Sumário montado pelo plugin.
    await page.waitForFunction(() => document.querySelectorAll("#print-page-toc li").length > 0,
      { timeout: 120000, polling: 500 });
    // Diagramas Mermaid: o Material troca cada <pre class="mermaid"> por um <div class="mermaid">
    // com o SVG num shadow DOM fechado. Renderizado = nenhum <pre> restante e todos com altura.
    await page.waitForFunction(
      () => document.querySelectorAll("pre.mermaid").length === 0 &&
        [...document.querySelectorAll("div.mermaid")].every((el) => el.getBoundingClientRect().height > 0),
      { timeout: 300000, polling: 1000 });
    await page.evaluate(() => document.fonts.ready);
    const stats = await page.evaluate(() => ({
      diagramas: document.querySelectorAll(".mermaid").length,
      secoes: document.querySelectorAll("#print-site-page section.print-page").length,
    }));
    console.log(`Seções: ${stats.secoes} · diagramas: ${stats.diagramas}`);

    const hoje = new Date();
    const contracapa = fs.readFileSync(path.join(ROOT, "overrides/print/contracapa.html"), "utf8");
    await page.evaluate((info, contracapa) => {
      document.querySelectorAll("details").forEach((d) => d.setAttribute("open", ""));
      document.querySelectorAll(".tabbed-set").forEach((set) => {
        const labels = [...set.querySelectorAll(":scope > .tabbed-labels > label")];
        [...set.querySelectorAll(":scope > .tabbed-content > .tabbed-block")].forEach((block, i) => {
          block.style.display = "block";
          const title = document.createElement("p");
          title.className = "bp-print-tab-title";
          title.textContent = labels[i] ? labels[i].textContent.trim() : "";
          block.prepend(title);
        });
        const bar = set.querySelector(":scope > .tabbed-labels");
        if (bar) bar.style.display = "none";
      });
      const fill = (sel, text) => document.querySelectorAll(sel).forEach((el) => { el.textContent = text; });
      fill(".bp-edition", info.edicao);
      fill(".bp-version", info.versao);
      fill(".bp-generated", info.gerado);
      fill(".bp-year", info.ano);
      fill(".bp-access", info.acesso);
      const back = document.createElement("section");
      back.id = "bp-back-cover";
      back.innerHTML = contracapa;
      document.getElementById("print-site-page").appendChild(back);
    }, {
      edicao: `${MESES[hoje.getMonth()]} de ${hoje.getFullYear()}`,
      versao: VERSION,
      gerado: hoje.toLocaleDateString("pt-BR"),
      ano: String(hoje.getFullYear()),
      acesso: `${hoje.getDate()} ${MESES_ABREV[hoje.getMonth()]} ${hoje.getFullYear()}`,
    }, contracapa);
    await page.emulateMediaType("print");

    const capa = await renderPart(page, "capa", { margin: "0" });
    const rosto = await renderPart(page, "rosto", { margin: "22mm 20mm 22mm 20mm" });
    const miolo = await renderPart(page, "miolo", { margin: "18mm 16mm 20mm 16mm", numbered: true, outline: true });
    const verso = await renderPart(page, "contracapa", { margin: "0" });

    // O miolo é a base: mantém links internos e marcadores; as demais partes são inseridas.
    const book = await PDFDocument.load(miolo);
    let at = 0;
    for (const part of [capa, rosto]) {
      const src = await PDFDocument.load(part);
      const pages = await book.copyPages(src, src.getPageIndices());
      for (const p of pages) book.insertPage(at++, p);
    }
    const back = await PDFDocument.load(verso);
    for (const p of await book.copyPages(back, back.getPageIndices())) book.addPage(p);

    book.setTitle("Brasil Participativo SaaS — Documentação técnica");
    book.setAuthor("LabLivre/UnB");
    book.setSubject("Documentação técnica, transferência, inovação e estatísticas do Brasil Participativo SaaS: Participa e participação multicanal");
    book.setKeywords(["Brasil Participativo", "Participa", "SaaS", "Decidim", "multicanal", "WhatsApp", "participação social", "software livre", "gov.br"]);
    book.setLanguage("pt-BR");
    book.setCreator("scripts/gerar_pdf.cjs");
    book.setProducer("LabLivre/UnB");

    fs.mkdirSync(path.dirname(path.resolve(output)), { recursive: true });
    fs.writeFileSync(output, await book.save());
    console.log(`PDF gerado: ${output} · ${book.getPageCount()} páginas · ` +
      `${Math.round(fs.statSync(output).size / 1024)} KB`);
  } finally {
    await browser.close();
    server.close();
  }
})().catch((err) => {
  console.error(err);
  process.exit(1);
});
