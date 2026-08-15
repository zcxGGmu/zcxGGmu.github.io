from __future__ import annotations

import base64
import importlib.util
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
BASE_SCRIPT = TASKS / "publish-three-life-business-articles-20260809.py"
ASSET_DIR = TASKS / "video-batch-20260816-bv1ug" / "screenshots"

spec = importlib.util.spec_from_file_location("publish_base", BASE_SCRIPT)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = base
spec.loader.exec_module(base)

_base_run_gh = base.run_gh


def run_gh_with_retry(args: list[str], payload: dict | None = None):
    for attempt in range(5):
        try:
            return _base_run_gh(args, payload)
        except RuntimeError as exc:
            msg = str(exc).lower()
            if attempt < 4 and any(token in msg for token in ["stream error", "cancel", "connection", "reset", "timeout", "temporarily"]):
                time.sleep(2 + attempt * 3)
                continue
            raise


base.run_gh = run_gh_with_retry
base.__file__ = __file__
base.DATE = "2026-08-16"
base.BASE_DT = datetime(2026, 8, 16, 1, 15, 0, tzinfo=timezone(timedelta(hours=8)))
base.PREV_EXISTING_URL = "/2026/semiconductor-equipment-wfe-localization-100b-2028-gap/"
base.PREV_EXISTING_TITLE = "1000 亿美元 WFE 市场：中国半导体设备国产化从 23% 走向 52%"
base.SCRIPT_NAME = Path(__file__).name
base.MANIFEST_NAME = "publish-deepseek-harness-cordis-article-20260816-changed-files.json"
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

PAGE1_SIZE = 24
PAGE_SIZE = 10
SLUG = "deepseek-harness-cordis-spatiotemporal-composability-runtime-agent-evolution"
_active_ref = None


def fig(slug: str, name: str, caption: str) -> str:
    return f'<figure class="post-figure"><img src="/images/posts/{slug}/{name}" alt="{caption}" loading="lazy"><figcaption>{caption}</figcaption></figure>'


BODY = rf'''
<p><a href="https://github.com/deepseek-ai/deepseek-harness" target="_blank" rel="noopener">DeepSeek Harness</a> 的重要性，不在于又多了一个 Agent 框架，而在于它把模型、工具、技能、沙箱、循环和界面都放进同一个插件化运行层里。一个智能体系统不再只是“模型加工具”的组合，而是一个可以在运行时装入、卸载、替换和演化的系统。</p>
<p>真正难的问题也随之出现：运行中的系统如果换掉一个组件，能不能不重启，还能证明旧组件留下的修改已经被收干净？如果 Agent 未来要持续自我改造，错误修改能不能被完整撤回？这不是产品体验问题，而是运行时正确性问题。</p>
<p><a href="https://github.com/cordiverse/paper" target="_blank" rel="noopener">A Programming Paradigm for Spatiotemporal Composability</a> 给出的答案，是把动态组合拆成“时间”和“空间”两个维度：时间上，组件卸载以后，它对环境造成的影响要能被回收；空间上，组件之间的依赖关系要能声明出来，并且随着环境变化自动调整。理论落在 <a href="https://github.com/cordiverse/cordis" target="_blank" rel="noopener">Cordis</a> 这个开源元框架上，并在 <a href="https://github.com/koishijs/koishi" target="_blank" rel="noopener">Koishi</a> 生态中经过长期工程检验。</p>
{fig(SLUG, 'paper-outline.jpg', '论文目录把问题拆成可逆效应、响应式余效应、组件加载器与元定理，核心是时空可组合性。')}

<h2 id="why-runtime-composability-matters">一、为什么运行时换组件不能只靠重启</h2>
<p>传统工程处理动态变化，最粗暴的办法是重启进程。组件坏了，配置错了，依赖冲突了，把进程拉起来重来。对于很多服务，这个办法确实能解决一部分问题，因为进程退出会顺便清掉内存、连接、监听器、缓存和临时状态。</p>
<p>但 Agent Harness 的运行形态把这个办法逼到了边界。Harness 不是一个孤立函数，而是模型外围的一层工作系统：它管理工具调用、长短期记忆、上下文组织、循环调度、沙箱执行、界面适配和外部服务连接。一次重启可能丢掉正在执行的任务，打断长连接，清空缓存，重建上下文，甚至让恢复机制本身失效。</p>
<p>容器编排也只能解决服务粒度的问题。它可以替换一个容器，却很难表达同一个进程里两个模块之间的细粒度依赖。原本一次函数调用可以完成的协作，如果为了隔离全部拆成进程间通信，系统复杂度、性能成本和部署负担都会上升。</p>
<p>更关键的是自进化。Meta-Harness、AHE、Continual Harness、Autogenesis 等方向都在把 Harness 继续推向自动搜索、自动改造和持续演化。只要系统允许自己生成并替换自己的组件，每一次自修改都是一次运行时动态组合。如果每次都靠重启兜底，频率一高就不可用；如果错误修改把恢复路径也破坏了，系统连自救都做不到。</p>

<h2 id="two-axes-time-and-space">二、时空可组合性：时间要能撤，空间要能接</h2>
<p>这项工作的核心，是把动态组合拆成两个正交维度。第一个维度是时间可组合性。组件被加载以后，会对环境做修改：注册路由、添加事件监听、注入服务、打开资源、写入上下文。组件卸载时，这些修改不能只靠程序员凭记忆手写清理代码，而要有一套机制保证它们按正确顺序被撤回。</p>
<p>第二个维度是空间可组合性。组件之间不是孤立存在的，一个插件可能依赖数据库服务，一个工具可能依赖模型接口，一个沙箱适配器可能依赖文件系统权限。依赖关系如果藏在命令式代码里，运行时就无法判断谁该先启动，谁该等服务准备好，谁在服务消失后必须停下来。</p>
<p>所以，时间维度回答“改过的环境怎样恢复”；空间维度回答“依赖的环境怎样声明和响应”。二者合在一起，才构成真正适合 Agent Harness 的运行时组合模型。</p>

<h2 id="from-effects-to-runtime-objects">三、把效应和余效应从编译期搬到运行时</h2>
<p>程序语言理论里早就有“效应”和“余效应”的概念。效应描述一段计算会怎样修改环境，余效应描述一段计算依赖环境中的什么能力。传统效应系统主要服务编译期静态分析：代码写好以后，编译器检查它会使用什么资源、产生什么副作用、是否满足类型和上下文约束。</p>
<p>运行时动态插件的问题在于，编译期并不知道未来会加载什么组件，也不知道某个服务会在什么时候出现、什么时候消失。依赖可能在系统运行几小时、几天以后才出现，修改也可能来自外部安装的新组件。静态分析的词汇仍然有价值，但不能原封不动地套用。</p>
<p>因此，Cordis 的方案不是只在类型层面描述效应，而是把效应和余效应实体化，变成运行时可以记录、组合、撤回和通知的对象。每一次环境修改都带着一个逆变换，每一份依赖都变成声明式规格，运行时据此维护组件状态。</p>

<h2 id="reversible-effects">四、可逆效应：每一次修改都必须自带撤销路径</h2>
<p>时间维度的关键机制叫可逆效应。系统里每一次对环境的修改，不能只交出一个新状态，还必须同时交出一个逆操作。注册路由时，要知道如何注销路由；添加监听器时，要知道如何移除监听器；注入服务时，要知道如何从上下文中撤掉服务；打开资源时，要知道怎样释放资源。</p>
<p>这些逆操作不是由框架在事后统一猜出来的，而是在执行点当场构造。原因很直接：很多撤销所需的信息只有当下才存在。资源句柄、注册键、实际替换掉的旧值、分配出来的生成性名称，都必须在修改发生那一刻被捕获。等到卸载时再想办法找回来，往往已经太晚。</p>
<p>运行时把这些逆操作按相反顺序复合起来，形成一个后进先出的累加器。加载时先执行 A 再执行 B，卸载时就先撤 B 再撤 A。这个顺序并不是代码洁癖，而是恢复正确性的基本条件。后来的修改通常建立在先前修改之上，反过来撤销才能避免悬空引用和半清理状态。</p>
<p>逆操作还要满足见证约束：把逆操作应用在新状态上，必须回到原来的状态。这个要求把“尽量清理”提升成了可证明的局部契约。每一步都能局部撤回，复合起来才可能得到整体恢复。</p>

<h2 id="observational-equivalence">五、恢复不是字节级倒带，而是观测等价</h2>
<p>可逆效应并不承诺把世界恢复到字节级完全相同。它追求的是观测等价：外部观察者无法通过系统定义的接口区分恢复后的状态和加载前的状态。内存分配地址可能不同，生成性名称可能重新分配，缓存内部布局可能改变，只要这些差异不影响可观察行为，就不破坏恢复语义。</p>
<p>这个边界非常重要。运行时系统如果要求字节级倒带，很快会变得不可实现，也无法处理真实系统中的资源分配和调度差异。观测等价把保证限定在接口可见行为上，让理论和工程可以接上。</p>
<p>与此同时，效应独立性并不是免费得到的。多个组件交错修改同一环境时，某些操作必须两两可交换，才能保证不同执行顺序不会改变最终可观察结果。这个可交换性不是靠框架凭空判断，而是落在提供者接口的定义上。接口设计者必须说明哪些键、哪些操作、哪些状态变化可以互不干扰。</p>

<h2 id="reactive-coeffects">六、响应式余效应：依赖不是暗线，而是声明式规格</h2>
<p>空间维度的核心机制叫响应式余效应。组件不应该在加载函数里偷偷读取某个服务，然后把依赖关系藏进闭包里。它应该声明自己需要哪些上下文键、哪些服务、哪些能力。运行时维护全局依赖注册表，根据环境变化对组件状态进行分类处理。</p>
<p>当某个组件需要的依赖全部满足，变化就是激活型，组件可以进入加载流程；当依赖消失或不再满足，变化就是失活型，组件需要进入卸载流程；当变化不影响它的依赖集合，就是中性变化，可以保持当前状态。</p>
<p>这种设计把“谁依赖谁”从隐式工程约定变成运行时事实。插件加载不再只是执行一个函数，而是把组件实例、依赖规格、上下文隔离、绑定元数据和状态迁移都纳入同一个注册表。运行时可以据此决定启动顺序、暂停时机、卸载路径和重新激活范围。</p>

<h2 id="two-phase-unload">七、两阶段卸载：先断新引用，再等旧引用清理</h2>
<p>动态系统最容易出错的地方，是提供者和消费者的卸载顺序。数据库服务、存储后端、模型适配器、工具执行器都可能被其他组件使用。如果提供者一卸载就立刻释放资源，消费者还没完成清理，就会拿着已经失效的引用继续运行，最终触发难排查的错误。</p>
<p>两阶段卸载解决的是这个顺序问题。第一阶段，提供者先从全局服务表中移除，让新的消费者无法再解析到它；但提供者资源暂时不立刻释放。第二阶段，运行时等待已有消费者完成清理，确认没有旧依赖继续使用它，再调用累加器释放提供者自身资源。</p>
<p>这让系统同时避免两类问题：一方面，不会继续产生新的依赖；另一方面，也不会提前释放仍被旧消费者使用的资源。对于长期运行的 Agent Harness，这种顺序保证比单纯的“卸载回调”更可靠。</p>
{fig(SLUG, 'runtime-fiber-rules.jpg', '组件加载与卸载被拆成一串有状态的效应迭代，而不是一次性完成的黑箱动作。')}

<h2 id="activation-is-iterative">八、加载不是一口气完成，而是一串效应迭代</h2>
<p>组件激活也不是一次函数调用就结束。真实加载过程可能包含多个步骤：解析依赖、注入上下文、注册监听器、异步导入模块、初始化资源、启动服务。每一步都会产生效应，也可能在中途遇到目标状态变化。</p>
<p>因此，加载过程被建模为一串效应迭代，并且在边界处设置检查点。如果组件正在加载，而系统目标突然变成卸载，运行时不会粗暴打断任意中间状态，而是在迭代边界把路径转向卸载。如果有异步操作已经在路上，它必须先落地，然后马上转入回滚路径。</p>
<p>失败处理也被纳入同一语义。加载中某一步失败，已经产生的部分效应要按累加器回滚，错误记录在组件实例上，而不是让半加载状态泄露到环境里。这样，失败不是“工程异常”，而是运行时状态机的一部分。</p>

<h2 id="metatheorems">九、五条元定理：给动态组合加上明确前提</h2>
<p>这套机制最有价值的地方，不只是提出工程模式，而是给出带前提的形式化保证。五条元定理大致覆盖保持性、恢复精确性、保序性、进度和合流性。</p>
<p>保持性说明系统从一个良构状态出发，经过合法迁移以后仍然保持良构。恢复精确性说明在满足条件时，卸载累加器可以把环境恢复到加载前的观测等价状态。保序性说明组件之间的依赖和卸载顺序不会被任意打乱。进度说明在依赖无环、迭代有界等前提下，系统不会卡在无法推进的中间状态。合流性说明在无失败且系统达到静止时，不同合法执行路径会收敛到同一个可观察结果。</p>
<p>这些定理都带着明确前提。合流性不覆盖失败情形，失败由恢复和保序相关语义处理；效应独立依赖操作可交换；依赖注册表必须良构；迭代必须有界。清楚写出前提，比泛泛声称“可热插拔”更重要，因为它告诉工程师保证在哪里成立，也告诉工程师边界在哪里。</p>

<h2 id="ctx-effect-in-cordis">十、Cordis 的实现：ctx.effect 把清理路径从加载路径里长出来</h2>
<p>Cordis 在工程实现上抓住了一个关键原语：<code>ctx.effect</code>。插件作者在加载时通过它登记对上下文的修改，运行时同时获得对应的清理信息。这样，卸载路径不是另一段容易遗忘、容易写错、容易和加载逻辑不一致的代码，而是从加载过程中的效应记录自然派生出来。</p>
<p>这和常见 Webpack、Vite 热模块替换有本质差别。传统 HMR 往往围绕模块边界和手写 accept/dispose 回调工作，开发者需要自己维护哪些状态可保留、哪些状态要清掉。Cordis 的边界来自组件实例、效应、依赖规格和上下文注册表。热替换不只是重新 import 一个模块，而是一场带依赖重算、效应回滚和状态迁移的事务。</p>
<p>如果新模块导入失败，事务式热替换可以整体回滚；如果依赖变化只影响部分插件，运行时只重新激活受影响组件，而不是把整个系统推倒重来。这一点对 Agent Harness 尤其关键，因为 Harness 的每个部件都可能是插件：模型适配器、工具集合、记忆层、沙箱、循环策略和 UI 通道都需要可替换，但不能每次替换都破坏整个工作环境。</p>
{fig(SLUG, 'component-loader.jpg', '组件加载器把 ctx.effect、ctx.use、ctx.set 等命令式原语组织为声明式的动态组合过程。')}

<h2 id="koishi-case">十一、Koishi 案例：4000 多个插件的工程压力测试</h2>
<p>Koishi 是 Cordis 之上的聊天机器人框架，长期积累了 4000 多个社区插件。这个案例的意义，不在于它能替代受控实验，而在于它证明这套抽象能在真实社区生态里承受插件数量、作者差异和长期演进的压力。</p>
<p>插件作者不需要为每个改动单独维护一份卸载路径，仍然可以获得有序清理。存储后端切换时，系统不需要全量重启，而是根据依赖关系只让相关插件失活并重新激活。服务提供者、消费者和上下文隔离通过运行时注册表连接起来，复杂度集中在框架语义里，而不是分散到每个插件的手写生命周期代码中。</p>
<p>当然，这仍然是单一 TypeScript 生态下的观察性案例，不是跨语言、跨运行时、跨组织的对照实验。它证明“可用”，但还没有完全证明“处处适用”。这一区分必须保留。</p>

<h2 id="limits-and-boundaries">十二、边界：发射型操作、沙箱和抽象开销</h2>
<p>任何恢复机制都有系统边界。能被可逆效应覆盖的，是那些在运行环境里留下可追踪记录的操作，比如注册监听、打开资源、写入上下文、注入服务。已经发射出去的动作则不同：网络消息已经发出，共享文件已经写入，外部支付已经完成，远端系统已经收到请求，这些效果不能靠本地累加器直接收回。</p>
<p>这类操作需要两种策略。第一种是延迟提交，在状态确定以后再向外部世界发射；第二种是应用层补偿，比如退款、删除自己创建的文件、撤销远端记录。补偿也可以按后进先出方式组织，但它已经超出原本定理的保证范围，需要新的应用语义支撑。</p>
<p>还有一个边界是不可信代码。组件如果绕过上下文，直接触碰底层对象或系统资源，语言层的效应记录无法自动拦住它。真正的不可信执行仍然需要沙箱、权限隔离和进程级边界。Cordis 解决的是协作式组件在同一运行时里的组合正确性，不是把恶意代码变成安全代码。</p>
<p>最后是成本问题。动态依赖注册、效应记录、状态迁移和事务式回滚都不是免费的。目前最缺的是抽象开销的定量数据：在大量组件、高频热替换和复杂依赖图下，运行时管理成本到底多高，还需要更多测量。</p>

<h2 id="agent-evolution">十三、对 Agent 自进化的意义：能改自己只是开始</h2>
<p>Agent 自进化最容易被讲成一个生成问题：系统能不能写出新工具，能不能生成新策略，能不能自动搜索更好的 Harness。这个问题当然重要，但还不够。真正长期运行的系统，还必须回答另一个问题：改错以后怎么办。</p>
<p>如果每次改造都是不可逆的，系统越能自改，风险就越大。一个错误工具可能污染上下文，一个错误记忆组件可能破坏检索，一个错误沙箱策略可能放大权限风险，一个错误循环策略可能让任务永远跑不完。自进化必须和可回滚、可隔离、可观察的运行时语义绑定在一起。</p>
<p>Cordis 给出的启发是：Agent Harness 不应该只是插件仓库和工具注册表，而应该是一个带时空可组合性语义的运行系统。每次修改自带撤销路径，每份依赖显式声明，加载、失败、卸载和重载都有状态机，动态组合才能从经验工程走向可证明工程。</p>

<h2 id="final-view">十四、结论：把动态组件替换变成有定理兜底的工程对象</h2>
<p>DeepSeek Harness 把“Everything is a Plugin”推到 Agent 运行层，Cordis 和时空可组合性则回答了插件化之后最根本的问题：插件装上去以后怎样干净拆下来，依赖变化时怎样只重算必要部分，失败发生时怎样把局部修改退回去。</p>
<p>可逆效应解决时间维度，响应式余效应解决空间维度，两阶段卸载解决提供者与消费者的顺序，<code>ctx.effect</code> 把加载和清理合成同一条效应轨迹，五条元定理把保证建立在明确前提之上。它不是简单的热更新技巧，而是把运行时组件替换变成了一个有名字、有边界、有实现、有理论支撑的对象。</p>
<p>Agent 能改自己，只是开始。改错了还能完整退回，依赖变了还能有序重组，失败了还能回到可观察的一致状态，才谈得上持续演化。未来真正可靠的自进化 Harness，拼的不会只是模型生成能力，还会拼运行时能不能把每一次变化装得上、拆得净、回得来。</p>
'''


base.POSTS = [
    base.Post(
        slug=SLUG,
        title="DeepSeek Harness 背后的 Cordis：把 Agent 自进化变成可回滚的运行时系统",
        desc="从可逆效应、响应式余效应、两阶段卸载到 ctx.effect，理解 Cordis 怎样为 Agent Harness 的动态组件替换提供形式化地基。",
        category="AI",
        series="Agent 系统",
        tags=["DeepSeek Harness", "Cordis", "Agent", "自进化", "运行时", "插件系统", "Koishi", "形式化验证"],
        minutes=15,
        body=BODY,
        accent=("#111827", "#2563eb", "#10b981"),
        required=["DeepSeek Harness", "Cordis", "A Programming Paradigm for Spatiotemporal Composability", "可逆效应", "响应式余效应", "ctx.effect", "两阶段卸载", "观测等价", "合流性", "Koishi", "4000", "TypeScript", "Webpack", "Vite", "DeepSeek", "Autogenesis", "AHE"],
        minimum=5200,
    )
]

SCREENSHOT_SOURCES = {
    SLUG: [
        ("BV1ugby6jEKN_20.jpg", "paper-outline.jpg"),
        ("BV1ugby6jEKN_510.jpg", "runtime-fiber-rules.jpg"),
        ("BV1ugby6jEKN_790.jpg", "component-loader.jpg"),
    ]
}
_base_validate = base.validate


def get_file_at_active_ref(path: str) -> str | None:
    if _active_ref is None:
        raise RuntimeError("active remote ref is not set")
    try:
        data = base.run_gh([base.endpoint(f"contents/{quote(path, safe='/')}?ref={_active_ref.commit_sha}")])
    except RuntimeError as exc:
        if "Not Found" in str(exc):
            return None
        raise
    return base64.b64decode(data["content"]).decode("utf-8")


def cards_from(text: str) -> list[str]:
    return re.findall(r'<a href="[^"]+" class="a-block">.*?</a>', text, re.S)


def card_href(card: str) -> str:
    match = re.match(r'<a href="([^"]+)" class="a-block">', card)
    if match is None:
        raise RuntimeError("card href missing")
    return match.group(1)


def pagination_nav(page: int, total: int) -> str:
    previous = "" if page == 1 else "/" if page == 2 else f"/page/{page - 1}/"
    nxt = f"/page/{page + 1}/" if page < total else ""
    left = f'<a class="pagination-action" href="{previous}"><span class="pagination-action-icon" aria-hidden="true">‹</span></a>' if previous else '<span class="pagination-action disabled"><span class="pagination-action-icon" aria-hidden="true">‹</span></span>'
    right = f'<a class="pagination-action" href="{nxt}"><span class="pagination-action-icon" aria-hidden="true">›</span></a>' if nxt else '<span class="pagination-action disabled"><span class="pagination-action-icon" aria-hidden="true">›</span></span>'
    return f'''<div class="pagination">
    <a id="globalBackToTop" class="pagination-action animated-visibility invisible" href="#top"><span class="pagination-action-icon" aria-hidden="true">↑</span></a>
    {left}
    <div class="pagination-indicator"><span style="text-align:center;line-height:1.2em">{page}<br><div style="display:inline-block;transform:rotate(-28deg);margin:2px 0">-</div><br>{total}</span></div>
    {right}
  </div></div>
    <div class="pagination">
    {left}
    <div class="pagination-indicator"><span style="text-align:center;line-height:1.2em">{page}/{total}</span></div>
    {right}
  </div>'''


def page_html(template: str, cards: list[str], page: int, total: int) -> str:
    first = template.find('<a href="', template.find('post-list-container'))
    matches = list(re.finditer(r'<a href="[^"]+" class="a-block">.*?</a>', template, re.S))
    if first == -1 or not matches:
        raise RuntimeError("pagination card markers missing")
    result = template[:first] + "\n".join(cards) + template[matches[-1].end():]
    result = re.sub(
        r'(<div id="extraContainer" class="extra-container"><div class="toc-wrapper"></div>).*?(<div id="single-column-footer">)',
        lambda m: m.group(1) + pagination_nav(page, total) + "\n    " + m.group(2),
        result,
        count=1,
        flags=re.S,
    )
    url = base.SITE + ("/" if page == 1 else f"/page/{page}/")
    result = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', result, count=1)
    return re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', result, count=1)


def rebuild_pagination(outputs: dict[str, str | None]) -> tuple[int, int]:
    template = outputs["index.html"]
    cards = cards_from(template or "")
    previous_pages = 1
    for page in range(2, 200):
        source = get_file_at_active_ref(f"page/{page}/index.html")
        if source is None:
            break
        previous_pages = page
        cards.extend(cards_from(source))
    unique_cards: list[str] = []
    seen: set[str] = set()
    for card in cards:
        href = card_href(card)
        if href not in seen:
            seen.add(href)
            unique_cards.append(card)
    cards = unique_cards
    total = 1 + ((max(0, len(cards) - PAGE1_SIZE) + PAGE_SIZE - 1) // PAGE_SIZE)
    outputs["index.html"] = page_html(template or "", cards[:PAGE1_SIZE], 1, total)
    cursor = PAGE1_SIZE
    for page in range(2, total + 1):
        outputs[f"page/{page}/index.html"] = page_html(template or "", cards[cursor:cursor + PAGE_SIZE], page, total)
        cursor += PAGE_SIZE
    for page in range(total + 1, previous_pages + 1):
        outputs[f"page/{page}/index.html"] = None
    return len(cards), total


def collect_binary_outputs() -> dict[str, bytes]:
    out: dict[str, bytes] = {}
    for post in base.POSTS:
        for src, dest in SCREENSHOT_SOURCES[post.slug]:
            out[f"images/posts/{post.slug}/{dest}"] = (ASSET_DIR / src).read_bytes()
    return out


def refresh_manifest(outputs: dict[str, str | None], binary_outputs: dict[str, bytes]) -> None:
    manifest_path = f"tasks/{base.MANIFEST_NAME}"
    manifest_files = sorted({path for path, content in outputs.items() if content is not None} | set(binary_outputs.keys()) | {manifest_path})
    outputs[manifest_path] = json.dumps(manifest_files, ensure_ascii=False, indent=2)


def validate(outputs: dict[str, str | None], binary_outputs: dict[str, bytes], card_count: int, total_pages: int) -> None:
    text_outputs = {path: content for path, content in outputs.items() if content is not None}
    _base_validate(text_outputs)
    failures: list[str] = []
    forbidden = [
        "B站", "bilibili", "Bilibili", "哔哩", "视频里", "视频中", "原视频", "音频里", "音频中", "UP主", "up主", "这期", "本期",
        "作者说", "他提到", "观看", "点赞", "订阅", "投币", "收藏", "下期", "关注", "欢迎收看", "感谢大家", "三连", "BV1",
    ]
    for post in base.POSTS:
        article = outputs[f"2026/{post.slug}/index.html"] or ""
        cover = outputs[f"images/posts/{post.slug}/cover.svg"] or ""
        for word in forbidden:
            if word in article or word in cover:
                failures.append(f"{post.slug}: forbidden wording {word}")
        for _, dest in SCREENSHOT_SOURCES[post.slug]:
            remote_path = f"images/posts/{post.slug}/{dest}"
            if remote_path not in binary_outputs:
                failures.append(f"{post.slug}: missing binary screenshot {dest}")
            if f"/{remote_path}" not in article:
                failures.append(f"{post.slug}: article does not reference {dest}")
        if article.count('<figure class="post-figure">') != len(SCREENSHOT_SOURCES[post.slug]):
            failures.append(f"{post.slug}: figure count mismatch")
    all_hrefs: list[str] = []
    for page in range(1, total_pages + 1):
        path = "index.html" if page == 1 else f"page/{page}/index.html"
        html = outputs.get(path) or ""
        hrefs = re.findall(r'<a href="([^"]+)" class="a-block">', html)
        all_hrefs.extend(hrefs)
        if page == 1 and len(hrefs) != PAGE1_SIZE:
            failures.append(f"homepage card count {len(hrefs)} != {PAGE1_SIZE}")
        if page > 1 and page < total_pages and len(hrefs) != PAGE_SIZE:
            failures.append(f"{path} card count {len(hrefs)} != {PAGE_SIZE}")
    if len(all_hrefs) != card_count or len(all_hrefs) != len(set(all_hrefs)):
        failures.append("pagination coverage/duplicates failed")
    expected_prefix = base.PINNED_PREFIX + [post.url_path for post in base.POSTS] + [base.PREV_EXISTING_URL]
    home_hrefs = re.findall(r'<a href="([^"]+)" class="a-block">', outputs["index.html"] or "")
    if home_hrefs[: len(expected_prefix)] != expected_prefix:
        failures.append(f"homepage prefix mismatch: {home_hrefs[:len(expected_prefix)]}")
    if failures:
        raise SystemExit("\n".join(failures))


def write_outputs(outputs: dict[str, str | None], binary_outputs: dict[str, bytes]) -> None:
    out_dir = Path("/tmp/deepseek-harness-cordis-article-20260816-output")
    if out_dir.exists():
        import shutil

        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for rel, content in outputs.items():
        if content is None:
            continue
        path = out_dir / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    for rel, content in binary_outputs.items():
        path = out_dir / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    print(json.dumps({"local_output": str(out_dir), "text_files": len([v for v in outputs.values() if v is not None]), "binary_files": len(binary_outputs), "deleted": len([v for v in outputs.values() if v is None]), "urls": [post.full_url for post in base.POSTS]}, ensure_ascii=False, indent=2))


def render_asset_check() -> None:
    out_dir = Path("/tmp/deepseek-harness-cordis-article-20260816-output")
    for post in base.POSTS:
        svg = out_dir / f"images/posts/{post.slug}/cover.svg"
        png = Path(f"/tmp/{post.slug}-cover.png")
        subprocess.run(["sips", "-s", "format", "png", str(svg), "--out", str(png)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        probe = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(png)], check=True, stdout=subprocess.PIPE, text=True).stdout
        if "pixelWidth: 1600" not in probe or "pixelHeight: 900" not in probe:
            raise RuntimeError(f"cover render failed: {post.slug}: {probe}")
        for _, dest in SCREENSHOT_SOURCES[post.slug]:
            chart = out_dir / f"images/posts/{post.slug}/{dest}"
            chart_probe = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(chart)], check=True, stdout=subprocess.PIPE, text=True).stdout
            if "pixelWidth: 852" not in chart_probe or "pixelHeight: 480" not in chart_probe:
                raise RuntimeError(f"screenshot dimensions failed: {post.slug}/{dest}: {chart_probe}")


def create_commit(outputs: dict[str, str | None], binary_outputs: dict[str, bytes], ref) -> str:
    entries = []
    for path, content in sorted(outputs.items()):
        if content is None:
            entries.append({"path": path, "mode": "100644", "type": "blob", "sha": None})
            continue
        blob = base.run_gh(["-X", "POST", base.endpoint("git/blobs"), "--input", "-"], {"content": content, "encoding": "utf-8"})
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    for path, content in sorted(binary_outputs.items()):
        blob = base.run_gh(["-X", "POST", base.endpoint("git/blobs"), "--input", "-"], {"content": base64.b64encode(content).decode("ascii"), "encoding": "base64"})
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    tree = base.run_gh(["-X", "POST", base.endpoint("git/trees"), "--input", "-"], {"base_tree": ref.tree_sha, "tree": entries})
    commit = base.run_gh(
        ["-X", "POST", base.endpoint("git/commits"), "--input", "-"],
        {"message": "Publish DeepSeek Harness Cordis article", "tree": tree["sha"], "parents": [ref.commit_sha]},
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
        binary_outputs = collect_binary_outputs()
        card_count, total_pages = rebuild_pagination(outputs)
        refresh_manifest(outputs, binary_outputs)
        validate(outputs, binary_outputs, card_count, total_pages)
        write_outputs(outputs, binary_outputs)
        render_asset_check()
        if base.get_ref().commit_sha != ref.commit_sha:
            continue
        try:
            commit_sha = create_commit(outputs, binary_outputs, ref)
        except RuntimeError as exc:
            if attempt < 2 and "Reference update failed" in str(exc):
                time.sleep(2)
                continue
            raise
        print(json.dumps({"parent": ref.commit_sha, "pushed": commit_sha, "cards": card_count, "pages": total_pages, "urls": [post.full_url for post in base.POSTS]}, ensure_ascii=False, indent=2))
        return
    raise RuntimeError("remote reference changed during all attempts")


if __name__ == "__main__":
    main()
