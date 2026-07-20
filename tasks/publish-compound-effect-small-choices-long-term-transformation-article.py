from __future__ import annotations

import html
import importlib.util
import json
import shutil
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
BASE_PATH = HERE / "publish-modern-single-men-happiness-article.py"
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
SPEC = importlib.util.spec_from_file_location("single_post_publisher", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load publisher template: {BASE_PATH}")
base = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(base)


base.SLUG = "compound-effect-small-choices-long-term-transformation"
base.URL = f"/2026/{base.SLUG}/"
base.ASSET_DIR = f"/images/posts/{base.SLUG}"
base.TITLE = "复利效应：别高估一年的改变，别低估五年的复利"
base.DESCRIPTION = "真正拉开人生差距的不是一次惊天逆转，而是微小选择、稳定行动与时间共同形成的复利。看懂正向与负向复利，建立可以持续五年的成长系统。"
base.DATE = "2026-07-20"
base.PUB_DATE = "Mon, 20 Jul 2026 23:50:00 +0800"
base.LAST_BUILD = "2026-07-20T23:50:00+08:00"
base.CATEGORY = "个人成长"
base.SERIES = "人生主线"
base.TAGS = ["复利效应", "长期主义", "习惯", "选择", "延迟满足", "自我成长", "复盘", "时间管理", "环境选择", "行动力"]
base.OLDER_URL = "/2026/physical-ai-investment-map-autonomous-driving-robotics-industrial-software/"
base.OLDER_TITLE = "物理 AI 投资图谱：智能驾驶、人形机器人与工业软件"
base.SCRIPT_NAME = "publish-compound-effect-small-choices-long-term-transformation-article.py"
base.MANIFEST_NAME = "publish-compound-effect-small-choices-long-term-transformation-changed-files.json"


base.SECTIONS = [
    (
        "life-operating-system",
        "复利不是财富技巧，而是人生的底层运行系统",
        [
            "人们谈到复利，通常想到的是利滚利、存款利息或指数收益。但复利真正支配的远不只是金钱。身材、收入、能力、人际关系、认知层次乃至最终的人生状态，都在服从同一套规律：微小选择经过持续行动，再被时间放大，最终形成看似突然、实则早已注定的结果。",
            "没有真正突如其来的成功，也没有真正突如其来的失败。今天的状态很少由昨天的一次偷懒决定，也很少由上个月的一次努力造就。它通常来自过去三年、五年甚至十年里，无数普通日子中的选择叠加。别人看似突然迎来突破，也往往只是长期坚持的结果终于越过临界点。",
            "复利可以写成一个朴素的关系式：微小而明智的选择，乘以持续一致的行动，再乘以足够长的时间，才会形成根本性的差异。三项缺一不可。只有正确选择而不行动，结果不会改变；偶尔行动而不能持续，积累会反复归零；持续时间不够，又只能停留在几乎看不见变化的前半程。",
            "普通人的困境往往不是不知道什么是对的，而是轻视微小的力量、迷恋巨大的改变。期待一年逆天改命，却不愿每天读十分钟、运动二十分钟、复盘一次；渴望抓住一次风口，却放任每一天被拖延和即时满足切碎。真正拉开差距的，恰恰是这些不起眼的小事。",
        ],
    ),
    (
        "exponential-cases",
        "两个指数增长案例：前半程越安静，后半程越惊人",
        [
            "国际象棋棋盘上的米粒，是理解复利最直观的入口。第一个格子放一粒米，第二个放两粒，第三个放四粒，之后每格翻倍。前十格加起来只有一千余粒，前二十格也仍然容易被低估；到了第三十一格，单格数量已经超过十亿粒。填满六十四格时，总量大到任何现实粮仓都无法兑现。",
            "人生与这张棋盘极其相似。每一天是一个格子，每一次选择是一粒米。阅读半个月、运动一个月、深耕技能两个月，通常不会带来肉眼可见的变化。由于没有反馈，人很容易把静默误判为无效，在最需要继续积累的时候放弃。可指数曲线的本质，就是前半段几乎贴着地面，真正的陡峭增长全部发生在后半段。",
            "另一道选择题同样揭示了即时收益的诱惑：立即拿走三百万美元，或者拿走一美分，并让它连续三十一天每天翻倍。直觉会把一美分视为荒谬的小数目，但它在第三十一天会超过一千万美元，远远超过眼前的三百万。差距不来自起点，而来自增长方式与等待时间。",
            "普通人更容易看见立刻到手的回报，高手更愿意等待复利越过临界点。刷碎片内容、熬夜、拖延，当下立刻舒服，代价却被推迟；阅读、训练、学习、复盘，当下需要付出，回报同样被推迟。即时反馈总在诱惑人选择安逸，而长期结果往往奖励那些能够穿过静默期的人。",
        ],
    ),
    (
        "three-groups",
        "三组人的三年分化：人生差距是怎样被一点点拉开的",
        [
            "设想三组起点相近的普通人。第一组维持原状，不刻意进步，也不刻意放纵；第二组每天增加一点点负面行为，例如多喝一杯含糖饮料、多消耗半小时在无意义娱乐上、每周少运动一次，偶尔晚睡或敷衍工作；第三组每天只增加一点点正向行为，例如少摄入约一百二十五卡路里、多走两千步、读几页书，再花十分钟复盘当天。",
            "最初六个月，三组人的体重、精神、工作和生活质量几乎没有差别。这正是复利最容易欺骗人之处：好的选择没有立即奖赏，坏的选择也没有立即惩罚。短期结果看似相同，于是第二组觉得放纵没有代价，第三组则开始怀疑坚持是否值得。",
            "一年半以后，差距才悄然出现。持续负面行为的人开始轻微发胖、精神萎靡、注意力下降，工作也更容易敷衍；持续正面行为的人身材更紧致、精力更充沛、效率更高，能力和职位逐渐改善。变化仍不算轰动，却已经朝着相反方向加速。",
            "三年以后，差距会大到难以忽视。负向习惯可能带来三十斤以上的体重增长、睡眠和代谢问题、能力停滞、收入停滞与人际关系恶化；正向习惯则让健康、认知、工作效率、核心竞争力、收入和社交圈层共同改善。没有哪一天发生了戏剧性转折，但每一天都在为最终结果投票。",
            "这组对照揭示了最重要的原则：复利不以强度为核心，而以一致性为核心。一天学习十小时、随后停十天，不如每天稳定学习半小时；一次拼命运动，随后长期躺平，也不如每天完成一小段训练。稳定的节奏，永远比一时的爆发更有力量。",
        ],
    ),
    (
        "choice-law",
        "法则一：选择就是命运的源代码",
        [
            "任何结果向前追溯，都能找到一连串选择。选择产生行为，行为重复为习惯，习惯经过时间形成结果。命运并不是某一天突然降临，而是由大量看似无关紧要的决定逐行写成。",
            "每天熬夜刷手机，不只是选择了今晚晚睡，也是在选择更差的精力、健康和效率；每天早睡、适度运动，则是在选择更稳定的身体与生活。长期敷衍工作，就是选择能力停滞和收入平庸；持续深耕技能、复盘改进，就是选择竞争力、认知与收入逐步上升。",
            "所有选择在当下都可能没有明显结果，但时间会放大它们。坏选择形成负向复利，让状态越来越差，修复成本越来越高；好选择形成正向复利，让能力彼此增强，机会越来越多。一次随性决定不会立刻改变人生，却会给未来铺一小段路，日积月累后，要么成为坦途，要么成为荆棘。",
            "掌握选择法则的第一步，是停止轻视日常。默认、拖延和随波逐流本身也是选择。真正有效的问题不是“我想得到什么”，而是“今天哪一个具体选择，会让未来的自己更接近那个结果”。",
        ],
    ),
    (
        "habit-law",
        "法则二：习惯让正确的小事自动循环",
        [
            "仅靠激情和意志力，很难支撑长期复利。激情会退去，意志力会耗尽，任何需要每天咬牙完成的事，最终都容易输给惰性。更可靠的方法，是把正确的小事变成不需要反复决策的习惯。",
            "习惯是复利的载体。睡前固定阅读几页，像刷牙洗脸一样自然，就不必每天重新说服自己；每天完成一次微小训练、记录一次支出、复盘一个问题，重复三百多天后形成的积累，远大于偶尔一次雄心勃勃的冲刺。",
            "坏习惯遵循同样的机制。熬夜、拖延、无意识刷手机，最初只是一次选择；重复之后变成默认动作，最后反过来控制精力、情绪和人生节奏。负向复利最危险的地方，正是它在习惯化之后几乎不再需要主动选择。",
            "改变不必从彻底重塑自己开始。先删掉三个最消耗你的微小坏习惯，再建立三个最滋养你的微小好习惯。让行为足够小、触发条件足够明确、执行阻力足够低，直到它成为日常常态。只要习惯能够持续，时间就会自动替你放大结果。",
        ],
    ),
    (
        "responsibility-law",
        "法则三：百分之百为自己的人生负责",
        [
            "复利生效有一个经常被忽略的前提：停止向外归因，百分之百承担自己能够承担的责任。收入不理想时怪环境和行业，生活平庸时怪出身和运气，事情失败时怪别人、意外和条件，短期会让情绪轻松一些，却也同时交出了改变的主动权。",
            "外部条件当然真实存在，人与人的起点也并不相同。但只要一个人把全部注意力放在不可控因素上，就不会认真调整自己的选择、行为和习惯。责任的意义，不是否认现实，而是把精力重新放回可控范围：今天可以改什么，明天可以多做哪一步，下一次如何避免重复。",
            "只要仍在抱怨和找借口，行为就很难改变，正向复利也无法启动。当一个人愿意承认当前的迷茫、停滞和失败中，有一部分来自自己的选择，他才真正获得修正选择、替换习惯和重新积累的可能。",
            "一边渴望人生巨变，一边拒绝为选择负责，是最隐蔽的自我欺骗。责任不是额外负担，而是重获控制权的入场券。只有承认自己是选择的主体，才能成为结果的建设者。",
        ],
    ),
    (
        "environment-law",
        "法则四：环境决定复利的方向与速度",
        [
            "人不仅被自己的行为塑造，也被每天接触的人、氛围和信息持续塑造。环境的影响往往没有单次冲击，而是潜移默化地改变判断标准、情绪水平、习惯与选择，再通过复利把微小影响放大。",
            "如果周围充满抱怨、消极、躺平和敷衍，负面情绪与低标准会不断侵蚀行动。即使原本自律上进，也可能在日复一日的同化中降低要求，正向积累被抵消。很多人的问题并非完全不努力，而是长期被一个持续消耗自己的环境拖住。",
            "相反，当身边的人都在学习、精进、做事和提升自己，成长会成为默认氛围。哪怕最初惰性很强，也会被更高的标准和节奏带动。个人努力仍然重要，但一个支持正确行为的环境，可以让复利速度显著提升。",
            "优化环境包括三件事：筛选长期相处的圈层，减少消耗性的关系；管理信息入口，远离无意义的情绪和噪声；主动靠近能够提供高标准、真实反馈和正向行动的人。靠意志力硬扛常常逆着人性，设计环境则让正确行为顺着人性发生。",
        ],
    ),
    (
        "failure-traps",
        "三大致命陷阱：为什么很多努力始终没有复利",
        [
            "第一种陷阱是“微波炉思维”，也就是极度渴望即时回报。今天付出，明天就想看到结果；本月努力，下月就要求兑现。一旦短期没有反馈，便立即放弃、摆烂或否定自己。可复利天然先慢后快、先静默后爆发，读书不会立刻增加收入，运动不会立刻改变身材，复盘不会立刻带来升职，但它们会持续推动你接近临界点。",
            "第二种陷阱是忽视负向复利。偶尔熬夜、偶尔拖延、偶尔敷衍，看起来都“没关系”，但无数个没关系会累积成状态下滑。一次偷懒看不出问题，反复偷懒会瓦解节奏与自我信任。人生的下滑通常并非源于一次重大失误，而是来自大量微小恶习长期叠加。先切断持续流血的负向行为，往往比盲目增加新习惯更重要。",
            "第三种陷阱是三分钟热度。间歇性努力、持续性摆烂，无法形成任何复利。一天学习十二小时后休息十天，不如每天稳定学习一小时；一周疯狂运动五次后停一个月，不如每天运动二十分钟。复利只认持续，不认一时强度。",
            "三个陷阱背后其实是同一个问题：把成长当成一次事件，而不是一套系统。事件依赖情绪，系统依赖节奏；事件追求立刻证明，系统接受长期沉默；事件在热情消失后停止，系统让最小行动在普通日子里继续发生。",
        ],
    ),
    (
        "four-steps",
        "四步落地：建立能够持续五年的复利系统",
        [
            "第一步，每日只做微小增量，不追求一次巨变。放下“彻底改变自己”的宏大幻想，把目标缩小为今天比昨天多读一页、多运动十分钟、少消耗十分钟、多复盘一个问题。每天进步百分之一的重点不是数学神话，而是让行为小到可以长期重复。只做增量，不让过高强度摧毁持续性。",
            "第二步，记录并量化行为。无法测量的东西很难优化。每天花十分钟回答几个问题：今天做对了什么，做错了什么，时间浪费在哪里，获得了什么成长，明天最需要优化哪一件事。记录让模糊感受变成可观察数据，也让选择、反馈和调整形成正向循环。",
            "第三步，锁定正向环境，切断负向消耗。清理持续消耗注意力的人际关系、无意义社交、娱乐与八卦；主动接触上进、深耕、自律的人和优质信息。短期独处并不可怕，它常常是从旧环境脱离、重建生活秩序的必要阶段。让环境推动成长，比每天与环境对抗更轻松、更持久。",
            "第四步，长期坚守，熬过复利的静默期。前三个月、半年甚至一年，可能没有掌声、回报和明显结果，旁人不理解，自己也会怀疑。此时真正需要坚持的，不是高强度，而是最低限度的稳定输出。不是看到希望才坚持，而是坚持到足够久，才有机会看见希望。",
            "一套可执行的日常模板可以非常简单：固定一个最小成长动作，记录是否完成；每天做十分钟复盘；每周检查一次信息与社交环境；每月只调整一个关键习惯；用三年到五年的尺度观察方向，不用三天到五周的情绪评价人生。系统越简单，越容易存活；存活越久，复利越强。",
        ],
    ),
    (
        "conclusion",
        "真正的逆袭从来不是一鸣惊人，而是日积月累",
        [
            "人生没有可以替代积累的捷径。所谓奇迹，不过是微小正确行为长期累积后，终于以集中方式显现。天赋、运气、机遇和出身并非都能掌控，但每天的选择、习惯与最低限度的坚持，始终有一部分掌握在自己手中。",
            "短期看，一次阅读、一次训练、一次复盘都毫无波澜；长期看，它们会共同改变身体、认知、能力、收入和关系。反过来，一次放纵似乎无伤大雅，长期重复却会把人带到完全不同的位置。时间从不负责判断方向，它只负责放大你持续投入的东西。",
            "不要高估一年里能够完成的戏剧性改变，也不要低估五年稳定积累的复利。戒掉浮躁，停止追逐立刻证明自己的冲动，把每一个平凡日子都变成一笔小额但方向正确的投入。终有一天，那些无人注意的选择会越过临界点，让你在时间里遇见一个脱胎换骨的自己。",
        ],
    ),
]


def body_html() -> str:
    chunks = [f'<p><img src="{base.ASSET_DIR}/cover.svg" alt="{html.escape(base.TITLE, quote=True)}"></p>']
    intro = [
        "人生最大的误判之一，是把成功想象成一次惊天动地的逆袭，把改变寄托在一个千载难逢的风口。于是，人们不断寻找更大的目标、更猛的方法和更快的反馈，却看不起那些微不足道、日复一日的小事。",
        "真正决定人生方向的，往往不是某个戏剧性的瞬间，而是每一个普通日子里的选择。一次偷懒、一次放纵、一次阅读、一次训练，都小到不会立即改变结果；但当同类选择持续叠加，时间会把微小差异放大成完全不同的人生。",
        "《复利效应》的价值，就在于把复利从理财概念扩展成一套生活、工作、财富、健康、人际关系与自我成长的运行系统。它不承诺速成，也不提供捷径，只揭示一个朴素而严格的规律：小选择加上持续行动，再交给时间，最终会产生远超直觉的结果。",
    ]
    chunks.extend(f"<p>{html.escape(paragraph)}</p>" for paragraph in intro)
    for anchor, heading, paragraphs in base.SECTIONS:
        chunks.append(f'<h2 id="{anchor}">{html.escape(heading)}</h2>')
        chunks.extend(f"<p>{html.escape(paragraph)}</p>" for paragraph in paragraphs)
    return "\n".join(chunks)


def cover_svg() -> str:
    title = html.escape(base.TITLE)
    desc = html.escape(base.DESCRIPTION)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630" role="img" aria-labelledby="title desc">
  <title id="title">{title}</title>
  <desc id="desc">{desc}</desc>
  <rect width="1200" height="630" fill="#f8fafc"/>
  <rect x="54" y="52" width="1092" height="526" rx="8" fill="#17202a"/>
  <line x1="112" y1="500" x2="1088" y2="500" stroke="#64748b" stroke-width="2"/>
  <line x1="112" y1="500" x2="112" y2="124" stroke="#64748b" stroke-width="2"/>
  <path d="M112 494 C330 490 514 482 656 452 C798 422 920 346 1088 146" fill="none" stroke="#22c55e" stroke-width="8" stroke-linecap="round"/>
  <path d="M112 490 C338 486 570 478 810 472 C916 470 1000 468 1088 466" fill="none" stroke="#f59e0b" stroke-width="5" stroke-linecap="round" stroke-dasharray="12 12"/>
  <g fill="#22c55e">
    <circle cx="282" cy="488" r="7"/><circle cx="508" cy="474" r="7"/><circle cx="704" cy="438" r="7"/><circle cx="890" cy="362" r="7"/><circle cx="1088" cy="146" r="9"/>
  </g>
  <rect x="112" y="84" width="306" height="40" rx="4" fill="#f8fafc"/>
  <text x="130" y="112" fill="#17202a" font-family="Noto Sans SC, PingFang SC, Arial, sans-serif" font-size="22" font-weight="700">THE COMPOUND EFFECT</text>
  <text x="112" y="190" fill="#ffffff" font-family="Noto Sans SC, PingFang SC, Arial, sans-serif" font-size="54" font-weight="800">别高估一年的改变</text>
  <text x="112" y="258" fill="#bbf7d0" font-family="Noto Sans SC, PingFang SC, Arial, sans-serif" font-size="48" font-weight="800">别低估五年的复利</text>
  <text x="112" y="316" fill="#cbd5e1" font-family="Noto Sans SC, PingFang SC, Arial, sans-serif" font-size="25">微小选择 × 持续行动 × 时间 = 人生质变</text>
  <g font-family="Noto Sans SC, PingFang SC, Arial, sans-serif" font-size="21" font-weight="600">
    <rect x="112" y="354" width="118" height="44" rx="4" fill="#263341" stroke="#38bdf8"/><text x="148" y="383" fill="#bae6fd">选择</text>
    <rect x="248" y="354" width="118" height="44" rx="4" fill="#263341" stroke="#22c55e"/><text x="284" y="383" fill="#bbf7d0">习惯</text>
    <rect x="384" y="354" width="118" height="44" rx="4" fill="#263341" stroke="#f59e0b"/><text x="420" y="383" fill="#fde68a">责任</text>
    <rect x="520" y="354" width="118" height="44" rx="4" fill="#263341" stroke="#a78bfa"/><text x="556" y="383" fill="#ddd6fe">环境</text>
  </g>
  <text x="846" y="540" fill="#94a3b8" font-family="Noto Sans SC, PingFang SC, Arial, sans-serif" font-size="20">短期平缓 · 长期陡峭</text>
</svg>
'''


base.body_html = body_html
base.cover_svg = cover_svg


def skip_template_artifact_copy() -> None:
    return None


base.copy_script_and_manifest = skip_template_artifact_copy


def changed_files() -> list[str]:
    paths = [
        f"2026/{base.SLUG}/index.html",
        base.OLDER_URL.strip("/") + "/index.html",
        "archive/index.html",
        "categories/index.html",
        f"categories/{base.CATEGORY}/index.html",
        f"images/posts/{base.SLUG}/cover.svg",
        "index.html",
        "index.xml",
        "series/index.html",
        f"series/{base.SERIES}/index.html",
        "tags/index.html",
        "tasks/pinned_home.py",
        f"tasks/{base.SCRIPT_NAME}",
        f"tasks/{base.MANIFEST_NAME}",
    ]
    paths.extend(f"tags/{tag}/index.html" for tag in base.TAGS)
    return sorted(dict.fromkeys(paths))


base.changed_files = changed_files


def main() -> None:
    base.main()
    task_root = base.ROOT / "tasks"
    pinned_source = HERE / "pinned_home.py"
    pinned_target = task_root / "pinned_home.py"
    if pinned_source.resolve() != pinned_target.resolve():
        shutil.copyfile(pinned_source, pinned_target)
    published_script = task_root / base.SCRIPT_NAME
    if Path(__file__).resolve() != published_script.resolve():
        shutil.copyfile(Path(__file__), published_script)
    (base.ROOT / "tasks" / base.MANIFEST_NAME).write_text(
        json.dumps(base.changed_files(), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Published {base.URL}")


if __name__ == "__main__":
    main()
