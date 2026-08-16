from __future__ import annotations

import base64
import importlib.util
import json
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
TEMPLATE_SCRIPT = TASKS / "publish-deepseek-harness-cordis-article-20260816.py"
ASSET_DIR = TASKS / "video-batch-20260816-bv1ab-bv1l8" / "clean-screenshots-final"
OUT_DIR = Path("/tmp/two-investment-closed-door-articles-20260816-output")

SLUG_AI = "ai-bubble-hong-kong-japan-fed-china-path"
SLUG_CONSUMER = "consumer-panels-large-screen-tcl-oligonucleotide-protein-cycle"

spec = importlib.util.spec_from_file_location("publish_template", TEMPLATE_SCRIPT)
template = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = template
spec.loader.exec_module(template)

base = template.base
base.__file__ = __file__
base.DATE = "2026-08-16"
base.BASE_DT = datetime(2026, 8, 16, 2, 30, 0, tzinfo=timezone(timedelta(hours=8)))
base.PREV_EXISTING_URL = "/2026/ai-skills-agent-infrastructure-open-source-daily-20260814/"
base.PREV_EXISTING_TITLE = "AI Agent 基础设施 53 项速览：从可插拔 Harness 到本地推理与安全治理"
base.SCRIPT_NAME = Path(__file__).name
base.MANIFEST_NAME = "publish-two-investment-closed-door-articles-20260816-changed-files.json"
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


def fig(slug: str, name: str, caption: str) -> str:
    return f'<figure class="post-figure"><img src="/images/posts/{slug}/{name}" alt="{caption}" loading="lazy"><figcaption>{caption}</figcaption></figure>'


BODY_AI = rf'''
<p>AI 不是因为足够伟大，就天然免疫泡沫。PC、互联网、移动互联网都曾经是确定的技术方向，也都经历过估值过热、资金退潮和产业再出发。AI 的特殊之处在于，它不仅是一轮生产率革命，也是一场围绕社会结构、资源分配和技术路径的分裂。</p>
<p>这轮分裂可以归纳成三条线：AI 到底是服务少数精英，还是服务普罗大众；这一轮产业主导权究竟偏向美国，还是偏向中国；投资收益到底来自生产者的资本开支，还是来自消费者生活效率的提升。三条线最后会汇到同一个判断：如果相信少数精英、生产者主导和线上模型竞赛，定价重心就在美国；如果相信大众受益、消费者主导和软硬结合的落地，定价重心就更容易转向中国资产。</p>
{fig(SLUG_AI, 'ai-hk-japan-briefing-card.jpg', 'AI、港股与日本资产的核心判断：技术路径、流动性和市场宽度共同决定配置方向。')}

<h2 id="ai-can-be-good-and-expensive">一、好技术也会进入泡沫阶段</h2>
<p>“这一次不一样”通常只说对了一半。AI 确实和过去几轮技术周期不同，因为它触及智能、劳动、权力和人的位置；但只要资本市场把长期想象提前折现，就仍然会出现估值、融资和现金流之间的拉扯。</p>
<p>PC 和互联网的争议，更多集中在阶段：它是不是好东西、是不是会改变世界，答案并不难；真正难的是判断当时的估值有没有过度透支。AI 更复杂，因为它本身就带有社会争议。有人期待它让少数技术精英成为未来秩序的定义者，也有人担心它替代普通劳动者；有人把它当作生产端资本开支的竞赛，也有人更看重它能不能让普通生活变得更便宜、更省力、更可靠。</p>
<p>因此，AI 的投资判断不能只停在“它很重要”。更关键的问题是：资本开支能不能转化为收入，收入能不能转化为自由现金流，估值能不能被真实渗透率消化。技术越重要，越容易被市场提前讲成终局；而提前讲成终局，正是泡沫形成的土壤。</p>

<h2 id="three-splits">二、三重分裂：精英、大众、生产者与消费者</h2>
<p>第一重分裂，是 AI 为谁服务。美国硅谷叙事里，OpenAI、Anthropic、Palantir、马斯克式公司和加速主义话语，往往更容易呈现出“少数精英定义未来”的气质。极端表达是：技术快速冲向 AGI，少数人让世界变好，大众被安排在新的秩序里。</p>
<p>中国路径更偏向另一种表达：AI 的最终价值，是提高生产力，让普通人拿到实惠。这个实惠不一定来自更多线上对话产品，而更可能来自软硬结合、制造能力、机器人、终端设备、供应链效率和线下服务升级。</p>
<p>第二重分裂，是主导权。美国强在基础模型、顶级算力和资本市场定价权；中国强在场景、制造、数据密度和工程落地。第三重分裂，是投资到底赚谁的钱。美国 AI 定价主要围绕生产者资本开支、云厂商投入和大模型付费使用；中国资产更有可能从消费者端、产业端和实体效率改善中兑现。</p>
<p>三重分裂背后，是同一个问题：如果 AI 最终只是继续占据线上时间，增量空间会受限；如果 AI 进入物理世界，真正解决通勤、家务、物流、护理、运动、线下交互和劳动替代，增量空间会大得多。</p>

<h2 id="physical-world-pain-points">三、中国路径的关键，是解决物理世界痛点</h2>
<p>线上世界已经很拥挤。娱乐、资讯、社交、游戏和内容消费不断抢夺时间，但人的时间每天只有 24 小时。问题不是还能不能生产更多内容，而是普通人有没有更多时间消化内容。真正消耗人的，往往不是线上内容不够，而是通勤、体力劳动、家务、照护、排队、配送、维修和线下协作。</p>
<p>这正是中国路径的优势。中国不只是某个 AI 模型突然变强，而是在制造业的方方面面出现“涌现”：新能源汽车、光伏、储能、机器人、消费电子、家电、供应链自动化，都能把软件能力变成硬件产品，再把硬件产品扩散到大规模市场。</p>
<p>AI 如果只停在线上，会变成一场模型产品之间的注意力竞争；AI 如果进入物理世界，就会变成生活成本和生产成本的下降。后者才是更广谱、更接近普罗大众的价值，也是港股和中国资产重新被定价的重要逻辑。</p>

<h2 id="liquidity-shock">四、近期调整的核心，是微观和宏观流动性同时收紧</h2>
<p>近期 AI 资产的波动，表面看是高位回撤，底层更像一轮流动性冲击。微观层面，韩国高杠杆 ETF 和 AI 硬件相关标的的大幅波动，放大了全球 AI 硬件链条的联动调整。硬件链条本来就高度集中，一端出问题，容易迅速传导到其他市场。</p>
<p>宏观层面，6 月以来美元流动性从价格和数量上都有收紧迹象。美国财政部发债压力上升，二季度净发债规模相对温和，三季度计划净发债大幅增加；与此同时，云厂商和 AI 大厂的资本开支仍在上行。当自由现金流被大量 capex 消耗，外部融资条件就变得更重要。</p>
<p>这意味着 10 年期美债、美元流动性、美联储资产负债表和信用融资环境，都不只是宏观背景，而是 AI 交易能不能继续扩张的核心变量。AI 大厂如果需要越来越多债务或外部资金支撑未来投资，那么金融条件一旦收紧，估值就会更敏感。</p>

<h2 id="fed-path">五、美联储不加息，是短期市场支撑的关键假设</h2>
<p>市场一度把美联储重新转向加息的概率计入价格，但这个判断并不稳。只要核心通胀环比仍在温和区间，经济数据又没有强到迫使政策重新转鹰，美联储进一步加息的必要性就不高。</p>
<p>真正要看的，不只是口头表态，而是资产负债表。2019 年回购市场压力出现后，美联储名义上不承认重启量化宽松，但资产负债表已经扩张。现在如果在 QT 环境下资产负债表仍然扩张，就说明系统流动性已经需要被动补水。三季度发债压力更高时，这个变量尤其重要。</p>
<p>如果美联储不加息，金融条件会缓和，AI 与风险资产会得到支撑；如果重新加息，美元、利率和融资成本会同时压制估值。这是短期最直接的宏观分水岭。</p>

<h2 id="china-ai-catch-up">六、中国 AI 的追赶速度，正在改变收入预期</h2>
<p>中国短板一直被认为是算力，但模型能力和应用场景的进步正在改变这个框架。Kimi、DeepSeek、混元、字节等大模型不断迭代，开源模型和开放权重也在提高可用性。只要模型能力足够强，算力短板就不一定完全阻断产业机会。</p>
<p>更重要的是数据和场景。阿里、美团、京东、腾讯、字节以及大量产业互联网公司，都掌握真实交易、履约、物流、内容、用户行为和本地生活数据。AI 如果最终为消费者服务，这些数据和场景就会变成优势。</p>
<p>这也会反过来冲击美国大模型公司的收入假设。OpenAI 和 Anthropic 的年化收入过去高速增长，但如果微软、企业客户或开发者开始采用更便宜、更开放、更可控的中国模型替代部分能力，原有收入曲线就可能被拉平。模型再强，也绕不开数据质量；垃圾输入仍然会导向垃圾输出。数据、场景和成本，会重新分配模型公司的定价权。</p>

<h2 id="bubble-dashboard">七、监测 AI 泡沫，不能只看股价</h2>
<p>AI 泡沫是否进入更危险阶段，可以用四组指标交叉判断。第一是美联储政策和美元流动性。利率、美元、油价如果同时偏高，会像 2000 年科技泡沫后期那样，形成整体金融条件收紧。</p>
<p>第二是市场宽度。宽度扩散本身不一定坏，关键要看扩散到哪里、估值高不高。美国 AI 估值高，非 AI 部分相对合理；日本不仅局部热，扩散后的整体估值也偏高，风险更大；中国和港股很多非 AI 资产仍然便宜，宽度扩散反而有助于市场稳定。</p>
<p>第三是头部模型公司的年化收入。模型公司收入如果继续加速，资本开支故事还能延续；如果增速持续放缓，市场会重新审视算力和云投资的回报周期。</p>
<p>第四是自由现金流和杠杆率。AI 资本开支需要钱，钱来自经营现金流、外部融资和债务。如果自由现金流持续被消耗，同时债务融资依赖上升，利率环境就会直接打到估值根部。</p>

<h2 id="japan-us-hk">八、港股、日本和美国：同样扩散，不同风险</h2>
<p>日本资产现在更需要谨慎。日元、资金回流、估值扩散和海外资金持仓叠在一起，使日本不只是局部 AI 热，而是更广泛资产都被抬高。市场宽度扩大，如果发生在整体估值已经偏高的市场，就不再是安全垫，而可能变成泡沫外溢。</p>
<p>美国处在中间状态。AI 定价高，但大量非 AI 公司估值还没有失控，宽度扩散短期可以缓冲风险。不过美国最大变量仍然是金融条件和模型公司收入兑现。</p>
<p>中国和港股的状态不同。这里的扩散更多发生在低估值资产之间，尤其是消费、互联网、制造和部分硬科技。资金从过热资产流向便宜资产，反而会让市场结构更稳。看空日本、增配港股的核心，不是简单的地域偏好，而是同样的宽度扩散在不同估值底座上的风险收益完全不同。</p>

<h2 id="rmb-framework">九、RMB 框架：Return、Money、Belief</h2>
<p>理解中国资产，不能只看短期收益率，也要看信念。RMB 可以拆成三层：R 是 Return，代表回报和利差；M 是 Money，代表货币和流动性；B 是 Belief，代表到底相信中国还是相信美国。</p>
<p>2015 年以后，人民币悲观情绪一度非常浓。真正支撑长期判断的，不只是某个季度的利差，而是中国制造业能力的持续涌现。所谓涌现，不是单点突破，而是跨行业能力突然开始互相强化：工程师、供应链、设备、工艺、市场和资本形成正反馈。</p>
<p>AI 也会沿着这条路走。中国不一定在每一项基础模型指标上领先，但只要制造、场景和数据持续涌现，AI 就会以更贴近普通生活的方式扩散。这个信念，是港股和中国资产重估的底层基础。</p>

<h2 id="allocation-conclusion">十、结论：回避高估值扩散，寻找低估值重估</h2>
<p>AI 仍然是大方向，但大方向不等于任何价格都合理。短期看，美联储是否加息、美元流动性是否缓和、10 年期美债压力是否释放，会决定全球风险资产的弹性。中期看，OpenAI、Anthropic 等模型公司的年化收入，以及大厂自由现金流能否支撑资本开支，会决定 AI 交易是否继续健康。</p>
<p>资产选择上，应回避已经从局部过热扩散到全市场偏贵的区域，尤其是日本这类估值和资金结构都更脆弱的市场。相反，港股和中国资产仍有大量便宜板块，AI、消费、制造和互联网的扩散不一定增加泡沫，反而可能带来估值修复。</p>
<p>最终要回到一个朴素判断：AI 不是只属于模型公司和云厂商的资本开支竞赛，它也可以是一场进入物理世界、服务普通生活、重塑制造业和消费者体验的生产力扩散。只要这条中国路径继续成立，港股相对日本的吸引力就会持续上升。</p>

<h2 id="practical-checklist">十一、实际操作：把叙事拆成四张表</h2>
<p>第一张表是流动性表。把美元指数、10 年期美债、油价、美联储资产负债表和美国财政部发债节奏放在一起看。如果美元、油价和利率同时偏高，而美联储资产负债表又没有扩张缓冲，AI 交易就容易从高估值变成高波动。</p>
<p>第二张表是资本开支表。云厂商和模型公司的故事，必须落到 capex、折旧、债务融资和自由现金流。资本开支越大，越需要外部融资环境支持；如果融资成本上升，而收入兑现速度没有同步加快，估值自然会被压缩。</p>
<p>第三张表是收入质量表。模型公司年化收入不能只看绝对规模，还要看增速、客户集中度、替代风险和开源模型压力。中国开放权重模型如果在企业端持续替代部分闭源能力，美国模型公司的收入曲线就会被重新定价。</p>
<p>第四张表是市场宽度表。宽度扩散不是天然利好，低估值市场的扩散是稳定器，高估值市场的扩散可能是泡沫后期。日本的风险在于整体估值和资金结构更脆弱，港股的优势在于扩散发生在更低估值底座上。</p>
<p>把这四张表放在一起，结论会更清楚：短期风险来自流动性，中期风险来自资本回报，长期机会来自中国制造和物理世界落地。只看 AI 叙事容易过度兴奋，只看宏观又容易错过产业扩散，真正有效的框架必须把二者合并。</p>

<h2 id="what-can-break-the-view">十二、什么情况会推翻这个框架</h2>
<p>第一，美联储如果在通胀压力下重新加息，并且资产负债表没有扩张缓冲，风险资产会重新面对更紧的金融条件。这种情况下，港股和中国资产也会被外部流动性拖累，只是因为估值更低，回撤结构可能不同。</p>
<p>第二，美国模型公司如果年化收入重新加速，并且大客户没有转向更便宜的开放模型，闭源模型的高估值会获得更长兑现期。相反，如果收入增速放缓、企业客户转向多模型混合架构，AI 主线会从模型公司转向应用、数据和物理终端。</p>
<p>第三，中国路径如果只停留在概念，没能持续把 AI 接入制造、终端、机器人和线下服务，那么港股重估也会缺少产业利润支撑。中国资产的机会不是情绪反转，而是便宜估值叠加真实产业扩散。没有后者，前者只能是短线修复。</p>
'''


BODY_CONSUMER = rf'''
<p>消费板块的机会，不是简单押注总需求突然大反转，而是在多个细分行业里寻找“压力见底、供给收缩、成本改善、产品升级和催化密集”同时出现的位置。家电、面板、纺织服装代工、健康原料、拼搭玩具、寡核酸药物和替代蛋白，表面看不属于同一条产业链，底层却有相似逻辑：过去几个季度的压制因素正在松动，下一阶段要看盈利弹性而不只是收入增速。</p>
<p>主线可以分成两类：一类是传统消费和制造链的修复，包括白电、面板、代工和玩具；另一类是功能性消费和生命科学的增量，包括健康原料、寡核酸和微生物蛋白。前者看周期位置，后者看需求渗透和技术催化。</p>
{fig(SLUG_CONSUMER, 'panel-tcl-briefing-card.jpg', '面板供给出清、大屏化需求和折旧下降共同构成 TCL 等龙头的利润修复框架。')}

<h2 id="home-appliance-bottom">一、白电：二季度大概率是国内销售底部</h2>
<p>白电行业的第一个变化，是收入压力开始缓和。安徽、湖北、浙江、四川等地 7 月空调零售数据重新转正，一方面来自天气恢复正常、高温带动空调需求；另一方面也与部分省份以旧换新补贴预算在 7 月前后使用完毕、零售基数下行有关。</p>
<p>线上数据同样出现边际改善，说明行业在经历二季度较低景气之后，正在从左侧过渡到右侧。只要收入增速压力缓解，平台方和品牌方在终端价格、出厂价格和渠道费用上就会有更多选择，沉闷的经营压力也更容易向利润改善传导。</p>
<p>三大白电龙头之外，二线标的的弹性更值得重新评估。海信家电、澳柯玛等公司如果能在行业改善后释放收入和业绩弹性，估值修复可能比稳态龙头更明显。白电不是爆发式主题，而是从低景气走向修复的右侧交易。</p>

<h2 id="panel-supply-demand">二、面板：供给出清与大屏化需求同时发生</h2>
<p>面板行业的底层变化，是固定资产投资周期结束后，供需结构开始改善。友达 7.5 代 A 线出售传闻再次强化了供给侧收缩预期。如果一条成熟产线被出售或改造为洁净室用途，LCD 供给会出现实际减少。台湾厂商出售旧产线用于洁净室改造也不是第一次，海外新建洁净室往往需要两到三年，现成产线改造对买方有吸引力。</p>
<p>需求侧则是电视大屏化和高端化。国内线下 80 英寸以上电视销量占比已经接近三成，线上占比也超过一成半。电视尺寸每增加 1 英寸，面板面积消耗会明显放大；即便整机销量小幅下降，面积需求仍可能增长。</p>
<p>海外同样在变化。美国电视平均尺寸已超过 50 英寸，80 英寸以上产品增长更快；欧洲因为渠道层级多、库存消化慢，结构升级节奏落后，但当旧库存逐渐耗尽后，大屏化有望继续推进。面板需求不只看台数，更要看面积。</p>

<h2 id="tcl-profit-release">三、TCL 科技：价格不涨，也能有利润释放</h2>
<p>高世代面板线资本开支很重，单条产线投资可能超过 300 亿元。在需求没有爆发式增长的背景下，行业大规模新增产能基本停住。京东方、TCL 科技等龙头既有产线进入折旧下降阶段，又没有明显新增大额资本开支，这会带来利润释放。</p>
<p>面板投资的关键不一定是继续涨价。只要电视面板价格能够稳定在当前位置，折旧下降、供给收缩和面积需求增长就足以改善利润。TCL 科技如果能稳定在百亿级利润中枢，对应估值约 10 倍，正常估值修复就可能带来较大的上行空间。</p>
<p>这类机会的核心是“低估值加小盈利弹性”。行业不需要出现极端景气，只要供给端不再乱投、需求端面积继续增长、价格维持稳定，龙头就能释放利润。</p>

<h2 id="textile-oem">四、纺织服装代工：汇率和关税是短期冲击，不是长期恶化</h2>
<p>纺织服装代工龙头上半年业绩承压。申洲国际发布盈利预警，净利润同比下滑明显；裕元集团上半年利润也大幅下降。表面看是订单、产能利用率和利润率同时承压，底层主要有三类短期因素。</p>
<p>第一是汇率。人民币兑美元阶段性升值，使以美元计价收入、人民币成本和美元资产负债结构的公司出现汇兑损失。第二是产能利用率不足。订单不足导致固定成本摊薄变差，叠加海外产能和人工成本，毛利率被压制。第三是关税和客户让利。关税政策不明朗时，代工企业可能主动承担一部分成本，短期压缩毛利。</p>
<p>下半年需要看的拐点，是订单、产能利用率、成本传导和汇兑压力。品牌客户库存持续下降后，补库需求有望释放；印尼、越南等海外产能如果随订单回暖逐步爬坡，毛利率会得到改善。龙头企业具备面料研发、快速交付、一体化制造和多地供应链能力，成本压力向客户传导的能力更强。短期业绩波动之后，龙头估值已经进入更有吸引力的位置。</p>

<h2 id="health-ingredients">五、健康原料：涨价、替代和需求升级三条线</h2>
<p>健康原料可以从三条线看。第一条是原材料涨价周期。晨光生物的叶黄素、辣椒红、辣椒精等植提产品，受主产区种植面积下降影响，可能进入提价周期。辣椒主产区种植面积预计减少 10% 到 15%，新原料季到来后，价格弹性会逐步体现。</p>
<p>第二条是原料替代。乳清蛋白涨价，会强化酵母蛋白等替代方案；鱼油价格上行，也会强化藻油替代逻辑。安琪酵母的酵母蛋白、金达威的藻油相关产能，都是在这一框架下被重新评估的方向。只要替代品的成本、营养结构和应用稳定性被下游接受，利润率就会随规模释放。</p>
<p>第三条是需求升级。减糖、控糖、运动营养和功能食品推动膳食纤维、阿洛酮糖等原料高速增长。膳食纤维全球需求仍处在成长阶段，阿洛酮糖长期空间更大。百龙创园的扩产和泰国产能如果顺利释放，产能结构优化会带来业绩增量。</p>
<p>这条线不是单纯讲“健康消费”，而是把原材料价格、替代路径和下游需求放在一起。晨光生物、百龙创园、金达威、安琪酵母等标的，核心都在于能否把产业趋势转化成产能、价格和利润率。</p>

<h2 id="bloks-growth">六、布鲁可：从国内积木玩具龙头走向全球化玩具公司</h2>
<p>布鲁可上半年收入和利润保持较快增长，经营质量稳健。增长不再只依赖国内经销商，而是逐渐形成国内稳健、海外高增、产品多线驱动的新结构。渠道库存和终端动销质量改善，是基本盘稳定的前提。</p>
<p>区域上，国内业务仍然保持双位数增长，海外收入增速更高，占比继续提升。美国和亚洲市场已经成为重要海外市场，增长不只是渠道数量增加，也来自既有渠道产出提升和国家覆盖面扩大。海外扩张开始从单一渠道增长，转向渠道数量与单店产出共同增长。</p>
<p>产品上，积木车是重要新增量。它面向车迷、模型玩家和改装爱好者，帮助公司从儿童玩具扩展到更广泛年龄层。16 岁以上产品收入占比明显提升，49 元以上成人向产品 SKU 增多，产品矩阵从 29 元低价带到百元以上高客单逐步完善。</p>
<p>海外消费者往往通过成人模型和粉丝向产品认识品牌，因此成人向产品与海外扩张相互强化。下半年要跟踪积木车新品、新 IP、原创机械类产品、旅行箱类产品、海外渠道扩张以及毛利率环比回升。盈利改善可能是渐进过程，但增长结构已经从单点扩张转向多点驱动。</p>

<h2 id="oligonucleotide-catalysts">七、寡核酸：下半年进入密集催化期</h2>
<p>医药方向里，寡核酸药物从 2026 年下半年开始进入密集催化期。siRNA、ASO、抗体偶联寡核酸等技术路线同时推进，疾病覆盖从肝内向肝外扩展，从罕见病向慢病和更大适应症外延，递送系统也在迭代。</p>
<p>这轮行业变化的核心，不只是某个药物单点突破，而是竞争维度从序列优化、靶点跟踪，升级到递送系统、平台能力和全球管线布局。多项核心品种进入上市审评或关键数据读出窗口，全球大药企的合作、收购和授权动作，也会把产业链估值推到更高能见度。</p>
<p>产业链上，CRO、CDMO、原料供应、递送系统和全球领先公司合作标的都值得纳入框架。寡核酸的投资不是只看某个临床数据，而是看技术平台、产能承接和客户合作能否形成连续订单。</p>

<h2 id="microbial-protein">八、微生物蛋白：供给降本与 GLP-1 需求共振</h2>
<p>微生物蛋白进入供需两端同时催化的阶段。供给端，合成生物学、菌株优化和发酵工艺改进，正在持续降低成本。部分微生物蛋白成本已经低于猪肉和牛肉，产业化条件逐步成熟。</p>
<p>需求端，GLP-1 类药物使用人群扩大，带来额外蛋白补充需求。减重药物用户为了应对肌肉流失，往往需要更高质量蛋白摄入，食品和营养品开始从“蛋白粉”走向“万物加蛋白”。传统乳清蛋白 WPC80 价格快速上涨，也给酵母蛋白、微生物蛋白等替代品创造窗口。</p>
<p>微生物蛋白的优势在于蛋白含量高、营养结构可控、对环境更友好，并且可以进入食品、营养保健品和功能食品配方。安琪酵母、圣泉股份、蔚蓝生物等公司具备菌种、发酵工艺和产品开发积累，后续要看产能验证、客户导入和商业放量节奏。</p>

<h2 id="portfolio-view">九、结论：从总量叙事转向细分盈利弹性</h2>
<p>这组线索的共同点，是都不能只用宏观消费强弱来解释。白电看国内销售底和二线弹性；面板看供给退出、大屏化和折旧下降；代工看汇率、关税和产能利用率修复；健康原料看涨价、替代和需求升级；布鲁可看海外扩张与成人向产品；寡核酸看密集催化；微生物蛋白看供给降本与 GLP-1 需求共振。</p>
<p>配置上，不能把所有消费都当成同一个 beta。更有效的方式，是找那些已经经历压力、估值没有透支、又有清晰盈利改善抓手的细分环节。真正有弹性的公司，往往不需要总量环境突然变得很强，只需要库存、价格、成本、产能利用率或产品结构中的一个关键变量转好。</p>
<p>下一阶段的消费和制造投资，核心不是讲复苏口号，而是逐项拆开：哪里供给不再增加，哪里需求仍有结构升级，哪里成本压力开始回落，哪里产品矩阵打开新人群，哪里技术催化正在密集兑现。答案越具体，胜率越高。</p>

<h2 id="risk-map">十、风险地图：每条线都有自己的验证点</h2>
<p>白电的风险在于补贴节奏和天气扰动。如果零售转正只是低基数或短期高温带动，而终端价格没有稳定，二线弹性会被延后。判断白电右侧是否成立，要看线上线下销量、均价、渠道库存和出厂价格是否同步改善。</p>
<p>面板的风险在于价格和产能纪律。友达产线出售如果没有真正落地，供给侧预期会打折；如果大屏化速度不足以抵消台数下滑，面积需求也会低于预期。TCL 科技的利润释放，需要面板价格稳定、折旧下降兑现和新增 capex 克制三者同时成立。</p>
<p>代工的风险在于客户订单恢复慢于预期。汇率和关税冲击如果持续，利润率改善会变慢；但龙头的多地产能、面料研发和快速交付能力，仍然决定了它们比中小代工厂更容易拿到稳定订单。</p>
<p>健康原料、微生物蛋白和寡核酸的风险更偏产业化。涨价品种要看能否顺利传导到下游，替代品要看配方验证和客户导入，寡核酸要看关键数据、审批节奏和订单兑现。真正的产业趋势，必须从主题热度走到产能、客户、价格和利润。</p>

<h2 id="how-to-read-the-cycle">十一、怎样读这轮多行业周期</h2>
<p>这轮机会的难点，是它不像单一行业景气周期那样整齐。白电是低位修复，面板是供给出清，代工是利润表修补，布鲁可是品牌出海和人群扩张，健康原料是价格与替代，寡核酸是研发催化，微生物蛋白是供需共振。不同产业不能套同一套估值逻辑。</p>
<p>更合理的读法，是把每条线拆成三个问题：第一，压制因素是否已经见顶；第二，盈利改善的触发点是否足够具体；第三，估值是否已经提前反映。只有三项同时成立，才值得把它从主题放进组合。</p>
<p>面板和代工偏周期修复，胜负手在利润率；布鲁可偏成长消费，胜负手在海外和产品矩阵；健康原料和微生物蛋白偏产业替代，胜负手在成本曲线和客户导入；寡核酸偏创新药产业链，胜负手在临床、审批和大药企合作。把这些差异拆清楚，才不会把所有机会都混成一句“消费复苏”。</p>

<h2 id="execution-order">十二、执行顺序：先确定拐点，再比较弹性</h2>
<p>第一步先确认行业拐点。白电要看二季度是否真是国内销售底；面板要看供给退出是否落地；代工要看订单和产能利用率；健康原料要看提价能否被下游接受；布鲁可要看海外渠道和成人向产品是否继续放量；寡核酸要看关键品种审批和订单；微生物蛋白要看客户配方验证。</p>
<p>第二步比较弹性。低估值周期股看利润率每提升一个点能释放多少利润；成长消费看新品和海外收入能否把收入中枢抬高；医药产业链看单个催化能否转化为持续订单；原料替代看价格、成本和产能是否同时向好。</p>
<p>第三步控制位置。已经被预期充分交易的标的，需要等业绩确认；还停留在低位、但变量正在变好的标的，才有更好的赔率。真正的组合不是把每条线都买一遍，而是在每条线里挑出“拐点最清楚、估值最克制、验证路径最短”的公司。</p>
'''


base.POSTS = [
    base.Post(
        slug=SLUG_AI,
        title="AI 泡沫、港股与日本：从流动性到中国路径的市场框架",
        desc="从 AI 三重分裂、美元流动性、美联储政策、模型公司收入和市场宽度，理解为什么港股相对日本更有吸引力。",
        category="投资",
        series="内资闭门会",
        tags=["AI", "港股", "日本股市", "美联储", "流动性", "中国资产", "人民币", "科技周期"],
        minutes=13,
        body=BODY_AI,
        accent=("#111827", "#059669", "#22c55e"),
        required=["AI", "港股", "日本", "美联储", "OpenAI", "Anthropic", "Kimi", "DeepSeek", "RMB", "Return", "Money", "Belief", "10 年期美债", "自由现金流"],
        minimum=4700,
    ),
    base.Post(
        slug=SLUG_CONSUMER,
        title="面板拐点与消费复苏：从 TCL 到寡核酸、微生物蛋白",
        desc="白电、面板、TCL 科技、纺织服装代工、健康原料、布鲁可、寡核酸和微生物蛋白的多线索修复框架。",
        category="投资",
        series="内资闭门会",
        tags=["消费", "面板", "TCL 科技", "白电", "纺织服装", "健康原料", "寡核酸", "微生物蛋白"],
        minutes=15,
        body=BODY_CONSUMER,
        accent=("#0f172a", "#0ea5e9", "#22c55e"),
        required=["白电", "面板", "TCL 科技", "友达", "申洲国际", "裕元", "晨光生物", "百龙创园", "金达威", "布鲁可", "寡核酸", "微生物蛋白", "GLP-1", "WPC80"],
        minimum=4700,
    ),
]

template.SLUG = SLUG_AI
template.ASSET_DIR = ASSET_DIR
template.SCREENSHOT_SOURCES = {
    SLUG_AI: [("ai-hk-japan-briefing-card.jpg", "ai-hk-japan-briefing-card.jpg")],
    SLUG_CONSUMER: [("panel-tcl-briefing-card.jpg", "panel-tcl-briefing-card.jpg")],
}


def write_outputs(outputs: dict[str, str | None], binary_outputs: dict[str, bytes]) -> None:
    if OUT_DIR.exists():
        import shutil

        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for rel, content in outputs.items():
        if content is None:
            continue
        path = OUT_DIR / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    for rel, content in binary_outputs.items():
        path = OUT_DIR / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    print(json.dumps({"local_output": str(OUT_DIR), "text_files": len([v for v in outputs.values() if v is not None]), "binary_files": len(binary_outputs), "deleted": len([v for v in outputs.values() if v is None]), "urls": [post.full_url for post in base.POSTS]}, ensure_ascii=False, indent=2))


def render_asset_check() -> None:
    from PIL import Image

    for post in base.POSTS:
        svg = OUT_DIR / f"images/posts/{post.slug}/cover.svg"
        png = Path(f"/tmp/{post.slug}-cover.png")
        subprocess.run(["sips", "-s", "format", "png", str(svg), "--out", str(png)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        probe = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(png)], check=True, stdout=subprocess.PIPE, text=True).stdout
        if "pixelWidth: 1600" not in probe or "pixelHeight: 900" not in probe:
            raise RuntimeError(f"cover render failed: {post.slug}: {probe}")
        for _, dest in template.SCREENSHOT_SOURCES[post.slug]:
            chart = OUT_DIR / f"images/posts/{post.slug}/{dest}"
            chart_probe = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(chart)], check=True, stdout=subprocess.PIPE, text=True).stdout
            if "pixelWidth: 852" not in chart_probe or "pixelHeight: 480" not in chart_probe:
                raise RuntimeError(f"screenshot dimensions failed: {post.slug}/{dest}: {chart_probe}")
            img = Image.open(chart).convert("RGB")
            lower = img.crop((0, int(img.height * 0.55), img.width, img.height))
            purple_pixels = sum(
                1
                for r, g, b in lower.getdata()
                if r > 90 and b > 80 and g < 90 and r > g * 1.4 and b > g * 1.2
            )
            if purple_pixels > 100:
                raise RuntimeError(f"subtitle-like purple overlay detected in {post.slug}/{dest}: {purple_pixels} pixels")


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
        {"message": "Publish two investment closed-door articles", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    base.run_gh(["-X", "PATCH", base.endpoint(f"git/refs/heads/{base.BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


template.write_outputs = write_outputs
template.render_asset_check = render_asset_check
template.create_commit = create_commit


if __name__ == "__main__":
    for attempt in range(3):
        try:
            template.main()
            break
        except RuntimeError as exc:
            if attempt < 2 and any(token in str(exc) for token in ["Reference update failed", "remote reference changed"]):
                time.sleep(2)
                continue
            raise
