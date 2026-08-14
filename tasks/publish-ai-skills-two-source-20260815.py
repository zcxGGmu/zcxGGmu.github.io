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
BASE = TASKS / "publish-three-life-business-articles-20260809.py"
spec = importlib.util.spec_from_file_location("publisher", BASE)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = base
spec.loader.exec_module(base)

base.__file__ = __file__
base.DATE = "2026-08-15"
base.BASE_DT = datetime(2026, 8, 15, 6, 10, tzinfo=timezone(timedelta(hours=8)))
base.PREV_EXISTING_URL = "/2026/kingboard-laminates-ai-ccl-fr4-special-glass-revaluation/"
base.PREV_EXISTING_TITLE = "建滔积层板：AI CCL、FR-4 与特种玻纤的重估逻辑"
base.PINNED_PREFIX = [
    "/ai-news-radar/",
    "/2026/codeinsights-local-first-agent-workbench/",
    "/2026/what-you-need-to-learn-from-claw-code-repo/",
    "/2026/gaojingqi-investment-system/",
    "/2026/ai-revolution-permanent-underclass-career-selection/",
    "/2026/live-longer-than-earn-fast-investment-infinite-game/",
]
base.SCRIPT_NAME = Path(__file__).name
base.MANIFEST_NAME = "publish-ai-skills-two-source-20260815-changed-files.json"

BODY_A = r'''
<p>AI 开发工具正在从单项能力的比拼，进入工作系统的比拼。近期活跃的项目横跨局域网文件协作、本地模型训练、技能包、任务编排、知识检索、办公生成和终端编码。它们看似分散，实际上都在补同一个缺口：如何让模型不仅能回答问题，还能在清楚的边界里完成可验证的工作。</p>
<p>面对密集出现的工具，最重要的不是一次性安装四十个项目，而是把它们放回工作流。谁负责提供知识，谁负责执行，谁负责验证，谁保留状态，谁拥有最终批准权，决定了自动化最终是在节省时间，还是扩大返工。下面按能力层次整理一套更可落地的判断框架。</p>

<h2 id="signals">一、七类热点透露出的共同方向</h2>
<p>这轮工具分布覆盖了开发者常见的七个层面：本地数据流动与模型训练，Skills 的可复用知识，Agent 的任务骨架，执行与安全工具，企业知识和办公产物，技能市场，以及终端编码生态。共同趋势不是“更强的聊天”，而是把模型接入文件、终端、网页、知识库、任务队列和审查环节。</p>
<p>因此，选型不应从项目热度开始，而应从待解决的问题开始。高频、低风险、输入输出明确的流程最适合先自动化，例如资料整理、格式转换、测试报告、文档检索和草稿生成。涉及生产写入、对外发送、权限变更或敏感数据时，必须先设计审批、日志和回滚。</p>

<h2 id="local-first">二、本地优先解决数据与算力边界</h2>
<p>局域网文件传输和本地模型微调之所以同时受到重视，是因为它们都试图减少不必要的外部依赖。前者让设备之间直接交换资料，后者通过降低显存压力，让个人开发者能在有限硬件上做实验。两种能力都不等于天然安全：本地网络仍需鉴别设备身份，模型训练仍需检查数据许可、样本质量和硬件余量。</p>
<p>本地优先的真正价值是可控性。数据是否离开设备、过程是否能复现、失败是否能定位，都可以被明确记录。团队落地时应把临时文件、训练数据、模型权重、访问令牌和实验结论分开管理，避免把“离线”误认为“不需要治理”。</p>

<h2 id="skills">三、Skills 要从提示词升级为受管依赖</h2>
<p><a href="https://github.com/anthropics/claude-plugins-official" target="_blank" rel="noopener">anthropics/claude-plugins-official</a> 展示了一个稳定方向：将测试、审查、发布和领域规则组织成可安装、可版本化的能力包。这样做的重点不是把判断外包给工具，而是让每次任务在开始前获得同一套边界、检查项和参考资料。</p>
<p>把 Skills 当作依赖而不是文本片段，可以把治理前移。每个能力包至少应记录来源、版本、权限、允许访问的资源和验证命令；安装前检查其指令是否要求越权访问，升级后复查行为是否变化。涉及文件删除、网络发送、账号操作和密钥读取的动作，应默认增加人工确认。</p>

<h2 id="agent-frameworks">四、Agent 框架的价值是拆解与交接</h2>
<p>多 Agent 系统最容易被误解为“并行调用更多模型”。真正有价值的部分是职责边界：研究角色收集证据，执行角色只拥有完成任务所需的工具，验证角色独立检查结果，协调角色处理依赖和最终交付。没有清楚的输入、输出和验收条件，角色数量只会放大噪声。</p>
<p>并行适合相互独立的检索、测试矩阵、模块开发和输出核查；共享状态、严格时序或高影响动作应顺序执行。每次交接都应保留已验证事实、变更清单、失败原因和下一步，这样长任务才不会因为上下文切换而重新猜测。</p>

<h2 id="execution">五、执行层必须把能力变成受控动作</h2>
<p>模型能推理，并不意味着它天然能可靠执行。一个成熟执行层需要把终端、网页、文件、存储和插件拆成可配置的部件，并对每项动作记录目标、参数、结果和错误。可替换组件能降低锁定风险，但也要求更严格的接口契约和集成测试。</p>
<p>执行权限应分级：只读检索和草稿生成可自动进行；修改文件、提交表单、发送消息和调用付费服务应显式授权；生产数据、资金和密钥相关动作必须设置人工闸门。可靠性来自可停止、可检查和可回滚，而不是无限制地扩大行动范围。</p>

<h2 id="knowledge">六、知识系统的核心是可追溯性</h2>
<p><a href="https://github.com/infiniflow/ragflow" target="_blank" rel="noopener">infiniflow/ragflow</a> 代表的检索增强路线，强调先理解文档、再按证据回答。企业知识系统的质量取决于原始材料、切分策略、权限隔离和引用链，而不是单纯增加模型上下文。对于表格、多栏版面和图片密集资料，解析质量本身就是答案质量的一部分。</p>
<p>图谱、记忆和可问责机制应服务于同一个目标：每个关键结论都能回到来源。无法查到依据时，系统应明确不确定性，而不是补全看似合理的内容。长期运行还需要失效时间和纠错机制，避免旧决策被误当成永久知识。</p>

<h2 id="office">七、生成办公产物时，可编辑性比一次成型更重要</h2>
<p><a href="https://github.com/gitbrent/PptxGenJS" target="_blank" rel="noopener">gitbrent/PptxGenJS</a> 这类程序化演示文稿工具的意义，在于把重复页面、品牌母版和数据图表纳入版本控制。自动生成可以显著缩短从零到一的时间，但不能取代对信息结构、图表口径、文字溢出和视觉层级的复核。</p>
<p>对报告、表格和演示稿的验收至少应包括三层：文件能否在目标软件打开，数据与引用是否可核对，内容是否仍能被人编辑。把输出锁成一张图会掩盖错误，也会增加后续维护成本；可编辑、可追溯、可复跑，才是办公自动化真正应保留的资产。</p>

<h2 id="skill-market">八、技能市场需要供应链视角</h2>
<p>自我改进、主动提醒、结构化记忆、代码托管操作、办公套件连接、天气和多源搜索等能力，能够快速扩展 Agent 的覆盖面，也会扩大供应链和权限风险。下载量可以反映需求，却不能证明其指令安全、依赖可信或适合生产。</p>
<p>推荐建立固定的接入流程：先在隔离环境检查内容与依赖，再以最小权限试运行；为读写边界、外部网络、账号授权和数据留存分别做审查；最后用真实小样本衡量成功率、耗时、成本和失败模式。高风险能力即使通过自动扫描，也应保留人工审计。</p>

<h2 id="codex">九、终端编码的关键是工程闭环</h2>
<p><a href="https://github.com/openai/codex" target="_blank" rel="noopener">openai/codex</a> 把代码阅读、编辑和命令执行放进连续工作环境中。它带来的价值不是跳过工程流程，而是让读取约束、提出最小变更、运行验证和解释差异可以在同一条链路完成。工具越接近代码库和部署环境，越需要清楚记录实际执行过的命令。</p>
<p>团队应把编码自动化嵌回已有质量机制：受影响测试、静态检查、依赖和密钥扫描、代码审查、变更说明与回滚方案缺一不可。自动评审可提高覆盖率，却不能替代合并责任；最终决策仍需要结合业务上下文、架构边界和风险承受能力。</p>

<h2 id="adoption">十、从一条可回滚流程开始采用</h2>
<p>个人使用时，可以先选择一条只读或低风险流程：整理资料、生成测试清单、汇总日志、输出可编辑的演示稿草稿。团队使用时，应优先补齐权限模型、审计日志、密钥管理、成本监控和事故回滚。只有这些基础设施可用，更多 Skills 和 Agent 才会带来复利。</p>
<p>评估时不要只问“能不能跑”，还要问“失败后会怎样”：是否可解释，是否能中止，是否保留证据，是否能恢复到上一状态，谁来批准对外动作。把这些问题写进验收标准，才会让热度转化为可持续的生产能力。</p>

<h2 id="evaluation">十一、评估不能只看星标和演示效果</h2>
<p>每项候选能力都应经过小样本验证。先写出成功定义，例如知识检索是否给出可用引用、代码修改是否通过受影响测试、文档生成是否能在目标软件中打开；再记录单次耗时、模型和工具成本、人工修订时间、失败率与重试次数。没有指标的“效率提升”很容易只是把工作从执行阶段转移到返工阶段。</p>
<p>验证样本也要包含异常：缺少字段的文档、超长输入、权限不足、网络超时、重复请求和不可解析页面。系统若只能在理想输入上工作，就不具备生产价值。将失败样本沉淀为回归用例，才能判断新版本和新 Skill 是否真的提高了可靠性。</p>

<h2 id="operations">十二、运行期需要可观测性和交接记录</h2>
<p>上线后的重点是可观测性。每次运行应保留输入版本、所用工具和模型、关键参数、耗时、成本、输出位置、验证结论和人工决定。对长链路任务，阶段性摘要比完整聊天记录更有用：当前完成了什么、依据是什么、下一步依赖什么、已知风险是什么。</p>
<p>这种记录让系统能够被接手、复跑和审计。当模型、人员或执行环境变化时，团队不必重新猜测历史决策。对于定时流程，还应配置告警阈值和停用开关，避免低质量输出在无人值守时持续积累。</p>

<h2 id="architecture">十三、组合能力时先定义接口，再追求自主</h2>
<p>Skills、框架、检索、记忆和终端工具并非彼此替代，而是不同层的组件。较稳妥的组合方式是先定义每层输入输出：知识层返回带来源的材料，规划层产出可验证步骤，执行层返回动作日志，验证层给出通过或失败证据，协调层保留最终决策。接口清楚以后，组件才能被独立替换和测试。</p>
<p>自主程度应随证据增长，而不是随功能数量增长。先让系统在只读任务上持续通过验证，再扩展到低风险写入，最后才评估更高影响的自动化。把权限扩大与指标、审计和回滚绑定，能让能力增长不以失控为代价。</p>

<h2 id="conclusion">十四、结论：工具密度需要治理密度</h2>
<p>从本地数据、Skills、Agent 框架到知识检索、办公生成和终端编码，AI 工具正在补齐真实工作的不同环节。成熟的系统并不是功能最多的系统，而是能把能力、权限、状态、验证和责任组织起来的系统。先让一个小闭环稳定、可测、可回滚，再逐步扩大自动化范围，才能真正获得长期效率。</p>
'''

BODY_B = r'''
<p>重复操作往往不是因为任务困难，而是因为流程只存在于人的记忆里：打开页面、筛选信息、复制到表格、补充说明、发出结果。若把这些动作直接照抄为脚本，页面变化、数据量增加和异常条件很快就会让脚本失效。更有价值的路径，是先从人的示范中提取任务目标、判断条件和可调用工具，再将它们整理成可审查的 Skill。</p>
<p><a href="https://github.com/microsoft/skill-recorder" target="_blank" rel="noopener">microsoft/skill-recorder</a> 聚焦的正是这一步：记录一次真实操作和必要的口头判断，分析后形成可以修改、复用并交给 Agent 调用的工作说明。它不是鼠标轨迹回放器，而是尝试把行为背后的目标转成可泛化的执行步骤。</p>

<h2 id="problem">一、重复操作的难点不在点击，而在判断</h2>
<p>很多日常流程包含隐含判断：先看哪些任务尚未处理，只保留符合条件的数据，发送前再核对结果。若只保存坐标和点击顺序，流程一旦遇到不同页面、不同数据量或不同窗口布局，就容易失效。能够复用的自动化需要表达“为什么做这一步”，而不仅是“当时点了哪里”。</p>
<p>示范式记录让操作者在执行时补充判断依据，后续分析再将画面、窗口切换、页面访问与说明组合起来。得到的产物更接近任务说明书：目标是什么，输入在哪里，条件如何判断，结果写向何处，哪些环节需要确认。</p>

<h2 id="record">二、记录阶段应保留必要信息，而非无差别采集</h2>
<p>一次录制可以覆盖应用打开、窗口切换、页面访问和少量剪贴板预览，同时允许补充文字或语音说明。高质量示范的原则是只做目标流程，不夹杂无关浏览、私人对话和临时试错；必要判断应说清筛选条件、例外情况和完成标准。</p>
<p>录制并不等于安全。窗口标题、地址、剪贴板和屏幕内容都可能包含敏感信息。开始前应关闭密码管理器、密钥页面、客户资料和内部文档，并确认剪贴板没有遗留令牌或隐私数据。能在本地完成的捕获应保留在本地，后续分析前再明确哪些材料会被发送。</p>

<h2 id="analysis">三、分析结果必须先被人审阅</h2>
<p>分析阶段的目标是归纳任务和步骤，而非直接授权执行。操作者应先检查生成结果：任务目标是否被正确理解，条件是否遗漏，是否混入无关动作，外部写入是否被标出。错误的步骤可以修改，偶发的操作可以删除，无法解释的结论应退回重新示范。</p>
<p>这一步是从“记录行为”走向“形成能力”的分界线。人类示范常带有临时习惯和环境噪声，只有经过审阅的流程才值得沉淀。对于会影响文件、消息、表单或外部系统的步骤，审阅者还应明确前置条件、失败处理和回滚方式。</p>

<h2 id="abstraction">四、可复用 Skill 要抽象目标，而不是复刻轨迹</h2>
<p>网页操作的价值在于可以被更稳定的工具调用替代。例如，查看代码托管平台的待处理问题、回复评论和添加标签，可以被整理为读取问题、创建评论和修改标签等语义动作。这样，后续任务不必重复打开页面和点击固定位置，也能适应新的问题编号和数据数量。</p>
<p>抽象后仍需验证工具契约：Agent 是否真的拥有对应的命令、API 和权限，参数含义是否一致，读操作与写操作是否被区分。不同 Agent 的工具名、认证方式和执行模型并不相同，Skill 不能未经检查就跨环境复制。</p>

<h2 id="generalize">五、泛化能力来自数据结构，而不是一次示范</h2>
<p>以价格记录为例，一次示范可能只处理一条数据，但成熟的步骤应描述“读取页面上的所有目标条目、提取价格字段、写入表格的指定列”，而不是绑定某个具体位置。这样页面出现多条数据时，任务仍能按相同规则扩展。</p>
<p>泛化也需要边界。页面结构变化、字段缺失、单位异常、重复数据和网络失败都应有明确处理策略。最稳妥的第一版只处理可识别的正常情况，把异常输出为待人工确认清单；在积累真实失败样本后，再逐步扩展规则。</p>

<h2 id="automation">六、Skill 与定时自动化是两种不同责任</h2>
<p>Skill 通常由人主动调用，适合需要即时判断的工作；定时或条件触发的自动化则会在无人操作时运行，适合每日汇总、例行检查和提醒。后者的影响范围更大，因此必须额外设计运行时机、失败通知、幂等性和人工暂停开关。</p>
<p>若录制过程没有包含运行时间，系统给出的时间安排应被视为建议，而不是默认授权。任何对外发送、批量写入或可能产生费用的自动化，都应在启用前由负责人确认，并在初期保留人工复核。</p>

<h2 id="write-boundaries">七、读写边界要在发布前显式标注</h2>
<p>读取资料、筛选数据和计算结果通常不改变外部状态；发送消息、修改文件、提交表单和更新标签则会产生可见影响。把这两类动作混在一起，是自动化事故最常见的来源之一。每项写操作都应单独显示目标、参数、预期结果和撤销路径。</p>
<p>实际执行时应采用最小权限：只给当前流程所需的仓库、文档或表格访问范围；为高影响动作增加二次确认；为批量写入设置上限和预览。日志要能回答谁在何时以何种权限做了什么，而不仅是“任务运行成功”。</p>

<h2 id="fit">八、适用场景取决于是否存在可调用接口</h2>
<p>网页、表格、邮件、日历和开发工具通常拥有命令、API 或 Agent 工具，因此更适合从示范中转成可靠的 Skill。相比之下，纯图形界面、封闭软件或依赖实时视觉判断的环境，往往缺少稳定的执行接口；即使能够总结步骤，也未必能安全完成执行。</p>
<p>尤其要避免把这类能力误用于违反服务规则的自动控制。技术上可记录某些界面，不等于可以绕过平台限制或模拟人类行为。评估时应同时检查目标系统的条款、账号风险和可用接口，而不是只看能否识别屏幕内容。</p>

<h2 id="privacy">九、隐私与数据流向必须先于效率</h2>
<p>屏幕捕获、地址片段、剪贴板预览、语音说明和提取图像一旦进入云端分析，就可能构成敏感数据外发。组织应为录制定义禁止内容清单，配置脱敏规则，并在分析前让操作者清楚知道数据会被何种服务处理、保存多久、谁可以访问。</p>
<p>对于客户资料、内部财务、身份信息和密钥，默认策略应是排除而不是事后清理。若业务确实需要处理敏感内容，应优先寻找隔离环境、私有部署或经过审批的数据通道，并保留审计记录。</p>

<h2 id="adoption">十、落地方法：从一项低风险流程验证</h2>
<p>开始时选择一项可观察、可回滚、影响范围小的流程，例如把公开页面的固定字段整理到草稿表格，或生成待处理事项摘要。先由人完整示范并审阅生成的 Skill，再在少量真实样本上比较人工和自动结果，记录准确率、耗时、异常和人工接管次数。</p>
<p>当流程连续稳定后，再增加条件触发、更多数据量和受控写入。每次扩展都应重新检查权限、失败通知、成本和数据边界。示范可以缩短把经验转成能力的时间，但可靠运行仍依赖清晰的约束、验证和负责人。</p>

<h2 id="testing">十一、为生成的 Skill 写一组验收样本</h2>
<p>一份 Skill 在进入日常使用前，应至少用正常、空值、重复值、字段缺失和权限不足等样本测试。验收结果不应停留在“运行成功”，而要核对目标数据是否读取完整、筛选规则是否正确、写入位置是否准确、异常是否被明确报告。对于包含写操作的流程，先使用草稿目标或测试账号，确认无误后再接入真实系统。</p>
<p>测试也能暴露示范中的隐含假设。例如某一步是否依赖固定页面顺序，是否默认数据只有一条，是否把临时命名当成恒定规则。把这些假设写成前置条件或显式分支，Skill 才能从个人习惯变成可交接的团队资产。</p>

<h2 id="maintenance">十二、工作流需要版本和变更管理</h2>
<p>页面、API、表格字段和业务规则都会变化，因此生成后的 Skill 不应被视为一次性产物。每次修改应记录版本、修改原因、适用环境和验证证据；重要变更需要小范围灰度运行，出现异常时能够快速回到上一稳定版本。把工作流放入版本控制，也方便团队审查权限与逻辑差异。</p>
<p>维护责任同样需要明确。谁负责检查上游接口变化，谁接收失败通知，谁有权批准新的写操作，谁负责定期复核数据留存，必须在自动化启用前写清楚。缺少责任人的流程往往不是自动化，而是被延迟发现的风险。</p>

<h2 id="measurement">十三、用业务结果衡量是否值得自动化</h2>
<p>自动化的价值不是录制次数，而是可量化地减少了什么：人工处理时间、遗漏率、等待时间、重复录入或响应延迟。还要统计新增成本，例如模型调用、运行环境、维护、审阅和异常处理。只有把收益和代价放在同一张表里，才能决定应当扩大、保持还是停止一条流程。</p>
<p>最好的长期状态不是完全去掉人，而是让人从机械搬运转向规则设计、异常判断和结果负责。Skill 将经验转成可调用单元，负责人继续用真实反馈修正它，两者形成的闭环才会随时间变得更可靠。</p>

<h2 id="conclusion">十四、结论：把经验沉淀为可审查的工作单元</h2>
<p>从真实操作中生成 Skill 的价值，不是把每一次点击机械复制，而是把目标、判断、工具和责任组织成可编辑的工作单元。好的自动化应能说明它准备做什么、为什么这样做、哪些动作会改变外部状态，以及出现异常时如何停止。以低风险流程开始、审阅每次抽象、保留人为批准，才能让重复劳动真正转化为长期可控的效率。</p>
'''

base.POSTS = [
    base.Post(
        slug="ai-skills-agent-fullstack-open-source-daily-20260814",
        title="8月14日 AI Skills/Agent 全栈开源项目速览：把工具热度接进可验证的工作流",
        desc="从 Skills、Agent 框架、知识检索到终端编码，梳理 AI 工具如何在权限、验证与回滚边界内形成稳定工作系统。",
        category="AI工具",
        series="AI Agent",
        tags=["AI Skills", "AI Agent", "开源项目", "GitHub", "Codex", "Agent框架", "工作流", "软件工程"],
        minutes=15,
        body=BODY_A,
        accent=("#0f172a", "#0f766e", "#b45309"),
        required=["Skills", "Agent", "验证", "权限", "Codex", "知识", "回滚"],
        minimum=3500,
    ),
    base.Post(
        slug="skill-recorder-from-demonstration-to-reusable-agent-workflows",
        title="Skill Recorder：把一次真实操作沉淀成可审查的 Agent 工作流",
        desc="从操作示范、任务抽象、权限边界到定时自动化，拆解如何把重复劳动转化为可编辑、可验证的 Skills。",
        category="AI工具",
        series="AI Agent",
        tags=["AI Skills", "自动化", "GitHub", "Copilot", "工作流", "Agent框架"],
        minutes=10,
        body=BODY_B,
        accent=("#111827", "#2563eb", "#047857"),
        required=["Skill", "自动化", "权限", "审阅", "Agent", "隐私", "验证"],
        minimum=3400,
    ),
]

FORBIDDEN = ["B站", "bilibili", "Bilibili", "哔哩", "UP主", "up主", "原视频", "视频中", "视频里", "音频中", "音频里", "本期", "这期", "观看", "点赞", "投币", "收藏", "订阅", "关注", "三连", "BV1"]
EXPECTED_LINKS = {
    "ai-skills-agent-fullstack-open-source-daily-20260814": {
        "https://github.com/anthropics/claude-plugins-official",
        "https://github.com/infiniflow/ragflow",
        "https://github.com/gitbrent/PptxGenJS",
        "https://github.com/openai/codex",
    },
    "skill-recorder-from-demonstration-to-reusable-agent-workflows": {
        "https://github.com/microsoft/skill-recorder",
    },
}
PAGE_SIZE = 10
active_ref = None


def get_file_at_active_ref(path: str) -> str | None:
    if active_ref is None:
        raise RuntimeError("active remote ref is not set")
    try:
        data = base.run_gh([base.endpoint(f"contents/{quote(path, safe='/')}?ref={active_ref.commit_sha}")])
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


def update_home_after_pinned(text: str) -> str:
    for post in base.POSTS:
        text = base.strip_home_card(text, post.url_path)
    matches = list(re.finditer(r'<a href="[^"]+" class="a-block">.*?</a>', text, re.S))
    pinned_last = base.PINNED_PREFIX[-1]
    target = next((match for match in matches if card_href(match.group(0)) == pinned_last), None)
    if target is None:
        raise RuntimeError("final pinned homepage card is missing")
    block = "\n".join(base.home_card(post) for post in base.POSTS) + "\n"
    return text[:target.end()] + "\n" + block + text[target.end():]


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
    cards = cards_from(template)
    previous_pages = 1
    for page in range(2, 100):
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
    total = (len(cards) + PAGE_SIZE - 1) // PAGE_SIZE
    if total < 2:
        raise RuntimeError("expected multiple pagination pages")
    outputs["index.html"] = page_html(template, cards[:PAGE_SIZE], 1, total)
    for page in range(2, total + 1):
        outputs[f"page/{page}/index.html"] = page_html(template, cards[(page - 1) * PAGE_SIZE:page * PAGE_SIZE], page, total)
    for page in range(total + 1, previous_pages + 1):
        outputs[f"page/{page}/index.html"] = None
    return len(cards), total


def validate_cover_rendering(outputs: dict[str, str | None]) -> None:
    output_root = Path("/tmp/three-life-business-articles-20260809-publish-output")
    for post in base.POSTS:
        svg = output_root / f"images/posts/{post.slug}/cover.svg"
        png = Path(f"/tmp/{post.slug}-cover.png")
        subprocess.run(["sips", "-s", "format", "png", str(svg), "--out", str(png)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        probe = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(png)], check=True, stdout=subprocess.PIPE, text=True).stdout
        if "pixelWidth: 1600" not in probe or "pixelHeight: 900" not in probe or png.stat().st_size < 4096:
            raise RuntimeError(f"{post.slug}: cover PNG rendering failed: {probe.strip()}")


def remote_file(path: str, commit_sha: str) -> str:
    data = base.run_gh([base.endpoint(f"contents/{quote(path, safe='/')}?ref={commit_sha}")])
    return base64.b64decode(data["content"]).decode("utf-8")


def verify_remote_publish(commit_sha: str, expected_cards: int, total_pages: int) -> None:
    tree = base.run_gh([base.endpoint(f"git/trees/{commit_sha}?recursive=1")])["tree"]
    paths = {entry["path"] for entry in tree}
    if any("__pycache__" in path for path in paths):
        raise RuntimeError("remote tree includes __pycache__")
    rss = remote_file("index.xml", commit_sha)
    home = remote_file("index.html", commit_sha)
    cards: list[str] = []
    for page in range(1, total_pages + 1):
        path = "index.html" if page == 1 else f"page/{page}/index.html"
        if path not in paths:
            raise RuntimeError(f"remote pagination page missing: {path}")
        cards.extend(re.findall(r'<a href="([^"]+)" class="a-block">', remote_file(path, commit_sha)))
    if len(cards) != expected_cards or len(cards) != len(set(cards)) or "/page/0/" in home:
        raise RuntimeError("remote pagination coverage failed")
    for post in base.POSTS:
        article_path = f"2026/{post.slug}/index.html"
        if article_path not in paths:
            raise RuntimeError(f"remote article missing: {article_path}")
        article = remote_file(article_path, commit_sha)
        if post.title not in article or post.full_url not in rss:
            raise RuntimeError(f"remote article or RSS verification failed: {post.slug}")

    for _ in range(12):
        try:
            build = base.run_gh([base.endpoint("pages/builds/latest")])
            error = build.get("error") or {}
            error_message = error.get("message") if isinstance(error, dict) else error
            if build.get("commit") == commit_sha and build.get("status") == "built" and not error_message:
                return
            if build.get("commit") == commit_sha and error_message:
                raise RuntimeError(f"GitHub Pages build failed: {error_message}")
        except RuntimeError as exc:
            if "Not Found" not in str(exc):
                raise
        time.sleep(5)
    raise RuntimeError("GitHub Pages build did not reach built state for published commit")


def validate(outputs: dict[str, str | None]) -> None:
    base.validate(outputs)
    for post in base.POSTS:
        article = outputs[f"2026/{post.slug}/index.html"]
        cover = outputs[f"images/posts/{post.slug}/cover.svg"]
        body = re.search(r'<div class="post-body" v-pre>(.*?)</div></div><nav', article, re.S)
        if body is None:
            raise SystemExit(f"{post.slug}: body missing")
        links = set(re.findall(r'https://github\.com/[^"<]+', body.group(1)))
        if links != EXPECTED_LINKS[post.slug]:
            raise SystemExit(f"{post.slug}: GitHub link coverage mismatch: {sorted(links)}")
        forbidden = [word for word in FORBIDDEN if word in article or word in cover]
        if forbidden:
            raise SystemExit(f"{post.slug}: forbidden wording: {forbidden}")

    cards = []
    for path in ["index.html", *sorted(path for path, content in outputs.items() if content is not None and re.fullmatch(r"page/\d+/index\.html", path))]:
        cards.extend(re.findall(r'<a href="([^"]+)" class="a-block">', outputs[path] or ""))
    if len(cards) != len(set(cards)):
        raise SystemExit("pagination duplicates cards")
    if "/page/0/" in outputs["index.html"]:
        raise SystemExit("homepage pagination contains page 0")
    home_cards = re.findall(r'<a href="([^"]+)" class="a-block">', outputs["index.html"])
    expected = base.PINNED_PREFIX + [post.url_path for post in base.POSTS]
    if home_cards[:len(expected)] != expected:
        raise SystemExit(f"homepage prefix mismatch: {home_cards[:len(expected)]}")


def create_commit(outputs: dict[str, str | None], ref) -> str:
    entries = []
    for path, content in sorted(outputs.items()):
        if content is None:
            entries.append({"path": path, "mode": "100644", "type": "blob", "sha": None})
            continue
        blob = base.run_gh(["-X", "POST", base.endpoint("git/blobs"), "--input", "-"], {"content": content, "encoding": "utf-8"})
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    tree = base.run_gh(["-X", "POST", base.endpoint("git/trees"), "--input", "-"], {"base_tree": ref.tree_sha, "tree": entries})
    commit = base.run_gh(
        ["-X", "POST", base.endpoint("git/commits"), "--input", "-"],
        {"message": "Publish AI Skills articles 2026-08-15", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    base.run_gh(["-X", "PATCH", base.endpoint(f"git/refs/heads/{base.BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


def main() -> None:
    global active_ref
    for attempt in range(3):
        ref = base.get_ref()
        active_ref = ref
        base.get_file = get_file_at_active_ref
        base.update_home = update_home_after_pinned
        outputs = base.collect_outputs()
        card_count, total_pages = rebuild_pagination(outputs)
        outputs[f"tasks/{base.MANIFEST_NAME}"] = json.dumps(sorted(path for path, content in outputs.items() if content is not None), ensure_ascii=False, indent=2)
        validate(outputs)
        base.write_outputs({path: content for path, content in outputs.items() if content is not None})
        validate_cover_rendering(outputs)
        if base.get_ref().commit_sha != ref.commit_sha:
            continue
        try:
            commit_sha = create_commit(outputs, ref)
        except RuntimeError as exc:
            if attempt < 2 and "Reference update failed" in str(exc):
                time.sleep(2)
                continue
            raise
        current = base.get_ref().commit_sha
        if current != commit_sha:
            comparison = base.run_gh([base.endpoint(f"compare/{commit_sha}...{current}")])
            if comparison.get("status") != "ahead":
                raise RuntimeError("published commit is not an ancestor of current remote head")
        verify_remote_publish(commit_sha, card_count, total_pages)
        print(json.dumps({"parent": ref.commit_sha, "pushed": commit_sha, "files": len(outputs), "cards": card_count, "pages": total_pages, "urls": [post.full_url for post in base.POSTS]}, ensure_ascii=False))
        return
    raise RuntimeError("remote reference changed during all publication attempts")


if __name__ == "__main__":
    main()
