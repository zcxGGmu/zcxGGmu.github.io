import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, "..");
const outDir = path.join(rootDir, "images", "posts", "lithium-mining-battery-investment-analysis");

const W = 1400;
const H = 820;

const C = {
  paper: "#fbfcfd",
  panel: "#f3f6f8",
  ink: "#16212c",
  muted: "#63707c",
  grid: "#d8e0e7",
  blue: "#1f73b7",
  teal: "#178b83",
  green: "#4c8c57",
  amber: "#c98528",
  red: "#bd5148",
  purple: "#6d5aa6",
  slate: "#5d6b78",
  white: "#ffffff",
  softBlue: "#dcebf7",
  softGreen: "#e0efe4",
  softAmber: "#f8ead7",
  softRed: "#f5dedc",
  softPurple: "#e9e4f4"
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

function pathD(points) {
  return points.map((p, i) => `${i === 0 ? "M" : "L"} ${p[0]} ${p[1]}`).join(" ");
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
  ${text(82, 146, subtitle, { size: 21, color: C.muted })}
  ${body}
  ${text(82, 770, source, { size: 16, color: C.muted })}
</svg>
`;
}

function legend(items, x, y) {
  return items.map((item, i) => {
    const xx = x + i * item.gap;
    return `${rect(xx, y - 15, 26, 14, item.color, { rx: 4 })}${text(xx + 36, y, item.label, { size: 18, color: C.muted, weight: 700 })}`;
  }).join("\n");
}

function fmt(value, digits = 1) {
  return Number(value).toFixed(digits);
}

function cover() {
  const cards = [
    ["需求端", "EV + 储能仍在增长", "2025 全球 EV 超 2000 万辆；EV 电池部署 1.2TWh"],
    ["供给端", "矿端扩张快于消费", "USGS 估算 2025 全球矿山产量同比 +31%"],
    ["价格端", "低位修复但未回暴利期", "2026 初锂价较 2025 同期翻倍，但较 2022 高点低约 70%"],
    ["公司端", "资源、成本、现金流分化", "融捷、天齐、永兴分别对应三种上游路径"]
  ];
  let body = "";
  body += text(86, 220, "锂矿、锂电池全景投资分析", { size: 54, weight: 900, color: C.ink });
  body += text(88, 276, "重点公司：融捷股份、天齐锂业、永兴材料", { size: 30, weight: 800, color: C.blue });
  body += text(90, 326, "从供需周期、价格弹性、财务质量到技术壁垒，拆解 2026 年锂产业链的真实投资变量。", { size: 24, color: C.muted, weight: 650 });
  cards.forEach((card, i) => {
    const x = 92 + (i % 2) * 610;
    const y = 388 + Math.floor(i / 2) * 142;
    const colors = [C.softBlue, C.softGreen, C.softAmber, C.softPurple];
    const strong = [C.blue, C.green, C.amber, C.purple];
    body += rect(x, y, 560, 106, colors[i], { rx: 16, stroke: "#d7e0e8", sw: 1 });
    body += text(x + 24, y + 38, card[0], { size: 20, weight: 850, color: strong[i] });
    body += text(x + 126, y + 38, card[1], { size: 24, weight: 850 });
    body += text(x + 24, y + 74, card[2], { size: 18, weight: 700, color: C.muted });
  });
  body += line(92, 680, 1270, 680, { stroke: "#cbd6df", sw: 2 });
  body += text(92, 718, "结论先行：锂不是需求崩塌行业，而是从资源普涨进入成本曲线、现金流和产品质量竞争。", { size: 22, weight: 800, color: C.ink });
  return base(
    "锂产业链：从周期暴利回到资源与成本",
    "公开资料更新至 2026-06-09；本文不构成投资建议",
    body,
    "数据来源：IEA Global EV Outlook 2026、USGS MCS 2026、公司 2025 年报与 2026Q1 公告"
  );
}

function demandSupply() {
  const left = [
    ["全球 EV 销量", "2025 >2000 万辆", "+20%，占新车约 25%"],
    ["2026 EV 预测", "2300 万辆", "IEA 预计占新车约 28%"],
    ["EV 电池部署", "1.2 TWh", "2025 同比接近 +30%"],
    ["中国动力电池装车", "769.7 GWh", "2025 同比 +40.4%"]
  ];
  const right = [
    ["全球锂消费量", "26.3 万吨 Li", "2025 同比 +20%"],
    ["全球矿山产量", "29.0 万吨 Li", "2025 同比 +31%"],
    ["电池用途占比", "88%", "锂终端消费的主体"],
    ["全球锂储量", "3700 万吨 Li", "资源并不稀缺，低成本才稀缺"]
  ];
  let body = text(92, 205, "需求还在增长，但供给增速更快，价格压力来自供需错配。", { size: 24, weight: 800 });
  body += rect(92, 236, 580, 458, C.white, { rx: 18, stroke: "#dce3ea", sw: 1 });
  body += rect(728, 236, 580, 458, C.white, { rx: 18, stroke: "#dce3ea", sw: 1 });
  body += text(124, 286, "需求端：EV 与储能", { size: 30, weight: 850, color: C.blue });
  body += text(760, 286, "供给端：矿山与资源", { size: 30, weight: 850, color: C.green });
  left.forEach((item, i) => {
    const y = 342 + i * 78;
    body += circle(128, y - 8, 7, C.blue);
    body += text(150, y, item[0], { size: 20, weight: 800 });
    body += text(370, y, item[1], { size: 24, weight: 900, color: C.blue });
    body += text(150, y + 30, item[2], { size: 17, color: C.muted, weight: 650 });
  });
  right.forEach((item, i) => {
    const y = 342 + i * 78;
    body += circle(764, y - 8, 7, C.green);
    body += text(786, y, item[0], { size: 20, weight: 800 });
    body += text(1010, y, item[1], { size: 24, weight: 900, color: C.green });
    body += text(786, y + 30, item[2], { size: 17, color: C.muted, weight: 650 });
  });
  body += rect(144, 640, 1108, 34, "#eef3f7", { rx: 8 });
  body += text(166, 664, "投资含义：看需求不用只盯乘用车，还要看储能；看供给不用只看资源量，更要看现金成本和投产节奏。", { size: 19, weight: 750, color: C.ink });
  return base(
    "锂产业链供需：需求增长遇上矿端放量",
    "2025 年需求仍强，但矿山供给增长更快，行业从短缺转向成本曲线竞争",
    body,
    "数据来源：IEA Global EV Outlook 2026、USGS Mineral Commodity Summaries 2026、中国汽车动力电池产业创新联盟"
  );
}

function priceCycle() {
  const data = [
    { year: "2021", price: 11.7 },
    { year: "2022", price: 63.7 },
    { year: "2023", price: 39.0 },
    { year: "2024", price: 11.8 },
    { year: "2025E", price: 9.0 }
  ];
  const x0 = 146;
  const y0 = 610;
  const bw = 142;
  const gap = 72;
  const max = 70;
  let body = text(92, 205, "碳酸锂价格已经从 2022 年极端高位回落，2025 年低位震荡后边际修复。", { size: 24, weight: 800 });
  body += legend([
    { label: "电池级碳酸锂年均价（千美元/吨）", color: C.amber, gap: 315 },
    { label: "周期解释", color: C.blue, gap: 150 }
  ], 822, 194);
  body += line(120, y0, 810, y0, { stroke: "#b9c7d3", sw: 2 });
  [0, 20, 40, 60].forEach((tick) => {
    const y = y0 - tick / max * 360;
    body += line(120, y, 810, y, { stroke: C.grid, sw: 1 });
    body += text(90, y + 6, tick, { size: 16, color: C.muted, anchor: "end" });
  });
  data.forEach((d, i) => {
    const x = x0 + i * (bw + gap);
    const h = d.price / max * 360;
    body += rect(x, y0 - h, bw, h, C.amber, { rx: 10 });
    body += text(x + bw / 2, y0 - h - 14, fmt(d.price, 1), { size: 20, color: C.amber, weight: 850, anchor: "middle" });
    body += text(x + bw / 2, y0 + 34, d.year, { size: 18, color: C.muted, weight: 800, anchor: "middle" });
  });
  const notes = [
    ["2022", "供应短缺 + EV 放量，价格极端化"],
    ["2024", "扩产集中释放，价格跌回现金成本压力区"],
    ["2026 初", "IEA 称较 2025 同期翻倍以上，但仍低于 2022 高点约 70%"]
  ];
  notes.forEach((n, i) => {
    const y = 280 + i * 112;
    body += rect(910, y, 360, 78, [C.softAmber, C.softRed, C.softBlue][i], { rx: 14, stroke: "#dce3ea", sw: 1 });
    body += text(934, y + 31, n[0], { size: 22, weight: 900, color: [C.amber, C.red, C.blue][i] });
    body += wrapText(1010, y + 31, n[1], 18, 26, { size: 18, color: C.ink, weight: 750 });
  });
  body += text(120, 708, "读法：价格反弹会先改善矿端利润，但只有低成本、现金流稳定、客户认证强的公司能穿越下一轮下行。", { size: 19, color: C.muted, weight: 750 });
  return base(
    "锂价周期：从暴利到修复，而不是回到短缺神话",
    "USGS 年均价口径；2026 年状态采用 IEA 趋势描述",
    body,
    "数据来源：USGS MCS 2026 Lithium；IEA Global EV Outlook 2026 Batteries"
  );
}

function companyFinancials() {
  const companies = [
    {
      name: "融捷股份",
      color: C.blue,
      rev: [12.11, 5.61, 8.40, 3.76],
      profit: [3.80, 2.15, 2.79, 2.78],
      note: "国内硬岩矿弹性高，2026Q1 利润受锂精矿量价与联营投资收益拉动。"
    },
    {
      name: "天齐锂业",
      color: C.green,
      rev: [405.03, 130.63, 103.46, 51.28],
      profit: [72.97, -79.05, 4.63, 18.76],
      note: "全球资源最强，利润受锂价、SQM 权益法、少数股东和汇率共同影响。"
    },
    {
      name: "永兴材料",
      color: C.amber,
      rev: [121.89, 80.74, 74.23, 24.29],
      profit: [34.07, 10.43, 6.61, 4.89],
      note: "锂云母一体化 + 特钢底盘，锂价上行弹性被双主业结构部分摊薄。"
    }
  ];
  const years = ["2023", "2024", "2025", "2026Q1"];
  const chartX = 115;
  const chartY = 254;
  const chartW = 720;
  const chartH = 360;
  let body = text(92, 205, "2026Q1 三家公司利润均修复，但修复来源和可持续性不同。", { size: 24, weight: 800 });
  body += rect(96, 230, 782, 450, C.white, { rx: 18, stroke: "#dce3ea", sw: 1 });
  body += text(chartX, 252, "归母净利润（亿元）", { size: 20, weight: 850 });
  [-80, -40, 0, 40, 80].forEach((tick) => {
    const y = chartY + chartH - ((tick + 80) / 160) * chartH;
    body += line(chartX, y, chartX + chartW, y, { stroke: tick === 0 ? "#9aabb7" : C.grid, sw: tick === 0 ? 2 : 1 });
    body += text(chartX - 14, y + 6, tick, { size: 15, color: C.muted, anchor: "end" });
  });
  companies.forEach((co, ci) => {
    const pts = co.profit.map((v, i) => {
      const x = chartX + 86 + i * 185;
      const y = chartY + chartH - ((v + 80) / 160) * chartH;
      return [x, y];
    });
    body += `<path d="${pathD(pts)}" fill="none" stroke="${co.color}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>`;
    pts.forEach((p, i) => {
      body += circle(p[0], p[1], 7, co.color, { stroke: C.white, sw: 3 });
      body += text(p[0], p[1] - 13, fmt(co.profit[i], co.profit[i] < 0 ? 1 : 2), { size: 15, weight: 800, color: co.color, anchor: "middle" });
    });
  });
  years.forEach((year, i) => {
    body += text(chartX + 86 + i * 185, chartY + chartH + 34, year, { size: 17, color: C.muted, weight: 800, anchor: "middle" });
  });
  body += legend([
    { label: "融捷", color: C.blue, gap: 90 },
    { label: "天齐", color: C.green, gap: 90 },
    { label: "永兴", color: C.amber, gap: 90 }
  ], 575, 254);
  companies.forEach((co, i) => {
    const y = 248 + i * 140;
    body += rect(925, y, 330, 106, [C.softBlue, C.softGreen, C.softAmber][i], { rx: 14, stroke: "#dce3ea", sw: 1 });
    body += text(950, y + 35, co.name, { size: 24, color: co.color, weight: 900 });
    body += text(950, y + 69, `2026Q1 收入 ${fmt(co.rev[3], 2)} 亿，归母 ${fmt(co.profit[3], 2)} 亿`, { size: 18, weight: 750 });
    body += wrapText(950, y + 96, co.note, 19, 24, { size: 16, color: C.muted, weight: 650 });
  });
  return base(
    "三家公司财务弹性：同样修复，不同驱动",
    "金额为人民币亿元；2026Q1 为单季数，未年化",
    body,
    "数据来源：融捷股份、天齐锂业、永兴材料 2025 年报及 2026Q1 公告"
  );
}

function resourceCapacity() {
  const rows = [
    ["融捷股份", "甲基卡 134 号脉", "锂辉石", "105 万吨/年采矿，45 万吨/年选矿；锂精矿 18.56 万吨", C.blue],
    ["天齐锂业", "Greenbushes / SQM / 扎布耶", "硬岩 + 盐湖权益", "Greenbushes 锂精矿产能约 214 万吨/年；锂化工约 12.16 万吨/年", C.green],
    ["永兴材料", "宜丰化山瓷石矿", "锂云母 / 锂瓷石", "采选冶一体化；2025 碳酸锂收入 16.15 亿元、毛利率 33.4%", C.amber]
  ];
  let body = text(92, 205, "三家公司代表三条不同的上游路径：国内硬岩、全球硬岩 + 盐湖、国内锂云母。", { size: 24, weight: 800 });
  rows.forEach((row, i) => {
    const y = 250 + i * 145;
    body += rect(96, y, 1208, 112, C.white, { rx: 16, stroke: "#dce3ea", sw: 1 });
    body += rect(96, y, 12, 112, row[4], { rx: 6 });
    body += text(128, y + 42, row[0], { size: 28, weight: 900, color: row[4] });
    body += text(340, y + 42, row[1], { size: 25, weight: 850 });
    body += rect(340, y + 62, 170, 30, row[4], { rx: 8, opacity: 0.14 });
    body += text(356, y + 84, row[2], { size: 17, weight: 800, color: row[4] });
    body += wrapText(575, y + 43, row[3], 38, 27, { size: 20, color: C.ink, weight: 750 });
  });
  body += rect(126, 690, 1148, 44, "#eef3f7", { rx: 10 });
  body += text(150, 719, "投资含义：不要只比较“吨数”，还要比较资源禀赋、选矿回收率、锂盐转化率、客户认证和环保约束。", { size: 19, color: C.muted, weight: 750 });
  return base(
    "资源与产能：三种路径，三种风险收益特征",
    "锂辉石、盐湖、锂云母的成本曲线和扩产弹性并不相同",
    body,
    "数据来源：三家公司 2025 年报；公司公告披露口径"
  );
}

function moatMatrix() {
  const factors = ["资源禀赋", "成本位置", "产品质量", "客户认证", "现金流韧性", "扩产确定性"];
  const scores = [
    { name: "融捷", color: C.blue, values: [4, 4, 3, 3, 3, 3] },
    { name: "天齐", color: C.green, values: [5, 4, 5, 5, 4, 4] },
    { name: "永兴", color: C.amber, values: [3, 4, 4, 4, 5, 4] }
  ];
  const cx = 700;
  const cy = 430;
  const r = 250;
  const angle = (i) => -Math.PI / 2 + i * (Math.PI * 2 / factors.length);
  let body = text(92, 205, "技术壁垒不是单一专利，而是资源、工艺、客户认证和环保能力的组合。", { size: 24, weight: 800 });
  [1, 2, 3, 4, 5].forEach((level) => {
    const pts = factors.map((_, i) => {
      const a = angle(i);
      return `${cx + Math.cos(a) * r * level / 5},${cy + Math.sin(a) * r * level / 5}`;
    }).join(" ");
    body += polygon(pts, "none", { stroke: C.grid, sw: 1 });
  });
  factors.forEach((factor, i) => {
    const a = angle(i);
    const x = cx + Math.cos(a) * (r + 62);
    const y = cy + Math.sin(a) * (r + 62);
    body += line(cx, cy, cx + Math.cos(a) * r, cy + Math.sin(a) * r, { stroke: C.grid, sw: 1 });
    body += text(x, y + 6, factor, { size: 19, weight: 850, color: C.ink, anchor: x < cx - 20 ? "end" : x > cx + 20 ? "start" : "middle" });
  });
  scores.forEach((s, idx) => {
    const pts = s.values.map((v, i) => {
      const a = angle(i);
      return [cx + Math.cos(a) * r * v / 5, cy + Math.sin(a) * r * v / 5];
    });
    body += `<path d="${pathD(pts)} Z" fill="${s.color}" opacity="${0.14 + idx * 0.03}" stroke="${s.color}" stroke-width="3"/>`;
  });
  body += legend([
    { label: "融捷", color: C.blue, gap: 92 },
    { label: "天齐", color: C.green, gap: 92 },
    { label: "永兴", color: C.amber, gap: 92 }
  ], 1020, 230);
  const notes = [
    ["融捷", "国内高品位锂辉石矿弹性强，但并表锂盐规模小，扩产进度需跟踪。", C.blue],
    ["天齐", "全球资源和客户认证最完整，是上游核心资产，但海外和权益法变量多。", C.green],
    ["永兴", "锂云母工艺与特钢现金流构成韧性，长期看环保和低品位成本纪律。", C.amber]
  ];
  notes.forEach((n, i) => {
    const y = 578 + i * 48;
    body += circle(1020, y - 7, 7, n[2]);
    body += text(1040, y, n[0], { size: 18, color: n[2], weight: 900 });
    body += text(1098, y, n[1], { size: 16, color: C.muted, weight: 650 });
  });
  return base(
    "技术壁垒与护城河：资源、工艺、认证和环保",
    "5 分为相对更强；为研究框架评分，不是投资评级",
    body,
    "数据来源：公司年报、产品/质量体系披露；评分为基于公开资料的研究判断"
  );
}

async function main() {
  await fs.mkdir(outDir, { recursive: true });
  const charts = {
    "lithium-cover.svg": cover(),
    "lithium-demand-supply.svg": demandSupply(),
    "lithium-price-cycle.svg": priceCycle(),
    "lithium-company-financials.svg": companyFinancials(),
    "lithium-resource-capacity.svg": resourceCapacity(),
    "lithium-moat-matrix.svg": moatMatrix()
  };
  await Promise.all(Object.entries(charts).map(([name, svg]) => fs.writeFile(path.join(outDir, name), svg, "utf8")));
}

await main();
