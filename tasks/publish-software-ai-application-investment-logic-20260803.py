from __future__ import annotations

import html
import importlib.util
import json
import os
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.dont_write_bytecode = True

ROOT_HINT = Path("/tmp/blog-publish-bv1rk-20260803.path")
ROOT = Path(os.environ.get("BLOG_ROOT") or ROOT_HINT.read_text(encoding="utf-8").strip())
BASE_PATH = Path(__file__).with_name("publish-physical-ai-three-article-batch.py")
if not BASE_PATH.exists():
    BASE_PATH = ROOT / "tasks" / "publish-physical-ai-three-article-batch.py"

spec = importlib.util.spec_from_file_location("base_publisher_software_ai", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Unable to load base publisher: {BASE_PATH}")
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
_BASE_VALIDATE = base.validate


BODY = """
<p><img src="/images/posts/software-ai-application-investment-logic-agent-custom-software/cover.svg" alt="软件与 AI 应用投资逻辑：从大模型商业化到 Agent 和定制软件"></p>
<p>软件和 AI 应用的投资逻辑，不能只看模型排行榜，也不能只看某个应用短期下载量。更关键的问题是：模型能力怎样转化为可收费的软件，软件怎样嵌入企业流程，企业为什么愿意为效率提升付费，哪些环节会被模型压缩，哪些环节反而因为 AI 获得更高价值。</p>
<p>大模型商业化大致有两条路径。一条是卖 API、卖算力、卖基础模型能力，收入像云服务一样按调用量增长；另一条是把模型能力包装成软件、工作流和行业解决方案，直接替代或增强企业里的具体岗位、流程和产出。两者对应的市场空间和估值逻辑完全不同。卖 API 是基础设施生意，卖软件是应用和客户价值生意。</p>
<p>真正的变化从 AI 编程开始变得清晰。模型从“会回答问题”升级到“能用代码解决问题”，再进一步进入办公、分析、素材、广告、电商、行业软件和定制开发。这个过程不是单点爆发，而是一条时间线：模型能力先提升，开发者工具先验证付费，软件公司随后被重估，最后才进入企业内部工作流和行业交付。</p>

<h2 id="timeline">一、时间线：AI 软件化从编程能力开始</h2>
<p>2025 年上半年是一个关键起点。海外模型厂商连续推出更强的推理和编程模型，开发者工具完成大额融资，AI 编程助手开始从尝鲜工具变成开发者日常工作入口。这个阶段的核心信号不是某个模型参数提高了多少，而是模型开始具备“理解需求、拆解任务、调用工具、生成代码、修复错误”的闭环能力。</p>
<p>编程之所以重要，是因为代码是连接数字世界和企业流程的通用工具。一个模型如果只能写文案，商业化范围会受内容场景限制；如果能写代码，它就能参与数据处理、报表生成、自动化脚本、内部工具、接口调用、业务分析和软件定制。代码能力让模型不再只是聊天界面，而是解决问题的执行层。</p>
<p>随后，国内模型也开始强化长思考、工具调用和编程能力。模型从单纯回答问题，转向用代码、检索、表格、流程和插件完成任务。软件行业的分界线由此出现：能否把模型能力变成稳定可交付的工作流，成为判断应用价值的核心。</p>

<h2 id="api-vs-software">二、API 收入和软件收入不是一回事</h2>
<p>基础模型卖 API，本质上是把智能能力按调用量出售。它的优点是规模大、边际成本下降快、开发者生态容易扩张；缺点是价格竞争明显，模型同质化后，单位调用价格会持续下行。基础模型会越来越像云计算、水电和网络，是企业数字化的新底座。</p>
<p>软件收入则不同。企业购买软件，买的不是某一次模型调用，而是一个流程、权限、数据结构、协作界面、审计机制和组织习惯。软件嵌入越深，迁移成本越高，客户越愿意为稳定性、安全性和持续服务付费。</p>
<p>因此，AI 应用的估值不能简单按 token 调用量推算。一个模型 API 可以生成一段代码，但企业真正付钱的可能是完整的研发工作台、需求管理、代码审查、测试部署、权限控制和私有化交付。基础模型创造能力，软件把能力变成可持续收入。</p>
<p>这也是软件公司仍然有位置的原因。模型厂商可以提供通用能力，却不一定愿意深入每个客户的组织结构、历史系统、权限规则和交付细节。企业客户购买的是“少出错、可追责、能审计、能连续运行”的结果，而不是一次聪明回答。模型越强，越需要软件把它约束在可管理的边界里。</p>

<h2 id="software-repricing">三、AI 会压低一部分软件价格，也会抬高另一部分软件价值</h2>
<p>AI 出现后，很多传统软件首先感受到的是价格压力。用户会问：既然模型可以生成表格、做分析、写文案、写脚本，为什么还要为老牌软件支付高昂年费？一些试用转化、咨询服务和效率工具，都会先被这种心理冲击。</p>
<p>但这不代表软件行业整体失去价值。真正被压缩的，是功能单薄、数据不深、流程不复杂、替换成本低的工具。真正变得更有价值的，是掌握客户数据、行业流程、协作关系、权限体系和交付能力的软件。AI 会让“单点功能”便宜，却会让“端到端解决问题的系统”更重要。</p>
<p>办公软件、协同工具、行业垂直软件和企业管理系统，都有机会通过 AI 重新升级。关键不是在界面上加一个聊天框，而是让模型进入真实流程：自动写文档、整理会议、生成素材、分析经营数据、调用内部系统、完成审批建议、辅助客服和销售跟进。软件价值从“提供按钮”转向“完成任务”。</p>

<h2 id="coding-tools">四、AI 编程工具验证了第一轮真实付费</h2>
<p>AI 编程工具是最早跑出商业化斜率的方向。原因很直接：开发者付费能力强，效率提升可以被感知，模型生成结果可以通过编译、测试和运行来验证。相比纯文本应用，代码场景更容易形成闭环，也更容易证明 ROI。</p>
<p>Cursor、Claude Code 以及类似工具的快速增长，说明模型能力一旦进入专业工作流，就不只是娱乐性应用。开发者不只是让模型写几行代码，而是把它当成需求拆解、代码生成、调试、重构和自动化任务的助手。</p>
<p>这也给其他软件方向提供了样板。AI 应用要真正收费，最好具备三个条件：任务高频、结果可验证、节省成本足够明确。编程满足这三个条件，所以率先爆发。后续办公、数据分析、法务、财务、设计、电商素材和行业软件，也要沿着同样标准判断。</p>

<h2 id="domestic-work-assistant">五、国内工作助手：先抢通用办公入口</h2>
<p>国内市场出现的通用工作助手，本质上是在复刻 AI 编程工具的路径，只是从代码场景扩展到普通白领工作。它们试图承接搜索、写作、表格、PPT、文档、素材、日程、知识库和简单数据分析等需求，让用户在一个入口里完成更多工作。</p>
<p>这类产品的优势是用户基数大、上手门槛低、传播速度快。问题也很明显：通用办公需求很广，但单个任务付费意愿未必高。大量用户会试用，真正愿意长期付费的人群，可能集中在一二线城市写字楼、内容生产者、市场销售、咨询分析和中小企业主。</p>
<p>因此，通用工作助手的关键不是日活数字本身，而是能否把免费使用转化为高频刚需，再进一步进入企业账户、团队协作和私有数据。只有完成从个人工具到组织流程的迁移，收入质量才会明显改善。</p>

<h2 id="installed-software">六、中国软件的特殊性：本地部署和数据安全</h2>
<p>中国企业软件和海外 SaaS 有一个显著差异：本地部署、私有化部署和项目制交付比例更高，纯按月续费 SaaS 占比相对低。这会带来两面影响。</p>
<p>一方面，本地部署让软件公司升级 AI 的难度更大。数据分散在客户现场，版本复杂，接口标准不统一，部署和运维成本高。模型要进入企业流程，不只是调用 API，还要解决权限、数据安全、网络环境、合规和历史系统兼容。</p>
<p>另一方面，本地部署也保护了软件公司的客户关系。企业的财务、人事、供应链、生产、客户和经营数据，不会轻易交给外部通用模型。掌握客户现场、行业知识和交付经验的软件公司，反而有机会成为模型进入企业的桥梁。AI 不是简单替代企业软件，而是需要通过企业软件进入真实数据和流程。</p>

<h2 id="custom-software">七、定制软件开发会被重构，而不是消失</h2>
<p>定制软件原来是一门人力密集型生意。客户提出需求，服务商派项目经理、架构师、开发、测试和实施团队，按人天、项目或维护费收费。问题在于成本高、周期长、质量不稳定，很多客户也不想长期养大规模开发团队。</p>
<p>AI 编程会改变这条链。前期仍然需要有经验的人理解业务、梳理需求、设计架构、确认数据接口和安全边界；但中后期大量代码生成、页面搭建、测试脚本、文档整理和简单迭代，都可以被模型加速。结果是交付团队人数减少，项目周期缩短，单位项目毛利有机会改善。</p>
<p>这不是“所有程序员都被替代”，而是分工改变。真正稀缺的人会从写重复代码，转向需求定义、系统设计、业务理解、客户沟通和交付负责。定制软件公司如果只是卖人头，会被 AI 压缩；如果能把行业模板、低代码平台、模型能力和交付经验沉淀为产品，就会获得新的价值。</p>

<h2 id="agent-model">八、Agent 和模型不是零和关系</h2>
<p>市场经常担心一个问题：如果模型越来越强，Agent 和应用是否会被模型吃掉。这个问题不能简单回答。模型和 Agent 的关系，更像基础能力和工程化产品的关系。模型能力越强，Agent 能做的事情越多；但企业要真正使用，还需要权限、工具、流程、记忆、评测、审计和异常处理。</p>
<p>Agent 的本质不是一个神秘新物种，而是一套工程系统：把目标拆成步骤，把步骤交给模型或工具执行，把结果反馈回来，再根据约束继续推进。它和软件编程里的工程逻辑非常相似。模型负责智能密度，Agent 负责把智能装进可运行流程。</p>
<p>因此，Agent 和模型不是必然对立。真正容易被模型吞掉的是薄封装应用：只是套壳、没有数据、没有流程、没有客户粘性。真正有价值的 Agent，会深度绑定企业系统、业务规则、行业数据和执行结果。模型越强，它反而越能交付复杂任务。</p>
<p>一个可用的企业 Agent 至少要解决四件事。第一，知道能调用哪些系统，不能越权。第二，知道任务完成到什么程度才算合格。第三，知道失败时如何停止、回滚或交给人工。第四，能把每一步执行过程留痕。没有这些工程约束，Agent 只是演示；具备这些约束，Agent 才可能成为企业软件的新交互层。</p>

<h2 id="capex-return">九、资本开支回报：大模型正在成为基础服务</h2>
<p>市场对 AI 资本开支的核心担忧，是投入巨大但短期回报不清晰。芯片、数据中心、训练、推理和人才成本都很高，如果只靠聊天会员收入和 API 降价，商业模型会承受压力。</p>
<p>更长期的逻辑是，大模型有机会成为企业基础服务。过去企业需要电、网络、云计算、数据库和办公软件；未来还会需要模型能力。它可能不会只由一家供应商提供，也不会只有一个价格体系，而是形成基础模型、私有模型、行业模型、端侧模型和企业工作流的多层市场。</p>
<p>资本开支能否兑现，最终取决于模型是否进入足够多的真实场景。编程、办公、客服、营销、广告、电商、财务、法务、研发、数据分析、工业设计和定制软件，都是把算力投入转化为收入的出口。只要应用层持续扩张，基础设施投入就有回收路径。</p>

<h2 id="video-generation">十、文生视频和素材生产正在打开第二条应用曲线</h2>
<p>除了编程和办公，文生图、文生视频、数字人、广告素材和电商内容，是另一条重要应用曲线。它们不一定需要非常复杂的推理，但能直接连接内容生产、广告投放、电商转化和品牌营销。</p>
<p>这一类应用的商业价值在于“可变现的内容供给”。商家需要大量商品图、短视频、直播素材、广告片段和投放版本。过去这些内容依赖摄影、剪辑、设计和运营团队，成本高、周期长、迭代慢。生成式工具让素材生产变成低成本高频流程。</p>
<p>如果平台能够把生成工具、素材管理、投放系统、电商转化和数据反馈连接起来，就不只是娱乐工具，而是商业增长工具。它创造的是广告预算、商家服务费和电商经营效率，而不是单纯的模型调用收入。</p>

<h2 id="investment-map">十一、投资图谱：三条主线同时展开</h2>
<p>第一条主线是基础模型和云基础设施。它看的是算力投入、推理成本、模型能力、生态入口和企业 API 调用。这里的核心变量是模型能力能否持续领先，以及单位推理成本能否下降到大规模商业化可承受。</p>
<p>第二条主线是通用软件和办公入口。它看的是用户规模、付费转化、组织渗透、数据粘性和协作场景。AI 办公、知识管理、文档、表格、PPT、会议和搜索，都属于这一层。</p>
<p>第三条主线是行业软件和定制交付。它看的是行业数据、客户现场、私有部署、项目交付和业务闭环。金融、制造、政企、医疗、教育、零售、电商、广告和研发工具，都可能出现 AI 重估。</p>
<p>三条主线对应不同交易节奏。基础模型看技术和资本开支，通用软件看产品和用户增长，行业软件看订单和交付毛利。把它们混在一起估值，会导致判断失真。</p>
<p>更细地看，基础模型更接近“卖铲子”，通用软件更接近“抢入口”，行业软件更接近“做交付”。卖铲子的风险是价格下降和算力成本，抢入口的风险是用户不付费，做交付的风险是项目周期和人力成本。三类公司可能都叫 AI 应用，但利润来源完全不同。</p>

<h2 id="domestic-opportunity">十二、国内软件公司的机会和约束</h2>
<p>国内软件公司最大的机会，是拥有客户入口和场景经验。企业客户不可能把所有数据直接交给海外模型，也不会把核心流程完全交给一个通用聊天工具。懂行业、懂客户、能落地、能本地部署的软件公司，有机会把模型变成企业可用的系统。</p>
<p>但约束也很清楚。国内企业软件付费能力相对弱，项目制收入占比高，标准化程度不足，客户需求碎片化，销售和交付成本偏高。如果 AI 只是增加研发费用和营销概念，却不能提高客单价、续费率、毛利率或交付效率，价值并不会自动提升。</p>
<p>所以判断国内软件公司的 AI 价值，要看四个指标：第一，AI 功能是否进入核心流程，而不是边缘演示；第二，是否提升客户续费或新增付费；第三，是否降低交付和研发成本；第四，是否形成行业数据和模板沉淀。只有这四点至少兑现两点，估值重估才有基础。</p>

<h2 id="valuation">十三、估值方法：从故事回到收入质量</h2>
<p>AI 应用早期最容易出现叙事溢价。只要产品能演示，市场就容易按巨大空间定价。但软件公司的价值最终要回到收入质量：续费是否稳定，客户是否复购，毛利率是否改善，销售费用率是否下降，现金流是否真实，研发投入是否能沉淀为平台。</p>
<p>对 AI 编程工具，可以看付费开发者数、团队版渗透率、企业安全和代码库接入。对办公软件，可以看 DAU、付费率、企业账户、文档和协作数据留存。对行业软件，可以看新增订单、私有化交付、项目毛利、客户续约和行业模板复用。</p>
<p>估值上不能只用“AI 应用空间巨大”作为理由。更稳妥的做法，是把公司放进三类：已经有收入验证的应用、正在形成客户粘性的工具、还停留在概念演示的产品。第一类可以给成长估值，第二类需要持续跟踪，第三类只能按主题弹性处理。</p>
<p>财务报表里最值得看的变化，是 AI 是否让原有软件的经营杠杆变强。如果收入增长但毛利率下降、费用率上升、现金流变差，说明 AI 可能只是增加了成本和宣传点；如果收入增长同时交付成本下降、客户留存改善、同一套产品能复制到更多客户，才说明 AI 真正变成了软件公司的利润杠杆。</p>

<h2 id="risks">十四、风险：技术进步不等于股东回报</h2>
<p>AI 软件化的趋势很强，但风险同样明显。第一，模型价格下降会压缩薄应用利润。只要应用没有数据和流程壁垒，模型厂商或大平台就可能直接覆盖。第二，企业落地比消费级试用慢，数据治理、权限、安全、合规和组织习惯都会拖慢商业化。</p>
<p>第三，资本开支和推理成本仍然需要收入证明。如果模型能力持续提升但应用收入跟不上，基础设施端会面临回报压力。第四，软件公司可能用 AI 概念包装传统业务，实际收入仍然依赖项目制和人力交付，估值却提前透支。</p>
<p>第五，竞争格局还没有稳定。模型厂商、云厂商、办公软件、行业软件、创业公司和系统集成商都在争夺入口。未来哪些公司拥有客户关系，哪些公司只承担低毛利交付，还需要用订单和财务数据验证。</p>

<h2 id="strategy">十五、买入策略：先看验证，再看弹性</h2>
<p>AI 应用投资不适合只追概念。更合理的策略，是把仓位分为三层。第一层是已经有客户入口和现金流的软件公司，作为底仓观察 AI 对续费、客单价和毛利率的改善。第二层是 AI 编程、办公助手、内容生成和行业 Agent 等高景气方向，用产品数据和收入验证动态加仓。第三层是主题弹性仓，只在产业催化和估值匹配时参与。</p>
<p>买点上，最好避开单纯发布会和演示驱动的高热度阶段。更好的信号是：客户开始续费，企业版本上线，私有化订单增加，交付人员效率提高，毛利率改善，或者大客户把 AI 功能从试点转为正式采购。</p>
<p>卖出或降仓信号也要清楚：用户增长停滞、付费率不升、AI 成本高于新增收入、交付仍然高度人力依赖、产品被平台级模型复制、估值已经把多年增长全部提前反映。这些情况出现时，再好的主题也要回到风险收益比。</p>

<h2 id="conclusion">十六、结论：AI 应用真正的价值在工作流里</h2>
<p>软件和 AI 应用的核心，不是模型会不会回答问题，而是模型能否进入工作流，稳定完成任务，并让企业愿意持续付费。AI 编程已经证明，专业场景一旦形成闭环，就能快速商业化。办公、行业软件、定制开发、素材生产和企业 Agent，正在沿着类似路径推进。</p>
<p>基础模型会越来越像底层公共能力，价格会下降，能力会普及。真正稀缺的是客户场景、数据结构、流程嵌入、交付经验和组织信任。软件公司的价值不会因为模型变强而消失，但会被重新分层：薄工具被压缩，深流程被重估，能把 AI 变成结果的公司会获得更高价值。</p>
<p>投资上，不必为每一次模型发布而兴奋，也不能忽视 AI 正在重塑软件商业模式。正确的方式，是沿着时间线看能力迁移，沿着工作流看付费逻辑，沿着财务报表看收入质量。软件与 AI 应用的机会，最终不在概念里，而在客户愿意为“少花钱、少用人、更快交付、更高转化”持续买单的地方。</p>
"""


def _plain_text(html_text: str) -> str:
    return re.sub(r"<[^>]+>", "", html.unescape(html_text))


def validate() -> None:
    _BASE_VALIDATE()
    failures: list[str] = []
    forbidden = [
        "B站", "bilibili", "哔哩", "视频里", "视频中", "原视频", "音频里", "音频中",
        "UP主", "up主", "这期", "本期", "作者说", "他提到", "观看", "点赞", "订阅",
        "投币", "收藏", "下期", "关注", "欢迎收看", "感谢大家", "三连", "BV1",
    ]
    post = base.INPUT_ORDER[0]
    article_path = base.ROOT / post.url_path.strip("/") / "index.html"
    article = article_path.read_text(encoding="utf-8")
    body_match = re.search(r'<div class="post-body" v-pre>(.*?)</div></div><nav', article, re.S)
    plain = _plain_text(body_match.group(1)) if body_match else ""
    if len(plain) < 6500:
        failures.append(f"{post.slug}: body too short: {len(plain)}")
    for word in forbidden:
        if word in article:
            failures.append(f"{post.slug}: forbidden/source wording present: {word}")
    required_terms = [
        "大模型", "AI", "软件", "API", "编程", "Cursor", "Claude Code", "Agent",
        "定制软件", "办公", "SaaS", "私有化", "资本开支", "文生视频", "工作流",
        "投资图谱", "估值", "买入策略",
    ]
    for word in required_terms:
        if word not in article:
            failures.append(f"{post.slug}: missing required topic: {word}")
    h2 = re.findall(r'<h2 id="([^"]+)">', article)
    links = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', article)
    if h2 != links or len(h2) < 12:
        failures.append(f"{post.slug}: toc mismatch or too few h2: h2={len(h2)} links={len(links)}")
    cover_text = (base.ROOT / "images/posts" / post.slug / "cover.svg").read_text(encoding="utf-8")
    ET.fromstring(cover_text)
    for word in forbidden:
        if word in cover_text:
            failures.append(f"{post.slug}: forbidden/source wording present in cover: {word}")

    home = (base.ROOT / "index.html").read_text(encoding="utf-8")
    cards = re.findall(r'<a href="([^"]+)" class="a-block">', home)
    expected_cards = [
        "/ai-news-radar/",
        "/2026/codeinsights-local-first-agent-workbench/",
        "/2026/what-you-need-to-learn-from-claw-code-repo/",
        "/2026/gaojingqi-investment-system/",
        "/2026/ai-revolution-permanent-underclass-career-selection/",
        "/2026/live-longer-than-earn-fast-investment-infinite-game/",
        post.url_path,
        base.PREV_EXISTING_URL,
    ]
    if cards[: len(expected_cards)] != expected_cards:
        failures.append(f"homepage order mismatch: {cards[:len(expected_cards)]}")

    archive = (base.ROOT / "archive/index.html").read_text(encoding="utf-8")
    rss = (base.ROOT / "index.xml").read_text(encoding="utf-8")
    ET.parse(base.ROOT / "index.xml")
    if post.url_path not in archive:
        failures.append(f"archive missing {post.url_path}")
    if post.full_url not in rss:
        failures.append(f"rss missing {post.full_url}")
    taxonomy_expectations = [
        ("categories/index.html", post.category),
        ("series/index.html", post.series),
        ("tags/index.html", post.tags[0]),
        (f"categories/{post.category}/index.html", post.url_path),
        (f"series/{post.series}/index.html", post.url_path),
        (f"tags/{post.tags[0]}/index.html", post.url_path),
    ]
    for rel, expected_text in taxonomy_expectations:
        path = base.ROOT / rel
        if expected_text not in path.read_text(encoding="utf-8"):
            failures.append(f"{rel} missing {expected_text}")
    previous = (base.ROOT / base.PREV_EXISTING_URL.strip("/") / "index.html").read_text(encoding="utf-8")
    if post.url_path not in previous:
        failures.append("previous existing article newer link missing")
    pycache = [str(p) for p in base.ROOT.rglob("__pycache__")]
    if pycache:
        failures.append(f"__pycache__ present: {pycache[:3]}")
    if failures:
        raise SystemExit("\n".join(failures))


def copy_script_and_manifest() -> None:
    tasks_dir = base.ROOT / "tasks"
    tasks_dir.mkdir(parents=True, exist_ok=True)
    script_path = tasks_dir / base.SCRIPT_NAME
    source_script = Path(__file__)
    if source_script.resolve() != script_path.resolve():
        shutil.copyfile(source_script, script_path)
    base.rec(script_path)
    for rel in ["categories/index.html", "series/index.html", "tags/index.html"]:
        base.rec(base.ROOT / rel)
    manifest_path = tasks_dir / base.MANIFEST_NAME
    all_changed = sorted(base.CHANGED | {f"tasks/{base.SCRIPT_NAME}", f"tasks/{base.MANIFEST_NAME}"})
    manifest_path.write_text(json.dumps(all_changed, ensure_ascii=False, indent=2), encoding="utf-8")
    base.rec(manifest_path)


base.ROOT = ROOT
base.DATE = "2026-08-03"
base.BASE_DT = datetime(2026, 8, 3, 21, 5, tzinfo=timezone(timedelta(hours=8)))
base.PREV_EXISTING_URL = "/2026/zheshenshinei-china-economy-housing-local-debt-trade-war/"
base.PREV_EXISTING_TITLE = "置身事内：看懂中国经济、房价、地方债与贸易战的一条线"
base.SCRIPT_NAME = "publish-software-ai-application-investment-logic-20260803.py"
base.MANIFEST_NAME = "publish-software-ai-application-investment-logic-20260803-changed-files.json"
base.CHANGED = set()
base.INPUT_ORDER = [
    base.Post(
        source_id="BV1rK3f6YEQt",
        slug="software-ai-application-investment-logic-agent-custom-software",
        title="软件与 AI 应用投资逻辑：从大模型商业化到 Agent 和定制软件",
        desc="从 AI 编程、办公助手、SaaS 重估、私有化部署、定制软件、Agent、资本开支回报和文生视频，拆解软件与 AI 应用的投资主线。",
        category="投资研究",
        series="AI应用",
        tags=["AI应用", "大模型", "软件", "Agent", "AI编程", "Cursor", "Claude Code", "SaaS", "定制软件", "文生视频", "资本开支"],
        minutes=28,
        body=BODY,
        cover_kicker="软件 × AI",
        cover_line="编程工具 · Agent · 定制软件 · 工作流",
        cover_theme=("#111827", "#2563eb", "#22c55e"),
        duration=2700.921905,
        segments=1727,
        chars=16315,
    )
]
base.PUBLISH_ORDER = list(reversed(base.INPUT_ORDER))
base.validate = validate
base.copy_script_and_manifest = copy_script_and_manifest


if __name__ == "__main__":
    base.main()
