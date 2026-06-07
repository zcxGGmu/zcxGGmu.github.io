import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { spawnSync } from "node:child_process";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, "..");
const outputDir = path.join(rootDir, "images", "posts", "lazycodex");
const skillDir = path.join(os.homedir(), ".codex", "skills", "fireworks-tech-graph");
const generator = path.join(skillDir, "scripts", "generate-from-template.py");

fs.mkdirSync(outputDir, { recursive: true });

const claude = {
  style: 6,
  style_overrides: {
    title_align: "center",
    node_stroke: "#d9d0c3",
    section_stroke: "#ded8cf",
    arrow_label_bg: "#f8f6f3"
  }
};

const diagrams = [
  {
    type: "architecture",
    file: "lazycodex-cover",
    pngScale: 2,
    data: {
      ...claude,
      width: 1200,
      height: 630,
      title: "LazyCodex",
      subtitle: "把 OmO agent harness 打包成 Codex 的项目记忆、规划、执行与验证工作台",
      containers: [
        { x: 70, y: 132, width: 1060, height: 104, side_label: "Install", side_label_x: 36, side_label_anchor: "start", stroke: "#ded8cf", fill: "none" },
        { x: 70, y: 276, width: 1060, height: 116, side_label: "Codex", side_label_x: 36, side_label_anchor: "start", stroke: "#ded8cf", fill: "none" },
        { x: 70, y: 432, width: 1060, height: 112, side_label: "Evidence", side_label_x: 36, side_label_anchor: "start", stroke: "#ded8cf", fill: "none" }
      ],
      nodes: [
        { id: "alias", kind: "rect", x: 128, y: 156, width: 226, height: 72, label: "npx lazycodex-ai", sublabel: "install alias", type_label: "ALIAS", fill: "#fffaf3", stroke: "#d97757", flat: true },
        { id: "omo", kind: "double_rect", x: 478, y: 150, width: 246, height: 84, label: "oh-my-openagent", sublabel: "omo install --platform=codex", type_label: "HARNESS", fill: "#f7ecda", stroke: "#d0b893" },
        { id: "plugin", kind: "double_rect", x: 836, y: 150, width: 230, height: 84, label: "OMO Plugin", sublabel: "skills + hooks + MCP", type_label: "PLUGIN", fill: "#c8e4db", stroke: "#7b8b5c" },
        { id: "memory", kind: "rect", x: 120, y: 310, width: 196, height: 68, label: "/init-deep", sublabel: "hierarchical AGENTS.md", type_label: "MEMORY", fill: "#e9f1fb", stroke: "#8c6f5a", flat: true },
        { id: "plan", kind: "rect", x: 384, y: 310, width: 196, height: 68, label: "$ulw-plan", sublabel: "decision-complete plan", type_label: "PLANNING", fill: "#f7ecda", stroke: "#d0b893", flat: true },
        { id: "work", kind: "rect", x: 648, y: 310, width: 196, height: 68, label: "$start-work", sublabel: "Boulder execution", type_label: "DELIVERY", fill: "#c8e4db", stroke: "#7b8b5c", flat: true },
        { id: "loop", kind: "rect", x: 912, y: 310, width: 196, height: 68, label: "$ulw-loop", sublabel: "Oracle verified loop", type_label: "VERIFY", fill: "#efe8de", stroke: "#d0c3b3", flat: true },
        { id: "rules", kind: "cylinder", x: 144, y: 462, width: 190, height: 72, label: "Rule Context", sublabel: "CONTEXT / rules / instructions", fill: "#e5e8df", stroke: "#7b8b5c" },
        { id: "diagnostics", kind: "rect", x: 428, y: 470, width: 216, height: 60, label: "LSP + Comment Check", sublabel: "post-edit feedback", type_label: "DIAGNOSTICS", fill: "#e9f1fb", stroke: "#8c6f5a", flat: true },
        { id: "ledger", kind: "cylinder", x: 742, y: 462, width: 214, height: 72, label: "Evidence Ledger", sublabel: ".omo/start-work/*.jsonl", fill: "#efe8de", stroke: "#d0c3b3" }
      ],
      arrows: [
        { source: "alias", target: "omo", source_port: "right", target_port: "left", flow: "control", label: "delegates" },
        { source: "omo", target: "plugin", source_port: "right", target_port: "left", flow: "write", label: "installs" },
        { source: "memory", target: "plan", source_port: "right", target_port: "left", flow: "read" },
        { source: "plan", target: "work", source_port: "right", target_port: "left", flow: "control" },
        { source: "work", target: "loop", source_port: "right", target_port: "left", flow: "feedback" },
        { source: "rules", target: "diagnostics", source_port: "right", target_port: "left", flow: "read" },
        { source: "diagnostics", target: "ledger", source_port: "right", target_port: "left", flow: "write" }
      ],
      legend: []
    }
  },
  {
    type: "architecture",
    file: "lazycodex-system-architecture",
    pngScale: 2,
    data: {
      ...claude,
      width: 1200,
      height: 840,
      title: "LazyCodex 系统架构",
      subtitle: "轻量 npm 入口 + OmO 聚合插件 + Codex 生命周期扩展 + 本地证据层",
      containers: [
        { x: 58, y: 112, width: 1084, height: 106, side_label: "Entry", side_label_x: 30, side_label_anchor: "start", stroke: "#ded8cf", fill: "none" },
        { x: 58, y: 252, width: 1084, height: 128, side_label: "Package", side_label_x: 30, side_label_anchor: "start", stroke: "#ded8cf", fill: "none" },
        { x: 58, y: 416, width: 1084, height: 132, side_label: "Surface", side_label_x: 30, side_label_anchor: "start", stroke: "#ded8cf", fill: "none" },
        { x: 58, y: 584, width: 1084, height: 126, side_label: "Runtime", side_label_x: 30, side_label_anchor: "start", stroke: "#ded8cf", fill: "none" }
      ],
      nodes: [
        { id: "user", kind: "user_avatar", x: 92, y: 138, width: 190, height: 64, label: "Codex User", sublabel: "workspace task", fill: "#e9f1fb", stroke: "#8c6f5a" },
        { id: "codex", kind: "double_rect", x: 430, y: 132, width: 260, height: 76, label: "Codex App / CLI", sublabel: "plugins + hooks enabled", type_label: "HOST", fill: "#fffaf3", stroke: "#d0b893" },
        { id: "alias", kind: "rect", x: 116, y: 286, width: 246, height: 70, label: "lazycodex-ai", sublabel: "bin/lazycodex-ai.js", type_label: "NPM ALIAS", fill: "#fffaf3", stroke: "#d97757", flat: true },
        { id: "npx", kind: "rect", x: 474, y: 286, width: 226, height: 70, label: "npx Delegation", sublabel: "--package oh-my-openagent", type_label: "PROCESS", fill: "#f7ecda", stroke: "#d0b893", flat: true },
        { id: "installer", kind: "double_rect", x: 830, y: 280, width: 230, height: 82, label: "OmO Installer", sublabel: "omo install --platform=codex", type_label: "INSTALLER", fill: "#c8e4db", stroke: "#7b8b5c" },
        { id: "manifest", kind: "rect", x: 96, y: 448, width: 190, height: 70, label: "plugin.json", sublabel: "omo namespace", type_label: "MANIFEST", fill: "#efe8de", stroke: "#d0c3b3", flat: true },
        { id: "skills", kind: "rect", x: 356, y: 448, width: 190, height: 70, label: "skills/", sublabel: "workflow playbooks", type_label: "PLAYBOOKS", fill: "#e9f1fb", stroke: "#8c6f5a", flat: true },
        { id: "hooks", kind: "rect", x: 616, y: 448, width: 190, height: 70, label: "hooks/", sublabel: "lifecycle injection", type_label: "LIFECYCLE", fill: "#f7ecda", stroke: "#d0b893", flat: true },
        { id: "mcp", kind: "rect", x: 876, y: 448, width: 190, height: 70, label: ".mcp.json", sublabel: "LSP / grep / context", type_label: "TOOLS", fill: "#c8e4db", stroke: "#7b8b5c", flat: true },
        { id: "components", kind: "double_rect", x: 154, y: 622, width: 276, height: 70, label: "Component CLIs", sublabel: "rules, lsp, telemetry, ulw", type_label: "DIST", fill: "#fffaf3", stroke: "#d0b893" },
        { id: "state", kind: "cylinder", x: 562, y: 614, width: 220, height: 84, label: "Local State", sublabel: ".omo + plugin data", fill: "#e5e8df", stroke: "#7b8b5c" },
        { id: "web", kind: "rect", x: 894, y: 632, width: 176, height: 60, label: "Docs Site", sublabel: "lazycodex.ai", type_label: "NEXT.JS", fill: "#efe8de", stroke: "#d0c3b3", flat: true }
      ],
      arrows: [
        { source: "user", target: "codex", source_port: "right", target_port: "left", flow: "control", label: "runs task" },
        { source: "alias", target: "npx", source_port: "right", target_port: "left", flow: "control", label: "rewrites args" },
        { source: "npx", target: "installer", source_port: "right", target_port: "left", flow: "control", label: "executes" },
        { source: "installer", target: "manifest", source_port: "bottom", target_port: "top", flow: "write", route_points: [[945, 392], [190, 392], [190, 438]], label: "copies plugin" },
        { source: "installer", target: "skills", source_port: "bottom", target_port: "top", flow: "write", route_points: [[945, 392], [451, 392], [451, 438]] },
        { source: "installer", target: "hooks", source_port: "bottom", target_port: "top", flow: "write", route_points: [[945, 392], [711, 392], [711, 438]] },
        { source: "installer", target: "mcp", source_port: "bottom", target_port: "top", flow: "write", route_points: [[945, 392], [971, 392], [971, 438]] },
        { source: "hooks", target: "components", source_port: "bottom", target_port: "top", flow: "read", route_points: [[711, 562], [292, 562], [292, 622]] },
        { source: "components", target: "state", source_port: "right", target_port: "left", flow: "write", label: "persist" },
        { source: "mcp", target: "components", source_port: "bottom", target_port: "top", flow: "read", route_points: [[971, 562], [292, 562], [292, 622]] },
        { source: "skills", target: "state", source_port: "bottom", target_port: "top", flow: "feedback", dashed: true, route_points: [[451, 562], [672, 562], [672, 614]] }
      ],
      legend: [
        { flow: "control", label: "CLI delegation" },
        { flow: "write", label: "installed / persisted state" },
        { flow: "read", label: "hook and MCP dispatch" },
        { flow: "feedback", label: "workflow evidence loop" }
      ],
      legend_position: "bottom-right",
      legend_box: true,
      legend_box_fill: "#fffaf3",
      legend_y: 750
    }
  },
  {
    type: "flowchart",
    file: "lazycodex-command-workflow",
    pngScale: 2,
    data: {
      ...claude,
      width: 1200,
      height: 900,
      title: "LazyCodex 工作流",
      subtitle: "从项目记忆到规划、执行、证据记录，再到独立验证的闭环",
      containers: [
        { x: 66, y: 112, width: 1070, height: 116, side_label: "Memory", side_label_x: 30, side_label_anchor: "start", stroke: "#ded8cf", fill: "none" },
        { x: 66, y: 262, width: 1070, height: 164, side_label: "Plan", side_label_x: 30, side_label_anchor: "start", stroke: "#ded8cf", fill: "none" },
        { x: 66, y: 462, width: 1070, height: 198, side_label: "Execute", side_label_x: 30, side_label_anchor: "start", stroke: "#ded8cf", fill: "none" },
        { x: 66, y: 722, width: 1070, height: 112, side_label: "Done", side_label_x: 30, side_label_anchor: "start", stroke: "#ded8cf", fill: "none" }
      ],
      nodes: [
        { id: "repo", kind: "rect", x: 128, y: 140, width: 210, height: 66, label: "Repository", sublabel: "large / old codebase", type_label: "CODEBASE", fill: "#e9f1fb", stroke: "#8c6f5a", flat: true },
        { id: "init", kind: "rect", x: 462, y: 140, width: 220, height: 64, label: "/init-deep", sublabel: "generate AGENTS.md", type_label: "DISCOVERY", fill: "#c8e4db", stroke: "#7b8b5c", flat: true },
        { id: "agents", kind: "rect", x: 828, y: 140, width: 210, height: 66, label: "AGENTS.md", sublabel: "hierarchical memory", type_label: "MEMORY", fill: "#e5e8df", stroke: "#7b8b5c", flat: true },
        { id: "request", kind: "speech", x: 118, y: 304, width: 216, height: 66, label: "User Goal", sublabel: "ambiguous work", fill: "#e9f1fb", stroke: "#8c6f5a" },
        { id: "plan", kind: "rect", x: 448, y: 302, width: 240, height: 70, label: "$ulw-plan", sublabel: "explore -> ask -> approve", type_label: "PROMETHEUS", fill: "#f7ecda", stroke: "#d0b893", flat: true },
        { id: "planfile", kind: "rect", x: 826, y: 302, width: 222, height: 72, label: ".omo/plans/*.md", sublabel: "decision-complete TODOs", type_label: "PLAN FILE", fill: "#efe8de", stroke: "#d0c3b3", flat: true },
        { id: "boulder", kind: "cylinder", x: 120, y: 500, width: 218, height: 88, label: "Boulder State", sublabel: ".omo/boulder.json", fill: "#e5e8df", stroke: "#7b8b5c" },
        { id: "execute", kind: "rect", x: 452, y: 492, width: 240, height: 76, label: "$start-work", sublabel: "next checkbox + subagents", type_label: "EXECUTION", fill: "#c8e4db", stroke: "#7b8b5c", flat: true },
        { id: "evidence", kind: "cylinder", x: 822, y: 492, width: 234, height: 88, label: "Evidence Ledger", sublabel: "tests / QA / cleanup", fill: "#efe8de", stroke: "#d0c3b3" },
        { id: "review", kind: "rect", x: 450, y: 606, width: 244, height: 62, label: "AdversarialVerify", sublabel: "independent reviewer", type_label: "ORACLE", fill: "#fffaf3", stroke: "#d97757", flat: true },
        { id: "done", kind: "double_rect", x: 416, y: 754, width: 330, height: 66, label: "ORCHESTRATION COMPLETE", sublabel: "all checkboxes verified", type_label: "FINISH", fill: "#c8e4db", stroke: "#7b8b5c" },
        { id: "loop", kind: "rect", x: 822, y: 614, width: 238, height: 56, label: "$ulw-loop", sublabel: "verified completion loop", type_label: "OPEN-ENDED", fill: "#f7ecda", stroke: "#d0b893", flat: true }
      ],
      arrows: [
        { source: "repo", target: "init", source_port: "right", target_port: "left", flow: "read", label: "scan" },
        { source: "init", target: "agents", source_port: "right", target_port: "left", flow: "write", label: "write memory" },
        { source: "request", target: "plan", source_port: "right", target_port: "left", flow: "control", label: "clarify" },
        { source: "agents", target: "plan", source_port: "bottom", target_port: "top", flow: "read", route_points: [[933, 250], [568, 250], [568, 302]], label: "context" },
        { source: "plan", target: "planfile", source_port: "right", target_port: "left", flow: "write", label: "approved plan" },
        { source: "planfile", target: "boulder", source_port: "bottom", target_port: "top", flow: "write", route_points: [[937, 444], [229, 444], [229, 500]], label: "active work" },
        { source: "boulder", target: "execute", source_port: "right", target_port: "left", flow: "read", label: "resume" },
        { source: "execute", target: "evidence", source_port: "right", target_port: "left", flow: "write", label: "record" },
        { source: "evidence", target: "review", source_port: "bottom", target_port: "right", flow: "feedback", route_points: [[939, 596], [939, 637], [694, 637]], label: "audit" },
        { source: "review", target: "execute", source_port: "top", target_port: "bottom", flow: "feedback", dashed: true, route_points: [[568, 606], [568, 568]], label: "needs-fix" },
        { source: "review", target: "done", source_port: "bottom", target_port: "top", flow: "control", route_points: [[572, 692], [572, 754]], label: "confirmed" },
        { source: "loop", target: "review", source_port: "left", target_port: "right", flow: "feedback", dashed: true, label: "oracle gate" }
      ],
      legend: [
        { flow: "read", label: "context read" },
        { flow: "write", label: "state / evidence write" },
        { flow: "control", label: "approved control path" },
        { flow: "feedback", label: "review loop" }
      ],
      legend_position: "bottom-right",
      legend_box: true,
      legend_box_fill: "#fffaf3",
      legend_y: 776
    }
  },
  {
    type: "architecture",
    file: "lazycodex-hook-lifecycle",
    pngScale: 2,
    data: {
      ...claude,
      width: 1200,
      height: 920,
      title: "Codex 生命周期 Hook",
      subtitle: "LazyCodex 在会话、提示、工具调用、压缩和停止阶段注入上下文、检查与续跑指令",
      containers: [
        { x: 66, y: 112, width: 1070, height: 92, side_label: "Session", side_label_x: 26, side_label_anchor: "start", stroke: "#ded8cf", fill: "none" },
        { x: 66, y: 236, width: 1070, height: 120, side_label: "Prompt", side_label_x: 26, side_label_anchor: "start", stroke: "#ded8cf", fill: "none" },
        { x: 66, y: 388, width: 1070, height: 118, side_label: "Tool Use", side_label_x: 26, side_label_anchor: "start", stroke: "#ded8cf", fill: "none" },
        { x: 66, y: 538, width: 1070, height: 110, side_label: "PostTool", side_label_x: 26, side_label_anchor: "start", stroke: "#ded8cf", fill: "none" },
        { x: 66, y: 700, width: 1070, height: 118, side_label: "Stop", side_label_x: 26, side_label_anchor: "start", stroke: "#ded8cf", fill: "none" }
      ],
      nodes: [
        { id: "ss", kind: "rect", x: 112, y: 136, width: 170, height: 48, label: "SessionStart", type_label: "EVENT", fill: "#e9f1fb", stroke: "#8c6f5a", flat: true },
        { id: "rules0", kind: "rect", x: 362, y: 134, width: 178, height: 52, label: "Rules", sublabel: "static context", type_label: "CONTEXT", fill: "#e5e8df", stroke: "#7b8b5c", flat: true },
        { id: "telemetry", kind: "rect", x: 602, y: 134, width: 178, height: 52, label: "Telemetry", sublabel: "daily active", type_label: "LOCAL", fill: "#efe8de", stroke: "#d0c3b3", flat: true },
        { id: "update", kind: "rect", x: 842, y: 134, width: 178, height: 52, label: "Auto Update", sublabel: "startup only", type_label: "CHECK", fill: "#f7ecda", stroke: "#d0b893", flat: true },
        { id: "ups", kind: "rect", x: 112, y: 276, width: 170, height: 48, label: "Prompt", type_label: "EVENT", fill: "#e9f1fb", stroke: "#8c6f5a", flat: true },
        { id: "rules1", kind: "rect", x: 342, y: 270, width: 182, height: 62, label: "Rules", sublabel: "load project rules", type_label: "CONTEXT", fill: "#e5e8df", stroke: "#7b8b5c", flat: true },
        { id: "ultra", kind: "rect", x: 578, y: 270, width: 188, height: 62, label: "Ultrawork", sublabel: "trigger directive", type_label: "MODE", fill: "#f7ecda", stroke: "#d0b893", flat: true },
        { id: "steer", kind: "rect", x: 820, y: 270, width: 194, height: 62, label: "ulw-loop", sublabel: "steering update", type_label: "GOAL", fill: "#fffaf3", stroke: "#d97757", flat: true },
        { id: "pre", kind: "rect", x: 112, y: 416, width: 170, height: 48, label: "PreToolUse", type_label: "EVENT", fill: "#e9f1fb", stroke: "#8c6f5a", flat: true },
        { id: "gitbash", kind: "rect", x: 342, y: 408, width: 188, height: 64, label: "Git Bash MCP", sublabel: "Bash guidance", type_label: "SHELL", fill: "#f7ecda", stroke: "#d0b893", flat: true },
        { id: "goalguard", kind: "rect", x: 582, y: 408, width: 190, height: 64, label: "Goal Guard", sublabel: "deny token_budget", type_label: "GUARD", fill: "#fffaf3", stroke: "#d97757", flat: true },
        { id: "post", kind: "rect", x: 826, y: 416, width: 170, height: 48, label: "PostToolUse", type_label: "EVENT", fill: "#e9f1fb", stroke: "#8c6f5a", flat: true },
        { id: "comment", kind: "rect", x: 270, y: 560, width: 196, height: 58, label: "Comment Checker", sublabel: "edit-like tools", type_label: "QUALITY", fill: "#efe8de", stroke: "#d0c3b3", flat: true },
        { id: "lsp", kind: "rect", x: 520, y: 560, width: 196, height: 58, label: "LSP Diagnostics", sublabel: "post-edit errors", type_label: "CODE INTEL", fill: "#e9f1fb", stroke: "#8c6f5a", flat: true },
        { id: "rules2", kind: "rect", x: 770, y: 560, width: 196, height: 58, label: "Dynamic Rules", sublabel: "file-specific context", type_label: "CONTEXT", fill: "#e5e8df", stroke: "#7b8b5c", flat: true },
        { id: "stop", kind: "rect", x: 134, y: 736, width: 170, height: 48, label: "Stop", type_label: "EVENT", fill: "#e9f1fb", stroke: "#8c6f5a", flat: true },
        { id: "boulder", kind: "cylinder", x: 418, y: 724, width: 208, height: 74, label: "Boulder Reader", sublabel: ".omo/boulder.json", fill: "#e5e8df", stroke: "#7b8b5c" },
        { id: "block", kind: "double_rect", x: 760, y: 730, width: 244, height: 64, label: "Continuation Block", sublabel: "inject next turn", type_label: "RESUME", fill: "#f7ecda", stroke: "#d0b893" }
      ],
      arrows: [
        { source: "ss", target: "rules0", source_port: "right", target_port: "left", flow: "read" },
        { source: "rules0", target: "telemetry", source_port: "right", target_port: "left", flow: "control" },
        { source: "telemetry", target: "update", source_port: "right", target_port: "left", flow: "control" },
        { source: "ups", target: "rules1", source_port: "right", target_port: "left", flow: "read" },
        { source: "rules1", target: "ultra", source_port: "right", target_port: "left", flow: "control" },
        { source: "ultra", target: "steer", source_port: "right", target_port: "left", flow: "feedback" },
        { source: "pre", target: "gitbash", source_port: "right", target_port: "left", flow: "control" },
        { source: "gitbash", target: "goalguard", source_port: "right", target_port: "left", flow: "feedback" },
        { source: "post", target: "comment", source_port: "bottom", target_port: "top", flow: "read", route_points: [[911, 522], [368, 522], [368, 560]] },
        { source: "post", target: "lsp", source_port: "bottom", target_port: "top", flow: "read", route_points: [[911, 522], [618, 522], [618, 560]] },
        { source: "post", target: "rules2", source_port: "bottom", target_port: "top", flow: "read", route_points: [[911, 522], [868, 522], [868, 560]] },
        { source: "stop", target: "boulder", source_port: "right", target_port: "left", flow: "read", label: "read state" },
        { source: "boulder", target: "block", source_port: "right", target_port: "left", flow: "write", label: "decision:block" }
      ],
      legend: [
        { flow: "read", label: "context or state read" },
        { flow: "control", label: "lifecycle dispatch" },
        { flow: "write", label: "hook output / block directive" },
        { flow: "feedback", label: "steering or guard feedback" }
      ],
      legend_position: "bottom-right",
      legend_box: true,
      legend_box_fill: "#fffaf3",
      legend_y: 812
    }
  },
  {
    type: "architecture",
    file: "lazycodex-module-map",
    pngScale: 2,
    data: {
      ...claude,
      width: 1200,
      height: 880,
      title: "LazyCodex 功能模块图",
      subtitle: "命令、skills、hooks、MCP、组件和文档站共同构成 Codex 侧的工程工作台",
      containers: [
        { x: 62, y: 112, width: 1080, height: 148, side_label: "Distribution", side_label_x: 28, side_label_anchor: "start", stroke: "#ded8cf", fill: "none" },
        { x: 62, y: 298, width: 1080, height: 178, side_label: "Workflow", side_label_x: 28, side_label_anchor: "start", stroke: "#ded8cf", fill: "none" },
        { x: 62, y: 514, width: 1080, height: 126, side_label: "Runtime", side_label_x: 28, side_label_anchor: "start", stroke: "#ded8cf", fill: "none" },
        { x: 62, y: 682, width: 1080, height: 92, side_label: "Support", side_label_x: 28, side_label_anchor: "start", stroke: "#ded8cf", fill: "none" }
      ],
      nodes: [
        { id: "rootpkg", kind: "rect", x: 110, y: 148, width: 220, height: 72, label: "lazycodex-ai", sublabel: "npm package 0.2.2", type_label: "ROOT", fill: "#fffaf3", stroke: "#d97757", flat: true },
        { id: "submodule", kind: "double_rect", x: 448, y: 144, width: 232, height: 80, label: "oh-my-openagent", sublabel: "src submodule", type_label: "CORE", fill: "#f7ecda", stroke: "#d0b893" },
        { id: "web", kind: "rect", x: 810, y: 150, width: 224, height: 66, label: "packages/web", sublabel: "Next.js docs", type_label: "DOCS", fill: "#efe8de", stroke: "#d0c3b3", flat: true },
        { id: "commands", kind: "rect", x: 106, y: 328, width: 230, height: 76, label: "Command Pillars", sublabel: "ulw-plan / start-work / ulw-loop", type_label: "COMMANDS", fill: "#f7ecda", stroke: "#d0b893", flat: true },
        { id: "memory", kind: "rect", x: 404, y: 328, width: 214, height: 76, label: "Project Memory", sublabel: "init-deep / rules", type_label: "CONTEXT", fill: "#e5e8df", stroke: "#7b8b5c", flat: true },
        { id: "skills", kind: "rect", x: 690, y: 328, width: 214, height: 76, label: "Specialist Skills", sublabel: "review / refactor / frontend", type_label: "SKILLS", fill: "#e9f1fb", stroke: "#8c6f5a", flat: true },
        { id: "quality", kind: "rect", x: 954, y: 328, width: 130, height: 76, label: "QA", sublabel: "visual + LSP", type_label: "CHECK", fill: "#efe8de", stroke: "#d0c3b3", flat: true },
        { id: "hooks", kind: "rect", x: 124, y: 536, width: 214, height: 74, label: "Hook Layer", sublabel: "Codex lifecycle", type_label: "HOOKS", fill: "#f7ecda", stroke: "#d0b893", flat: true },
        { id: "mcp", kind: "rect", x: 430, y: 536, width: 214, height: 74, label: "MCP Layer", sublabel: "lsp / grep / context7", type_label: "MCP", fill: "#c8e4db", stroke: "#7b8b5c", flat: true },
        { id: "components", kind: "double_rect", x: 738, y: 532, width: 246, height: 82, label: "Components", sublabel: "rules, lsp, telemetry, git-bash", type_label: "LOCAL CLIS", fill: "#fffaf3", stroke: "#d0b893" },
        { id: "tests", kind: "rect", x: 226, y: 704, width: 208, height: 60, label: "Tests", sublabel: "package contracts", type_label: "SAFETY NET", fill: "#efe8de", stroke: "#d0c3b3", flat: true },
        { id: "catalog", kind: "rect", x: 574, y: 704, width: 208, height: 60, label: "Model Catalog", sublabel: "managed profiles", type_label: "ROUTING", fill: "#e5e8df", stroke: "#7b8b5c", flat: true },
        { id: "privacy", kind: "rect", x: 876, y: 704, width: 208, height: 60, label: "Privacy Surface", sublabel: "telemetry opt-out", type_label: "DISCLOSURE", fill: "#e9f1fb", stroke: "#8c6f5a", flat: true }
      ],
      arrows: [
        { source: "rootpkg", target: "submodule", source_port: "right", target_port: "left", flow: "control", label: "delegates" },
        { source: "submodule", target: "web", source_port: "right", target_port: "left", flow: "read", label: "documents" },
        { source: "commands", target: "memory", source_port: "right", target_port: "left", flow: "read" },
        { source: "memory", target: "skills", source_port: "right", target_port: "left", flow: "control" },
        { source: "skills", target: "quality", source_port: "right", target_port: "left", flow: "feedback" },
        { source: "hooks", target: "components", source_port: "right", target_port: "left", flow: "control", route_points: [[338, 573], [738, 573]] },
        { source: "mcp", target: "components", source_port: "right", target_port: "left", flow: "read" },
        { source: "components", target: "tests", source_port: "bottom", target_port: "top", flow: "feedback", dashed: true, route_points: [[861, 654], [330, 654], [330, 688]] },
        { source: "components", target: "catalog", source_port: "bottom", target_port: "top", flow: "read", route_points: [[861, 654], [678, 654], [678, 688]] },
        { source: "components", target: "privacy", source_port: "bottom", target_port: "top", flow: "write", route_points: [[861, 654], [980, 654], [980, 688]] }
      ],
      legend: [
        { flow: "control", label: "command / hook control" },
        { flow: "read", label: "context, model, MCP read" },
        { flow: "write", label: "state or disclosure surface" },
        { flow: "feedback", label: "quality feedback" }
      ],
      legend_position: "bottom-right",
      legend_box: true,
      legend_box_fill: "#fffaf3",
      legend_y: 802
    }
  }
];

function run(command, args, options = {}) {
  const result = spawnSync(command, args, {
    cwd: rootDir,
    encoding: "utf8",
    env: { ...process.env, PYTHONIOENCODING: "utf-8" },
    ...options
  });
  if (result.status !== 0) {
    throw new Error(`${command} ${args.join(" ")} failed\n${result.stderr || result.stdout}`);
  }
  return result;
}

function findEdge() {
  const candidates = [
    "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe",
    "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
  ];
  const found = candidates.find((candidate) => fs.existsSync(candidate));
  if (!found) throw new Error("Microsoft Edge was not found for SVG PNG export.");
  return found;
}

function exportPngWithEdge(svgPath, pngPath, width, height, scale) {
  const edge = findEdge();
  const profileDir = fs.mkdtempSync(path.join(os.tmpdir(), "lazycodex-edge-"));
  try {
    run(edge, [
      "--headless=new",
      "--disable-gpu",
      "--no-first-run",
      "--no-default-browser-check",
      `--user-data-dir=${profileDir}`,
      `--force-device-scale-factor=${scale}`,
      `--window-size=${width},${height}`,
      `--screenshot=${pngPath}`,
      pathToFileURL(svgPath).href
    ]);
  } finally {
    fs.rmSync(profileDir, { recursive: true, force: true });
  }
}

for (const diagram of diagrams) {
  const svgPath = path.join(outputDir, `${diagram.file}.svg`);
  const pngPath = path.join(outputDir, `${diagram.file}.png`);
  run("python", [generator, diagram.type, svgPath], {
    input: JSON.stringify(diagram.data)
  });
  run("python", ["-c", "import sys, xml.etree.ElementTree as ET; ET.parse(sys.argv[1])", svgPath]);
  exportPngWithEdge(svgPath, pngPath, diagram.data.width, diagram.data.height, diagram.pngScale ?? 2);
  console.log(`generated ${path.relative(rootDir, pngPath)}`);
}
