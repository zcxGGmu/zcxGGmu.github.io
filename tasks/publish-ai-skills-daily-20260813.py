from __future__ import annotations

import importlib.util
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
BASE = TASKS / "publish-three-life-business-articles-20260809.py"
spec = importlib.util.spec_from_file_location("publisher", BASE)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = base
spec.loader.exec_module(base)

base.__file__ = __file__
base.DATE = "2026-08-14"
base.BASE_DT = datetime(2026, 8, 14, 6, 20, tzinfo=timezone(timedelta(hours=8)))
base.PREV_EXISTING_URL = "/2026/remotion-claude-code-vox-motion-design-workflow/"
base.PREV_EXISTING_TITLE = "用 Remotion 和 Claude Code 生成 Vox 风格动效短片：从视觉系统到自动渲染"
base.SCRIPT_NAME = Path(__file__).name
base.MANIFEST_NAME = "publish-ai-skills-daily-20260813-changed-files.json"

BODY = r'''
<p>AI 工具的竞争焦点正在从模型参数转向工作完成率。一个能长期使用的系统，必须把知识、工具、执行环境、记忆、验证和界面质量接进同一条流程：先理解任务，再选择合适的能力包，随后在受控环境中执行，最后把结果和证据交回给人。8 月 13 日的项目热度，把这条链路集中呈现了出来。</p>
<p>面对几十个快速增长的项目，最重要的不是逐个安装，而是识别它们各自补的是哪一块短板。以下按任务执行、技能治理、并行协作、网页与知识、记忆与编码、界面质量六个层面整理，并把能够确认的开源仓库直接列出。</p>

<h2 id="from-chat-to-task">一、从聊天入口到任务执行器</h2>
<p><a href="https://github.com/Significant-Gravitas/AutoGPT" target="_blank" rel="noopener">Significant-Gravitas/AutoGPT</a> 是自主任务执行最早的代表之一。它把目标拆分、资料收集、工具调用和结果汇总组织成循环，适合用来理解 Agent 为什么不只是对话框。实际落地时仍应把目标、预算、可访问资源和验收标准写清楚；高风险动作不能因为“能自动完成”就跳过人工确认。</p>
<p>任务型 Agent 的可靠性来自边界，而不是无限授权。一个实用的流程应先把任务拆成可验证步骤，再限制每一步可访问的数据和工具；对外发送、资金、生产系统和敏感文件应设置人工闸门。执行日志、失败原因和可复跑命令要成为交付物的一部分。</p>

<h2 id="skills-as-operational-knowledge">二、Skills 是可执行的团队知识</h2>
<p><a href="https://github.com/anthropics/claude-plugins-official" target="_blank" rel="noopener">anthropics/claude-plugins-official</a>、<a href="https://github.com/obra/superpowers" target="_blank" rel="noopener">obra/superpowers</a> 和 <a href="https://github.com/google/skills" target="_blank" rel="noopener">google/skills</a> 指向同一种方法：把规划、实现、测试、审查、发布和领域规则写成能在正确时机加载的操作说明。这样做的收益不是让助手替代工程判断，而是减少重复解释，把成熟做法变成稳定的起始约束。</p>
<p>技能包应像依赖一样管理。每个包都需要来源、版本、适用范围、权限和验证方式；安装第三方能力前，先用 <a href="https://github.com/cisco-ai-defense/skill-scanner" target="_blank" rel="noopener">cisco-ai-defense/skill-scanner</a> 这类检查工具审视可疑指令、越权行为和供应链风险。技能越接近文件、网络和账号操作，越要把最小权限和人工复核放在前面。</p>
<p>对于授权安全研究，<a href="https://github.com/zhaoxuya520/reverse-skill" target="_blank" rel="noopener">zhaoxuya520/reverse-skill</a> 的价值在于按目标类型组织工具与报告，而不是无边界地扫描。安全自动化必须先明确书面授权、目标范围和证据留存要求；自动结果只能作为初筛，关键系统仍需要独立人工审计。</p>

<h2 id="code-understanding-and-discipline">三、代码理解与工程纪律要一起补</h2>
<p>大代码库里，真正稀缺的不是生成几段代码，而是快速判断该改哪里、会影响什么、怎样证明没有回归。代码图谱、依赖索引和架构笔记可以把模块关系先组织起来，让 Agent 只读取必要上下文。这样既降低 token 消耗，也减少在陌生项目里误改无关文件的概率。</p>
<p>终端编码可直接使用 <a href="https://github.com/openai/codex" target="_blank" rel="noopener">openai/codex</a>，但稳定产出依赖工程闭环：先读约束和现有测试，提出最小修改，再运行定向验证，最后交代实际运行过的命令与剩余风险。代码审查不应被当成形式动作，尤其要检查输入边界、权限、错误处理、并发和部署回滚。</p>
<p>“少写不必要代码”也是重要能力。AI 容易把简单需求扩成多层抽象，短期看很全面，长期却抬高维护成本。评审时应主动追问：现有模块是否已经覆盖这个需求？能否删除而不是新增？接口是否真的需要泛化？克制的实现通常更容易测试、解释和维护。</p>

<h2 id="agent-orchestration">四、并行协作的前提是职责清晰</h2>
<p>多 Agent 的价值不是把同一问题问很多遍，而是把相互独立的工作拆给不同角色：研究者收集证据，实现者改动代码，测试者复现和验证，审查者专门寻找风险。主控角色只负责拆分、合并和最终决策，每个子任务必须交回可检查的证据，而不是只有一句结论。</p>
<p>并行适合资料检索、独立模块实现、测试矩阵和输出核查；存在共享状态、严格时序或高风险副作用的工作应串行推进。把每个任务的输入、允许工具、输出格式和完成条件写清楚，才能避免多个执行器互相覆盖、重复消耗或把错误放大。</p>

<h2 id="web-and-knowledge">五、网页与知识库先结构化，再交给模型</h2>
<p><a href="https://github.com/firecrawl/firecrawl" target="_blank" rel="noopener">firecrawl/firecrawl</a> 解决的是网页内容难以直接被模型使用的问题：把页面清洗为 Markdown 或结构化数据，再进入研究、检索和问答流程。网页抓取需要遵守站点条款、访问控制和数据边界；需要登录或受限的数据不能用“自动化”绕过授权。</p>
<p><a href="https://github.com/infiniflow/ragflow" target="_blank" rel="noopener">infiniflow/ragflow</a> 代表检索增强的另一端：回答前优先查真实资料，找不到就明确不确定。企业知识库的效果取决于原始文档质量、切分策略、权限隔离和引用可追溯性。把文档直接堆给模型并不能自动得到可靠知识系统。</p>
<p>资料进入工作流后，应保留来源、版本和时间。研究结论要能回到原始证据，关键数字和政策信息要交叉核验。Agent 适合做初步收集、分类和摘要，但不应凭空补全缺失事实。</p>

<h2 id="context-and-cost-control">六、上下文压缩与成本控制不能牺牲证据</h2>
<p>长任务的真正瓶颈常常不是模型能力，而是上下文越堆越长。有效的做法不是粗暴删减，而是先把问题、约束、已验证事实、待办和失败尝试分别存放；后续执行者只读取当前步骤需要的部分。代码地图、文档索引和结构化任务记录都能降低重复阅读的成本。</p>
<p>压缩后的信息必须保留出处和不确定性。数字、接口契约、权限规则、测试结论不能被压成一句没有来源的断言。对于长链路任务，推荐在每个阶段生成简短的交接记录：完成了什么、依据是什么、修改了哪些文件、还剩什么风险。这样即使模型切换或任务中断，也能从可靠状态继续。</p>
<p>成本治理也需要可观测性。记录模型调用、工具耗时、失败重试和输出质量，才能判断某项自动化到底是在省时间还是在制造返工。先用小样本验证质量与单次成本，再扩大使用范围，比一次性把整条生产流程交给新工具稳得多。</p>

<h2 id="memory-and-long-running-work">七、记忆让经验复利，也带来治理责任</h2>
<p><a href="https://github.com/TencentCloud/TencentDB-Agent-Memory" target="_blank" rel="noopener">TencentCloud/TencentDB-Agent-Memory</a> 把对话事实、技能、文档知识和代码图谱分层保存。没有记忆的助手每次都像新成员；没有边界的记忆又会把隐私和错误偏好永久放大。正确做法是分层存储、角色访问、可删除、可审计，并给每条长期事实保留来源与失效条件。</p>
<p>自我改进也不等于自我放权。复盘可以记录失败模式、验证命令和用户偏好，但不能把未经确认的假设当成永久规则。对持续运行的任务，要有周期性复核、变更历史和一键停用机制；真正可靠的助手应该能解释“为什么这样做”，也能在证据不足时停止。</p>

<h2 id="creative-and-office-workflows">八、内容与办公自动化需要可编辑结果</h2>
<p><a href="https://github.com/Comfy-Org/ComfyUI" target="_blank" rel="noopener">Comfy-Org/ComfyUI</a> 用节点图把图像和影像生成拆成可复用步骤，适合需要精细控制模型、提示词、采样和后处理的创作工作流。节点化的优势是参数可追踪、结果可复现；代价是需要管理模型、显存、素材来源和工作流版本。</p>
<p>办公自动化的验收不应只是“生成了文件”。报告、表格和演示稿必须保持可编辑、结构正确、数据可核对，并且在真实办公软件中打开检查。自动化适合处理格式整理、初稿和批量转换，关键结论、排版与对外措辞仍需要负责人审阅。</p>

<h2 id="deployment-and-verification">九、部署与验证：自动化必须能证明自己正确</h2>
<p>无论输出是代码、研究报告、网页还是办公文档，都应该在交付前通过与风险相称的验证。代码至少要运行受影响的测试和静态检查；网页要检查链接、结构、移动端和构建产物；数据任务要核对样本范围、时间和异常值；涉及远端写入时要先读取当前版本，再以正常快进方式提交。</p>
<p>验证不仅是命令返回成功。需要检查结果内容是否真的符合预期：接口是不是返回了正确的 JSON，页面是不是有正确的标题和索引，生成文件是否可以打开，关键条目是否在正确顺序，失败是否被清晰记录。对可重复任务，最好把这些检查编进脚本，使每次执行都留下相同维度的证据。</p>
<p>发布环境还要考虑并发。多人或多个自动化同时更新时，不能基于过期版本覆盖远端内容；应在创建提交前重新读取分支头部，发现已变化就重新生成。可回滚的提交、内容清单、构建状态与已知限制，构成了自动化交付最后一道防线。</p>

<h2 id="ui-quality-is-a-system">十、UI 质量不是最后加一层皮肤</h2>
<p><a href="https://github.com/nextlevelbuilder/ui-ux-pro-max-skill" target="_blank" rel="noopener">nextlevelbuilder/ui-ux-pro-max-skill</a> 把色彩、排版、间距、组件层级、响应式边界和常见反模式整理成可调用的设计约束。它适合让生成式前端先遵守设计系统，再处理页面细节，而不是批量产出“能跑但缺乏秩序”的界面。</p>
<p>界面验收应覆盖信息层级、对比度、移动端文字溢出、交互状态、键盘访问和真实数据长度。截图好看只是开始；一个可用产品还要在加载、错误、空状态和窄屏下保持一致。设计规范和组件测试应尽早进入开发流程。</p>

<h2 id="selection-playbook">十一、选型顺序：先解决一条工作流</h2>
<p>个人开发者可以从一条低风险链路开始：用 Skills 固化编码与验证习惯，使用只读网页解析做资料整理，把项目决策写入本地记忆文件，再由测试与审查收口。团队则应先补权限、日志、密钥、审计和回滚，再扩展到多 Agent、云端电脑和对外自动化。</p>
<p>每个候选项目都值得做一次小范围验证：许可证与维护状态是否清楚，是否会发送敏感数据，依赖是否可信，失败时能否退出，能否接入现有测试与发布流程。热度说明需求强，却不能替代生产证据。</p>

<h2 id="conclusion">十二、结论：把工具组合成可治理的生产系统</h2>
<p>AI Skills、代码图谱、网页解析、记忆层、终端 Agent 和设计系统并不是互相替代的单品，而是组成可靠工作系统的不同层。技能提供方法，工具提供行动，记忆提供延续，测试提供证据，权限和审计提供边界。先让一条具体流程稳定运转，再逐步增加自动化，才能把开源项目的热度沉淀为持续效率。</p>
'''

base.POSTS = [base.Post(
    slug="ai-skills-agent-fullstack-open-source-daily-20260813",
    title="8月13日 AI Skills/Agent 全栈开源项目速览：把热度变成可治理的工作系统",
    desc="从任务执行、Skills 治理、代码理解、Agent 协作到网页知识、记忆与 UI 质量，梳理 AI 工具进入真实工作流的关键边界。",
    category="AI工具", series="AI Agent",
    tags=["AI Skills", "AI Agent", "开源项目", "GitHub", "Codex", "Agent框架", "工作流", "UI设计"],
    minutes=12, body=BODY, accent=("#0b1220", "#0f766e", "#2563eb"),
    required=["AutoGPT", "Skills", "Codex", "firecrawl", "记忆", "UI", "验证"], minimum=3600,
)]

_base_validate = base.validate
FORBIDDEN = ["B站", "bilibili", "Bilibili", "哔哩", "UP主", "up主", "原视频", "视频中", "视频里", "音频中", "音频里", "本期", "这期", "观看", "点赞", "投币", "收藏", "订阅", "关注", "三连", "BV1"]
EXPECTED = {
    "https://github.com/Significant-Gravitas/AutoGPT", "https://github.com/anthropics/claude-plugins-official",
    "https://github.com/obra/superpowers", "https://github.com/google/skills", "https://github.com/cisco-ai-defense/skill-scanner",
    "https://github.com/zhaoxuya520/reverse-skill", "https://github.com/openai/codex", "https://github.com/firecrawl/firecrawl",
    "https://github.com/infiniflow/ragflow", "https://github.com/TencentCloud/TencentDB-Agent-Memory",
    "https://github.com/Comfy-Org/ComfyUI", "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill",
}

def validate(outputs: dict[str, str]) -> None:
    _base_validate(outputs)
    article = outputs["2026/ai-skills-agent-fullstack-open-source-daily-20260813/index.html"]
    cover = outputs["images/posts/ai-skills-agent-fullstack-open-source-daily-20260813/cover.svg"]
    failures = [f"forbidden wording: {w}" for w in FORBIDDEN if w in article or w in cover]
    links = set(re.findall(r'https://github\.com/[^"<]+', article))
    missing = EXPECTED - links
    if missing: failures.append("missing verified links: " + ", ".join(sorted(missing)))
    if failures: raise SystemExit("\\n".join(failures))

base.validate = validate
base.main()
