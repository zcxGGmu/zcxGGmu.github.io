from __future__ import annotations

import base64
import importlib.util
import json
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
BASE_SCRIPT = TASKS / "publish-three-life-business-articles-20260809.py"

spec = importlib.util.spec_from_file_location("publish_base", BASE_SCRIPT)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = base
spec.loader.exec_module(base)

_base_run_gh = base.run_gh


def run_gh_with_stream_retry(args: list[str], payload: dict | None = None):
    for attempt in range(5):
        try:
            return _base_run_gh(args, payload)
        except RuntimeError as exc:
            msg = str(exc).lower()
            if attempt < 4 and any(token in msg for token in ["stream error", "cancel", "connection", "reset", "timeout", "temporarily"]):
                time.sleep(2 + attempt * 3)
                continue
            raise


base.run_gh = run_gh_with_stream_retry

base.__file__ = __file__
base.DATE = "2026-08-14"
base.BASE_DT = datetime(2026, 8, 14, 10, 20, 0, tzinfo=timezone(timedelta(hours=8)))
base.PREV_EXISTING_URL = "/2026/ai-skills-agent-fullstack-open-source-daily-20260813/"
base.PREV_EXISTING_TITLE = "8月13日 AI Skills/Agent 全栈开源项目速览：把热度变成可治理的工作系统"
base.SCRIPT_NAME = Path(__file__).name
base.MANIFEST_NAME = "publish-goldman-pcb-ccl-ai-server-20260814-changed-files.json"


BODY = r'''
<p>AI 硬件链条的共识常常集中在 GPU、HBM、光模块和液冷上，但服务器内部还有一条被低估的价值链正在快速放大：PCB 和 CCL。高盛全球科技硬件团队给出的核心判断很直接：AI 服务器不是只带来更多出货量，也在把单机规格、材料等级和单位价值同时推高。量和价一起变化，才是 PCB/CCL 市场进入指数级扩张阶段的根本原因。</p>
<p>到 2028 年，AI 服务器相关 PCB 与 CCL 的市场规模预计分别达到约 840 亿美元和 481 亿美元，两年复合增速分别高达 148% 和 161%。这不是一个传统电子材料小幅提价的故事，而是 AI 服务器架构升级、背板复杂度提升、高速信号损耗约束、散热压力和高层数需求共同推动的产业重估。</p>

<h2 id="ai-server-demand">一、AI 服务器的量价同时放大</h2>
<p>先看量。2027 年和 2028 年，英伟达 AI 服务器机架预测被上调至约 9.2 万台和 14.8 万台。AI 服务器出货量在 2026 至 2028 年预计分别达到 190 万台、240 万台和 260 万台。服务器数量增长本身已经足够可观，但对 PCB/CCL 来说，更关键的是每台服务器内部需要更大面积、更高层数、更复杂的板材结构。</p>
<p>PCB 出货面积预计从 2026 年的约 130 万平方米增至 2028 年的约 450 万平方米，两年复合增速约 85%。CCL 出货张数则预计从约 4200 万张增至 1.31 亿张，两年复合增速约 77%。这说明需求扩张不是单点事件，而是从整机、机架、背板、板材到覆铜板逐层向上传导。</p>
<p>再看价。AI 服务器对 PCB 和 CCL 的要求明显高于传统服务器：信号损耗要更低，散热要更好，层数要更高，材料稳定性和加工难度也更强。单台服务器中 PCB 每平方米均价预计从 2025 年的约 5833 美元提升到 2028 年的约 18549 美元；CCL 每张均价预计从 93 美元提升到 362 美元。</p>
<p>这组数字解释了为什么市场规模的弹性远高于单纯出货量。AI 服务器不是把旧服务器多卖几台，而是在改变板材规格和价格结构。规格升级带来的单位价值提升，才是产业链利润弹性的关键。</p>

<h2 id="tam-upgrade">二、TAM 上调来自 Rubin Ultra 和新平台架构</h2>
<p>高盛这次上调幅度相当激进：2027 年 AI PCB TAM 被上调 38%，AI CCL TAM 被上调 18%。背后的关键变量是 Rubin Ultra 架构全面升级，以及 NVL144、NVL576 等新平台对背板、HDI、高层数多层板和高端 CCL 的需求超出此前预期。</p>
<p>AI 集群对 GPU、加速器、交换芯片、存储和电源管理之间的高速互联提出更高要求。高速信号在板内传输时，材料介电性能、铜箔粗糙度、线路精度、层间结构和散热能力都会影响最终性能。越往新架构演进，PCB 和 CCL 越不只是配套件，而是决定系统能否稳定跑满性能的基础材料。</p>
<p>规格升级路径很清晰：6 阶以上 HDI PCB 在 HDI 总 TAM 中的占比，预计将从目前约 35% 提升至 2028 年约 66%；M9 级以上 CCL 的占比预计从约 41% 提升至约 58%。这意味着市场增长会向高端产品集中，而不是所有厂商平均受益。</p>
<p>对投资判断来说，这一点非常重要。若只看 PCB 或 CCL 的总需求，容易低估结构分化；真正的利润来源在高频高速、高层数、高可靠性、材料认证和大客户导入能力上。能进入新平台供应链并稳定量产的公司，才拥有更强的业绩弹性。</p>

<h2 id="material-path">三、背板材料路线争议不改变大方向</h2>
<p>市场对 NVL144、Rubin Ultra 背板材料路径存在争议，核心在于未来到底采用 M9、PTFE 还是 M8 等方案。高盛做了情景分析，结论是不同材料路径对 2028 年 GPU PCB/CCL 总 TAM 的影响约 6 亿美元；相对约 425 亿美元的总盘子，这个差异并不构成方向性改变。</p>
<p>也就是说，材料路线会影响个别厂商、具体产品组合和短期订单节奏，但不会改变 AI 驱动 PCB/CCL 升级的主趋势。AI 服务器对高速信号、低损耗、散热和层数的要求已经确定，背板材料怎么选，更多是在高端需求内部重新分配，而不是让需求消失。</p>
<p>这也提醒市场，不必把投资判断过度压在单一技术路线之上。真正应当评估的是厂商能否覆盖多种材料体系，是否具备客户联合开发能力，是否能在验证阶段提供稳定样品，是否有足够产能承接平台放量。</p>
<p>高端材料的验证周期通常较长，原因在于它不是只看实验室参数。客户需要确认高速信号完整性、热稳定性、长期可靠性、压合良率和大批量一致性。一个材料方案即使指标先进，如果无法在大规模生产中维持稳定，也很难进入主平台。因此，供应商越早参与架构开发，越容易在新一代平台中形成先发优势。</p>

<h2 id="upstream-materials">四、上游材料：三井金属与日东纺的隐形壁垒</h2>
<p>上游材料端，三井金属是真正意义上的隐形冠军。其 VSP 系列超低粗糙度双面光滑铜箔，在 HVLP4 级以上超高端电解铜箔市场拥有约 80% 的全球份额。对高速电子设备来说，电解铜箔就像信号传输的高速公路：表面越光滑、纯度越高，信号传输速度越快，功耗和损耗越低。</p>
<p>三井金属的竞争优势不只在单个材料指标，还在于与主流 CCL 厂商从开发初期就深度绑定。高端 CCL 不是简单采购铜箔再压合，材料之间的匹配、工艺窗口和长期可靠性都需要海量数据。三井金属在 M8 以上高端 CCL 应用中的认证深度和历史数据，构成了竞争对手难以复制的壁垒。</p>
<p>高盛预计，其 VSP 铜箔业务 FY3/26 至 FY3/29 的销售复合增速约 56%，且供需已经趋紧。如果后续扩产落地，业务仍有进一步上行空间。这类上游材料公司往往不在终端叙事中心，但当高端铜箔成为高速平台的约束条件时，盈利弹性会被重新发现。</p>
<p>日东纺则是低介电玻璃布领域的全球龙头。公司早在 1998 年率先实现相关材料商业化，第二代 N12 Glass 具备压倒性的市场份额，竞争对手在技术和客户验证上仍有差距。低介电玻璃布进入 CCL 后，可以改善高速信号传输表现，降低损耗，同时适配更高端的 AI 服务器板材需求。</p>
<p>玻璃布在 CCL 中过去可能受良率和成本约束，但随着 AI 服务器规格升级，客户对性能的支付意愿更强，应用受限的概率正在下降。高盛预计 N12 Glass 增长前景强劲，FY3/26 至 FY3/29 的销售复合增速有望达到约 60%。</p>

<h2 id="ccl-beneficiaries">五、CCL 环节：生益科技和松下的结构升级</h2>
<p>中游 CCL 环节，生益科技是核心受益标的之一。公司产品组合正从 M6、M7 向 M9 等级迁移。随着 AI 服务器高端材料需求提升，生益科技的收入结构和利润率都具备改善空间。</p>
<p>到 2027 年，AI 服务器相关收入占比预计达到约 40%，长期有望超过 50%。营业利润率预计从 2025 年约 15% 扩张至 2027 年约 20%。在产品升级和需求放量共同作用下，2026 年和 2027 年净利润同比增速预计分别达到约 104% 和 73%。</p>
<p>生益科技的逻辑不是普通 CCL 景气修复，而是高端 CCL 产品占比提升带来的盈利模型变化。M9 等级材料对介电性能、损耗、稳定性、认证和量产能力都有更高要求，能够切入 AI 服务器供应链的厂商，利润率和估值中枢都有重新评估的空间。</p>
<p>松下的 MEGTRON 系列同样受益明显。MEGTRON 9 已经启动小批量客户验证，高端产品占比到 FY3/27 预计提升至约 60%。松下产线可灵活切换，既能承接高端材料需求，也能根据客户验证进度调整组合。对全球 AI 服务器供应链来说，松下仍是高端 CCL 领域的重要参与者。</p>

<h2 id="pcb-beneficiaries">六、PCB 环节：胜宏科技的产能节奏和客户延伸</h2>
<p>下游 PCB 环节，胜宏科技的泰国工厂布局领先。A1 工厂已经量产，A2 目标在 2026 年第三季度量产，A2 和 A3 单厂产值预计分别比 A1 高 40% 至 100%。约 80% 的 A1 产值用于 AI PCB，说明公司新增产能不是普通扩产，而是直接对接高景气应用。</p>
<p>高盛看好胜宏科技的逻辑包括四个方面：全球 AI 基础设施扩张带来需求增长；PCB 向更高层数升级，推高单机价值；高端 PCB 在部分连接和背板方案中替代传统铜缆或低规格方案；公司有机会向 AI 加速卡、AI 服务器等客户和产品线继续延伸。</p>
<p>PCB 环节的难点在于量产良率和客户认证。层数越高、信号速度越快、散热要求越高，工艺复杂度越强。产能扩张只有在良率稳定、客户验证通过、交付周期可控的情况下，才能真正转化为收入和利润。胜宏科技的领先布局，使其在 AI PCB 放量阶段占据较有利位置。</p>
<p>除胜宏科技外，沪电股份、深南电路等公司也被纳入高盛买入推荐。它们共同对应的是 PCB 从传统通信、汽车、消费电子向 AI 服务器和高端计算平台迁移的结构性机会。行业不会只看总订单，而会越来越看谁能做高层数、高可靠性和高价值量产品。</p>

<h2 id="investment-map">七、投资图谱：从材料到板厂的链条重估</h2>
<p>把产业链连起来看，AI 服务器 PCB/CCL 的投资图谱可以分成三层。第一层是上游材料，包括超低粗糙度铜箔、低介电玻璃布等关键材料。这里的壁垒来自材料配方、客户联合开发、长期验证数据和产能约束。</p>
<p>第二层是 CCL，包括 M9 级以上高端覆铜板。这里的壁垒来自材料组合、压合工艺、稳定性和终端客户认证。产品从 M6、M7 向 M9 升级时，收入和利润率都会发生结构变化。</p>
<p>第三层是 PCB，包括 HDI、高层数多层板、背板和 AI 服务器相关板卡。这里的壁垒来自高层数加工能力、良率、交付能力、海外产能布局和客户关系。AI 服务器架构越复杂，下游板厂的价值量越高。</p>
<p>高盛推荐买入的标的覆盖这三层：生益科技、胜宏科技、沪电股份、深南电路、松下、三井金属、日东纺。这个组合背后不是单一公司故事，而是 AI 服务器把材料、覆铜板和 PCB 同时推向更高规格。</p>
<p>如果按弹性排序，最值得比较的是“稀缺程度”和“收入占比”。材料端稀缺但公司整体收入可能更分散，板厂端收入弹性更直接但竞争和良率压力更大，CCL 环节则处在材料升级和客户认证的中间位置。不同环节的估值逻辑并不完全相同。</p>

<h2 id="risks">八、风险：高景气也需要约束条件</h2>
<p>高增长预期并不等于没有风险。第一类风险是 AI 基础设施投资不及预期。如果云厂商、模型公司或企业客户放缓资本开支，机架和服务器出货预测就会下修，PCB/CCL 需求也会同步回落。</p>
<p>第二类风险是技术路径发生重大变化。虽然材料路线争议不改变大方向，但如果系统架构、互联方式或封装方案出现更大变化，个别材料和厂商的受益程度仍可能被重新分配。</p>
<p>第三类风险是高端领域竞争加剧。高利润会吸引更多厂商投入，若新进入者突破认证和良率，现有龙头的价格和份额都可能承压。第四类风险是宏观环境波动影响中端需求，尤其是传统通信、消费电子和工业板材需求若偏弱，会拖累部分公司非 AI 业务。</p>
<p>因此，PCB/CCL 的投资判断不能只看 TAM 上调，还要持续跟踪 AI 服务器订单、平台验证节奏、材料认证、产能爬坡、良率表现和产品结构变化。只有需求、规格、产能和利润率同时兑现，产业链重估才会更扎实。</p>
<p>更实用的跟踪框架，是把宏观 AI 投资、英伟达平台切换、客户认证进度、材料等级迁移和单厂产能释放放在同一张表里。若服务器机架预测继续上修，而高端铜箔、玻璃布、M9 CCL 和高层数 PCB 产能仍然偏紧，利润弹性就会更集中；若出货预期放缓或新产能集中释放，估值也需要更谨慎。</p>

<h2 id="conclusion">九、结论：AI 服务器正在重写 PCB/CCL 估值逻辑</h2>
<p>AI 服务器带来的不是传统电子材料的周期性反弹，而是规格体系的跃迁。PCB 和 CCL 同时受益于出货量提升、单机用量增加、材料等级升级和单位价值提升。2027 年 TAM 上调、2028 年高增长预测、M9 CCL 占比提升、6 阶以上 HDI PCB 渗透提高，都指向同一个结论：AI 正在把 PCB/CCL 从传统配套环节推向高价值硬件基础设施。</p>
<p>真正需要抓住的是结构性变化。上游材料看三井金属和日东纺，中游 CCL 看生益科技和松下，下游 PCB 看胜宏科技、沪电股份和深南电路。不同公司处在不同环节，但受益逻辑一致：AI 服务器架构越复杂，越需要低损耗、高层数、高可靠性和经过验证的材料与工艺。</p>
<p>这条链条的定价逻辑正在改变。过去 PCB/CCL 更容易被当作传统制造业估值，未来高端 AI 服务器供应链会让市场重新衡量技术壁垒、客户认证、产能稀缺性和利润弹性。高增长预期最终仍要靠订单和业绩兑现，但方向已经清楚：AI 硬件的下一层价值，不只在芯片和光模块，也在承载高速信号的板材和材料系统。</p>
<p>以上内容仅用于产业研究和框架梳理，不构成任何投资建议。</p>
'''


base.POSTS = [
    base.Post(
        slug="goldman-ai-server-pcb-ccl-rubin-ultra-supply-chain",
        title="高盛上调 AI 服务器 PCB/CCL 市场：Rubin Ultra、M9 材料与国产链条重估",
        desc="从 AI 服务器机架上修、PCB/CCL 量价齐升、Rubin Ultra 架构升级，到三井金属、日东纺、生益科技和胜宏科技的产业链弹性。",
        category="投资",
        series="硬科技投资",
        tags=["AI服务器", "PCB", "CCL", "高盛", "Rubin Ultra", "生益科技", "胜宏科技", "沪电股份", "深南电路", "投资"],
        minutes=9,
        body=BODY,
        accent=("#111827", "#2563eb", "#f97316"),
        required=["PCB", "CCL", "Rubin Ultra", "M9", "三井金属", "日东纺", "生益科技", "胜宏科技", "840 亿美元"],
        minimum=5200,
    )
]


_active_ref = None
_base_validate = base.validate


def get_file_at_active_ref(path: str) -> str | None:
    if _active_ref is None:
        raise RuntimeError("active remote ref is not set")
    api_path = quote(path, safe="/")
    try:
        data = base.run_gh([base.endpoint(f"contents/{api_path}?ref={_active_ref.commit_sha}")])
    except RuntimeError as exc:
        if "Not Found" in str(exc):
            return None
        raise
    return base64.b64decode(data["content"]).decode("utf-8")


def validate(outputs: dict[str, str]) -> None:
    _base_validate(outputs)
    extra_forbidden = ["Bilibili", "哔哩哔哩", "视频里", "视频中", "原视频", "音频里", "音频中", "这期", "本期", "作者说", "他提到", "观看", "点赞", "订阅", "投币", "收藏", "下期", "关注", "感谢大家", "BV1"]
    failures: list[str] = []
    post = base.POSTS[0]
    article = outputs[f"2026/{post.slug}/index.html"]
    cover = outputs[f"images/posts/{post.slug}/cover.svg"]
    for word in extra_forbidden:
        if word in article or word in cover:
            failures.append(f"{post.slug}: forbidden wording present: {word}")
    detailed_terms = ["148%", "161%", "9.2 万台", "14.8 万台", "450 万平方米", "1.31 亿张", "NVL144", "NVL576", "VSP", "N12 Glass", "MEGTRON", "不构成任何投资建议"]
    for term in detailed_terms:
        if term not in article:
            failures.append(f"{post.slug}: missing detailed term {term}")
    if failures:
        raise SystemExit("\n".join(failures))


def write_outputs(outputs: dict[str, str]) -> None:
    out_dir = Path("/tmp/goldman-pcb-ccl-ai-server-20260814-publish-output")
    if out_dir.exists():
        import shutil

        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for rel, content in outputs.items():
        path = out_dir / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(json.dumps({"local_output": str(out_dir), "files": len(outputs), "urls": [post.full_url for post in base.POSTS]}, ensure_ascii=False, indent=2))


def create_commit(outputs: dict[str, str], ref: base.RemoteRef) -> str:
    entries = []
    for path, content in sorted(outputs.items()):
        blob = base.run_gh(["-X", "POST", base.endpoint("git/blobs"), "--input", "-"], {"content": content, "encoding": "utf-8"})
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    tree = base.run_gh(["-X", "POST", base.endpoint("git/trees"), "--input", "-"], {"base_tree": ref.tree_sha, "tree": entries})
    commit = base.run_gh(
        ["-X", "POST", base.endpoint("git/commits"), "--input", "-"],
        {"message": "Publish Goldman AI server PCB and CCL article", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    base.run_gh(["-X", "PATCH", base.endpoint(f"git/refs/heads/{base.BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


def main() -> None:
    global _active_ref
    for attempt in range(3):
        ref = base.get_ref()
        _active_ref = ref
        base.get_file = get_file_at_active_ref
        outputs = base.collect_outputs()
        validate(outputs)
        write_outputs(outputs)
        try:
            commit_sha = create_commit(outputs, ref)
        except RuntimeError as exc:
            if attempt < 2 and "Reference update failed" in str(exc):
                continue
            raise
        current_head = base.get_ref().commit_sha
        if current_head != commit_sha:
            comparison = base.run_gh([base.endpoint(f"compare/{commit_sha}...{current_head}")])
            if comparison.get("status") not in {"ahead", "identical"}:
                raise RuntimeError("published commit is not an ancestor of current remote head")
        print(json.dumps({"parent": ref.commit_sha, "pushed": commit_sha, "urls": [post.full_url for post in base.POSTS]}, ensure_ascii=False, indent=2))
        return
    raise RuntimeError("publication retried after concurrent updates but did not succeed")


if __name__ == "__main__":
    main()
