import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, "..");
const outDir = path.join(rootDir, "images", "posts", "inside-the-black-box-quant-investing-summary");

const palette = {
  ink: "#1f2933",
  muted: "#52606d",
  line: "#d9e2ec",
  paper: "#f8fafc",
  blue: "#2563eb",
  teal: "#0f766e",
  green: "#2f855a",
  amber: "#b7791f",
  red: "#c2410c",
  slate: "#334155",
  softBlue: "#dbeafe",
  softTeal: "#ccfbf1",
  softGreen: "#dcfce7",
  softAmber: "#fef3c7",
  softRed: "#ffedd5",
  white: "#ffffff"
};

function escapeXml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function wrapText(text, maxChars = 16) {
  const segments = [];
  let line = "";
  for (const char of String(text)) {
    const projected = line + char;
    const len = [...projected].reduce((sum, item) => sum + (/[\u4e00-\u9fff]/.test(item) ? 1 : 0.55), 0);
    if (len > maxChars && line) {
      segments.push(line);
      line = char;
    } else {
      line = projected;
    }
  }
  if (line) segments.push(line);
  return segments;
}

function multiline(text, x, y, options = {}) {
  const {
    size = 26,
    weight = 500,
    fill = palette.ink,
    anchor = "middle",
    maxChars = 16,
    lineHeight = 1.32,
    className = ""
  } = options;
  const lines = Array.isArray(text) ? text : wrapText(text, maxChars);
  const firstDy = lines.length > 1 ? -((lines.length - 1) * size * lineHeight) / 2 : 0;
  const tspans = lines
    .map((line, index) => {
      const dy = index === 0 ? firstDy : size * lineHeight;
      return `<tspan x="${x}" dy="${index === 0 ? dy : dy}">${escapeXml(line)}</tspan>`;
    })
    .join("");
  return `<text x="${x}" y="${y}" text-anchor="${anchor}" font-size="${size}" font-weight="${weight}" fill="${fill}" class="${className}">${tspans}</text>`;
}

function rect(x, y, width, height, options = {}) {
  const {
    fill = palette.white,
    stroke = palette.line,
    radius = 10,
    strokeWidth = 2,
    opacity = 1,
    extra = ""
  } = options;
  return `<rect x="${x}" y="${y}" width="${width}" height="${height}" rx="${radius}" fill="${fill}" stroke="${stroke}" stroke-width="${strokeWidth}" opacity="${opacity}" ${extra}/>`;
}

function pill(x, y, width, height, label, options = {}) {
  const fill = options.fill || palette.softBlue;
  const stroke = options.stroke || "none";
  const textFill = options.textFill || palette.ink;
  return `${rect(x, y, width, height, { fill, stroke, radius: height / 2, strokeWidth: stroke === "none" ? 0 : 2 })}
  ${multiline(label, x + width / 2, y + height / 2 + 8, { size: options.size || 22, fill: textFill, weight: options.weight || 600, maxChars: 12 })}`;
}

function arrow(x1, y1, x2, y2, color = palette.slate, width = 3) {
  return `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${color}" stroke-width="${width}" stroke-linecap="round" marker-end="url(#arrow)"/>`;
}

function baseSvg(width, height, body, title, description = "") {
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" role="img" aria-labelledby="title desc">
  <title id="title">${escapeXml(title)}</title>
  <desc id="desc">${escapeXml(description || title)}</desc>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.slate}"/>
    </marker>
    <linearGradient id="coverGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ecfeff"/>
      <stop offset="46%" stop-color="#f8fafc"/>
      <stop offset="100%" stop-color="#fff7ed"/>
    </linearGradient>
    <filter id="softShadow" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="12" stdDeviation="12" flood-color="#0f172a" flood-opacity="0.10"/>
    </filter>
  </defs>
  <style>
    text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif; }
    .mono { font-family: "SFMono-Regular", "Menlo", "Consolas", monospace; }
  </style>
  <rect width="100%" height="100%" fill="${palette.paper}"/>
  ${body}
</svg>
`;
}

async function writeSvg(name, svg) {
  await fs.mkdir(outDir, { recursive: true });
  await fs.writeFile(path.join(outDir, name), svg.replace(/[ \t]+$/gm, ""), "utf8");
}

function cover() {
  const body = `
  <rect width="1400" height="760" fill="url(#coverGradient)"/>
  <path d="M 110 585 C 300 480, 390 630, 575 525 S 890 405, 1045 492 1220 575, 1310 445" fill="none" stroke="#bae6fd" stroke-width="18" opacity="0.65"/>
  <path d="M 105 615 C 330 520, 455 645, 650 540 S 965 440, 1130 540 1248 575, 1328 508" fill="none" stroke="#fed7aa" stroke-width="16" opacity="0.68"/>
  ${rect(96, 86, 1208, 584, { fill: "rgba(255,255,255,0.82)", stroke: "#e2e8f0", radius: 18, extra: 'filter="url(#softShadow)"' })}
  ${pill(152, 142, 250, 54, "读书笔记", { fill: palette.softTeal, textFill: palette.teal })}
  ${multiline("打开量化投资的黑箱", 152, 264, { anchor: "start", size: 62, weight: 800, maxChars: 22, fill: palette.ink })}
  ${multiline("从信号、组合、交易到风控的系统化投资框架", 152, 350, { anchor: "start", size: 34, weight: 600, maxChars: 16, fill: palette.slate })}
  ${multiline("Rishi K. Narang 的核心贡献，是把“黑箱”拆成可检查、可治理、可评估的投资系统。", 152, 468, { anchor: "start", size: 25, weight: 450, maxChars: 28, fill: palette.muted })}
  ${rect(820, 172, 370, 306, { fill: "#0f172a", stroke: "#1e293b", radius: 14 })}
  ${multiline("BLACK BOX", 1005, 224, { size: 34, weight: 800, fill: "#e2e8f0", maxChars: 12 })}
  ${rect(870, 264, 270, 48, { fill: "#1e293b", stroke: "#334155", radius: 8 })}
  ${rect(870, 335, 270, 48, { fill: "#1e293b", stroke: "#334155", radius: 8 })}
  ${rect(870, 406, 270, 48, { fill: "#1e293b", stroke: "#334155", radius: 8 })}
  ${multiline("Alpha / Risk / Cost", 1005, 296, { size: 21, weight: 650, fill: "#bfdbfe", maxChars: 18 })}
  ${multiline("Portfolio Construction", 1005, 367, { size: 21, weight: 650, fill: "#ccfbf1", maxChars: 20 })}
  ${multiline("Execution & Feedback", 1005, 438, { size: 21, weight: 650, fill: "#fed7aa", maxChars: 20 })}
  <circle cx="782" cy="326" r="9" fill="#2563eb" opacity="0.7"/>
  <circle cx="1228" cy="326" r="9" fill="#b7791f" opacity="0.7"/>
  ${multiline("量化不是神秘公式，而是一组有边界的工程流程", 700, 610, { size: 28, weight: 600, fill: palette.slate, maxChars: 34 })}
`;
  return baseSvg(1400, 760, body, "打开量化投资的黑箱读书笔记封面");
}

function hero() {
  const body = `
  <defs>
    <linearGradient id="heroGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#020617"/>
      <stop offset="52%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#164e63"/>
    </linearGradient>
    <radialGradient id="heroGlow" cx="32%" cy="26%" r="70%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.38"/>
      <stop offset="46%" stop-color="#2563eb" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#020617" stop-opacity="0"/>
    </radialGradient>
    <filter id="heroShadow" x="-15%" y="-15%" width="130%" height="130%">
      <feDropShadow dx="0" dy="18" stdDeviation="20" flood-color="#000000" flood-opacity="0.32"/>
    </filter>
  </defs>
  <rect width="1400" height="760" fill="url(#heroGradient)"/>
  <rect width="1400" height="760" fill="url(#heroGlow)"/>
  <g opacity="0.24">
    <path d="M 110 180 C 320 95, 455 238, 675 165 S 1010 72, 1295 210" fill="none" stroke="#67e8f9" stroke-width="4"/>
    <path d="M 90 595 C 265 470, 458 665, 662 534 S 1018 430, 1316 570" fill="none" stroke="#fed7aa" stroke-width="5"/>
    <path d="M 180 378 L 1220 378" stroke="#e2e8f0" stroke-width="2" stroke-dasharray="10 16"/>
  </g>
  <g transform="translate(690 122)" filter="url(#heroShadow)">
    ${rect(0, 0, 444, 360, { fill: "#0b1220", stroke: "#334155", radius: 18, strokeWidth: 2 })}
    <circle cx="62" cy="58" r="15" fill="#38bdf8" opacity="0.9"/>
    <circle cx="112" cy="58" r="15" fill="#2dd4bf" opacity="0.9"/>
    <circle cx="162" cy="58" r="15" fill="#f59e0b" opacity="0.9"/>
    ${rect(54, 122, 336, 52, { fill: "#111827", stroke: "#334155", radius: 10 })}
    ${rect(54, 206, 336, 52, { fill: "#111827", stroke: "#334155", radius: 10 })}
    ${rect(54, 290, 336, 52, { fill: "#111827", stroke: "#334155", radius: 10 })}
    <line x1="92" y1="148" x2="282" y2="148" stroke="#bfdbfe" stroke-width="8" stroke-linecap="round" opacity="0.72"/>
    <line x1="92" y1="232" x2="338" y2="232" stroke="#ccfbf1" stroke-width="8" stroke-linecap="round" opacity="0.72"/>
    <line x1="92" y1="316" x2="246" y2="316" stroke="#fed7aa" stroke-width="8" stroke-linecap="round" opacity="0.72"/>
    <circle cx="340" cy="148" r="8" fill="#bfdbfe" opacity="0.86"/>
    <circle cx="284" cy="316" r="8" fill="#fed7aa" opacity="0.86"/>
  </g>
  <g>
    ${rect(180, 286, 170, 58, { fill: "#dbeafe", stroke: "none", radius: 29, strokeWidth: 0, opacity: 0.92 })}
    ${rect(430, 286, 170, 58, { fill: "#ccfbf1", stroke: "none", radius: 29, strokeWidth: 0, opacity: 0.92 })}
    ${rect(1178, 286, 170, 58, { fill: "#fef3c7", stroke: "none", radius: 29, strokeWidth: 0, opacity: 0.92 })}
    <circle cx="230" cy="315" r="11" fill="#1d4ed8" opacity="0.9"/>
    <circle cx="280" cy="315" r="11" fill="#38bdf8" opacity="0.9"/>
    <circle cx="480" cy="315" r="11" fill="#0f766e" opacity="0.9"/>
    <circle cx="530" cy="315" r="11" fill="#2dd4bf" opacity="0.9"/>
    <circle cx="1232" cy="315" r="11" fill="#b7791f" opacity="0.9"/>
    <circle cx="1282" cy="315" r="11" fill="#f59e0b" opacity="0.9"/>
    ${arrow(350, 315, 430, 315, "#94a3b8", 4)}
    ${arrow(600, 315, 690, 315, "#94a3b8", 4)}
    ${arrow(1134, 315, 1178, 315, "#94a3b8", 4)}
  </g>
  <g opacity="0.42">
    <circle cx="186" cy="152" r="4" fill="#e0f2fe"/>
    <circle cx="248" cy="214" r="4" fill="#e0f2fe"/>
    <circle cx="360" cy="152" r="4" fill="#e0f2fe"/>
    <circle cx="468" cy="220" r="4" fill="#e0f2fe"/>
    <line x1="186" y1="152" x2="248" y2="214" stroke="#bae6fd" stroke-width="2"/>
    <line x1="248" y1="214" x2="360" y2="152" stroke="#bae6fd" stroke-width="2"/>
    <line x1="360" y1="152" x2="468" y2="220" stroke="#bae6fd" stroke-width="2"/>
  </g>
`;
  return baseSvg(1400, 760, body, "Quant investing system hero", "Decorative system diagram for the article hero.");
}

function pipeline() {
  const steps = [
    ["数据", "价格、成交、基本面、另类数据、组合状态", palette.softBlue, palette.blue],
    ["Alpha 模型", "把信息转成预期收益或相对排序", palette.softTeal, palette.teal],
    ["风险模型", "估计波动、相关性、因子暴露和尾部风险", palette.softAmber, palette.amber],
    ["成本模型", "手续费、价差、冲击、延迟与容量", palette.softRed, palette.red],
    ["组合构建", "在约束下把信号变成目标持仓", palette.softGreen, palette.green],
    ["执行系统", "把目标持仓拆成可成交订单并反馈", "#e0e7ff", palette.blue]
  ];
  const cards = steps.map((step, i) => {
    const x = 70 + i * 210;
    const y = i % 2 === 0 ? 205 : 315;
    return `${rect(x, y, 178, 142, { fill: step[2], stroke: step[3], radius: 12 })}
      ${multiline(step[0], x + 89, y + 42, { size: 26, weight: 800, fill: step[3], maxChars: 7 })}
      ${multiline(step[1], x + 89, y + 96, { size: 18, weight: 480, fill: palette.ink, maxChars: 12 })}`;
  }).join("\n");
  const arrows = steps.slice(0, -1).map((_, i) => {
    const x1 = 248 + i * 210;
    const y1 = i % 2 === 0 ? 276 : 386;
    const x2 = 70 + (i + 1) * 210;
    const y2 = (i + 1) % 2 === 0 ? 276 : 386;
    return arrow(x1 + 8, y1, x2 - 10, y2, palette.slate, 3);
  }).join("\n");
  const body = `
  ${multiline("量化“黑箱”的标准流水线", 700, 80, { size: 40, weight: 800, fill: palette.ink, maxChars: 24 })}
  ${multiline("每个模块都应有输入、输出、假设、约束和事后反馈；神秘感来自外部不可见，不来自不可解释。", 700, 130, { size: 22, weight: 450, fill: palette.muted, maxChars: 58 })}
  ${cards}
  ${arrows}
  <path d="M 1168 455 C 970 588, 430 588, 242 455" fill="none" stroke="${palette.slate}" stroke-width="3" stroke-dasharray="8 8" marker-end="url(#arrow)" opacity="0.8"/>
  ${multiline("实盘反馈：成交质量、滑点、回撤、信号衰减、容量变化", 700, 560, { size: 23, weight: 650, fill: palette.slate, maxChars: 42 })}
  ${pill(134, 494, 210, 52, "研究闭环", { fill: "#eef2ff", textFill: palette.blue })}
  ${pill(1048, 494, 210, 52, "交易闭环", { fill: palette.softAmber, textFill: palette.amber })}
`;
  return baseSvg(1400, 640, body, "量化黑箱系统流水线");
}

function modelStack() {
  const layers = [
    ["治理层", "投资目标、授权边界、风控红线、模型变更审批", 90, palette.softRed, palette.red],
    ["组合层", "预期收益 - 风险 - 成本 - 约束：共同决定目标权重", 190, palette.softGreen, palette.green],
    ["模型层", "Alpha、风险、交易成本、容量、执行质量模型", 300, palette.softTeal, palette.teal],
    ["数据层", "行情、财报、基本面、订单簿、事件、另类数据", 410, palette.softBlue, palette.blue],
    ["基础设施", "数据清洗、回测、监控、交易接口、审计日志", 520, "#e2e8f0", palette.slate]
  ];
  const blocks = layers.map(([name, desc, y, fill, stroke]) => `
    ${rect(210, y, 980, 78, { fill, stroke, radius: 12 })}
    ${multiline(name, 305, y + 49, { size: 26, weight: 800, fill: stroke, maxChars: 8 })}
    ${multiline(desc, 760, y + 49, { size: 23, weight: 500, fill: palette.ink, maxChars: 34 })}
  `).join("");
  const body = `
  ${multiline("量化系统不是一个模型，而是一组分层责任", 700, 60, { size: 38, weight: 800, fill: palette.ink, maxChars: 28 })}
  ${blocks}
  ${arrow(700, 505, 700, 488, palette.slate, 3)}
  ${arrow(700, 395, 700, 378, palette.slate, 3)}
  ${arrow(700, 285, 700, 268, palette.slate, 3)}
  ${arrow(700, 175, 700, 158, palette.slate, 3)}
  ${rect(72, 165, 96, 350, { fill: "#ffffff", stroke: palette.line, radius: 12 })}
  ${multiline(["可", "检", "查"], 120, 245, { size: 28, weight: 800, fill: palette.slate, maxChars: 2 })}
  ${multiline(["可", "复", "盘"], 120, 365, { size: 28, weight: 800, fill: palette.slate, maxChars: 2 })}
  ${multiline(["可", "治理"], 120, 485, { size: 28, weight: 800, fill: palette.slate, maxChars: 2 })}
  ${rect(1232, 165, 96, 350, { fill: "#ffffff", stroke: palette.line, radius: 12 })}
  ${multiline(["防", "过", "拟", "合"], 1280, 245, { size: 25, weight: 800, fill: palette.red, maxChars: 2 })}
  ${multiline(["防", "拥", "挤"], 1280, 385, { size: 25, weight: 800, fill: palette.amber, maxChars: 2 })}
  ${multiline(["防", "失", "控"], 1280, 500, { size: 25, weight: 800, fill: palette.green, maxChars: 2 })}
`;
  return baseSvg(1400, 650, body, "量化投资系统责任分层");
}

function taxonomy() {
  const items = [
    ["高频 / 做市 / 微观结构", "毫秒到分钟", "速度、订单簿、库存控制", 80, 170, palette.softBlue, palette.blue],
    ["统计套利 / 均值回归", "分钟到数天", "价差、配对、短期偏离", 390, 170, palette.softTeal, palette.teal],
    ["趋势 / 动量", "数天到数月", "延续性、止损、波动过滤", 700, 170, palette.softGreen, palette.green],
    ["基本面 / 事件 / 质量", "季度到数年", "估值、盈利、公告事件", 1010, 170, palette.softAmber, palette.amber],
    ["机器学习 / 另类数据", "跨时间尺度", "特征工程、验证、模型治理", 235, 400, "#eef2ff", palette.blue],
    ["组合与风险预算", "横跨所有策略", "相关性、容量、杠杆、回撤", 855, 400, palette.softRed, palette.red]
  ];
  const cards = items.map(([title, horizon, desc, x, y, fill, stroke]) => `
    ${rect(x, y, 300, 156, { fill, stroke, radius: 12 })}
    ${multiline(title, x + 150, y + 44, { size: 24, weight: 800, fill: stroke, maxChars: 15 })}
    ${multiline(horizon, x + 150, y + 90, { size: 21, weight: 650, fill: palette.ink, maxChars: 12 })}
    ${multiline(desc, x + 150, y + 128, { size: 18, weight: 480, fill: palette.muted, maxChars: 17 })}
  `).join("");
  const body = `
  ${multiline("量化不是一种策略，而是一条策略谱系", 700, 74, { size: 40, weight: 800, fill: palette.ink, maxChars: 26 })}
  ${multiline("越短周期越依赖执行和市场微观结构；越长周期越依赖研究假设、数据质量和风险预算。", 700, 126, { size: 22, weight: 450, fill: palette.muted, maxChars: 54 })}
  ${cards}
  <line x1="190" y1="360" x2="1210" y2="360" stroke="${palette.slate}" stroke-width="4" stroke-linecap="round"/>
  <circle cx="190" cy="360" r="9" fill="${palette.blue}"/>
  <circle cx="1210" cy="360" r="9" fill="${palette.amber}"/>
  ${multiline("交易速度", 190, 386, { size: 20, weight: 700, fill: palette.blue, maxChars: 8 })}
  ${multiline("研究深度", 1210, 386, { size: 20, weight: 700, fill: palette.amber, maxChars: 8 })}
`;
  return baseSvg(1400, 640, body, "量化策略谱系与时间尺度");
}

function riskChecklist() {
  const rows = [
    ["信号风险", "样本外失效、因子拥挤、数据挖掘", "滚动验证、实盘跟踪、信号衰减监控"],
    ["模型风险", "参数不稳、协方差估计错误、极端相关性上升", "压力测试、情景分析、模型委员会"],
    ["成本风险", "滑点高于回测、市场冲击、容量瓶颈", "成交回放、容量约束、低换手优先"],
    ["流动性风险", "无法成交、集中持仓、赎回压力", "持仓限额、现金缓冲、分层减仓"],
    ["操作风险", "代码错误、数据断流、交易接口异常", "灰度发布、kill switch、审计日志"],
    ["治理风险", "黑箱不可解释、权限失控、临时改规则", "权限边界、变更审批、事后复盘"]
  ];
  const rowSvg = rows.map((row, i) => {
    const y = 145 + i * 72;
    const fill = i % 2 === 0 ? "#ffffff" : "#f1f5f9";
    return `${rect(70, y, 1260, 58, { fill, stroke: palette.line, radius: 8, strokeWidth: 1 })}
      ${multiline(row[0], 180, y + 37, { size: 21, weight: 800, fill: palette.red, maxChars: 8 })}
      ${multiline(row[1], 560, y + 37, { size: 20, weight: 500, fill: palette.ink, maxChars: 27 })}
      ${multiline(row[2], 1040, y + 37, { size: 20, weight: 600, fill: palette.green, maxChars: 27 })}`;
  }).join("");
  const body = `
  ${multiline("评估量化策略时，先问风险如何被控制", 700, 72, { size: 39, weight: 800, fill: palette.ink, maxChars: 28 })}
  ${rect(70, 104, 1260, 40, { fill: palette.slate, stroke: palette.slate, radius: 8 })}
  ${multiline("风险类别", 180, 131, { size: 20, weight: 800, fill: palette.white, maxChars: 8 })}
  ${multiline("典型失效方式", 560, 131, { size: 20, weight: 800, fill: palette.white, maxChars: 12 })}
  ${multiline("应有控制机制", 1040, 131, { size: 20, weight: 800, fill: palette.white, maxChars: 12 })}
  ${rowSvg}
  ${multiline("黑箱可怕的不是复杂，而是没有权限边界、没有成本校准、没有可复盘的失败记录。", 700, 618, { size: 24, weight: 650, fill: palette.slate, maxChars: 48 })}
`;
  return baseSvg(1400, 680, body, "量化策略风险与尽调清单");
}

await writeSvg("quant-blackbox-cover.svg", cover());
await writeSvg("quant-blackbox-hero.svg", hero());
await writeSvg("quant-blackbox-pipeline.svg", pipeline());
await writeSvg("quant-blackbox-model-stack.svg", modelStack());
await writeSvg("quant-blackbox-strategy-taxonomy.svg", taxonomy());
await writeSvg("quant-blackbox-risk-checklist.svg", riskChecklist());

console.log(`Generated SVG assets in ${outDir}`);
