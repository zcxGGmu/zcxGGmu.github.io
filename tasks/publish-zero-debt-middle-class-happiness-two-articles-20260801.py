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
spec = importlib.util.spec_from_file_location("base_publisher_zero_debt_middle_class", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Unable to load base publisher: {BASE_PATH}")
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
_BASE_VALIDATE = base.validate


BODY_ZERO_DEBT = """
<p><img src="/images/posts/zero-debt-era-cashflow-safety-2026/cover.svg" alt="零负债时代：把债务清零，才是真正的安全感"></p>
<p>2026 年，真正过得滋润的人，未必是住大房子、开豪车、账面资产很高的人，而是那些没有房贷、车贷、消费贷和信用卡分期压力的人。过去二十年，很多人相信胆子越大、杠杆越高、资产越多，人生就越成功；但当收入预期下降、资产价格不再单边上涨、现金流开始变得脆弱，游戏规则已经反过来了。</p>
<p>零负债不是贫穷，也不是苦行。它是一种新的财富状态：房贷清零，或者买房时没有把未来几十年的收入完全押进去；消费贷不碰，分期和借贷不碰；生活流水健康，每一笔收入扣除日常开销后，都真正属于自己。这样的家庭未必最有钱，却拥有非常稀缺的东西：下限稳、压力小、选择权大。</p>
<p>在债务驱动的年代，负债看起来像加速器；在收入不确定、资产回报下降的年代，负债更像压在身上的重量。风平浪静时，它让人显得体面；风浪到来时，它会决定一个人沉得多快。</p>

<h2 id="change">一、聚会上的风向已经变了</h2>
<p>过去的饭局里，很多人聊的是谁又加杠杆买了新房，谁换了新车，谁能借到更多钱，谁敢把资产盘子做大。那时的气氛里，债务不是压力，而像一种能力证明：能贷款、敢贷款、敢上车，似乎就意味着站在上升通道里。</p>
<p>现在话题变了。有人拿到奖金后的第一件事，不是旅游，不是买理财，也不是升级消费，而是把剩余房贷一次性还掉。手机银行里显示房贷为零的那一刻，长期绷紧的神经才真正松下来。哪怕行业下行，公司裁员，也不会立刻被每月固定还款压垮。</p>
<p>还有小微经营者，过去一年最大的成就不是赚了多少，而是还清了银行贷款。终于能睡一个安稳觉，不用睁眼就想到利息和还款日。这些不是孤立个案，而是同一个信号：财富评价正在从“能借多少”转向“能不欠多少”。</p>

<h2 id="definition">二、零负债人群到底是什么</h2>
<p>零负债人群不是没有欲望，也不是没有消费能力，而是极早看懂了规则变化。第一，他们没有房贷这座月供大山，或者至少已经把高利率时期的贷款大幅压下去。第二，他们严控消费贷，不为了还没吃进肚子里的肉透支明天的钱。第三，他们的生活极简但不寒酸，现金流干净，固定成本低。</p>
<p>真正的零负债，不只是债务数字为零，更是一种财务哲学：不把未来收入过度卖给今天，不把脆弱的工作收入抵押给长期负债，不为了表面体面牺牲睡眠和自由。这样的人看起来低调，却已经把生活下限守住了。</p>
<p>过去很多人把负债当常态，甚至把零负债当成需要解释的异常。但在今天，异常的也许不是不借钱，而是把几十年现金流全部绑定在一套资产和一个工作预期上，还以为自己非常安全。</p>

<h2 id="income">三、收入预期下降，让债务变成断头台</h2>
<p>债务最可怕的地方，是它不关心你的收入是否稳定。月薪三万元时，每月一万五的房贷还能勉强承受；月薪降到一万五时，同样的房贷立刻变成悬在脖子上的刀。很多行业已经从年年涨薪、奖金丰厚，走向降薪、裁员、补贴取消、奖金回收。未来收入的不确定性，正在重塑家庭财务决策。</p>
<p>过去的乐观来自收入曲线向上。只要工资会涨，今天看起来沉重的月供，几年后就会变轻。但现在，很多人的收入曲线不再向上，甚至可能阶梯式下行。此时继续维持高负债，等于用旧时代的假设承担新时代的风险。</p>
<p>零负债人群对自己的下限非常谨慎。他们不一定追求最高收益，却会先确保最坏情况下仍能活下去。这个顺序非常重要：先活得稳，再谈赚得快；先确保不会被债务拖死，再谈资产增值。</p>

<h2 id="asset">四、资产不再单边增值，利息就变成真实成本</h2>
<p>过去很多人敢贷款，是因为相信房子会涨。哪怕贷款利率 5%，只要房价每年涨 10%，杠杆就是助力。问题在于，当房价不涨甚至下跌时，逻辑彻底反转：本金不再扩张，利息却还在每个月稳定流出。</p>
<p>一笔 150 万贷款，利率 4.2%，每月还款一万多，其中很大一部分都是利息。清掉贷款之后，家庭固定生活成本可能从两万多降到几千。账面现金少了，但抗风险能力反而翻倍，因为每个月不再被银行优先扣走一大笔。</p>
<p>这就是去杠杆的力量。它不是让人突然暴富，而是把家庭现金流从“先还银行”改成“先保自己”。在资产不再保证增值的环境里，减少利息支出本身就是一种确定性收益。</p>

<h2 id="deflation">五、从通胀思维转向通缩思维</h2>
<p>十年前，很多债务会被通胀稀释。物价涨、工资涨、资产涨，今天看起来沉重的还款，几年后可能就变轻了。那时借钱买资产，等于是用未来更便宜的钱偿还今天的债务。</p>
<p>但如果进入通缩压力环境，逻辑完全不同。收入不涨，资产缩水，钱变得更贵，债务反而越来越重。房子市值下降，欠银行的钱却不会跟着下降；工资变少，月供也不会自动变少。这就是很多断供风险背后的真实结构。</p>
<p>在这种周期里，提前还贷不再只是保守选择，而是对宏观环境的防御。既然保本理财收益很难跑赢房贷利率，减少利息支出就变成了最稳的一种“投资”。</p>

<h2 id="profit">六、没有债务后，每一分收入才真正是利润</h2>
<p>很多人看似收入不低，但钱还没捂热就流走了。房贷扣掉一大块，车贷扣掉一块，信用卡和消费贷再扣一层，最后能自由支配的现金少得可怜。收入数字很漂亮，实际控制权却很小。</p>
<p>零负债人群不一样。赚到的钱扣除日常生活后，大部分都能留下来。月收入不一定最高，但每一分现金流都更干净，心理压力也更小。一个月赚三万但只剩五千可支配，和一个月赚一万五但没有固定债务，生活韧性可能完全不同。</p>
<p>财务自由的第一步，不是资产数字巨大，而是收入不再被债务预先分走。钱流进来之后，真正由自己决定去向，这才叫拥有现金流。</p>

<h2 id="low-cost">七、低生活成本带来反脆弱性</h2>
<p>零负债的家庭，固定成本往往低到惊人。没有房贷车贷，一个月的基础开销可以压到很低。公交、地铁、公园、图书馆、社区设施、公共医疗和城市基础设施，构成了低成本生活的底座。</p>
<p>这些公共资源的建设成本很高，但普通人使用成本很低。只要没有沉重负债，一个家庭可以用很低的现金消耗维持体面生活。行业变化、收入下降、短期失业，都不会立刻把家庭推入绝境。</p>
<p>这就是反脆弱性：别人必须维持高收入才能维持生活，你只需要维持基本收入就能不崩。别人被迫忍受不喜欢的工作，你有时间寻找新路径。真正贵的不是房子和车，而是被高固定成本锁死的人生。</p>

<h2 id="transfer">八、负债人群在补贴零负债人群</h2>
<p>高负债家庭通常承担更多利息、更高税费和更重消费支出。这些钱一部分进入金融系统，一部分进入财政和公共建设，再转化为地铁、高铁、公园、电网、学校和城市设施。零负债人群同样享受这些公共资源，却没有对应的债务压力。</p>
<p>这听起来扎心，但它揭示了一个事实：当一个人清空负债、持有现金流优势，就从高压力循环里跳了出来。他不再需要为了维持高成本生活不断把自己卖给系统，也不再用未来收入为今天的体面持续买单。</p>
<p>负债不一定错误，但在错误周期里，高负债会把人变成系统的燃料。零负债则让人从被动付款者，转向主动选择者。</p>

<h2 id="actions">九、普通人的三条行动建议</h2>
<p>第一，有能力就优先处理高利率老贷款。尤其在保本收益跑不过房贷利率时，还贷等于锁定收益。要把投资和债务分开看：还债是确定性减少支出，投资是承担风险获取收益，二者不是一回事。</p>
<p>第二，没能力一次性清贷，就坚决不再加杠杆。消费贷、信用卡分期、装修贷、旅游贷、所谓免息，都要谨慎。通缩预期下，每一笔新债都可能变成未来现金流的深坑。保护现金流，要像保护生命一样认真。</p>
<p>第三，建立现金流护城河。至少准备覆盖全家六个月开支的应急金；同时建立主业、副业、稳健资产三元结构。主业求生存，副业求发展，资产配置做增值。真正的安全感，不是一份所谓铁饭碗，而是离开单一收入来源后仍能活得下去。</p>

<h2 id="balance-sheet">十、给家庭资产负债表做一次压力测试</h2>
<p>判断自己是否应该提前还债，不能只看账户里有多少钱，而要看家庭资产负债表能不能经受压力测试。把未来十二个月的固定支出列出来：房贷、车贷、教育、保险、赡养、基本生活，再假设收入下降三成、五成甚至短期归零，看看现金流能撑多久。</p>
<p>如果一旦降薪就立刻紧张，说明债务已经超过安全边界；如果失业半年仍能正常生活，说明家庭有真正的缓冲。很多人追求资产增值，却忽视了负债端的刚性。资产价格会波动，收入会波动，债务还款日却不会因为情绪和周期而推迟。</p>
<p>压力测试之后，才知道自己需要的是投资收益，还是先降低固定成本。对多数普通家庭来说，先把高息债务压下去，往往比追逐不确定收益更务实。</p>
<p>执行上可以分三步：先保留六到十二个月应急金，再优先偿还高利率和期限长的债务，最后才考虑投资组合优化。这样做不刺激，但能把家庭从被动还款状态里慢慢救出来。</p>

<h2 id="freedom">十一、真正的富裕，是不需要借钱也能过得好</h2>
<p>零负债不是要求每个人都过极端苦行生活，而是提醒人看清时代底色。债务驱动、欲望膨胀、资产单边上涨的阶段已经过去，普通人最可靠的财富密码，是降低负债、降低固定成本、守住现金流、提高选择权。</p>
<p>能让人躺赢的，不是更高杠杆，而是更清醒的财务结构。没有债务，不代表没有野心；恰恰相反，它让一个人有机会在风险来临时不被迫出局，有机会重新选择工作、城市、行业和生活方式。</p>
<p>真正的财富自由，不是能借到多少，而是不借也能活得很好。2026 年最好的护身符，可能不是更大的资产盘子，而是一张干净的负债表。</p>
"""


BODY_MIDDLE_CLASS = """
<p><img src="/images/posts/middle-class-income-happiness-enough-money/cover.svg" alt="月入五六万的幸福边界：中产家庭的财富够用哲学"></p>
<p>在中国，最幸福的人未必是最有钱的人。真正舒服的状态，常常出现在一个很微妙的区间：城市家庭月收入五万到六万元，房贷压力不过度，生活开销可控，理财结构简单，时间还属于自己。这个数字不绝对，但它背后有一条清晰逻辑：钱足以覆盖大多数生活问题，却还没有复杂到反过来管理人。</p>
<p>财富的作用并不是无限增加快乐。钱少时，每多一笔收入都能快速减少焦虑；但当基本生活、安全感、教育、医疗、旅行和应急资金都能覆盖之后，继续增加财富带来的幸福提升会明显变慢。再往上，钱甚至会制造新的工作、新的责任和新的关系成本。</p>
<p>幸福的关键不是账户数字最大，而是生活掌控感最强。收入能覆盖生活，资产能抵御风险，欲望没有超过能力，财富没有复杂到吞掉全部精力，这才是许多家庭真正向往的状态。</p>

<h2 id="threshold">一、为什么不是越有钱越幸福</h2>
<p>财富当然重要。它带来选择权、教育资源、医疗保障、抗风险能力和更好的生活条件。问题在于，财富对幸福的边际贡献并不是线性的。穷困时，钱能直接解决痛苦；温饱之后，钱能提高舒适；但过了某个临界点，更多财富带来的快乐会越来越少。</p>
<p>高资产家庭可能拥有更大的房子、更复杂的投资、更高端的消费和更多社会资源，但也会面对资产配置、税务合规、股权结构、家族传承、公司现金流、人情关系和风险隔离。钱不再只是工具，而会变成一套需要持续照看的系统。</p>
<p>所以，真正值得追求的不是无限堆高资产，而是在“够用、稳健、简单、可控”之间找到平衡点。对许多城市家庭来说，月入五六万恰好接近这个平衡点。</p>

<h2 id="budget">二、认真算一笔家庭账</h2>
<p>假设夫妻两人税前月收入合计五万到六万元，加上年终奖，全年税前收入大约七十五万到八十万元。扣除个税和社保后，家庭全年可支配收入大概在六十万元上下。这个数字在一线城市算不上大富大贵，但如果房贷没有失控，已经能覆盖三口之家的大部分需求。</p>
<p>房贷每月一万二到一万五，一年约十五到十八万；日常吃用每月八千到一万，一年约十到十二万；孩子教育、家庭保险一年约七到十万；养车交通一年约四万；再加旅行、人情和其他支出，全年总开销大约四十一到五十二万元。</p>
<p>最后还能结余八到十九万元。这个结余不是夸张的暴富数字，却足以建立应急金、做基础资产配置、覆盖短期风险。更重要的是，生活里的多数常见问题都能处理：房贷还得起，孩子养得起，父母看病有准备，一年能安排旅行，想吃顿好的不用反复纠结。</p>

<h2 id="coverage">三、舒服的收入不是想买什么都买得起</h2>
<p>真正舒服的收入，不是让人什么都买得起，而是让人多数时候不用因为钱做违心选择。五六万的家庭月收入，微妙之处正在这里。它还没有到挥霍无度，却能让生活摆脱很多具体焦虑。</p>
<p>孩子的教育可以选择适合的方案，不必为了证明阶层硬挤昂贵圈层；家庭保险可以配置基本保障，不必遇到疾病就现金流崩溃；旅行和餐饮可以保留品质，不必每次都看价格；偶尔买喜欢的东西，也不用纠结半个月。</p>
<p>这不是奢侈自由，而是日常自由。很多幸福感并不来自顶级消费，而来自“不必为普通消费过度紧张”。钱在这里的价值，是把生活从低层次焦虑中解放出来。</p>

<h2 id="security">四、生存焦虑基本消失</h2>
<p>收入较低时，焦虑往往非常具体：几千元的维修、一次体检、孩子一学期课外班、父母一次住院、短期失业，都可能打乱家庭节奏。当家庭月收入达到五六万，并且有一定储蓄后，这些问题不再立刻变成灾难。</p>
<p>安全感不是抽象感受，而是现金流和储蓄给出的底气。一个家庭如果有应急金、有保险、有稳定结余，即使遇到短期波动，也有时间处理，而不是马上被迫做糟糕选择。</p>
<p>这种安全感，是更低收入家庭尚未建立起来的，也是一些高收入但高负债、高支出家庭反而失去的。收入数字并不等于安全感，现金流结构才决定安全感。</p>

<h2 id="complexity">五、钱还没有变成新的工作</h2>
<p>当资产达到很高规模，管理财富本身会变成一份工作。房产怎么配置，股权怎么持有，税务怎么合规，家庭资产怎么隔离，孩子未来怎么传承，企业现金流怎么安排，每一项都要投入时间和精力。</p>
<p>钱少时，人追着钱跑；钱多到一定程度后，人可能开始替钱打工。每天睁眼第一件事，不再是今天如何生活，而是公司现金流有没有问题、投资有没有回撤、账户安排有没有漏洞、资产结构是否安全。</p>
<p>月入五六万的中产家庭，通常还处在财富管理相对简单的阶段。存款、保险、指数基金、稳健资产配置，再加定期复盘，基本就能覆盖大部分需求。不需要频繁和财富顾问开会，也不需要把生活变成复杂资产管理项目。</p>

<h2 id="consumption">六、消费有品质，但没有身份负担</h2>
<p>这个收入区间的消费状态很舒服：下馆子不用每次都精打细算，买东西不用天天比价，一年可以安排一两次旅行，孩子可以上公立学校并搭配真正需要的课外班。生活能买到舒适、安全和体面，但还不需要为了证明自己进入豪宅、豪车、国际学校和昂贵圈层。</p>
<p>真正的消费自由，不是每两年换一辆百万豪车，而是花钱时不心疼，不花时也不觉得丢人。它不是炫耀型消费，而是舒适型消费；不是为了给别人看，而是为了让家庭生活更稳定、更放松。</p>
<p>如果欲望超过能力，五六万也会焦虑；如果欲望被管理得很好，这个收入就足以形成非常高的生活满意度。</p>

<h2 id="relationships">七、社会关系相对干净</h2>
<p>收入太低时，人在很多关系里容易缺少底气。可财富太高后，也会出现另一种麻烦：有人找你借钱，有人找你投资，有人找你借资源，有人靠近你不是因为喜欢你，而是因为你身上有可利用价值。</p>
<p>月入五六万的家庭，通常能够维持体面，却又没有成为所有人眼中的资源中心。人际关系不会因为贫穷失衡，也不会因为财富过度复杂。这种干净和松弛，是很多钱也不一定买得到的。</p>
<p>家庭幸福很依赖关系质量。钱越多，如果关系越复杂、压力越大、算计越多，幸福感未必上升。适度财富反而能让人保持体面边界和生活秩序。</p>

<h2 id="hedonic">八、享乐适应会让高消费变普通</h2>
<p>第一次住五星级酒店会很开心，连续住一年就会习惯；第一次开百万级汽车会兴奋，半年后它也只是交通工具。这是人类的享乐适应。生活标准不断提高，但快乐不会永远同步上涨。</p>
<p>因此，财富增加到一定程度后，继续消费带来的兴奋会快速衰减。一个人很容易进入更高消费标准，却不一定获得更高幸福感。最后留下来的，可能只是更高的维护成本和更重的比较压力。</p>
<p>反过来，如果一个家庭懂得控制欲望，把钱用在安全感、健康、陪伴、体验和长期资产上，五六万的月收入已经能让生活非常稳。幸福不是无限升级消费，而是知道什么足够。</p>

<h2 id="time">九、幸福非常依赖时间</h2>
<p>很多高资产人群最缺的不是钱，而是完整睡眠、自由时间和不被打扰的生活。资产越多，要守护的东西也越多；企业越大，对员工、客户、股东和现金流的责任越重。能松一口气的时刻反而越来越少。</p>
<p>幸福依赖时间。能休息，能陪伴家人，能在遇到问题时有应对方案，能不被账户数字持续绑架，才是真正踏实的生活。钱到了够用的量级，剩下的应该是生活，而不是继续给自己增加财富管理任务。</p>
<p>月入五六万的幸福，本质是钱够用之后，生活还能属于自己。它不是最高财富状态，却可能是时间、收入、关系和风险之间最平衡的状态。</p>

<h2 id="not-absolute">十、五六万不是标准答案，结构才是答案</h2>
<p>这个收入数字当然不是全国统一标准。城市不同，房贷不同，家庭成员不同，父母健康状况不同，孩子教育选择不同，都会改变幸福边界。小城市可能不需要五六万也很从容，一线城市核心区如果房贷过重，五六万也会紧张。</p>
<p>真正重要的不是某个绝对数字，而是结构：固定支出有没有失控，结余率是否稳定，应急金是否充足，财富管理是否简单，消费欲望是否可控，时间是否仍然属于自己。只要这些结构成立，收入数字可以低一些；如果结构崩坏，收入再高也会焦虑。</p>

<h2 id="principle">十一、幸福的财富状态有四个共同点</h2>
<p>第一，收入能覆盖生活。房贷、教育、医疗、保险、日常消费和适度旅行，都不会把家庭压垮。第二，资产能抵御风险。至少有应急金、基础保险和稳健配置，短期失业或突发支出不会让家庭崩盘。</p>
<p>第三，欲望没有超过能力。消费有品质，但不为了面子强行升级。第四，财富没有复杂到占据全部精力。资产结构简单，决策清楚，钱服务生活，而不是生活服务钱。</p>
<p>真正的财富自由，不是账户拥有最多的钱，而是钱够用之后，还能把生活还给自己。对很多中产家庭来说，追求这个状态，比盲目追求更高数字更有意义。</p>
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
    required_terms = {
        "zero-debt-era-cashflow-safety-2026": ["零负债", "现金流", "房贷", "消费贷", "提前还贷", "通缩", "储蓄", "选择权"],
        "middle-class-income-happiness-enough-money": ["月入五六万", "幸福", "中产", "可支配收入", "房贷", "安全感", "消费自由", "享乐适应", "时间"],
    }
    min_lengths = {
        "zero-debt-era-cashflow-safety-2026": 3600,
        "middle-class-income-happiness-enough-money": 3200,
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
base.BASE_DT = datetime(2026, 8, 1, 22, 40, tzinfo=timezone(timedelta(hours=8)))
base.PREV_EXISTING_URL = "/2026/consumerism-poverty-cashflow-self-investment/"
base.PREV_EXISTING_TITLE = "消费主义与贫穷循环：把钱花在刀刃上的生活框架"
base.SCRIPT_NAME = "publish-zero-debt-middle-class-happiness-two-articles-20260801.py"
base.MANIFEST_NAME = "publish-zero-debt-middle-class-happiness-two-articles-20260801-changed-files.json"
base.CHANGED = set()
base.INPUT_ORDER = [
    base.Post(
        source_id="public-audio-zero-debt-era-20260801",
        slug="zero-debt-era-cashflow-safety-2026",
        title="零负债时代：把债务清零，才是真正的安全感",
        desc="零负债不是苦行，而是在收入预期下降、资产不再单边增值和通缩压力下，用低固定成本、干净现金流和选择权重建家庭安全感。",
        category="财富认知",
        series="债务与自由",
        tags=["零负债", "现金流", "提前还贷", "房贷", "消费贷", "通缩", "储蓄", "选择权", "反脆弱", "财富自由"],
        minutes=11,
        body=BODY_ZERO_DEBT,
        cover_kicker="债务与自由",
        cover_line="零负债 · 现金流 · 选择权",
        cover_theme=("#111827", "#0f766e", "#f59e0b"),
        duration=622.9681875,
        segments=295,
        chars=3827,
    ),
    base.Post(
        source_id="public-audio-middle-class-happiness-20260801",
        slug="middle-class-income-happiness-enough-money",
        title="月入五六万的幸福边界：中产家庭的财富够用哲学",
        desc="月入五六万的城市中产之所以可能更幸福，是因为收入覆盖生活、资产抵御风险、消费保持品质、财富管理仍然简单，生活还能属于自己。",
        category="财富认知",
        series="幸福财务",
        tags=["月入五六万", "中产", "幸福", "可支配收入", "安全感", "消费自由", "享乐适应", "时间", "财富管理", "够用哲学"],
        minutes=7,
        body=BODY_MIDDLE_CLASS,
        cover_kicker="幸福财务",
        cover_line="够用 · 简单 · 生活掌控感",
        cover_theme=("#111827", "#2563eb", "#22c55e"),
        duration=408.64,
        segments=286,
        chars=2707,
    ),
]
base.PUBLISH_ORDER = list(base.INPUT_ORDER)
base.validate = validate
base.copy_script_and_manifest = copy_script_and_manifest


if __name__ == "__main__":
    shutil.rmtree(Path(__file__).with_name("__pycache__"), ignore_errors=True)
    base.main()
    shutil.rmtree(Path(__file__).with_name("__pycache__"), ignore_errors=True)
