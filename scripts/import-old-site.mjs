import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import * as cheerio from "cheerio";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, "..");
const sourceDir = path.resolve(
  process.argv[2] || path.join(rootDir, "..", "_downloads", "old-site", "zcxGGmu.github.io-gh-pages")
);
const contentDir = path.join(rootDir, "content", "blog");

const coverImages = [
  "/images/covers/cover-virtualization.png",
  "/images/covers/cover-riscv.png",
  "/images/covers/cover-kernel.png",
  "/images/covers/cover-blog.png"
];

function assertInside(parent, target) {
  const parentPath = path.resolve(parent);
  const targetPath = path.resolve(target);
  if (!targetPath.startsWith(parentPath)) {
    throw new Error(`Refusing to write outside ${parentPath}: ${targetPath}`);
  }
}

async function walk(dir) {
  const entries = await fs.readdir(dir, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files.push(...await walk(fullPath));
    } else if (entry.isFile()) {
      files.push(fullPath);
    }
  }
  return files;
}

function cleanText(value) {
  return String(value || "")
    .replace(/\s+/g, " ")
    .replace(/^#\s*/, "")
    .trim();
}

function inferCategory(title, tags) {
  const text = `${title} ${tags.join(" ")}`;
  if (/虚拟化|KVM|VT-x|VT-d|I\/O|设备|内存|cpu/i.test(text)) return "虚拟化";
  if (/RISC-V|SIMD|Vector|APLIC/i.test(text)) return "体系结构";
  if (/调度|Linux|kernel/i.test(text)) return "内核";
  if (/Hexo|blog|博客/i.test(text)) return "博客搭建";
  return "技术";
}

function inferSeries(title, tags) {
  const text = `${title} ${tags.join(" ")}`;
  if (/虚拟化|KVM|VT-x|VT-d|I\/O|设备|内存|cpu/i.test(text)) return "虚拟化笔记";
  if (/RISC-V/i.test(text)) return "RISC-V 笔记";
  if (/SIMD|Vector/i.test(text)) return "向量计算笔记";
  return "";
}

function yamlScalar(value) {
  return JSON.stringify(String(value || ""));
}

function yamlList(values) {
  const list = [...new Set(values.filter(Boolean).map(String))];
  if (!list.length) return "[]";
  return `\n${list.map((item) => `  - ${yamlScalar(item)}`).join("\n")}`;
}

function slugFromPath(filePath) {
  return path.basename(path.dirname(filePath));
}

function getDate($) {
  return (
    $('time[itemprop*="datePublished"]').first().attr("datetime") ||
    $('meta[property="article:published_time"]').attr("content") ||
    ""
  );
}

function getUpdated($) {
  return (
    $('time[itemprop*="dateModified"]').first().attr("datetime") ||
    $('meta[property="article:modified_time"]').attr("content") ||
    ""
  );
}

function extractTags($) {
  const tags = [];
  $('meta[property="article:tag"]').each((_, node) => tags.push(cleanText($(node).attr("content"))));
  $(".post-tags a").each((_, node) => tags.push(cleanText($(node).text())));
  return [...new Set(tags.filter(Boolean))];
}

function normalizeBody($) {
  const body = $('.post-body[itemprop="articleBody"]').first();
  body.find("a.headerlink").remove();
  body.find("script, style").remove();
  body.find("p").each((_, node) => {
    if ($(node).text().trim().toLowerCase() === "[toc]") $(node).remove();
  });
  body.contents().each((_, node) => {
    if (node.type === "text" && String(node.data || "").trim().toLowerCase() === "[toc]") {
      $(node).remove();
    }
  });
  body.find("img").each((_, node) => {
    const img = $(node);
    if (!img.attr("alt")) img.attr("alt", "");
    img.removeAttr("data-src").removeAttr("loading");
  });
  body.find("a[target]").each((_, node) => {
    const link = $(node);
    if (!link.attr("rel")) link.attr("rel", "noopener noreferrer");
  });
  return body.html()?.trim() || "";
}

async function main() {
  await fs.access(sourceDir);
  assertInside(rootDir, contentDir);
  await fs.rm(contentDir, { recursive: true, force: true });
  await fs.mkdir(contentDir, { recursive: true });

  const htmlFiles = (await walk(path.join(sourceDir, "2025")))
    .filter((file) => path.basename(file) === "index.html")
    .filter((file) => /[\\/]\d{4}[\\/]\d{2}[\\/]\d{2}[\\/][^\\/]+[\\/]index\.html$/.test(file))
    .sort();

  const imported = [];
  for (const [index, file] of htmlFiles.entries()) {
    const html = await fs.readFile(file, "utf8");
    const $ = cheerio.load(html, { decodeEntities: false });
    const title = cleanText($("h1.post-title").first().text() || $('meta[property="og:title"]').attr("content"));
    const description = cleanText($('meta[name="description"]').attr("content") || $(".post-body p").first().text());
    const tags = extractTags($);
    const category = inferCategory(title, tags);
    const series = inferSeries(title, tags);
    const date = getDate($);
    const updated = getUpdated($);
    const slug = slugFromPath(file);
    const featuredImage = coverImages[index % coverImages.length];
    const body = normalizeBody($);

    const frontmatter = [
      "---",
      `title: ${yamlScalar(title)}`,
      `date: ${yamlScalar(date)}`,
      `updated: ${yamlScalar(updated)}`,
      `slug: ${yamlScalar(slug)}`,
      `description: ${yamlScalar(description)}`,
      `categories: ${yamlList([category])}`,
      `tags: ${yamlList(tags)}`,
      `series: ${series ? yamlList([series]) : "[]"}`,
      `featured_image: ${yamlScalar(featuredImage)}`,
      "pinned: false",
      "---",
      "",
      body,
      ""
    ].join("\n");

    const safeName = `${date.slice(0, 10) || "undated"}-${slug}.md`.replace(/[<>:"/\\|?*]/g, "-");
    const target = path.join(contentDir, safeName);
    assertInside(contentDir, target);
    await fs.writeFile(target, frontmatter, "utf8");
    imported.push({ title, target });
  }

  console.log(`Imported ${imported.length} posts into ${contentDir}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
