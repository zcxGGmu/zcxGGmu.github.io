from __future__ import annotations

import importlib.util
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


TASKS = Path(__file__).resolve().parent
BASE = TASKS / "publish-three-life-business-articles-20260809.py"
spec = importlib.util.spec_from_file_location("publisher", BASE)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = base
spec.loader.exec_module(base)

base.__file__ = __file__
base.DATE = "2026-08-11"
base.BASE_DT = datetime(2026, 8, 11, 6, 25, tzinfo=timezone(timedelta(hours=8)))
base.PREV_EXISTING_URL = "/2026/young-workers-flexible-jobs-factory-labor-dignity/"
base.PREV_EXISTING_TITLE = "为什么年轻人宁愿跑外卖也不进厂：自由、即时回报与劳动尊严"
base.SCRIPT_NAME = Path(__file__).name
base.MANIFEST_NAME = "publish-ai-skills-two-source-20260811-changed-files.json"

BODY_A = r'''
<p>AI 开发工具正在从“一个模型加一个聊天框”转向可组合的工作系统。新的分工越来越清楚：Skills 负责把专业做法变成可调用步骤，Agent 框架负责拆任务和交接，运行环境负责执行隔离，记忆层负责让经验不随会话消失，前端工具则把设计、代码和性能检查接到同一条流水线上。</p>
<p>这套工具栈的关键不在于装得越多越好，而在于把高频、可验证、边界明确的工作固化下来。开发者真正需要的是一套能控制输入、过程、权限和输出的协作系统，而不是一个无边界的万能助手。</p>
<h2 id="skills-are-operational-knowledge">一、Skills 把经验变成可执行接口</h2>
<p><a href="https://github.com/obra/superpowers">obra/superpowers</a> 代表了技能目录的价值：把开发、测试、审查、发布等方法写成可安装的工作约束。它不替代工程判断，而是让 Agent 在进入任务前先获得一致的操作边界。</p>
<p>官方插件与技能目录同样在推动格式标准化。<a href="https://github.com/anthropics/claude-plugins-official">anthropics/claude-plugins-official</a> 提供经过维护的插件集合；当团队把内部规范也组织成类似入口文件、检查清单和参考资料时，个人经验才有机会变成可复用资产。</p>
<h2 id="security-routing-needs-guardrails">二、安全任务必须先路由再执行</h2>
<p><a href="https://github.com/zhaoxuya520/reverse-skill">zhaoxuya520/reverse-skill</a> 的思路是先识别授权逆向、APK、前端加密、接口测试或固件分析等任务类型，再加载相应工具链。重点不是让模型“更敢做”，而是让它先说明范围、选择理由、证据和报告。</p>
<p>对第三方 Skills 也应先做供应链检查。<a href="https://github.com/cisco-ai-defense/skill-scanner">cisco-ai-defense/skill-scanner</a> 将技能内容中的危险指令、可疑行为和权限风险作为安装前检查项。把能力包当依赖管理，而不是当提示词复制，才是可靠的使用方式。</p>
<h2 id="multi-agent-is-workflow-design">三、多 Agent 的价值在于角色边界</h2>
<p>多人协作不是把同一个问题交给多个模型重复回答。有效的编排会分开计划、执行、验证与交付，并让每个角色只持有完成职责所需的上下文和权限。这样既能并行，也能让错误在审查环节被截住。</p>
<p>持久化记忆是这个体系的另一半。<a href="https://github.com/TencentCloud/TencentDB-Agent-Memory">TencentCloud/TencentDB-Agent-Memory</a> 将对话事实、Skill、文档知识与代码图分层保存，并允许按角色受控共享。接手者不必重新翻完历史，但也不该获得与任务无关的全部记忆。</p>
<h2 id="learning-and-local-inference">四、学习与推理都要可落地</h2>
<p><a href="https://github.com/microsoft/AI-For-Beginners">microsoft/AI-For-Beginners</a> 提供循序渐进的课程与实验，适合作为从概念到可运行代码的学习路径。课程、实验和复盘结合，比只积累术语更容易形成实际能力。</p>
<p>本地推理并不等于只能使用小模型。<a href="https://github.com/lyogavin/airllm">lyogavin/airllm</a> 通过分层装载降低大模型推理的显存门槛；<a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a> 则把终端式编码 Agent 的长时运行与前缀缓存稳定性放在核心位置。前者解决资源约束，后者解决持续工作时的上下文与运行稳定性。</p>
<h2 id="runtime-browser-and-model-gateway">五、执行环境、浏览器和模型网关</h2>
<p>Agent 一旦能运行代码、读写文件和访问网页，隔离就成为默认要求。<a href="https://github.com/cloudflare/sandbox-sdk">cloudflare/sandbox-sdk</a> 提供受隔离的运行环境思路：把不可信执行放进一次性或受控沙箱，而不是直接交给主机。</p>
<p>模型调用也应通过统一的可观测层管理。<a href="https://github.com/BerriAI/litellm">BerriAI/litellm</a> 支持统一接口、路由、成本记录和故障切换。对于浏览器任务，<a href="https://github.com/vercel-labs/agent-browser">vercel-labs/agent-browser</a> 提示了另一条原则：自动化需要可选择、可审计的专属浏览器上下文，不能任意接管用户正在使用的页面。</p>
<h2 id="knowledge-engineering">六、长资料先结构化，再交给 Agent</h2>
<p><a href="https://github.com/virgiliojr94/book-to-skill">virgiliojr94/book-to-skill</a> 把技术书和长文档拆成入口、章节、术语与速查结构。它的收益不是取代原始资料，而是让 Agent 先定位相关章节，再读取必要证据，减少整本资料反复进入上下文的成本。</p>
<p>知识工程的底线也很明确：自动整理稿不能替代关键数据、公式、许可条款和安全规则的人工核验。长期维护时，应记录来源、版本、修订人和适用范围，像维护代码一样维护 Skill。</p>
<h2 id="frontend-workflow">七、前端自动化应服务于设计系统</h2>
<p>前端 AI 的成熟标志不是更快生成一个页面，而是能检测组件层级、样式一致性、性能瓶颈与可访问性问题。设计稿转代码、性能分析和界面评审必须回到现有设计系统，否则“自动化”只会批量制造不一致。</p>
<p>例如 <a href="https://github.com/nextlevelbuilder/ui-ux-pro-max-skill">nextlevelbuilder/ui-ux-pro-max-skill</a> 将设计规则整理为可调用的技能。它更适合作为审查与约束层：统一色彩、字体、间距、组件行为和响应式边界，再由工程师对业务语义和真实交互负责。</p>
<h2 id="operating-model">八、从项目清单到团队操作系统</h2>
<p>这轮工具演进共同指向一个朴素结论：Agent 的能力来自工程系统，而不只来自模型参数。技能负责方法，编排负责责任，记忆负责延续，沙箱负责边界，网关负责模型治理，验证负责把输出变成可交付结果。</p>
<p>实际落地应从一个高频流程开始，例如“需求澄清到代码审查”或“长资料到团队知识库”。先定义输入、验收标准、权限和人工审批点，再逐步添加 Skills 与自动化。流程能稳定复现之后，工具数量才会成为杠杆，而不是维护负担。</p>
'''

BODY_B = r'''
<p>一周的 GitHub AI 增长榜并不等于长期价值榜，但它能及时显示开发者正在补哪些基础设施：安全路由、文档处理、团队记忆、本地推理、课程化学习，以及把模型能力嵌入生产流程的工具链。判断项目时，新增 Star 只是起点，更重要的是问题边界、实现路径和可持续维护能力。</p>
<h2 id="weekly-signal">一、增长信号要和问题定义一起看</h2>
<p>榜单的前列集中在三个问题：怎样让 Agent 先选对工具，怎样让它可靠处理复杂文档，怎样让它把项目经验留给下一个执行者。这些并不是花哨的应用层功能，而是 Agent 进入团队工作流前必须补齐的基础能力。</p>
<h2 id="reverse-skill">二、先判断任务类型的安全路由</h2>
<p><a href="https://github.com/zhaoxuya520/reverse-skill">zhaoxuya520/reverse-skill</a> 面向授权逆向、安全测试与研究场景，把 APK、前端代码、接口和固件等目标路由到不同技能与工具。其核心设计是按需加载而非一次性暴露所有工具，并保留范围、时间线、证据和报告。</p>
<p>这类项目的使用前提是明确授权。安全自动化的质量不只取决于能否得到结果，也取决于每一步是否可解释、可审计、可在权限边界内停止。</p>
<h2 id="pdf-inspector">三、PDF 处理先分流，后 OCR</h2>
<p><a href="https://github.com/firecrawl/pdf-inspector">firecrawl/pdf-inspector</a> 的价值在于先判断页面是文字页、扫描页、图片页还是混合页。带文字层的页面直接抽取并转为结构化文本，没有文字层的页面再进入 OCR，能避免把所有资料都送进昂贵且容易失真的识别流程。</p>
<p>文档工具的评价标准应包含表格、代码块、多栏阅读顺序、标题层级和浏览器端处理能力。对 RAG、合规归档与研究工作流而言，保留结构通常和提取正文同样重要。</p>
<h2 id="agent-memory">四、团队记忆不是聊天记录堆积</h2>
<p><a href="https://github.com/TencentCloud/TencentDB-Agent-Memory">TencentCloud/TencentDB-Agent-Memory</a> 将对话偏好、可复用 Skill、文档知识和代码图拆成不同资产，再按团队与角色受控分发。这样的分层能避免新 Agent 从零开始，也能降低把私有上下文无差别扩散给所有角色的风险。</p>
<h2 id="learning-inference-workflow">五、学习、推理与生成工作流</h2>
<p><a href="https://github.com/microsoft/AI-For-Beginners">microsoft/AI-For-Beginners</a> 把 AI 基础拆成课程和可运行实验；<a href="https://github.com/lyogavin/airllm">lyogavin/airllm</a> 通过分层加载降低大模型本地推理资源门槛；<a href="https://github.com/Comfy-Org/ComfyUI">Comfy-Org/ComfyUI</a> 用节点方式组织图像与视频生成步骤。这三类项目对应“学会原理、跑得起来、流程可复现”的连续链条。</p>
<h2 id="coding-and-reusable-knowledge">六、终端编码与可复用知识</h2>
<p><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a> 面向终端内的编码 Agent 与稳定的长时运行；<a href="https://github.com/virgiliojr94/book-to-skill">virgiliojr94/book-to-skill</a> 则把书籍与长文档转成 Agent 可逐章读取的知识包。前者缩短实现循环，后者降低重复查资料的上下文成本。</p>
<h2 id="voice-video-agents">七、实时交互 Agent 的组合方式</h2>
<p><a href="https://github.com/livekit/agents">livekit/agents</a> 面向语音和视频 Agent，连接语音识别、语言模型、语音合成与实时通信。真正的难点不只是接通组件，还包括延迟、打断处理、状态同步、错误恢复和用户隐私边界。</p>
<h2 id="google-skills">八、技能目录的价值在于边界清楚</h2>
<p><a href="https://github.com/google/skills">google/skills</a> 展示了面向产品与云服务的官方技能集合。相比零散提示词，明确的使用条件、参数、限制和示例更适合被 Agent 调用，也更便于团队审查版本变化。</p>
<h2 id="how-to-use-a-weekly-list">九、把榜单变成选型清单</h2>
<p>采用新项目时，先验证维护者、许可证、发布节奏、真实依赖和安全模型；然后用一个可回滚的小任务评估输出质量、成本和故障模式；最后才决定是否接入团队主流程。增长快可以说明需求强，但不能替代生产验证。</p>
'''

base.POSTS = [
    base.Post("ai-skills-agent-fullstack-open-source-daily-20260810", "8月10日 AI Skills/Agent 全栈开源项目速览：从技能标准到团队工作系统", "从 Skills、协作编排、记忆与沙箱，到模型网关和前端自动化，梳理 AI 开发工具栈正在形成的工程边界。", "AI工具", "AI Agent", ["AI Skills", "AI Agent", "开源项目", "Agent框架", "Claude Code", "Codex", "GitHub"], 15, BODY_A, ("#0b1020", "#075985", "#15803d"), ["Skills", "Agent", "记忆", "沙箱", "GitHub"], 2000),
    base.Post("github-ai-trending-weekly-20260803-09", "GitHub AI 趋势周榜：安全路由、PDF 解析与团队记忆为何集中爆发", "围绕一周新增 Star 的十个 AI 项目，拆解安全路由、文档分流、团队记忆、本地推理和实时 Agent 的工程价值。", "AI工具", "AI Agent", ["GitHub", "AI Agent", "AI Skills", "开源项目", "RAG", "Agent记忆"], 9, BODY_B, ("#111827", "#7c2d12", "#0f766e"), ["reverse-skill", "PDF", "记忆", "GitHub", "Agent"], 1300),
]
base.main()
