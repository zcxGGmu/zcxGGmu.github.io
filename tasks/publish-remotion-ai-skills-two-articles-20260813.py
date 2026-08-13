from __future__ import annotations

import base64
import importlib.util
import json
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
BASE_SCRIPT = TASKS / "publish-three-life-business-articles-20260809.py"

spec = importlib.util.spec_from_file_location("publish_base", BASE_SCRIPT)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = base
spec.loader.exec_module(base)

_base_run_gh = base.run_gh


def run_gh_with_stream_retry(args: list[str], payload: dict | None = None):
    for attempt in range(5):
        try:
            return _base_run_gh(args, payload)
        except RuntimeError as exc:
            msg = str(exc).lower()
            if attempt < 4 and any(token in msg for token in ["stream error", "cancel", "connection", "reset", "timeout", "temporarily"]):
                time.sleep(2 + attempt * 3)
                continue
            raise


base.run_gh = run_gh_with_stream_retry

base.__file__ = __file__
base.DATE = "2026-08-13"
base.BASE_DT = datetime(2026, 8, 13, 21, 5, 0, tzinfo=timezone(timedelta(hours=8)))
base.PREV_EXISTING_URL = "/2026/memory-capex-hbm-dram-shortage-nand-balance-2027/"
base.PREV_EXISTING_TITLE = "海外存储扩产不改紧平衡：HBM 挤占、DRAM 缺口与 NAND 分化"
base.SCRIPT_NAME = Path(__file__).name
base.MANIFEST_NAME = "publish-remotion-ai-skills-two-articles-20260813-changed-files.json"


BODY_REMOTION = r'''
<p>用代码完成一支 Vox 风格的动效短片，关键不在于让 AI 随机生成几个漂亮画面，而在于先锁定视觉系统，再把每个场景拆成可复用、可微调、可同步声音的工程组件。<a href="https://github.com/remotion-dev/remotion" target="_blank" rel="noopener">Remotion</a> 负责把 React 组件变成时间轴和渲染结果，<a href="https://github.com/anthropics/claude-code" target="_blank" rel="noopener">Claude Code</a> 负责搭项目、写场景、修错误、加控制项和组装主序列。整个流程更像在搭一套动态图形生产线，而不是打开剪辑软件逐帧操作。</p>
<p>这类工作流的核心，是把“视觉设计”提前变成结构。统一背景、统一字体、统一强调色、统一纸质肌理和统一入场节奏，会让多个场景看起来像一个连续镜头。每个场景只改变中景和前景元素，背景保持稳定，就能形成 Vox 常见的解释型动效：画面不是被硬切成一段段素材，而是人物、图表、地图和标注在同一个视觉空间里依次弹出。</p>

<h2 id="lock-the-visual-system">一、先锁视觉系统，而不是先写动画</h2>
<p>真正要先做的不是新建项目，而是锁定一套视觉系统。背景应该在所有场景中保持一致，字体、强调色和整体调性也要一致。变化发生在中景和前景：人物抠图、建筑、船只、地图、曲线图、数字标注和手绘线条按叙事需要进入画面。</p>
<p>这种分层方式能减少随机感。AI 生成动效时最容易出现的问题，是每个场景都像来自不同模板：颜色变了，构图变了，字体也变了。统一视觉系统相当于先给 AI 一条轨道，让它在轨道内做变化。</p>
<p>Vox 风格的精髓并不是某一个具体滤镜，而是解释型信息图的秩序感：静态底图提供稳定空间，黑白半调人物提供纸媒质感，红色或高饱和标注提供强调，图表和地图负责把事实转成可视化证据。</p>
<p>开工前还要把画幅、帧率、总时长和语气定下来。以 1080p 横屏为例，最好先决定所有元素都在 16:9 安全区里工作，标题和数字不要贴边，人物不要挡住主要图表。帧率通常保持项目默认即可，真正影响体验的是节奏：每个元素弹出要有间隔，解释数字时画面要停得住，转场不能抢旁白。</p>
<p>脚本也要先拆成镜头清单。每一句旁白对应什么画面、需要哪些元素、哪个数字要被强调、是否需要地图或图表，都可以提前写成表格。Claude Code 接到的任务越像“分镜执行单”，生成出来的 Remotion 代码越稳定。反过来，如果只说“做一个 Vox 风格短片”，结果往往会停留在表面样式，缺少叙事节奏。</p>

<h2 id="connect-assets-through-mcp">二、把素材工具接进 Claude Code</h2>
<p>在正式搭 Remotion 项目前，先把素材生成和处理工具接到 Claude Code 的连接器里。通过设置里的 Connectors 和自定义 MCP 服务，可以把 Magnific、Higgsfield 这类图像或影像工具接入工作流。这样需要抠图、贴图或生成素材时，不必反复离开编辑环境手工下载再拖回项目。</p>
<p>MCP 连接器的意义在于让 Claude Code 直接调用外部服务。比如需要某个人物的透明背景图，需要把人物转成黑白半调风格，或者需要一段去背景的海面素材，都可以通过自然语言指令让它准备并放进对应文件夹。</p>
<p>这一步决定了后面是否顺。动效项目不是只有代码，素材命名、目录位置、透明通道、图片尺寸和风格一致性都会影响最终结果。把素材生产接进同一条工作流，后续场景搭建才不会被文件管理打断。</p>
<p>素材进入项目时要顺手建立命名规则。人物可以用 people/trump-cutout.png 这类可读名称，建筑、交通工具、地图、海面素材和纹理各放一类。Claude Code 处理文件时非常依赖明确路径，路径越清楚，后续指令越短。比如“把 scene-oil 里的 tanker 调大一点”比“把那艘船调大一点”稳定得多。</p>

<h2 id="scene-folder-architecture">三、每个场景一个文件夹，共用背景</h2>
<p>项目结构要尽量清楚：每个场景放在独立文件夹里，共享背景单独存放，每个场景再放自己的抠图、图表、地图、标注和辅助素材。场景一可以是白宫、人物和红色标注；场景二可以是油轮、海面、价格数字；场景三可以是债务或通胀曲线、美国地图和转场元素。</p>
<p>这样的结构让 Claude Code 更容易理解任务。它知道 scene one 里有哪些素材，scene two 里有哪些素材，也知道哪些是共享资源。后续要求它修改某个场景时，不会把全局背景和局部素材混在一起。</p>
<p>每个场景最好有自己的组件文件。场景内部再分三层：背景层、中景层、前景层。背景层稳定不动，中景层常用于半调人物或纸质纹理，前景层放建筑、船只、地图、曲线和数字。只要层次稳定，动画就更容易用统一语言描述。</p>
<p>共享背景不一定只是一张图片，也可以是一个 Background 组件。组件里放纸张底色、细颗粒纹理、轻微网点、统一边框和全局光影。这样场景切换时仍然是同一个世界，只是前景发生变化。后续如果想把背景颜色从浅灰改成米白，或者把颗粒强度调低，只需要改一个组件。</p>
<p>组件拆分可以按“能否复用”来判断。背景、纸质噪声、红色描边、弹出容器、数字标签、折线图和地图标注都适合抽成通用组件；某个场景专用的人物组合、建筑位置和故事元素则留在场景组件里。这样既不会过度抽象，也能让下一次制作复用真正稳定的部分。</p>

<h2 id="halftone-cutouts">四、人物抠图要做成黑白半调纸质感</h2>
<p>Vox 风格中最容易识别的质感，是类似杂志剪贴的黑白半调人物。做法不是手工在设计软件里一点点调，而是准备透明背景人物图后，直接让 Claude Code 把指定文件夹中的人物改成黑白、添加 halftone pattern，并保持透明背景和边缘干净。</p>
<p>人物可以是政治人物、企业人物或任何叙事主体。关键不是人物是谁，而是所有人物都要进入同一种视觉语言：黑白、半调、纸张纹理、轻微颗粒感，再配上红色偏移描边或 marker stroke。这样画面会有纸媒拼贴感，而不是纯数字图片的塑料感。</p>
<p>半调风格还有一个好处：它能降低素材来源差异。不同图片的光线、清晰度和色彩往往不一致，统一转为黑白半调后，差异会被压平，画面整体更像来自同一个编辑系统。</p>
<p>处理人物时要检查三件事：透明背景是否真的透明，边缘是否有白边，黑白半调是否压掉了面部识别度。若边缘有脏边，可以让 Claude Code 重新处理 alpha；若半调太重，就降低点阵密度或对比度。风格化不是把细节毁掉，而是让细节服从统一视觉。</p>

<h2 id="animate-with-intent">五、用自然语言描述动画意图</h2>
<p>Remotion 底层可以使用 spring 和 interpolate 等函数完成弹出、缓动、位移和透明度变化，但不需要先记住函数名。更有效的方式，是用自然语言描述动画意图：白宫先弹出，然后人物依次出现，不要同时移动；每个元素后面加红色偏移描边；图表线条随后出现，数字最后强调。</p>
<p>Claude Code 会把这种意图翻译成 Remotion 组件逻辑。spring 负责弹出和回弹感，interpolate 负责位置、透明度和尺度变化，stagger 负责错峰入场。对创作者来说，重点是说清楚顺序、层级、节奏和强调点，而不是手写每一帧。</p>
<p>“带意图的动画”比“随便动起来”重要得多。解释型动效必须服务叙事：谁先出现，谁后出现，哪个数字被强调，哪个地图只是背景信息，都应该由内容逻辑决定。</p>
<p>提示词可以直接写成镜头调度：“背景保持不动；建筑从 92% 放大到 100%；人物从画面下方弹入，带一点 overshoot；红色数字延迟 12 帧出现；最后用横向 marker stroke 圈出重点。”这种描述同时包含动作、方向、时间差和强调对象，Claude Code 更容易生成可控动画。</p>

<h2 id="use-remotion-studio-for-fine-tuning">六、用 Remotion Studio 做最后微调</h2>
<p>AI 能搭出场景，但第一次结果通常不会刚好到位。Remotion Studio 的价值在这里体现出来：打开预览后，如果报错，就直接让 Claude Code 修；如果元素位置不舒服，就要求它给每个元素暴露 prop controls。</p>
<p>有了 prop controls，人物、建筑和图表的 scale、x、y 等参数可以直接在 Studio 里调整。比如白宫可以先从 1.5 放到 1.8，人物可以调大到 1.4，再微调 X/Y 位置。每次改完要保存数值，让下一次预览保持一致。</p>
<p>这个环节是人类审美和 AI 执行的交界处。AI 负责把控制项做出来，人负责判断构图是否稳、人物是否太小、建筑是否压住主体、红色标注是否抢戏。最后的质感，往往就来自这些微小参数。</p>
<p>调参顺序也很重要。先调主体大小，再调位置，最后调动画节奏。不要一边改图表、一边改人物、一边改转场，否则很难判断问题来自哪里。每完成一个场景，就把控制项整理成默认值，避免下一次重新打开 Studio 时又回到临时状态。</p>

<h2 id="build-scenes-as-independent-modules">七、场景要独立，再统一组装</h2>
<p>每个场景都应该先单独完成。白宫场景完成后，再做油轮场景；油轮场景可以使用去背景的海面动态素材，让油轮、海浪和油价数字依次出现；债务或通胀场景可以让美国地图、折线图和转场元素顺序进入。</p>
<p>独立场景的好处，是问题容易定位。某一段构图不好，只改对应组件；某一个图表节奏不对，只调对应场景的 spring 或 interpolate；某一个素材边缘不好，只替换该场景文件夹里的素材。</p>
<p>当所有场景都完成后，再让 Claude Code 创建 master sequence，把场景按叙事顺序串起来。每个场景播放多久，不应凭感觉，而应根据旁白的段落长度来定。这样画面和声音才能同步推进。</p>
<p>主序列可以先按段落粗切，再按句子细调。粗切负责保证每个场景覆盖对应叙述，细调负责让关键画面落在关键词附近。比如谈到油价时油轮和价格数字必须已经出现，谈到债务或通胀时折线图不能还在入场，否则画面会滞后于信息。</p>

<h2 id="sync-voiceover-and-music">八、旁白、音乐和音效决定完成度</h2>
<p>旁白可以单独用 ElevenLabs 生成，例如选择更偏纪录片感的英式叙述声音。生成后把音频放回项目目录，再让 Claude Code 将它嵌入 composition，并按旁白切分每个场景的起止时间。</p>
<p>声音同步的提示词要具体：每个场景从自己的叙述段落开始，在对应叙述结束时收尾，场景之间连续播放，不要让画面提前太多或滞后太多。需要更精细时，再加入背景音乐、环境音和轻微 whoosh 类转场音效。</p>
<p>Remotion Studio 里拖动预览时，音频有时会听起来断续或卡顿，这通常只是预览环境的问题。最终渲染后，声音会更干净。若想后期再混音，也可以只导出画面 composition，再进入专业剪辑软件处理声音。</p>

<h2 id="render-final-mp4">九、最后渲染成 1080p 成片</h2>
<p>当场景、旁白、音乐和节奏都稳定后，直接让 Claude Code 调用 Remotion 渲染 1080p MP4。更完整的提示可以写成：把整个 composition 渲染为 1080p MP4，并混入旁白和音乐，确保场景按主序列顺序播放。</p>
<p>这一步体现出代码化动效的优势。所有场景都是 React 组件，所有参数都能版本化，所有素材都在文件夹中可追踪。修改不再是“重新剪一遍”，而是改组件、调参数、重渲染。</p>
<p>如果要做系列内容，还可以把这套结构变成模板：固定背景系统、固定半调人物处理、固定图表组件、固定转场方式、固定旁白同步脚本。下一支短片只需要替换脚本、素材和数据。</p>
<p>渲染前建议做一次 checklist：所有素材路径是否存在，透明图是否缺失，时间轴有没有空白段，音量有没有爆掉，字幕或标题是否出安全区，图表数字是否和脚本一致，最终文件是否带上旁白和音乐。Remotion 的工程化能力很强，但前提是最后也按工程方式验收。</p>
<p>如果最终文件用于公开发布，还要额外检查压缩质量和首尾节奏。开头几秒需要迅速建立主题，结尾不要突然断掉；音乐应该给旁白让位，音效只负责增强入场和转场，不要持续干扰信息。动效短片的专业感，往往来自这种“每个细节都没有出戏”的收尾检查。</p>
<p>这一套方法最适合解释型内容、商业案例、宏观故事、产品发布和教育课程。只要内容需要用人物、地图、数字和图表讲清楚，Remotion 的代码化时间轴就能把一次制作经验沉淀成长期模板，也能让修改、复用和批量生产变得更可控。</p>

<h2 id="workflow-lessons">十、真正的价值是把动效制作变成工程流程</h2>
<p>这套流程的价值，不是证明传统工具不重要，而是把原本依赖时间轴和手工操作的动态图形，拆成了可复用工程流程。脚本决定叙事，视觉系统决定统一感，场景文件夹决定可维护性，Remotion 组件决定可渲染性，Claude Code 负责把自然语言意图翻译为代码实现。</p>
<p>更稳的实践顺序是：先写脚本和镜头清单，再锁视觉系统；先搭目录和共享背景，再生成素材；先单独完成每个场景，再组装主序列；先同步旁白，再加音乐和音效；最后渲染成片并回看节奏。</p>
<p>AI 可以让动效生产速度大幅提高，但专业感仍然来自结构和审美判断。提示词越具体，文件越有组织，场景越模块化，人类越愿意在 Remotion Studio 里微调参数，最终结果越接近真正的商业级解释型动效。</p>
'''


BODY_AI_SKILLS = r'''
<p>AI 开源工具的主线已经从“哪个模型更会聊天”转向“怎样让 AI 真正动手工作”。最近一批高热项目集中在几个方向：长期记忆、自我改进、技能市场、代码地图、云端电脑、网页理解、多模型路由、内容生产、终端编码和 UI 设计约束。它们共同说明，AI 工具正在从对话入口变成一套能规划、执行、复盘、审查和交付的工作系统。</p>
<p>这份速览可以按七层来理解：第一层是热门 Agent 项目，负责让 AI 从聊天走向任务执行；第二层是 Skills 生态，把专家经验打包成可安装能力；第三层是 Agent 框架，解决多角色和长期运行；第四层是执行工具，把搜索、云端电脑、浏览器和网页数据接进来；第五层是效率应用，把文档、社媒、研究、知识库和内容生产自动化；第六层是 Codex 生态，把终端编码、审查和插件扩展串起来；第七层是 UI/UX 设计系统，专门修复 AI 生成界面的审美和一致性问题。</p>

<h2 id="hot-projects">一、热门项目：让 AI 从聊天变成会干活</h2>
<p><strong><a href="https://github.com/NousResearch/hermes-agent" target="_blank" rel="noopener">NousResearch/hermes-agent</a></strong> 的定位，是一个会长期成长的 AI 助手框架。它不仅能完成任务，还会把任务过程中的经验沉淀下来，下次遇到类似工作时直接复用。长期记忆、工具调用、安全沙箱、本地与云端运行、多模态输入，共同构成了它的核心价值。对长期使用 AI 办公或开发的人来说，真正重要的是越用越懂需求，而不是每次都重新交代上下文。</p>
<p><strong><a href="https://github.com/anthropics/skills" target="_blank" rel="noopener">anthropics/skills</a></strong> 则把 Skills 变成官方标准库。它像一个 AI 编程技能商店：前端、测试、代码审查、项目脚手架、文档处理等能力，都可以通过技能包的方式安装。Skills 的价值在于不用从零教 AI 怎么做某类工作，而是让它直接加载一套经过审查的专业做法。</p>
<p><strong><a href="https://github.com/contains-studio/agents" target="_blank" rel="noopener">contains-studio/agents</a></strong> 代表专业角色库方向。通用 AI 什么都懂一点，但写后端、做运维、看安全、搭前端时，需要的思维方式并不一样。角色库的价值，就是把 AI 切换到资深后端、DevOps、全栈工程师、测试工程师等专业人格，让同一个工具在不同任务里有不同工作习惯。</p>
<p><strong><a href="https://github.com/Graphify-Labs/graphify" target="_blank" rel="noopener">Graphify-Labs/graphify</a></strong> 解决大代码库理解问题。项目一大，AI 直接读文件会消耗大量 token，还容易丢上下文。Graphify 把模块、函数、调用关系和依赖整理成知识图谱，让 AI 先看代码地图，再决定读哪些文件。对新人接手陌生项目、团队做架构梳理、Agent 分析代码影响面都很有价值。</p>
<p><strong><a href="https://github.com/runaki-ai/ponytail-gain" target="_blank" rel="noopener">runaki-ai/ponytail-gain</a></strong> 对应的是“少写不必要代码”的工程品味。AI 写代码容易堆复杂度，明明三行能解决的问题，常常扩成一大段抽象。把资深工程师的克制原则写进工作流，可以减少 token、降低维护成本，也减少未来出 bug 的概率。</p>
<p><strong><a href="https://github.com/addyosmani/agent-skills" target="_blank" rel="noopener">addyosmani/agent-skills</a></strong> 来自长期工程实践，尤其适合前端和全栈开发者。它把代码审查、性能优化、项目脚手架、工程规范等内容整理成可调用技能。真正值得学习的不是某条提示词，而是一个成熟工程师怎样把 AI 纳入生产流程。</p>
<p>这一组项目给出的共同信号很明确：AI 编程不再只是“帮我写代码”，而是让 AI 拥有记忆、角色、知识地图、工程纪律和稳定执行环境。</p>

<h2 id="workflow-and-learning">二、工作管理与学习路径：从混乱工具到有章法流程</h2>
<p>AI 工具变多之后，新的问题是任务分散、进度分散、结果也分散。PaperClip 这类工作管理平台试图把多个智能体任务放到一个面板里，统一分配、追踪和汇总结果。它面向的不是单个提示词，而是产品经理、项目经理和创业团队每天要处理的一堆自动化任务。</p>
<p><strong><a href="https://github.com/shanraisshan/claude-code-best-practice" target="_blank" rel="noopener">shanraisshan/claude-code-best-practice</a></strong> 则更像 Claude Code 工程实践手册。复杂项目不能让 AI 随便写，必须先拆任务、给规则、设置检查点、处理跑偏。它的价值是把“手忙脚乱地让 AI 改代码”，推进到“有流程、有边界、有验收地使用 Agent”。</p>
<p><strong><a href="https://github.com/microsoft/AI-For-Beginners" target="_blank" rel="noopener">microsoft/AI-For-Beginners</a></strong> 提供 12 周、24 课时左右的系统学习路径，从基础概念到实战代码逐步推进。工具每天都在变，但基础概念、实验能力和评估意识不会过时。对零基础学生、转行开发者和企业培训来说，系统课程仍然是最稳的入口。</p>
<p>AI 驱动的敏捷方法论也开始出现。它讨论的不是某个工具，而是团队怎样在需求、拆分、实现、测试、审查和交付中安排 AI 的位置。AI 会写代码之后，管理问题反而更重要：什么时候让 AI 做初稿，什么时候必须人工确认，什么时候交给测试和审查，什么时候停止自动化。</p>
<p>这类流程工具真正要解决的是“任务可见性”。一个 Agent 做了什么、卡在哪里、用了哪些文件、跑过哪些验证、输出是否能追溯，都必须在团队层面看得见。否则 AI 自动化越多，项目管理反而越混乱。能把任务状态、证据和交付物统一呈现的工具，会比单纯的聊天界面更接近企业刚需。</p>

<h2 id="skills-ecosystem">三、Skills 生态：把专家经验变成可安装能力</h2>
<p><strong><a href="https://github.com/obra/superpowers" target="_blank" rel="noopener">obra/superpowers</a></strong> 是 Skills 生态里非常关键的项目。它把规划、实现、验证、审查、调试等经验写成结构化技能，让 AI 在任务开始前就加载正确的方法。跨平台、不锁厂商、强调生产环境验证，是它最重要的特点。</p>
<p><strong><a href="https://github.com/mattpocock/skills" target="_blank" rel="noopener">mattpocock/skills</a></strong> 展示了 TypeScript 专家怎样使用 AI。它强调实用边界、触发条件和工程纪律，而不是把 AI 当玩具。一个技能什么时候该用、什么时候不该用、会带来什么约束，都要写清楚。</p>
<p><strong><a href="https://github.com/zhaoxuya520/reverse-skill" target="_blank" rel="noopener">zhaoxuya520/reverse-skill</a></strong> 面向授权安全研究和渗透测试。它让 AI 根据任务类型自动选择工具链、沉淀经验知识库，并在合法边界内完成漏洞扫描、分析和报告。安全技能尤其需要边界清楚，所有操作都必须建立在授权和审计之上。</p>
<p><strong><a href="https://github.com/cisco-ai-defense/skill-scanner" target="_blank" rel="noopener">cisco-ai-defense/skill-scanner</a></strong> 代表技能安装前的安全审查。技能市场越大，供应链风险越高。安装前检查恶意代码、后门、异常权限和可疑行为，会成为企业使用 Skills 的基本步骤。</p>
<p><strong><a href="https://github.com/claw-opus/proactive-self-improving-agent" target="_blank" rel="noopener">claw-opus/proactive-self-improving-agent</a></strong> 和 <strong><a href="https://github.com/lanyasheng/self-improving-agent" target="_blank" rel="noopener">lanyasheng/self-improving-agent</a></strong> 则把自我改进写成技能：每次任务后自动复盘，把错误、修正和偏好保存下来，下次直接调用。重度 AI 用户真正需要的不是一次性输出，而是一个能持续变熟的助手。</p>
<p>Skills 的另一层意义，是让团队规范可以被机器执行。过去规范通常写在文档里，开发者未必会读，AI 更不会自动遵守。把规范做成技能后，触发条件、禁止事项、验证命令、交付格式都可以在任务开始时加载。它不是提示词摘录，而是把团队经验变成运行时约束。</p>
<p>技能市场后续会像软件包管理一样分层：个人技能解决个人偏好，团队技能固化内部流程，安全技能检查外部依赖，领域技能沉淀行业知识。真正难的不是写一个 skill 文件，而是让它在正确时机触发，并且不会和用户当前指令冲突。</p>

<h2 id="agent-frameworks">四、Agent 框架：从单个助手到一组智能体协作</h2>
<p>Skills 是单项能力，Agent 框架则是能持续运行、会规划任务的底层骨架。Pi 一类 Agent 工具箱的思路，是把统一 LLM API、智能体循环、终端界面和命令行编码助手合在一起，减少开发者在多个工具之间来回切换。统一接口尤其重要：换底层模型时，最好只改配置，不改业务代码。</p>
<p>Orta 这类“舰队指挥官”式工具强调并行调度。很多任务可以拆开同时做：一个 Agent 查资料，一个 Agent 写代码，一个 Agent 做测试，一个 Agent 做总结。单个 AI 一次只做一件事，效率容易卡住；多 Agent 的价值，是把任务拆清楚后同时推进。</p>
<p><strong><a href="https://github.com/Panniantong/Agent-Reach" target="_blank" rel="noopener">Panniantong/Agent-Reach</a></strong> 给 Agent 补上跨平台搜索能力。内容创作、市场调研和舆情分析都需要跨多个社区、搜索引擎和内容平台搜集信息。一个命令汇总多平台结果，比手动逐个打开平台效率高得多。它的重点是覆盖广、成本低，对中文内容场景也更友好。</p>
<p><strong><a href="https://github.com/cloudflare/computer" target="_blank" rel="noopener">cloudflare/computer</a></strong> 则给 Agent 配了一台云端电脑。AI 可以在这个环境里创建文档、构建应用、运行任务，依托 Cloudflare Workers 的全球网络和隔离环境。对企业开发者来说，稳定、安全、随用随开的执行空间，比单纯聊天能力更接近生产基础设施。</p>
<p>多 Agent 系统最大的难点不是“能不能同时跑”，而是上下文边界和结果合并。每个 Agent 必须只拿到完成任务所需的信息，产出要能被主流程验证，失败时要能重试或回滚。否则并行只会把一个人的混乱放大成一组助手的混乱。</p>
<p>比较成熟的做法，是让主控 Agent 只负责拆分、验收和决策，把搜索、实现、测试、审查这类独立任务派给子 Agent。每个子 Agent 交回来的不应只是结论，还要包含证据：读了哪些文件、运行了哪些命令、发现了哪些风险。只有证据能汇总，多 Agent 才能形成工程能力。</p>

<h2 id="execution-and-productivity-tools">五、执行层工具：网页、模型路由、内容生产和记忆</h2>
<p><strong><a href="https://github.com/firecrawl/firecrawl" target="_blank" rel="noopener">firecrawl/firecrawl</a></strong> 解决 AI 读网页的问题。普通抓取拿到的 HTML 往往混乱，AI 难以直接使用。Firecrawl 能把页面转成干净的 Markdown 或结构化内容，处理动态渲染和复杂页面，是 RAG、研究工具和网页分析应用的重要底座。</p>
<p><strong><a href="https://github.com/diegosouzapw/OmniRoute" target="_blank" rel="noopener">diegosouzapw/OmniRoute</a></strong> 代表多模型统一 API 和路由层。模型越来越多，接口、计费、延迟和上下文能力都不一样。统一入口能让开发者快速切换模型，并通过压缩、路由和降级策略降低成本。</p>
<p>OpenMontage 代表 AI 影像生产系统方向，类似把策划、素材、剪辑、字幕和生成工具整合成一个自动化工作室。<strong><a href="https://github.com/maiqingbu/openmontage-desktop" target="_blank" rel="noopener">maiqingbu/openmontage-desktop</a></strong> 是 OpenMontage 的桌面壳项目，体现了这类系统从命令行走向可操作产品的趋势。未来内容生产会越来越像 Agent 调用工具完成流水线，而不是人手工搬运每一步。</p>
<p><strong><a href="https://github.com/TencentCloud/TencentDB-Agent-Memory" target="_blank" rel="noopener">TencentCloud/TencentDB-Agent-Memory</a></strong> 是团队级记忆层。它把对话、技能、文档知识和代码图谱分层保存，让多个智能体跨会话共享必要上下文。没有记忆的 Agent 每次都像新员工；有记忆但没有权限边界的 Agent 又会带来隐私风险。分层、可控、可审计才是记忆系统的重点。</p>
<p><strong><a href="https://github.com/huggingface/speech-to-speech" target="_blank" rel="noopener">huggingface/speech-to-speech</a></strong> 把语音识别、语言模型和语音合成连成一条本地链路，适合搭建隐私友好的语音助手。<strong><a href="https://github.com/livekit/agents" target="_blank" rel="noopener">livekit/agents</a></strong> 则面向实时语音和多模态 Agent，重点处理延迟、打断、状态同步和实时通信。</p>
<p>执行层工具的价值可以用一句话概括：让模型离真实世界更近，但每一步都要可控。网页抓取要能复现来源，多模型路由要能记录成本和失败原因，内容生产要能保留素材链路，记忆系统要能删除和分级，实时语音要能处理中断和延迟。没有这些工程细节，Agent 很难进入长期生产。</p>

<h2 id="office-and-knowledge-skills">六、办公与知识技能：从 Notion 到 Word、PPT 和研究报告</h2>
<p>Notion 集成让 AI 能直接读写页面和数据库，把个人知识库变成可操作空间。会议纪要、项目资料、读书笔记和任务数据库都可以被 AI 检索、整理和更新。知识管理的关键，是让资料不再停留在孤立页面里，而是能进入工作流。</p>
<p>Word 和 PPT 技能把办公文件生成、编辑和检查变成自动化任务。报告、方案、合同草稿、演示文稿、培训材料，都可以由 AI 先生成可交付格式，再由人做内容判断和最终修改。真正节省时间的不是“写几段文字”，而是减少格式、排版、批量处理和反复复制粘贴。</p>
<p><strong><a href="https://github.com/sleepinginsummer/agent-browser-cli" target="_blank" rel="noopener">sleepinginsummer/agent-browser-cli</a></strong> 代表无头浏览器自动化。它让 AI 能打开网页、点击、填表、截图和抓取页面，而不必依赖网站 API。网页操作一旦涉及账户、提交和外部状态，就必须进入隔离环境，并保留日志和人工确认点。</p>
<p>Deep Research Forge、Ontology、Humanizer、PostFlight 等技能，则分别对应深度研究、领域概念图谱、AI 文本自然化和社媒发布节奏。它们说明 Skills 不只是开发者工具，也会进入办公室、内容团队、研究团队和个人品牌运营。</p>
<p>办公技能和开发技能的共同点，是都在减少重复动作。区别在于办公场景更强调格式、权限和协作。Word 文档要考虑修订和批注，PPT 要考虑版式一致，知识库要考虑谁能读写，研究报告要保留引用链路。AI 能自动生成初稿，但真正能落地的系统必须尊重这些组织流程。</p>

<h2 id="codex-ecosystem">七、Codex 生态：终端编码、审查、安全和插件扩展</h2>
<p><strong><a href="https://github.com/openai/codex" target="_blank" rel="noopener">openai/codex</a></strong> 是终端里的 AI 编码助手。它和传统聊天工具最大的区别，是可以直接进入项目上下文，读取文件、修改代码、运行命令和处理错误。开发者不再需要来回复制代码片段，AI 直接在仓库里工作。</p>
<p>DeepSeek Reasonix 一类终端工具则体现成本和本地化路线。<strong><a href="https://github.com/esengine/DeepSeek-Reasonix" target="_blank" rel="noopener">esengine/DeepSeek-Reasonix</a></strong> 基于 DeepSeek 模型思路，强调推理稳定、上下文处理和终端内编码体验。对中文开发者来说，低成本、中文交流和隐私边界都是重要选型变量。</p>
<p>Codex Security 类项目解决 AI 生成代码的安全审查。AI 直接写代码以后，注入、越权、敏感信息泄漏、依赖风险和不安全默认值都需要自动扫描。安全审查最好跑在 CI/CD 里，每次提交都查一遍，而不是上线前才人工补救。</p>
<p><strong><a href="https://github.com/openai/codex-plugin-cc" target="_blank" rel="noopener">openai/codex-plugin-cc</a></strong> 让 Claude Code 和 Codex 可以互相委托任务。多工具协作的关键，是让不同 Agent 做自己擅长的部分，而不是人工纠结该切到哪个窗口。Codex Review 类技能则把代码审查、变更记录和提交说明自动化，让维护开源项目或处理 PR 的开发者减少重复劳动。</p>
<p><strong><a href="https://github.com/andrewyng/openworker" target="_blank" rel="noopener">andrewyng/openworker</a></strong> 代表“独立交付型 Agent”的方向。它强调从需求到规划、执行、检查和交付都由 AI 自主完成。对知识工作者、内容团队和工程团队来说，真正值得评估的是哪些任务可以完整外包，哪些任务必须保留人工决策。</p>
<p><strong><a href="https://github.com/virgiliojr94/book-to-skill" target="_blank" rel="noopener">virgiliojr94/book-to-skill</a></strong> 把书籍和长文档转成 Agent 可加载的技能包。一本技术书经过拆解、提炼和结构化之后，可以变成 AI 工作流的一部分。学习不再只是人读完再复述，而是把知识直接注入助手的可调用上下文。</p>
<p><strong><a href="https://github.com/MoonshotAI/Kimi-K2" target="_blank" rel="noopener">MoonshotAI/Kimi-K2</a></strong> 代表国产长上下文和中文体验路线。围绕 Kimi 模型的终端编码助手，适合中文沟通、大文件理解和安全检查场景。对于国内开发者，中文自然表达、成本和响应速度会直接影响日常使用黏性。</p>
<p>终端编码生态的关键变化，是 AI 开始直接进入“读文件、改文件、跑命令、看失败、再修复”的闭环。这个闭环要求工具既要有权限控制，也要能保留操作证据。一个成熟的编码 Agent 不应只会生成代码，还要知道什么时候先写测试、什么时候不要动用户改过的文件、什么时候必须把失败日志带回给人。</p>

<h2 id="uiux-design-system">八、UI/UX 设计系统：让 AI 生成的界面不再千篇一律</h2>
<p>AI 写代码越来越强，但生成界面常常缺少审美、层级和设计系统意识。<strong><a href="https://github.com/nextlevelbuilder/ui-ux-pro-max-skill" target="_blank" rel="noopener">nextlevelbuilder/ui-ux-pro-max-skill</a></strong> 把设计规范、配色、组件层级、响应式约束和反模式检查整理成 AI 可调用技能。它的价值，是让 AI 先理解什么是好界面，再去写代码。</p>
<p>这类技能特别适合前端工程师、全栈开发者和独立开发者。没有设计背景时，AI 很容易做出“能跑但不好看”的页面；有了设计技能约束，输出会更像真实产品，而不是模板拼接。</p>
<p>UI/UX 技能也提醒开发者：生成式界面不是只看首屏截图，还要看信息密度、按钮状态、移动端适配、文字是否溢出、对比度是否够、交互是否符合用户预期。真正进入生产的界面，必须同时过设计和工程两道关。</p>

<h2 id="selection-framework">九、选型框架：先补短板，再装工具</h2>
<p>面对密集出现的 AI 项目，最容易犯的错是按热度全部尝试。更稳的顺序是先判断自己的工作流缺哪一层。缺经验沉淀，就看 Skills；缺长期记忆，就看记忆层；缺网页数据，就看 Firecrawl 和浏览器工具；缺执行环境，就看云端电脑和沙箱；缺代码质量，就看审查、安全扫描和测试闭环；缺界面质量，就看 UI/UX 技能。</p>
<p>每个项目都应该用一个小任务验证：能否安装，许可证是否清楚，是否仍在维护，是否会上传敏感数据，是否能接入现有工作流，失败后是否能回滚。新增 Star 和热榜只能说明需求强，不能替代生产验证。</p>
<p>真正有价值的 AI 工具，不是让人多开几个入口，而是把重复劳动变成稳定流程。先让一个流程跑通，再把稳定步骤抽成技能，把历史决策交给记忆，把外部动作交给受控工具，把结果交给测试和审查。这样，开源项目的热度才会变成长期效率。</p>
<p>落地时可以按低风险到高风险排序：先用 Skills 管理个人提示和工程规范，再接入只读搜索与网页解析；确认稳定后接入代码修改和本地命令；最后才让 Agent 访问账户、提交表单或触发外部任务。越接近真实业务动作，越需要审计、权限、回滚和人工检查点。</p>
<p>对个人开发者来说，最实际的路径是先建立一个小而稳定的工具栈：一个终端编码助手，一个 Skills 目录，一个网页解析工具，一个项目记忆文件，再加一组固定验证命令。等这套流程稳定后，再逐步尝试云端电脑、多 Agent 调度和自动发布。工具越多，越需要先有秩序。</p>
<p>对团队来说，判断一个 AI 工具是否值得进入生产，不应只看演示效果，而要看它能否进入现有权限体系、能否留下审计记录、能否通过测试与代码审查、能否在成员流动后继续复用经验。能沉淀流程的工具，才会留下真正的复利；只制造新入口的工具，很快会被更稳定、更可治理的工作流替代，长期价值也会被重新定价。</p>

<h2 id="final-view">十、结论：AI 工具正在变成生产系统</h2>
<p>这一批项目覆盖了从 AI 编程、Agent 框架、技能市场、云端执行、网页理解、办公自动化、内容生产到 UI 设计的完整链条。它们的共同方向，是让 AI 不只会回答，而是能在明确边界内完成任务、保存经验、调用工具、接受审查并交付结果。</p>
<p>下一阶段的竞争，不只是谁的模型更强，而是谁能把模型接进可控工作流：有技能，有记忆，有权限，有沙箱，有审查，有回滚，也有面向真实业务的交付标准。开发者和团队要做的，不是追逐每一个新项目，而是建立自己的 AI 工作系统。</p>
'''


base.POSTS = [
    base.Post(
        slug="remotion-claude-code-vox-motion-design-workflow",
        title="用 Remotion 和 Claude Code 生成 Vox 风格动效短片：从视觉系统到自动渲染",
        desc="从视觉系统、MCP 素材、场景分层、半调人物、Remotion Studio 微调到旁白同步，拆解代码化动效生产工作流。",
        category="AI工具",
        series="内容自动化",
        tags=["Remotion", "Claude Code", "Vox", "动效", "MCP", "AI创作", "内容生产"],
        minutes=11,
        body=BODY_REMOTION,
        accent=("#111827", "#7c3aed", "#ef4444"),
        required=["Remotion", "Claude Code", "MCP", "半调", "Remotion Studio", "1080p", "旁白"],
        minimum=5200,
    ),
    base.Post(
        slug="ai-skills-agent-fullstack-open-source-daily-20260812",
        title="8月12日 AI Skills/Agent 全栈开源项目速览：从自进化助手到 Codex 插件生态",
        desc="梳理 AI Skills、Agent 框架、云端执行、网页理解、办公技能、Codex 生态和 UI/UX 设计系统的开源工具链。",
        category="AI工具",
        series="AI Agent",
        tags=["AI Skills", "AI Agent", "开源项目", "GitHub", "Codex", "Claude Code", "Agent框架", "UI设计"],
        minutes=16,
        body=BODY_AI_SKILLS,
        accent=("#0f172a", "#0f766e", "#2563eb"),
        required=["hermes-agent", "anthropics/skills", "Graphify", "superpowers", "Firecrawl", "Codex", "Kimi-K2", "UI/UX"],
        minimum=7600,
    ),
]


_active_ref = None
_base_validate = base.validate


def get_file_at_active_ref(path: str) -> str | None:
    if _active_ref is None:
        raise RuntimeError("active remote ref is not set")
    api_path = quote(path, safe="/")
    try:
        data = base.run_gh([base.endpoint(f"contents/{api_path}?ref={_active_ref.commit_sha}")])
    except RuntimeError as exc:
        if "Not Found" in str(exc):
            return None
        raise
    return base64.b64decode(data["content"]).decode("utf-8")


def validate(outputs: dict[str, str]) -> None:
    _base_validate(outputs)
    extra_forbidden = ["Bilibili", "哔哩哔哩", "视频里", "视频中", "原视频", "音频里", "音频中", "这期", "本期", "作者说", "他提到", "观看", "点赞", "订阅", "投币", "收藏", "下期", "关注", "感谢大家", "BV1"]
    expected_links = {
        "https://github.com/NousResearch/hermes-agent",
        "https://github.com/anthropics/skills",
        "https://github.com/contains-studio/agents",
        "https://github.com/Graphify-Labs/graphify",
        "https://github.com/runaki-ai/ponytail-gain",
        "https://github.com/addyosmani/agent-skills",
        "https://github.com/shanraisshan/claude-code-best-practice",
        "https://github.com/microsoft/AI-For-Beginners",
        "https://github.com/obra/superpowers",
        "https://github.com/mattpocock/skills",
        "https://github.com/zhaoxuya520/reverse-skill",
        "https://github.com/cisco-ai-defense/skill-scanner",
        "https://github.com/claw-opus/proactive-self-improving-agent",
        "https://github.com/lanyasheng/self-improving-agent",
        "https://github.com/Panniantong/Agent-Reach",
        "https://github.com/cloudflare/computer",
        "https://github.com/firecrawl/firecrawl",
        "https://github.com/diegosouzapw/OmniRoute",
        "https://github.com/maiqingbu/openmontage-desktop",
        "https://github.com/TencentCloud/TencentDB-Agent-Memory",
        "https://github.com/huggingface/speech-to-speech",
        "https://github.com/livekit/agents",
        "https://github.com/sleepinginsummer/agent-browser-cli",
        "https://github.com/openai/codex",
        "https://github.com/esengine/DeepSeek-Reasonix",
        "https://github.com/openai/codex-plugin-cc",
        "https://github.com/andrewyng/openworker",
        "https://github.com/virgiliojr94/book-to-skill",
        "https://github.com/MoonshotAI/Kimi-K2",
        "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill",
    }
    failures: list[str] = []
    for post in base.POSTS:
        slug = post.slug
        article = outputs[f"2026/{slug}/index.html"]
        cover = outputs[f"images/posts/{slug}/cover.svg"]
        for word in extra_forbidden:
            if word in article or word in cover:
                failures.append(f"{slug}: forbidden wording present: {word}")
    article2 = outputs["2026/ai-skills-agent-fullstack-open-source-daily-20260812/index.html"]
    actual_links = set(re.findall(r'https://github\.com/[^"<]+', article2))
    missing = sorted(expected_links - actual_links)
    if missing:
        failures.append("AI Skills article missing GitHub links: " + ", ".join(missing))
    detailed_terms = {
        "2026/remotion-claude-code-vox-motion-design-workflow/index.html": ["统一背景", "prop controls", "spring", "interpolate", "ElevenLabs", "master sequence"],
        "2026/ai-skills-agent-fullstack-open-source-daily-20260812/index.html": ["长期记忆", "技能市场", "云端电脑", "多模型", "无头浏览器", "终端编码", "UI/UX"],
    }
    for path, terms in detailed_terms.items():
        article = outputs[path]
        for term in terms:
            if term not in article:
                failures.append(f"{path}: missing detailed term {term}")
    if failures:
        raise SystemExit("\n".join(failures))


def write_outputs(outputs: dict[str, str]) -> None:
    out_dir = Path("/tmp/remotion-ai-skills-two-articles-20260813-publish-output")
    if out_dir.exists():
        import shutil

        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for rel, content in outputs.items():
        path = out_dir / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(json.dumps({"local_output": str(out_dir), "files": len(outputs), "urls": [post.full_url for post in base.POSTS]}, ensure_ascii=False, indent=2))


def create_commit(outputs: dict[str, str], ref: base.RemoteRef) -> str:
    entries = []
    for path, content in sorted(outputs.items()):
        blob = base.run_gh(["-X", "POST", base.endpoint("git/blobs"), "--input", "-"], {"content": content, "encoding": "utf-8"})
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    tree = base.run_gh(["-X", "POST", base.endpoint("git/trees"), "--input", "-"], {"base_tree": ref.tree_sha, "tree": entries})
    commit = base.run_gh(
        ["-X", "POST", base.endpoint("git/commits"), "--input", "-"],
        {"message": "Publish Remotion workflow and AI Skills daily articles", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    base.run_gh(["-X", "PATCH", base.endpoint(f"git/refs/heads/{base.BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


def main() -> None:
    global _active_ref
    for attempt in range(3):
        ref = base.get_ref()
        _active_ref = ref
        base.get_file = get_file_at_active_ref
        outputs = base.collect_outputs()
        validate(outputs)
        write_outputs(outputs)
        try:
            commit_sha = create_commit(outputs, ref)
        except RuntimeError as exc:
            if attempt < 2 and "Reference update failed" in str(exc):
                continue
            raise
        current_head = base.get_ref().commit_sha
        if current_head != commit_sha:
            comparison = base.run_gh([base.endpoint(f"compare/{commit_sha}...{current_head}")])
            if comparison.get("status") != "ahead":
                raise RuntimeError("published commit is not an ancestor of current remote head")
        print(json.dumps({"parent": ref.commit_sha, "pushed": commit_sha, "urls": [post.full_url for post in base.POSTS]}, ensure_ascii=False, indent=2))
        return
    raise RuntimeError("publication retried after concurrent updates but did not succeed")


if __name__ == "__main__":
    main()
