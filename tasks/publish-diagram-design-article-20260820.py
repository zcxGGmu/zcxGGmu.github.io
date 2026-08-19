from __future__ import annotations

import importlib.util
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
TEMPLATE = TASKS / "publish-ai-skills-two-source-20260819.py"
spec = importlib.util.spec_from_file_location("daily_20260819", TEMPLATE)
wrapper = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = wrapper
spec.loader.exec_module(wrapper)

template = wrapper.template

base = template.base
base.__file__ = __file__
base.DATE = "2026-08-20"
base.BASE_DT = datetime(2026, 8, 20, 6, 0, tzinfo=timezone(timedelta(hours=8)))
base.SCRIPT_NAME = Path(__file__).name
base.MANIFEST_NAME = "publish-diagram-design-article-20260820-changed-files.json"
base.PREV_EXISTING_URL = "/2026/housing-provident-fund-real-estate-financialization-wealth-transfer/"
base.PREV_EXISTING_TITLE = "住房公积金：房地产金融化、财富转移与普通人的资产选择"
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

BODY = r'''
<p>AI 生成架构图常见的问题，不是完全错误，而是“看起来像一张图，却不像可以交付的工程文档”：节点排列雷同，连线缺少方向，层级没有重点，颜色和字体也无法与团队已有的设计系统衔接。<a href="https://github.com/cathrynlavery/diagram-design" target="_blank" rel="noopener">cathrynlavery/diagram-design</a> 试图把这类视觉判断整理为可调用的规则，让 Claude Code、Codex 和 Pi 可以从自然语言需求出发，选择图表类型、组织信息并生成自包含的 HTML 与 SVG 文件。
</p>
<p>它的价值不在于替人决定系统结构，而在于把已经确认的事实转成清晰、可编辑、可复用的表达。图表仍然必须以真实模块、接口和数据关系为输入；如果输入关系写错，工具只会把错误排得更整齐。</p>

<h2 id="problem">一、它解决的是表达质量，而不是架构判断</h2>
<p>临时图通常从一组圆角框和几条连接线开始，信息密度一高就会出现交叉、拥挤和重点不明。工程文档需要同时服务于实现者、评审者和管理者：实现者关心接口与依赖，评审者关心边界与异常，管理者需要快速理解范围和风险。三类读者面对同一份原始信息，所需的细节层级并不相同。</p>
<p>Diagram Design 把这一步拆成三个判断：先识别要表达的关系，再选择适合的图表结构，最后控制节点数量、文字长度、留白和连线方向。它不要求使用者记住一长串模板名称，输入重点是目标、受众和关系。这样做能减少“先画图再想表达什么”的倒置。</p>

<h2 id="types">二、27 种图表类型对应不同的信息关系</h2>
<p>仓库围绕架构图、流程图、时序图、数据流图、甘特图、组织结构图、时间线和泳道图等类型提供规则。它们并非同一种画布换颜色，而是对应不同的问题：架构图说明组件边界，流程图说明决策路径，时序图说明调用先后，数据流图说明数据如何移动，甘特图说明任务与时间的约束。</p>
<p>选择类型时应先问“关系是什么”，再问“想要什么风格”。如果把带有时间顺序的系统交互硬套成静态架构图，视觉上可能整齐，语义却会丢失。工具负责缩短选择路径，工程师仍需对关系的准确性负责。</p>

<h2 id="layout">三、布局规则让图表更接近可交付文档</h2>
<p>可交付的图表需要稳定的视觉层级。普通元素使用克制的灰黑色，强调色只用于关键节点、异常路径或当前状态；连线尽量保持直观方向，避免无意义的阴影、发光边框和装饰图标。节点越多，越应该拆成总览与细节，而不是把几十个模块压进一张画布。</p>
<p>这类限制看似降低了“炫技空间”，实际是在保护阅读速度。一个评审者首先要找到入口、边界和关键依赖，然后才会深入局部实现。留白和分组不是装饰，而是把注意力顺序写进图里的结构。</p>

<h2 id="export">四、自包含 HTML 与 SVG 适合版本化和交接</h2>
<p>项目将样式与 SVG 放进同一个 HTML 文件，普通静态图不需要单独启动工程，双击即可打开。需要进入设计工具时可以导出 SVG，需要放入报告或演示稿时可以导出 PNG。相比只保存一张截图，自包含文件保留了文本、节点和样式，后续修改不会从零开始。</p>
<p>导出仍有环境条件：使用外部字体时首次加载可能需要联网，自动导出 PNG 需要准备 Playwright。团队应把这些依赖写进交接文档，并在 CI 或发布前检查文件是否能在目标环境打开。不能因为生成动作很快，就跳过实际渲染检查。</p>

<h2 id="redraw">五、重绘旧图时要保留关系并重新组织视觉</h2>
<p>已有 Mermaid 代码或 draw.io 文件可以作为结构输入。重绘的重点不是复制旧图的坐标和颜色，而是读取节点与关系后按新的受众、尺寸和细节级别重新排版。工程师版本可以保留接口、端口和实现细节，面向管理层的版本则应把信息压缩成边界、依赖和关键路径。</p>
<p>重绘完成后要检查变更记录：哪些内容保留，哪些被合并，哪些被省略，哪些关系的方向发生了变化。任何被简化的节点都应能回到原始结构，避免视觉优化掩盖语义丢失。</p>

<h2 id="branding">六、品牌样式应是显式配置，而不是隐式覆盖</h2>
<p>为不同客户或产品维护独立样式，可以让背景色、文字色、强调色和字体保持一致。工具可以从网站地址读取样式线索，也可以直接接受明确的色板和字体配置。更稳妥的做法是先列出准备修改的样式，再由负责人确认，避免一次自动化把多个项目的视觉规范混在一起。</p>
<p>品牌配置也需要版本管理。颜色、字号和字体变化都会影响可读性与打印效果，不能只保存最终图片而不保存配置来源。将样式文件和图表文件一起提交，后续才能复现相同的输出。</p>

<h2 id="animation">七、轻量动效可以解释顺序，但不替代专业视频工具</h2>
<p>对于流程和状态变化，Reveal.js 或 Loop 动效可以让节点按顺序出现，或让数据路径逐步高亮。这种动效适合解释先后关系、状态转换和依赖链，尤其适用于评审演示和内部培训。</p>
<p>它不等于完整的视频制作。复杂转场、镜头编排、旁白、配乐和长时间线仍应交给专门的视频工具。把图表工具的动效边界说清楚，能避免为了追求视觉效果而牺牲文件可维护性。</p>

<h2 id="input">八、输入事实必须先于排版</h2>
<p>图表生成器不会自动知道真实系统结构。模块名称、调用关系、数据方向、时间范围和异常分支都需要在输入阶段确认。最简单的质量门是先列一份结构化清单：节点、关系、方向、约束、受众和输出尺寸；清单通过审阅后，再交给工具排版。</p>
<p>如果图表用于架构评审或事故复盘，还应附上来源、版本和更新时间。图表是事实的表达层，不是事实本身。任何没有来源的箭头，都可能在交接中被误读成正式依赖。</p>

<h2 id="workflow">九、把图表能力接入工程工作流</h2>
<p>一个可复用的工作流可以分为五步：先收集模块和关系，接着确定读者和图表类型，然后生成 HTML/SVG，随后执行渲染与语义检查，最后把源文件和导出文件一起提交。渲染检查负责发现文字溢出、裁切、错位和字体缺失；语义检查负责确认节点、方向、单位和异常分支没有被改写。</p>
<p>在 CI 中可以加入最小验收：HTML 能被无头浏览器打开，SVG 是有效 XML，关键节点和标题存在，图片尺寸符合文档要求。对于面向外部客户的图表，再增加人工视觉复核，确认品牌色和表达层级没有偏离。</p>

<h2 id="security">十、工具权限应与图表任务保持最小范围</h2>
<p>Diagram Design 面向 Claude Code、Codex 和 Pi 的 Skill 形态，接入时不应因此获得整个代码库的默认写入权限。读取仓库结构、生成草稿和导出文件可以在隔离目录完成；修改正式架构文档、提交代码或调用外部服务则应保留预览和人工批准。</p>
<p>如果样式来自客户网站或内部系统，还要确认网络访问范围、缓存内容和凭据边界。图表生成通常是低风险任务，但它可能接触商业架构、客户品牌和内部接口，权限治理不能因为输出是一张图就被忽略。</p>

<h2 id="adoption">十一、适合从一张低风险图开始试用</h2>
<p>最初可以选择一个公开项目的应用架构图，要求工具输出总览图和一张局部细节图，再分别交给工程师和非技术读者阅读。记录生成耗时、人工修改次数、渲染失败类型、语义遗漏和最终文件大小，这些指标比单纯比较“好不好看”更能说明工具是否值得接入。</p>
<p>当输入清单、模板选择和渲染检查连续稳定后，再扩展到事故时间线、数据流图和客户品牌样式。每次扩展都要保留旧版本与回滚路径，避免把一次不成功的自动排版直接覆盖正式文档。</p>

<h2 id="conclusion">十二、图表自动化的边界是可解释、可编辑、可复核</h2>
<p>Diagram Design 的核心贡献，是把“画得像样”拆成一组可以复用的规则：类型选择、信息分组、节点控制、样式配置、导出格式和轻量动效。它让 Agent 具备更稳定的表达能力，却没有替工程师决定系统事实。</p>
<p>可靠的图表交付应能回答四个问题：输入关系来自哪里，为什么选择这种图表，哪些内容被保留或省略，导出的文件是否在目标环境中正确打开。把这四个问题写进工作流，AI 生成的图才会从临时演示变成可以进入设计评审、方案文档和团队交接的工程资产。</p>
'''

SLUG = "diagram-design-27-editorial-diagram-types-ai-visualization"
base.POSTS = [
    base.Post(
        slug=SLUG,
        title="Diagram Design：用 27 种专业图表规则把 AI 输出变成可交付文档",
        desc="拆解图表类型、布局约束、HTML/SVG 导出与工程验证。",
        category="AI工具",
        series="AI Agent",
        tags=["AI Skills", "AI Agent", "开源项目", "GitHub", "Diagram Design", "可视化", "工作流", "软件工程"],
        minutes=6,
        body=BODY,
        accent=("#111827", "#0f766e", "#d97706"),
        required=["Diagram Design", "图表", "HTML", "SVG", "渲染", "权限", "验证"],
        minimum=2800,
    )
]

template.EXPECTED_LINKS = {SLUG: {"https://github.com/cathrynlavery/diagram-design"}}
template.FORBIDDEN = ["B站", "bilibili", "Bilibili", "哔哩", "UP主", "up主", "原视频", "视频中", "视频里", "音频中", "音频里", "本期", "这期", "观看", "点赞", "投币", "收藏", "订阅", "关注", "三连", "BV1"]


def create_commit(outputs, ref):
    entries = []
    for path, content in sorted(outputs.items()):
        if content is None:
            if base.get_file(path) is not None:
                entries.append({"path": path, "mode": "100644", "type": "blob", "sha": None})
            continue
        blob = base.run_gh(["-X", "POST", base.endpoint("git/blobs"), "--input", "-"], {"content": content, "encoding": "utf-8"})
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    tree = base.run_gh(["-X", "POST", base.endpoint("git/trees"), "--input", "-"], {"base_tree": ref.tree_sha, "tree": entries})
    commit = base.run_gh(["-X", "POST", base.endpoint("git/commits"), "--input", "-"], {"message": "Publish Diagram Design AI Skills article 2026-08-20", "tree": tree["sha"], "parents": [ref.commit_sha]})
    base.run_gh(["-X", "PATCH", base.endpoint(f"git/refs/heads/{base.BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


template.create_commit = create_commit

if __name__ == "__main__":
    template.main()
