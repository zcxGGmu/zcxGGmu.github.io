from __future__ import annotations

import importlib.util
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
TEMPLATE = TASKS / "publish-ai-skills-two-source-20260818.py"
spec = importlib.util.spec_from_file_location("daily_20260818", TEMPLATE)
runner = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = runner
spec.loader.exec_module(runner)

base = runner.base
template = runner.template
base.__file__ = __file__
base.DATE = "2026-08-19"
base.BASE_DT = datetime(2026, 8, 19, 6, 0, tzinfo=timezone(timedelta(hours=8)))
base.SCRIPT_NAME = Path(__file__).name
base.MANIFEST_NAME = "publish-ai-skills-two-source-20260819-changed-files.json"
base.PREV_EXISTING_URL = "/2026/hermes-agent-memory-background-tasks-model-routing-local-os/"
base.PREV_EXISTING_TITLE = "Hermes Agent：23分钟浓缩百小时的实战经验"
base.PINNED_PREFIX = [
    "/ai-news-radar/",
    "/2026/codeinsights-local-first-agent-workbench/",
    "/2026/what-you-need-to-learn-from-claw-code-repo/",
    "/2026/gaojingqi-investment-system/",
    "/2026/ai-revolution-permanent-underclass-career-selection/",
    "/2026/live-longer-than-earn-fast-investment-infinite-game/",
    "/2026/original-accumulation-time-autonomy-ordinary-people/",
    "/2026/next-decade-wealth-leap-deflation-rmb-ai-cashflow/",
]

BODY_A = r'''
<p>AI 开源生态正在从“会不会写代码”转向“能不能稳定把事情做完”。最新一批项目覆盖运行时、任务编排、Skills、知识库、应用工具和治理安全等层次，背后共同的问题是：如何让 Agent 拥有明确的工作方法、足够的上下文、可恢复的状态和可审计的权限。把这些项目放在一条交付链上，比逐个追逐功能更容易看清它们的真实价值。</p>
<p>下面只讨论能够确认仓库归属的项目，并把项目放回具体工程边界中。热度可以帮助筛选候选，但不能替代许可证、维护活跃度、数据权限和失败恢复测试。</p>

<h2 id="runtime">一、运行时从可替换组件开始</h2>
<p><a href="https://github.com/deepseek-ai/deepseek-harness" target="_blank" rel="noopener">deepseek-ai/deepseek-harness</a> 把模型、工具、提示词、循环、存储、沙箱和界面拆成可替换模块。它的启发不是“换一个模型就够了”，而是把每次调用的契约、状态保存和错误恢复都变成可以单独测试的边界。长任务遇到超时或上下文切换时，系统应该知道从哪个检查点继续，而不是重新猜测整个过程。</p>
<p><a href="https://github.com/msitarzewski/agency-agents" target="_blank" rel="noopener">msitarzewski/agency-agents</a> 用不同职责的角色组织前端、后端、测试和研究工作；<a href="https://github.com/bytedance/deer-flow" target="_blank" rel="noopener">bytedance/deer-flow</a> 则把研究、编码和长流程放进可持续运行的工作台。角色越多，越需要明确输入、输出、所有权和完成条件，否则并行只是把冲突隐藏到最后。</p>

<h2 id="orchestration">二、并行协作必须有唯一所有者</h2>
<p><a href="https://github.com/HKUDS/nanobot" target="_blank" rel="noopener">HKUDS/nanobot</a> 代表轻量、本地化的助手形态，适合在资源受限的环境中执行边界清晰的任务。<a href="https://github.com/superset-sh/superset" target="_blank" rel="noopener">superset-sh/superset</a> 把多个编码 Agent 放到桌面调度台中；<a href="https://github.com/PrimeIntellect-ai/prime-agent" target="_blank" rel="noopener">PrimeIntellect-ai/prime-agent</a> 进一步强调后台任务、长期目标和经验积累。它们都说明并行的关键不是角色数量，而是每个工作区能否独立保存上下文并在完成后交回可核验结果。</p>
<p>数据库迁移、发布分支、依赖锁文件和外部写入必须设置唯一所有者。调度层应记录允许使用的工具、预算、输出格式和回滚方式；任何一个子任务失败，都不应静默地触发后续写操作。</p>

<h2 id="specification">三、先写规格，再让 Agent 执行</h2>
<p><a href="https://github.com/github/spec-kit" target="_blank" rel="noopener">github/spec-kit</a> 把需求、规格、计划和实现连接起来，适合把“想做一个功能”拆成可以验收的文档。规格的价值在于减少隐含假设：输入是什么、边界在哪里、成功如何定义、哪些动作需要批准。没有这些内容，Agent 很容易把局部正确误认为整体完成。</p>
<p><a href="https://github.com/paperclipai/paperclip" target="_blank" rel="noopener">paperclipai/paperclip</a> 则提供目标、任务、预算、审批和运行状态的控制面。项目管理界面不能替代工程责任，但能让负责人看到并行任务的真实成本和权限，及时停止偏离目标的执行。</p>

<h2 id="skills">四、Skills 是需要版本管理的工程依赖</h2>
<p><a href="https://github.com/obra/superpowers" target="_blank" rel="noopener">obra/superpowers</a> 将规划、实现、测试、审查和收尾整理成可调用的方法；<a href="https://github.com/affaan-m/ECC" target="_blank" rel="noopener">affaan-m/ECC</a> 把工程约束、记忆和质量实践组合成一套工作框架；<a href="https://github.com/mattpocock/skills" target="_blank" rel="noopener">mattpocock/skills</a> 展示了如何把日常工程经验写成可复用的步骤。它们都不应获得默认生产写入权限，升级时还应比较行为差异。</p>
<p><a href="https://github.com/anthropics/skills" target="_blank" rel="noopener">anthropics/skills</a>、<a href="https://github.com/addyosmani/agent-skills" target="_blank" rel="noopener">addyosmani/agent-skills</a> 和 <a href="https://github.com/trailofbits/skills" target="_blank" rel="noopener">trailofbits/skills</a> 分别代表官方能力、生产工程实践和安全审计方法。安装前应检查网络、文件、凭据和命令权限，先在隔离工作区试运行，再接入真实仓库。</p>

<h2 id="knowledge">五、知识输入必须保留来源</h2>
<p><a href="https://github.com/virgiliojr94/book-to-skill" target="_blank" rel="noopener">virgiliojr94/book-to-skill</a> 尝试把书籍内容整理为可以调用的工作知识，<a href="https://github.com/firecrawl/firecrawl" target="_blank" rel="noopener">firecrawl/firecrawl</a> 则把网页转换为结构化上下文。它们提升了输入效率，却不会自动保证事实正确。关键结论仍应回到原始页面、版本、页码或抓取时间，并处理许可和页面变化。</p>
<p><a href="https://github.com/TencentCloud/TencentDB-Agent-Memory" target="_blank" rel="noopener">TencentCloud/TencentDB-Agent-Memory</a> 适合把对话、文档、代码和经验沉淀为团队记忆；<a href="https://github.com/semantica-agi/semantica" target="_blank" rel="noopener">semantica-agi/semantica</a> 则强调资料、决定、证据和来源之间的关系。事实、偏好、任务状态和推测应采用不同的写入门槛与保留期，过期信息也要能被清理。</p>

<h2 id="local">六、本地执行扩大了能力边界，也扩大了风险</h2>
<p><a href="https://github.com/unslothai/unsloth" target="_blank" rel="noopener">unslothai/unsloth</a> 面向本地模型运行与训练，<a href="https://github.com/ToolJet/ToolJet" target="_blank" rel="noopener">ToolJet/ToolJet</a> 面向内部应用和工作流，<a href="https://github.com/cactus-compute/needle" target="_blank" rel="noopener">cactus-compute/needle</a> 则探索小模型在设备端完成工具调用和结构化提取。低延迟、离线和隐私是优势，但模型、数据、提示词、工具和日志仍需要权限与版本治理。</p>
<p>试点应先从只读任务和脱敏数据开始，比较质量、延迟、资源占用和异常回退。用结构化输出、范围限制和失败清单约束模型，比单纯追求吞吐更可靠。</p>

<h2 id="applications">七、应用层项目要接入质量门</h2>
<p><a href="https://github.com/langflow-ai/langflow" target="_blank" rel="noopener">langflow-ai/langflow</a> 让团队用可视化方式组合 AI 应用，适合快速验证流程，但正式交付仍需要固定输入输出、权限和回归样本。<a href="https://github.com/openai/codex" target="_blank" rel="noopener">openai/codex</a> 把代码阅读、编辑、命令执行和验证放进连续工作环境，真正的价值是让工程闭环更顺畅，而不是跳过测试与审查。</p>
<p>输入门检查资料许可、分支和任务范围；执行门限制网络、文件系统、账号和费用；输出门核对事实、测试、格式与未授权写入。三道质量门缺一不可。</p>

<h2 id="visualization">八、图表与界面是沟通层，不是事实来源</h2>
<p><a href="https://github.com/cathrynlavery/diagram-design" target="_blank" rel="noopener">cathrynlavery/diagram-design</a> 为架构图、流程图、时序图和数据图提供可生成的视觉类型。图表能缩短交接路径，但每张图仍应说明数据来源、口径和更新时间。漂亮的连线不能替代对异常分支和单位的检查。</p>
<p>UI 与自动化输出也应纳入验收：文本不能溢出，导出的 HTML、SVG 和文档要能在目标软件中打开，颜色和图例要表达真实关系。视觉交付完成后仍需要人工复核。</p>

<h2 id="governance">九、治理层决定系统能否规模化</h2>
<p>一套可运行的 Agent 系统至少要保留输入版本、工具调用、模型版本、耗时、成本、输出位置和人工决定。对高影响操作设置预览与二次批准，对网络和凭据采用最小权限，对每次记忆更新保留来源和回滚点。</p>
<p>“自我改进”应优先理解为工作说明、测试样本和经验记录的改进，而不是让模型无边界地改变自身。所有自动更新都应经过差异审阅，并能退回上一稳定版本。</p>

<h2 id="adoption">十、从一个低风险闭环开始采用</h2>
<p>最稳妥的顺序是：先用公开或脱敏资料完成只读整理，再接入可编辑草稿，最后评估受控写入。每一步记录成功率、人工修订时间、单次成本、失败类型和恢复耗时；连续稳定后再扩大并发量和权限。</p>
<p>运行时让任务可持续，Skills 让方法可复用，知识与记忆让上下文可追溯，应用工具把能力接进业务，治理与质量门则决定系统是否值得信任。项目数量不是成熟度指标，能够解释“准备做什么、依据什么做、实际做了什么、失败后如何恢复”，才是工程化的起点。</p>
'''

BODY_B = r'''
<p>长任务最容易在两个地方失效：上下文不断膨胀，或者终端关闭后状态消失。<a href="https://github.com/PrimeIntellect-ai/prime-agent" target="_blank" rel="noopener">PrimeIntellect-ai/prime-agent</a> 针对的正是这类问题：主 Agent 可以把复杂工作拆给多个子 Agent，让每个子任务保留自己的上下文，最后再把结构化结果交回主流程。</p>
<p>它更适合被理解为一个可持续运行的工作台，而不是另一个聊天窗口。真正值得评估的是任务拆分、后台恢复、长期目标、经验记录和权限边界能否形成闭环。</p>

<h2 id="delegation">一、把复杂任务拆成有边界的子任务</h2>
<p>以排查登录问题为例，主 Agent 可以让一个子 Agent 阅读认证代码，让另一个查找相关测试，再让第三个整理配置和错误日志。每个子 Agent 只接收完成任务所需的上下文，输出发现、证据、未解决问题和建议动作。主 Agent 不需要把所有文件重新塞进同一段对话。</p>
<p>拆分的边界必须可验证。子任务要有输入文件、允许工具、完成条件和超时策略；共享数据库、发布分支和凭据操作不能被多个子 Agent 同时拥有。并行提高的是信息覆盖和等待时间，不是免除所有权。</p>

<h2 id="rlm">二、RLM 的价值在于递归委派</h2>
<p>项目中的 RLM 思路可以理解为：主 Agent 在遇到上下文或步骤复杂度上升时，继续调用新的 Agent 处理局部问题，再把结果压缩回当前任务。这样既能保持主线，又能让专门任务使用更完整的局部材料。</p>
<p>压缩不是简单截断文本。返回结果应包含结论、证据位置、假设和风险；如果缺少证据，主 Agent 应保留待确认项，而不是把推测合并成确定事实。</p>

<h2 id="background">三、后台会话让长任务跨越终端生命周期</h2>
<p>关闭终端不应等于任务消失。后台进程需要保存任务目标、检查点、子任务状态和日志，并允许重新打开后查看仍在运行的工作。恢复时应先展示当前状态和即将执行的动作，再继续写入文件或调用外部服务。</p>
<p>稳定性验证至少包含三组样本：中断后从正确检查点恢复、一个子任务失败时阻止后续写入、重复恢复时不重复创建副作用。没有幂等和停止开关，后台运行只会让问题更晚暴露。</p>

<h2 id="goals">四、目标与定时检查形成可观察的闭环</h2>
<p>复杂任务往往不是“执行一次命令”，而是修复问题、运行完整测试、等待部署、再次检查结果。目标和定时检查可以把这些步骤保留在同一个任务中，减少每次重新解释前因后果的成本。</p>
<p>定时器本身不能证明部署成功。每个检查点都要定义可测信号，例如测试退出码、构建状态、健康检查和生成文件哈希；信号缺失时应该转入人工确认，而不是继续推进。</p>

<h2 id="continual">五、Continual Harness 改的是经验记录</h2>
<p>任务结束后回看哪些方法有效、哪些目录不能修改、哪条测试应优先执行，可以形成补充说明、记忆或工作模板。这里的“自我改进”不是重新训练模型，而是改进下一次任务会读取的工作材料。</p>
<p>经验更新必须留下差异、来源和适用范围。错误的经验比没有经验更危险，因此每次更新都应经过审阅，并且能退回前一个版本。对于不同仓库和不同团队，经验不能未经筛选直接共享。</p>

<h2 id="skills">六、Python Skills 把工具能力接进任务</h2>
<p>除了普通说明文件，Prime Agent 还支持带 Python 功能的 Skills，用来处理搜索、数据整理和固定流程。已有的 Codex 或 Claude Code 工作规则可以在确认工具契约后复用，但命令、环境变量和权限边界必须重新核对。</p>
<p>Skills 的验收不应只看“能不能调用”。还要测试空值、网络失败、权限不足、重复请求和异常输出，并确认失败时不会留下半完成状态。对外发送、数据库写入和生产部署仍需要单独批准。</p>

<h2 id="architecture">七、底座与产品化能力应分开评估</h2>
<p>项目的基础 Agent 能力提供模型调用、工具执行和会话循环，Prime Agent 在此之上增加子 Agent、后台任务、长期目标和经验积累。评估时应分别看底座的可扩展性和产品层的可观察性，避免把界面功能误认为运行时可靠性。</p>
<p>模型、API 和本地服务可以按团队环境接入，但每种认证方式都要记录费用、配额和数据流向。第三方工具调用可能产生额外用量，不能默认包含在普通套餐额度中。</p>

<h2 id="security">八、权限边界比自动化速度更重要</h2>
<p>Prime Agent 会以当前电脑账户权限运行生成的 Python 和项目命令，因此它不是安全沙箱。首次试用应使用临时项目、独立工作副本和最小权限账号，确认文件改动、网络访问和命令调用后，再接入重要代码。</p>
<p>后台任务尤其需要停止按钮、日志和资源上限。对凭据、生产目录、发布分支和不可逆操作设置人工闸门，才能避免“任务还在运行”被误解为“任务可以自由行动”。</p>

<h2 id="evaluation">九、用真实小样本验证长期运行</h2>
<p>建议用三类任务验收：需要多个领域判断的研究任务、需要多轮测试的代码修复、需要等待外部状态的部署检查。记录拆分后的总耗时、上下文节省、人工接管次数、恢复成功率和失败回滚时间。</p>
<p>如果子 Agent 只是增加协调成本，或者经验更新没有提高下一次成功率，就应减少并发与自动化范围。长期运行的价值必须由可重复指标证明。</p>

<h2 id="conclusion">十、长任务系统的核心是可恢复、可审计、可停止</h2>
<p>Prime Agent 展示了一条清晰路径：主 Agent 负责目标与合并，子 Agent 负责局部调查，后台会话负责跨越终端生命周期，目标检查负责等待与复核，经验记录负责下一次复用。任何一个环节都不能脱离权限、日志和回滚。</p>
<p>真正可靠的长期任务不是让系统永远运行，而是让它在每个检查点都能回答：现在完成了什么、依据是什么、下一步会改变什么、失败后如何停下。把这些答案写进工作流，Agent 才能从一次性演示变成可治理的工程能力。</p>
'''

SLUG_A = "ai-skills-agent-fullstack-open-source-daily-20260818"
SLUG_B = "prime-agent-long-running-multi-agent-workflow-analysis"
base.POSTS = [
    base.Post(
        slug=SLUG_A,
        title="8月18日 AI Skills/Agent 全栈开源项目速览：从插件生态到可治理工作系统",
        desc="围绕运行时、任务编排、Skills、知识库、本地模型和治理安全，梳理 AI Agent 如何从会写代码走向稳定完成工作。",
        category="AI工具", series="AI Agent",
        tags=["AI Skills", "AI Agent", "开源项目", "GitHub", "Agent框架", "工作流", "AI治理", "软件工程"],
        minutes=15, body=BODY_A, accent=("#0f172a", "#0f766e", "#b45309"),
        required=["运行时", "Skills", "知识", "治理", "验证", "权限"], minimum=2500,
    ),
    base.Post(
        slug=SLUG_B,
        title="Prime Agent 深度拆解：多 Agent 分工、后台续跑与经验回滚",
        desc="从任务拆分、RLM、后台会话、定时检查到 Continual Harness，分析长任务 Agent 的可恢复性与安全边界。",
        category="AI工具", series="AI Agent",
        tags=["AI Agent", "Prime Agent", "开源项目", "GitHub", "多Agent", "工作流", "自动化", "安全治理"],
        minutes=10, body=BODY_B, accent=("#111827", "#2563eb", "#047857"),
        required=["Prime Agent", "子 Agent", "后台", "经验", "权限", "回滚"], minimum=2100,
    ),
]

template.EXPECTED_LINKS = {
    SLUG_A: {
        "https://github.com/deepseek-ai/deepseek-harness", "https://github.com/msitarzewski/agency-agents",
        "https://github.com/bytedance/deer-flow", "https://github.com/HKUDS/nanobot",
        "https://github.com/superset-sh/superset", "https://github.com/PrimeIntellect-ai/prime-agent",
        "https://github.com/github/spec-kit", "https://github.com/paperclipai/paperclip",
        "https://github.com/obra/superpowers", "https://github.com/affaan-m/ECC",
        "https://github.com/mattpocock/skills", "https://github.com/anthropics/skills",
        "https://github.com/addyosmani/agent-skills", "https://github.com/trailofbits/skills",
        "https://github.com/virgiliojr94/book-to-skill", "https://github.com/firecrawl/firecrawl",
        "https://github.com/TencentCloud/TencentDB-Agent-Memory", "https://github.com/semantica-agi/semantica",
        "https://github.com/unslothai/unsloth", "https://github.com/ToolJet/ToolJet",
        "https://github.com/cactus-compute/needle", "https://github.com/langflow-ai/langflow",
        "https://github.com/openai/codex", "https://github.com/cathrynlavery/diagram-design",
    },
    SLUG_B: {"https://github.com/PrimeIntellect-ai/prime-agent"},
}
template.FORBIDDEN = ["B站", "bilibili", "Bilibili", "哔哩", "UP主", "up主", "原视频", "视频中", "视频里", "音频中", "音频里", "本期", "这期", "观看", "点赞", "投币", "收藏", "订阅", "关注", "三连", "BV1"]

if __name__ == "__main__":
    template.main()
