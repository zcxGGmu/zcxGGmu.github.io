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
spec = importlib.util.spec_from_file_location("base_publisher_naval_ai", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Unable to load base publisher: {BASE_PATH}")
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
_BASE_VALIDATE = base.validate


BODY = """
<p><img src="/images/posts/navalmanack-ai-era-wealth-happiness-judgment-map/cover.svg" alt="纳瓦尔宝典：AI 时代的财富、判断力与幸福地图"></p>
<p>一个人真正想要的，通常不是单纯变得更有钱，而是拥有更多选择，同时不在追逐更多的路上把自己弄丢。《纳瓦尔宝典》把财富和幸福放在同一本书里，正是因为这两个问题无法拆开：没有基本经济安全，很多自由只是纸面上的自由；可收入增加以后，焦虑、比较、欲望和身份压力也不会自动消失。</p>
<p>AI 时代让这个问题变得更尖锐。写作、代码、设计、翻译、研究、运营等脑力任务正在被重新定价，很多过去需要多年训练才能完成的标准化工作，开始被工具压缩到几秒钟。焦虑并不能靠一句“会用工具的人不会被替代”来化解，因为更关键的问题是：哪些任务的价格会下降，效率收益会归谁，哪些判断和责任不能外包，职业价格变化后，一个人还如何看待自己。</p>
<p>纳瓦尔提供的不是一份职业安全名单，而是一张控制权地图。财富是不让收入永远受制于出售时间；判断力是不把现实解释权交给情绪、舆论和算法；幸福是不把情绪开关交给欲望和比较；自我救赎是不让身体、习惯和注意力自动驾驶；哲学是不再等待外界替自己规定生命意义。把这五张图合在一起，核心只有一件事：在无法完全掌控的时代里，尽量把关键控制权拿回自己手里。</p>

<h2 id="map">一、财富与幸福必须放在同一张地图里</h2>
<p>只谈财富，容易把人生变成一张永远不够的资产负债表；只谈幸福，又容易忽视账单、房租、医疗、家庭责任和现实压力。更稳妥的顺序是：先用财富减少匮乏和被迫，再用“足够”约束无止境的追逐。缺钱时，谈自由要先过生存这一关；有钱以后，谈幸福还要过欲望这一关。</p>
<p>财富扩大外部选择，幸福减少内心强迫。一个人如果没有收入缓冲，所谓随心所欲往往只是自我安慰；一个人如果被欲望不断牵着走，资产越多也可能越焦虑。外部选择和内在平静少了哪一边，自由都会变成一项永远完不成的任务。</p>
<p>因此，《纳瓦尔宝典》的价值不在几句金句，而在于它把财富、判断、欲望、健康和意义重新连接起来。它提醒人，赚钱不是为了无限证明自己，幸福也不是对现实困难的逃避。真正的问题是：怎样在现实约束中积累选择权，同时避免让选择权反过来吞掉生活。</p>

<h2 id="wealth-definition">二、财富不是金钱，也不是地位</h2>
<p>财富、金钱和地位经常被混在一起，但它们不是同一种东西。地位是相对排名，办公室里的头衔、圈子里的座次、平台上的可见度，都带有零和性质。一个人往前，另一个人就会感到后退，所以地位竞争很容易把讨论变成人生攻击。</p>
<p>金钱是交换媒介，它让价值可以计量、储存和转移，却不等于财富本身。真正的财富，是那些不用持续出售时间也能产生价值的资产。它可以是公司股权、软件、设备、内容、品牌、方法论、客户信任，也可以是一套能被重复使用的流程和产品。</p>
<p>这一点非常关键。一个人如果只能用时间换钱，收入上限就被每日可出售时间锁住；一旦停止出勤，收入也会停止。财富的本质，是把劳动成果从劳动者当下的时间里解放出来，让它在自己不在场时仍然创造价值。</p>
<p>但财富游戏只有在创造真实价值时才是正和游戏。如果收益来自欺骗、寻租、垄断、信息差收割，或者把成本转嫁给更弱的人，那只是披着财富外衣的地位争夺。先创造社会真正需要的东西，再通过所有权保留其中一部分，才是更稳的财富路径。</p>

<h2 id="formula">三、财富公式：专长、责任感、杠杆与判断力</h2>
<p>财富可以拆成四个相互放大的要素：专长、责任感、杠杆和判断力。它们不是相加关系，而更像相乘关系。任何一项长期接近零，其他再高，结果也很难好。</p>
<p>专长不是标准化培训能完整复制的技能。社会能够批量培训的东西，通常也能批量培训别人来替代你。证书和技能当然有价值，但入口越清楚、路径越标准，人才市场越容易找到可比对象。真正的专长，往往来自个人天赋、成长环境、长期兴趣、现场经验、对具体人的理解，以及大量犯错后留下的直觉。</p>
<p>一个长期做社区房产服务的人，可能不只是会背户型和价格，而是知道不同家庭真正关心什么，知道装修、学位、通勤、交易流程里最容易出问题的环节。客户描述几句处境，他就能迅速缩小选择范围。这种能力来自多年现场语境、关系网络和对人的理解，很难被短期课程复制。</p>
<p>责任感不是年会口号，而是愿意把自己的名字和可验证交付联系起来。公开负责会带来更多信任、资源、股权和杠杆，也会带来声誉代价。责任、权力和收益必须尽量对称，否则责任感很容易退化为弱势一方单独背锅。普通人需要承担的是可承受的责任，而不是把家庭现金流暴露在无限风险里。</p>
<p>杠杆让专长和责任感获得规模。劳动力杠杆是组织别人共同工作；资本杠杆是让资金参与生产和投资；代码与媒体杠杆则让一次劳动被复制给更多人。过去，代码和媒体被称为无需许可的杠杆，因为创作和分发不必先等机构批准。</p>

<h2 id="ai-leverage">四、AI 让杠杆变便宜，也让稀缺性转移</h2>
<p>AI 的到来，让代码、文字、图像、分析和信息整理的生产成本继续下降。看起来每个人都拥有了更强杠杆，但财富不会自动增加。原因很简单：当杠杆变成公共品，稀缺性就会转移。</p>
<p>过去稀缺的是会写代码、会写文案、会做设计、会整理资料；现在这些能力正在被工具快速普及。新的稀缺性会落到问题选择、审美判断、具体语境、客户信任、责任承担和长期资产上。别人为什么相信你，为什么选择你，为什么愿意长期回来，才是更难复制的部分。</p>
<p>AI 对工作的冲击，可以拆成三步。第一步是任务替代。一个岗位通常由许多任务组成，工具会先压低规则清楚、重复出现、验收标准明确的任务价格。第二步是岗位重组。标准任务减少后，人的价值会更多集中在理解需求、沟通承诺、处理例外、承担结果和建立信任上。第三步是身份震动。当过去赖以确认自我价值的专业能力被工具接近，人必须重新回答“我是谁”和“我仍然能创造什么”。</p>
<p>因此，真正有效的动作不是简单学会更多按钮，而是把 AI 当杠杆，把问题、标准、责任和资产留在自己手里。用工具减少标准执行，把省下的时间投向具体语境、责任信任和可积累资产。如果只是用工具更快做完标准任务，再接受更多同类任务，长期结果可能只是变成更高效的任务接口。</p>

<h2 id="micro-asset">五、普通人的稳妥路径：微型资产，而不是孤注一掷</h2>
<p>很多人一听到财富和杠杆，就想到辞职创业、贷款冒险或追求百万流量。对缺少试错资本的人来说，这种路径太危险。更稳的办法，是先打造微型资产。</p>
<p>微型资产可以是一套解决行业问题的模板，一个稳定服务小客户群的方法论，一份持续增长的行业数据库，一个反复更新的内容栏目，一套自动化流程，或者一个能持续被别人使用的小工具。它的特点是：解决真实问题，能被复用，能经过反馈迭代，未来可能带来收入、机会、信誉或关系。</p>
<p>微型资产的好处，是失败成本可控。它不要求立刻辞职，也不要求把现金流押上去。白天做好本职工作，晚上和周末用有限时间测试一个真实问题，先看有没有人愿意使用、愿意复购、愿意介绍别人，或者愿意为它付费。这样积累出来的资产，才更接近选择权，而不是自我感动。</p>
<p>在 AI 时代，微型资产尤其重要。工具会让每个人的产能提高，但真正能留下来的不是“今天又完成了更多任务”，而是能否沉淀成自己带得走的东西。公司客户名单、内部保密成果和一次性汇报材料，不一定会变成个人资产；公开作品、方法论、口碑、产品、数据、流程和长期关系，才更可能在离开当前岗位后继续发挥价值。</p>

<h2 id="judgment">六、判断力是杠杆时代最昂贵的能力</h2>
<p>杠杆越大，判断越不能含糊。判断力不是知道更多，而是在不确定中估计长期后果，并做出较好选择的能力。资源、运气和制度都会影响结果，但判断力决定人在有限条件下如何行动。</p>
<p>判断力没有速成证书，它需要在真实反馈中反复校准。训练判断力的第一件事，是把自我从判断里请出去。人做决定时，总会优先寻找证明自己正确的证据。成熟的做法，是把观点当成待检验的假设，提前写清楚什么情况会证明自己错了。</p>
<p>第二件事，是用长期后果检验短期冲动。困难的选择不一定正确，但很多真正有价值的选择，短期都会更痛苦。是否增加未来选项，是否保留复利空间，是否让责任和收益更对称，是否让自己更接近长期目标，是判断力需要反复追问的问题。</p>
<p>第三件事，是记录而不是只靠感觉。一次结果容易让人误判自己，长期记录才能暴露模式。重要决定可以写下假设、证据、担忧、反方意见、预期兑现条件和复盘日期。几个月后再回头看，才知道自己是判断正确、运气好，还是只是被短期结果奖励了错误过程。</p>
<p>AI 可以帮助生成选项、压缩信息、寻找反例和模拟情境，但不能替人承担价值判断。工具可以分析怎样裁员最有效率，却不能替企业决定如何对待长期员工；工具可以列出投资方案，却不能替人承担亏损；工具可以生成漂亮表达，却不能替人决定自己要成为什么样的人。</p>

<h2 id="luck-compound">七、运气、复利与长期游戏</h2>
<p>财富绕不开运气，但运气并不只有一种。有人偶然撞上一轮行情，这是无法训练的运气；有人持续行动，增加了碰到机会的概率；有人长期积累，形成了敏锐判断，别人看不懂的机会他能看懂；还有一种运气，会主动找上门，因为一个人的专长、作品和信誉已经足够鲜明。</p>
<p>真正可训练的是后几种运气。持续行动让人暴露在更多可能性面前，长期学习让人识别别人看不见的机会，公开作品和稳定信誉让机会更容易找到你。所谓“好运”，很多时候是长期积累塑造出来的必然性。</p>
<p>复利也不只存在于金钱里。知识、关系、声誉、判断力、身体和习惯都来自复利。复利要成立，需要长期、稳定、可重复，还需要合作对象愿意继续和你玩长期游戏。短期冲刺可以带来漂亮数据，但如果损害信任、健康和声誉，就会破坏复利底座。</p>
<p>长期主义不是死扛。长期主义允许退出，尤其当目标已经失真、合作关系无法信任、健康被持续透支、机会成本明显过高时，退出不是背叛，而是为下一段值得长期投入的事情留下空间。真正重要的是和长期的人，做长期的事，用长期的方式积累。</p>

<h2 id="freedom">八、财富的终点是自由，而不是数字崇拜</h2>
<p>财富的目的，是减少被迫，增加选择。它不是为了把数字推到没有尽头，也不是为了赢过所有人。一个人可以通过积累足够资产降低真实生活成本，也可以找到愿意长期做的事，从而让“退休”不再只是停止工作，而是停止做自己不愿意做的事。</p>
<p>问题在于，财富数字不会自动告诉人什么时候够了。目标如果不提前写下，欲望会跑得比收入还快，积累最后可能变成一台永远不能关机的焦虑机器。所谓足够线，就是在资产、现金流、生活成本、健康、家庭责任和时间自由之间，给自己画出一条可执行的边界。</p>
<p>足够线不是躺平，也不是自我设限，而是把财富重新放回生活目的之下。钱负责提供缓冲和选择权，不该负责替人证明全部价值。一个人越早知道什么是足够，就越不容易被比较和排名拖进无休止的地位游戏。</p>

<h2 id="happiness">九、幸福是一种技能，而不是财富到账后的奖励</h2>
<p>幸福不是成功之后自动发放的奖品，而是一种可以练习的能力。这里的幸福更接近内心平和，而不是短暂狂喜。平和是静态的幸福，幸福是动态的平和。当一个人停止对外部世界无休止索取，并在此时此刻感到自己并不缺少什么，内心才有可能安静下来。</p>
<p>欲望可以理解成和自己签下的一份协议：在得到某个东西之前，我不会快乐。每多一个欲望，就多签一份不快乐协议。欲望本身没有错，问题是合同太多，而且经常默认自动续费。人一边抱怨压力，一边默默同意更多条件，最后把幸福推迟到下一个目标。</p>
<p>成功和幸福之间存在张力。成功常常来自对现状的不满，幸福却来自对现状的满足。一个人如果完全满足，可能缺少行动动力；如果永远不满，又永远无法安静。更成熟的方式，是保留少数真正重要的生成性欲望，把其他身份竞争型欲望逐步削掉。</p>
<p>欲望可以分成三类。生存性欲望关乎安全、住房、医疗、家庭和现金流；地位性欲望关乎比别人更高、更贵、更容易被看见；生成性欲望关乎创作、照料、探索、掌握一门技艺。生存需要资源，地位需要边界，生成需要时间和投入。越过基本安全线以后，幸福更依赖后两者的取舍。</p>

<h2 id="china-reality">十、在 2026 年的现实里理解“放下欲望”</h2>
<p>谈幸福不能脱离现实。一个人连房租、医疗和基本生活都无法保证时，劝他“幸福只来自内心”并不负责。外部条件会长期影响幸福，贫困、失业、疼痛、孤独和家庭压力不会因为一句格言就消失。</p>
<p>今天很多年轻人的痛苦，并不只是主动欲望太多，而是防御性欲望太重。买房不是单纯想炫耀，而是想获得安全感；拼命工作不是只为了排名，而是害怕失去收入；学习新工具不是只想卷别人，而是担心被系统淘汰。把这些都简单归为“欲望太强”，会误解真实处境。</p>
<p>因此，更实用的幸福练习不是要求自己立刻放下所有目标，而是先建立基本安全，再辨认哪些欲望来自真实需要，哪些来自比较、算法和社会评价。生存问题要用收入、缓冲和支持系统解决；地位焦虑要用边界解决；生成性欲望要用长期投入解决。</p>
<p>AI 时代还有一个效率悖论：工具省下的时间，未必自动变成自由。很多组织会把效率提升写进绩效表，工具替人省出两小时，系统转身要求再多产出三小时。如果效率长期只换来更多任务，而没有换来更少焦虑、更高自主权和更多可积累资产，就要警惕自己只是被改造成更高效的接口。</p>

<h2 id="health">十一、自我救赎从身体、注意力和习惯开始</h2>
<p>财富、判断力和幸福最终都会落到身体里。长期睡眠不足、久坐、过度加工饮食和持续屏幕刺激，会损害注意力、情绪和决策质量。一个身体反复报警的人，即使抓住机会，也可能没有足够耐力把它转化为结果。</p>
<p>健康不需要复杂包装。规律睡眠、日常活动、力量训练、相对少加工的食物、减少久坐、保留户外时间，这些听起来不刺激，却能持续十年。真正有效的习惯往往很朴素，问题是能否重复。</p>
<p>注意力也是需要训练的肌肉。冥想不必神秘化，它可以只是安静坐下，观察念头如何出现、消失、把人带走，再把注意力带回呼吸或一个稳定锚点。它像程序员查看代码如何运行：不是责骂自己为什么有杂念，而是看清系统怎么工作。</p>
<p>习惯设计要足够小。目标太大容易制造挫败，动作足够小、环境能够提醒、完成成本足够低，才可能持续。每天十分钟行走、二十分钟不看手机、固定睡前关闭屏幕、每周一次复盘，比宏大的自我改造更可靠。自我救赎不是燃烧意志力，而是给长期生活重新布线。</p>

<h2 id="philosophy">十二、哲学不是逃避现实，而是重新安放意义</h2>
<p>生命意义不能由统一答案发放。工作可以有意义，家庭可以有意义，创作可以有意义，照料他人可以有意义，学习和探索也可以有意义。意义不是天上掉下来的标签，而是在现实条件中主动赋予并持续验证的阶段性解释。</p>
<p>这和存在主义非常接近：世界未必先给人安排意义，人要在荒谬中创造意义。一个人持续做了什么，会让某些话慢慢变得可信。说家庭重要，就要在忙碌时给家人留出时间；说自由重要，就要为现金流和边界付出行动；说诚实重要，就要在说真话有代价时守住底线。</p>
<p>所谓理性佛教，可以理解为一边保持科学和理性，一边吸收观察欲望、训练注意力、减少执着的方法。它不是要求人脱离现实，也不是拒绝赚钱，而是提醒人不要把职业价格、市场评价和算法排名误认为全部自我。</p>
<p>AI 让哲学问题变成了现实压力。当机器可以写作、编程、分析、生成图像和组织材料，很多脑力劳动者赖以确认自我价值的身份会被动摇。真正需要重建的是：我是否把太多自我评价压在“我比机器强”上。人可以使用工具，也可以承认工具很强，但不必把存在价值交给效率竞赛。</p>

<h2 id="attention">十三、保护注意力，就是保护最重要的资产</h2>
<p>算法二十四小时营业，而且非常清楚人对愤怒、恐惧、紧迫感和比较最难拒绝。注意力被切得越碎，别人替我们安排欲望就越容易。一个人如果连一段完整思考的时间都守不住，独立判断很容易只剩一句口号。</p>
<p>每天应当留出一块不被打扰的空间。不带手机，不开即时通讯，不立刻问模型，也不评价自己表现好坏，只是把问题写下来，观察自己的担忧、假设和已知事实。先让大脑独立跑一遍，再用工具补材料、挑漏洞、找反例。这样，AI 会成为判断力的放大器，而不是判断力的替代品。</p>
<p>注意力训练的目标不是变成一个永远平静的人，而是少被外部刺激自动牵走。情绪出现时，能多停一秒；冲动消费前，能问一句这是不是地位性欲望；职业焦虑时，能把任务拆开，而不是把整个人生判死刑。这些微小停顿，会慢慢变成内在自由。</p>

<h2 id="actions">十四、七天实验：从一个最小动作开始</h2>
<p>知道和做到之间，差的通常不是下一句金句，而是一个足够小的动作、一点环境安排，以及面对反馈的耐心。不必在明天同时改变全部生活，七天只选一个实验就够。</p>
<p>可以做一次专长盘点：写下自己现在靠什么赚钱，哪些能力来自标准培训，哪些来自具体语境、长期经验、客户信任和独特组合。也可以记录一次重要决定：先写自己的判断，再让工具补充信息，最后对照结果复盘。也可以画出足够线：最低安全现金流、理想生活成本、健康底线、关系底线和不愿再牺牲的时间。</p>
<p>如果最困扰的是 AI 冲击，就做一张工作任务清单。把每天任务分成四类：标准执行、具体语境、责任信任、可积累资产。主动用工具减少第一类，把省下来的时间投向后三类。一个月后再看，自己得到的究竟只是更多任务，还是多了一项能带走的能力。</p>
<p>七天不能让人生翻盘，它只负责提供第一组真实样本。七天后，不看自己记住多少道理，只看哪个真实行为发生变化。能推动一个动作发生变化的思想，才算真正进入了生活。</p>

<h2 id="ninety-days">十五、九十天计划：把效率变成选择权</h2>
<p>如果想做得更系统，可以用九十天跑一轮闭环。前三十天做任务审计，把每天工作拆成标准执行、具体语境、责任信任和可积累资产四类，摸清哪些重复最多，哪些必须依赖现场语境，哪些可以用工具压缩。</p>
<p>中间三十天，把省下来的时间投向一个微型资产。它不必宏大，但必须解决真实问题，并经过别人反馈。可以是一套模板、一个小工具、一个行业资料库、一个稳定输出的专栏、一个自动化流程，或者一个为客户持续降低成本的方法。</p>
<p>最后三十天，验证它能否创造新的选择。有没有人愿意再次使用，愿意介绍别人，愿意给出反馈，愿意付费，或者愿意因为它信任你更多。只有经过反馈的资产，才不是自嗨。九十天计划的重点不是“创业成功”，而是把效率提升转化为选择权，而不是转化为更多消耗。</p>
<p>底线同样重要：不能为了打造副业，再次透支睡眠、关系和本职工作的基本信用。复利的前提是不要提前出局。健康、信誉和现金流一旦被击穿，很多选择权会一起消失。</p>

<h2 id="conclusion">十六、在效率之外，守住不被定价的部分</h2>
<p>财富和幸福可以同时存在，但它们处理的是不同问题。财富解决外部有没有选择，幸福处理做出选择以后内心能否安稳。财富最好用来增加余地，欲望也需要一条足够的边界。</p>
<p>AI 会越来越强，效率会继续提高，很多任务会被重新定价。但人的分量不是在和机器的效率比赛中撑出来的。人会孤独、迷茫、牵挂、后悔、重新开始，也会给自己的存在赋予意义。一段需要耐心才能维持的关系，一项只有自己知道为什么重要的坚持，一个没有任何产出却让心安静下来的夜晚，都不会出现在绩效表上，但它们构成了生活本身。</p>
<p>工具可以替人完成越来越多任务，却不能替人决定怎样对待一个不能帮自己赚钱的人，怎样在没有掌声的日子里继续做认为对的事，怎样在所有人都加速时允许自己慢下来想一想。财富、判断力、幸福、健康和哲学最终汇到同一个答案：把工具当工具，把人生还给自己。</p>
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
    if len(plain) < 6200:
        failures.append(f"{post.slug}: body too short: {len(plain)}")
    for word in forbidden:
        if word in article:
            failures.append(f"{post.slug}: forbidden/source wording present: {word}")
    required_terms = [
        "纳瓦尔宝典", "财富", "幸福", "AI", "人工智能", "专长", "责任感", "杠杆",
        "判断力", "复利", "欲望", "足够线", "自我救赎", "注意力", "理性佛教",
        "微型资产", "九十天计划",
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


base.ROOT = Path("/tmp/blog-publish-bv1is-20260802.stOOSI")
base.DATE = "2026-08-02"
base.BASE_DT = datetime(2026, 8, 2, 11, 25, tzinfo=timezone(timedelta(hours=8)))
base.PREV_EXISTING_URL = "/2026/poor-charlies-almanack-munger-mental-models-a-share-investing/"
base.PREV_EXISTING_TITLE = "穷查理宝典投资框架：芒格的多元思维模型与 A 股实践"
base.SCRIPT_NAME = "publish-naval-ai-wealth-happiness-article-20260802.py"
base.MANIFEST_NAME = "publish-naval-ai-wealth-happiness-article-20260802-changed-files.json"
base.CHANGED = set()
base.INPUT_ORDER = [
    base.Post(
        source_id="public-audio-naval-ai-wealth-happiness-20260802",
        slug="navalmanack-ai-era-wealth-happiness-judgment-map",
        title="纳瓦尔宝典：AI 时代的财富、判断力与幸福地图",
        desc="AI 正在重写脑力劳动价格，真正需要重建的是财富、判断力、幸福、健康和意义的控制权：把工具当杠杆，把人生还给自己。",
        category="读书笔记",
        series="纳瓦尔宝典",
        tags=["纳瓦尔", "财富", "幸福", "AI", "人工智能", "判断力", "杠杆", "专长", "复利", "注意力"],
        minutes=17,
        body=BODY,
        cover_kicker="纳瓦尔宝典",
        cover_line="财富 · 判断力 · 幸福 · AI 时代",
        cover_theme=("#111827", "#2563eb", "#f59e0b"),
        duration=5504.597375,
        segments=1716,
        chars=28107,
    ),
]
base.PUBLISH_ORDER = list(base.INPUT_ORDER)
base.validate = validate
base.copy_script_and_manifest = copy_script_and_manifest


if __name__ == "__main__":
    shutil.rmtree(Path(__file__).with_name("__pycache__"), ignore_errors=True)
    base.main()
    shutil.rmtree(Path(__file__).with_name("__pycache__"), ignore_errors=True)
