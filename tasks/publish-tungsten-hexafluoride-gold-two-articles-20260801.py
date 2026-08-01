from __future__ import annotations

import html
import importlib.util
import json
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path


sys.dont_write_bytecode = True
BASE_PATH = Path(__file__).with_name("publish-physical-ai-three-article-batch.py")
spec = importlib.util.spec_from_file_location("base_publisher_tungsten_gold", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Unable to load base publisher: {BASE_PATH}")
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
_BASE_VALIDATE = base.validate


BODY_TUNGSTEN = """
<p><img src="/images/posts/tungsten-hexafluoride-supply-gap-domestic-special-gas-investment/cover.svg" alt="六氟化钨投资框架：供需缺口、国产卡位与盈利弹性"></p>
<p>六氟化钨是半导体先进制程里非常关键的含钨前驱体材料，主要用于沉积工艺中的钨相关薄膜和接触孔填充。它不是一个大众化化工品，而是被晶圆制造工艺、客户认证、纯度控制、稳定供货能力共同约束的电子特气品种。正因为这种“用量不算最大、但环节足够关键”的特点，一旦供需关系发生变化，价格和盈利弹性会非常集中地体现出来。</p>
<p>当前六氟化钨的投资逻辑，可以拆成三条主线：第一，下游晶圆厂资本开支仍在高位，先进存储、特殊芯片和先进逻辑继续拉动需求；第二，3D NAND、HBM 和先进逻辑制程升级带来单片用量提升；第三，日系高端供给收缩形成刚性缺口，国产企业迎来份额提升和国际定价切换窗口。</p>
<p>这不是单纯的主题炒作，而是一条从材料属性、工艺用量、供给扰动、价格传导到公司盈利的完整链条。真正要判断机会大小，不能只看“涨价”两个字，而要看缺口是否刚性、客户认证是否真实、产能是否已经具备、价格能否传导，以及盈利能否在二三季度之后持续释放。</p>

<h2 id="material">一、六氟化钨为什么关键</h2>
<p>六氟化钨的核心价值，在于它是钨沉积工艺中的重要前驱体。先进制程里，芯片结构越来越复杂，互连、接触孔、栅极和存储结构对材料的一致性、纯度、稳定性要求越来越高。电子特气不像普通大宗化工品，客户不会只看价格，最看重的是长期稳定、杂质可控、批次一致、供应不中断。</p>
<p>在晶圆制造中，一种材料进入供应链往往需要较长认证周期。客户要验证纯度、杂质、工艺适配、良率影响、连续供货和质量体系。越是头部晶圆厂，越不可能轻易换供应商。也正因为认证壁垒高，一旦国产企业通过验证并形成稳定供货，份额提升就具有较强黏性。</p>
<p>六氟化钨不是简单“有产能就能卖”的产品。高纯化、杂质控制、包装运输、安全管理和连续稳定生产能力，构成了它的技术壁垒。供给紧张时，市场也很难临时找出大量合格产能来填补缺口。</p>

<h2 id="demand">二、需求端：晶圆厂资本开支和单片用量双驱动</h2>
<p>需求端第一条线，是全球晶圆厂资本开支仍然维持在较高水平。海外存储大厂、先进逻辑厂，以及国内长存、长鑫、中芯、华虹等晶圆制造体系，都在支撑电子特气需求。无论是存储扩产，还是逻辑制程推进，只要晶圆厂建设和稼动持续，六氟化钨就会跟随制造环节形成消耗。</p>
<p>第二条线，是工艺迭代带来的单片用量提升。3D NAND 从 128 层继续向 200 层、300 层演进，垂直堆叠结构增加，每一层都需要更多高深宽比孔洞和相关沉积工艺，单片晶圆对六氟化钨的消耗会显著提升。从拉动强度看，3D NAND 是最明确的增量方向。</p>
<p>HBM 也会带来用量提升。高带宽存储对互联密度、接触孔数量和封装连接提出更高要求，单位晶圆的材料消耗会高于普通 DRAM。AI 服务器和先进封装需求越强，HBM 产业链对上游关键材料的牵引就越明显。</p>
<p>先进逻辑同样不可忽视。随着 7nm、5nm、3nm 等节点推进，晶体管密度提升，接触孔数量增加，单片用量稳步上行。综合排序上，3D NAND 的拉动大于 HBM，HBM 又强于先进逻辑；三者叠加，构成了六氟化钨中期需求增长的基础。</p>

<h2 id="growth">三、需求增速：中期维持双位数增长</h2>
<p>按照行业跟踪数据，2025 年全球六氟化钨消耗量大约在八九千吨级别，过去几年已经保持十几个点的增长。展望未来五年，需求复合增速至少仍有双位数基础，在存储复苏、HBM 放量和先进制程推进更顺利的情形下，年复合增速有机会达到 15% 到 20%。</p>
<p>这个增速的意义在于，六氟化钨不是一个静态市场。即使没有供给扰动，需求端也在持续扩容；一旦供给端出现收缩，原本健康增长的市场就会迅速转化为价格弹性。对上游企业来说，最好的状态不是短期脉冲需求，而是长期消耗量不断抬升、客户结构不断升级、定价机制逐步向供需主导切换。</p>
<p>真正需要观察的是需求质量。普通低端需求增长对盈利帮助有限，高端客户、海外客户、先进存储和先进逻辑客户，才更能贡献定价权和利润率。谁能进入这些客户的供应链，谁就能在行业景气时获得更高弹性。</p>

<h2 id="supply">四、供给端：日系高端产能收缩带来缺口</h2>
<p>供给端的核心变化，是日系高端六氟化钨供给出现刚性收缩。国内钨相关出口管制、海外高端产能调整，以及部分日系企业对日本之外客户停止或减少供货，使全球高端供应体系出现缺口。市场预期受影响供给至少在千吨级别，这对一个八九千吨级别的市场来说并不小。</p>
<p>更关键的是，这个缺口不容易被快速补上。六氟化钨导入头部晶圆厂供应链时间较长，客户不会因为短期缺货就随便接受未经充分验证的材料。高纯杂质控制和连续稳定生产能力不是短期扩产能解决的，合格供给本身就稀缺。</p>
<p>因此，当前的供给偏紧不是普通库存周期，而更像高端供给体系重构。日系供给收缩之后，中国企业不仅有机会提升份额，也有机会进入过去较难打开的海外客户体系。这个窗口期的战略价值，可能大于单次涨价本身。</p>

<h2 id="domestic">五、国产企业的窗口：份额提升与海外验证</h2>
<p>国产六氟化钨企业正处在战略卡位期。已经具备实际规模化能力、客户认证基础和持续供货能力的公司，将最直接受益。中船特气是代表性企业，产能规模较大，并且已覆盖多家全球主流晶圆厂客户；昊华科技拥有六氟化钨产能基础，随着后续验证和客户突破，有望贡献新增弹性；部分本土特气企业也在绑定国内晶圆厂，并寻求海外市场突破。</p>
<p>机会的关键不只是产能数字，而是“产能乘以客户”。没有客户验证的产能，短期很难兑现为收入；没有稳定品质的产能，无法进入高端供应链；没有海外客户的产能，可能只能享受国内价格弹性。真正有价值的是产能、认证、客户结构和定价能力同时具备。</p>
<p>日系产能降低之后，此前海外拓展顺利的企业，有望拿到更多海外订单；此前海外拓展有限的企业，也会迎来客户验证的关键窗口。对国产企业来说，这是一次从“替代”走向“参与全球定价”的机会。</p>

<h2 id="price">六、价格：从钨成本驱动转向供需驱动</h2>
<p>2026 年二季度，供需错配叠加钨价格上涨，共同推动六氟化钨价格明显上行。部分出口单价已经呈现快速抬升，市场报价也从早期成本推动，逐步转向供需紧张推动。更重要的是，海外价格可能还没有完全反映高端供给缺口。</p>
<p>价格传导通常不是一天完成的。晶圆厂客户合同、认证节奏、供应切换、成本谈判和库存周期，都会影响涨价兑现。二季度可能只是价格变化的开始，三季度和四季度才更能观察涨价向客户侧传导的力度。</p>
<p>如果后续钨价回落，而六氟化钨终端价格保持韧性，上游企业单位盈利会进入扩张阶段。这是当前逻辑最有吸引力的地方：成本端可能缓和，产品端却因供需紧张保持高位，价差扩大带来利润弹性。</p>

<h2 id="valuation">七、投资框架：看三类能力</h2>
<p>第一，看真实产能。六氟化钨不是概念品种，必须有可量产、可交付、可持续稳定运行的装置。产能规模越大，越能承接供给缺口；但产能利用率和客户订单更重要。</p>
<p>第二，看客户认证。通过海力士、三星、台积电、中芯、华虹等头部客户验证的企业，壁垒更强。电子特气一旦进入客户体系，后续份额提升和价格谈判都会更有基础。</p>
<p>第三，看盈利弹性。价格上涨能否落到毛利率和净利率，取决于产品结构、海外客户占比、原材料成本、库存节奏和合同模式。最理想的企业，是产能扩张、客户升级和单位盈利改善同时发生。</p>
<p>从这个框架看，中船特气是最直接的代表，昊华科技和其他具备产能及客户突破的国产企业也值得纳入跟踪。投资上不应只看“谁有六氟化钨”，而要看谁能在高端供应链里拿到真实订单和更强定价。</p>

<h2 id="strategy">八、买入策略：景气确认后分批布局</h2>
<p>六氟化钨当前具备产业景气、供给缺口和盈利扩张三重逻辑，但交易上不能把短期涨价简单外推成无限上涨。更合理的策略，是围绕三类信号分批布局：价格持续高位、客户订单验证、季度业绩兑现。</p>
<p>如果市场因短期情绪回落、原材料价格波动或半导体板块调整而出现估值回落，但供给缺口和客户导入没有被破坏，反而是较好的左侧观察窗口。若三季度、四季度业绩验证涨价传导，右侧趋势会更清晰。</p>
<p>仓位上应避免一次性重仓。电子特气弹性大，估值也容易受主题情绪影响。更稳妥的做法，是底仓跟踪产业趋势，业绩验证后加仓，价格过度透支时降低追高冲动。</p>
<p>买入纪律上，最理想的区间不是市场情绪最热的时候，而是产业逻辑仍在、估值因板块波动被压下来的时候。若产品价格、客户订单和毛利率三者同向改善，说明景气正在进入报表；若只有价格传闻，没有订单和盈利兑现，就需要降低仓位弹性。</p>
<p>这类品种最怕把产业窗口误读成永久垄断。好的买点来自验证和分歧并存，而不是所有人都已经按最乐观情形定价。若后续价格、订单、毛利率只兑现其中一项，就只能按交易机会处理；三项同时兑现，才更接近产业重估。否则就要承认弹性存在，但确定性还没有完全落地，需要继续等报表验证。</p>
<p>如果后续海外客户订单、价格韧性和毛利率同步兑现，六氟化钨就不只是短期涨价交易，而是国产电子特气进入全球供应链再定价的中期机会。</p>


<h2 id="tracking">九、后续跟踪清单：用事实验证逻辑</h2>
<p>六氟化钨后续要用事实持续验证。第一，看出口单价和海外报价是否继续维持高位。如果价格只是短期尖峰，很难支撑长期盈利重估；如果价格逐季抬升或高位稳定，说明供需缺口正在变成定价权。</p>
<p>第二，看企业季度毛利率和单吨盈利。原材料钨价回落时，若产品价格没有同步回落，利润弹性会在报表中体现。第三，看客户验证公告和订单节奏，尤其是海外头部晶圆厂、先进存储和先进逻辑客户。第四，看新增产能投放速度，既要看公司自身扩产，也要看行业是否出现过度扩产。第五，看下游晶圆厂稼动率与资本开支，如果半导体景气回落，材料消耗也会承压。</p>
<p>因此，这条主线最适合用“产业数据 + 公司报表 + 客户认证”三重证据跟踪。只讲故事不看报表，容易被主题带偏；只看短期报表不看供需重构，又容易错过产业拐点。</p>

<h2 id="risks">十、风险：最怕缺口修复和价格传导不及预期</h2>
<p>第一，价格不能如期上行或涨价无法传导。若下游晶圆厂议价能力强，或者合同价格调整慢，产品涨价未必马上变成利润。</p>
<p>第二，日系供给恢复。如果海外高端产能重新释放，当前供需缺口会被压缩，价格弹性也会下降。</p>
<p>第三，国内新增产能过大。若多家企业同时扩产，未来行业可能从紧缺转向阶段性过剩。</p>
<p>第四，下游晶圆厂扩产不及预期。半导体资本开支若放缓，3D NAND、HBM 和先进逻辑需求会低于预期。</p>
<p>第五，钨价大幅波动和客户认证不及预期。原材料成本变化会影响价差，客户认证进度则决定产能能否真正释放。</p>
<p>六氟化钨的核心机会来自“高端供给缺口 + 国产认证突破 + 价格向盈利传导”。只要这三点仍在，行业中期逻辑就没有结束；但任何一点被证伪，都需要重新评估仓位和估值。</p>
"""


BODY_GOLD = """
<p><img src="/images/posts/gold-pullback-opportunity-rate-hike-deficit-central-bank-demand/cover.svg" alt="黄金回调即机会：加息预期、财政赤字与央行买盘的再定价"></p>
<p>黄金的短期波动，最容易被市场情绪放大。加息预期、实际利率上行、地缘冲突降温、美元反弹，都会成为压制金价的理由。但真正决定黄金中期趋势的，不是单一事件，而是利率、财政、央行买盘、美元信用和全球避险需求共同构成的再定价框架。</p>
<p>当前黄金的核心判断是：加息预期和地缘压力测试已经较充分地体现在价格里，若后续出现回调，反而更像中期布局窗口。黄金多头逻辑没有结束，只是从单纯地缘交易，逐步切换到美国财政赤字、实际利率约束和央行持续买盘这条更深的主线。</p>

<h2 id="rate-hike">一、加息预期已经成为压力测试</h2>
<p>黄金最怕的是实际利率快速上行。市场一旦预期美联储重新加息，短端利率和实际利率走高，黄金会承压。但问题在于，当前加息预期已经被债券市场较充分地定价。两年期利率和利率期货已经提前反映了部分加息可能，黄金价格也已经经历了一轮压力测试。</p>
<p>真正加息落地时，未必继续构成新的重大利空。除非加息是为了把经济打入衰退、强行压制通胀，否则一般加息落地后，市场会进入“利空兑现”阶段。也就是说，预期阶段的压力可能比行动本身更大。</p>
<p>不加息的情形下，黄金反而会修复之前被压制的估值；加息的情形下，也可能先跌后涨，因为市场会开始交易美国经济承压、后续政策转向和金融条件放松的可能。黄金真正怕的不是一次加息，而是持续、强劲、无衰退代价的高实际利率环境。</p>

<h2 id="us-economy">二、美国经济没有强到可以长期大幅加息</h2>
<p>当前美国经济内部并不均衡。大型科技公司和部分资产价格仍然强势，但中小企业、居民消费和部分信用领域并不稳。通胀回落背景下，如果继续大幅加息，会给企业融资、居民负担和财政利息支出带来更大压力。</p>
<p>这意味着美联储并不具备无限加息的基本面条件。尤其当科技股已经出现较大回调、消费和中小企业承压时，政策进一步收紧反而可能倒逼未来更宽松的路径。黄金会在这种预期切换中重新获得支撑。</p>
<p>短期加息预期压制黄金，中期增长压力和政策回摆又支撑黄金。这个矛盾决定了金价可能震荡，但很难简单判断多头趋势已经结束。</p>

<h2 id="geopolitics">三、地缘冲突更像阶段性压力测试</h2>
<p>地缘冲突对黄金的影响，通常不是单向的。冲突升级会推升避险需求，但如果冲突没有进一步恶化，市场也会出现“避险退潮”的交易。当前相关冲突更像一次阶段性压力测试，而不是能够持续改写黄金中期逻辑的单一变量。</p>
<p>在重大选举或政治周期临近时，大规模长期冲突的概率会受到约束。市场更可能交易冲突的边际变化，而不是无限升级。只要油价没有失控、通胀没有再次全面抬头，地缘因素对黄金的短期扰动会逐步让位于利率和财政主线。</p>
<p>因此，地缘缓和带来的金价回调，不一定是趋势反转，更可能是中期逻辑里的买点重塑。</p>

<h2 id="central-bank">四、央行买盘仍然稳定</h2>
<p>黄金过去一轮大行情的重要支撑，是全球央行持续买入。央行买盘不是短线投机资金，它更看重储备多元化、美元信用风险对冲和长期安全资产配置。只要这类买盘没有明显撤出，金价下方就会有结构性支撑。</p>
<p>近期并未看到类似大规模央行抛售的信号。部分国家黄金储备仍在累积，买盘更像稳定底仓，而不是追涨杀跌的资金。与普通投资者不同，央行买黄金不是为了博短期涨幅，而是为了重构储备资产结构。</p>
<p>这意味着黄金即使回调，也很难仅凭短期利空就彻底破坏中期趋势。央行买盘提供的是长期底层需求，而不是交易层面的短暂情绪。</p>

<h2 id="deficit">五、美国财政赤字成为更深主线</h2>
<p>黄金真正的新主线，是美国财政赤字和利息负担。随着债务规模上升，利率维持高位会让财政利息支出变成越来越沉重的约束。即使名义 GDP 继续增长，只要利息成本高于财政承受能力，市场就会重新定价美元信用和长期实际利率。</p>
<p>如果未来美国希望稳定债务率，要么需要非常强的实际 GDP 增长，要么需要通胀、金融压抑或政策组合来缓释债务压力。但实现长期 8% 到 10% 的实际增长几乎不现实。财政约束越强，黄金作为无负债资产的配置价值越突出。</p>
<p>这也是黄金逻辑从“抗通胀”走向“抗财政信用压力”的关键。通胀只是表层，深层是债务、赤字、利息支出和美元资产安全性的再平衡。</p>

<h2 id="path">六、短期路径：7 到 9 月是确认期</h2>
<p>短期看，7 到 9 月可能是黄金的重要确认期。市场需要消化加息预期、通胀数据、地缘边际变化、美元和实际利率走势。如果加息预期继续强化，黄金可能还有波动；如果预期降温，金价会修复压力。</p>
<p>更重要的是，若黄金在压力测试中没有破坏中期结构，回调反而会让风险收益比变好。很多优质黄金股和黄金资产，在金价调整时会出现更好的配置价格。</p>
<p>交易上不需要追逐每一次短线波动，而要围绕中期逻辑做仓位管理。黄金不是没有波动的资产，真正的机会往往出现在市场把短期利空过度定价的时候。</p>

<h2 id="strategy">七、配置策略：回调分批，不追情绪高点</h2>
<p>黄金资产适合用分批策略。若价格因加息预期或地缘缓和出现快速回调，但央行买盘、财政赤字和实际利率约束没有变化，可以逐步提高配置比例。若价格在避险情绪推动下快速拉升，则应避免情绪高点追涨。</p>
<p>黄金股弹性更大，但也更受成本、产量、汇率、估值和市场风险偏好影响。配置黄金股时，要优先选择资源质量好、成本曲线低、产量增长清晰、资产负债表稳健的公司。金价上涨不代表所有黄金股都会同等受益。</p>
<p>对组合来说，黄金更像风险对冲和宏观信用对冲，而不是单纯博弈短期涨跌的交易品种。适度配置可以对冲美元信用、财政赤字、地缘不确定性和实际利率下行风险。</p>


<h2 id="gold-stocks">八、黄金股：比金价更有弹性，也更挑公司</h2>
<p>黄金股不是黄金本身。金价上涨时，黄金股通常具备更高弹性，因为收入端跟随金价上行，而成本端相对滞后，利润会被放大。但金价下跌时，这种弹性也会反向放大，尤其是高成本矿山、产量不稳和负债较高的公司。</p>
<p>筛选黄金股要看四个指标。第一是资源禀赋，包括储量、品位、矿山寿命和扩产潜力；第二是成本曲线，低成本公司在金价回调时更抗跌；第三是产量增长，只有产量和金价共振，业绩弹性才强；第四是资本开支和资产负债表，重资本行业一旦扩产过猛，现金流压力会压制估值。</p>
<p>因此，黄金回调时可以把实物黄金、黄金 ETF 和黄金股分开看。前两者更偏防御和资产配置，黄金股更偏进攻和业绩弹性。组合里同时保留防御和进攻，通常比单押某一类资产更稳。</p>
<p>宏观确认指标也很重要：实际利率是否见顶，美元是否继续强势，通胀是否重新抬头，财政利息支出是否继续挤压预算，以及央行购金是否延续。只要这些指标没有系统性反转，黄金回调就更像赔率改善，而不是趋势结束。</p>
<p>真正的纪律，是在恐慌回调里检查主线是否仍在，而不是在价格上涨后才寻找理由。黄金最好的买点通常不是叙事最顺的时候，而是短期利空足够拥挤、中期约束仍未消失的时候。此时用分批方式进入，比在一致乐观时追高更符合风险收益比，也更容易在波动中保持仓位纪律。</p>
<p>真正需要等待的是利率预期从压制转向缓和，以及财政主线被更多资金重新定价；在此之前，回调更适合分批承接，而不是情绪化追涨。</p>

<h2 id="risks">九、风险：真正的压力来自强增长和高实际利率</h2>
<p>黄金最大的风险，是美国经济真正实现强劲增长，同时通胀受控、实际利率维持高位、财政压力被名义增长消化。在这种情形下，黄金会受到较大压制。</p>
<p>第二个风险，是央行买盘明显放缓或反向流出。如果长期买盘撤退，金价底部支撑会变弱。</p>
<p>第三个风险，是美元重新走强并伴随全球风险偏好修复。短期资金可能从黄金流向权益和美元资产。</p>
<p>但从当前约束看，这些风险尚未完全成为主导。财政赤字、利息支出、经济分化和央行储备多元化，仍然支撑黄金中期逻辑。回调不是多头结束的证据，更多时候是更好价格出现的过程。</p>
"""


def _plain_text(html_text: str) -> str:
    return re.sub(r"<[^>]+>", "", html.unescape(html_text))


def validate() -> None:
    _BASE_VALIDATE()
    failures: list[str] = []
    forbidden = [
        "B站",
        "bilibili",
        "哔哩",
        "视频里",
        "视频中",
        "原视频",
        "音频里",
        "音频中",
        "UP主",
        "up主",
        "这期",
        "本期",
        "作者说",
        "他提到",
        "观看",
        "点赞",
        "订阅",
        "投币",
        "收藏",
        "下期",
        "关注",
        "BV1",
    ]
    required_terms = {
        "tungsten-hexafluoride-supply-gap-domestic-special-gas-investment": [
            "六氟化钨",
            "供需缺口",
            "3D NAND",
            "HBM",
            "先进逻辑",
            "中船特气",
            "昊华科技",
            "客户认证",
            "价格传导",
            "盈利弹性",
        ],
        "gold-pullback-opportunity-rate-hike-deficit-central-bank-demand": [
            "黄金",
            "加息预期",
            "实际利率",
            "央行买盘",
            "财政赤字",
            "美元信用",
            "回调",
            "配置策略",
            "地缘冲突",
        ],
    }
    min_lengths = {
        "tungsten-hexafluoride-supply-gap-domestic-special-gas-investment": 4200,
        "gold-pullback-opportunity-rate-hike-deficit-central-bank-demand": 3000,
    }
    for post in base.INPUT_ORDER:
        article_path = base.ROOT / post.url_path.strip("/") / "index.html"
        article = article_path.read_text(encoding="utf-8")
        body_match = re.search(r'<div class="post-body" v-pre>(.*?)</div></div><nav', article, re.S)
        plain = _plain_text(body_match.group(1)) if body_match else ""
        if len(plain) < min_lengths[post.slug]:
            failures.append(f"{post.slug}: body too short: {len(plain)}")
        for word in forbidden:
            if word in article:
                failures.append(f"{post.slug}: forbidden/source wording present: {word}")
        for word in required_terms[post.slug]:
            if word not in article:
                failures.append(f"{post.slug}: missing required topic: {word}")
        h2 = re.findall(r'<h2 id="([^"]+)">', article)
        links = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', article)
        if h2 != links or len(h2) < 8:
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
    ] + [post.url_path for post in base.INPUT_ORDER] + [base.PREV_EXISTING_URL]
    if cards[: len(expected_cards)] != expected_cards:
        failures.append(f"homepage order mismatch: {cards[:len(expected_cards)]}")

    archive = (base.ROOT / "archive/index.html").read_text(encoding="utf-8")
    rss = (base.ROOT / "index.xml").read_text(encoding="utf-8")
    ET.parse(base.ROOT / "index.xml")
    for post in base.INPUT_ORDER:
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


base.ROOT = Path("/tmp/bv1ka-bv169-sparse.Nkhbld")
base.DATE = "2026-08-01"
base.BASE_DT = datetime(2026, 8, 1, 13, 15, tzinfo=timezone(timedelta(hours=8)))
base.PREV_EXISTING_URL = "/2026/reading-compound-interest-booklist-eink-guide/"
base.PREV_EXISTING_TITLE = "读书像一场无痛换脑：阅读复利、书单与电纸书选择"
base.SCRIPT_NAME = "publish-tungsten-hexafluoride-gold-two-articles-20260801.py"
base.MANIFEST_NAME = "publish-tungsten-hexafluoride-gold-two-articles-20260801-changed-files.json"
base.CHANGED = set()
base.INPUT_ORDER = [
    base.Post(
        source_id="public-audio-bv1hdgf6hepg-20260801",
        slug="tungsten-hexafluoride-supply-gap-domestic-special-gas-investment",
        title="六氟化钨投资框架：供需缺口、国产卡位与盈利弹性",
        desc="六氟化钨的机会来自半导体需求扩容、单片用量提升、日系高端供给收缩和国产企业客户认证突破，核心是价格能否传导为盈利弹性。",
        category="股票研究",
        series="半导体材料",
        tags=["六氟化钨", "电子特气", "半导体材料", "中船特气", "昊华科技", "HBM", "3D NAND", "国产替代", "供需缺口", "盈利弹性"],
        minutes=11,
        body=BODY_TUNGSTEN,
        cover_kicker="半导体材料",
        cover_line="供需缺口 · 国产卡位 · 盈利弹性",
        cover_theme=("#111827", "#2563eb", "#f59e0b"),
        duration=637.5503125,
        segments=231,
        chars=3617,
    ),
    base.Post(
        source_id="public-audio-bv1tzgf6mep9-20260801",
        slug="gold-pullback-opportunity-rate-hike-deficit-central-bank-demand",
        title="黄金回调即机会：加息预期、财政赤字与央行买盘的再定价",
        desc="黄金短期承压来自加息预期和地缘压力测试，但中期主线仍是财政赤字、实际利率约束、央行买盘和美元信用再定价。",
        category="投资策略",
        series="宏观资产配置",
        tags=["黄金", "加息预期", "实际利率", "央行买盘", "财政赤字", "美元信用", "资产配置", "避险资产", "黄金股", "回调机会"],
        minutes=5,
        body=BODY_GOLD,
        cover_kicker="宏观资产配置",
        cover_line="加息预期 · 财政赤字 · 央行买盘",
        cover_theme=("#111827", "#b45309", "#facc15"),
        duration=284.2586875,
        segments=180,
        chars=1664,
    ),
]
base.PUBLISH_ORDER = list(base.INPUT_ORDER)
base.validate = validate
base.copy_script_and_manifest = copy_script_and_manifest


if __name__ == "__main__":
    shutil.rmtree(Path(__file__).with_name("__pycache__"), ignore_errors=True)
    base.main()
    shutil.rmtree(Path(__file__).with_name("__pycache__"), ignore_errors=True)
