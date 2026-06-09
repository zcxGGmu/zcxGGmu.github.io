import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, "..");
const outDir = path.join(rootDir, "images", "posts", "smic-huahong-investment-analysis");

const W = 1400;
const H = 820;
const C = {
  ink: "#17212b",
  muted: "#65737e",
  grid: "#d5dde5",
  paper: "#fbfcfd",
  panel: "#f4f7f9",
  smic: "#1b76b8",
  smicSoft: "#d9ebf7",
  hua: "#c77d1f",
  huaSoft: "#f6e8d3",
  green: "#558b5b",
  red: "#b94b4b",
  teal: "#198c7c",
  purple: "#6f5aa8",
  gray: "#8d98a3",
  dark: "#111a22",
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
  ${text(82, 102, title, { size: 40, weight: 800 })}
  ${text(82, 146, subtitle, { size: 21, color: C.muted })}
  ${body}
  ${text(82, 770, source, { size: 16, color: C.muted })}
</svg>
`;
}

function legend(items, x, y) {
  return items.map((item, i) => {
    const xx = x + i * item.gap;
    return `${rect(xx, y - 15, 26, 14, item.color, { rx: 4 })}${text(xx + 36, y, item.label, { size: 18, color: C.muted })}`;
  }).join("\n");
}

function pct(v) {
  return `${v.toFixed(1)}%`;
}

function fmt(v, digits = 1) {
  return Number(v).toFixed(digits);
}

function financialScale() {
  const groups = [
    {
      label: "2025 收入",
      unit: "十亿美元",
      max: 10,
      smic: 9.327,
      hua: 2.402,
      notes: ["中芯收入约为华虹 3.9 倍", "体量优势意味着客户覆盖和产能调度空间更大"]
    },
    {
      label: "2026Q1 收入",
      unit: "十亿美元",
      max: 2.7,
      smic: 2.505,
      hua: 0.661,
      notes: ["华虹同比增速更高", "中芯 Q2 指引环比 +14% 至 +16%"]
    },
    {
      label: "2025 归母利润",
      unit: "亿美元",
      max: 7.5,
      smic: 6.851,
      hua: 0.549,
      notes: ["华虹集团口径仍亏损", "新产线少数股东损益影响大"]
    }
  ];
  const x0 = 120;
  const y0 = 238;
  const barW = 720;
  const barH = 34;
  let body = legend([
    { label: "中芯国际", color: C.smic, gap: 132 },
    { label: "华虹半导体", color: C.hua, gap: 160 }
  ], 1010, 194);
  body += text(92, 205, "财务体量：中芯是规模型龙头，华虹是特色工艺型选手。", { size: 24, weight: 800 });
  groups.forEach((g, i) => {
    const y = y0 + i * 150;
    body += text(x0, y - 20, `${g.label}（${g.unit}）`, { size: 22, weight: 800 });
    body += rect(x0, y, barW, barH, "#e7edf2", { rx: 9 });
    body += rect(x0, y, g.smic / g.max * barW, barH, C.smic, { rx: 9 });
    body += text(x0 + g.smic / g.max * barW + 14, y + 25, fmt(g.smic, g.smic >= 1 ? 2 : 3), { size: 20, weight: 800, color: C.smic });
    body += rect(x0, y + 56, barW, barH, "#e7edf2", { rx: 9 });
    body += rect(x0, y + 56, g.hua / g.max * barW, barH, C.hua, { rx: 9 });
    body += text(x0 + g.hua / g.max * barW + 14, y + 81, fmt(g.hua, g.hua >= 1 ? 2 : 3), { size: 20, weight: 800, color: C.hua });
    body += rect(905, y - 12, 365, 112, C.white, { rx: 16, stroke: "#dce3ea", sw: 1 });
    body += tspans(930, y + 26, g.notes, { size: 18, color: C.ink, weight: 650, lineHeight: 31 });
  });
  body += rect(120, 693, 1150, 36, "#eaf0f5", { rx: 8 });
  body += text(140, 718, "读法：收入与利润不能单独决定投资价值，后续还要看毛利率、资本开支、折旧和估值口径。", { size: 19, color: C.muted, weight: 700 });
  return base(
    "中芯国际 vs 华虹：经营体量对比",
    "收入与利润均采用公司披露美元口径；归母利润为 profit attributable to owners/shareholders",
    body,
    "数据来源：中芯国际 2025 年报、2026Q1 公告；华虹半导体 2025 年报、2026Q1 公告"
  );
}

function marginUtilization() {
  const cards = [
    {
      name: "中芯国际",
      color: C.smic,
      items: [
        ["2025 毛利率", 21.0, "%", 35],
        ["2026Q1 毛利率", 20.1, "%", 35],
        ["2025 产能利用率", 93.5, "%", 115],
        ["2026Q1 产能利用率", 93.1, "%", 115]
      ],
      note: "规模更大，毛利率显著高于华虹；但扩产带来的折旧压力已经在销售成本里持续体现。"
    },
    {
      name: "华虹半导体",
      color: C.hua,
      items: [
        ["2025 毛利率", 11.8, "%", 35],
        ["2026Q1 毛利率", 13.0, "%", 35],
        ["2025 产能利用率", 106.1, "%", 115],
        ["2026Q1 产能利用率", 99.7, "%", 115]
      ],
      note: "利用率更紧，毛利率处于修复通道；FAB9 爬坡决定后续折旧吸收能力。"
    }
  ];
  let body = text(92, 205, "一个看盈利厚度，一个看产能紧张度。", { size: 24, weight: 800 });
  cards.forEach((card, idx) => {
    const x = idx === 0 ? 100 : 740;
    body += rect(x, 236, 560, 428, C.white, { rx: 18, stroke: "#dce3ea", sw: 1.2 });
    body += text(x + 30, 286, card.name, { size: 30, weight: 850, color: card.color });
    card.items.forEach((item, i) => {
      const y = 340 + i * 70;
      const w = Math.min(item[1] / item[3] * 280, 280);
      body += text(x + 34, y, item[0], { size: 19, color: C.muted, weight: 700 });
      body += rect(x + 210, y - 24, 280, 28, "#edf2f6", { rx: 8 });
      body += rect(x + 210, y - 24, w, 28, card.color, { rx: 8 });
      body += text(x + 510, y, `${fmt(item[1], 1)}${item[2]}`, { size: 22, color: card.color, weight: 850, anchor: "end" });
    });
    body += line(x + 34, 602, x + 526, 602, { stroke: "#dce3ea", sw: 1 });
    body += wrapText(x + 34, 632, card.note, 25, 28, { size: 19, color: C.ink, weight: 700 });
  });
  return base(
    "盈利质量：毛利率与产能利用率",
    "华虹利用率更高，但毛利率仍低；中芯规模和产品组合带来更强盈利厚度",
    body,
    "数据来源：两家公司 2025 年报及 2026Q1 公告"
  );
}

function capacityCapex() {
  const rows = [
    { label: "2025 月产能", smic: 1058.75, hua: 486, unit: "千片/月", max: 1120 },
    { label: "2026Q1 月产能", smic: 1078.25, hua: 489, unit: "千片/月", max: 1120 },
    { label: "2026Q1 资本开支", smic: 1.563, hua: 0.925, unit: "十亿美元", max: 1.7 },
    { label: "2026Q1 经营现金流", smic: 0.685, hua: 0.130, unit: "十亿美元", max: 0.8 }
  ];
  let body = legend([
    { label: "中芯国际", color: C.smic, gap: 132 },
    { label: "华虹半导体", color: C.hua, gap: 160 }
  ], 955, 194);
  body += text(92, 205, "中芯绝对产能更大，华虹扩产强度相对收入更重。", { size: 24, weight: 800 });
  rows.forEach((row, i) => {
    const y = 260 + i * 95;
    body += text(110, y, `${row.label}（${row.unit}）`, { size: 21, weight: 800 });
    body += rect(390, y - 29, 640, 28, "#e8eef4", { rx: 8 });
    body += rect(390, y - 29, row.smic / row.max * 640, 28, C.smic, { rx: 8 });
    body += rect(390, y + 17, 640, 28, "#e8eef4", { rx: 8 });
    body += rect(390, y + 17, row.hua / row.max * 640, 28, C.hua, { rx: 8 });
    body += text(1060, y - 7, fmt(row.smic, row.smic > 10 ? 0 : 3), { size: 20, color: C.smic, weight: 850 });
    body += text(1060, y + 39, fmt(row.hua, row.hua > 10 ? 0 : 3), { size: 20, color: C.hua, weight: 850 });
  });
  body += rect(118, 655, 1160, 72, "#fff7eb", { rx: 14, stroke: "#efd7b5", sw: 1 });
  body += text(146, 690, "关键矛盾：两家公司都在重资本开支周期，经营现金流不能完全覆盖扩产投入，折旧吸收和需求持续性是估值核心变量。", { size: 20, color: C.ink, weight: 750 });
  return base(
    "产能与资本开支：规模、利用率与现金流的拉扯",
    "月产能均为折合 8 英寸等效片；资本开支和经营现金流为 2026Q1",
    body,
    "数据来源：中芯国际 2026Q1 公告；华虹半导体 2026Q1 公告"
  );
}

function revenueMix() {
  const smicApps = [
    ["消费电子", 46.2, C.smic],
    ["智能手机", 18.9, "#4c9cc9"],
    ["工业与汽车", 14.0, C.green],
    ["电脑与平板", 13.6, C.purple],
    ["互联与可穿戴", 7.3, C.gray]
  ];
  const huaTech = [
    ["eNVM", 27.9, C.hua],
    ["模拟与电源管理", 26.3, "#d99a42"],
    ["功率器件", 25.9, C.green],
    ["逻辑与射频", 11.3, C.purple],
    ["sNVM", 8.6, C.gray]
  ];
  function stacked(items, x, y, title, subtitle) {
    let out = text(x, y, title, { size: 26, weight: 850 });
    out += text(x, y + 34, subtitle, { size: 17, color: C.muted });
    let cursor = x;
    const width = 520;
    const barY = y + 70;
    items.forEach((item, idx) => {
      const w = item[1] / 100 * width;
      out += rect(cursor, barY, w, 58, item[2], { rx: idx === 0 ? 10 : 0 });
      if (w > 58) out += text(cursor + w / 2, barY + 37, `${item[1]}%`, { size: 18, color: C.white, weight: 800, anchor: "middle" });
      cursor += w;
    });
    out += rect(x, barY, width, 58, "none", { rx: 10, stroke: "#cbd6de", sw: 1 });
    items.forEach((item, i) => {
      const yy = y + 170 + i * 46;
      out += rect(x, yy - 18, 22, 14, item[2], { rx: 4 });
      out += text(x + 34, yy, item[0], { size: 19, color: C.ink, weight: 700 });
      out += text(x + 470, yy, `${fmt(item[1], 1)}%`, { size: 19, color: item[2], weight: 850, anchor: "end" });
    });
    return out;
  }
  let body = text(92, 205, "中芯按终端应用披露，华虹按技术平台披露；这本身就体现了商业模型差异。", { size: 23, weight: 800 });
  body += rect(96, 236, 590, 430, C.white, { rx: 18, stroke: "#dce3ea", sw: 1 });
  body += rect(714, 236, 590, 430, C.white, { rx: 18, stroke: "#dce3ea", sw: 1 });
  body += stacked(smicApps, 130, 286, "中芯国际：2026Q1 晶圆收入按应用", "更像综合平台型晶圆代工");
  body += stacked(huaTech, 748, 286, "华虹半导体：2026Q1 收入按技术平台", "更像特色工艺组合");
  body += rect(130, 690, 1140, 40, "#eaf0f5", { rx: 9 });
  body += text(152, 716, "读法：中芯优势在客户和应用广度，华虹优势在 eNVM、功率、BCD/PMIC 等平台辨识度。", { size: 19, color: C.muted, weight: 750 });
  return base(
    "收入结构：综合平台 vs 特色工艺",
    "中芯披露应用口径；华虹披露技术平台口径，均为 2026Q1",
    body,
    "数据来源：中芯国际 2026Q1 公告；华虹半导体 2026Q1 公告"
  );
}

function techMatrix() {
  const columns = [
    { x: 92, w: 590, name: "中芯国际：热门平台", color: C.smic, soft: C.smicSoft, rows: [
      ["28nm ULL", "PDK、标准单元库、Memory Compiler 已发布；面向 IoT、手机、DTV、机顶盒、图像处理。"],
      ["28nm SST e-Flash", "关键工艺完成，SRAM/Flash bit cell 已展示；目标高端 MCU、车域控制器、ADAS。"],
      ["65nm RF-SOI", "新一代 PDK 发布并进入新产品测试验证；面向射频前端、Wi-Fi。"],
      ["90nm/8英寸 BCD", "低/中压 PDK 发布，车规、高压、SOI BCD 平台推进；面向 PMIC、电机驱动、汽车。"],
      ["HV Display Driver", "中尺寸显示驱动平台量产，大尺寸平台工艺完成并开发 PDK。"]
    ] },
    { x: 718, w: 590, name: "华虹半导体：热门平台", color: C.hua, soft: C.huaSoft, rows: [
      ["eNVM / MCU", "55nm eFlash 大规模量产；40nm eFlash 定制产品进入预生产；车规产品批量供货。"],
      ["sNVM / NOR", "NORD、ETOX Flash 持续迭代，48nm NOR Flash 出货占比提升。"],
      ["Analog & PM / BCD", "0.18um BCD 120V 支撑汽车 48V 系统；90nm BCD 稳定量产；BCD+eFlash 放量。"],
      ["Power Discrete", "1.6um IGBT 产品占比快速提升，面向电动车主逆变器、风光储充；布局 Power GaN。"],
      ["Logic & RF / CIS", "40nm ULP 特色工艺量产；65nm RF SOI 收入增长；CIS 面向手机主摄和车载视觉。"]
    ] }
  ];
  let body = text(92, 205, "技术壁垒不是单个节点，而是 PDK、IP、可靠性、良率、客户验证和产能交付的组合。", { size: 23, weight: 800 });
  columns.forEach((col) => {
    body += rect(col.x, 238, col.w, 478, C.white, { rx: 18, stroke: "#dce3ea", sw: 1 });
    body += rect(col.x, 238, col.w, 62, col.soft, { rx: 18 });
    body += text(col.x + 28, 278, col.name, { size: 28, weight: 850, color: col.color });
    col.rows.forEach((row, i) => {
      const y = 334 + i * 76;
      body += circle(col.x + 34, y - 7, 8, col.color);
      body += text(col.x + 58, y, row[0], { size: 20, weight: 850, color: col.color });
      body += wrapText(col.x + 190, y, row[1], 29, 24, { size: 17, color: C.ink, weight: 650 });
      if (i < col.rows.length - 1) body += line(col.x + 28, y + 34, col.x + col.w - 28, y + 34, { stroke: "#edf1f5", sw: 1 });
    });
  });
  return base(
    "热门工艺平台与技术壁垒",
    "按公司年报披露整理；区分“已量产”“验证中”“目标量产”的阶段差异",
    body,
    "数据来源：中芯国际 2025 年报 R&D ongoing projects；华虹半导体 2025 年报 process platforms"
  );
}

function cashCapex() {
  const data = [
    { label: "中芯 2025", ocf: 3.194, invest: -6.495, cash: 5.873, capex: null, color: C.smic },
    { label: "中芯 2026Q1", ocf: 0.685, invest: -1.697, cash: 7.279, capex: 1.563, color: C.smic },
    { label: "华虹 2025", ocf: 0.650, invest: -1.786, cash: 4.894, capex: 1.814, color: C.hua },
    { label: "华虹 2026Q1", ocf: 0.130, invest: -0.857, cash: 4.868, capex: 0.925, color: C.hua }
  ];
  const chart = { x: 128, y: 250, w: 800, h: 390 };
  let body = legend([
    { label: "经营现金流", color: C.green, gap: 142 },
    { label: "投资现金流流出", color: C.red, gap: 176 },
    { label: "期末现金", color: C.purple, gap: 130 }
  ], 830, 194);
  body += text(92, 205, "两家公司都能造现金，但扩产消耗更快。", { size: 24, weight: 800 });
  for (let i = 0; i <= 4; i++) {
    const y = chart.y + chart.h - i * chart.h / 4;
    body += line(chart.x, y, chart.x + chart.w, y, { stroke: C.grid, sw: 1 });
    body += text(chart.x - 18, y + 6, String(i * 2), { size: 16, color: C.muted, anchor: "end" });
  }
  body += text(chart.x - 72, chart.y - 16, "十亿美元", { size: 16, color: C.muted });
  data.forEach((d, i) => {
    const baseX = chart.x + 52 + i * 185;
    const bw = 34;
    const scale = chart.h / 8;
    const vals = [
      { v: d.ocf, color: C.green, dx: 0 },
      { v: Math.abs(d.invest), color: C.red, dx: 44 },
      { v: d.cash, color: C.purple, dx: 88 }
    ];
    vals.forEach((bar) => {
      const h = Math.max(bar.v * scale, 3);
      body += rect(baseX + bar.dx, chart.y + chart.h - h, bw, h, bar.color, { rx: 7 });
      body += text(baseX + bar.dx + bw / 2, chart.y + chart.h - h - 10, fmt(bar.v, 1), { size: 15, weight: 800, color: bar.color, anchor: "middle" });
    });
    body += text(baseX + 46, chart.y + chart.h + 38, d.label, { size: 17, color: C.ink, weight: 800, anchor: "middle" });
  });
  body += rect(990, 258, 285, 332, C.white, { rx: 18, stroke: "#dce3ea", sw: 1 });
  body += text(1020, 306, "资本开支压力", { size: 24, weight: 850 });
  body += text(1020, 354, "中芯 Q1 Capex", { size: 18, color: C.muted });
  body += text(1020, 389, "15.63 亿美元", { size: 28, color: C.smic, weight: 850 });
  body += text(1020, 444, "华虹 Q1 Capex", { size: 18, color: C.muted });
  body += text(1020, 479, "9.25 亿美元", { size: 28, color: C.hua, weight: 850 });
  body += wrapText(1020, 535, "读法：自由现金流短期承压不等于价值毁灭，但要求产能爬坡、客户导入和毛利率改善同步兑现。", 18, 27, { size: 18, color: C.ink, weight: 700 });
  return base(
    "现金流与扩产：投资价值的硬约束",
    "经营现金流、投资现金流和期末现金均为公司披露美元口径",
    body,
    "数据来源：两家公司 2025 年报及 2026Q1 公告"
  );
}

function valuationLens() {
  const fx = 0.86716;
  const usdCny = 6.794828;
  const rows = [
    {
      name: "中芯国际",
      a: 123.51,
      h: 72.55,
      aShares: 1999562549,
      hShares: 6013932328,
      revenue: 9.326799,
      profit: 0.685131,
      equity: 35.791097,
      color: C.smic
    },
    {
      name: "华虹半导体",
      a: 220.17,
      h: 140.50,
      aShares: 407750000,
      hShares: 1329928568,
      revenue: 2.402064,
      profit: 0.054881,
      equity: 9.28436,
      color: C.hua
    }
  ].map((r) => {
    const marketCapCny = (r.aShares * r.a + r.hShares * r.h * fx) / 1e9;
    const marketCapUsd = marketCapCny / usdCny;
    return {
      ...r,
      marketCapCny,
      marketCapUsd,
      ps: marketCapUsd / r.revenue,
      pe: marketCapUsd / r.profit,
      pb: marketCapUsd / r.equity
    };
  });
  let body = text(92, 205, "估值要先统一股本、币种和市场价格，不能把 A/H 行情页展示市值直接相加。", { size: 23, weight: 800 });
  body += rect(98, 238, 1204, 100, C.white, { rx: 16, stroke: "#dce3ea", sw: 1 });
  body += text(130, 278, "混合市值估算公式", { size: 22, weight: 850 });
  body += text(130, 314, "A 股数量 × A 股价 + H 股数量 × H 股价 × HKD/CNY；行情时间约为 2026-06-09 09:30，汇率为 1 HKD ≈ 0.867 CNY。", { size: 18, color: C.muted, weight: 700 });
  const headings = ["公司", "混合市值", "P/S", "P/E", "P/B", "解释"];
  const xs = [130, 360, 550, 700, 850, 995];
  body += rect(98, 374, 1204, 55, "#eaf0f5", { rx: 10 });
  headings.forEach((h, i) => {
    body += text(xs[i], 409, h, { size: 18, color: C.ink, weight: 850 });
  });
  rows.forEach((r, i) => {
    const y = 462 + i * 114;
    body += rect(98, y - 38, 1204, 96, C.white, { rx: 12, stroke: "#e1e7ed", sw: 1 });
    body += text(xs[0], y, r.name, { size: 21, weight: 850, color: r.color });
    body += text(xs[1], y, `${fmt(r.marketCapCny, 0)} 亿元`, { size: 20, weight: 850 });
    body += text(xs[2], y, fmt(r.ps, 1), { size: 20, weight: 850 });
    body += text(xs[3], y, r.pe > 500 ? ">600" : fmt(r.pe, 0), { size: 20, weight: 850 });
    body += text(xs[4], y, fmt(r.pb, 1), { size: 20, weight: 850 });
    const note = i === 0
      ? "利润更稳定，但 PE 已隐含国产替代和产能期权；需用 EBITDA/现金流交叉验证。"
      : "利润基数太低，PE 失真；更适合看 PB、PS、毛利率修复和 FAB9 爬坡兑现。";
    body += wrapText(xs[5], y - 18, note, 19, 24, { size: 17, color: C.muted, weight: 700 });
  });
  body += rect(118, 667, 1164, 62, "#fff7eb", { rx: 14, stroke: "#efd7b5", sw: 1 });
  body += text(146, 706, "提示：行情与汇率会变，表格用于展示估值方法；正文不把该时点估值当作买卖建议。", { size: 20, color: C.ink, weight: 750 });
  return base(
    "估值口径：A/H 混合市值示意",
    "以 2025 年收入、归母利润和 2026Q1 权益估算 P/S、P/E、P/B，仅作方法示例",
    body,
    "行情来源：上交所、腾讯财经行情接口；汇率来源：open.er-api.com；财务来源：公司公告"
  );
}

function scorecard() {
  const rows = [
    ["规模与客户覆盖", 5, 3, "中芯收入、产能、平台覆盖显著更大。"],
    ["特色工艺辨识度", 3, 5, "华虹在 eNVM、BCD、功率器件、MCU 更集中。"],
    ["盈利厚度", 4, 2, "中芯毛利率约 20%，华虹仍在修复。"],
    ["利用率弹性", 3, 5, "华虹 2025 超 100%，中芯稳定在 90%+。"],
    ["资本开支压力", 3, 2, "两者均重，华虹相对收入的 Q1 Capex 更高。"],
    ["出口管制敏感度", 2, 3, "中芯先进制程叙事更敏感；华虹偏成熟特色但仍受设备周期影响。"]
  ];
  let body = text(92, 205, "不是谁绝对更好，而是风险收益结构不同。", { size: 24, weight: 800 });
  const x0 = 120;
  const y0 = 260;
  body += legend([
    { label: "中芯国际", color: C.smic, gap: 132 },
    { label: "华虹半导体", color: C.hua, gap: 160 }
  ], 1000, 194);
  rows.forEach((row, i) => {
    const y = y0 + i * 72;
    body += text(x0, y, row[0], { size: 20, weight: 850 });
    for (let j = 0; j < 5; j++) {
      body += circle(390 + j * 32, y - 7, 10, j < row[1] ? C.smic : "#dce3ea");
      body += circle(590 + j * 32, y - 7, 10, j < row[2] ? C.hua : "#dce3ea");
    }
    body += wrapText(790, y - 17, row[3], 23, 24, { size: 17, color: C.muted, weight: 700 });
    if (i < rows.length - 1) body += line(x0, y + 31, 1280, y + 31, { stroke: "#e1e7ed", sw: 1 });
  });
  body += rect(118, 704, 1164, 36, "#eaf0f5", { rx: 8 });
  body += text(144, 728, "结论：偏稳健看中芯的规模与盈利，偏弹性看华虹的特色工艺修复；两者都不能忽视折旧和估值。", { size: 19, color: C.muted, weight: 750 });
  return base(
    "投资画像：优势与风险打分",
    "主观评分用于组织分析框架，不代表目标价或评级",
    body,
    "数据来源：公司公告；评分为本文基于财务、产能、产品平台和风险的主观判断"
  );
}

function cover() {
  const body = `
  <defs>
    <linearGradient id="fab" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0%" stop-color="#e8f3fb"/>
      <stop offset="52%" stop-color="#f9efe1"/>
      <stop offset="100%" stop-color="#edf2f4"/>
    </linearGradient>
    <pattern id="wafer" width="42" height="42" patternUnits="userSpaceOnUse">
      <circle cx="21" cy="21" r="15" fill="none" stroke="#c8d4de" stroke-width="1"/>
      <line x1="6" y1="21" x2="36" y2="21" stroke="#d9e1e8" stroke-width="1"/>
      <line x1="21" y1="6" x2="21" y2="36" stroke="#d9e1e8" stroke-width="1"/>
    </pattern>
  </defs>
  ${rect(80, 190, 1240, 500, "url(#fab)", { rx: 28, stroke: "#dce3ea", sw: 1 })}
  ${rect(80, 190, 1240, 500, "url(#wafer)", { rx: 28, opacity: 0.38 })}
  ${polygon("290,565 560,385 835,565", C.smic, { opacity: 0.9 })}
  ${polygon("600,565 860,310 1140,565", C.hua, { opacity: 0.9 })}
  ${rect(160, 292, 540, 168, "rgba(255,255,255,0.88)", { rx: 18, stroke: "#dce3ea", sw: 1 })}
  ${text(190, 350, "中芯国际", { size: 42, weight: 900, color: C.smic })}
  ${text(190, 400, "规模、12英寸产能、综合平台", { size: 24, weight: 750 })}
  ${rect(720, 292, 520, 168, "rgba(255,255,255,0.88)", { rx: 18, stroke: "#dce3ea", sw: 1 })}
  ${text(750, 350, "华虹半导体", { size: 42, weight: 900, color: C.hua })}
  ${text(750, 400, "特色工艺、功率/MCU、利用率", { size: 24, weight: 750 })}
  ${text(700, 618, "投资分析与优势对比", { size: 42, weight: 900, anchor: "middle" })}
  `;
  return base(
    "中芯国际与华虹半导体",
    "晶圆代工双样本：规模型龙头与特色工艺平台的投资价值比较",
    body,
    "本文图表基于公司公告、行业公开资料整理"
  );
}

const charts = [
  ["smic-huahong-cover.svg", cover()],
  ["smic-huahong-financial-scale.svg", financialScale()],
  ["smic-huahong-margin-utilization.svg", marginUtilization()],
  ["smic-huahong-capacity-capex.svg", capacityCapex()],
  ["smic-huahong-revenue-mix.svg", revenueMix()],
  ["smic-huahong-technology-platforms.svg", techMatrix()],
  ["smic-huahong-cash-capex.svg", cashCapex()],
  ["smic-huahong-valuation-lens.svg", valuationLens()],
  ["smic-huahong-scorecard.svg", scorecard()]
];

function cleanSvg(svg) {
  return svg.replace(/[ \t]+$/gm, "");
}

await fs.mkdir(outDir, { recursive: true });
await Promise.all(charts.map(([name, svg]) => fs.writeFile(path.join(outDir, name), cleanSvg(svg), "utf8")));
console.log(`Generated ${charts.length} SVG charts in ${outDir}`);
