import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, "..");
const outDir = path.join(rootDir, "images", "posts", "robosense-investment-analysis");

const W = 1400;
const H = 820;
const C = {
  ink: "#142127",
  muted: "#607078",
  grid: "#d6e0dc",
  panel: "#f6f8f2",
  paper: "#fbfcf8",
  teal: "#1b8a7c",
  mint: "#62cbb7",
  blue: "#386fa4",
  amber: "#d59f2f",
  red: "#c94c4c",
  green: "#5c8a3d",
  purple: "#7761a8",
  gray: "#8d9798",
  dark: "#0f1b20"
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
    className = "",
    family = "Arial, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif"
  } = opts;
  return `<text x="${x}" y="${y}" fill="${color}" font-family="${family}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}" class="${className}">${esc(value)}</text>`;
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
  return lines.map((line, i) => text(x, y + i * lineHeight, line, opts)).join("\n");
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
  const { stroke = "none", sw = 0 } = opts;
  return `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${fill}" stroke="${stroke}" stroke-width="${sw}"/>`;
}

function pathD(d, opts = {}) {
  const { stroke = C.ink, fill = "none", sw = 3, dash = "", opacity = 1 } = opts;
  return `<path d="${d}" fill="${fill}" stroke="${stroke}" stroke-width="${sw}"${dash ? ` stroke-dasharray="${dash}"` : ""} stroke-linecap="round" stroke-linejoin="round" opacity="${opacity}"/>`;
}

function base(title, subtitle, body, source) {
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" role="img" aria-labelledby="title desc">
  <title id="title">${esc(title)}</title>
  <desc id="desc">${esc(subtitle)}</desc>
  <rect width="${W}" height="${H}" fill="${C.paper}"/>
  <rect x="38" y="34" width="${W - 76}" height="${H - 68}" rx="26" fill="${C.panel}" stroke="#dbe5df"/>
  ${text(82, 104, title, { size: 40, weight: 800 })}
  ${text(82, 148, subtitle, { size: 22, weight: 500, color: C.muted })}
  ${body}
  ${text(82, 770, source, { size: 17, weight: 500, color: C.muted })}
</svg>
`;
}

function legend(items, x, y) {
  return items.map((item, i) => {
    const xx = x + i * item.gap;
    return `${rect(xx, y - 15, 26, 14, item.color, { rx: 4 })}
${text(xx + 36, y, item.label, { size: 18, color: C.muted })}`;
  }).join("\n");
}

function percent(v) {
  return `${v.toFixed(1)}%`;
}

function revenueMix() {
  const rows = [
    { year: "2024", total: 16.489, values: [
      { label: "ADAS", value: 13.353, color: C.teal },
      { label: "机器人及其他", value: 1.985, color: C.amber },
      { label: "解决方案", value: 0.980, color: C.blue },
      { label: "服务及其他", value: 0.172, color: C.gray }
    ] },
    { year: "2025", total: 19.410, values: [
      { label: "ADAS", value: 11.059, color: C.teal },
      { label: "机器人及其他", value: 7.098, color: C.amber },
      { label: "解决方案", value: 0.776, color: C.blue },
      { label: "服务及其他", value: 0.476, color: C.gray }
    ] }
  ];
  const x = 230;
  const y0 = 295;
  const barW = 860;
  const barH = 74;
  const max = 20;
  let body = legend([
    { label: "ADAS", color: C.teal, gap: 128 },
    { label: "机器人及其他", color: C.amber, gap: 208 },
    { label: "解决方案", color: C.blue, gap: 150 },
    { label: "服务及其他", color: C.gray, gap: 160 }
  ], 580, 198);
  body += text(82, 224, "收入结构从单一车载 ADAS，转向 ADAS + 机器人双主线。", { size: 24, weight: 700 });
  rows.forEach((row, idx) => {
    const y = y0 + idx * 150;
    body += text(96, y + 48, row.year, { size: 30, weight: 800 });
    body += text(1120, y + 48, `总收入 ${row.total.toFixed(2)} 亿元`, { size: 24, weight: 800, color: C.ink });
    let cursor = x;
    row.values.forEach((seg) => {
      const w = seg.value / max * barW;
      body += rect(cursor, y, w, barH, seg.color, { rx: cursor === x ? 16 : 0 });
      if (w > 86) {
        body += text(cursor + w / 2, y + 46, `${seg.label} ${seg.value.toFixed(2)}`, { size: 20, weight: 700, color: "#ffffff", anchor: "middle" });
      }
      cursor += w;
    });
    body += rect(x, y, barW, barH, "none", { rx: 16, stroke: "#bac8c1", sw: 1.5 });
  });
  body += rect(100, 585, 540, 102, "#ffffff", { rx: 18, stroke: "#dbe5df", sw: 1 });
  body += text(130, 626, "ADAS 占比", { size: 20, color: C.muted });
  body += text(130, 668, "约 81.0% → 57.0%", { size: 32, weight: 800, color: C.teal });
  body += rect(720, 585, 540, 102, "#ffffff", { rx: 18, stroke: "#dbe5df", sw: 1 });
  body += text(750, 626, "机器人及其他占比", { size: 20, color: C.muted });
  body += text(750, 668, "约 12.0% → 36.6%", { size: 32, weight: 800, color: C.amber });
  return base(
    "速腾聚创收入结构变化",
    "单位：亿元人民币；2025 年机器人及其他收入快速成为第二曲线",
    body,
    "数据来源：RoboSense 2025 Annual Report；2025 Annual Results Announcement"
  );
}

function industryMarket() {
  const market = [
    { year: "2023", value: 5.38 },
    { year: "2024", value: 8.59 },
    { year: "2025E", value: 12.0 },
    { year: "2030E", value: 36.0 }
  ];
  const chart = { x: 112, y: 235, w: 760, h: 390, max: 40 };
  let body = text(96, 206, "车载/Robotaxi 激光雷达市场仍小，但增长快。", { size: 24, weight: 700 });
  for (let i = 0; i <= 4; i++) {
    const y = chart.y + chart.h - i * chart.h / 4;
    body += line(chart.x, y, chart.x + chart.w, y, { stroke: C.grid, sw: 1 });
    body += text(chart.x - 20, y + 6, String(i * 10), { size: 16, color: C.muted, anchor: "end" });
  }
  body += text(chart.x - 62, chart.y - 12, "亿美元", { size: 17, color: C.muted });
  market.forEach((d, i) => {
    const bw = 100;
    const gap = 86;
    const x = chart.x + 70 + i * (bw + gap);
    const h = d.value / chart.max * chart.h;
    const y = chart.y + chart.h - h;
    const color = i < 2 ? C.teal : C.amber;
    body += rect(x, y, bw, h, color, { rx: 12 });
    body += text(x + bw / 2, y - 14, d.value.toFixed(d.value >= 10 ? 0 : 2), { size: 22, weight: 800, color, anchor: "middle" });
    body += text(x + bw / 2, chart.y + chart.h + 38, d.year, { size: 20, weight: 700, anchor: "middle" });
  });
  body += rect(925, 236, 340, 340, "#ffffff", { rx: 22, stroke: "#dbe5df", sw: 1 });
  body += text(954, 286, "2024 全球车载份额", { size: 24, weight: 800 });
  const shares = [
    ["中国供应商", 93, C.green],
    ["禾赛", 33, C.blue],
    ["速腾聚创", 24, C.teal],
    ["华为", 19, C.amber]
  ];
  shares.forEach((s, i) => {
    const y = 330 + i * 58;
    body += text(954, y, s[0], { size: 20, color: C.muted });
    body += rect(1075, y - 22, 150, 26, "#e8eee9", { rx: 8 });
    body += rect(1075, y - 22, s[1] / 100 * 150, 26, s[2], { rx: 8 });
    body += text(1242, y, `${s[1]}%`, { size: 21, weight: 800, color: s[2], anchor: "end" });
  });
  body += wrapText(954, 610, "结论：行业增速快，但收入池仍不大；赢家要靠规模、成本和客户绑定留下利润。", 25, 27, { size: 19, color: C.ink, weight: 700 });
  return base(
    "激光雷达行业空间与竞争位置",
    "Yole 口径：乘用车 + Robotaxi LiDAR 市场，2024-2030E CAGR 约 24%",
    body,
    "数据来源：Yole/optics.org；RoboSense 引述 Yole 2025 报告"
  );
}

function shipmentsAsp() {
  const x = 110;
  const y = 282;
  const w = 540;
  const h = 320;
  const max = 100;
  const bars = [
    { label: "2024", adas: 51.98, robot: 2.44 },
    { label: "2025", adas: 60.90, robot: 30.30 },
    { label: "2026Q1", adas: 14.48, robot: 18.55 }
  ];
  let body = text(92, 206, "销量高增，但必须结合 ASP 下行一起看。", { size: 24, weight: 700 });
  body += legend([
    { label: "ADAS 出货", color: C.teal, gap: 150 },
    { label: "机器人及其他出货", color: C.amber, gap: 230 }
  ], 112, 244);
  for (let i = 0; i <= 4; i++) {
    const yy = y + h - i * h / 4;
    body += line(x, yy, x + w, yy, { stroke: C.grid, sw: 1 });
    body += text(x - 18, yy + 6, String(i * 25), { size: 16, color: C.muted, anchor: "end" });
  }
  body += text(x - 72, y - 12, "万台", { size: 17, color: C.muted });
  bars.forEach((d, i) => {
    const bw = 105;
    const bx = x + 76 + i * 155;
    const adasH = d.adas / max * h;
    const robotH = d.robot / max * h;
    const baseY = y + h;
    body += rect(bx, baseY - adasH, bw, adasH, C.teal, { rx: 10 });
    body += rect(bx, baseY - adasH - robotH, bw, robotH, C.amber, { rx: 10 });
    body += text(bx + bw / 2, baseY - adasH - robotH - 12, (d.adas + d.robot).toFixed(2), { size: 20, weight: 800, anchor: "middle" });
    body += text(bx + bw / 2, baseY + 36, d.label, { size: 19, weight: 700, anchor: "middle" });
  });
  const ax = 782;
  const ay = 282;
  const aw = 490;
  const ah = 320;
  body += text(ax, 244, "平均单价下降", { size: 22, weight: 800 });
  for (let i = 0; i <= 4; i++) {
    const yy = ay + ah - i * ah / 4;
    body += line(ax, yy, ax + aw, yy, { stroke: C.grid, sw: 1 });
    body += text(ax - 20, yy + 6, String(i * 2000), { size: 16, color: C.muted, anchor: "end" });
  }
  body += text(ax - 72, ay - 12, "元/台", { size: 17, color: C.muted });
  const xs = [ax + 70, ax + 230, ax + 390];
  const yv = (v) => ay + ah - v / 8500 * ah;
  const adas = [
    ["2024", 2600],
    ["2025", 1800],
    ["2025Q4", 1500]
  ];
  const robot = [
    ["2024", 8100],
    ["2025", 2300]
  ];
  body += pathD(`M${xs[0]},${yv(2600)} L${xs[1]},${yv(1800)} L${xs[2]},${yv(1500)}`, { stroke: C.teal, sw: 5 });
  body += pathD(`M${xs[0]},${yv(8100)} L${xs[1]},${yv(2300)}`, { stroke: C.amber, sw: 5 });
  adas.forEach((d, i) => {
    body += circle(xs[i], yv(d[1]), 8, C.teal, { stroke: "#fff", sw: 3 });
    body += text(xs[i], yv(d[1]) - 18, `${d[1]}`, { size: 18, weight: 800, color: C.teal, anchor: "middle" });
  });
  robot.forEach((d, i) => {
    body += circle(xs[i], yv(d[1]), 8, C.amber, { stroke: "#fff", sw: 3 });
    body += text(xs[i], yv(d[1]) - 18, `${d[1]}`, { size: 18, weight: 800, color: C.amber, anchor: "middle" });
  });
  ["2024", "2025", "2025Q4"].forEach((label, i) => {
    body += text(xs[i], ay + ah + 36, label, { size: 18, weight: 700, anchor: "middle" });
  });
  body += rect(100, 662, 1178, 56, "#ffffff", { rx: 16, stroke: "#dbe5df", sw: 1 });
  body += text(130, 698, "关键读法：销量增长本身不是利润保证，必须看 ASP 下降后毛利率能否守住。", { size: 22, weight: 800, color: C.ink });
  return base(
    "出货放量与 ASP 下行并存",
    "出货：万台；ASP：人民币/台。2026Q1 为单季度，不可直接年化",
    body,
    "数据来源：RoboSense 2025 Annual Report；2025 Annual Results；2026 Q1 Results"
  );
}

function profitabilityCash() {
  const cols = [
    { label: "2024", gm: 17.2, net: -4.82, adj: -3.96, ocf: -0.65 },
    { label: "2025", gm: 26.5, net: -1.45, adj: -0.54, ocf: -5.82 },
    { label: "2025Q4", gm: 28.5, net: 1.04, adj: 1.25, ocf: null },
    { label: "2026Q1", gm: 21.7, net: -0.63, adj: -0.44, ocf: -0.89 }
  ];
  const x = 108;
  const y = 244;
  const w = 780;
  const h = 370;
  const netScale = 6;
  const zeroY = y + h * 0.42;
  let body = text(92, 206, "利润表改善，但现金流仍是硬约束。", { size: 24, weight: 700 });
  body += legend([
    { label: "毛利率", color: C.green, gap: 116 },
    { label: "净利润/亏损", color: C.teal, gap: 160 },
    { label: "经营现金流", color: C.red, gap: 160 }
  ], 675, 206);
  for (let i = -6; i <= 4; i += 2) {
    const yy = zeroY - i / netScale * h * 0.52;
    body += line(x, yy, x + w, yy, { stroke: i === 0 ? "#9fb1aa" : C.grid, sw: i === 0 ? 2 : 1 });
    body += text(x - 18, yy + 6, `${i}`, { size: 15, color: C.muted, anchor: "end" });
  }
  body += text(x - 74, y - 12, "亿元", { size: 17, color: C.muted });
  cols.forEach((d, i) => {
    const gx = x + 75 + i * 175;
    const barW = 44;
    const barY = d.net >= 0 ? zeroY - d.net / netScale * h * 0.52 : zeroY;
    const barH = Math.abs(d.net) / netScale * h * 0.52;
    body += rect(gx, barY, barW, barH, d.net >= 0 ? C.teal : C.red, { rx: 8 });
    body += text(gx + barW / 2, d.net >= 0 ? barY - 12 : barY + barH + 24, d.net.toFixed(2), { size: 17, weight: 800, color: d.net >= 0 ? C.teal : C.red, anchor: "middle" });
    if (d.ocf !== null) {
      const ox = gx + 58;
      const oy = d.ocf >= 0 ? zeroY - d.ocf / netScale * h * 0.52 : zeroY;
      const oh = Math.abs(d.ocf) / netScale * h * 0.52;
      body += rect(ox, oy, barW, oh, C.dark, { rx: 8, opacity: 0.82 });
      body += text(ox + barW / 2, oy + oh + 24, d.ocf.toFixed(2), { size: 17, weight: 800, color: C.dark, anchor: "middle" });
    }
    body += text(gx + 48, y + h + 38, d.label, { size: 18, weight: 700, anchor: "middle" });
  });
  const lx = 995;
  const ly = 262;
  body += rect(940, 238, 318, 408, "#ffffff", { rx: 22, stroke: "#dbe5df", sw: 1 });
  body += text(970, 286, "毛利率走势", { size: 24, weight: 800 });
  const mXs = [980, 1060, 1140, 1220];
  const mY = (v) => ly + 300 - v / 35 * 300;
  body += pathD(`M${mXs[0]},${mY(17.2)} L${mXs[1]},${mY(26.5)} L${mXs[2]},${mY(28.5)} L${mXs[3]},${mY(21.7)}`, { stroke: C.green, sw: 6 });
  cols.forEach((d, i) => {
    body += circle(mXs[i], mY(d.gm), 8, C.green, { stroke: "#fff", sw: 3 });
    body += text(mXs[i], mY(d.gm) - 18, `${d.gm}%`, { size: 16, weight: 800, color: C.green, anchor: "middle" });
    body += text(mXs[i], ly + 334, d.label.replace("2025", "25"), { size: 14, color: C.muted, anchor: "middle" });
  });
  body += wrapText(964, 610, "Q4 首次盈利很重要，但 2026Q1 又亏损，说明拐点还需要连续季度验证。", 22, 25, { size: 18, weight: 700, color: C.ink });
  return base(
    "盈利拐点与现金流压力",
    "净利润/经营现金流单位：亿元；毛利率单位：%",
    body,
    "数据来源：RoboSense 2025 Annual Results；2026 Q1 Results"
  );
}

function customersOrders() {
  let body = text(92, 206, "定点和订单强，但客户集中与替代风险仍要跟踪。", { size: 24, weight: 700 });
  const steps = [
    { lines: ["汽车 OEM", "及 Tier 1"], value: "36 家", color: C.blue },
    { lines: ["车型量产", "定点"], value: "177 款", color: C.teal },
    { lines: ["已 SOP", "车型"], value: "69 款", color: C.green },
    { lines: ["ADAS", "在手订单"], value: ">900 万台", color: C.amber }
  ];
  steps.forEach((s, i) => {
    const x = 110 + i * 300;
    body += rect(x, 262, 232, 148, s.color, { rx: 24, opacity: 0.95 });
    body += text(x + 116, 324, s.value, { size: 36, weight: 900, color: "#ffffff", anchor: "middle" });
    s.lines.forEach((lineLabel, lineIndex) => {
      body += text(x + 116, 362 + lineIndex * 25, lineLabel, { size: 18, weight: 700, color: "#ffffff", anchor: "middle" });
    });
    if (i < steps.length - 1) {
      body += pathD(`M${x + 242},336 L${x + 288},336`, { stroke: C.muted, sw: 4 });
      body += pathD(`M${x + 276},324 L${x + 290},336 L${x + 276},348`, { stroke: C.muted, sw: 4 });
    }
  });
  body += text(105, 488, "客户集中度改善", { size: 25, weight: 800 });
  const metrics = [
    { label: "最大客户收入占比", v2024: 34.7, v2025: 26.7, color: C.teal },
    { label: "前五大客户收入占比", v2024: 83.4, v2025: 59.7, color: C.amber },
    { label: "前五大供应商采购占比", v2024: 59.4, v2025: 32.5, color: C.blue }
  ];
  metrics.forEach((m, i) => {
    const y = 532 + i * 62;
    body += text(112, y, m.label, { size: 19, color: C.muted });
    body += rect(360, y - 24, 260, 24, "#e6eee9", { rx: 8 });
    body += rect(360, y - 24, m.v2024 / 100 * 260, 24, "#b7c2bd", { rx: 8 });
    body += text(635, y - 4, `2024 ${percent(m.v2024)}`, { size: 17, color: C.muted });
    body += rect(760, y - 24, 260, 24, "#e6eee9", { rx: 8 });
    body += rect(760, y - 24, m.v2025 / 100 * 260, 24, m.color, { rx: 8 });
    body += text(1035, y - 4, `2025 ${percent(m.v2025)}`, { size: 17, weight: 800, color: m.color });
  });
  body += rect(1080, 514, 190, 144, "#ffffff", { rx: 20, stroke: "#dbe5df", sw: 1 });
  body += text(1108, 558, "读法", { size: 23, weight: 900 });
  body += text(1108, 598, "定点不是收入，", { size: 17, color: C.ink, weight: 700 });
  body += text(1108, 622, "SOP 和实际销量", { size: 17, color: C.ink, weight: 700 });
  body += text(1108, 646, "才是兑现。", { size: 17, color: C.ink, weight: 700 });
  return base(
    "客户、订单与集中度",
    "截至 2026-03-31 的设计定点/SOP；集中度为 2024-2025 年报口径",
    body,
    "数据来源：RoboSense 2025 Annual Report；2026 Q1 Results"
  );
}

function valuationScenarios() {
  const scenarios = [
    { label: "悲观", revenue: 24, margin: -1, profit: -0.2, color: C.red },
    { label: "中性", revenue: 30, margin: 5, profit: 1.5, color: C.gray },
    { label: "乐观", revenue: 40, margin: 10, profit: 4.0, color: C.teal },
    { label: "强乐观", revenue: 50, margin: 12, profit: 6.0, color: C.green }
  ];
  let body = text(92, 206, "当前估值要求增长和盈利继续兑现。", { size: 24, weight: 700 });
  body += rect(100, 248, 360, 168, C.dark, { rx: 24 });
  body += text(132, 304, "取数时点", { size: 21, color: "#c9d7d1" });
  body += text(132, 354, "2026-06-08", { size: 34, weight: 900, color: "#ffffff" });
  body += text(132, 392, "市值约 152.1 亿港元", { size: 20, color: "#d9e7df" });
  body += rect(510, 248, 360, 168, "#ffffff", { rx: 24, stroke: "#dbe5df", sw: 1 });
  body += text(542, 304, "当前市销率", { size: 21, color: C.muted });
  body += text(542, 354, "约 6.5x", { size: 42, weight: 900, color: C.teal });
  body += text(542, 392, "TTM 仍亏损，静态 PE 不适用", { size: 19, color: C.muted });
  body += rect(920, 248, 360, 168, "#ffffff", { rx: 24, stroke: "#dbe5df", sw: 1 });
  body += text(952, 304, "2025 收入", { size: 21, color: C.muted });
  body += text(952, 354, "19.41 亿元", { size: 40, weight: 900, color: C.amber });
  body += text(952, 392, "年度仍亏损，现金流为负", { size: 19, color: C.muted });
  const x = 130;
  const y = 500;
  const maxRev = 55;
  scenarios.forEach((s, i) => {
    const sx = x + i * 300;
    body += text(sx + 95, y - 32, s.label, { size: 23, weight: 900, color: s.color, anchor: "middle" });
    body += rect(sx, y, 190, 34, "#e7eee9", { rx: 10 });
    body += rect(sx, y, s.revenue / maxRev * 190, 34, s.color, { rx: 10 });
    body += text(sx + 95, y + 62, `收入 ${s.revenue} 亿`, { size: 18, weight: 700, anchor: "middle" });
    body += text(sx + 95, y + 94, `净利率 ${s.margin}%`, { size: 18, color: C.muted, anchor: "middle" });
    body += text(sx + 95, y + 134, `净利润 ${s.profit} 亿`, { size: 22, weight: 900, color: s.color, anchor: "middle" });
  });
  body += rect(100, 670, 1180, 54, "#ffffff", { rx: 16, stroke: "#dbe5df", sw: 1 });
  body += text(130, 705, "这不是预测，而是估值压力测试：若收入和利润不能继续上台阶，成长股倍数会先收缩。", { size: 21, weight: 800 });
  return base(
    "估值敏感性：从主题定价到盈利支撑",
    "当前行情口径 + 作者情景测算；金额单位按文中口径近似",
    body,
    "数据来源：StockAnalysis 2026-06-08；RoboSense 2025 Annual Report；作者测算"
  );
}

function cellLines(x, y, lines, opts = {}) {
  const { lineHeight = 23, size = 17, weight = 600, color = C.ink } = opts;
  return lines.map((lineText, i) => text(x, y + i * lineHeight, lineText, { size, weight, color })).join("\n");
}

function productMoatMatrix() {
  const rows = [
    {
      product: "EM4",
      color: C.teal,
      role: ["高阶 ADAS /", "Robotaxi 主雷达"],
      specs: ["2160-beam；600m 最远测距", "SPAD-SoC；60% 数据压缩"],
      commercial: ["2025Q4 大规模交付", "Robotaxi EM4+E1 方案"],
      read: ["高性能旗舰，验证技术上限", "但收入弹性取决于高端车型"]
    },
    {
      product: "EMX",
      color: C.blue,
      role: ["主流 ADAS", "前向主雷达"],
      specs: ["192-beam；300m 最远测距", "20Hz；120×80×30mm"],
      commercial: ["2025 年内投产", "2026Q1 初期量产影响毛利"],
      read: ["承担中高配车型放量", "良率爬坡决定毛利修复"]
    },
    {
      product: "MX",
      color: C.green,
      role: ["低成本", "中距车载雷达"],
      specs: ["25mm；<10W；200m", "M-Core SoC；ROI 251 线"],
      commercial: ["低价 MX 占比提升", "推动 ADAS ASP 下行"],
      read: ["打开 15-20 万元车渗透", "也加剧价格战压力"]
    },
    {
      product: "E1 / E1R",
      color: C.amber,
      role: ["车载补盲 /", "机器人导航"],
      specs: ["120°×90°；75m / 30m@10%", "全固态；SoC 集成感知"],
      commercial: ["E 平台交付 >30 万台", "割草机器人/Robotaxi 使用"],
      read: ["平台复用价值高", "是车规能力外溢到机器人"]
    },
    {
      product: "Airy / Fairy",
      color: C.purple,
      role: ["机器人", "广域感知"],
      specs: ["Airy 360°×90°；30m@10%", "Fairy 150m；0.5cm 精度"],
      commercial: ["Airy Lite 2025Q4 交付", "机器人出货 2025 年 30.3 万台"],
      read: ["支撑第二曲线", "需验证复购与 ASP 稳定"]
    },
    {
      product: "AC2",
      color: C.red,
      role: ["具身智能", "操作视觉"],
      specs: ["dToF + 双目 RGB + IMU", "±5mm；0.05-8m；<1ms"],
      commercial: ["欧洲人形机器人批量订单", "仍处早期放量"],
      read: ["从雷达到机器人视觉", "早期产品，需看规模收入"]
    }
  ];
  let body = text(92, 206, "产品不是孤立 SKU，而是车载高阶化、低成本普及和机器人第二曲线的载体。", { size: 24, weight: 700 });
  const cols = [
    { label: "产品", x: 94, w: 112 },
    { label: "定位", x: 220, w: 190 },
    { label: "公开参数/技术特征", x: 428, w: 300 },
    { label: "商业化信号", x: 752, w: 235 },
    { label: "投资含义", x: 1010, w: 270 }
  ];
  const tableX = 82;
  const tableY = 242;
  const rowH = 70;
  body += rect(tableX, tableY, 1218, 46, C.dark, { rx: 16 });
  cols.forEach((col) => {
    body += text(col.x, tableY + 31, col.label, { size: 18, weight: 800, color: "#ffffff" });
  });
  rows.forEach((row, i) => {
    const y = tableY + 46 + i * rowH;
    body += rect(tableX, y, 1218, rowH, i % 2 === 0 ? "#ffffff" : "#f2f6f0", { rx: i === rows.length - 1 ? 16 : 0, stroke: "#dbe5df", sw: 1 });
    body += rect(94, y + 16, 88, 38, row.color, { rx: 12 });
    body += text(138, y + 42, row.product, { size: 19, weight: 900, color: "#ffffff", anchor: "middle" });
    body += cellLines(220, y + 27, row.role, { size: 16, lineHeight: 22, color: C.ink, weight: 700 });
    body += cellLines(428, y + 27, row.specs, { size: 16, lineHeight: 22, color: C.ink, weight: 700 });
    body += cellLines(752, y + 27, row.commercial, { size: 16, lineHeight: 22, color: C.muted, weight: 700 });
    body += cellLines(1010, y + 27, row.read, { size: 16, lineHeight: 22, color: C.ink, weight: 700 });
  });
  body += rect(100, 725, 1180, 40, "#ffffff", { rx: 14, stroke: "#dbe5df", sw: 1 });
  body += text(126, 751, "读法：产品矩阵越丰富，越能覆盖车企与机器人客户；但护城河最终由成本、良率、SOP 转化和现金流验证。", { size: 19, weight: 800, color: C.ink });
  return base(
    "速腾聚创热门产品矩阵与投资含义",
    "公司披露参数与商业化信号整理；产品性能陈述不等于独立验证结论",
    body,
    "数据来源：RoboSense 产品页、2025 年报/业绩公告、2026Q1 公告；作者整理"
  );
}

async function main() {
  await fs.mkdir(outDir, { recursive: true });
  const charts = {
    "robosense-industry-market.svg": industryMarket(),
    "robosense-revenue-mix.svg": revenueMix(),
    "robosense-shipments-asp.svg": shipmentsAsp(),
    "robosense-profitability-cash.svg": profitabilityCash(),
    "robosense-customers-orders.svg": customersOrders(),
    "robosense-product-moat-matrix.svg": productMoatMatrix(),
    "robosense-valuation-scenarios.svg": valuationScenarios()
  };
  await Promise.all(Object.entries(charts).map(([name, svg]) => fs.writeFile(path.join(outDir, name), svg, "utf8")));
  for (const name of Object.keys(charts)) {
    console.log(path.join("images/posts/robosense-investment-analysis", name));
  }
}

await main();
