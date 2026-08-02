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

ROOT_HINT = Path("/tmp/blog-publish-bv14u-four-20260802.path")
ROOT = Path(os.environ.get("BLOG_ROOT") or ROOT_HINT.read_text(encoding="utf-8").strip())
BASE_PATH = Path(__file__).with_name("publish-physical-ai-three-article-batch.py")
if not BASE_PATH.exists():
    BASE_PATH = ROOT / "tasks" / "publish-physical-ai-three-article-batch.py"

spec = importlib.util.spec_from_file_location("base_publisher_zheshenshinei", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Unable to load base publisher: {BASE_PATH}")
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
_BASE_VALIDATE = base.validate


BODY = """
<p><img src="/images/posts/zheshenshinei-china-economy-housing-local-debt-trade-war/cover.svg" alt="置身事内：看懂中国经济、房价、地方债与贸易战的一条线"></p>
<p>理解中国经济，不能把政府放在场外。企业投资、城市扩张、房地产、地方债、制造业崛起、消费不足、出口顺差，表面上是不同问题，背后却连在同一套制度和激励链条上。兰小欢的《置身事内：中国政府与经济发展》真正有价值的地方，不只是解释宏观名词，而是把地方政府如何行动、为什么行动、行动之后怎样改变市场，一层一层拆开。</p>
<p>中国经济过去几十年的高增长，不是靠单一因素推动的。廉价劳动力、全球化、人口红利、基础设施、土地制度、金融体系、产业政策和地方政府竞争，都只是拼图的一部分。真正把这些因素组织起来的，是地方政府这台发动机：它既是规则执行者，也是资源组织者；既要完成上级目标，也要面对本地就业、税收、债务和增长压力。</p>
<p>如果把这条线拉直，可以看到一组清晰的因果关系：地方政府承担大量发展责任，需要收入和融资；分税制让中央财政能力增强，也让地方财政压力上升；土地财政和城投平台补上了地方资金缺口；基础设施和招商引资推动工业化；户籍、高房价和收入分配抑制居民消费；内需不足带来高储蓄和高出口；外部顺差最终演化成贸易摩擦。房价、地方债和贸易战并不是三件孤立的事，而是一条链上的不同环节。</p>
<p>这条链条也解释了为什么很多普通人的切身问题会和宏观制度相连。房价不是单纯由供求决定，它还连接土地出让、地方财政、银行抵押品和居民预期；地方债不是单纯的财务数字，它背后有基建、招商、政绩、公共服务和期限错配；贸易摩擦也不只是外部谈判问题，它和国内收入分配、居民消费、企业投资和储蓄结构有关。宏观不是远方的抽象变量，而是日常生活的背景系统。</p>

<h2 id="inside-system">一、为什么必须置身事内</h2>
<p>很多宏观分析喜欢把政府当成外生变量：政策放松，市场上涨；政策收紧，市场下跌。这样看问题很方便，却容易失真。中国经济里的政府不是偶尔出手的旁观者，而是深度嵌入土地、金融、基建、产业、城市化和企业行为的关键参与者。</p>
<p>地方政府尤其重要。它不是抽象的行政名词，而是影响企业选址、土地价格、银行授信、产业补贴、基础设施、教育医疗资源和城市发展方向的真实力量。理解地方政府的激励，就能理解为什么有些城市拼命修路建新区，为什么有些行业会在短期内集中扩产，为什么房地产长期扮演财政和金融枢纽，为什么很多政策看似矛盾却能在同一套目标函数里成立。</p>
<p>置身事内的意思，不是为某种制度简单辩护，也不是把所有问题都归因于政府，而是承认政府、市场、金融和地方发展目标共同组成了现实环境。普通人买房、就业、投资、创业、选择城市，本质上都在这套系统里做决策。看不懂系统，就容易把结果误认为原因。</p>
<p>这也是这本书区别于普通财经读物的地方。它没有把宏观经济写成一串指标，而是不断追问指标背后的组织机制：钱从哪里来，权责如何分配，地方为什么愿意承担风险，银行为什么愿意放款，企业为什么愿意进入某个园区，居民为什么不敢消费。只要这些问题连起来，许多看似突然发生的市场波动，就会变得有迹可循。</p>

<h2 id="local-government">二、地方政府是中国经济的核心执行器</h2>
<p>中国的地方政府既有行政层级，也有地域分工。中央制定大方向，地方负责落地执行。经济发展、招商引资、基础设施、土地开发、财政收支、社会稳定、公共服务，很多任务最终都压到地方。地方官员的考核也长期与经济增长、投资、税收、就业和项目落地相关，这就形成了强烈的发展激励。</p>
<p>这种结构有一个好处：一旦目标明确，地方政府能够快速调动土地、资金、企业、银行和建设资源，把计划转化成项目。道路、园区、厂房、港口、地铁、新区和配套设施，往往不是企业单独能完成的，而是地方政府组织能力的结果。</p>
<p>但这种结构也有副作用。地方政府既是裁判员，又是运动员。它一方面要维护市场秩序，另一方面又要完成增长目标；一方面要控制风险，另一方面又要融资建设；一方面要服务民生，另一方面又要争夺产业项目。当激励过强而约束不足时，重复建设、过度举债、土地依赖和短期政绩冲动就会出现。</p>

<h2 id="incentives">三、激励相容：政策分析的第一把尺子</h2>
<p>理解地方政府行为，不能只看文件表述，更要看激励是否相容。所谓激励相容，就是各方在追求自身目标时，是否会自然推动整体目标实现。如果地方政府既承担发展责任，又能从增长中获得财政收入和政绩回报，它就会主动招商、建设和扶持企业。如果地方承担支出责任，却缺少稳定收入来源，它就会寻找土地、融资平台和隐性债务等替代工具。</p>
<p>很多政策落地效果不佳，不是因为目标不正确，而是因为激励不匹配。要求地方稳增长，却不解决资金来源，地方就会继续依赖投资和债务；要求扩大消费，却让居民长期面对高房价、教育医疗不确定性和户籍限制，居民就会倾向储蓄；要求产业升级，却用短期补贴和政绩考核推动项目，企业就可能先追逐补贴而不是真实需求。</p>
<p>这把尺子也适合投资和商业判断。看一个行业，不只要看政策是否支持，还要看地方政府、企业、银行、消费者和监管机构的利益是否同向。如果补贴一撤需求就消失，如果订单靠行政推动而不是客户真实付费，如果地方财政已经吃紧却仍大规模承诺投入，就要警惕繁荣的持续性。</p>

<h2 id="tax-sharing">四、分税制：中央财力增强，地方压力上升</h2>
<p>改革开放早期，财政包干极大激发了地方发展经济的积极性。地方多收多得，愿意扶持企业、扩大税源、推动乡镇工业和招商引资。但财政包干也带来一个严重问题：中央财政收入占比不断下降，宏观调控和跨地区公共建设能力被削弱。一个财力不足的中央，很难承担全国性基础设施、转移支付和逆周期调节。</p>
<p>1994 年分税制改革改变了这种格局。中央通过增值税等税种安排重新掌握更大比例财政收入，国家宏观调控能力显著增强。与此同时，许多公共支出责任仍然留在地方，教育、医疗、社保、基建、城市维护和发展项目都需要地方出钱。于是，一个新的矛盾出现了：地方要办的事很多，但可支配财力没有同步增长。</p>
<p>这不是简单的“中央拿走地方的钱”，而是国家治理能力重构的结果。它解决了中央财力弱的问题，也把地方政府推向新的融资路径。地方必须在预算内收入之外寻找资金，土地财政、地方融资平台和以地融资，就是在这个背景下迅速扩张起来的。</p>

<h2 id="land-finance">五、土地财政：房价、城市化与财政的连接器</h2>
<p>土地财政不是一句口号，而是一套财政和金融机制。城市土地归国家所有，地方政府通过土地出让获得一次性收入。开发商拿地、银行放贷、居民按揭、地方获得土地出让金，城市再用这些资金修路、建学校、做配套、推动新区开发。土地由此成为地方政府组织城市化和融资的关键资产。</p>
<p>在房价和地价持续上涨时期，这套机制运转非常顺畅。土地升值提高地方收入，基础设施改善城市面貌，房地产销售带动上下游产业，银行资产看起来有抵押物支撑，居民也相信买房能够保值增值。土地、房价、信贷和城市扩张形成正反馈。</p>
<p>问题在于，这套机制高度依赖预期。一旦人口流入放缓、居民杠杆上升、房价不再持续上涨、开发商资金链收紧，土地出让收入就会下降。土地卖不动以后，地方财政缺口、城投偿债压力、房地产链条收缩和居民资产负债表压力会同时显现。房地产作为中国经济核心驱动力的时代已经结束，继续用“房价永远涨”的旧逻辑配置资产，风险会越来越高。</p>

<h2 id="city-investment">六、城投平台：基础设施奇迹背后的债务机制</h2>
<p>地方融资平台的出现，是为了在预算约束之外筹集建设资金。城投公司以地方政府信用、土地储备和项目收益为支撑，从银行、信托、债券市场获得资金，再投入道路、桥梁、地铁、园区、棚改、水利和公共设施。很多城市面貌的快速变化，都离不开这套机制。</p>
<p>它的好处是把未来收益提前用于当前建设。基础设施具有外部性，单个项目未必直接赚钱，但能改善营商环境、提高土地价值、吸引企业和人口。在高增长阶段，提前建设往往能带来明显正反馈。</p>
<p>真正的风险在于期限错配和隐性担保。城投借来的钱往往是三到五年的债务，投下去的却是二十年、三十年才逐渐发挥作用的资产，有些公益项目甚至没有直接现金流。当地价上涨、融资顺畅时，可以借新还旧；一旦土地收入下降、融资收紧，短债长投的问题就会暴露。金融机构如果只看政府背景，不看项目现金流，道德风险也会被放大。</p>

<h2 id="industrialization">七、招商引资：中国制造业崛起的组织密码</h2>
<p>中国成为世界工厂，绝不仅仅因为劳动力便宜。地方政府在工业化中的作用非常关键。为了吸引企业，地方提供工业用地、基础设施、税收优惠、融资协调、审批服务、配套园区和供应链组织。企业因此能够快速落地，产业链也能在区域内形成集聚。</p>
<p>地方政府之间的竞争，像一场长期招商锦标赛。谁能拿到大项目，谁就能带来就业、税收、上下游企业和城市声誉。工业园区、开发区、高新区、保税区，各类平台的背后，都是地方政府争夺产业和税源的努力。</p>
<p>这种模式创造了惊人的制造能力，也带来了产能过剩和补贴依赖的风险。当多个地方同时押注同一新兴产业，短期内会出现资本、土地和政策资源集中涌入，形成主题繁荣。但如果终端需求不足，行业会迅速进入价格战和产能出清。新能源、机器人、低空经济、先进制造等方向都可能重复这一逻辑：早期政策催化带来交易机会，长期价值必须回到订单、成本、现金流和竞争格局。</p>
<p>制造业竞争的另一面，是地方政府愿意牺牲短期土地收益和财政收益，换取长期产业链。工业用地价格往往低于住宅和商业用地，园区还会配套道路、电力、污水处理、人才公寓和税收优惠。企业看中的不只是便宜土地，而是一整套低成本生产环境。正是这种组织能力，让很多产业在中国形成了完整链条和快速迭代能力。</p>
<p>但地方政府并不天然知道哪个产业最终会胜出。越是热门的新兴产业，越容易出现一拥而上的投资冲动。真正优秀的地方产业政策，应当从“给钱给地”转向“降低交易成本、完善公共平台、培养产业人才、促进真实需求和技术验证”。否则，政策越热，未来出清越痛。</p>

<h2 id="urbanization">八、半城市化：消费不足的制度根源之一</h2>
<p>中国拥有规模庞大的劳动力群体，也生产了大量商品，但居民消费占比长期偏低。这不能简单解释为中国人天生爱储蓄。更深的原因是，许多在城市工作的劳动者并没有完全获得城市公共服务和稳定预期。</p>
<p>如果一个人在城市工作，却担心子女教育、医疗保障、养老安排和住房成本，就很难放心消费。户籍制度、公共服务差异和高房价共同制造了半城市化状态：人在城市劳动，家庭安全感却没有完全落在城市。于是收入的一部分被储蓄、汇回老家或用于防御性支出。</p>
<p>这会形成宏观悖论：大量劳动者参与城市生产，却不能以同等力度参与城市消费；企业能生产大量商品，居民却不敢充分消费；社会总储蓄率偏高，内需不足，经济增长不得不更多依赖投资和出口。扩大消费不能只靠发放短期补贴，还要改善收入分配、公共服务、住房负担和社会保障预期。</p>

<h2 id="regional-gap">九、区域差距：城市竞争会自我强化</h2>
<p>地方竞争不是平均竞争。沿海城市、中心城市和产业基础较强的地区，更容易吸引企业、人才、资本和基础设施投资；资源越集中，机会越多，机会越多又吸引更多资源。这就是区域发展的自我强化。</p>
<p>落后地区也会努力招商，但如果缺少市场、物流、人才、产业配套和财政能力，单纯靠补贴未必能形成长期竞争力。有些地方为了留住企业，必须付出更高财政成本，甚至用债务维持表面繁荣。结果是强者更强，弱者更依赖转移支付和债务。</p>
<p>对个人而言，城市选择就是参与这种长期分化。人口净流入、产业集聚、财政质量、公共服务和真实就业机会，比短期房价涨跌更重要。对投资而言，也要看企业所在区域能否提供产业链、人才和政策配套，而不是只看地方口号。</p>

<h2 id="debt-resolution">十、债务化解：真正问题不是数字，而是现金流</h2>
<p>地方债务风险不只是余额高低，更关键的是现金流能否覆盖利息和到期压力。短期债务投向长期项目，土地收入下降，城投再融资难度上升，这些因素叠加，就会让局部风险更容易暴露。</p>
<p>债务化解通常有几类路径。第一是置换，用期限更长、利率更低、透明度更高的债务替换高成本隐性债务。第二是展期和重组，缓解短期流动性压力。第三是盘活资产和压缩低效支出。第四是财政体制改革，让地方拥有更稳定、可持续的收入来源。</p>
<p>货币政策也能争取时间。降息、增加流动性、资产购买、财政和货币配合，都可能缓解债务压力。但这些工具本质上是在买时间，而不是自动创造现金流。如果地方经济增长、土地收入、企业利润和居民收入不能恢复，债务问题只会从一个账户转移到另一个账户。</p>
<p>因此，化债不能只看有没有兑付，更要看地方发展模式是否改变。如果继续用新债维持低效投资，用短期融资支撑长期低回报项目，即使表面风险暂时下降，经济资源也会被锁在低效率资产里。真正健康的化债，是让地方财政重新回到可持续收入、清晰预算约束和有效项目筛选上。</p>
<p>这对金融资产也有直接影响。高收益城投债、地方国企信用、区域银行资产质量、基建链条订单，都与地方财政质量相关。投资者不能只看票面利率或主体级别，还要看所在地区人口、产业、土地市场、一般公共预算收入、转移支付依赖度和债务期限结构。</p>

<h2 id="trade-war">十一、贸易摩擦：外部冲突背后的内部失衡</h2>
<p>中美贸易冲突当然包含地缘政治、产业竞争、技术封锁和国家安全考量，但从宏观账户看，中国内部的储蓄和消费结构也是重要来源。居民消费不足，企业和政府部门投资强，社会储蓄率高，生产能力持续扩张，结果就是大量工业品需要外部市场消化。</p>
<p>经常账户差额本质上等于国民储蓄与国内投资的差额。当一个经济体储蓄长期高于国内投资需求，就会形成对外顺差。顺差不是单纯由汇率或某项贸易政策决定，而是由收入分配、财政结构、消费能力、产业结构和金融体系共同塑造。</p>
<p>因此，贸易摩擦的根源不能只在边境线上寻找。真正要降低外部失衡，需要提高居民收入占比，降低防御性储蓄需求，改善社保和公共服务，减少对投资和出口的过度依赖。这是一场内部结构调整，而不是靠几轮谈判就能彻底解决。</p>

<h2 id="market-implication">十二、资本市场里的政策市，应当这样理解</h2>
<p>中国资本市场长期带有政策市特征，但政策市不是简单的“政策一松就买，政策一紧就卖”。更准确的理解是，政策会改变行业规则、盈利分配、融资条件、估值中枢和竞争格局。它影响的是赛道边界和利润归属，而不仅是短期情绪。</p>
<p>房地产链条的估值逻辑改变，来自土地财政和人口预期的改变；制造业的主题行情，来自地方产业政策和全球需求变化；消费复苏的强弱，取决于居民收入和资产负债表；高股息资产的吸引力，来自低增长环境下现金流确定性的再定价。政策不是噪声，而是商业模型的一部分。</p>
<p>投资上要分清三类机会。第一类是政策托底带来的修复，适合看估值和风险释放；第二类是产业政策推动的成长，适合看订单和竞争格局；第三类是制度转型带来的长期再定价，适合看现金流、分红、资产质量和治理结构。把政策口号直接等同于长期价值，是常见错误。</p>

<h2 id="housing-strategy">十三、房地产：从全民信仰回到现金流资产</h2>
<p>过去房地产同时承载居住、投资、财政、抵押品和财富效应。它不是普通行业，而是中国经济的枢纽资产。正因如此，房地产调整也不会只是房企问题，而会影响土地财政、城投融资、居民资产负债表、银行资产质量和地方公共支出。</p>
<p>但趋势已经改变。人口结构、城镇化速度、居民杠杆、房价收入比和土地财政约束，都不支持“所有城市房价长期普涨”的旧信仰。未来房地产会更像分化严重的现金流资产：核心城市核心地段仍有稀缺性，人口流出地区、供应过剩地区和缺少产业支撑地区，资产价格可能长期承压。</p>
<p>个人决策上，买房首先回到居住和家庭稳定，而不是默认投资回报。判断一套房，不只看单价和过去涨幅，还要看城市人口、产业、租金回报、公共服务、持有成本和未来流动性。房地产从金融加速器退回民生资产，是理解下一阶段资产配置的关键。</p>

<h2 id="industrial-policy">十四、产业政策：机会在早期，答案在出清后</h2>
<p>地方政府推动产业升级，仍然会是未来很多年的主线。新能源、半导体、人工智能、机器人、低空经济、生物医药、高端装备，都可能获得政策、资本和园区资源支持。早期政策密集催化，往往会带来明显市场机会。</p>
<p>但产业政策不是利润保证。一个行业能否真正成立，要看终端需求是否真实，产品是否具备成本优势，技术能否规模化，现金流能否转正，竞争是否会快速恶化。很多行业在政策支持初期热闹非凡，随后进入价格战、产能过剩和淘汰赛，只有少数公司能穿越周期。</p>
<p>因此，产业投资要分阶段。早期按主题和催化交易，中期看订单、良率、成本和客户结构，后期看格局、现金流和资本回报率。不能在第一阶段就把所有公司按长期龙头估值，也不能在行业出清前重仓押注没有财务验证的故事。</p>

<h2 id="transition">十五、转型的方向：从投资驱动到居民部门修复</h2>
<p>中国经济下一阶段的核心，不是再复制一轮土地、基建和房地产驱动，而是让增长更多来自居民收入、技术进步、有效消费、产业升级和更可持续的公共财政。这意味着旧模式不会突然消失，新模式也不会一夜成型，转型更可能是渐进式的。</p>
<p>渐进式转型有三个特征。第一，政府仍会深度参与资源配置和风险处置，政策变化会长期影响市场。第二，地方债务、房地产和区域分化会持续消化，资产价格不一定快速修复。第三，产业升级和居民部门修复会同时推进，但节奏并不一致。</p>
<p>普通人需要接受一个现实：未来不是强刺激解决一切的环境，也不是完全自由放任的市场。更稳妥的策略是降低高杠杆资产依赖，保留现金流安全边际，选择财政质量和产业基础更好的城市，投资上更重视真实利润、分红能力、资产负债表和长期竞争力。</p>
<p>从政策方向看，未来更重要的不是再造一轮土地扩张，而是重新平衡政府、企业和居民部门。政府需要降低对土地和债务的依赖，企业需要从规模扩张转向效率和创新，居民部门需要更稳定的收入预期和更低的防御性储蓄。三者中任何一环缺失，转型都会变慢。</p>
<p>这也解释了为什么很多宏观政策看起来会同时强调稳增长、控风险、扩内需、促消费、产业升级和安全底线。它们不是互相独立的口号，而是在处理旧模式后遗症和新模式建设之间的张力。真正困难的地方在于，短期稳增长需要投资和信用支持，长期转型又要求减少无效投资和债务依赖。政策的摇摆感，往往来自这种双重目标。</p>

<h2 id="action-map">十六、普通人的行动地图</h2>
<p>第一，重新评估城市和房产。人口流入、产业结构、财政质量和公共服务，是比短期价格更重要的指标。对没有长期人口和产业支撑的区域，不要再用过去二十年的房地产经验外推未来。</p>
<p>第二，理解地方债和财政约束。地方财政压力会影响基建速度、公共服务、产业补贴和城投信用。高收益、低风险、政府兜底这类表述需要格外谨慎，真正要看现金流和偿债来源。</p>
<p>第三，投资制造业时重视周期和出清。政策支持可以制造机会，但长期回报来自成本、技术、客户、规模和现金流。补贴驱动的繁荣不能直接等同于企业内在价值。</p>
<p>第四，把消费复苏放在收入和保障体系里看。居民敢不敢消费，取决于收入预期、就业稳定、房价压力、教育医疗和养老安排。单一促销或短期补贴能改善边际需求，但很难改变长期储蓄倾向。</p>
<p>第五，建立政策与财务双重视角。政策决定行业边界，财务决定企业能否活下来。只懂政策容易追高，只看财务又可能忽略规则变化。两者结合，才更接近中国资产定价的真实逻辑。</p>

<h2 id="conclusion">十七、看懂一条线，才看得懂当下</h2>
<p>《置身事内》最重要的启发，是把看似分散的现象重新连成一条线。地方政府为什么拼增长，分税制为什么改变财政格局，土地财政为什么能支撑城市扩张，城投债为什么会累积，制造业为什么能崛起，消费为什么偏弱，贸易顺差为什么长期存在，外部摩擦为什么加剧，这些问题不是孤立答案，而是同一套制度和激励的连续结果。</p>
<p>中国经济过去的成功，来自政府组织能力、地方竞争、全球化窗口、基础设施和产业链集聚的结合。今天的压力，也来自同一套模式的边际变化：土地不再高速增值，居民杠杆接近上限，地方债务需要消化，外部环境更复杂，消费和收入分配必须重新调整。</p>
<p>真正成熟的判断，不是简单乐观或简单悲观，而是看清发动机如何运转、哪些零件已经老化、哪些零件仍有优势、哪些地方需要重构。只有把房价、地方债、制造业、消费和贸易放在同一张图上，才能理解当下中国经济的真实约束，也才能在个人选择和投资决策中少犯方向性错误。</p>
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
    if len(plain) < 7800:
        failures.append(f"{post.slug}: body too short: {len(plain)}")
    for word in forbidden:
        if word in article:
            failures.append(f"{post.slug}: forbidden/source wording present: {word}")
    required_terms = [
        "置身事内", "兰小欢", "地方政府", "分税制", "土地财政", "城投", "地方债",
        "房地产", "招商引资", "工业化", "户籍", "消费不足", "贸易摩擦", "高储蓄",
        "政策市", "居民部门", "转型",
    ]
    for word in required_terms:
        if word not in article:
            failures.append(f"{post.slug}: missing required topic: {word}")
    h2 = re.findall(r'<h2 id="([^"]+)">', article)
    links = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', article)
    if h2 != links or len(h2) < 14:
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
base.DATE = "2026-08-02"
base.BASE_DT = datetime(2026, 8, 2, 16, 5, tzinfo=timezone(timedelta(hours=8)))
base.PREV_EXISTING_URL = "/2026/navalmanack-ai-era-wealth-happiness-judgment-map/"
base.PREV_EXISTING_TITLE = "纳瓦尔宝典：AI 时代的财富、判断力与幸福地图"
base.SCRIPT_NAME = "publish-zheshenshinei-china-economy-article-20260802.py"
base.MANIFEST_NAME = "publish-zheshenshinei-china-economy-article-20260802-changed-files.json"
base.CHANGED = set()
base.INPUT_ORDER = [
    base.Post(
        source_id="BV14u3c6LEUE",
        slug="zheshenshinei-china-economy-housing-local-debt-trade-war",
        title="置身事内：看懂中国经济、房价、地方债与贸易战的一条线",
        desc="从地方政府激励出发，把分税制、土地财政、城投债、工业化、消费不足和贸易摩擦连成一条完整的中国经济因果链。",
        category="宏观经济",
        series="置身事内",
        tags=["置身事内", "中国经济", "地方政府", "分税制", "土地财政", "地方债", "房地产", "产业政策", "贸易摩擦", "消费"],
        minutes=31,
        body=BODY,
        cover_kicker="置身事内",
        cover_line="地方政府 · 土地财政 · 债务 · 贸易失衡",
        cover_theme=("#172554", "#0f766e", "#facc15"),
        duration=6369.789333,
        segments=2889,
        chars=30667,
    )
]
base.PUBLISH_ORDER = list(reversed(base.INPUT_ORDER))
base.validate = validate
base.copy_script_and_manifest = copy_script_and_manifest


if __name__ == "__main__":
    base.main()
