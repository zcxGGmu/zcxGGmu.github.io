import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, "..");
const outDir = path.join(rootDir, "images", "posts", "serenity-aleabitoreddit-analysis");

const W = 1400;
const H = 820;
const C = {
  paper: "#fbfcfd",
  panel: "#f4f7f9",
  ink: "#17212b",
  muted: "#65737e",
  grid: "#d8e0e8",
  blue: "#2166a5",
  cyan: "#1585a0",
  green: "#4f8a5b",
  amber: "#c57c1f",
  red: "#b44b4b",
  violet: "#7158a6",
  slate: "#596775",
  lightBlue: "#dcecf7",
  lightGreen: "#e1f1e5",
  lightAmber: "#f7ead5",
  lightRed: "#f7dddd",
  white: "#ffffff"
};

const corpus = {
  localPosts: 832,
  mayPosts: 621,
  junePosts: 211,
  archiveStart: "2026-05-01T02:31:08Z",
  archiveEnd: "2026-06-08T08:43:24Z",
  mirrorLatest35: 35,
  mirrorAfterArchive: 18,
  mirrorEnd: "2026-06-09T02:29:21Z",
  mirrorSync: "2026-06-09 GMT+8 10:50",
  xArticlesSinceMay: 1,
  views: 94409865,
  likes: 408336,
  bookmarks: 120754,
  replies: 50009,
  retweets: 21513,
  profileFollowersFromMirror: 759921
};

const themes = [
  { name: "CPO/光通信/硅光", posts: 383, views: 47132938, color: C.blue },
  { name: "组合/收益/社群", posts: 144, views: 30665498, color: C.violet },
  { name: "AI 算力/云/Neocloud", posts: 105, views: 17372847, color: C.cyan },
  { name: "政策/资本市场", posts: 89, views: 16318566, color: C.slate },
  { name: "存储/HBM/NAND", posts: 72, views: 14389238, color: C.green },
  { name: "电力/800V/电网", posts: 52, views: 7279690, color: C.amber },
  { name: "机器人/实体 AI/关键材料", posts: 50, views: 11768958, color: C.red },
  { name: "航天/防务", posts: 24, views: 4718366, color: "#7b6f55" }
];

const tickers = [
  { ticker: "$SIVE", count: 214, views: 29028232, group: "CPO laser" },
  { ticker: "$NVDA", count: 80, views: 18058457, group: "downstream AI capex" },
  { ticker: "$AAOI", count: 72, views: 12069391, group: "optical transceiver" },
  { ticker: "$LITE", count: 69, views: 15814143, group: "laser incumbent" },
  { ticker: "$SOI", count: 57, views: 11546852, group: "SOI substrate" },
  { ticker: "$AXTI", count: 50, views: 10813935, group: "InP substrate/feedstock" },
  { ticker: "$JBL", count: 40, views: 5259031, group: "1.6T LRO module" },
  { ticker: "$NBIS", count: 35, views: 6039826, group: "neocloud" },
  { ticker: "$MRVL", count: 31, views: 6304994, group: "ASIC/CPO demand" },
  { ticker: "$LPK", count: 29, views: 6359556, group: "glass substrate tools" },
  { ticker: "$IREN", count: 29, views: 5106275, group: "negative case" },
  { ticker: "$POET", count: 25, views: 5764812, group: "packaging route" }
];

const dailyPosts = [
  ["05-01", 20], ["05-02", 15], ["05-03", 20], ["05-04", 21], ["05-05", 25],
  ["05-06", 22], ["05-07", 34], ["05-08", 27], ["05-09", 8], ["05-10", 8],
  ["05-11", 31], ["05-12", 22], ["05-13", 36], ["05-14", 19], ["05-15", 24],
  ["05-16", 8], ["05-17", 24], ["05-18", 5], ["05-19", 31], ["05-20", 34],
  ["05-21", 16], ["05-22", 19], ["05-23", 23], ["05-24", 16], ["05-25", 14],
  ["05-26", 11], ["05-27", 12], ["05-28", 17], ["05-29", 15], ["05-30", 39],
  ["05-31", 5], ["06-01", 53], ["06-02", 23], ["06-03", 37], ["06-04", 31],
  ["06-05", 27], ["06-06", 19], ["06-07", 15], ["06-08", 6]
];

function esc(value) {
  return String(value).replace(/[&<>"']/g, (ch) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    "\"": "&quot;",
    "'": "&#39;"
  })[ch]);
}

function text(x, y, value, opts = {}) {
  const {
    size = 22,
    weight = 500,
    color = C.ink,
    anchor = "start",
    family = "Arial, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif"
  } = opts;
  return `<text x="${x}" y="${y}" fill="${color}" font-family="${family}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}">${esc(value)}</text>`;
}

function tspans(x, y, lines, opts = {}) {
  const lineHeight = opts.lineHeight || 28;
  const attrs = `x="${x}" y="${y}" fill="${opts.color || C.ink}" font-family="${opts.family || "Arial, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif"}" font-size="${opts.size || 20}" font-weight="${opts.weight || 500}" text-anchor="${opts.anchor || "start"}"`;
  return `<text ${attrs}>${lines.map((line, i) => `<tspan x="${x}" dy="${i === 0 ? 0 : lineHeight}">${esc(line)}</tspan>`).join("")}</text>`;
}

function wrap(value, maxChars) {
  const lines = [];
  let line = "";
  for (const ch of String(value)) {
    if ((line + ch).length > maxChars) {
      lines.push(line);
      line = ch;
    } else {
      line += ch;
    }
  }
  if (line) lines.push(line);
  return lines;
}

function rect(x, y, w, h, fill, opts = {}) {
  const { rx = 0, stroke = "none", sw = 0, opacity = 1 } = opts;
  return `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${rx}" fill="${fill}" stroke="${stroke}" stroke-width="${sw}" opacity="${opacity}"/>`;
}

function line(x1, y1, x2, y2, opts = {}) {
  const { stroke = C.grid, sw = 2, dash = "", opacity = 1 } = opts;
  return `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${stroke}" stroke-width="${sw}"${dash ? ` stroke-dasharray="${dash}"` : ""} opacity="${opacity}"/>`;
}

function circle(cx, cy, r, fill, opts = {}) {
  const { stroke = "none", sw = 0, opacity = 1 } = opts;
  return `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${fill}" stroke="${stroke}" stroke-width="${sw}" opacity="${opacity}"/>`;
}

function pill(x, y, label, color, width = 160) {
  return `${rect(x, y, width, 34, color, { rx: 17, opacity: 0.12, stroke: color, sw: 1 })}
${text(x + width / 2, y + 23, label, { size: 16, weight: 700, color, anchor: "middle" })}`;
}

function base(title, subtitle, body, source) {
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" role="img" aria-labelledby="title desc">
  <title id="title">${esc(title)}</title>
  <desc id="desc">${esc(subtitle)}</desc>
  <rect width="${W}" height="${H}" fill="${C.paper}"/>
  <rect x="36" y="32" width="${W - 72}" height="${H - 64}" rx="20" fill="${C.panel}" stroke="#dce3ea"/>
  ${text(82, 102, title, { size: 40, weight: 800 })}
  ${text(82, 146, subtitle, { size: 21, color: C.muted })}
  ${body}
  ${text(82, 770, source, { size: 16, color: C.muted })}
</svg>
`;
}

function fmtInt(n) {
  return new Intl.NumberFormat("en-US").format(n);
}

function fmtWan(n) {
  return `${(n / 10000).toFixed(1)} 万`;
}

function cover() {
  const title = "Serenity（@aleabitoreddit）5 月以来发文深度拆解";
  const subtitle = "CPO/硅光是主线，融资质量和供应链瓶颈是方法论内核";
  let body = "";
  body += rect(82, 196, 1236, 510, C.white, { rx: 16, stroke: "#d8e0e8" });
  body += tspans(130, 276, [
    "研究对象：公开 X 发文 + X Article 摘要索引",
    "本地归档：832 条非转推公开记录（2026-05-01 至 2026-06-08 UTC）",
    "镜像增量：serenitysaid 最新 35 条覆盖至 2026-06-09 02:29 UTC",
    "5 月以来唯一长文：SIVE - The CPO Laser Chokepoint for Hyperscalers"
  ], { size: 25, lineHeight: 48, weight: 700 });
  const cards = [
    ["832", "本地归档帖子", C.blue],
    ["94.4M", "累计可见浏览", C.green],
    ["214", "$SIVE 提及", C.amber],
    ["1", "5 月以来 X Article", C.violet]
  ];
  cards.forEach((card, i) => {
    const x = 126 + i * 300;
    body += rect(x, 502, 250, 120, "#f8fafc", { rx: 14, stroke: "#d9e2ea" });
    body += text(x + 125, 554, card[0], { size: 38, weight: 800, color: card[2], anchor: "middle" });
    body += text(x + 125, 592, card[1], { size: 19, weight: 700, color: C.muted, anchor: "middle" });
  });
  body += line(105, 664, 1295, 664, { stroke: "#d4dce4" });
  body += text(130, 702, "结论：这是一个以“上游瓶颈”为核心的高频公开研究流，而不是可直接复制的交易系统。", { size: 24, weight: 800, color: C.ink });
  return base(title, subtitle, body, "数据：yan-labs/serenity-aleabitoreddit 公开归档、serenitysaid 镜像，统计时间 2026-06-09");
}

function corpusChart() {
  const title = "语料边界：本地全量归档 + 公开镜像增量";
  const subtitle = "X 时间线未登录访问不稳定，因此必须明确覆盖范围";
  let body = "";
  body += rect(82, 188, 1226, 505, C.white, { rx: 16, stroke: "#d8e0e8" });
  body += text(118, 238, "本地归档覆盖", { size: 26, weight: 800 });
  body += rect(118, 278, 850, 42, C.lightBlue, { rx: 21, stroke: C.blue, sw: 2 });
  body += rect(118, 278, 636, 42, C.blue, { rx: 21 });
  body += text(130, 306, "2026-05-01 02:31 UTC", { size: 18, color: C.white, weight: 800 });
  body += text(940, 306, "2026-06-08 08:43 UTC", { size: 18, color: C.blue, weight: 800, anchor: "end" });
  body += text(118, 362, `${corpus.localPosts} 条非转推公开记录：5 月 ${corpus.mayPosts} 条，6 月前 8 天 ${corpus.junePosts} 条`, { size: 24, weight: 800 });
  body += text(118, 402, `累计浏览 ${fmtWan(corpus.views)}、点赞 ${fmtInt(corpus.likes)}、收藏 ${fmtInt(corpus.bookmarks)}、回复 ${fmtInt(corpus.replies)}`, { size: 21, color: C.muted });

  body += text(118, 482, "镜像增量核对", { size: 26, weight: 800 });
  body += rect(118, 522, 850, 42, C.lightGreen, { rx: 21, stroke: C.green, sw: 2 });
  body += rect(782, 522, 186, 42, C.green, { rx: 21 });
  body += text(130, 550, "2026-06-07 03:37 UTC", { size: 18, color: C.green, weight: 800 });
  body += text(940, 550, "2026-06-09 02:29 UTC", { size: 18, color: C.white, weight: 800, anchor: "end" });
  body += text(118, 606, `serenitysaid 首页内嵌最新 ${corpus.mirrorLatest35} 条，其中 ${corpus.mirrorAfterArchive} 条晚于本地归档末条`, { size: 24, weight: 800 });
  body += text(118, 646, `镜像同步标签：${corpus.mirrorSync}；该镜像用于确认增量，不替代本地全量归档`, { size: 21, color: C.muted });

  body += rect(1012, 242, 242, 350, "#f8fafc", { rx: 14, stroke: "#d9e2ea" });
  body += text(1133, 296, "1", { size: 54, weight: 800, color: C.violet, anchor: "middle" });
  body += tspans(1133, 342, ["5 月以来", "X Article"], { size: 24, weight: 800, anchor: "middle", lineHeight: 34 });
  body += text(1133, 436, "2026-05-19", { size: 22, weight: 800, color: C.ink, anchor: "middle" });
  body += tspans(1133, 476, ["SIVE - The CPO", "Laser Chokepoint", "for Hyperscalers"], { size: 18, color: C.muted, anchor: "middle", lineHeight: 27 });
  return base(title, subtitle, body, "限制：无法证明删除、私密、订阅者专属或 X 登录后才可见内容已覆盖。");
}

function themeDistribution() {
  const title = "主题强度：CPO/硅光是绝对主线";
  const subtitle = "同一帖子可能命中多个主题，因此主题帖子数不相加";
  const maxPosts = Math.max(...themes.map((d) => d.posts));
  const maxViews = Math.max(...themes.map((d) => d.views));
  let body = "";
  body += rect(82, 188, 1226, 515, C.white, { rx: 16, stroke: "#d8e0e8" });
  body += text(118, 232, "帖子命中数", { size: 22, weight: 800 });
  body += text(748, 232, "累计浏览", { size: 22, weight: 800 });
  themes.forEach((d, i) => {
    const y = 268 + i * 52;
    const postW = Math.round((d.posts / maxPosts) * 465);
    const viewW = Math.round((d.views / maxViews) * 365);
    body += text(118, y + 24, d.name, { size: 19, weight: 700 });
    body += rect(385, y, 470, 28, "#eef3f7", { rx: 14 });
    body += rect(385, y, postW, 28, d.color, { rx: 14 });
    body += text(870, y + 22, `${d.posts}`, { size: 18, weight: 800, color: d.color });
    body += rect(748, y + 31, 370, 12, "#edf2f6", { rx: 6 });
    body += rect(748, y + 31, viewW, 12, d.color, { rx: 6, opacity: 0.8 });
    body += text(1134, y + 42, fmtWan(d.views), { size: 17, weight: 700, color: C.muted });
  });
  body += rect(118, 650, 1138, 34, "#f7fafc", { rx: 10, stroke: "#dde5ed" });
  body += text(138, 673, "解释：5 月以来频道的“AI”并不是泛概念，而是沿 CPO、硅光、InP、激光、封装、存储和电力继续向上游拆链。", { size: 19, weight: 700, color: C.ink });
  return base(title, subtitle, body, "方法：基于关键词规则对 832 条本地归档帖子分类，人工复核主题边界。");
}

function tickerMentions() {
  const title = "热门标的：$SIVE 是整个样本的重心";
  const subtitle = "清洗尾部标点后统计 2026-05-01 以来 ticker 去重命中";
  const maxCount = Math.max(...tickers.map((d) => d.count));
  let body = "";
  body += rect(82, 188, 1226, 515, C.white, { rx: 16, stroke: "#d8e0e8" });
  tickers.forEach((d, i) => {
    const col = i < 6 ? 0 : 1;
    const row = i % 6;
    const x = col === 0 ? 120 : 730;
    const y = 236 + row * 73;
    const barW = Math.round((d.count / maxCount) * 365);
    const color = i === 0 ? C.red : i <= 5 ? C.blue : C.slate;
    body += text(x, y + 24, d.ticker, { size: 28, weight: 800, color });
    body += rect(x + 128, y + 3, 370, 26, "#eef3f7", { rx: 13 });
    body += rect(x + 128, y + 3, barW, 26, color, { rx: 13, opacity: 0.9 });
    body += text(x + 515, y + 24, `${d.count} 次`, { size: 19, weight: 800, color });
    body += text(x + 128, y + 56, `${d.group}；触达浏览约 ${fmtWan(d.views)}`, { size: 17, color: C.muted });
  });
  body += rect(120, 687, 1150, 28, C.lightRed, { rx: 10, stroke: "#efcaca" });
  body += text(142, 707, "$SIVE 的提及数约为 $NVDA 的 2.7 倍，说明下游 AI 巨头在该频道中常被当作需求源，而不是主要交易对象。", { size: 18, weight: 800, color: C.red });
  return base(title, subtitle, body, "统计字段：text 中 $ticker 去重命中；同一帖子多次出现同一 ticker 只计 1 次。");
}

function methodologyMap() {
  const title = "方法论：从下游资本开支追到上游瓶颈";
  const subtitle = "这套框架比具体 ticker 更耐用，也更适合读者迁移使用";
  const steps = [
    ["1", "下游需求", "AI 集群、CPO、机器人、800V、存储、太空防务", C.blue],
    ["2", "BOM 拆链", "从客户、模块、封装、基板、材料、设备逐层回溯", C.cyan],
    ["3", "瓶颈识别", "找替代少、验证慢、产能稀缺、客户离不开的环节", C.red],
    ["4", "证据拼接", "公告、演讲、客户网页、财报措辞、招聘、供应商变化", C.green],
    ["5", "资本结构过滤", "融资质量、ATM、可转债、客户信用、稀释方向", C.amber],
    ["6", "仓位与校准", "区分验证事实、合理推断、自报收益和社群噪音", C.violet]
  ];
  let body = "";
  body += rect(82, 188, 1226, 515, C.white, { rx: 16, stroke: "#d8e0e8" });
  steps.forEach((s, i) => {
    const x = 124 + (i % 3) * 400;
    const y = 236 + Math.floor(i / 3) * 218;
    body += rect(x, y, 330, 150, "#f8fafc", { rx: 15, stroke: "#d9e2ea" });
    body += circle(x + 42, y + 45, 27, s[3], { opacity: 0.16, stroke: s[3], sw: 2 });
    body += text(x + 42, y + 54, s[0], { size: 24, weight: 800, color: s[3], anchor: "middle" });
    body += text(x + 84, y + 47, s[1], { size: 25, weight: 800, color: C.ink });
    body += tspans(x + 30, y + 91, wrap(s[2], 18), { size: 18, lineHeight: 25, color: C.muted, weight: 600 });
    if (i % 3 !== 2) {
      body += line(x + 340, y + 76, x + 382, y + 76, { stroke: "#b8c6d3", sw: 3 });
      body += `<polygon points="${x + 382},${y + 76} ${x + 370},${y + 68} ${x + 370},${y + 84}" fill="#b8c6d3"/>`;
    }
  });
  body += line(1192, 312, 1192, 453, { stroke: "#b8c6d3", sw: 3 });
  body += `<polygon points="1192,453 1184,439 1200,439" fill="#b8c6d3"/>`;
  body += text(124, 680, "关键判断：他真正反复强调的不是“某只股票会涨”，而是“如果这个上游点断供，下游巨额资本开支会被迫让利”。", { size: 21, weight: 800 });
  return base(title, subtitle, body, "归纳自 methodology.md、articles.md、track-record.md 与 5 月以来样本。");
}

function siveSupplyChain() {
  const title = "SIVE 长文的供应链地图：强证据与推断路径要分开";
  const subtitle = "2026-05-19 X Article 是 5 月以来唯一长文，也是组合影响最大的一篇";
  let body = "";
  body += rect(82, 188, 1226, 515, C.white, { rx: 16, stroke: "#d8e0e8" });
  body += rect(560, 330, 280, 116, C.lightRed, { rx: 18, stroke: C.red, sw: 2 });
  body += text(700, 374, "SIVE / Sivers", { size: 28, weight: 800, color: C.red, anchor: "middle" });
  body += text(700, 412, "CW/DFB 激光源", { size: 22, weight: 800, color: C.red, anchor: "middle" });
  const left = [
    ["Jabil 1.6T LRO", "公开可映射", C.blue],
    ["POET ELS 合作", "公开可映射", C.blue],
    ["Ayar Labs 路径", "伙伴页/生态变化", C.green],
    ["O-Net / Enablence", "外部光源路径", C.green]
  ];
  const right = [
    ["MRVL / Celestial", "高置信推断", C.amber],
    ["Apple / Aeva", "高置信但未确认", C.amber],
    ["AMD / GFS", "平台参考设计路径", C.violet],
    ["Nokia / defense", "期权路径", C.slate]
  ];
  left.forEach((n, i) => {
    const y = 222 + i * 96;
    body += rect(126, y, 310, 66, "#f8fafc", { rx: 12, stroke: "#d9e2ea" });
    body += text(150, y + 27, n[0], { size: 21, weight: 800, color: n[2] });
    body += text(150, y + 52, n[1], { size: 16, color: C.muted, weight: 700 });
    body += line(436, y + 33, 560, 388, { stroke: n[2], sw: 2, opacity: 0.75 });
  });
  right.forEach((n, i) => {
    const y = 222 + i * 96;
    body += rect(964, y, 310, 66, "#f8fafc", { rx: 12, stroke: "#d9e2ea" });
    body += text(988, y + 27, n[0], { size: 21, weight: 800, color: n[2] });
    body += text(988, y + 52, n[1], { size: 16, color: C.muted, weight: 700 });
    body += line(840, 388, 964, y + 33, { stroke: n[2], sw: 2, opacity: 0.75 });
  });
  body += rect(472, 570, 456, 76, "#f7fafc", { rx: 14, stroke: "#d9e2ea" });
  body += tspans(700, 600, ["投资含义：SIVE 是该频道最高上下文密度的 CPO 激光瓶颈名。", "风险：客户多源、NDA 推断、产能爬坡和收入确认仍需后续验证。"], { size: 18, lineHeight: 28, anchor: "middle", color: C.ink, weight: 700 });
  return base(title, subtitle, body, "来源：references/articles.md 对 2026-05-19 X Article 的摘要与规则化拆解。");
}

function riskCalibration() {
  const title = "如何读这个频道：把证据、推断和社群热度分层";
  const subtitle = "高传播不等于高确定性，自报收益不能替代可审计记录";
  const rows = [
    ["更硬的证据", "公司公告、财报、客户/伙伴页面、指数/持仓披露", "可以进入研究清单，但仍要回到原始披露核验", C.green],
    ["合理推断", "供应链路径、客户映射、产品路线和量产时间窗口", "适合形成假设，不能当作事实直接定价", C.blue],
    ["市场结构", "ATM、可转债、被动资金、做空/流通股动态", "常影响赔率，但需要区分建设性融资和掠夺性稀释", C.amber],
    ["社群噪音", "众包清单、粉丝数、媒体报道、短期涨跌归因", "可作线索，不应作买入理由", C.violet],
    ["未验证项", "自报收益、私信线索、NDA 客户路径、删除/订阅内容", "必须降权处理，除非拿到独立证据", C.red]
  ];
  let body = "";
  body += rect(82, 188, 1226, 515, C.white, { rx: 16, stroke: "#d8e0e8" });
  body += text(122, 236, "层级", { size: 20, weight: 800, color: C.muted });
  body += text(334, 236, "典型内容", { size: 20, weight: 800, color: C.muted });
  body += text(850, 236, "读者使用方式", { size: 20, weight: 800, color: C.muted });
  rows.forEach((r, i) => {
    const y = 270 + i * 82;
    body += rect(114, y, 1160, 66, i % 2 === 0 ? "#f8fafc" : "#ffffff", { rx: 12, stroke: "#e0e7ef" });
    body += circle(152, y + 33, 14, r[3], { opacity: 0.18, stroke: r[3], sw: 2 });
    body += text(184, y + 40, r[0], { size: 20, weight: 800, color: r[3] });
    body += text(334, y + 40, r[1], { size: 19, color: C.ink, weight: 700 });
    body += text(850, y + 40, r[2], { size: 18, color: C.muted, weight: 700 });
  });
  body += rect(114, 696, 1160, 28, C.lightAmber, { rx: 10, stroke: "#ecd2aa" });
  body += text(136, 716, "一句话：把它当作供应链雷达和研究起点，不要当作交易指令或可复制收益曲线。", { size: 18, weight: 800, color: C.amber });
  return base(title, subtitle, body, "校准参考：track-record.md 明确提示自报收益未验证，并给出方向性复核而非经纪账户审计。");
}

function dailyCadence() {
  const title = "发文节奏：高频研究流，而非低频长文媒体";
  const subtitle = "5 月以来大多数内容是状态、线程、回复和众包清单";
  const max = Math.max(...dailyPosts.map((d) => d[1]));
  const chartX = 114;
  const chartY = 242;
  const chartW = 1160;
  const chartH = 360;
  const barGap = 5;
  const barW = (chartW - barGap * (dailyPosts.length - 1)) / dailyPosts.length;
  let body = "";
  body += rect(82, 188, 1226, 515, C.white, { rx: 16, stroke: "#d8e0e8" });
  [0, 10, 20, 30, 40, 50].forEach((v) => {
    const y = chartY + chartH - (v / 55) * chartH;
    body += line(chartX, y, chartX + chartW, y, { stroke: C.grid, sw: 1 });
    body += text(chartX - 18, y + 6, v, { size: 15, color: C.muted, anchor: "end" });
  });
  dailyPosts.forEach((d, i) => {
    const h = (d[1] / max) * (chartH - 8);
    const x = chartX + i * (barW + barGap);
    const y = chartY + chartH - h;
    const color = d[0].startsWith("06") ? C.green : C.blue;
    body += rect(x, y, barW, h, color, { rx: 5, opacity: 0.88 });
    if (["05-01", "05-15", "05-30", "06-01", "06-08"].includes(d[0])) {
      body += text(x + barW / 2, chartY + chartH + 26, d[0], { size: 13, color: C.muted, anchor: "middle" });
    }
  });
  body += text(112, 652, "峰值日：2026-06-01 有 53 条；2026-05-30 有 39 条；这类账号需要按主题聚类阅读，逐条复述会失真。", { size: 21, weight: 800 });
  body += pill(1040, 635, "5 月", C.blue, 88);
  body += pill(1142, 635, "6 月", C.green, 88);
  return base(title, subtitle, body, "统计：本地归档 2026-05-01 至 2026-06-08 UTC 每日非转推公开记录。");
}

const outputs = [
  ["serenity-cover.svg", cover()],
  ["serenity-corpus-boundary.svg", corpusChart()],
  ["serenity-theme-distribution.svg", themeDistribution()],
  ["serenity-ticker-mentions.svg", tickerMentions()],
  ["serenity-methodology-map.svg", methodologyMap()],
  ["serenity-sive-supply-chain.svg", siveSupplyChain()],
  ["serenity-risk-calibration.svg", riskCalibration()],
  ["serenity-daily-cadence.svg", dailyCadence()]
];

await fs.mkdir(outDir, { recursive: true });
await Promise.all(outputs.map(([name, svg]) => fs.writeFile(path.join(outDir, name), svg)));
console.log(`Generated ${outputs.length} Serenity analysis SVGs in ${outDir}`);
