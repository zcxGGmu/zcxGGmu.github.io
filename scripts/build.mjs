import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import zlib from "node:zlib";
import matter from "gray-matter";
import { marked } from "marked";
import * as cheerio from "cheerio";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, "..");
const config = JSON.parse(await fs.readFile(path.join(rootDir, "site.config.json"), "utf8"));
const contentDir = path.join(rootDir, "content", "blog");
const assetVersion = "20260607-sidebar-collapse";
const generatedTargets = [
  "index.html",
  "index.xml",
  "sitemap.xml",
  "robots.txt",
  "404.html",
  "blog",
  "page",
  "categories",
  "tags",
  "series",
  "archive",
  "about",
  "friends"
];

marked.setOptions({
  gfm: true,
  breaks: false,
  mangle: false,
  headerIds: false
});

function assertInside(parent, target) {
  const parentPath = path.resolve(parent);
  const targetPath = path.resolve(target);
  if (!targetPath.startsWith(parentPath)) {
    throw new Error(`Refusing to write outside ${parentPath}: ${targetPath}`);
  }
}

async function ensureDir(dir) {
  assertInside(rootDir, dir);
  await fs.mkdir(dir, { recursive: true });
}

async function writeFile(relativePath, content) {
  const target = path.join(rootDir, relativePath);
  assertInside(rootDir, target);
  await ensureDir(path.dirname(target));
  await fs.writeFile(target, content, "utf8");
}

function escapeHtml(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function escapeAttr(value) {
  return escapeHtml(value).replace(/'/g, "&#39;");
}

function stripHtml(html) {
  return cheerio.load(html).text().replace(/\s+/g, " ").trim();
}

function slugifyHeading(text) {
  const normalized = String(text || "")
    .trim()
    .toLowerCase()
    .replace(/<[^>]*>/g, "")
    .replace(/&[a-z0-9#]+;/gi, "")
    .replace(/[\s_]+/g, "-")
    .replace(/[^\p{Letter}\p{Number}-]+/gu, "")
    .replace(/-+/g, "-")
    .replace(/^-|-$/g, "");
  return normalized || "section";
}

function addHeadingIds(html) {
  const $ = cheerio.load(html, { decodeEntities: false });
  const used = new Map();

  $(".post-body h1, .post-body h2, .post-body h3, .post-body h4, h1, h2, h3, h4").each((_, node) => {
    const heading = $(node);
    const existing = String(heading.attr("id") || "").trim();
    const base = existing || slugifyHeading(heading.text().replace(/\s+/g, " ").trim());
    const count = used.get(base) || 0;
    used.set(base, count + 1);
    heading.attr("id", count ? `${base}-${count + 1}` : base);
  });

  return $("body").html() || $.root().html() || html;
}

function normalizeArray(value) {
  if (!value) return [];
  return Array.isArray(value) ? value.filter(Boolean).map(String) : [String(value)];
}

function dateLabel(value) {
  const raw = String(value || "");
  if (/^\d{4}-\d{2}-\d{2}/.test(raw)) return raw.slice(0, 10);
  const date = new Date(raw);
  if (Number.isNaN(date.getTime())) return "";
  return date.toISOString().slice(0, 10);
}

function dateYear(value) {
  const label = dateLabel(value);
  return label ? label.slice(0, 4) : "notes";
}

function sortDate(value) {
  const time = Date.parse(String(value || ""));
  return Number.isNaN(time) ? 0 : time;
}

function readMinutes(text) {
  const chineseChars = (text.match(/[\u4e00-\u9fff]/g) || []).length;
  const latinWords = (text.replace(/[\u4e00-\u9fff]/g, " ").match(/[A-Za-z0-9_+-]+/g) || []).length;
  return Math.max(1, Math.ceil((chineseChars + latinWords * 2) / 500));
}

function encodeUrlPath(rawPath) {
  return rawPath
    .split("/")
    .map((part, index) => (index === 0 ? part : encodeURIComponent(part)))
    .join("/");
}

function absoluteUrl(urlPath) {
  if (/^https?:\/\//.test(urlPath)) return urlPath;
  return `${config.baseUrl.replace(/\/$/, "")}${urlPath}`;
}

function pagePath(basePath, pageNumber) {
  if (pageNumber <= 1) return basePath;
  if (basePath === "/") return `/page/${pageNumber}/`;
  return `${basePath.replace(/\/$/, "")}/page/${pageNumber}/`;
}

function relFileForUrl(urlPath) {
  const clean = urlPath.replace(/^\//, "");
  if (!clean) return "index.html";
  const decoded = clean
    .split("/")
    .filter(Boolean)
    .map((part) => decodeURIComponent(part));
  return path.join(...decoded, "index.html");
}

async function cleanGenerated() {
  for (const target of generatedTargets) {
    const fullPath = path.join(rootDir, target);
    assertInside(rootDir, fullPath);
    await fs.rm(fullPath, { recursive: true, force: true });
  }
}

async function loadPosts() {
  const files = (await fs.readdir(contentDir)).filter((file) => file.endsWith(".md")).sort();
  const posts = [];
  for (const file of files) {
    const source = await fs.readFile(path.join(contentDir, file), "utf8");
    const parsed = matter(source);
    const data = parsed.data;
    const html = addHeadingIds(marked.parse(parsed.content));
    const plain = stripHtml(html);
    const slug = String(data.slug || file.replace(/\.md$/, ""));
    const year = dateYear(data.date);
    const url = encodeUrlPath(`/blog/${year}/${slug}/`);
    posts.push({
      file,
      title: String(data.title || slug),
      date: String(data.date || ""),
      updated: String(data.updated || ""),
      dateLabel: dateLabel(data.date),
      description: String(data.description || plain.slice(0, 180)),
      categories: normalizeArray(data.categories),
      tags: normalizeArray(data.tags),
      series: normalizeArray(data.series),
      featuredImage: String(data.featured_image || ""),
      pinned: Boolean(data.pinned),
      html,
      plain,
      minutes: readMinutes(plain),
      slug,
      year,
      url,
      sortTime: sortDate(data.date)
    });
  }
  return posts.sort((a, b) => {
    if (a.pinned !== b.pinned) return a.pinned ? -1 : 1;
    return b.sortTime - a.sortTime;
  });
}

function navItems(activeUrl) {
  return config.menu
    .map((item) => {
      const active = activeUrl === item.url || (item.url !== "/" && activeUrl.startsWith(item.url));
      return `<a class="a-block nav-link-item ${active ? "active" : "false"}" href="${item.url}">${item.name}</a>`;
    })
    .join("");
}

function drawerItems(activeUrl) {
  return config.menu
    .map((item) => {
      const active = activeUrl === item.url || (item.url !== "/" && activeUrl.startsWith(item.url));
      return `<a class="a-block drawer-menu-item ${active ? "active" : "false"}" href="${item.url}">${item.name}</a>`;
    })
    .join("");
}

function footerHtml() {
  const social = config.social
    .map((item) => `<a href="${escapeAttr(item.url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(item.name)}</a>`)
    .join("<br>");
  return `${social}<br><hr>魔改自 <a href="https://github.com/AmazingRise/hugo-theme-diary" target="_blank" rel="noopener noreferrer">Diary</a> by <a href="/">zcxGGmu</a><br>&copy; ${new Date().getFullYear()} ${escapeHtml(config.brand)}<br><span>备案信息占位</span>`;
}

function avatarHtml(className = "site-avatar") {
  if (!config.avatar) return "";
  return `<img class="${className}" src="${escapeAttr(config.avatar)}" alt="${escapeAttr(config.author)}" loading="lazy">`;
}

function themeToggleHtml(className = "") {
  const classes = ["theme-toggle", className].filter(Boolean).join(" ");
  return `<button class="${classes}" type="button" data-theme-toggle title="切换深色模式" aria-label="切换深色模式" aria-pressed="false"><span class="material-icons theme-toggle-icon" aria-hidden="true">dark_mode</span></button>`;
}

function themeBootstrapScript() {
  return `<script>
(function(){
  var key="blog-theme";
  var sidebarKey="blog-sidebar-collapsed";
  var theme="";
  try{theme=localStorage.getItem(key)||""}catch(_){}
  if(theme!=="light"&&theme!=="dark"){
    theme=window.matchMedia&&window.matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light";
  }
  document.documentElement.dataset.theme=theme;
  document.documentElement.style.colorScheme=theme;
  try{
    if(localStorage.getItem(sidebarKey)==="1") document.documentElement.classList.add("sidebar-collapsed");
  }catch(_){}
})();</script>`;
}

function headHtml(page) {
  const title = page.title === config.title ? config.title : `${page.title} - ${config.title}`;
  const description = page.description || config.description;
  const canonical = absoluteUrl(page.url || "/");
  return `<!doctype html>
<html lang="${config.language}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
  <meta name="generator" content="Custom static archive">
  <title>${escapeHtml(title)}</title>
  <meta name="description" content="${escapeAttr(description)}">
  <meta name="author" content="${escapeAttr(config.author)}">
  <meta name="theme-color" content="#f8fafc">
  <meta property="og:url" content="${escapeAttr(canonical)}">
  <meta property="og:site_name" content="${escapeAttr(config.title)}">
  <meta property="og:title" content="${escapeAttr(page.title)}">
  <meta property="og:description" content="${escapeAttr(description)}">
  <meta property="og:locale" content="zh_cn">
  <meta property="og:type" content="${page.isPost ? "article" : "website"}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="canonical" href="${escapeAttr(canonical)}">
  <link rel="icon" type="image/png" sizes="16x16" href="/images/favicon-16.png">
  <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/images/favicon-180.png">
  <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png">
  ${themeBootstrapScript()}
  <link rel="stylesheet" href="/scss/journal.min.css" media="screen">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Sans+SC:wght@400;500;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Material+Icons&display=swap">
  <link rel="stylesheet" href="/scss/modern.min.css?v=${assetVersion}" media="screen">
  <meta name="color-scheme" content="light dark">
</head>`;
}

function themeScript() {
  return `<script>
(function(){
  var key="blog-theme";
  var meta=document.querySelector('meta[name="theme-color"]');
  function systemTheme(){
    return window.matchMedia&&window.matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light";
  }
  function storedTheme(){
    try{return localStorage.getItem(key)||""}catch(_){return ""}
  }
  function setStoredTheme(theme){
    try{localStorage.setItem(key,theme)}catch(_){}
  }
  function setLegacyCookie(theme){
    document.cookie="night="+(theme==="dark"?"1":"0")+";path=/;max-age=31536000";
  }
  function applyTheme(theme,persist){
    theme=theme==="dark"?"dark":"light";
    document.documentElement.dataset.theme=theme;
    document.documentElement.style.colorScheme=theme;
    if(meta) meta.setAttribute("content",theme==="dark"?"#0f172a":"#f8fafc");
    if(persist!==false){
      setStoredTheme(theme);
      setLegacyCookie(theme);
    }
    document.querySelectorAll("[data-theme-toggle]").forEach(function(button){
      var dark=theme==="dark";
      var icon=button.querySelector(".theme-toggle-icon");
      if(icon) icon.textContent=dark?"light_mode":"dark_mode";
      button.setAttribute("aria-label",dark?"切换浅色模式":"切换深色模式");
      button.setAttribute("aria-pressed",dark?"true":"false");
      button.title=dark?"切换浅色模式":"切换深色模式";
    });
  }
  window.setColorTheme=function(theme){applyTheme(theme,true)};
  window.toggleColorTheme=function(){
    applyTheme(document.documentElement.dataset.theme==="dark"?"light":"dark",true);
  };
  window.toggleDarkMode=window.toggleColorTheme;
  document.addEventListener("DOMContentLoaded",function(){
    applyTheme(document.documentElement.dataset.theme||storedTheme()||systemTheme(),false);
    document.querySelectorAll("[data-theme-toggle]").forEach(function(button){
      button.addEventListener("click",function(){window.toggleColorTheme()});
    });
  });
  if(window.matchMedia){
    var query=window.matchMedia("(prefers-color-scheme: dark)");
    var onChange=function(){if(!storedTheme()) applyTheme(systemTheme(),false)};
    if(query.addEventListener) query.addEventListener("change",onChange);
    else if(query.addListener) query.addListener(onChange);
  }
})();</script>`;
}

function sidebarCollapseScript() {
  return `<script>
(function(){
  var key="blog-sidebar-collapsed";
  function storedCollapsed(){
    try{return localStorage.getItem(key)==="1"}catch(_){return false}
  }
  function storeCollapsed(collapsed){
    try{localStorage.setItem(key,collapsed?"1":"0")}catch(_){}
  }
  function applySidebarState(collapsed,persist){
    document.documentElement.classList.toggle("sidebar-collapsed",collapsed);
    if(persist!==false) storeCollapsed(collapsed);
    document.querySelectorAll("[data-sidebar-collapse-toggle]").forEach(function(button){
      var icon=button.querySelector(".sidebar-collapse-icon");
      if(icon) icon.textContent=collapsed?"chevron_right":"chevron_left";
      button.setAttribute("aria-label",collapsed?"展开左侧边栏":"收起左侧边栏");
      button.setAttribute("aria-expanded",collapsed?"false":"true");
      button.title=collapsed?"展开左侧边栏":"收起左侧边栏";
    });
  }
  window.toggleSidebarCollapsed=function(){
    applySidebarState(!document.documentElement.classList.contains("sidebar-collapsed"),true);
  };
  document.addEventListener("DOMContentLoaded",function(){
    applySidebarState(document.documentElement.classList.contains("sidebar-collapsed")||storedCollapsed(),false);
    document.querySelectorAll("[data-sidebar-collapse-toggle]").forEach(function(button){
      button.addEventListener("click",window.toggleSidebarCollapsed);
    });
  });
})();</script>`;
}

function progressScript() {
  return `<script>
(function(){
  function byId(id){return document.getElementById(id)}
  function ensureChrome(){
    if(!byId("reading-progress")){
      var progress=document.createElement("div");
      progress.id="reading-progress";
      progress.setAttribute("aria-hidden","true");
      document.body.appendChild(progress);
    }
    if(!byId("backToTop")){
      var button=document.createElement("button");
      button.id="backToTop";
      button.type="button";
      button.title="返回顶部";
      button.setAttribute("aria-label","返回顶部");
      button.innerHTML='<span class="pagination-action-icon" aria-hidden="true">↑</span>';
      button.addEventListener("click",function(){window.scrollTo({top:0,behavior:"smooth"})});
      document.body.appendChild(button);
    }
  }
  function update(){
    var root=document.documentElement;
    var total=root.scrollHeight-root.clientHeight;
    var percent=total>0?(root.scrollTop||document.body.scrollTop)/total*100:0;
    var progress=byId("reading-progress");
    var top=byId("backToTop");
    var global=byId("globalBackToTop");
    if(progress) progress.style.width=percent+"%";
    var show=(window.scrollY||root.scrollTop)>360;
    if(top) top.classList.toggle("show",show);
    if(global) global.classList.toggle("invisible",!show);
  }
  window.toggleDrawer=function(){
    var drawer=byId("drawer");
    var overlay=byId("drawer-overlay");
    var open=!drawer.classList.contains("single-column-drawer-container-active");
    drawer.classList.toggle("single-column-drawer-container-active",open);
    document.documentElement.style.overflow=open?"hidden":"";
    if(overlay) overlay.style.display=open?"block":"none";
  };
  document.addEventListener("DOMContentLoaded",function(){
    ensureChrome();
    update();
    window.addEventListener("scroll",update,{passive:true});
    window.addEventListener("resize",update,{passive:true});
  });
})();</script>`;
}

function lightboxScript() {
  return `<script>
(function(){
  function ready(fn){document.readyState==="loading"?document.addEventListener("DOMContentLoaded",fn,{once:true}):fn()}
  ready(function(){
    var images=document.querySelectorAll('.post-body img:not([data-lightbox="disabled"])');
    if(!images.length) return;
    var box=document.createElement("div");
    box.className="image-lightbox";
    box.setAttribute("role","dialog");
    box.setAttribute("aria-modal","true");
    box.innerHTML='<div class="image-lightbox__inner"><button class="image-lightbox__close" type="button" aria-label="关闭图片预览">×</button><img class="image-lightbox__img" alt=""></div>';
    document.body.appendChild(box);
    var preview=box.querySelector("img");
    var close=box.querySelector("button");
    function hide(){box.classList.remove("is-visible");document.body.classList.remove("lightbox-open");preview.removeAttribute("src")}
    images.forEach(function(img){
      img.tabIndex=0;
      img.addEventListener("click",function(){
        preview.src=img.currentSrc||img.src;
        preview.alt=img.alt||"";
        box.classList.add("is-visible");
        document.body.classList.add("lightbox-open");
      });
    });
    close.addEventListener("click",hide);
    box.addEventListener("click",function(event){if(event.target===box) hide()});
    document.addEventListener("keydown",function(event){if(event.key==="Escape") hide()});
  });
})();</script>`;
}

function paginationHtml(current, total, basePath, variant = "desktop") {
  if (total <= 1) {
    return `<div class="pagination"><a id="${variant === "desktop" ? "globalBackToTop" : ""}" class="pagination-action animated-visibility invisible" href="#top"><span class="pagination-action-icon" aria-hidden="true">↑</span></a></div>`;
  }
  const prev = current > 1 ? pagePath(basePath, current - 1) : "";
  const next = current < total ? pagePath(basePath, current + 1) : "";
  const indicator = variant === "desktop"
    ? `${current}<br><div style="display:inline-block;transform:rotate(-28deg);margin:2px 0">-</div><br>${total}`
    : `${current}/${total}`;
  return `<div class="pagination">
    ${variant === "desktop" ? '<a id="globalBackToTop" class="pagination-action animated-visibility invisible" href="#top"><span class="pagination-action-icon" aria-hidden="true">↑</span></a>' : ""}
    <a class="pagination-action" ${prev ? `href="${prev}"` : 'style="visibility:hidden"'}><span class="pagination-action-icon" aria-hidden="true">‹</span></a>
    <div class="pagination-indicator"><span style="text-align:center;line-height:1.2em">${indicator}</span></div>
    <a class="pagination-action" ${next ? `href="${next}"` : 'style="visibility:hidden"'}><span class="pagination-action-icon" aria-hidden="true">›</span></a>
  </div>`;
}

function layout(page, mainHtml, options = {}) {
  const activeUrl = page.activeUrl || page.url || "/";
  const desktopPagination = options.pagination ? paginationHtml(options.pagination.current, options.pagination.total, options.pagination.basePath, "desktop") : paginationHtml(1, 1, "/", "desktop");
  const mobilePagination = options.pagination ? paginationHtml(options.pagination.current, options.pagination.total, options.pagination.basePath, "mobile") : "";
  const mobilePaginationLine = mobilePagination ? `    ${mobilePagination}\n` : "";
  return `${headHtml(page)}
<body>
  <a class="skip-link" href="#main-content">跳到主要内容</a>
  <div id="app">
    <div class="single-column-drawer-container" id="drawer">
      <div class="drawer-content"><div class="drawer-profile">${avatarHtml("drawer-avatar")}<div class="drawer-title">${escapeHtml(config.brand)}</div></div><div class="drawer-menu">${drawerItems(activeUrl)}</div></div>
    </div>
    <div id="drawer-overlay" class="single-column-drawer-overlay" style="display:none" role="button" tabindex="0" aria-label="关闭菜单" onclick="toggleDrawer()" onkeydown='(event.key==="Enter"||event.key===" "||event.key==="Escape")&&(event.preventDefault(),toggleDrawer())'></div>
    <nav id="navBar" class="navbar sticky-top navbar-light single-column-nav-container">
      <div id="navBackground" class="nav-background"></div>
      <div class="container container-narrow nav-content">
        <button id="nav_dropdown_btn" class="nav-dropdown-toggle" type="button" aria-label="打开菜单" aria-expanded="false" onclick="toggleDrawer()"><span class="nav-menu-symbol" aria-hidden="true">☰</span></button>
        <a id="navTitle" class="navbar-brand" href="/">${escapeHtml(config.brand)}</a>
        ${themeToggleHtml("theme-toggle-mobile")}
      </div>
    </nav>
    <div class="single-column-header-container" id="pageHead">
      <a href="/">${avatarHtml("mobile-site-avatar")}<div class="single-column-header-title">${escapeHtml(config.brand)}</div><div class="single-column-header-subtitle">${escapeHtml(config.subtitle)}</div></a>
    </div>
    <div id="content">
      <div id="streamContainer" class="stream-container" role="main">
        <div id="main-content"></div>
        ${mainHtml}
      </div>
    </div>
    <div id="sideContainer" class="side-container">
      <button class="sidebar-collapse-toggle" type="button" data-sidebar-collapse-toggle title="收起左侧边栏" aria-label="收起左侧边栏" aria-expanded="true">
        <span class="material-icons sidebar-collapse-icon" aria-hidden="true">chevron_left</span>
      </button>
      <a class="a-block nav-head ${activeUrl === "/" ? "active" : "false"}" href="/">
        ${avatarHtml("site-avatar")}
        <div class="nav-title">${escapeHtml(config.brand)}</div>
        <div class="nav-subtitle">${escapeHtml(config.subtitle)}</div>
      </a>
      <div class="theme-switcher theme-switcher-desktop">${themeToggleHtml("theme-toggle-desktop")}</div>
      <div class="nav-link-list">${navItems(activeUrl)}</div>
      <div class="nav-footer">${footerHtml()}</div>
    </div>
    <div id="extraContainer" class="extra-container"><div class="toc-wrapper">${options.toc || ""}</div>${desktopPagination}</div>
${mobilePaginationLine}    <div id="single-column-footer">${footerHtml()}</div>
  </div>
  <script src="/js/journal.js"></script>
  <script src="/js/code-enhance.js"></script>
  ${themeScript()}
  ${sidebarCollapseScript()}
  ${progressScript()}
  ${lightboxScript()}
</body>
</html>`;
}

function renderPostList(posts) {
  return `<div class="post-list-container post-list-container-no-background">
    ${posts.map((post) => `<a href="${post.url}" class="a-block">
      <div class="post-item-wrapper ${post.pinned ? "post-item-pinned" : ""}">
        <div class="post-item post-item-no-divider">
          <div class="post-item-info-wrapper">
            <div class="post-item-title">${escapeHtml(post.title)}</div>
            <div class="post-item-summary">${escapeHtml(post.description)}</div>
            <div class="post-item-meta">${post.pinned ? '<span class="pin-badge">📌 置顶</span>&emsp;' : ""}${escapeHtml(post.dateLabel)}&emsp;<span class="meta-icon" aria-hidden="true">◷</span> ${post.minutes} min&emsp;</div>
          </div>
          ${post.featuredImage ? `<div class="post-item-image-wrapper"><div class="post-item-image" style="background-image:url('${escapeAttr(post.featuredImage)}')"></div></div>` : ""}
        </div>
      </div>
    </a>`).join("")}
  </div>`;
}

function renderToc(html) {
  const $ = cheerio.load(html, { decodeEntities: false });
  const headings = $(".post-body h1, .post-body h2, .post-body h3, .post-body h4")
    .toArray()
    .map((node) => ({
      level: Number(node.tagName.slice(1)),
      id: $(node).attr("id"),
      text: $(node).text().replace(/\s+/g, " ").trim()
    }))
    .filter((item) => item.id && item.text);
  if (!headings.length) return "";
  return `<div class="toc"><div class="toc-title">目录</div><nav>${headings.map((item) => `<a class="toc-link toc-level-${item.level}" href="#${escapeAttr(item.id)}">${escapeHtml(item.text)}</a>`).join("")}</nav></div>`;
}

function renderPost(post, previous, next) {
  const headerClass = post.featuredImage ? "post-head-wrapper" : "post-head-wrapper-text-only";
  const headerStyle = post.featuredImage ? ` style="background-image:url('${escapeAttr(post.featuredImage)}')"` : "";
  const meta = [
    post.dateLabel ? `<time itemprop="datePublished">${escapeHtml(post.dateLabel)}</time>` : "",
    post.categories.length ? `<span class="meta-icon" aria-hidden="true">▣</span> ${post.categories.map((item) => `<a href="/categories/${encodeURIComponent(item)}/">${escapeHtml(item)}</a>`).join("&nbsp;")}` : "",
    post.tags.length ? `<span class="meta-icon" aria-hidden="true">◇</span> ${post.tags.map((item) => `<a href="/tags/${encodeURIComponent(item)}/">${escapeHtml(item)}</a>`).join("&nbsp;")}` : "",
    `<span class="meta-icon" aria-hidden="true">◷</span> ${post.minutes} min`
  ].filter(Boolean).join("&nbsp;&nbsp;");
  const body = `<div class="post-list-container post-list-container-shadow">
    <article class="post">
      <div class="${headerClass}"${headerStyle}>
        <div class="post-title">${escapeHtml(post.title)}
          ${post.description ? `<div class="post-subtitle">${escapeHtml(post.description)}</div>` : ""}
          <div class="post-meta">${meta}</div>
        </div>
      </div>
      <div class="post-body-wrapper"><div class="post-body" v-pre>${post.html}<hr id="EOF"><p class="last-modified">最后整理于 ${escapeHtml(dateLabel(post.updated) || post.dateLabel)}</p></div></div>
      <nav class="post-pagination">
        ${next ? `<a class="newer-posts" href="${next.url}">下一篇<br>${escapeHtml(next.title)}</a>` : '<a class="newer-posts">下一篇<br>没有更新的文章</a>'}
        ${previous ? `<a class="older-posts" href="${previous.url}">上一篇<br>${escapeHtml(previous.title)}</a>` : '<a class="older-posts">上一篇<br>没有更早的文章</a>'}
      </nav>
    </article>
  </div>`;
  return { body, toc: renderToc(body) };
}

function mapBy(posts, key) {
  const bucket = new Map();
  for (const post of posts) {
    for (const value of post[key]) {
      if (!bucket.has(value)) bucket.set(value, []);
      bucket.get(value).push(post);
    }
  }
  return bucket;
}

function renderTermIndex(title, terms, baseUrl) {
  const sorted = [...terms.entries()].sort((a, b) => b[1].length - a[1].length || a[0].localeCompare(b[0], "zh-CN"));
  return `<div class="post-list-container post-list-container-shadow">
    <div class="taxonomy-page">
      <h1>${escapeHtml(title)}</h1>
      <div class="taxonomy-grid">
        ${sorted.map(([term, list]) => `<a class="taxonomy-card" href="${baseUrl}${encodeURIComponent(term)}/"><span>${escapeHtml(term)}</span><strong>${list.length}</strong></a>`).join("")}
      </div>
    </div>
  </div>`;
}

function renderTermPage(title, posts) {
  return `<div class="post-list-container post-list-container-shadow taxonomy-term-header">
    <div class="taxonomy-page"><h1>${escapeHtml(title)}</h1></div>
  </div>${renderPostList(posts)}`;
}

function renderArchive(posts) {
  const years = new Map();
  for (const post of posts) {
    if (!years.has(post.year)) years.set(post.year, []);
    years.get(post.year).push(post);
  }
  return `<div class="post-list-container post-list-container-shadow">
    <div class="archive-page">
      <h1>归档</h1>
      ${[...years.entries()].sort((a, b) => b[0].localeCompare(a[0])).map(([year, list]) => `
        <section class="archive-year">
          <h2>${escapeHtml(year)}</h2>
          ${list.map((post) => `<a class="archive-item" href="${post.url}"><time>${escapeHtml(post.dateLabel)}</time><span>${escapeHtml(post.title)}</span></a>`).join("")}
        </section>`).join("")}
    </div>
  </div>`;
}

function renderSimplePage(title, body) {
  return `<div class="post-list-container post-list-container-shadow">
    <article class="post">
      <div class="post-head-wrapper-text-only"><div class="post-title">${escapeHtml(title)}</div></div>
      <div class="post-body-wrapper"><div class="post-body">${body}</div></div>
    </article>
  </div>`;
}

async function writeListPages(posts, basePath, activeUrl, title) {
  const pageSize = Number(config.pageSize || 10);
  const total = Math.max(1, Math.ceil(posts.length / pageSize));
  for (let pageNumber = 1; pageNumber <= total; pageNumber++) {
    const start = (pageNumber - 1) * pageSize;
    const pagePosts = posts.slice(start, start + pageSize);
    const url = pagePath(basePath, pageNumber);
    await writeFile(relFileForUrl(url), layout({
      title,
      description: config.description,
      url,
      activeUrl
    }, renderPostList(pagePosts), {
      pagination: { current: pageNumber, total, basePath }
    }));
  }
}

function xmlEscape(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

async function writeFeeds(posts) {
  const items = posts.slice(0, 30).map((post) => `<item>
  <title>${xmlEscape(post.title)}</title>
  <link>${xmlEscape(absoluteUrl(post.url))}</link>
  <guid>${xmlEscape(absoluteUrl(post.url))}</guid>
  <pubDate>${new Date(post.sortTime).toUTCString()}</pubDate>
  <description>${xmlEscape(post.description)}</description>
</item>`).join("\n");
  await writeFile("index.xml", `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>${xmlEscape(config.title)}</title>
  <link>${xmlEscape(config.baseUrl)}</link>
  <description>${xmlEscape(config.description)}</description>
${items}
</channel>
</rss>`);

  const urls = ["/", "/blog/", "/categories/", "/tags/", "/series/", "/archive/", "/about/", "/friends/", ...posts.map((post) => post.url)];
  await writeFile("sitemap.xml", `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map((url) => `  <url><loc>${xmlEscape(absoluteUrl(url))}</loc></url>`).join("\n")}
</urlset>`);
  await writeFile("robots.txt", `User-agent: *
Allow: /
Sitemap: ${config.baseUrl.replace(/\/$/, "")}/sitemap.xml
`);
}

function redirectHtml(title, targetUrl) {
  return `<!doctype html>
<html lang="${config.language}">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0;url=${escapeAttr(targetUrl)}">
  <link rel="canonical" href="${escapeAttr(absoluteUrl(targetUrl))}">
  <title>${escapeHtml(title)} - ${escapeHtml(config.title)}</title>
</head>
<body>
  <p><a href="${escapeAttr(targetUrl)}">文章已迁移，点击继续阅读。</a></p>
</body>
</html>`;
}

async function writeLegacyRedirect(post) {
  if (!post.dateLabel || !post.slug) return;
  const [year, month, day] = post.dateLabel.split("-");
  const legacyUrl = encodeUrlPath(`/${year}/${month}/${day}/${post.slug}/`);
  await writeFile(relFileForUrl(legacyUrl), redirectHtml(post.title, post.url));
}

function crc32(buffer) {
  let crc = -1;
  for (let i = 0; i < buffer.length; i++) {
    crc ^= buffer[i];
    for (let j = 0; j < 8; j++) {
      crc = (crc >>> 1) ^ (0xedb88320 & -(crc & 1));
    }
  }
  return (crc ^ -1) >>> 0;
}

function pngChunk(type, data) {
  const typeBuffer = Buffer.from(type);
  const length = Buffer.alloc(4);
  length.writeUInt32BE(data.length);
  const crc = Buffer.alloc(4);
  crc.writeUInt32BE(crc32(Buffer.concat([typeBuffer, data])));
  return Buffer.concat([length, typeBuffer, data, crc]);
}

function makePng(width, height, palette) {
  const raw = Buffer.alloc((width * 4 + 1) * height);
  let offset = 0;
  for (let y = 0; y < height; y++) {
    raw[offset++] = 0;
    for (let x = 0; x < width; x++) {
      const tile = (Math.floor(x / 72) + Math.floor(y / 72)) % palette.length;
      const stripe = (x * 3 + y * 2) % 257 < 18 ? palette[(tile + 1) % palette.length] : palette[tile];
      const dot = ((x - width * 0.68) ** 2 + (y - height * 0.38) ** 2) ** 0.5 < 86 ? palette[(tile + 2) % palette.length] : stripe;
      raw[offset++] = dot[0];
      raw[offset++] = dot[1];
      raw[offset++] = dot[2];
      raw[offset++] = 255;
    }
  }
  const header = Buffer.alloc(13);
  header.writeUInt32BE(width, 0);
  header.writeUInt32BE(height, 4);
  header[8] = 8;
  header[9] = 6;
  header[10] = 0;
  header[11] = 0;
  header[12] = 0;
  return Buffer.concat([
    Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]),
    pngChunk("IHDR", header),
    pngChunk("IDAT", zlib.deflateSync(raw)),
    pngChunk("IEND", Buffer.alloc(0))
  ]);
}

async function generateCovers() {
  const dir = path.join(rootDir, "images", "covers");
  await ensureDir(dir);
  const covers = [
    ["cover-virtualization.png", [[15, 23, 42], [22, 120, 132], [241, 196, 15], [248, 250, 252]]],
    ["cover-riscv.png", [[248, 250, 252], [29, 78, 216], [220, 38, 38], [17, 24, 39]]],
    ["cover-kernel.png", [[24, 24, 27], [74, 222, 128], [250, 204, 21], [226, 232, 240]]],
    ["cover-blog.png", [[255, 255, 255], [14, 165, 233], [244, 114, 182], [51, 65, 85]]]
  ];
  for (const [name, palette] of covers) {
    await fs.writeFile(path.join(dir, name), makePng(900, 470, palette));
  }
}

async function main() {
  await cleanGenerated();
  await generateCovers();
  const posts = await loadPosts();

  await writeListPages(posts, "/", "/", config.title);
  await writeListPages(posts, "/blog/", "/blog/", "文章");

  const categories = mapBy(posts, "categories");
  const tags = mapBy(posts, "tags");
  const series = mapBy(posts, "series");

  await writeFile("categories/index.html", layout({ title: "分类", description: config.description, url: "/categories/", activeUrl: "/categories/" }, renderTermIndex("分类", categories, "/categories/")));
  for (const [term, list] of categories) {
    await writeFile(path.join("categories", term, "index.html"), layout({ title: term, description: `${term} 分类文章`, url: `/categories/${encodeURIComponent(term)}/`, activeUrl: "/categories/" }, renderTermPage(term, list)));
  }

  await writeFile("tags/index.html", layout({ title: "标签", description: config.description, url: "/tags/", activeUrl: "/tags/" }, renderTermIndex("标签", tags, "/tags/")));
  for (const [term, list] of tags) {
    await writeFile(path.join("tags", term, "index.html"), layout({ title: term, description: `${term} 标签文章`, url: `/tags/${encodeURIComponent(term)}/`, activeUrl: "/tags/" }, renderTermPage(`# ${term}`, list)));
  }

  await writeFile("series/index.html", layout({ title: "系列", description: config.description, url: "/series/", activeUrl: "/series/" }, renderTermIndex("系列", series, "/series/")));
  for (const [term, list] of series) {
    await writeFile(path.join("series", term, "index.html"), layout({ title: term, description: `${term} 系列文章`, url: `/series/${encodeURIComponent(term)}/`, activeUrl: "/series/" }, renderTermPage(term, list)));
  }

  await writeFile("archive/index.html", layout({ title: "归档", description: config.description, url: "/archive/", activeUrl: "/archive/" }, renderArchive(posts)));
  await writeFile("about/index.html", layout({ title: "关于", description: config.description, url: "/about/", activeUrl: "/about/" }, renderSimplePage("关于", "<p>这里是关于页占位内容。后续可以补充个人简介、关注领域、联系方式和归档原则。</p>")));
  await writeFile("friends/index.html", layout({ title: "友链", description: config.description, url: "/friends/", activeUrl: "/friends/" }, renderSimplePage("友链", "<p>这里是友链页占位内容。后续可以添加长期关注的博客、资料站和项目主页。</p>")));
  await writeFile("404.html", layout({ title: "404", description: "页面不存在", url: "/404.html", activeUrl: "/" }, renderSimplePage("404", "<p>页面不存在，回到 <a href=\"/\">首页</a> 继续浏览。</p>")));

  for (const [index, post] of posts.entries()) {
    const previous = posts[index + 1];
    const next = posts[index - 1];
    const rendered = renderPost(post, previous, next);
    await writeFile(relFileForUrl(post.url), layout({ title: post.title, description: post.description, url: post.url, activeUrl: "/blog/", isPost: true }, rendered.body, { toc: rendered.toc }));
    await writeLegacyRedirect(post);
  }

  await writeFeeds(posts);
  console.log(`Built ${posts.length} posts.`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
