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

ROOT_HINT = Path("/tmp/blog-publish-bv1ch-20260805.path")
ROOT = Path(os.environ.get("BLOG_ROOT") or ROOT_HINT.read_text(encoding="utf-8").strip())
BASE_PATH = Path(__file__).with_name("publish-physical-ai-three-article-batch.py")
if not BASE_PATH.exists():
    BASE_PATH = ROOT / "tasks" / "publish-physical-ai-three-article-batch.py"

spec = importlib.util.spec_from_file_location("base_publisher_robot_copper_20260805", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Unable to load base publisher: {BASE_PATH}")
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
_BASE_VALIDATE = base.validate


ROBOT_BODY = """
<p><img src="/images/posts/robot-sector-bottom-rebound-electronic-skin-dexterous-hand/cover.svg" alt="机器人板块底部反弹：电子皮肤、灵巧手电机与供应链再定价"></p>
<p>机器人板块正在进入一段由多重催化共同推动的底部修复窗口。短期看，板块经历调整后，核心公司估值和交易热度已经明显回落；中期看，宇树等国内机器人公司的上市进程、Google 机器人推理模型的发布、Optimus 远期产能目标上修，以及北美供应链的小批量订单验证，都在把机器人从概念交易重新拉回产业兑现。</p>
<p>这一轮机会的重点不是泛泛地买“机器人”三个字，而是抓住两个更清晰的增量环节：电子皮肤和灵巧手电机。前者对应机器人与外界交互的触觉和外观功能化，单机价值量高，格局尚未完全固化；后者对应灵巧手自由度提升和国产替代，属于从样机走向量产时绕不开的核心部件。</p>

<h2 id="catalysts">一、多重催化集中出现，板块底部条件正在形成</h2>
<p>机器人板块最重要的变化，是产业催化开始从单点消息变成连续事件。宇树的资本市场进程临近关键窗口，市场会重新评估国内机器人本体公司的估值映射。一旦核心本体公司进入上市节奏，供应链、零部件和相关国产替代标的都会获得新的比较坐标。</p>
<p>同时，Google 机器人推理模型的发布给“机器人应该如何思考和执行动作”提供了新的技术支撑。模型能力的变化不只是让机器人能识别物体，而是让机器人可以对每一步动作进行推理，完成下蹲、整理房间、协作等更广泛的任务。对二级市场而言，这类技术进展能在底部给具身智能方向提供估值支撑。</p>
<p>第三个催化来自 Optimus 远期产能目标上修。过去测算人形机器人空间时，市场多以百万台量级作为远期假设；如果远期目标被抬升到千万台量级，供应链的单机价值量和远期空间都会被重新估算。产业链反馈的小批量订单、9 月前后的准备节点、年底前的产能准备，以及明年十几万台级别的潜在产能规划，都是后续跟踪重点。</p>

<h2 id="bottom">二、为什么说现在更接近底部反弹窗口</h2>
<p>当前机器人板块不是在高位追逐故事，而是在调整后等待产业和业绩共同验证。中报陆续披露之后，很多公司的短期利润压力会被市场重新定价，原先悬着的不确定性会逐步落地。业绩底和产业催化叠加时，板块更容易出现向上修复。</p>
<p>这也是当前策略的关键：不是所有机器人标的都值得买，而是要在底部区间寻找已经跌出安全边际、同时又能被新订单、新客户、新产品验证的公司。单纯概念股在反弹中弹性可能很高，但持续性取决于订单和业绩；真正值得重视的是已经和北美客户、国内本体厂、核心零部件链条发生真实接触的公司。</p>

<h2 id="two-links">三、两条主线：电子皮肤和灵巧手电机</h2>
<p>这一轮机器人板块的增量链条，最值得优先看的不是传统减速器，也不是已经被反复交易的总成环节，而是电子皮肤和灵巧手电机。</p>
<p>电子皮肤的逻辑在于单机价值量高。机器人一旦从工厂搬运、展示演示走向更复杂交互，触觉、表面材料、外观件和功能性覆盖件的重要性会显著上升。手部皮肤的价值量可能达到万元级，身体皮肤也会形成新的零部件市场。</p>
<p>灵巧手电机的逻辑在于用量提升。机器人真正能工作，关键在手。灵巧手自由度提高，电机、传感器、控制器和结构件的数量都会上升。若按单个电机数百元级别测算，单机价值量可以超过万元；如果未来进入十万台以上规模，供应商的收入弹性会非常明显。</p>

<h2 id="electronic-skin">四、电子皮肤：高价值量、低渗透率和新龙头窗口</h2>
<p>电子皮肤目前最吸引人的地方，是价值量高但行业龙头尚未完全形成。过去市场对机器人皮肤和外观件的重视度不高，因为早期机器人更强调走路、控制和关节。但一旦机器人进入量产阶段，皮肤、触觉和功能外观件会从“可有可无”变成体验与安全的关键部件。</p>
<p>电子皮肤需要解决触觉感知、柔性材料、耐用性、贴合工艺、批量制造和成本下降等问题。单个方案现在成本仍高，但随着批量化生产推进，成本会下降，应用成熟度会提高。这个过程类似很多汽车零部件从高端车型向规模化车型渗透：早期看起来贵，量起来之后成本曲线会迅速改变。</p>
<p>在这个环节里，岱美股份和福莱新材值得重点跟踪。岱美原有主业具备汽车内饰和功能件基础，是全球遮阳板龙头，汽车客户基础和材料工艺积累较强；在机器人电子皮肤方向，公司与北美客户紧密对接，身体和手部皮肤都有潜在价值量。福莱新材则具备材料和功能膜基础，触觉传感器方向已有客户订单和本体厂合作线索，是从材料端切入机器人触觉链条的重要观察对象。</p>

<h2 id="daimei">五、岱美股份：主业韧性与电子皮肤期权叠加</h2>
<p>岱美股份的底层安全垫来自主业。公司在汽车内饰件尤其是遮阳板领域具备全球份额，客户基础、工艺能力和海外供应链能力较强。即使机器人业务还没有形成大规模收入，主业仍能提供现金流和估值支撑。</p>
<p>中报预告显示，公司在欧洲业务亏损压力下仍保持较强经营韧性，保险赔付等项目后续还可能继续到账。短期市场对汽车零部件公司利润波动反应较大，但一旦非经常性影响和欧洲业务压力被逐步消化，主业稳定性会重新成为估值基础。</p>
<p>机器人电子皮肤则是向上的期权。身体皮肤和手部皮肤的单机价值量不同，后者更高。若未来进入北美客户供应链，岱美不只是传统汽车零部件公司，而是具备机器人功能外观件和电子皮肤想象空间的供应商。底部区间看，它的吸引力来自“主业不贵 + 机器人期权未充分定价”。</p>

<h2 id="fulai">六、福莱新材：触觉传感器从小订单走向量产验证</h2>
<p>福莱新材的重点在于材料能力和触觉传感器方向。年初以来股价调整较充分，但公司在灵巧手、触觉传感器和机器人客户方面仍有进展。小批量订单不应被简单理解为业绩贡献，而应看作进入客户体系、验证产品可用性的信号。</p>
<p>机器人触觉传感器的难点在于稳定性、灵敏度、柔性贴合和成本控制。早期订单规模不大很正常，关键是能否伴随客户的样机、试产和量产节点持续迭代。若公司能在多个本体厂或北美客户链条中反复验证，后续弹性会来自订单从传感器样品转向批量供应。</p>
<p>这个方向的投资方法，是把福莱新材视为电子皮肤和触觉传感器的早期弹性标的。它不是低波动高股息资产，而是需要用客户、样机、订单、良率和量产节点持续跟踪的成长性标的。</p>

<h2 id="motor">七、灵巧手电机：单机价值量和国产替代同时打开</h2>
<p>灵巧手电机是机器人从“能动”走向“能干活”的关键。腿部和躯干让机器人移动，手部决定它能否抓取、整理、装配、开门、拿工具、完成精细操作。手部自由度越高，对小型电机、控制和传动的要求越高。</p>
<p>按每个电机数百元测算，灵巧手电机单机价值量可以超过万元。若明年产能进入十几万台级别，供应链收入弹性会非常可观。更重要的是，这个环节目前还没有形成绝对龙头，国内供应商处在快速验证阶段，谁先拿到图纸、开模、样件和客户认可，谁就有机会在量产前建立卡位优势。</p>
<p>恒帅股份是当前走得较快的方向之一。公司已经拿到两款灵巧手电机图纸并进入开模阶段，开模本身意味着客户开始为产品验证投入真金白银。这个阶段还不是利润释放期，却是供应链地位形成期。后续要跟踪的是样件验证、客户反馈、定点节奏和量产价格。</p>

<h2 id="motor-chain">八、伟创电气等电机链：调整后的赔率修复</h2>
<p>电机链条中，伟创电气等公司此前跟随机器人供应链预期波动较大。市场对具体客户、配套关系和订单节奏的预期出现分歧后，股价也经历了充分调整。</p>
<p>这类公司的机会不在于短期讲故事，而在于能否继续围绕本体厂和核心客户推进电机、驱动和控制方案。如果客户合作持续、海外产能和本地化配套能力跟上，调整之后的赔率会改善。反之，如果验证节奏低于预期，估值也会继续承压。</p>
<p>因此，电机链条的交易纪律要比电子皮肤更严格：左侧可以看底部修复，但右侧必须看图纸、开模、样件、定点和订单。没有这些节点，单纯估值低并不足以支撑趋势行情。</p>

<h2 id="xinquan">九、新泉股份：短期业绩扰动不改机器人期权</h2>
<p>新泉股份二季度收入端基本符合预期，但利润端低于预期，主要受到约 6300 万元减值和管理费用阶段性增加影响。减值更多与应收账款计提有关，未来并非完全没有冲回可能；管理费用增加则与海外布局和新业务投入相关。</p>
<p>从收入结构看，吉利、理想等客户贡献仍在增长，汽车内饰主业并没有失速。短期利润下修后，全年利润预期被调整到约 9 亿元附近，市场已经把一部分失望反映进价格。真正需要跟踪的是，下半年和四季度之后，机器人业务能否从期权进入更清晰的验证阶段。</p>
<p>公司机器人方向有两个重要变化。第一，相关机器人公司股权转让给凯迪后，合作关系更加明确，后续围绕关节、外壳、功能外观件等方向的协同值得跟踪。第二，公司在北美已经有机器人相关小批量出货，虽然金额很小，但代表从讨论走向交付。新泉本来就是北美核心客户汽车供应链的重要公司，机器人业务若以北美基地为切入口，后续配套空间值得继续观察。</p>

<h2 id="strategy">十、投资策略：左侧买底部，右侧买兑现</h2>
<p>机器人板块当前适合采用分层策略。底部仓位可以放在估值已经调整、主业有支撑、同时具备机器人期权的公司，例如岱美股份、新泉股份这类有传统业务安全垫的标的。进攻仓位可以放在电子皮肤、触觉传感器、灵巧手电机等高弹性环节，例如福莱新材、恒帅股份以及相关电机链公司。</p>
<p>左侧买入的逻辑是板块调整充分、产业催化密集、估值回到底部。右侧加仓的依据则必须是订单和客户验证：电子皮肤看开模和定点，触觉传感器看批量订单，灵巧手电机看图纸、样件和量产节奏，新泉看机器人业务收入和北美配套进展。</p>
<p>如果后续宇树资本市场进程、Google 机器人模型生态、Optimus 产能规划和国内供应链订单持续验证，机器人板块会从底部反弹走向趋势修复。如果这些催化落空，反弹也只能按交易性机会处理。</p>

<h2 id="risk">十一、风险：量产节奏和技术路线仍未完全确定</h2>
<p>机器人投资最大的风险，是把远期空间提前当成当期利润。产能目标并不等于真实订单，样机验证也不等于量产收入。Optimus 或国内本体厂的时间表若推迟，供应链公司股价会出现较大波动。</p>
<p>第二个风险是技术路线变化。电子皮肤、触觉传感器、灵巧手电机、执行器、关节和外观件都可能随着版本迭代发生方案切换。现在走得快的公司，不代表一定能在后续版本中持续保持份额。</p>
<p>第三个风险是业绩和估值错配。很多机器人供应链公司主业仍来自汽车、材料、电机或工业自动化，短期利润受原有业务影响很大。若主业低于预期，即使机器人期权存在，股价也可能继续承压。</p>

<h2 id="conclusion">结论：底部反弹的核心，是从概念回到供应链验证</h2>
<p>机器人板块正在从单纯主题交易，回到产业验证驱动。宇树、Google 机器人模型、Optimus 远期产能目标和供应链小批量订单，共同构成底部反弹的外部催化；电子皮肤、触觉传感器、灵巧手电机和机器人功能外观件，则是更值得细看的内部增量。</p>
<p>当前最重要的不是追高最强概念，而是在底部区间选择有主业安全垫、有客户进展、有单机价值量、有订单验证路径的公司。电子皮肤看岱美股份和福莱新材，灵巧手电机看恒帅股份及相关电机链，新泉股份则是汽车主业与机器人期权叠加的代表。后续真正决定行情级别的，是订单、定点、产能和利润兑现。</p>
"""


COPPER_BODY = """
<p><img src="/images/posts/copper-strongest-metal-h2-rate-cut-tariff-nonferrous-wave/cover.svg" alt="铜才是下半年最强王者：降息转向、关税扰动与有色主升浪"></p>
<p>下半年有色金属的核心判断很清晰：8 月到 9 月是逐步加仓窗口，四季度有望进入更顺的主升阶段。逻辑不是单一商品的短期涨跌，而是宏观转向与供给基本面共振。宏观上，美国利率从高位维持转向降息预期，商品资产的估值压制会逐步减弱；基本面上，铜的供给下修、关税扰动和需求韧性最强，黄金受益降息，铝有供给红线支撑，锂和锡则有阶段性修复弹性。</p>
<p>在排序上，黄金和铜应排在最前面，铝次之，锂和锡更偏阶段性修复与弹性交易。若只选一个下半年最强主线，铜仍然是最值得重视的金属：美国铜关税带来的库存迁移，矿端供给持续下修，国内精炼铜产量和开工率回落，叠加四季度需求环比改善，共同构成重新冲击前高甚至创新高的基础。</p>

<h2 id="macro-window">一、有色的时间窗口：8 到 9 月布局，四季度看主升</h2>
<p>有色金属的行情往往不是等到所有信号都确认后才开始，而是在宏观预期转向和基本面改善的交汇处提前启动。当前的窗口更像是左侧到右侧之间：市场尚未完全定价降息，但已经开始不相信高利率能长期维持；商品基本面尚未全面爆发，但供给端已经出现越来越多扰动。</p>
<p>8 月大概率仍是震荡和布局期，因为非农、通胀、PCE、杰克逊霍尔年会等关键事件还会反复扰动市场。但越是这种扰动期，越适合逐步建立有色仓位。若数据不佳导致商品或有色板块回调，反而是更好的加仓时点。</p>
<p>真正的顺风窗口更可能出现在 9 月之后。届时就业和通胀数据会给美联储更多决策依据，PCE 口径调整也可能带来核心通胀回落。如果降息路径变得更顺，有色金属尤其是黄金和铜，会同时受益于流动性改善和风险偏好修复。</p>

<h2 id="fed">二、美联储转向：市场已经不相信长期高利率</h2>
<p>7 月美联储维持利率不变，但市场已经不再完全相信高利率可以无限期维持。美债收益率创高之后，商品整体偏弱，但背后并不是需求崩塌，而是利率预期仍在反复。接下来决定有色节奏的核心，是就业和通胀数据能否持续回落。</p>
<p>就业端已经沿着 2025 年以来的下降趋势走弱。若后续非农数据继续低于市场预期，市场会快速上修降息概率。通胀端则受到油价和关税扰动，但油价中枢很难重新回到前期高位，这会对通胀形成压制。</p>
<p>美联储内部存在分歧，市场需要数据来打破僵局。若 8 月底杰克逊霍尔年会仍然释放偏鹰信号，板块可能短期挖坑；但在估值低位、基本面不差的情况下，低位利空的杀伤力有限，反而容易形成更好的买点。</p>

<h2 id="gold">三、黄金：降息预期重新打开高位突破条件</h2>
<p>黄金的主逻辑依然是降息预期从减弱到重新增强。当前金价处在高位平台震荡，前期均线和情绪压力需要时间消化。若后续就业数据走弱、核心通胀回落，美债实际利率下行，黄金向上突破会更顺。</p>
<p>黄金并不需要强经济才能上涨。它更需要的是实际利率下降、美元压力减弱、央行配置和避险需求共同支撑。当前宏观环境并不完美，但赔率已经比前期更好。若四季度降息预期兑现，黄金仍然是有色板块里确定性靠前的方向。</p>
<p>配置上，A 股可以重点跟踪赤峰黄金、招金黄金等弹性方向，港股则可跟踪中国黄金国际、灵宝黄金等品种。黄金股的弹性来自金价与成本之间的利润扩张，风险主要在于金价短期横盘过久、美元反弹和市场对降息重新降温。</p>

<h2 id="copper-tariff">四、铜关税：短期扰动，长期强化美国囤铜逻辑</h2>
<p>铜是这一轮基本金属里表现最强的品种，核心催化之一是美国铜关税。关税最终结果尚未完全落定，但不论是否立即落地，它已经改变了全球铜库存和贸易流向。</p>
<p>如果不加关税，COMEX 与 LME 的价差会回落，美国铜价会向国际价格收敛；但对 LME 铜价的冲击不会特别大。原因在于，已经运到美国的铜并不会轻易重新流出，除非海外价格显著高于美国价格并覆盖运输、融资和交易成本。短期价差波动更多影响区域套利，不等于全球铜价趋势反转。</p>
<p>如果加关税，尤其是以 2027、2028 年分阶段方式推进，美国囤铜逻辑会继续。美国希望把铜纳入更强的战略金属管理，同时发展本土冶炼和加工产业。在这种背景下，提前备货和库存迁移会加剧全球市场紧张。</p>

<h2 id="us-inventory">五、美国库存并不算过高，只是战略备货的开始</h2>
<p>当前美国显性铜库存已经明显上升，COMEX 库存折算后约六十多万吨，美国 LME 仓库也有接近十万吨，合计接近七十万吨级别。如果再考虑隐性库存，实际库存可能达到一百四十万到一百五十万吨。</p>
<p>表面看，这个库存规模不低。但美国表观铜消费量大约占全球 7% 到 8%，对应每年约一百七十万吨级别。若美国真的进入关税和战略备货周期，目前库存也只是接近一年消费量，并不能说明显过剩。</p>
<p>这也是铜价难以轻易转空的原因。市场担心美国库存流出冲击海外价格，但现实条件并不支持大规模回流。只要关税预期和战略备货动机仍在，美国库存更可能成为区域定价扰动，而不是全球铜价崩塌的源头。</p>

<h2 id="copper-supply">六、铜供给：矿端和冶炼端都在下修</h2>
<p>铜的第二条逻辑是供给持续下修。无论国内还是海外，市场对铜矿供给的预测一直在往下调。国内精炼铜产量在二三月见顶之后已经连续数月环比下降，行业开工率也回落到 2021 年以来较低位置。</p>
<p>这说明供给端不是口头紧张，而是在实际数据中体现出来。矿山品位下降、项目扰动、政策影响、检修和原料约束，会逐步传导到冶炼端。即使短期有库存和进口扰动，供给趋势仍然偏紧。</p>
<p>铜最好的地方在于，它的供给修复很慢。新矿开发周期长，资本开支约束强，环保和社区问题复杂。需求如果只是温和增长，供给紧张也足以支撑价格；如果四季度需求环比改善，铜价弹性会更明显。</p>

<h2 id="copper-demand">七、铜需求：淡季不弱，四季度更顺</h2>
<p>需求端比市场想象得更强。8 月属于传统淡季，需求不太可能出现超预期爆发，但国内铜库存仍在较低位置，预计只是小幅累库，对价格影响有限。真正值得看的，是四季度需求环比改善。</p>
<p>电网、新能源、数据中心、制造业更新、海外库存迁移和美国关税预期，共同抬高铜需求的韧性。铜不像某些品种那样单靠情绪推动，它有电气化、基建、AI 数据中心和制造业资本开支共同支撑。</p>
<p>因此，下半年铜价更可能表现为震荡中枢上移。若宏观转向顺利，铜价重新拿下上半年高点并创新高，是更符合基本面的路径。</p>

<h2 id="aluminum">八、铝：弱于铜，但供给红线和海外复产不及预期提供支撑</h2>
<p>铝的排序弱于铜，但并不差。近期铝价偏强，一方面是海外复产节奏没有市场之前担心得那么快，部分海外产能释放速度低于预期；另一方面，国内电解铝产能红线不会轻易放松。</p>
<p>黄河流域取水定额等政策，对电解铝也有边际影响。黄河流域在国内电解铝产量中占比较高，若水资源、能耗和产能政策继续收紧，铝供给弹性会受到限制。铝的逻辑不是强爆发，而是供给天花板和成本支撑。</p>
<p>配置上，港股若偏股息和低成本，可以跟踪中国宏桥；A 股若看价格弹性，则云铝股份、神火股份等更具周期修复特征。铝的风险在于海外产能释放超预期、需求走弱以及氧化铝和电力成本波动。</p>

<h2 id="lithium">九、锂：强现实与弱预期的修复交易</h2>
<p>锂的核心矛盾，是强现实和弱预期。市场一直担心明年供给过剩和需求走弱，但短期库存和价格并没有完全支持极端悲观。前期利好基本被价格消化，缺少新的边际催化时，锂价容易偏弱震荡。</p>
<p>但这种状态不是长期常态。7 月产业链去库约两万吨，8 月去库力度大概率不会比 7 月差太多；进入 9 月之后，旺季需求可能带来更明显去库。若库存继续下降，锂价在 12 万到 13 万附近形成底部区间的概率较高。</p>
<p>因此，锂更适合作为四季度修复方向，而不是当前最强主线。它的交易关键在于：库存是否继续下降、排产是否改善、价格是否守住底部区间。如果这些信号成立，四季度锂价和锂股都有修复空间。</p>

<h2 id="tin">十、锡：供给扰动叠加 AI 半导体需求</h2>
<p>小金属里，锡值得单独重视。锡价维持高位震荡的原因，一是供给扰动持续，二是需求端有 AI 和半导体加持。</p>
<p>供给端，全球重要锡矿供给国存在不同程度扰动。印尼计划上调相关资源使用费和税率，可能挤压成本曲线尾部矿山；缅甸锡矿复产进度不及预期；其他地区也存在疫情、政策和生产中断风险。锡本来就是小品种，供给扰动对价格弹性更大。</p>
<p>需求端，锡在半导体焊料和电子产业链中占比高。AI 数据中心快速发展，会带动高端电子和半导体材料需求。锡股短期可能跟随科技股波动，但从供需结构看，高位震荡仍有支撑。标的上，锡业股份是更直接的观察对象。</p>

<h2 id="ranking">十一、配置排序：黄金和铜靠前，铝次之，锂锡看弹性</h2>
<p>有色板块的排序可以分成三层。第一层是黄金和铜，前者受益降息和实际利率下行，后者受益关税、供给和需求三重支撑。它们是下半年最值得配置的核心。</p>
<p>第二层是铝。铝没有铜那么强的全球供给缺口故事，但国内产能天花板、海外复产低于预期和成本支撑，使得铝不应被低估。低成本龙头和高股息标的仍有配置价值。</p>
<p>第三层是锂和锡。锂看库存、排产和四季度修复；锡看供给扰动和 AI 半导体需求。它们更适合做弹性仓位，而不是组合的核心底仓。</p>

<h2 id="stocks">十二、标的线索：用 Beta 做底仓，用弹性做进攻</h2>
<p>黄金方向，A 股可重点跟踪赤峰黄金、招金黄金，港股可跟踪中国黄金国际、灵宝黄金。铜方向，如果做核心配置，可以看紫金矿业和洛阳钼业；如果追求弹性，可以看江西铜业、铜陵有色等与铜价弹性更强的公司。</p>
<p>铝方向，港股偏股息和成本优势可以看中国宏桥；A 股偏价格弹性可以看云铝股份、神火股份。锂方向要等库存和价格信号更明确，锡方向则以锡业股份为代表。</p>
<p>这些标的不是同一种资产。紫金、洛钼更像全球资源 Beta，江西铜业和铜陵有色更偏价格弹性，中国宏桥更偏低成本和股息，云铝、神火更偏电解铝价格和成本结构，锡业股份则是小金属供给扰动品种。组合构建时应把底仓和进攻仓分开。</p>

<h2 id="execution">十三、买入策略：回调加仓，不等完美右侧</h2>
<p>当前最合适的策略，是 8 月到 9 月逐步加仓，而不是等四季度行情完全确认。原因在于，等降息、供给和需求全部验证，价格往往已经提前反映。左侧布局的关键，是只买逻辑最硬、估值不贵、回调后赔率变好的方向。</p>
<p>如果 8 月非农、CPI、PCE 或杰克逊霍尔讲话带来短期回调，应把它视为较好的加仓窗口。尤其是铜和黄金，只要核心逻辑没有被破坏，宏观扰动带来的下跌更像买点，而不是趋势反转。</p>
<p>仓位上，可以先以黄金和铜建立核心仓位，再用铝做防守和股息补充，用锂、锡做弹性仓位。进入 9 月后，如果降息预期上修、铜库存没有明显恶化、四季度需求开始改善，再逐步提高仓位。</p>

<h2 id="risks">十四、风险：宏观和供给都可能反复</h2>
<p>有色板块的风险首先来自宏观。如果就业数据重新走强、通胀反弹超预期、美联储重新偏鹰，降息交易会降温，黄金和铜都可能出现阶段性调整。</p>
<p>第二个风险来自关税和库存。如果美国铜关税落地方式低于预期，COMEX 与 LME 价差会收敛，短期交易会波动。虽然对 LME 铜价冲击未必大，但情绪扰动不可忽视。</p>
<p>第三个风险来自需求。如果四季度工业需求没有改善，铜的主升逻辑会被削弱。铝、锂、锡也都需要需求验证。小金属还要警惕流动性不足和价格波动过大。</p>

<h2 id="conclusion">结论：下半年有色的主线，是铜和黄金带队</h2>
<p>下半年有色金属的方向不是全面平均上涨，而是围绕宏观转向和供给约束重新排序。黄金和铜最值得排在前面，铝次之，锂和锡提供阶段性弹性。</p>
<p>铜是其中最强的基本金属。美国关税和战略备货改变库存流向，矿端和冶炼端供给持续下修，淡季需求不弱，四季度需求有望改善。只要宏观不出现系统性反转，铜价重新冲击上半年高点甚至创新高，是更顺的路径。</p>
<p>策略上，8 月到 9 月就应该开始逐步加仓，不必等所有右侧信号出现。回调不是撤退理由，而是提高胜率的机会。真正要做的是选对排序、控制仓位、盯住数据，把宏观转向和供给紧张带来的主升浪留给组合里的核心资产。</p>
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
    required = {
        "robot-sector-bottom-rebound-electronic-skin-dexterous-hand": ["机器人", "电子皮肤", "灵巧手", "岱美股份", "福莱新材", "恒帅股份", "新泉股份", "Optimus"],
        "copper-strongest-metal-h2-rate-cut-tariff-nonferrous-wave": ["铜", "降息", "关税", "黄金", "铝", "锂", "锡", "四季度", "加仓"],
    }
    for post in base.INPUT_ORDER:
        article_path = base.ROOT / post.url_path.strip("/") / "index.html"
        article = article_path.read_text(encoding="utf-8")
        body_match = re.search(r'<div class="post-body" v-pre>(.*?)</div></div><nav', article, re.S)
        plain = _plain_text(body_match.group(1)) if body_match else ""
        if len(plain) < 3600:
            failures.append(f"{post.slug}: body too short: {len(plain)}")
        for word in forbidden:
            if word in article:
                failures.append(f"{post.slug}: forbidden/source wording present: {word}")
        for word in required[post.slug]:
            if word not in article:
                failures.append(f"{post.slug}: missing required topic: {word}")
        h2 = re.findall(r'<h2 id="([^"]+)">', article)
        links = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', article)
        if h2 != links or len(h2) < 10:
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
    ] + [post.url_path for post in base.PUBLISH_ORDER] + [base.PREV_EXISTING_URL]
    if cards[: len(expected_cards)] != expected_cards:
        failures.append(f"homepage order mismatch: {cards[:len(expected_cards)]}")

    ET.parse(base.ROOT / "index.xml")
    rss = (base.ROOT / "index.xml").read_text(encoding="utf-8")
    archive = (base.ROOT / "archive/index.html").read_text(encoding="utf-8")
    for post in base.INPUT_ORDER:
        if post.full_url not in rss:
            failures.append(f"rss missing {post.full_url}")
        if post.url_path not in archive:
            failures.append(f"archive missing {post.url_path}")
        for rel in [
            f"categories/{post.category}/index.html",
            f"series/{post.series}/index.html",
            f"tags/{post.tags[0]}/index.html",
        ]:
            if post.url_path not in (base.ROOT / rel).read_text(encoding="utf-8"):
                failures.append(f"{rel} missing {post.url_path}")
    previous = (base.ROOT / base.PREV_EXISTING_URL.strip("/") / "index.html").read_text(encoding="utf-8")
    if base.PUBLISH_ORDER[-1].url_path not in previous:
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
base.DATE = "2026-08-05"
base.BASE_DT = datetime(2026, 8, 5, 12, 30, tzinfo=timezone(timedelta(hours=8)))
base.PREV_EXISTING_URL = "/2026/august-a-share-counteroffensive-buyback-fundflow-window/"
base.PREV_EXISTING_TITLE = "8月A股反攻窗口：回购新高、资金低点与配置节奏"
base.SCRIPT_NAME = "publish-robot-copper-two-article-batch-20260805.py"
base.MANIFEST_NAME = "publish-robot-copper-two-article-batch-20260805-changed-files.json"
base.CHANGED = set()
base.INPUT_ORDER = [
    base.Post(
        source_id="BV1zYMr6gEQH",
        slug="robot-sector-bottom-rebound-electronic-skin-dexterous-hand",
        title="机器人板块底部反弹：电子皮肤、灵巧手电机与供应链再定价",
        desc="机器人板块在宇树上市进程、机器人推理模型、Optimus 产能目标和供应链订单催化下进入底部修复窗口，电子皮肤、灵巧手电机和新泉股份是更清晰的跟踪主线。",
        category="投资研究",
        series="机器人投资",
        tags=["机器人", "人形机器人", "电子皮肤", "灵巧手", "Optimus", "岱美股份", "福莱新材", "恒帅股份", "新泉股份", "具身智能", "供应链"],
        minutes=10,
        body=ROBOT_BODY,
        cover_kicker="机器人底部反弹",
        cover_line="电子皮肤 · 灵巧手电机 · 供应链验证",
        cover_theme=("#101827", "#1d4ed8", "#22c55e"),
        duration=657.589125,
        segments=254,
        chars=2558,
    ),
    base.Post(
        source_id="BV1sAMk6SE1P",
        slug="copper-strongest-metal-h2-rate-cut-tariff-nonferrous-wave",
        title="铜才是下半年最强王者：降息转向、关税扰动与有色主升浪",
        desc="下半年有色的核心是宏观降息转向与供给基本面共振，铜在关税、库存迁移、供给下修和四季度需求改善下排序最靠前，黄金、铝、锂和锡各有配置节奏。",
        category="投资研究",
        series="有色金属",
        tags=["铜", "有色金属", "降息", "铜关税", "黄金", "铝", "锂", "锡", "紫金矿业", "洛阳钼业", "中国宏桥", "云铝股份", "锡业股份"],
        minutes=13,
        body=COPPER_BODY,
        cover_kicker="铜最强主线",
        cover_line="降息转向 · 关税扰动 · 四季度主升浪",
        cover_theme=("#1c1917", "#b45309", "#facc15"),
        duration=872.582688,
        segments=521,
        chars=5374,
    ),
]
base.PUBLISH_ORDER = list(base.INPUT_ORDER)
base.validate = validate
base.copy_script_and_manifest = copy_script_and_manifest


if __name__ == "__main__":
    base.main()
