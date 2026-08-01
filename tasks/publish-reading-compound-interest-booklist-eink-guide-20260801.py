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
spec = importlib.util.spec_from_file_location("base_publisher_reading_booklist", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Unable to load base publisher: {BASE_PATH}")
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
_BASE_VALIDATE = base.validate


BODY = """
<p><img src="/images/posts/reading-compound-interest-booklist-eink-guide/cover.svg" alt="读书像一场无痛换脑：阅读复利、书单与电纸书选择"></p>
<p>读书最像一场无痛的换脑手术。坚持一年以上，并且不是漫无目的地翻页，而是持续读对自己有穿透力的书，一个人会明显感觉到自己的判断力、审美、决策水平和情绪韧性都在变强。大脑还是原来的大脑，记忆、性格和偏好没有被抹掉，但思维模型已经被悄悄重装。</p>
<p>阅读的价值不只在“知道更多”。真正厉害的是智力复利：长期积累高质量思想，形成一套能不断自我增殖的认知资本。巴菲特和芒格的优势，表面看是投资能力，深层看是长期阅读、学习、思辨和模型积累带来的决策质量。优秀直觉不是天降灵感，而是大量输入、反复比较、长期沉淀之后形成的快速判断。</p>
<p>在 AI 时代，阅读不会因为机器更会总结而失去价值。相反，越是信息泛滥，越需要一个更好用的大脑去筛选、连接、判断和决策。财富越来越像认知的奖赏，而不是单纯勤奋的补偿。一个正确决策会被工具和资本放大，无数正确决策会把人生曲线整体向上抬。</p>

<h2 id="reading-compound">一、阅读的第一层收益：智力复利</h2>
<p>教育的回报并不是抽象口号。《贫穷的本质》里提到过印度尼西亚在石油危机后大规模建学校的案例。研究者比较了受益于新建学校的年轻人和错过入学年龄的年长者，发现多接受一年小学教育，收入会出现可观提升。教育提升收入，并不是因为学历标签本身有魔法，而是因为它改变了一个人的能力、机会和选择范围。</p>
<p>保持阅读习惯，本质上是一种不离校的自我教育。不同的是，学校教育常常由课程表安排，而阅读可以自己筛选老师。一本好书就是一次跨时空对话：与你交谈的可能是科学家、企业家、哲学家、投资人、小说家，也可能是某个领域最会把复杂经验讲清楚的人。</p>
<p>读书久了，最明显的变化是决策质量。遇到问题时，脑子里不再只有本能反应，而会浮现许多模型：机会成本、复利、风险收益比、课题分离、均值回归、人性弱点、激励机制、长期主义、黑暗森林、市场先生。模型越多，现实越不容易把人困死在单一解释里。</p>
<p>阅读的复利还有一个特点：前期很慢，后期很猛。刚开始读书，像是在往空仓库里搬东西，短期看不到什么变化；读到一定数量后，书与书之间开始互相连接，新知识不断挂到旧模型上，判断速度和理解深度会突然提高。那一刻才会发现，过去所有看似零散的输入，其实都在给大脑搭桥。</p>

<h2 id="reading-resilience">二、阅读的第二层收益：生命韧性</h2>
<p>如果只把书当工具箱，阅读会显得很功利。遇上问题，就翻书找答案；工作卡住，就找方法论；心里痛苦，就找别人的经验。这个阶段当然有用，但阅读真正更深的价值，是它给人提供一个额外的精神空间。</p>
<p>现实生活总会有荒诞和至暗时刻。有人突然失业，有人关系破裂，有人疾病缠身，有人发现努力并不总有回报。小说、人文和历史在这种时候会发挥奇特作用：它让人看到更复杂的痛苦，也看到人在痛苦中如何没有立刻崩塌。</p>
<p>当小说里的人物惨到让人不忍心，现实中的自己反而会获得一点喘息：原来人可以这么难，原来苦难不是只发生在自己身上，原来人在荒诞里也能继续往前。好的故事不会把痛苦抹平，但会让痛苦变得可承受。</p>
<p>阅读慢慢会把生活变成一个更大的房间。外面下雨，灯光柔和，手边有茶，翻开书，人就进入另一个精神地带。那里可以休息，可以修炼，可以和远处的人共鸣，也可以暂时从现实泥潭里出来换一口气。</p>

<h2 id="book-principle">三、选书原则：你的感受以你为准</h2>
<p>书单再有名，也不能替代个人感受。别人再推荐，一本书如果读起来完全不喜欢，对你来说就不是此刻最好的书。阅读不是考试，不需要为了证明品位而硬啃所有经典。先建立“愿意继续读”的正反馈，比一开始就挑战最难的书更重要。</p>
<p>选书可以按四类来搭建：有趣的书，财富类的书，致用类的书，小说与人文类的书。有趣的书负责让人爱上阅读；财富类的书负责压住贪念、理解风险；致用类的书负责解决现实中的情绪、人际和工作问题；小说与人文类的书负责扩展生命经验和精神韧性。</p>
<p>真正好的阅读系统，不是只读一个方向。只读投资，人容易变得功利；只读文学，现实执行可能不足；只读方法论，精神会干枯；只读鸡汤，又容易失去判断。四类书交替阅读，脑子才会既有工具，也有审美；既有现实感，也有想象力。</p>

<h2 id="interesting-books">四、有趣的书：先让阅读变成一件想继续做的事</h2>
<p>第一类是有趣的书。对很多人来说，重新开始阅读最重要的不是深刻，而是好看。只要一本书能让人不断翻页，它就在帮你恢复阅读肌肉。</p>
<p>《挽救计划》适合作为科幻入口。很多关于外星文明的故事都写成黑暗森林式的猜疑、毁灭和战略对抗，而《挽救计划》在宇宙深处写出了罕见的友善。人类与外星生命从完全陌生到互相理解、互相调侃、互相救援，这种关系让冷冰冰的太空故事有了温度。它最好先读小说，再接触改编作品，因为想象力一旦被画面固定，阅读时的惊喜会被削掉一大块。</p>
<p>《万物简史》则把宇宙、地球、生命、人类和科学史写成一场轻松又宏大的脱口秀。它会提醒人：能活着本身就像中了宇宙彩票。原子没有散架，地球没有提前毁灭，恐龙刚好灭绝，祖先没有在无数灾难里断线。它既能讲宇宙大爆炸，也能讲科学家那些近乎疯狂的实验，让知识重新变得好玩。</p>
<p>《和狗狗的十二次哲学漫步》适合喜欢对话体的人。主人和狗狗的交流，把复杂哲学问题拉回日常场景。好的对话体会让读者像坐在老朋友旁边，一边聊天一边把心里的疑惑慢慢拆开。《被讨厌的勇气》《小强升职记》《不上班咖啡馆》也有类似的阅读体验：不端着讲道理，而是用故事把问题讲活。</p>

<h2 id="wealth-books">五、财富类书籍：不是教人暴富，而是读死贪念</h2>
<p>财富类书籍的第一作用，不是让人一夜暴富，而是让人知道什么东西不可能长期成立。市场上所有声称轻松高收益、稳定高年化、低风险暴利的东西，都要先被常识过滤。普通人能够主动触达的长期收益，本来就有上限；超过常识太多的承诺，往往不是机会，而是风险。</p>
<p>《简单致富》和《指数基金投资指南》可以作为两个市场的入门书。前者更适合理解美股长期指数化投资，后者更适合理解 A 股指数基金。它们共同强调一个朴素原则：先用简单方法拿到足够好的长期收益，再考虑是否有必要进一步学习和尝试。普通人一开始就追逐复杂策略，往往不是更专业，而是更容易被市场教育。</p>
<p>进阶之后，可以读段永平相关内容和《巴菲特致股东的信》。段永平最值得学习的，不只是投资结果，而是创业、商业、产品、组织和长期选择背后的方法论。他在高峰期能退出来，本身就说明其对目标和边界的理解很强。巴菲特的股东信则让人理解什么叫不被市场先生牵着走：真正看懂少数好公司，在极度低估时出手，在高估时保持清醒，中间认真生活。</p>
<p>芒格、格雷厄姆、费雪等人的作品也值得延伸阅读。它们最终不是为了让人每天盯盘，而是为了形成更稳定的判断：市场先生会发疯，但你不必陪他发疯。能看懂价值、耐心等待、控制贪婪和恐惧，才是财富书真正该教会人的东西。</p>

<h2 id="work-and-money">六、工作、自由与金钱心理</h2>
<p>如果想理解创业或工作方式，《每周工作四小时》值得一读。它不只是讲少工作，而是讲如何重新设计工作关系、地点自由、时间自由和收入结构。它提供的是一种反向视角：上班不是人生的终极目标，工作应当服务于更自由的生活，而不是把人永远固定在组织目标里。</p>
<p>稻盛和夫的《活法》《心法》《干法》代表另一种极致认真工作的路线。稻盛和夫创办两家世界五百强企业，也曾作为救火者重整企业，他对工作、勤奋、心性和经营的理解非常深。但国情和组织环境不同，日本式一生一社的工作观，并不一定适合所有人。更平衡的方式，是学习他对工作的认真和自我要求，同时用《每周工作四小时》对冲“把工作当成人生全部”的风险。</p>
<p>《金钱心理学》则适合反复读。它不是用复杂公式吓人，而是通过大量故事讲清楚财富独立、风险、运气、耐心、嫉妒和安全边际。很多财务问题不是数学问题，而是心理问题。一个人如果无法控制欲望、比较和恐惧，再好的策略也执行不了。</p>

<h2 id="practical-books">七、致用类书籍：减少情绪内耗和关系损耗</h2>
<p>致用类书不一定多，但价值很高。《被讨厌的勇气》和《幸福的勇气》是理解阿德勒心理学的好入口。核心概念之一是课题分离：把别人的事和自己的事分清楚。很多情绪内耗都来自越界，既替别人承担了不该承担的情绪，又把别人无法负责的评价塞进自己心里。</p>
<p>课题分离能帮助人减负，也能改善家庭和亲密关系。教育孩子时，它提醒父母不要把孩子当下属控制；人际交往中，它提醒人不要把所有人的评价都背在自己身上；亲密关系里，它提醒人不要用控制代替爱。</p>
<p>但任何方法论都有错误用法。伴侣难过时，如果只说“这是你的课题，与我无关”，那不是课题分离，而是缺乏同理心。课题分离不是冷漠，它只是帮助人弄清边界；边界清楚之后，仍然可以温柔地陪伴、倾听和支持。</p>
<p>阿德勒思想里还有一个很适合关系的概念：最佳分别。所有关系都以分别为前提，正因为时间有限，才更要努力让相遇变得值得。真正好的关系，不是害怕分别，而是为了某一天分别时能坦然说一句：和这个人一起走过的日子很好，很值得。</p>

<h2 id="fiction-humanities">八、小说与人文：扩展一生之外的生命经验</h2>
<p>小说与人文类书籍负责拓宽生命感。《四季奇谭》就是很好的例子。许多人熟悉《肖申克的救赎》，但它只是《四季奇谭》中的一个故事。剩下的故事同样有力量，尤其能展示人在黑暗、恐惧、束缚和重生里的挣扎。</p>
<p>好的小说不只是情节刺激，而是让人看到人性的阴影和韧性。人在现实里不可能经历所有命运，但可以通过小说提前感受许多人生。读完之后，世界会显得更宽，人也更不容易把自己的处境理解成唯一的绝境。</p>
<p>《昨日的世界》是茨威格写给欧洲旧世界的告别。它不是狭窄的个人传记，而是一个热爱生活的人对两次世界大战前后欧洲巨变的回忆。十九世纪末的欧洲曾充满进步、繁荣和奇迹，电灯、电话、汽车和现代城市系统让人相信文明会一路向上。战争到来后，秩序崩塌，身份、家园和安全感都被撕碎。</p>
<p>茨威格晚年的悲剧，来自一种深层失根感：一个有才华、有洞察力、热爱文明的人，突然发现自己的命运不再掌握在自己手中。《昨日的世界》后劲很大，因为它提醒人，时代并不总按个人愿望推进；越是和平安稳时，越要珍惜生活的根。</p>

<h2 id="reading-tools">九、阅读工具：让读书变得更容易发生</h2>
<p>阅读习惯能否持续，环境很重要。工具不是核心，但好工具能降低阻力。阅读支架、舒服的椅子、合适的灯光、电纸书设备，都会决定人是否愿意坐下来读更久。</p>
<p>阅读支架的关键是稳定、轻便、翻页顺手。尺寸不必贪大，小号支架反而更灵活，大书也能勉强承载。单人沙发则是长期阅读的舒适区，重点不是品牌崇拜，而是能否让身体稳定放松，不用十分钟就腰酸背痛。</p>
<p>电纸书设备选择要先看场景。10.3 英寸大屏适合读 PDF、做批注、看专业书；小尺寸 Kindle 更适合随身携带和纯文字阅读；开放系统设备适合微信读书、多平台阅读和文件管理；手机形态墨水屏适合通勤、碎片阅读和临时查阅。</p>
<p>如果追求极致显示，大屏黑白墨水屏仍然比彩墨更适合严肃阅读。彩墨大屏的问题是底色偏黑，看书的舒适度不如想象。Kindle 的优势在显示和背光调教，但系统封闭，需要适应传书和找书流程。文石的优势在开放系统、芯片速度和软件完整度，但背光观感不一定适合所有人。汉王的大屏显示有优势，但部分型号缺背光，会限制夜间场景。墨水屏手机则仍是小众市场，系统、刷新率、芯片和稳定性很难同时完美。</p>
<p>结论很现实：没有一台设备能满足所有需求。读 PDF、纯文字、微信读书、通勤、夜读、批注、手机形态，各自对应不同取舍。与其追求完美设备，不如先确认自己的最高频场景，再买最适配的一台。</p>


<h2 id="reading-system">十一、把书读进去：从输入到行动的闭环</h2>
<p>读书真正生效，需要从“读过”变成“进入生活”。最简单的闭环有四步：先用目录判断这本书解决什么问题，再在阅读时标出真正刺中自己的段落，读完后用自己的话写一段摘要，最后挑一个方法在现实里试用。只要完成这四步，一本书就不再只是信息，而会变成行动材料。</p>
<p>不要把笔记做成搬运。逐字摘录很容易让人产生努力错觉，真正有价值的是转译：这句话和我现在的问题有什么关系？它能解释我过去哪一次失败？它能帮我做哪个选择？如果明天就要用，我会怎么用？这些问题会迫使大脑把书里的知识和自己的生活连接起来。</p>
<p>也可以给书建立三种标签。第一种是模型标签，比如复利、边界、风险、激励、自由、情绪；第二种是场景标签，比如工作、投资、亲密关系、家庭、健康；第三种是行动标签，比如要尝试、要避开、要复盘。标签不是为了整理得漂亮，而是为了以后遇到现实问题时，能迅速调出对应思想。</p>
<p>阅读还有一个重要原则：不要急着追求“我读了多少本”，而要追问“哪些书改变了我的判断”。一年读三十本但没有改变任何选择，效果不如一年读五本却真的改掉一个坏习惯、避开一次风险、形成一个新能力。读书的单位不该只是本数，也应该是被改变的决策。</p>

<h2 id="ai-era-reading">十二、AI 时代更需要人自己读书</h2>
<p>AI 可以总结一本书的大意，也可以帮人整理知识卡片，但它替代不了个人阅读时发生的内在摩擦。真正改变人的，常常不是某条摘要，而是阅读过程中那种被一句话击中、被一个人物震动、被一个逻辑反复说服的体验。没有这个过程，知识很容易停在表面。</p>
<p>AI 更像阅读助理，而不是替身。它可以帮你解释陌生概念、列出延伸书目、对比不同观点、生成复习问题，也可以帮你把读书笔记重新组织成行动清单。但最终要不要相信、怎么取舍、放进哪段人生经验里，仍然要由自己的大脑完成。</p>
<p>越是工具强大，越要有更好的判断力。一个没有阅读积累的人，面对 AI 给出的答案很难判断优劣；一个长期阅读的人，反而能把 AI 当作放大器，用更高质量的问题换来更高质量的辅助。阅读让人拥有内在标尺，而内在标尺会决定工具到底是帮你变强，还是帮你更快变懒。</p>


<h2 id="reading-rhythm">十三、给自己设计一条可持续的阅读节奏</h2>
<p>真正能坚持的阅读计划，必须低摩擦。每天固定一个最小阅读量，比如十页或二十分钟；把书放在床头、书桌、包里和电纸书首页；在最容易刷手机的时间段，提前准备一本不太费力但足够吸引人的书。环境先替意志力做一部分工作，习惯才不会完全靠硬扛。</p>
<p>还可以把阅读分成三档：轻阅读负责恢复兴趣，中等难度负责扩展知识，硬书负责建立壁垒。状态差时读轻阅读，不必自责；状态好时啃硬书，也不必炫耀。阅读是一条长路，最重要的是不断回到书前，而不是每一天都像考试一样证明自己。</p>
<p>一年下来，只要有几本书真正进入了你的语言、判断和生活方式，这一年就没有白读。</p>
<p>读书不是和别人比速度，而是不断让自己变得更清醒、更稳、更有选择权。只要这件事发生了，阅读就已经开始回报你，也会在未来某个关键选择里继续保护你，让你少走许多本可避免的弯路。每一本真正读进去的书，都会在某个时刻变成判断力的一部分，长期看非常珍贵。</p>

<h2 id="how-to-read">十、真正重要的是让阅读回到生活里</h2>
<p>书单和设备最终都只是入口。最重要的是让阅读成为生活的一部分，而不是一年一次的仪式。每天读十页，长期看比偶尔猛读一本更可靠；读完之后写几句笔记，比只追求读完数量更有用；把书里的一个方法用到生活里，比存下一百条金句更能改变人生。</p>
<p>阅读不必完美。可以同时读几本，可以中途放弃不合适的书，可以先从有趣的书开始，也可以在不同阶段回到同一本书。很多好书不是读一次就结束，而是在不同年龄反复读，每一次都像打开另一层。</p>
<p>读书的最终目标，不是成为书架很满的人，而是成为脑子更清楚、心更稳、选择更好、生活更自由的人。它的功利收益会体现为收入、判断、品味和决策；它的非功利收益会体现为平和、韧性、共鸣和精神空间。</p>
<p>阅读是一种缓慢但猛烈的改变。前期像微光，后期像复利。只要持续把好书、好问题和好经验放进大脑，一个人的人生曲线就会被悄悄改写。</p>
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
        "BV1",
        "关注",
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
        "智力复利",
        "阅读",
        "贫穷的本质",
        "挽救计划",
        "万物简史",
        "简单致富",
        "指数基金投资指南",
        "巴菲特致股东的信",
        "被讨厌的勇气",
        "四季奇谭",
        "昨日的世界",
        "电纸书",
        "墨水屏",
    ]
    for word in required_terms:
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


base.ROOT = Path("/tmp/bv1ka-bv169-sparse.Nkhbld")
base.DATE = "2026-08-01"
base.BASE_DT = datetime(2026, 8, 1, 12, 45, tzinfo=timezone(timedelta(hours=8)))
base.PREV_EXISTING_URL = "/2026/attraction-love-logic-self-improvement-healthy-relationship/"
base.PREV_EXISTING_TITLE = "吸引力的底层逻辑：恋爱不是追出来的，而是经营出来的"
base.SCRIPT_NAME = "publish-reading-compound-interest-booklist-eink-guide-20260801.py"
base.MANIFEST_NAME = "publish-reading-compound-interest-booklist-eink-guide-20260801-changed-files.json"
base.CHANGED = set()
base.INPUT_ORDER = [
    base.Post(
        source_id="public-audio-bv18woabjecg-20260801",
        slug="reading-compound-interest-booklist-eink-guide",
        title="读书像一场无痛换脑：阅读复利、书单与电纸书选择",
        desc="阅读真正改变人的地方，不只是知道更多，而是通过智力复利、生命韧性、财富常识、关系方法和工具环境，把人生曲线慢慢向上抬。",
        category="读书笔记",
        series="阅读方法",
        tags=["阅读", "智力复利", "世界读书日", "书单", "电纸书", "墨水屏", "指数基金", "阿德勒", "小说", "财富管理"],
        minutes=16,
        body=BODY,
        cover_kicker="世界读书日",
        cover_line="阅读复利 · 书单 · 电纸书选择",
        cover_theme=("#111827", "#7c3aed", "#22c55e"),
        duration=966.089438,
        segments=664,
        chars=5787,
    )
]
base.PUBLISH_ORDER = list(base.INPUT_ORDER)
base.validate = validate
base.copy_script_and_manifest = copy_script_and_manifest


if __name__ == "__main__":
    shutil.rmtree(Path(__file__).with_name("__pycache__"), ignore_errors=True)
    base.main()
    shutil.rmtree(Path(__file__).with_name("__pycache__"), ignore_errors=True)
