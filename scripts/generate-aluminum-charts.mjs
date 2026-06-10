import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, "..");
const outDir = path.join(rootDir, "images", "posts", "china-hongqiao-vs-chalco-investment-analysis");

const W = 1400;
const H = 820;

const C = {
  paper: "#fbfcfd",
  panel: "#f4f7f9",
  ink: "#17212b",
  muted: "#65737e",
  grid: "#d6dfe7",
  hongqiao: "#1f76b4",
  hongqiaoSoft: "#dcebf6",
  chalco: "#b56f26",
  chalcoSoft: "#f4e4d2",
  green: "#4f8b5f",
  greenSoft: "#dfeee4",
  teal: "#178b83",
  tealSoft: "#dcefeb",
  purple: "#6f5aa8",
  purpleSoft: "#e9e5f5",
  red: "#b84e4e",
  amber: "#c78a2d",
  slate: "#536575",
  white: "#ffffff"
};

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
    size = 24,
    weight = 500,
    color = C.ink,
    anchor = "start",
    family = "Arial, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif"
  } = opts;
  return `<text x="${x}" y="${y}" fill="${color}" font-family="${family}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}">${esc(value)}</text>`;
}

function tspans(x, y, lines, opts = {}) {
  const lineHeight = opts.lineHeight || 30;
  const attrs = `x="${x}" y="${y}" fill="${opts.color || C.ink}" font-family="${opts.family || "Arial, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif"}" font-size="${opts.size || 22}" font-weight="${opts.weight || 500}" text-anchor="${opts.anchor || "start"}"`;
  return `<text ${attrs}>${lines.map((line, i) => `<tspan x="${x}" dy="${i === 0 ? 0 : lineHeight}">${esc(line)}</tspan>`).join("")}</text>`;
}

function wrapText(x, y, value, maxChars, lineHeight, opts = {}) {
  const lines = [];
  let current = "";
  for (const ch of String(value)) {
    if ((current + ch).length > maxChars) {
      lines.push(current);
      current = ch;
    } else {
      current += ch;
    }
  }
  if (current) lines.push(current);
  return tspans(x, y, lines, { ...opts, lineHeight });
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

function polygon(points, fill, opts = {}) {
  const { stroke = "none", sw = 0, opacity = 1 } = opts;
  return `<polygon points="${points}" fill="${fill}" stroke="${stroke}" stroke-width="${sw}" opacity="${opacity}"/>`;
}

function base(title, subtitle, body, source) {
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" role="img" aria-labelledby="title desc">
  <title id="title">${esc(title)}</title>
  <desc id="desc">${esc(subtitle)}</desc>
  <rect width="${W}" height="${H}" fill="${C.paper}"/>
  <rect x="36" y="32" width="${W - 72}" height="${H - 64}" rx="22" fill="${C.panel}" stroke="#dce3ea"/>
  ${text(82, 102, title, { size: 40, weight: 850 })}
  ${text(82, 146, subtitle, { size: 21, color: C.muted, weight: 650 })}
  ${body}
  ${text(82, 770, source, { size: 16, color: C.muted })}
</svg>
`;
}

function legend(items, x, y) {
  return items.map((item, i) => {
    const xx = x + i * item.gap;
    return `${rect(xx, y - 15, 26, 14, item.color, { rx: 4 })}${text(xx + 36, y, item.label, { size: 18, color: C.muted, weight: 750 })}`;
  }).join("\n");
}

function fmt(value, digits = 1) {
  return Number(value).toFixed(digits);
}

function cover() {
  const cards = [
    ["宏桥", "成本效率 + 民营一体化", "铝合金销量 582.4 万吨；氧化铝销量 1339.7 万吨"],
    ["中铝", "央企资源 + 全品类平台", "氧化铝产量 1735 万吨；电解铝产量 808 万吨"],
    ["行业", "供给总量受限", "中国原铝接近约 4500 万吨产能天花板"],
    ["趋势", "绿色铝与资源安全", "云南水电、几内亚矿、CBAM 与低碳认证成为估值变量"]
  ];
  let body = "";
  body += text(86, 218, "中国宏桥 vs 中国铝业", { size: 56, weight: 920 });
  body += text(88, 278, "从铝土矿、氧化铝、电解铝到绿色铝的投资分析", { size: 31, weight: 850, color: C.hongqiao });
  body += text(90, 326, "铝行业的核心问题不是谁收入更大，而是谁在资源、能源、成本曲线和产品平台上更能穿越周期。", { size: 23, color: C.muted, weight: 680 });
  cards.forEach((card, i) => {
    const x = 92 + (i % 2) * 610;
    const y = 388 + Math.floor(i / 2) * 138;
    const fills = [C.hongqiaoSoft, C.chalcoSoft, C.greenSoft, C.purpleSoft];
    const colors = [C.hongqiao, C.chalco, C.green, C.purple];
    body += rect(x, y, 560, 104, fills[i], { rx: 16, stroke: "#d7e0e8", sw: 1 });
    body += text(x + 24, y + 38, card[0], { size: 21, weight: 900, color: colors[i] });
    body += text(x + 126, y + 38, card[1], { size: 24, weight: 850 });
    body += text(x + 24, y + 74, card[2], { size: 18, weight: 700, color: C.muted });
  });
  body += line(92, 676, 1270, 676, { stroke: "#cbd6df", sw: 2 });
  body += text(92, 716, "结论先行：宏桥偏成本弹性，中铝偏资源平台；两者都受益于铝价，但利润来源和风险暴露明显不同。", { size: 22, weight: 850 });
  return base(
    "中国宏桥 vs 中国铝业：铝产业链投资框架",
    "公开资料更新至 2026-06-11；本文不构成投资建议",
    body,
    "数据来源：公司 2025 年报/业绩公告、2026Q1 报、USGS、IAI、World Bank"
  );
}

function valueChain() {
  const stages = [
    ["铝土矿", "几内亚/澳洲/中国", "资源禀赋与海运风险"],
    ["氧化铝", "拜耳法冶金级氧化铝", "矿石、烧碱、能源成本"],
    ["电解铝", "原铝/铝液/铝锭", "电力成本与碳排约束"],
    ["铝加工", "铝合金、板带箔、型材", "客户认证与产品结构"],
    ["终端需求", "交通、电网、光伏、包装", "地产弱化，新能源增强"]
  ];
  let body = text(92, 205, "铝的投资逻辑沿着“矿石 - 氧化铝 - 电解铝 - 加工 - 需求”传导。", { size: 24, weight: 830 });
  stages.forEach((s, i) => {
    const x = 88 + i * 252;
    const y = 276;
    const colors = [C.green, C.teal, C.hongqiao, C.chalco, C.purple];
    const soft = [C.greenSoft, C.tealSoft, C.hongqiaoSoft, C.chalcoSoft, C.purpleSoft];
    body += rect(x, y, 210, 210, soft[i], { rx: 16, stroke: "#d7e0e8", sw: 1 });
    body += circle(x + 42, y + 48, 18, colors[i]);
    body += text(x + 72, y + 56, s[0], { size: 25, weight: 900, color: colors[i] });
    body += wrapText(x + 24, y + 102, s[1], 12, 28, { size: 20, weight: 800 });
    body += wrapText(x + 24, y + 158, s[2], 13, 25, { size: 17, color: C.muted, weight: 700 });
    if (i < stages.length - 1) {
      body += line(x + 210, y + 104, x + 252, y + 104, { stroke: "#aab8c4", sw: 3 });
      body += polygon(`${x + 252},${y + 104} ${x + 238},${y + 96} ${x + 238},${y + 112}`, "#aab8c4");
    }
  });
  const companyRows = [
    ["中国宏桥", "几内亚资源/物流 + 山东/云南基地", "氧化铝、铝合金、电解铝、深加工均有布局，核心在成本曲线和规模效率。", C.hongqiao, C.hongqiaoSoft],
    ["中国铝业", "央企资源平台 + 国内多基地", "铝土矿、氧化铝、原铝、能源、贸易、高纯铝/镓等产品线更完整。", C.chalco, C.chalcoSoft]
  ];
  companyRows.forEach((row, i) => {
    const y = 552 + i * 78;
    body += rect(112, y, 1172, 58, row[4], { rx: 14, stroke: "#d7e0e8", sw: 1 });
    body += text(138, y + 37, row[0], { size: 23, weight: 900, color: row[3] });
    body += text(300, y + 37, row[1], { size: 20, weight: 800 });
    body += text(650, y + 37, row[2], { size: 18, weight: 700, color: C.muted });
  });
  return base(
    "铝产业链：利润在矿、氧化铝、电力和加工之间迁移",
    "宏桥更像成本效率型一体化平台；中铝更像资源、产品和政策平台型央企",
    body,
    "数据来源：USGS MCS 2026、IAI、公司年报；链条结构为本文整理"
  );
}

function financials() {
  const metrics = [
    ["收入", 1623.54, 2411.25, 2600, "亿元"],
    ["归母净利润", 226.36, 126.74, 250, "亿元"],
    ["经营现金流", 389.95, 340.92, 430, "亿元"],
    ["资本开支", 106.57, 151.48, 180, "亿元"],
    ["毛利率", 25.6, 18.03, 30, "%"],
    ["资产负债率", 42.2, 46.01, 55, "%"]
  ];
  let body = legend([
    { label: "中国宏桥", color: C.hongqiao, gap: 142 },
    { label: "中国铝业", color: C.chalco, gap: 150 }
  ], 992, 194);
  body += text(92, 205, "2025 年：中铝收入更大，宏桥利润率与归母利润更高。", { size: 24, weight: 830 });
  const x0 = 128;
  const y0 = 250;
  const barW = 760;
  metrics.forEach((m, i) => {
    const y = y0 + i * 72;
    const hqW = m[1] / m[3] * barW;
    const chW = m[2] / m[3] * barW;
    body += text(x0, y + 12, `${m[0]}（${m[4]}）`, { size: 19, color: C.muted, weight: 780 });
    body += rect(x0 + 160, y - 16, barW, 20, "#e7edf2", { rx: 7 });
    body += rect(x0 + 160, y - 16, hqW, 20, C.hongqiao, { rx: 7 });
    body += text(x0 + 930, y + 1, fmt(m[1], m[4] === "%" ? 1 : 0), { size: 18, weight: 850, color: C.hongqiao });
    body += rect(x0 + 160, y + 18, barW, 20, "#e7edf2", { rx: 7 });
    body += rect(x0 + 160, y + 18, chW, 20, C.chalco, { rx: 7 });
    body += text(x0 + 930, y + 35, fmt(m[2], m[4] === "%" ? 1 : 0), { size: 18, weight: 850, color: C.chalco });
  });
  body += rect(1020, 288, 248, 284, C.white, { rx: 16, stroke: "#dce3ea", sw: 1 });
  body += text(1048, 334, "读图要点", { size: 26, weight: 900 });
  body += tspans(1048, 382, [
    "1. 中铝收入含贸易属性，",
    "   收入规模不等于利润厚度。",
    "2. 宏桥利润弹性来自",
    "   铝价、氧化铝和成本曲线。",
    "3. 两家公司现金流都强，",
    "   但扩产与资源投入消耗资本。"
  ], { size: 18, color: C.muted, weight: 720, lineHeight: 29 });
  return base(
    "2025 财务对比：规模、利润和现金流",
    "单位为人民币亿元；宏桥为港股披露口径，中铝为中国会计准则口径",
    body,
    "数据来源：中国宏桥 2025 年业绩公告；中国铝业 2025 年年度报告"
  );
}

function revenueMix() {
  const hq = [
    ["铝合金产品", 65.3, C.hongqiao],
    ["氧化铝", 23.9, C.green],
    ["深加工铝产品", 9.2, C.chalco],
    ["其他/蒸汽", 1.6, C.slate]
  ];
  const ch = [
    ["原铝分部", 1455.64, C.chalco],
    ["氧化铝分部", 615.85, C.green],
    ["能源分部", 81.82, C.teal],
    ["营销/贸易分部", 1421.82, C.slate]
  ];
  let body = text(92, 205, "宏桥以铝合金和氧化铝为主；中铝分部更宽，但营销分部收入毛利率低。", { size: 24, weight: 830 });
  body += rect(92, 250, 570, 414, C.white, { rx: 18, stroke: "#dce3ea", sw: 1 });
  body += rect(738, 250, 570, 414, C.white, { rx: 18, stroke: "#dce3ea", sw: 1 });
  body += text(124, 302, "中国宏桥 2025 收入构成", { size: 28, weight: 900, color: C.hongqiao });
  body += text(770, 302, "中国铝业 2025 分部收入", { size: 28, weight: 900, color: C.chalco });
  let start = 0;
  hq.forEach((item, i) => {
    const x = 124 + start / 100 * 480;
    const w = item[1] / 100 * 480;
    body += rect(x, 342, w, 42, item[2], { rx: i === 0 || i === hq.length - 1 ? 8 : 0 });
    start += item[1];
  });
  hq.forEach((item, i) => {
    const y = 430 + i * 52;
    body += rect(126, y - 18, 22, 14, item[2], { rx: 4 });
    body += text(162, y, item[0], { size: 20, weight: 800 });
    body += text(582, y, `${fmt(item[1], 1)}%`, { size: 21, weight: 900, color: item[2], anchor: "end" });
  });
  const max = 1500;
  ch.forEach((item, i) => {
    const y = 350 + i * 70;
    const w = item[1] / max * 380;
    body += text(770, y, item[0], { size: 20, weight: 800 });
    body += rect(942, y - 24, 300, 28, "#edf2f6", { rx: 8 });
    body += rect(942, y - 24, Math.min(w, 300), 28, item[2], { rx: 8 });
    body += text(1252, y, `${fmt(item[1], 0)}亿`, { size: 20, weight: 900, color: item[2], anchor: "end" });
  });
  body += wrapText(770, 624, "注：中铝分部收入含营销/贸易等业务，不能直接等同于合并收入占比；该图用于展示经营重心和利润来源。", 31, 25, { size: 17, color: C.muted, weight: 700 });
  return base(
    "收入结构：宏桥集中，中铝平台更宽",
    "宏桥为合并收入构成；中铝为年报分部收入披露",
    body,
    "数据来源：中国宏桥 2025 年业绩公告；中国铝业 2025 年年度报告"
  );
}

function outputCapacity() {
  const rows = [
    ["宏桥：铝合金销量", 5.824, 9, "百万吨", C.hongqiao],
    ["宏桥：氧化铝销量", 13.397, 18, "百万吨", C.green],
    ["宏桥：深加工铝产品销量", 0.716, 2, "百万吨", C.chalco],
    ["中铝：氧化铝产量", 17.35, 18, "百万吨", C.green],
    ["中铝：电解铝产量", 8.08, 9, "百万吨", C.chalco],
    ["中铝：电解铝销量", 8.07, 9, "百万吨", C.purple]
  ];
  let body = text(92, 205, "中铝在氧化铝和电解铝产量上更大；宏桥在民营一体化成本与销量效率上更突出。", { size: 24, weight: 830 });
  const x0 = 132;
  rows.forEach((r, i) => {
    const y = 266 + i * 72;
    body += text(x0, y, r[0], { size: 20, weight: 800, color: i < 3 ? C.hongqiao : C.chalco });
    body += rect(x0 + 330, y - 24, 650, 30, "#e7edf2", { rx: 9 });
    body += rect(x0 + 330, y - 24, r[1] / r[2] * 650, 30, r[4], { rx: 9 });
    body += text(x0 + 1010, y, `${fmt(r[1], 2)} ${r[3]}`, { size: 21, weight: 900, color: r[4] });
  });
  body += rect(128, 690, 1132, 40, "#eef3f7", { rx: 10 });
  body += text(150, 716, "投资含义：产量越大越接近行业贝塔；低成本、资源自给、绿电比例和产品结构决定利润留存。", { size: 19, color: C.muted, weight: 760 });
  return base(
    "产销规模：氧化铝、电解铝与加工端",
    "2025 年披露数据；宏桥为销量，中铝为产量/销量，口径不同但可观察规模位置",
    body,
    "数据来源：中国宏桥 2025 年业绩公告；中国铝业 2025 年年度报告"
  );
}

function pricePolicy() {
  const prices = [
    ["2025 均价", 2632],
    ["2026Q1", 3193],
    ["2026年4月", 3600]
  ];
  const x0 = 132;
  const y0 = 596;
  const max = 4000;
  let body = text(92, 205, "铝价上行提供利润弹性，但氧化铝、电力、阳极和碳成本会重新分配利润。", { size: 24, weight: 830 });
  body += rect(100, 246, 620, 426, C.white, { rx: 18, stroke: "#dce3ea", sw: 1 });
  body += text(132, 296, "World Bank 铝价快照", { size: 28, weight: 900, color: C.hongqiao });
  [0, 1000, 2000, 3000, 4000].forEach((tick) => {
    const y = y0 - tick / max * 260;
    body += line(x0, y, 644, y, { stroke: C.grid, sw: 1 });
    body += text(x0 - 18, y + 6, tick, { size: 15, color: C.muted, anchor: "end" });
  });
  prices.forEach((p, i) => {
    const x = x0 + 58 + i * 160;
    const h = p[1] / max * 260;
    body += rect(x, y0 - h, 82, h, [C.hongqiao, C.green, C.chalco][i], { rx: 10 });
    body += text(x + 41, y0 - h - 14, p[1], { size: 20, weight: 900, color: [C.hongqiao, C.green, C.chalco][i], anchor: "middle" });
    body += text(x + 41, y0 + 34, p[0], { size: 17, weight: 800, color: C.muted, anchor: "middle" });
  });
  body += text(132, 644, "单位：美元/吨", { size: 16, color: C.muted, weight: 700 });
  const factors = [
    ["供给约束", "电解铝新增产能受控，运行率和置换决定边际供给。", C.green, C.greenSoft],
    ["能源结构", "云南水电降低碳足迹，但枯水期限电会影响产量。", C.hongqiao, C.hongqiaoSoft],
    ["资源安全", "几内亚铝土矿、港口铁路和海运扰动影响氧化铝成本。", C.chalco, C.chalcoSoft],
    ["低碳认证", "CBAM、绿电交易和再生铝提升长期产品分层。", C.purple, C.purpleSoft]
  ];
  factors.forEach((f, i) => {
    const x = 780;
    const y = 258 + i * 102;
    body += rect(x, y, 486, 76, f[3], { rx: 14, stroke: "#d7e0e8", sw: 1 });
    body += text(x + 24, y + 32, f[0], { size: 21, weight: 900, color: f[2] });
    body += wrapText(x + 132, y + 30, f[1], 20, 25, { size: 17, color: C.ink, weight: 700 });
  });
  return base(
    "价格与政策：高铝价不等于高利润",
    "利润弹性取决于铝价与氧化铝、电力、阳极、碳成本之间的剪刀差",
    body,
    "数据来源：World Bank Pink Sheet 2026-05、USGS、IAI、LME 公开资料入口"
  );
}

function moatMatrix() {
  const rows = [
    ["规模/成本曲线", 5.0, 4.6, "宏桥成本效率强；中铝规模更大但资产更复杂"],
    ["上游资源", 4.2, 4.8, "宏桥依托几内亚链条；中铝国内外资源和央企平台更宽"],
    ["能源/绿色铝", 4.0, 4.1, "两者均推进云南等清洁能源布局，但有枯水期限电风险"],
    ["产品平台宽度", 3.5, 4.8, "中铝产品覆盖氧化铝、原铝、高纯铝、镓、能源、贸易"],
    ["技术与工艺", 3.8, 4.3, "宏桥强在大槽型和一体化制造；中铝强在研发体系与品类"],
    ["资本/政策资源", 3.2, 5.0, "中铝央企属性在资源整合、融资和战略任务上更强"]
  ];
  let body = legend([
    { label: "中国宏桥", color: C.hongqiao, gap: 142 },
    { label: "中国铝业", color: C.chalco, gap: 150 }
  ], 1000, 194);
  body += text(92, 205, "护城河不是单一技术，而是资源、能源、成本、产品与资本的组合。", { size: 24, weight: 830 });
  const x0 = 122;
  const y0 = 268;
  rows.forEach((r, i) => {
    const y = y0 + i * 70;
    body += text(x0, y, r[0], { size: 20, weight: 850 });
    body += rect(x0 + 220, y - 22, 300, 24, "#e7edf2", { rx: 8 });
    body += rect(x0 + 220, y - 22, r[1] / 5 * 300, 24, C.hongqiao, { rx: 8 });
    body += text(x0 + 538, y - 2, fmt(r[1], 1), { size: 18, weight: 900, color: C.hongqiao });
    body += rect(x0 + 590, y - 22, 300, 24, "#e7edf2", { rx: 8 });
    body += rect(x0 + 590, y - 22, r[2] / 5 * 300, 24, C.chalco, { rx: 8 });
    body += text(x0 + 908, y - 2, fmt(r[2], 1), { size: 18, weight: 900, color: C.chalco });
    body += text(x0 + 970, y - 2, r[3], { size: 16, color: C.muted, weight: 680 });
  });
  body += rect(120, 704, 1160, 34, "#eef3f7", { rx: 8 });
  body += text(140, 728, "评分为本文基于公开披露的主观框架，不是财务预测；应结合铝价、电力、氧化铝和资本开支动态更新。", { size: 18, color: C.muted, weight: 750 });
  return base(
    "技术与竞争壁垒：宏桥成本弹性 vs 中铝平台资源",
    "5 分制：越高代表该维度公开可见的竞争壁垒越强",
    body,
    "数据来源：公司年报/业绩公告、公开行业资料；评分为本文整理"
  );
}

async function main() {
  await fs.mkdir(outDir, { recursive: true });
  const charts = {
    "aluminum-cover.svg": cover(),
    "aluminum-value-chain.svg": valueChain(),
    "aluminum-financials.svg": financials(),
    "aluminum-revenue-mix.svg": revenueMix(),
    "aluminum-output-capacity.svg": outputCapacity(),
    "aluminum-price-policy.svg": pricePolicy(),
    "aluminum-moat-matrix.svg": moatMatrix()
  };
  await Promise.all(Object.entries(charts).map(([name, svg]) => fs.writeFile(path.join(outDir, name), svg, "utf8")));
}

await main();
