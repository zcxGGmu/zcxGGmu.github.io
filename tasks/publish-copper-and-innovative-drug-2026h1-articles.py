from __future__ import annotations

import html
import json
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
from urllib.parse import quote


ROOT = Path("/tmp/hermes-video-publish")
PREVIOUS_URL = "/2026/innovative-drug-policy-bd-device-tender-turning-point/"
PREVIOUS_TITLE = "医药投资的政策拐点：创新药、BD 出海与器械招投标复苏"
SITE = "https://zcxggmu.github.io"
CHANGED: set[str] = set()


@dataclass(frozen=True)
class Post:
    slug: str
    title: str
    desc: str
    date: str
    pub_dt: datetime
    category: str
    series: str
    tags: list[str]
    minutes: int
    article_html: str
    cover_kind: str

    @property
    def url_path(self) -> str:
        return f"/2026/{self.slug}/"

    @property
    def full_url(self) -> str:
        return SITE + self.url_path

    @property
    def cover(self) -> str:
        return f"/images/posts/{self.slug}/cover.svg"


COPPER_HTML = r"""
<p>铜的核心矛盾正在变得清楚：短期看，三季度的价格弹性来自关税解释、库存去化和旺季补库；中长期看，铜矿供给持续不及预期，叠加 AI 数据中心、电力电网和变压器等结构性需求，铜价的向上逻辑并没有被削弱。</p>

<p>这不是一个单纯靠情绪推动的交易。盘面、现货流向、显性库存、下游补库、矿端扰动和需求结构都在指向同一个方向：铜的供需平衡表仍然偏紧，价格每次回落都会激发产业链补库，而美国关税只要没有被推翻，就会持续改变全球电解铜的流向，并压缩非美地区可交易库存。</p>

<h2 id="tariff-pricing">一、关税预期已经写进盘面，但还没有充分定价</h2>

<p>市场调研和期货盘面给出的信号基本一致：美国仍然大概率会沿着对电解铜加征关税的路径前进。主流预期倾向于阶梯式加征，2027 年 1 月 1 日开始加征 15%，2028 年提高到 30%。</p>

<p>关键在于，盘面虽然已经反映了关税预期，但反映得并不充分。COMEX 与 LME 的铜价差上，近月合约大致在 400 美元附近，对应伦铜价格的溢价不到 3%；十个月后的远月价差可以达到约 1000 美元，但仍显著低于 15% 关税理论上应当对应的价差。如果以 13500 美元附近的铜价计算，15% 的幅度约等于 2000 美元。</p>

<p>这说明市场并不是完全没有交易关税，而是还停留在“远端部分定价”的状态。真正的落地时间、加征路径和执行细节，仍然可能成为三季度铜价的重要催化。</p>

<h2 id="us-inventory">二、美国补库正在消耗非美现货</h2>

<p>现货流向比价格结构更能说明问题。美国电解铜和铜合金进口仍处在历史同期高位。上一轮异常补库年份比正常年份多进口约 75 万吨；今年上半年相比去年同期只少约 10 万吨，如果全年按类似节奏推算，今年仍可能比正常年份多进口约 50 万吨。</p>

<p>两年合计，美国可能多囤积约 120 万吨电解铜，接近美国半年消费量。这部分库存主要堆积在 COMEX 显性库存中，表面上看是美国库存增加，本质上是非美地区现货持续被抽走。</p>

<p>这正是关税交易最重要的地方：在加征窗口真正到来前，美国有强烈动机提前进口和囤积电解铜。越接近关税执行点，囤货动机越强；如果 2028 年继续加到 30%，那么 2027 年仍然会成为为 2028 年补库的窗口。</p>

<h2 id="not-reversed">三、只要关税不被推翻，中长期就是利多</h2>

<p>关税落地的短线节奏可能有差异，但长期方向更重要。若关税在 2027 年 1 月 1 日直接落地，铜价可能先出现一轮脉冲式上涨，随后出现冲高回落；但回落并不改变长期重心上移的方向，因为执行窗口前仍然存在囤货动力。</p>

<p>如果关税延后到 2027 年 6 月，甚至延后到 2028 年，逻辑也没有被破坏。延后并不等于利空，反而意味着美国有更长时间继续进口和囤积电解铜，非美地区现货会更紧。</p>

<p>LME 是全球定价市场，一旦非美现货紧张被定价，价格重心会自然上移。从交易层面看，非美地区处于低库存状态时，贸易商更容易反复挤仓，而美国库存难以顺畅回流到非美市场来形成库存压力。这会放大铜价的上行弹性。</p>

<p>因此，对关税问题的判断可以压缩成一句话：只要加征关税没有被彻底推翻，它对中长期电解铜价格就是向上的推动力量。三季度如果出现明确解释或落地安排，就会成为短期非常直接的触发器。</p>

<h2 id="domestic-demand">四、国内三季度是供需双弱，不是需求崩塌</h2>

<p>国内三季度供需状态可以概括为“供需双弱”。7 月到 8 月上旬本来就是传统消费淡季，年度检修和季节性检修也往往集中在这个阶段，供应端本身偏紧。需求端看起来不强，但价格下跌后，下游补库意愿仍然会被明显激发。</p>

<p>当铜价一度跌到 11600 美元附近，下游买货明显增加，随后社会库存出现较快去化，周度去库大约 3 万吨。这种去库速度放在淡季并不寻常，因为有些淡季甚至会累库。</p>

<p>近年来显性库存越来越像价格的结果，而不只是价格的原因。当价格下跌，下游补库，显性库存就会被消耗；库存去化反过来验证了消费韧性。也就是说，当前并不是淡季极弱或消费崩塌，而是正常的供需双弱环境中，低价触发了补库。</p>

<p>更重要的时间窗口可能在 8 月底到 9 月。传统旺季叠加宏观预期修复，如果下游订单和库存继续给出正反馈，铜的 beta 有机会重新回来。</p>

<h2 id="macro-micro">五、宏观与微观共振的时间点在 8 月下旬以后</h2>

<p>短期交易节奏上，7 月更像偏筑底阶段，买盘力量尚未全面上来。后续更值得关注的，是两个变量能否同时出现：美国关税解释形成外部催化，国内 8 月底到 9 月的消费旺季给出微观正反馈。</p>

<p>如果两者共振，铜价会从单纯的关税预期交易，转向宏观、现货和需求共同推动。届时，库存去化、下游补库、价格弹性和盘面结构会互相强化。</p>

<p>这也是当前铜交易的胜负手：不是在淡季最弱的时间点追逐短线情绪，而是在旺季前后观察真实需求是否接住价格。若低价补库持续出现，旺季订单没有显著走弱，价格底部就会越来越扎实。</p>

<h2 id="mine-supply">六、铜矿供给持续不及预期是长期支撑</h2>

<p>铜矿供给偏紧不是新故事，但它仍然是最重要的长期变量。过去几年，铜矿供给增速几乎每年都要被下调，矿端扰动不断出现，Kamoa-Kakula、Grasberg 等项目的恢复和放量节奏也不总是符合年初乐观预期。</p>

<p>高铜价本身会制造新的扰动。铜价处于历史高位且维持时间较长，铜矿利润率较高，这会引发劳资纠纷、资源民族主义和政府利益再分配诉求。刚果（金）对 KCC 的税务罚款、停产扰动，智利 Capstone 年初罢工停产一个月以上，都是高利润背景下矿端扰动上升的例子。</p>

<p>即使明年市场会放入部分矿山复产、扩产和新项目投产预期，也很难排除新的矿端故事出现。当前盘面对“铜矿供给持续下修”已经形成惯性认知，市场并不愿意提前交易明年大幅放量来做空铜价。</p>

<p>这意味着供应端仍然在给铜价提供底部支撑。若三季度冶炼端有一定减产，而矿端又维持偏紧，市场对供需紧张的担忧会进一步放大。</p>

<h2 id="ai-power">七、AI 数据中心正在重塑铜需求强度</h2>

<p>铜需求不能再简单套用过去的传统增速。历史上，美国 1930 年到 1940 年人均用铜强度快速提升，背后是制造业扩张和电力基础设施建设；1942 年到 1991 年，服务业占比提高，制造业占比被挤压，用铜强度相对下降；1990 年代以后，即使制造业占比没有明显上升，互联网周期仍然通过电力和基础设施需求拉动了铜消费强度。</p>

<p>现在的 AI 周期更像互联网周期的升级版。数据中心是最容易量化的一环。如果美国每年新增装机落在 10GW 到 20GW 区间，仅数据中心就可能拉动美国电力相关铜需求增长 3% 以上。若再考虑配套电源、光伏、储能、电网扩建和电力传输，海外铜需求给到 4% 左右的增长并不激进。</p>

<p>国内需求也呈现类似结构。传统黄铜订单并不强，甚至可能弱于往年；但磁性材料、漆包线、变压器等电力链条的增量很明显。部分企业反馈变压器订单相对历史同期增长约 20%，其中既有国内消耗，也有出口到美国的需求。</p>

<p>这说明 AI 带来的不是单点需求，而是数据中心、电源、电网、变压器、线缆和海外电力基础设施的一整套链条需求。铜正处在这条链条的核心位置。</p>

<h2 id="strategy">八、投资策略：赔率来自低库存、供给扰动和结构需求</h2>

<p>当前铜板块的赔率，来自三个层面的叠加。</p>

<p>第一，关税没有充分定价。COMEX 与 LME 价差已经反映预期，但远未达到理论关税幅度；只要加征路径不被推翻，全球现货流向就会继续偏向美国补库，非美低库存会支撑价格弹性。</p>

<p>第二，矿端供给仍然脆弱。高铜价带来的资源民族主义、劳资纠纷、税务争议和项目扰动，使供给放量难以完全按表推进。市场不愿提前做空明年矿端放量，本身就是对供给不确定性的承认。</p>

<p>第三，需求结构正在换挡。传统需求不强，但 AI 数据中心、电力电网、变压器、漆包线和海外电力基础设施形成新的增量。只要结构需求持续兑现，铜的长期消费强度就会被重新上修。</p>

<p>短期上，7 月更像筑底期，8 月下旬到 9 月是宏观与微观共振的关键窗口。中长期上，铜的核心不是追逐单日涨跌，而是跟踪关税路径、非美库存、矿端扰动和 AI 电力链需求是否继续强化。</p>

<p>本文仅用于产业研究和投资框架梳理，不构成任何投资建议。铜价受宏观流动性、美元、关税政策、矿端事故、库存变化和全球需求影响较大，具体交易需结合个人风险承受能力审慎判断。</p>
"""


DRUG_HTML = r"""
<p>中国创新药 2026 年上半年最大的特征，是产业基本面和资本市场表现之间出现了明显撕裂。政策在改善，研发在突破，BD 在继续放大，头部公司的商业化和盈利能力也在变强；但市场在相当长一段时间里并没有买账，甚至出现好数据也跌、好业绩也跌、大额 BD 也跌的局面。</p>

<p>这种撕裂说明，行业已经不再处于早期“有利好就普涨”的阶段。更准确的判断是：创新药的政策底、业绩底、估值底正在被确认，但这不是全面牛市的自动按钮。它代表产业逻辑进入新周期，不代表所有个股都会同步上涨。</p>

<h2 id="three-bottoms">一、三底共振：政策底、业绩底、估值底</h2>

<p>创新药的“底”，首先是产业底，而不是股价底。政策层面的不确定性正在逐步出清，行业不再持续担心新药上市即降价、研发成果被集采迅速压缩、长期研发投入没有安全感。顶层政策开始从控费优先，转向鼓励真创新、真鼓励创新。</p>

<p>业绩底则来自头部公司的真实修复。过去创新药经常被批评为“讲故事、不赚钱”，许多 BioTech 公司长期只有研发投入，没有药品收入。但 2026 年上半年，越来越多头部企业开始用产品销售、商业化放量和持续盈利证明自身价值，而不只是依靠一次性 BD 改善利润表。</p>

<p>估值底来自长期下跌后的市场再评估。2025 年三季度以来，A 股和港股创新药经历了持续调整，许多公司距离高点跌去 20% 到 30%。政策、临床数据、业绩和 BD 都无法立刻带动股价时，市场情绪已经足够悲观。6 月中下旬以后，部分公司开始反弹，回购增多，也说明产业内部对估值底部的认知在增强。</p>

<p>但必须区分：三底确认不等于全面狂欢。它意味着行业逻辑的底部被确认，不等于所有公司都拥有同等价值。未来最重要的是分化，真正具备临床价值、商业化能力和全球竞争力的公司会被重估，同质化管线和低效研发则会被继续淘汰。</p>

<h2 id="policy">二、政策底最清晰：制度开始保护真创新</h2>

<p>2026 年上半年最确定的变量，是政策端从分散支持走向系统协同。新版《药品管理法实施条例》落地后，创新药数据保护、市场独占期、突破性治疗、附条件批准、优先审评、特别审评等机制获得更明确的制度位置。很多事情过去可能已经在执行，但被行政法规层面确认后，行业预期会更加稳定。</p>

<p>第 12 批国家集采进一步强化了专利期创新药、国谈协议期药品豁免集采的规则。对企业和投资机构来说，这个信号很重要：真正有临床价值的创新药，能够拥有更清晰的自主定价权和收益预期，研发投入可以被更合理地折现。</p>

<p>支付端也在逐渐形成双轨结构。医保目录与商保创新药目录共同推进，虽然商保目录申报数量相比第一年有所减少，但这并不必然是悲观信号。第一版目录承接了多年积累的高价创新药，第二年申报规模回落符合正常节奏。真正需要观察的是，商业保险能否把创新药变成吸引客户的重要工具，能否通过精算、病种设计和目录管理承担更多高价值药品支付。</p>

<p>审评审批提速、境外临床数据互认、国内外同步开发等政策，也在推动创新药更快进入临床和市场。医疗反腐常态化同样对创新药有利，因为它削弱带金销售的旧模式，让竞争回到临床价值、学术价值和患者价值本身。</p>

<h2 id="research">三、研发端从粗放铺管线转向高质量创新</h2>

<p>2026 年上半年，国产创新药研发端出现了明显突破。国内诞生了多款真正意义上的全球首创一类新药，ASCO 等重要学术会议上的口头报告、LBA 和突破性数据数量继续创出高位。ADC、细胞疗法、AI 制药、多靶点 GLP-1、小核酸、放射性药物等前沿方向，都出现了持续兑现。</p>

<p>与之相对，过去依赖同质化扩张的路径正在失效。PD-1、PD-L1、HER2 ADC、单靶点小分子等拥挤赛道仍然内卷严重，价值被持续压缩。行业从 2018 年到 2024、2025 年的粗放铺管线时代，正在真正结束。</p>

<p>这并不是坏事。创新药行业本来就应该分层，本来就不应该所有公司都被笼统称为 BioTech 或创新药企业。真正的 first-in-class、best-in-class、平台型技术和全球化商业能力，会逐渐获得更高估值；低效、重复、缺乏临床价值的 fast-follow 和 me-too 管线，则会被资本和市场自然出清。</p>

<h2 id="bd">四、BD 出海仍是卖方市场，但交易逻辑升级了</h2>

<p>2026 年上半年，中国创新药出海 BD 热度没有下降，交易总额已经逼近千亿美元，百亿美元级总包合作密集落地。更重要的是，交易结构正在改变。</p>

<p>过去几年，国内药企出海多是把比较成熟的单一管线授权出去，换取短期回款。标的集中在临床二期、三期的肿瘤单品，合作模式相对简单，溢价能力也有限。今年上半年，跨国药企的采购逻辑开始从“买成熟产品”转向“买底层技术、买未来管线、买创新能力”。</p>

<p>小干扰 RNA 平台、ADC 偶联技术、AI 研发平台、早期靶点联合研发、NewCo、成本共担和利润共享等模式，说明中国药企不再只是出售单品，而是在出售研发体系、技术平台和未来创新能力。</p>

<p>BD 对创新药企业不是负面标签，而是重要融资和全球化工具。对大量 BioTech 乃至头部创新药企业来说，BD 是稳定现金流、支持后期临床、推进全球开发的关键方式。只要中国资产仍然处在“有东西、有人想买”的状态，BD 就仍然是行业景气的重要证明。</p>

<h2 id="tiers">五、行业分层会加速：四类企业的命运不同</h2>

<p>中国创新药接下来会越来越像一个成熟行业：有头部，有腰部，也有尾部。</p>

<p>第一类是全能型综合龙头，具备自研、商业化、全球临床、大额 BD、稳定现金流和完整闭环。这类企业抗风险能力最强，也最有机会在全球市场中获得长期估值。</p>

<p>第二类是细分平台型 BioTech，依托单一高壁垒技术平台形成差异化优势，通过 BD 变现和临床迭代稳步发展。这类公司不一定体量最大，但可能是行业创新的中坚力量。</p>

<p>第三类是前沿技术新锐公司，包括 AI 制药、RNA、多肽、细胞疗法、放射性药物等方向。它们还处在早期兑现阶段，风险高，但也可能代表未来。</p>

<p>第四类是主要依赖 me-too 或 fast-follow 的小型 BioTech。如果核心管线缺乏差异化，现金流又无法支撑长期临床，这类公司很可能在大浪淘沙中逐渐没落。过去部分企业依靠地方政府输血撑过寒冬，有些确实等到了“东方不亮西方亮”的机会，但更多公司仍要面对真实出清。</p>

<h2 id="beigene-hengrui">六、龙头公司：全球化、第二曲线与真创新能力</h2>

<p>百济神州上半年相对低调，但基本面表现仍然符合行业“一哥”的位置。泽布替尼在全球持续放量，欧美市场销售额继续创新高，依托自建海外商业化、医学和准入体系，BTK 抑制剂龙头地位进一步巩固。BCL-2 抑制剂 sonrotoclax 的全球推进，也让公司有机会形成泽布替尼之外的血液瘤双核心产品矩阵。</p>

<p>百济的重点仍在全球化。它是国内少数真正完成全球自主商业化落地的药企，也具备独立全球多中心临床运营能力。但短板同样存在：实体瘤管线相对弱，ADC、代谢等热门方向存在空白，市场会持续期待它在实体瘤和新平台上给出新的亮点。</p>

<p>恒瑞医药上半年的表现同样强。营收和利润稳步双增，创新药收入占比持续提升，肿瘤之外的代谢、自免板块正在成为第二曲线。HER2 ADC 在结直肠癌三期研究中显示出对传统标准治疗的优势，ASCO 口头报告数量亮眼；与 BMS 的全球战略合作覆盖多款双抗和 ADC 管线，也说明恒瑞正在加速全球化。</p>

<p>恒瑞真正要回答的问题，是第二曲线能否出现王牌产品，以及能否做出真正 first-in-class 或 best-in-class 的世界级管线。它的执行力、商业化和竞争团队无需怀疑，但下一阶段估值跃迁仍要靠更强的原创性和全球竞争力。</p>

<h2 id="sino-cspc-innovent">七、综合药企与平台公司：稳健性、技术平台和商业化</h2>

<p>中国生物制药是头部千亿俱乐部中稳健性、抗风险能力和均衡性很强的代表。公司进行港股回购，体现出对市值和业务表现的信心。仿创双轮驱动下，创新药收入持续提升，肿瘤、呼吸、自免、代谢等领域布局较全面。</p>

<p>它还在探索一带一路国家的临床和商业化空间。全球创新药市场长期由美国、欧洲、日本和中国主导，其他地区支付能力和可及性不足。如果中国药企依托自身供应链、临床能力和区域资源，把创新药推向更多新兴市场，这会形成新的想象空间。</p>

<p>石药集团上半年最有代表性的动作，是将全流程小干扰 RNA 小核酸技术平台整体授权给阿斯利康，覆盖代谢、纤维化、罕见病等多个靶点，总包规模突破百亿美元。这种平台级交易的意义很深：跨国药企不只是买一个单品，而是认可中国公司在 RNA 递送、序列设计和全链条研发上的底层技术。</p>

<p>信达生物上半年非常出圈。减重产品提升了大众认知度，和辉瑞、礼来的接近 200 亿美元重磅合作，则体现出其研发能力和靶点发现能力被全球巨头认可。代谢有望成为肿瘤之外的第二核心赛道，IBI363 在实体瘤领域也展示出较好的疗效和安全性。信达已经稳在中国创新药第一梯队，但核心产品仍偏集中，GLP-1 相关产品商业化竞争会非常激烈。</p>

<h2 id="akeso-adc">八、康方、科伦博泰、百利天恒与 ADC 主线</h2>

<p>康方生物上半年基本面并不差，但舆论压力很大。AK112 作为核心双抗产品，临床数据和市场关注度都很高，也因此被推到过高预期的位置。双抗加化疗对比 PD-1 加化疗的数据本身具备价值，且后续与 K 药头对头研究仍在推进。真正重要的，不是短期舆论狂欢或失望，而是关键临床能否继续验证产品价值，以及海外合作方能否更有效地推进全球开发。</p>

<p>科伦博泰和百利天恒代表 ADC 主线。科伦博泰的 TROP2 ADC 与默沙东合作，依托 K 药联用生态推进大量临床数据，并筹备欧美上市申报。公司还有多条差异化 ADC 管线，上半年新增 ADC 授权交易，并实现 ADC 核心中间体自给，降低研发和生产成本。</p>

<p>百利天恒则继续证明“千亿 ADC 平台”的含金量。EGFR/HER3 双抗 ADC 在 ASCO 上表现突出，6 月获批的自主研发 first-in-class 一类新药，有机会改变部分疾病的临床范式。公司 ADC 管线丰富，市值管理意识强，未来继续拿到百亿美元级 BD 并非没有可能。</p>

<p>荣昌生物、映恩生物等公司也体现出 ADC 赛道的不同路径。荣昌依靠商业化兑现和核心 ADC 放量实现持续扭亏，映恩则通过 B7-H3 ADC、定点偶联、新一代毒素和精准连接子等底层技术证明了中小型 BioTech 在细分技术上也能获得全球认可。</p>

<h2 id="ai-cell-rna-radio">九、AI 制药、细胞疗法、小核酸与放射性药物</h2>

<p>AI 制药正在从概念走向务实落地。晶泰科技与礼来、BMS 等顶级 MNC 达成长期合作，且从零设计的小分子药物进入临床，说明 AI 制药不只是话题炒作，而是可以转化为研发服务、平台合作和自研管线的商业模式。英矽智能虽然上市后股价承压，但在肿瘤、ADC、CGT、小核酸 RNA 等方向仍有不少合作和推进。</p>

<p>AI 制药最有想象力的地方，是“一小博大”。一个小团队如果拥有足够强的算法、平台和靶点设计能力，再叠加国内完善的 CRO、CXO、中试、生产和园区基础设施，就可能以较少人力撬动完整研发链条。</p>

<p>细胞疗法方面，科济药业实体瘤 CAR-T 获批是重要里程碑。实体瘤 CAR-T 长期被认为难度极高，产品商业化落地说明国内在细胞疗法上具备领先能力。通用型 CAR-T、体内 CAR-T、双靶点自体 CAR-T 等下一代方向也在推进。</p>

<p>小核酸方面，瑞博生物完成港交所上市，并与 Madrigal 达成 44 亿美元总规模交易，输出 6 款临床前小 RNA 管线，聚焦代谢功能障碍相关脂肪性肝炎。放射性药物方面，远大医药布局从诊断核素到同位素原料，形成较完整链条，也是值得持续关注的方向。</p>

<h2 id="risks">十、风险仍在：内卷、支付、地缘与现代化</h2>

<p>三底共振不代表风险消失。创新药行业仍然高度不确定，研发成功率低，投入周期长，估值对未来预期极其敏感。中国创新药过去大量做 fast-follow，即使如此研发成功率仍不高，这说明行业天然是高风险、高回报。</p>

<p>内卷仍是核心问题。靶点同质化、源头创新不足、重复管线过多，都需要市场自然出清。资本端已经不再轻易加注同质化项目，二级市场也会继续给内卷赛道折价。</p>

<p>支付端仍需突破。创新药不能长期只依赖医保和患者自费，多元支付体系必须建立。商业保险、医保、医院、药企和监管部门都需要形成更成熟的精算、目录和支付机制。</p>

<p>地缘风险也无法回避。医药是受政治影响的行业，美国保护本国产业，中国也会保护自身产业。优势在于，中国药企正在用大量管线、临床项目、ADC、CAR-T、双抗、小核酸和放射性药物证明自身创新能力。只要更多领域进入卖方市场，外部压力就不必然改变长期趋势。</p>

<p>此外，许多中国药企还需要真正完成现代化。研发、营销、品牌建设、全球组织、人事管理、医学事务和合规体系，都需要向百年 MNC 学习。技术突破之外，现代化管理能力会决定企业能否从中国创新药公司变成全球药企。</p>

<h2 id="conclusion">十一、结论：下半年应为真创新和真业绩买单</h2>

<p>2026 年上半年，中国创新药的政策底、业绩底、估值底已经较为清晰。政策不再是持续压制，头部企业开始用产品销售和商业化盈利证明自己，估值也在长期悲观后出现底部信号。行业正在从旧周期进入新周期。</p>

<p>但新周期不是普涨周期，而是分化周期。真正值得买单的，是临床价值明确、商业化能兑现、BD 能持续、全球化能力真实、技术平台有壁垒的公司。没有临床价值的伪创新、同质化 me-too 和缺乏现金流的低效管线，将继续被淘汰。</p>

<p>下半年最希望看到的，不是情绪炒作，而是市场愿意为真创新、真业绩、真全球化重新定价。中国创新药值得被认真称赞，但也必须接受成熟行业的筛选：好公司走出来，平庸公司被淘汰，产业才会真正变强。</p>

<p>本文仅用于产业研究和投资框架梳理，不构成任何投资建议。创新药行业波动大、研发失败率高、政策和地缘变量复杂，具体标的需结合估值、现金流、临床数据、商业化能力和个人风险承受能力审慎判断。</p>
"""


POSTS = [
    Post(
        slug="copper-tariff-inventory-ai-power-demand-long-cycle",
        title="铜的中长期赔率：关税、库存与 AI 电力需求的三重支撑",
        desc="电解铜关税只要不被推翻，就会持续改变全球现货流向；铜矿供给偏紧叠加 AI 数据中心和电力链需求，正在抬高铜价中长期重心。",
        date="2026-07-17",
        pub_dt=datetime(2026, 7, 17, 16, 45, tzinfo=timezone(timedelta(hours=8))),
        category="投资研究",
        series="周期研究",
        tags=["铜", "电解铜", "有色金属", "关税", "COMEX", "LME", "铜矿", "库存", "AI算力", "数据中心", "电力需求", "资源股"],
        minutes=12,
        article_html=COPPER_HTML,
        cover_kind="copper",
    ),
    Post(
        slug="china-innovative-drug-2026h1-policy-earnings-valuation-bottom",
        title="中国创新药 2026 半年复盘：政策底、业绩底与估值底",
        desc="政策保护真创新、头部企业业绩修复、估值长期调整后出现底部信号；BD 出海、ADC、AI 制药、细胞疗法和小核酸共同推动行业进入分化新周期。",
        date="2026-07-17",
        pub_dt=datetime(2026, 7, 17, 17, 10, tzinfo=timezone(timedelta(hours=8))),
        category="投资研究",
        series="医药投资",
        tags=["创新药", "医药投资", "BD出海", "政策底", "业绩底", "估值底", "药品管理法", "商保", "ADC", "双抗", "AI制药", "细胞疗法", "小核酸", "放射性药物", "百济神州", "恒瑞医药", "信达生物", "康方生物"],
        minutes=24,
        article_html=DRUG_HTML,
        cover_kind="drug",
    ),
]


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def record(path: Path) -> None:
    CHANGED.add(path.relative_to(ROOT).as_posix())


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    record(path)


def term_url(kind: str, term: str) -> str:
    return f"/{kind}/{quote(term)}/"


def meta_links(post: Post) -> str:
    cat = f'<a href="{term_url("categories", post.category)}">{esc(post.category)}</a>'
    tag_links = "&nbsp;".join(f'<a href="{term_url("tags", tag)}">{esc(tag)}</a>' for tag in post.tags)
    return f'<span class="meta-icon" aria-hidden="true">▣</span> {cat}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◇</span> {tag_links}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {post.minutes} min'


def build_toc(body: str) -> str:
    links = []
    for match in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', body):
        links.append(f'<a class="toc-link toc-level-2" href="#{match.group(1)}">{match.group(2)}</a>')
    return '<div class="toc-wrapper"><div class="toc"><div class="toc-title">目录</div><nav>' + "".join(links) + "</nav></div></div>"


def cover_svg(post: Post) -> str:
    if post.cover_kind == "copper":
        return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#3b1d0f"/>
      <stop offset="0.52" stop-color="#9a3412"/>
      <stop offset="1" stop-color="#0f766e"/>
    </linearGradient>
    <filter id="shadow"><feDropShadow dx="0" dy="16" stdDeviation="16" flood-color="#000" flood-opacity="0.32"/></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.18" stroke="#fed7aa" stroke-width="4">
    <path d="M120 700 H1480"/><path d="M120 580 H1480"/><path d="M120 460 H1480"/><path d="M120 340 H1480"/>
    <path d="M300 250 V750"/><path d="M590 250 V750"/><path d="M880 250 V750"/><path d="M1170 250 V750"/>
  </g>
  <path d="M145 655 C310 610 430 650 600 555 C760 465 880 520 1010 410 C1180 265 1320 315 1485 185" fill="none" stroke="#fbbf24" stroke-width="18" stroke-linecap="round" filter="url(#shadow)"/>
  <path d="M145 725 C350 650 520 735 745 630 C930 544 1080 610 1275 470 C1380 395 1455 372 1510 340" fill="none" stroke="#67e8f9" stroke-width="10" stroke-linecap="round"/>
  <circle cx="1485" cy="185" r="52" fill="#fdba74" filter="url(#shadow)"/>
  <circle cx="1275" cy="470" r="38" fill="#5eead4" filter="url(#shadow)"/>
  <text x="100" y="164" fill="#fff7ed" font-family="Noto Sans SC, PingFang SC, Arial" font-size="66" font-weight="800">铜的中长期赔率</text>
  <text x="104" y="246" fill="#ffedd5" font-family="Noto Sans SC, PingFang SC, Arial" font-size="40" font-weight="700">关税 · 库存 · AI 电力需求</text>
  <text x="106" y="320" fill="#ccfbf1" font-family="Noto Sans SC, PingFang SC, Arial" font-size="31" font-weight="600">非美低库存与矿端扰动抬高价格重心</text>
</svg>'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#111827"/>
      <stop offset="0.48" stop-color="#1e3a8a"/>
      <stop offset="1" stop-color="#0f766e"/>
    </linearGradient>
    <filter id="shadow"><feDropShadow dx="0" dy="18" stdDeviation="14" flood-color="#000" flood-opacity="0.32"/></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.2" fill="none" stroke="#bfdbfe" stroke-width="4">
    <path d="M205 675 C320 560 430 560 545 675 S770 790 885 675 S1110 560 1225 675 S1450 790 1565 675"/>
    <path d="M205 555 C320 440 430 440 545 555 S770 670 885 555 S1110 440 1225 555 S1450 670 1565 555"/>
  </g>
  <g filter="url(#shadow)">
    <rect x="238" y="505" width="300" height="122" rx="61" fill="#ecfeff"/>
    <circle cx="306" cy="566" r="36" fill="#0f766e"/>
    <circle cx="386" cy="566" r="36" fill="#3b82f6"/>
    <circle cx="466" cy="566" r="36" fill="#14b8a6"/>
    <path d="M690 635 C810 520 930 580 1040 440 C1135 320 1275 315 1415 235" stroke="#fde68a" stroke-width="16" fill="none" stroke-linecap="round"/>
    <circle cx="1040" cy="440" r="44" fill="#60a5fa"/>
    <circle cx="1415" cy="235" r="54" fill="#facc15"/>
  </g>
  <text x="98" y="150" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="64" font-weight="800">中国创新药 2026 半年复盘</text>
  <text x="102" y="232" fill="#ccfbf1" font-family="Noto Sans SC, PingFang SC, Arial" font-size="39" font-weight="700">政策底 · 业绩底 · 估值底</text>
  <text x="104" y="308" fill="#dbeafe" font-family="Noto Sans SC, PingFang SC, Arial" font-size="32" font-weight="600">从普涨修复转向真创新与真业绩</text>
</svg>'''


def make_cover(post: Post) -> None:
    path = ROOT / "images/posts" / post.slug / "cover.svg"
    write(path, cover_svg(post))


def build_article_page(post: Post, newer: Post | None, older_url: str, older_title: str) -> None:
    template = (ROOT / PREVIOUS_URL.strip("/") / "index.html").read_text(encoding="utf-8")
    start = template.find('<article class="post">')
    end = template.find("</article>", start) + len("</article>")
    if start == -1 or end == -1:
        raise RuntimeError("article template markers not found")
    head = template[:start]
    tail = template[end:]
    head = re.sub(r"<title>.*?</title>", f"<title>{esc(post.title)} - zcxGGmu's Blog</title>", head, flags=re.S)
    replacements = {
        r'<meta name="description" content="[^"]*">': f'<meta name="description" content="{esc(post.desc)}">',
        r'<meta property="og:url" content="[^"]*">': f'<meta property="og:url" content="{esc(post.full_url)}">',
        r'<meta property="og:title" content="[^"]*">': f'<meta property="og:title" content="{esc(post.title)}">',
        r'<meta property="og:description" content="[^"]*">': f'<meta property="og:description" content="{esc(post.desc)}">',
        r'<link rel="canonical" href="[^"]*">': f'<link rel="canonical" href="{esc(post.full_url)}">',
    }
    for pattern, repl in replacements.items():
        head = re.sub(pattern, repl, head)
    if newer is None:
        newer_link = '<a class="newer-posts">下一篇<br>没有更新的文章</a>'
    else:
        newer_link = f'<a class="newer-posts" href="{newer.url_path}">下一篇<br>{esc(newer.title)}</a>'
    article = f'''<article class="post"><div class="post-head-wrapper" style="background-image:url('{post.cover}')"><div class="post-title">{esc(post.title)}<div class="post-subtitle">{esc(post.desc)}</div><div class="post-meta"><time itemprop="datePublished">{post.date}</time>&nbsp;&nbsp;{meta_links(post)}</div></div></div><div class="post-body-wrapper"><div class="post-body" v-pre>{post.article_html}</div></div><nav class="post-pagination">{newer_link}<a class="older-posts" href="{older_url}">上一篇<br>{esc(older_title)}</a></nav>
    </article>'''
    tail = re.sub(r'<div class="toc-wrapper">.*?</div></div>', build_toc(post.article_html), tail, flags=re.S)
    write(ROOT / "2026" / post.slug / "index.html", head + article + tail)


def update_previous_newer() -> None:
    path = ROOT / PREVIOUS_URL.strip("/") / "index.html"
    text = path.read_text(encoding="utf-8")
    text = re.sub(
        r'<a class="newer-posts">下一篇<br>没有更新的文章</a>',
        f'<a class="newer-posts" href="{POSTS[0].url_path}">下一篇<br>{esc(POSTS[0].title)}</a>',
        text,
        count=1,
    )
    write(path, text)


def home_card(post: Post) -> str:
    return f'''<a href="{post.url_path}" class="a-block">
      <div class="post-item-wrapper ">
        <div class="post-item post-item-no-divider">
          <div class="post-item-info-wrapper">
            <div class="post-item-title">{esc(post.title)}</div>
            <div class="post-item-summary">{esc(post.desc)}</div>
            <div class="post-item-meta">{post.date}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {post.minutes} min&nbsp;&nbsp;</div>
          </div>
          <div class="post-item-image-wrapper"><div class="post-item-image" style="background-image:url('{post.cover}')"></div></div>
        </div>
      </div>
    </a>'''


def update_home() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    for post in POSTS:
        text = re.sub(rf'<a href="{re.escape(post.url_path)}" class="a-block">.*?</a>\s*', "", text, flags=re.S)
    marker = f'<a href="{PREVIOUS_URL}" class="a-block">'
    pos = text.find(marker)
    if pos == -1:
        raise RuntimeError("homepage insertion marker not found")
    block = home_card(POSTS[1]) + "\n" + home_card(POSTS[0]) + "\n"
    text = text[:pos] + block + text[pos:]
    write(path, text)


def update_rss() -> None:
    path = ROOT / "index.xml"
    text = path.read_text(encoding="utf-8")
    latest = POSTS[1]
    text = re.sub(r"<lastBuildDate>.*?</lastBuildDate>", f"<lastBuildDate>{format_datetime(latest.pub_dt)}</lastBuildDate>", text)
    for post in POSTS:
        text = re.sub(rf"<item>\s*<title>{re.escape(esc(post.title))}</title>.*?</item>\s*", "", text, flags=re.S)
    items = []
    for post in [POSTS[1], POSTS[0]]:
        items.append(f"""<item>
<title>{esc(post.title)}</title>
<link>{post.full_url}</link>
<guid>{post.full_url}</guid>
<pubDate>{format_datetime(post.pub_dt)}</pubDate>
<description>{esc(post.desc)}</description>
</item>
""")
    text = text.replace("<item>", "".join(items) + "<item>", 1)
    write(path, text)


def archive_item(post: Post) -> str:
    return f'''<div style="padding:8px 0;font-size:15px">
        <span style="color:#999">{post.date}</span>&nbsp;
        <a href="{post.url_path}">{esc(post.title)}</a>
        <span style="margin-left:10px"><span style="color:#999;font-size:12px">{esc(post.category)}</span></span>
      </div> '''


def update_archive() -> None:
    path = ROOT / "archive/index.html"
    text = path.read_text(encoding="utf-8")
    inserted = sum(1 for post in POSTS if post.url_path not in text)
    for post in POSTS:
        text = re.sub(rf'<div style="padding:8px 0;font-size:15px">\s*<span style="color:#999">{post.date}</span>&nbsp;\s*<a href="{re.escape(post.url_path)}">.*?</div>\s*', "", text, flags=re.S)
    if inserted:
        text = re.sub(
            r'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">(\d+) 篇</span>',
            lambda m: f'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">{int(m.group(1)) + inserted} 篇</span>',
            text,
            count=1,
        )
    marker = f'<a href="{PREVIOUS_URL}">'
    pos = text.find(marker)
    if pos == -1:
        raise RuntimeError("archive marker not found")
    start = text.rfind('<div style="padding:8px 0;font-size:15px">', 0, pos)
    if start == -1:
        raise RuntimeError("archive insertion point not found")
    block = archive_item(POSTS[1]) + archive_item(POSTS[0])
    text = text[:start] + block + text[start:]
    write(path, text)


def taxonomy_item(post: Post) -> str:
    return f'''<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">
        <a href="{post.url_path}" style="font-size:16px;text-decoration:none">{esc(post.title)}</a>
        <span style="color:#999;font-size:13px;margin-left:10px">{post.date}</span>
      </div> '''


def make_term_page(kind: str, term: str, title_prefix: str, emoji: str, posts: list[Post]) -> int:
    d = ROOT / kind / term
    path = d / "index.html"
    if path.exists():
        text = path.read_text(encoding="utf-8")
        inserted = sum(1 for post in posts if post.url_path not in text)
        for post in posts:
            text = re.sub(rf'<div style="padding:12px 0;border-bottom:1px solid rgba\(128,128,128,0\.08\)">\s*<a href="{re.escape(post.url_path)}".*?</div>\s*', "", text, flags=re.S)
        if inserted:
            text = re.sub(r"共 (\d+) 篇文章", lambda m: f"共 {int(m.group(1)) + inserted} 篇文章", text, count=1)
        first = text.find('<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">')
        if first == -1:
            first = text.find("</div></div></div>")
        text = text[:first] + "".join(taxonomy_item(p) for p in posts) + text[first:]
    else:
        inserted = len(posts)
        label = f"{title_prefix}: {term}" if title_prefix else term
        h1 = f"{emoji} {term}" if emoji else label
        text = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#f8fafc"><meta name="description" content="{esc(label)}"><meta property="og:title" content="{esc(label)} - zcxGGmu's Blog"><link rel="canonical" href="{SITE}/{kind}/{quote(term)}/"><link rel="stylesheet" href="/scss/journal.min.css"><link rel="stylesheet" href="/scss/modern.min.css?v=20260607-sidebar-collapse"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=Noto+Sans+SC:wght@400;500;700&amp;family=JetBrains+Mono:wght@400;500;600;700&amp;display=swap"><link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Material+Icons&amp;display=swap"><title>{esc(label)} - zcxGGmu's Blog</title></head><body><div class="stream-container"><div class="post-list-container" style="min-height:100vh"><div style="padding:40px 35px"><h1 style="font-size:30px;font-weight:500;margin-bottom:10px">{esc(h1)}</h1><p style="color:#999;margin-bottom:30px">共 {len(posts)} 篇文章</p>{''.join(taxonomy_item(p) for p in posts)}</div></div></div><script src="/js/journal.js"></script></body></html>'''
    write(path, text)
    return inserted


def update_term_index(kind: str, term: str, delta: int) -> None:
    path = ROOT / kind / "index.html"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    href = f"/{kind}/{quote(term)}/"
    if href in text:
        pattern = re.compile(rf'(<a href="{re.escape(href)}"[^>]*>{re.escape(esc(term))}<span style="color:#999[^>]*>\()(\d+)(\)</span></a>)')
        text = pattern.sub(lambda m: f"{m.group(1)}{int(m.group(2)) + delta}{m.group(3)}", text, count=1)
    else:
        if kind == "tags":
            item = f'<a href="{href}" style="display:inline-block;margin:5px 8px;padding:4px 12px;background:rgba(25,118,210,0.06);border-radius:4px;font-size:15px">{esc(term)}<span style="color:#999;font-size:12px;margin-left:4px">({delta})</span></a>\n'
        else:
            item = f'<a href="{href}" class="a-block" style="padding:8px 0;font-size:18px">{esc(term)}<span style="color:#999;margin-left:8px">({delta})</span></a>\n'
        pos = text.find("</div></div></div>")
        if pos != -1:
            text = text[:pos] + item + text[pos:]
    write(path, text)


def update_taxonomies() -> None:
    for kind, title_prefix, emoji, attr in [
        ("categories", "分类", "", "category"),
        ("series", "", "📚", "series"),
    ]:
        grouped: dict[str, list[Post]] = {}
        for post in POSTS:
            grouped.setdefault(getattr(post, attr), []).append(post)
        for term, posts in grouped.items():
            ordered = sorted(posts, key=lambda p: p.pub_dt, reverse=True)
            inserted = make_term_page(kind, term, title_prefix, emoji, ordered)
            if inserted:
                update_term_index(kind, term, inserted)
    grouped_tags: dict[str, list[Post]] = {}
    for post in POSTS:
        for tag in post.tags:
            grouped_tags.setdefault(tag, []).append(post)
    for tag, posts in grouped_tags.items():
        ordered = sorted(posts, key=lambda p: p.pub_dt, reverse=True)
        inserted = make_term_page("tags", tag, "标签", "🏷️", ordered)
        if inserted:
            update_term_index("tags", tag, inserted)


def validate() -> None:
    failures: list[str] = []
    forbidden = ["B站", "bilibili", "哔哩", "视频里", "视频中", "原视频", "音频里", "音频中", "UP主", "up主", "这期", "本期", "作者说", "他提到", "观看", "点赞", "订阅", "欢迎收看"]
    for post in POSTS:
        path = ROOT / "2026" / post.slug / "index.html"
        text = path.read_text(encoding="utf-8")
        for word in forbidden:
            if word in text:
                failures.append(f"{post.slug}: forbidden word {word}")
        h2s = re.findall(r'<h2 id="([^"]+)">', text)
        tocs = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', text)
        if h2s != tocs:
            failures.append(f"{post.slug}: toc mismatch")
        for required in [post.title, post.desc, post.cover, post.category]:
            if required not in text:
                failures.append(f"{post.slug}: missing {required}")
    home = (ROOT / "index.html").read_text(encoding="utf-8")
    links = re.findall(r'<a href="(/2026/[^"]+/)" class="a-block">', home)
    expected = [
        "/2026/codeinsights-local-first-agent-workbench/",
        "/2026/what-you-need-to-learn-from-claw-code-repo/",
        "/2026/gaojingqi-investment-system/",
        "/2026/ai-revolution-permanent-underclass-career-selection/",
        "/2026/live-longer-than-earn-fast-investment-infinite-game/",
        POSTS[1].url_path,
        POSTS[0].url_path,
        PREVIOUS_URL,
    ]
    if links[:8] != expected:
        failures.append(f"homepage order mismatch: {links[:8]}")
    rss = (ROOT / "index.xml").read_text(encoding="utf-8")
    for post in POSTS:
        if post.full_url not in rss:
            failures.append(f"rss missing {post.full_url}")
    try:
        ET.parse(ROOT / "index.xml")
    except Exception as exc:
        failures.append(f"rss xml parse failed: {exc}")
    prev = (ROOT / PREVIOUS_URL.strip("/") / "index.html").read_text(encoding="utf-8")
    if POSTS[0].url_path not in prev:
        failures.append("previous latest article does not link newer to copper article")
    copper = (ROOT / POSTS[0].url_path.strip("/") / "index.html").read_text(encoding="utf-8")
    if POSTS[1].url_path not in copper or PREVIOUS_URL not in copper:
        failures.append("copper article pagination incorrect")
    drug = (ROOT / POSTS[1].url_path.strip("/") / "index.html").read_text(encoding="utf-8")
    if POSTS[0].url_path not in drug or "没有更新的文章" not in drug:
        failures.append("drug article pagination incorrect")
    for post in POSTS:
        for path in [
            ROOT / "2026" / post.slug / "index.html",
            ROOT / "images/posts" / post.slug / "cover.svg",
            ROOT / "categories" / post.category / "index.html",
            ROOT / "series" / post.series / "index.html",
        ]:
            if not path.exists():
                failures.append(f"missing {path}")
        for tag in post.tags:
            if not (ROOT / "tags" / tag / "index.html").exists():
                failures.append(f"missing tag page {tag}")
    if failures:
        raise SystemExit("\n".join(failures))
    print("validation passed")


def main() -> None:
    for post in POSTS:
        make_cover(post)
    build_article_page(POSTS[0], POSTS[1], PREVIOUS_URL, PREVIOUS_TITLE)
    build_article_page(POSTS[1], None, POSTS[0].url_path, POSTS[0].title)
    update_previous_newer()
    update_home()
    update_rss()
    update_archive()
    update_taxonomies()
    validate()
    changed_path = ROOT / "tasks" / "publish-copper-and-innovative-drug-2026h1-changed-files.json"
    write(changed_path, json.dumps(sorted(CHANGED), ensure_ascii=False, indent=2))
    print(json.dumps({"changed": sorted(CHANGED), "urls": [p.full_url for p in POSTS]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
