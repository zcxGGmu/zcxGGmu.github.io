from __future__ import annotations

import html
import json
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
from urllib.parse import quote


ROOT = Path("/tmp/hermes-video-publish-20260727-bv16-bv1gr.s5tOc3")
SITE = "https://zcxggmu.github.io"
DATE = "2026-07-27"
BASE_DT = datetime(2026, 7, 27, 23, 20, tzinfo=timezone(timedelta(hours=8)))
PREV_EXISTING_URL = "/2026/fields-medal-chinese-education-talent-freedom/"
PREV_EXISTING_TITLE = "真正留住天才的不是筛选，而是自由：从菲尔兹奖看中式教育的边界"
SCRIPT_NAME = "publish-agentteams-deep-dive-article-20260727.py"
MANIFEST_NAME = "publish-agentteams-deep-dive-article-20260727-changed-files.json"
CHANGED: set[str] = set()


@dataclass(frozen=True)
class Post:
    slug: str
    title: str
    desc: str
    category: str
    series: str
    tags: list[str]
    minutes: int
    body: str

    @property
    def url_path(self) -> str:
        return f"/2026/{self.slug}/"

    @property
    def full_url(self) -> str:
        return SITE + self.url_path

    @property
    def asset_prefix(self) -> str:
        return f"/images/posts/{self.slug}"

    @property
    def cover(self) -> str:
        return f"{self.asset_prefix}/cover.svg"


ARTICLE_BODY = """
<p><img src="/images/posts/agentteams-collaborative-multi-agent-os-openclaw-hermes/cover.svg" alt="AgentTeams 深度拆解：Matrix 房间里的多 Agent 协作操作系统" style="width:100%;height:auto;object-fit:contain"></p>
<p>AgentTeams 的核心价值，不是再造一个大模型 Agent 内核，而是把多个已经存在的 Agent runtime 组织成一个可见、可管、可审计的协作系统。它把人、Manager、Worker、Team、文件系统、模型网关和运行时容器放到同一张控制面里，让多 Agent 协作从“聊天窗口里的临时分工”变成“有身份、有房间、有状态、有存储、有生命周期”的操作系统。</p>
<p>这套系统最有意思的地方在于它承认现实：不同 Agent runtime 有不同优势。OpenClaw 适合做多渠道、多房间、多技能的协调入口；QwenPaw/CoPaw 可以承担另一类 Python 运行时和团队领导者角色；Hermes 更像自治执行型 Worker，适合在隔离容器里完成代码、自动化和长任务。AgentTeams 站在它们上方，提供协作协议、控制面和基础设施，把“谁负责协调、谁负责执行、谁能看到什么、结果放在哪里、什么时候启动或休眠”这些问题系统化。</p>
<p>因此，AgentTeams 更接近一个协作型 Multi-Agent OS：Matrix 是消息总线和审计时间线，Tuwunel 是房间服务器，Element 是人类可见界面，Higress 是 LLM/MCP/API 网关，MinIO/OSS 是共享文件系统，Controller 是声明式控制面，Manager 是调度员，Worker 是执行单元，Team 是层级化协作组织。</p>

<h2 id="positioning">定位：多 Agent 协作操作系统，而不是单体 Agent</h2>
<p>传统 Agent 项目通常从一个“智能体大脑”开始：定义提示词、工具、记忆、模型和执行循环。AgentTeams 的切入点不同，它从协作系统开始：先定义人类、Manager、Worker 和 Team 的关系，再把不同 runtime 装进容器，通过统一的房间、凭据、文件和控制接口连接起来。</p>
<p>这种定位带来三个直接结果。第一，AgentTeams 不需要押注某一个 Agent 内核永远胜出。OpenClaw、QwenPaw、Hermes 可以共存，runtime 只是 Worker 或 Manager 的实现方式。第二，协作过程天然可见。任务分配、追问、阻塞、结果通知都发生在 Matrix 房间，人类可以旁观，也可以随时介入。第三，状态不完全依赖上下文窗口。任务说明、计划、进度、结果、技能和运行时配置被写入对象存储，即使 Agent 会话重置，也能从文件恢复。</p>
<p>这解决的是多 Agent 工程化里最常见的几个痛点：临时拉起的 Agent 容易失联；上下文断掉后无法恢复；不同 Agent 之间缺少共享状态；工具凭据容易泄漏；人类只看到最终结论，看不到过程；多个 Worker 的生命周期和成本不可控。AgentTeams 用平台层把这些问题收束起来。</p>

<h2 id="architecture">总体架构：控制面、协作面、数据面和运行时</h2>
<figure>
  <img src="/images/posts/agentteams-collaborative-multi-agent-os-openclaw-hermes/architecture.svg" alt="AgentTeams 总体架构图" style="width:100%;height:auto;object-fit:contain">
  <figcaption>AgentTeams 把人类界面、Matrix 房间、控制器、对象存储、网关和多种 Worker runtime 分层连接。</figcaption>
</figure>
<p>AgentTeams 的架构可以拆成四层。</p>
<p>第一层是人类交互层。用户通过 Element Web 或其他接入渠道和 Manager、Worker、Team 房间沟通。这里的关键不是“聊天”，而是把人类监督变成一条可审计时间线：每个任务如何被分配，谁提出问题，谁批准执行，谁报告完成，都能在房间里追溯。</p>
<p>第二层是协作通信层。Tuwunel 提供 Matrix homeserver，所有 Agent 都有自己的 Matrix 身份。Manager 与 Human 有 DM，Manager 与 Worker 有专属 Worker Room，Team 有 Team Room，Team Leader 还可能拥有和 Team Admin 的 Leader DM。@mention 不是礼貌动作，而是唤醒协议：只有被明确点名的 Agent 才应该处理任务，避免多 Agent 房间里互相误触发。</p>
<p>第三层是控制面。agentteams-controller 是 Go 编写的 operator 与 REST API 服务。它维护 Worker、Manager、Team、Human 等 CRD，负责 reconcile、创建账号、生成凭据、创建房间、写入配置、调度容器、暴露服务、刷新状态。`agt` CLI 和 Manager 的管理技能最终都应该通过这个控制面做资源变更，而不是手写临时命令。</p>
<p>第四层是数据面与运行时层。MinIO/OSS 存放 `agents/<name>/`、`shared/tasks/`、`manager/` 等对象；Higress 提供统一 AI Gateway 与 MCP Server 路由；Docker/Kubernetes backend 负责拉起不同 runtime 的容器或 Pod。OpenClaw、QwenPaw/CoPaw、Hermes 不需要彼此直接耦合，它们通过 Matrix、共享文件和控制器契约协作。</p>

<h2 id="control-plane">控制面：CRD + Reconciler + REST API</h2>
<p>AgentTeams 的工程内核在 `agentteams-controller`。它不是一个简单的脚本集合，而是 Kubernetes controller-runtime 风格的应用容器：启动时初始化 scheme、基础设施客户端、controller manager、backend registry、字段索引、鉴权中间件、服务层、各类 reconciler 和 HTTP server。启动后，HTTP API、初始化器、远端客户端维护、凭据清理和 controller manager 并行运行。</p>
<p>CRD 是系统的声明式入口。WorkerSpec 包含模型、runtime、镜像、身份、SOUL、AGENTS、技能、远程技能、MCP Server、包、端口暴露、channelPolicy、资源、空闲超时、生命周期状态、AccessEntry、AgentIdentity、CredentialBinding、deployMode、serviceEnabled、backendRuntime、Pod labels、volumes 和 mounts。Manager、Team、Human 也各有资源模型。用户要表达的是“我想要什么样的 Agent 成员”，Controller 负责把它收敛成真实的账号、房间、文件、网关消费者和容器。</p>
<p>REST API 是命令式入口。`/api/v1/workers`、`/api/v1/teams`、`/api/v1/humans`、`/api/v1/managers` 提供 CRUD；`wake`、`sleep`、`ensure-ready`、`ready`、`status` 提供生命周期控制；Gateway endpoint 管消费者；Credentials endpoint 发放 STS 和 Matrix token；Matrix AppService endpoint 接收 homeserver 事件；嵌入式模式下还有受安全校验保护的 Docker API passthrough。</p>
<p>这意味着 AgentTeams 同时支持两种使用姿势：人可以在 Matrix 中让 Manager 创建 Worker，也可以用 `agt create worker` 或 YAML 直接声明资源。前者适合日常协作，后者适合自动化、CI、Kubernetes 和平台集成。</p>

<h2 id="worker-lifecycle">Worker 生命周期：从声明到可执行容器</h2>
<figure>
  <img src="/images/posts/agentteams-collaborative-multi-agent-os-openclaw-hermes/workflow.svg" alt="AgentTeams Worker 生命周期流程图" style="width:100%;height:auto;object-fit:contain">
  <figcaption>Worker 创建不是单一容器启动，而是身份、房间、网关、存储、配置和运行时容器的连续收敛。</figcaption>
</figure>
<p>Worker 创建流程体现了 AgentTeams 的平台化程度。一个 Worker 从 CR 或 Manager 指令进入系统后，控制器先进入 infrastructure phase：加载或生成凭据，注册 Matrix 账号，必要时创建 MinIO 用户和策略，创建或解析 Worker 房间，邀请 admin、manager、worker，设置 power level，再创建 Higress consumer 和 key-auth 绑定。</p>
<p>接着是 config phase。Deployer 会部署包、写入 inline identity/soul/agents、生成 `openclaw.json`、合并 AGENTS.md、写入 SOUL.md、配置 mcporter、推送内置技能，并把文件同步到对象存储。对于 QwenPaw 或 Edge/remote-managed local 这类运行时，控制器还会写 `agents/<runtimeName>/runtime/runtime.yaml`，把团队关系、模型、MCP、channelPolicy、状态、存储前缀和凭据环境变量名投影给 runtime。</p>
<p>最后是 container phase。Controller 根据 desired state 决定 Worker 应该 Running、Sleeping 还是 Stopped。Docker backend 通过 Docker Engine API 创建容器，Kubernetes backend 创建 Pod 并挂载 service account token。spec 变更会触发删除旧资源再重建，睡眠状态会停止或删除容器，edge worker 则跳过托管 Pod，只保留凭据和 runtime.yaml 这类远端运行需要的控制信息。</p>
<p>这个设计的重点是幂等。WorkerReconciler 并不假设一次命令一定成功，而是不断观察现实状态与期望状态的差异：房间没建好就重试，配置没写完就继续写，容器缺失就创建，spec hash 不一致就重建，状态进入 transient 就等待下一轮事件或周期 reconcile。多 Agent 平台要长时间运行，幂等比“演示时能跑通”更重要。</p>

<h2 id="manager">Manager：调度员、记忆入口和系统管理员</h2>
<p>Manager 是 AgentTeams 的协调中心。它不是所有任务的执行者，而是把人类目标转化为资源创建、任务登记、文件准备、Worker 唤醒、房间通知、结果收集和状态更新的调度员。</p>
<p>Manager 的系统文件主要是 `SOUL.md`、`HEARTBEAT.md` 和 `AGENTS.md`。内置技能覆盖 channel management、file sync、git delegation、worker/team/human management、MCP server management、model switch、project management、task coordination、task management、service publishing 等。这里体现了 AgentTeams 的设计哲学：Manager 不应该用零散自然语言“凭感觉管理”，而应该通过技能和 CLI 调用控制面。</p>
<p>Manager 的 `AGENTS.md` 里把很多协作规则写得非常工程化：创建多个 Worker 时要并行发起 `agt create worker --no-wait`；给 Worker 分配任务必须在 Worker Room 或 Project Room 里真正 @mention，而不能只在 admin DM 中说“已分配”；任务必须登记到 `state.json`，否则 idle timeout 可能把 Worker 停掉；Worker 完成后不能只口头确认，必须拉取任务目录、读 result、更新 meta/state、写 memory、通知 admin。</p>
<p>这种规则看似繁琐，本质上是在把多 Agent 协作从“聊天即执行”拉回“有状态的工作流”。Manager 的价值不在于永远亲自完成任务，而在于让每一个任务都有编号、有目录、有负责人、有进度、有结果、有恢复路径。</p>

<h2 id="worker-runtime">Worker Runtime：OpenClaw、QwenPaw/CoPaw 与 Hermes</h2>
<p>Worker 是轻量、相对无状态的执行容器。它们连接 Matrix，拉取 MinIO/OSS 中的配置和共享数据，通过 AI Gateway 访问模型，通过 mcporter 调 MCP Server，通过本地工作区产生结果，再把结果同步回共享文件系统。</p>
<p>OpenClaw Worker 采用 `/root/agentteams-fs/agents/<worker-name>/` 作为 HOME 和工作区，`openclaw.json`、SOUL、AGENTS、skills 和 `.openclaw/` 都在这个目录下。入口脚本会配置 `mc`，拉取 `agents/<name>/` 和 `shared/`，建立 skills symlink，启动本地到远端的变更推送，再每 5 分钟拉取 Manager 管理的配置与共享文件。OpenClaw 配置支持 Matrix channel、AI Gateway provider、memory-core、session reset、invite auto-join、私网 homeserver 访问等细节。</p>
<p>QwenPaw/CoPaw Worker 更偏 Python runtime。CoPaw 有 standard/lite 模式，QwenPaw 把工作目录设在 `/root/agentteams-fs/agents/<worker-name>` 下，并使用 `.qwenpaw` 作为运行时目录。它更依赖 controller 写入的 runtime.yaml 和 worker 自己的 desired-state apply loop，是 AgentTeams 向“runtime-neutral contract”演进的重要方向。</p>
<p>Hermes Worker 的入口明确把 HOME、workspace 和 MinIO mirror root 对齐到 `/root/agentteams-fs/agents/<worker-name>/`，并把 `HERMES_HOME` 放在 `.hermes/`。它默认开启 `HERMES_YOLO_MODE=1`，因为 Worker 容器本身就是隔离边界；如果每个危险命令都等待人工批准，多 Agent 工作流会卡住。Hermes 还会设置 `MATRIX_HOME_CHANNEL=disabled`，避免每个会话反复出现不适合 Worker 场景的 home channel 提示。</p>

<h2 id="openclaw-hermes">OpenClaw 与 Hermes 的协作关系</h2>
<figure>
  <img src="/images/posts/agentteams-collaborative-multi-agent-os-openclaw-hermes/runtime-collaboration.svg" alt="OpenClaw 与 Hermes 在 AgentTeams 中的协作关系" style="width:100%;height:auto;object-fit:contain">
  <figcaption>OpenClaw 更适合协调入口和 Leader，Hermes 更适合自治执行 Worker；AgentTeams 提供统一房间、文件、凭据和生命周期控制。</figcaption>
</figure>
<p>OpenClaw 与 Hermes 在 AgentTeams 中不是二选一关系，而是上下游协作关系。AgentTeams 把 runtime 差异藏在 Worker 规格、镜像、入口脚本、工作区布局和 runtime config 里，对协作层暴露的是统一身份、统一房间、统一文件目录、统一任务约定和统一生命周期。</p>
<p>OpenClaw 的优势在协调：多渠道、Matrix 插件、技能目录、房间协议、heartbeat、任务状态、控制 UI 和 Manager/Leader 工作流都更适合做“组织者”。一个 OpenClaw Manager 可以接收人类需求，拆解任务，选择 Worker，创建项目房间，准备共享文件，@mention Worker，追踪结果，必要时升级给人类。</p>
<p>Hermes 的优势在执行：它更适合在容器内完成相对独立的开发、自动化、工具调用和长周期任务。它不需要成为系统唯一入口，也不需要承担所有协调规则；只要能读取任务目录、使用模型与工具、把产物写回共享空间，并在房间里报告完成，就能作为高自治 Worker 嵌入 AgentTeams。</p>
<p>这是一种很务实的组合：用 OpenClaw/QwenPaw 这类更确定的协调 runtime 当 Manager 或 Team Leader，用 Hermes 这类自治执行 runtime 当 Worker，AgentTeams 负责“组织协作”。当 Agent 内核还在快速迭代时，把协作协议、身份、文件、网关和生命周期放在平台层，会比把所有能力塞进一个超大 Agent 更稳。</p>

<h2 id="team">Team：从扁平 Worker 池到层级协作组织</h2>
<p>单 Manager 管多个 Worker 容易形成瓶颈。Team 资源把协作层级化：Team 有 Leader、Workers、Admin、Human Members、Team Room、Leader DM 和 per-worker rooms。TeamReconciler 会解析 Human 身份，把有权限的人加入团队上下文，并同步人类房间状态。</p>
<p>控制器还会把 Coordination block 注入 AGENTS.md。Leader 会知道上游 coordinator 是 Manager，Team Admin 是谁，Team Room 在哪里，Worker 列表和房间 ID 是什么，heartbeat 间隔和 idle timeout 是什么；Worker 会知道自己的 coordinator 是 Team Leader，不能直接 @mention Manager，完成、阻塞和问题都要报给 Leader。</p>
<p>这解决了多 Agent 规模化中的一个关键问题：协作拓扑不能靠 Agent 自己猜。谁能分配任务、谁能做决策、谁向谁汇报、哪些人可以 @mention Worker，都应该成为运行时提示词和配置的一部分。AgentTeams 用 Team CRD 和 Coordination injection 把这些关系写成可管理的系统事实。</p>

<h2 id="storage">共享文件系统：比上下文窗口更可靠的协作记忆</h2>
<p>多 Agent 协作不能只依赖对话历史。AgentTeams 把持久状态放在 MinIO/OSS：Manager 配置在 `agents/manager/`，Worker 配置在 `agents/<name>/`，共享任务在 `shared/tasks/<task-id>/`，结果通常写入 `result.md`，进度可以按日期写入 `progress/YYYY-MM-DD.md`。</p>
<p>这种设计有三个好处。第一，任务上下文可以恢复。Worker 会话重置后，可以读取 task-history、spec、plan 和 progress 重新接上。第二，文件是跨 runtime 的最低共同协议。OpenClaw、QwenPaw、Hermes 都能读写文件，不必共享同一个内存系统。第三，审计更清楚。房间记录“谁说了什么”，对象存储记录“任务文件和产物是什么”，两者合在一起才是真正可追踪的协作日志。</p>
<p>文件同步策略也体现了工程经验。OpenClaw Worker 不再简单依赖 `mc mirror --watch`，而是用变更检测推送 Worker 管理内容，对 Manager 管理的 openclaw.json、mcporter 配置和 skills 做周期拉取和按需同步，避免刚拉下来的配置被本地旧文件反向覆盖。对多 Agent 系统来说，文件所有权和同步方向必须清晰，否则很容易出现配置互相覆盖。</p>

<h2 id="gateway-security">网关、凭据与安全边界</h2>
<p>AgentTeams 把 LLM 与 MCP 访问集中到 Higress AI Gateway。每个 Worker 对应 gateway consumer 和 key-auth，控制器把模型 provider、MCP Server endpoint 和 Authorization header 写进配置或 runtime.yaml。这样，Worker 不需要直接拿到平台全局 API Key，而是使用自己的 consumer key 和授权范围访问模型与工具。</p>
<p>CRD 里还把 AccessEntry、AgentIdentity、CredentialBinding 作为一等字段。AccessEntry 描述对象存储、AI gateway、AI registry、scheduler 等服务权限；AgentIdentity 提供工作负载身份事实；CredentialBinding 只引用凭据 provider，不携带真实 secret，并允许配置 tool whitelist。这是把“Agent 能访问什么”从提示词约束推进到平台资源模型。</p>
<p>Matrix 也承担安全边界。房间邀请、allowlist、power level、@mention 协议和 Matrix token 控制了谁能向 Agent 发送有效消息。Manager 侧还明确要求敏感信息不要通过聊天消息泄露，凭据通过文件系统和控制器流转。</p>
<p>这套安全模型不是完美终局，但方向正确：多 Agent 平台不能把安全只写进系统提示词。身份、凭据、网关授权、对象存储前缀、ServiceAccount token、房间权限和工具白名单，必须在平台层共同约束。</p>

<h2 id="deployment">部署拓扑：本地嵌入式与 Kubernetes</h2>
<p>本地嵌入式部署把 Higress、Tuwunel、MinIO、Element Web 和 controller 运行在 `agentteams-controller` 容器中，Manager 单独运行，Worker 由 Controller 或 Manager 通过 Docker socket 拉起。这适合个人开发、演示、小团队本机使用，优点是启动快、依赖少、可直接在 Element 里看到协作过程。</p>
<p>Kubernetes 部署则更接近生产形态：Higress 作为子 chart，Tuwunel StatefulSet，MinIO 或 OSS，Element Web，controller Deployment，Manager/Worker 由 CRD 驱动创建 Pod。K8s backend 会使用 in-cluster config 或 kubeconfig，给 Pod 挂载 projected service account token，设置 owner reference，让 CR 删除能触发 Kubernetes 垃圾回收。</p>
<p>两种拓扑的核心差异不是功能多少，而是控制边界。本地模式更像一体化开发环境，Kubernetes 模式更像平台工程：资源限制、service account、命名空间、PodTemplate overlay、网关和对象存储都需要更严格治理。文章级理解可以把它们视为同一个控制面在不同基础设施 backend 上的落地。</p>

<h2 id="module-breakdown">模块拆解：每一层各司其职</h2>
<p>按代码模块看，AgentTeams 的职责边界比较清晰。</p>
<p>`agentteams-controller/api/v1beta1` 定义资源模型和契约，包括 Worker、Manager、Team、Human 以及 AccessEntry、MCPServer、RemoteSkillSource、CredentialBinding 等字段。它决定平台能声明什么。</p>
<p>`internal/app` 负责应用装配：基础设施客户端、backend、auth、service layer、reconciler 和 HTTP server 都在这里接线。它决定控制器如何启动。</p>
<p>`internal/controller` 负责声明式收敛。WorkerReconciler、ManagerReconciler、TeamReconciler、HumanReconciler 分别处理不同 CR，member_reconcile 把 Worker 与 Team member 的通用流程抽出来，避免 standalone Worker 和 Team Worker 各走一套逻辑。</p>
<p>`internal/service` 是平台操作层。Provisioner 管 Matrix、Gateway、MinIO、ServiceAccount 和端口暴露；Deployer 管配置生成、包部署、AGENTS 合并、技能推送、runtime.yaml 写入；EnvBuilder 管容器环境变量。</p>
<p>`internal/backend` 抽象运行实例。Docker backend 管本地容器，Kubernetes backend 管 Pod，sandbox backend 是更高级隔离形态的入口；runtime resolution 在这里统一处理 explicit runtime、caller fallback 和 openclaw 默认值。</p>
<p>`manager/agent/skills` 是 Manager 的操作手册库，负责把“如何创建 Worker、如何管理任务、如何同步文件、如何发布服务、如何切换模型”变成可复用技能。`worker/scripts`、`hermes/scripts`、`copaw/scripts`、`qwenpaw/scripts` 则是不同 runtime 的容器入口，把平台凭据和文件系统契约翻译成具体 Agent 进程。</p>

<h2 id="teamharness">TeamHarness：插件化协作语义的预演</h2>
<p>AgentTeams 还在推进 TeamHarness 这类 runtime-neutral 插件包。它的边界很明确：提供团队协作提示词、角色提示词、组织/沟通/文件共享/项目管理/任务委派/任务执行等技能，以及 message、filesync、projectflow、taskflow 等 MCP 工具；但不负责 Worker 生命周期、Controller reconcile、runtime desired-state apply loop、凭据值存储或周期性文件同步。</p>
<p>这个边界很重要。AgentTeams 的主平台负责“资源和生命周期”，TeamHarness 负责“协作语义和工具包”，具体 runtime adapter 负责“把这些语义落到 QwenPaw、Claude Code 或其他运行时”。如果这三层混在一起，插件会变成小型控制器，runtime 会偷偷管理平台资源，系统边界会迅速失控。</p>
<p>更长远看，AgentTeams 的协作能力可能会从 Manager 技能逐步沉淀到 TeamHarness 这类插件契约中。控制器继续写 runtime.yaml，runtime adapter 读取 desired state，TeamHarness 提供统一协作工具。这样，多 Agent OS 才能真正支持更多 runtime，而不是围绕某一个 Agent 内核写死。</p>

<h2 id="workflow">完整工作流：一个任务如何被执行</h2>
<p>一次典型任务可以这样理解。</p>
<p>人类先在 Manager DM 或 Team Admin 入口提出目标。Manager 判断是否需要新建 Worker 或使用已有 Worker。如果需要新建，它通过 `agt` 或技能创建 Worker CR，控制器完成账号、房间、网关、存储、配置和容器创建。Worker Ready 后，Manager 在共享文件系统中写入任务目录，包括 meta、spec、plan 或必要输入文件。</p>
<p>随后 Manager 在正确房间 @mention Worker 或 Team Leader。Worker 收到 Matrix 消息后拉取任务文件，执行任务，把中间进度写到 `shared/tasks/<task-id>/progress/`，把最终结果写入 `result.md`，再在房间里 @mention coordinator 报告完成。如果任务复杂，Team Leader 可以继续拆给多个 Worker，在 Team Room 中协调分工。</p>
<p>Manager 收到完成通知后，不应该只发一句“收到”。正确流程是拉取任务目录、读取 result、更新 meta.json 和 state.json、写 memory、必要时通知人类、归档或继续下一步。整个过程中，人类可以在 Element 中看到消息时间线，也可以直接介入问题、批准敏感动作、调整任务范围。</p>
<p>这个流程把 Agent 的“智能执行”嵌入到“工程化协作”里。前者决定任务能否做成，后者决定任务能否被管理、恢复、审计和规模化。</p>

<h2 id="strengths">核心优势：透明、可插拔、可恢复、可治理</h2>
<p>AgentTeams 最大的优势是透明。传统后台 Agent 任务一旦跑起来，人类往往只能等最终结果；AgentTeams 把协作放进房间，过程天然可见。透明不是为了好看，而是为了干预和审计。</p>
<p>第二个优势是 runtime 可插拔。OpenClaw、QwenPaw、Hermes 可以在同一个房间体系和对象存储体系中协作，平台不被单一 Agent 内核绑定。Agent 技术迭代太快，平台层越中立，长期越有韧性。</p>
<p>第三个优势是可恢复。任务文件、进度日志、task history、runtime config 和共享目录让系统不完全依赖模型上下文。session reset、容器重启、Worker 睡眠后再唤醒，都不必从零开始。</p>
<p>第四个优势是可治理。CRD、REST API、ServiceAccount、Gateway consumer、Matrix identity、对象存储前缀、AccessEntry、CredentialBinding、channelPolicy 让平台可以逐步把权限和生命周期收束到可管理模型里。</p>

<h2 id="limits">边界与风险：复杂度来自真实协作</h2>
<p>AgentTeams 的复杂度不低。Matrix、Higress、MinIO/OSS、Controller、Manager、Worker、runtime entrypoint、技能、对象存储同步、gateway auth、Kubernetes/Docker backend 共同组成系统，排障要求比单体 Agent 高得多。</p>
<p>第二个风险是 runtime 差异。OpenClaw 使用 openclaw.json 和 Matrix 插件，QwenPaw/Hermes 逐步使用 runtime.yaml 契约，CoPaw 又有不同安装目录和 console 模式。平台虽然抽象了 runtime，但每个 runtime 的文件布局、热加载能力、审批模型、日志和工具行为仍然不同。</p>
<p>第三个风险是协作纪律。@mention 协议、任务登记、文件先推送再通知、Worker 完成后必须读 result 并更新 state，这些流程如果被 Manager 或技能违反，系统仍会卡住。多 Agent 平台不是只靠模型更强就能自动正确，流程约束必须持续打磨。</p>
<p>第四个风险是生产安全。YOLO Worker、Docker socket、本地 host-share、MCP 工具、模型网关和凭据流转都需要严格边界。AgentTeams 已经把很多边界放到平台层，但生产落地仍要结合网络隔离、最小权限、日志审计、敏感数据策略和人工审批机制。</p>

<h2 id="when-to-use">适用场景：什么时候值得引入 AgentTeams</h2>
<p>如果只是让一个 Agent 帮忙写一段代码、查一个问题、处理一个简单文件，单体 Agent 足够。AgentTeams 的价值出现在更复杂的场景：需要多个 Worker 并行处理任务；需要人类实时旁观和介入；需要长期任务恢复；需要不同 runtime 协作；需要统一管理模型、MCP、凭据和文件；需要把任务执行过程留痕。</p>
<p>典型场景包括：研发团队把需求拆给多个 coding worker；运维团队让不同 Worker 处理监控、日志、修复和报告；数据团队让 Worker 并行清洗、分析、制图和写报告；企业内部把不同部门的工具通过 MCP 暴露给 Agent；个人高级用户把 Hermes、OpenClaw、QwenPaw 等不同执行器组织成一个可控工作台。</p>
<p>简单说，AgentTeams 不适合把简单任务复杂化，但适合把复杂协作标准化。</p>

<h2 id="conclusion">结论：AgentTeams 的价值在“组织智能”</h2>
<p>AgentTeams 的长期价值不在于某个单点模型调用，也不在于某个 Worker runtime 的即时能力，而在于它把 Agent 协作中的组织问题工程化了。身份、房间、@mention、任务目录、结果文件、技能、网关、权限、生命周期、状态恢复，这些看似琐碎的东西，恰恰是多 Agent 从演示走向日常工作的关键。</p>
<p>OpenClaw 与 Hermes 的关系也应该放在这个框架下理解：OpenClaw 更适合成为协调入口和团队 Leader，Hermes 更适合作为自治执行 Worker；AgentTeams 则提供让它们协作的操作系统层。未来 Agent runtime 还会不断变化，但只要人类监督、多 Agent 分工、共享文件、工具权限和任务恢复仍是刚需，AgentTeams 这种控制面优先的架构就有持续价值。</p>
"""


POST = Post(
    slug="agentteams-collaborative-multi-agent-os-openclaw-hermes",
    title="AgentTeams 深度拆解：Matrix 房间里的多 Agent 协作操作系统",
    desc="AgentTeams 把 Manager、Worker、Team、Matrix 房间、MinIO/OSS、Higress 网关和 OpenClaw/Hermes 等运行时组织成可见、可管、可审计的多 Agent 协作系统。",
    category="AI工具",
    series="Agent工程",
    tags=["AgentTeams", "多Agent", "OpenClaw", "Hermes", "Matrix", "Higress", "MinIO", "Kubernetes", "MCP", "Agent架构"],
    minutes=18,
    body=ARTICLE_BODY,
)


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def rec(path: Path) -> None:
    CHANGED.add(path.relative_to(ROOT).as_posix())


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    rec(path)


def term_url(kind: str, term: str) -> str:
    return f"/{kind}/{quote(term)}/"


def meta_links(post: Post) -> str:
    cat = f'<a href="{term_url("categories", post.category)}">{esc(post.category)}</a>'
    tags = "&nbsp;".join(f'<a href="{term_url("tags", tag)}">{esc(tag)}</a>' for tag in post.tags)
    return f'<span class="meta-icon" aria-hidden="true">▣</span> {cat}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◇</span> {tags}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {post.minutes} min'


def build_toc(body: str) -> str:
    links = [
        f'<a class="toc-link toc-level-2" href="#{m.group(1)}">{m.group(2)}</a>'
        for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    ]
    return '<div class="toc-wrapper"><div class="toc"><div class="toc-title">目录</div><nav>' + "".join(links) + "</nav></div></div>"


def cover_svg() -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" role="img" aria-labelledby="title desc">
  <title id="title">{esc(POST.title)}</title>
  <desc id="desc">{esc(POST.desc)}</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0f172a"/><stop offset="0.52" stop-color="#1e3a8a"/><stop offset="1" stop-color="#0f766e"/>
    </linearGradient>
    <filter id="shadow"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-color="#000" flood-opacity="0.28"/></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.16" stroke="#e0f2fe" stroke-width="3">
    <path d="M160 170 H1440"/><path d="M160 350 H1440"/><path d="M160 530 H1440"/><path d="M160 710 H1440"/>
    <path d="M260 110 V790"/><path d="M540 110 V790"/><path d="M820 110 V790"/><path d="M1100 110 V790"/><path d="M1380 110 V790"/>
  </g>
  <g filter="url(#shadow)">
    <rect x="118" y="112" width="420" height="130" rx="28" fill="#f8fafc" opacity="0.96"/>
    <text x="152" y="190" fill="#1e3a8a" font-family="Noto Sans SC, PingFang SC, Arial" font-size="48" font-weight="800">AgentTeams</text>
    <circle cx="800" cy="445" r="92" fill="#f8fafc" opacity="0.92"/>
    <text x="737" y="459" fill="#0f172a" font-family="Arial" font-size="48" font-weight="800">OS</text>
    <rect x="310" y="520" width="230" height="86" rx="20" fill="#38bdf8" opacity="0.96"/>
    <rect x="655" y="620" width="290" height="86" rx="20" fill="#a7f3d0" opacity="0.96"/>
    <rect x="1060" y="520" width="230" height="86" rx="20" fill="#fde68a" opacity="0.96"/>
    <text x="362" y="575" fill="#082f49" font-family="Noto Sans SC, PingFang SC, Arial" font-size="34" font-weight="800">OpenClaw</text>
    <text x="726" y="675" fill="#064e3b" font-family="Noto Sans SC, PingFang SC, Arial" font-size="34" font-weight="800">Matrix Room</text>
    <text x="1110" y="575" fill="#78350f" font-family="Noto Sans SC, PingFang SC, Arial" font-size="34" font-weight="800">Hermes</text>
    <path d="M540 562 C625 530 690 492 725 458" fill="none" stroke="#f8fafc" stroke-width="9" stroke-linecap="round"/>
    <path d="M860 462 C925 512 1002 542 1060 562" fill="none" stroke="#f8fafc" stroke-width="9" stroke-linecap="round"/>
    <path d="M800 537 V620" fill="none" stroke="#f8fafc" stroke-width="9" stroke-linecap="round"/>
  </g>
  <text x="118" y="338" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="62" font-weight="800">Matrix 房间里的</text>
  <text x="118" y="420" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="62" font-weight="800">多 Agent 协作操作系统</text>
  <text x="120" y="785" fill="#e0f2fe" font-family="Noto Sans SC, PingFang SC, Arial" font-size="30" font-weight="600">Controller · Manager · Worker · Team · MinIO/OSS · Higress · OpenClaw · Hermes</text>
</svg>'''


def architecture_svg() -> str:
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="980" viewBox="0 0 1800 980" role="img" aria-labelledby="title desc">
  <title id="title">AgentTeams 总体架构</title><desc id="desc">展示 Human、Element、Matrix、Controller、MinIO、Higress 与多种 Agent runtime 的关系。</desc>
  <rect width="1800" height="980" fill="#f8fafc"/>
  <text x="72" y="86" font-family="Noto Sans SC, PingFang SC, Arial" font-size="42" font-weight="800" fill="#0f172a">AgentTeams 总体架构</text>
  <text x="72" y="126" font-family="Noto Sans SC, PingFang SC, Arial" font-size="22" fill="#475569">协作面承载消息与审计，控制面收敛资源，数据面提供模型、工具和共享文件，运行时负责实际执行。</text>
  <g font-family="Noto Sans SC, PingFang SC, Arial">
    <rect x="70" y="190" width="350" height="210" rx="18" fill="#dbeafe" stroke="#2563eb" stroke-width="3"/>
    <text x="105" y="250" font-size="30" font-weight="800" fill="#1e3a8a">人类交互层</text>
    <text x="105" y="302" font-size="23" fill="#1e3a8a">Human Admin / Team Admin</text>
    <text x="105" y="342" font-size="23" fill="#1e3a8a">Element Web / 其他渠道</text>

    <rect x="505" y="190" width="440" height="210" rx="18" fill="#dcfce7" stroke="#16a34a" stroke-width="3"/>
    <text x="540" y="250" font-size="30" font-weight="800" fill="#166534">协作通信层</text>
    <text x="540" y="302" font-size="23" fill="#166534">Tuwunel Matrix Homeserver</text>
    <text x="540" y="342" font-size="23" fill="#166534">DM · Worker Room · Team Room</text>

    <rect x="1030" y="190" width="690" height="210" rx="18" fill="#ede9fe" stroke="#7c3aed" stroke-width="3"/>
    <text x="1065" y="250" font-size="30" font-weight="800" fill="#5b21b6">控制面</text>
    <text x="1065" y="302" font-size="23" fill="#5b21b6">agentteams-controller · REST API · agt CLI</text>
    <text x="1065" y="342" font-size="23" fill="#5b21b6">Worker / Manager / Team / Human CRD + Reconciler</text>

    <rect x="70" y="500" width="510" height="250" rx="18" fill="#fef3c7" stroke="#d97706" stroke-width="3"/>
    <text x="105" y="560" font-size="30" font-weight="800" fill="#92400e">共享文件系统</text>
    <text x="105" y="612" font-size="23" fill="#92400e">MinIO / OSS</text>
    <text x="105" y="652" font-size="23" fill="#92400e">agents/&lt;name&gt; · shared/tasks · runtime.yaml</text>
    <text x="105" y="692" font-size="23" fill="#92400e">spec · plan · progress · result</text>

    <rect x="665" y="500" width="430" height="250" rx="18" fill="#fee2e2" stroke="#dc2626" stroke-width="3"/>
    <text x="700" y="560" font-size="30" font-weight="800" fill="#991b1b">网关与工具</text>
    <text x="700" y="612" font-size="23" fill="#991b1b">Higress AI Gateway</text>
    <text x="700" y="652" font-size="23" fill="#991b1b">LLM Provider · MCP Server</text>
    <text x="700" y="692" font-size="23" fill="#991b1b">Consumer Key · Route Auth</text>

    <rect x="1180" y="500" width="540" height="250" rx="18" fill="#e0f2fe" stroke="#0284c7" stroke-width="3"/>
    <text x="1215" y="560" font-size="30" font-weight="800" fill="#075985">运行时容器 / Pod</text>
    <text x="1215" y="612" font-size="23" fill="#075985">Manager: OpenClaw / QwenPaw</text>
    <text x="1215" y="652" font-size="23" fill="#075985">Workers: OpenClaw · QwenPaw/CoPaw · Hermes</text>
    <text x="1215" y="692" font-size="23" fill="#075985">Docker backend · Kubernetes backend</text>

    <defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#334155"/></marker></defs>
    <path d="M420 295 H505" stroke="#334155" stroke-width="4" marker-end="url(#arrow)"/>
    <path d="M945 295 H1030" stroke="#334155" stroke-width="4" marker-end="url(#arrow)"/>
    <path d="M1375 400 V500" stroke="#334155" stroke-width="4" marker-end="url(#arrow)"/>
    <path d="M1180 625 H1095" stroke="#334155" stroke-width="4" marker-end="url(#arrow)"/>
    <path d="M665 625 H580" stroke="#334155" stroke-width="4" marker-end="url(#arrow)"/>
    <path d="M725 400 V500" stroke="#334155" stroke-width="4" marker-end="url(#arrow)"/>
    <path d="M325 500 V400 H245" stroke="#334155" stroke-width="4" marker-end="url(#arrow)"/>
  </g>
</svg>'''


def workflow_svg() -> str:
    labels = [
        ("1", "创建 Worker CR", "人类/Manager/agt 声明期望资源"),
        ("2", "Provision Infra", "Matrix 账号、房间、MinIO 用户、Gateway consumer"),
        ("3", "Deploy Config", "openclaw.json / runtime.yaml / AGENTS / skills / MCP"),
        ("4", "Create Runtime", "Docker 容器或 Kubernetes Pod"),
        ("5", "Assign Task", "写 shared/tasks，再在正确房间 @mention"),
        ("6", "Execute & Sync", "Worker 执行、写 progress/result、同步对象存储"),
        ("7", "Collect Result", "Manager 读取结果、更新 meta/state、通知人类"),
    ]
    x0, gap = 80, 238
    steps = []
    arrows = []
    for i, (n, title, sub) in enumerate(labels):
        x = x0 + i * gap
        steps.append(f'''<g>
  <rect x="{x}" y="265" width="200" height="230" rx="22" fill="#ffffff" stroke="#0f766e" stroke-width="3"/>
  <circle cx="{x+100}" cy="320" r="36" fill="#0f766e"/><text x="{x+90}" y="333" font-family="Arial" font-size="34" font-weight="800" fill="#ffffff">{n}</text>
  <text x="{x+28}" y="385" font-family="Noto Sans SC, PingFang SC, Arial" font-size="24" font-weight="800" fill="#0f172a">{esc(title)}</text>
  <foreignObject x="{x+24}" y="410" width="152" height="70"><div xmlns="http://www.w3.org/1999/xhtml" style="font-family:Noto Sans SC,PingFang SC,Arial;font-size:18px;line-height:1.45;color:#475569;text-align:center">{esc(sub)}</div></foreignObject>
</g>''')
        if i < len(labels) - 1:
            arrows.append(f'<path d="M{x+200} 380 H{x+gap}" stroke="#334155" stroke-width="4" marker-end="url(#arrow)"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="760" viewBox="0 0 1800 760" role="img" aria-labelledby="title desc">
  <title id="title">AgentTeams Worker 生命周期流程</title><desc id="desc">从创建 Worker CR 到执行任务并收集结果的流程。</desc>
  <rect width="1800" height="760" fill="#f8fafc"/>
  <defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#334155"/></marker></defs>
  <text x="72" y="88" font-family="Noto Sans SC, PingFang SC, Arial" font-size="42" font-weight="800" fill="#0f172a">Worker 生命周期：声明式收敛 + 房间任务流</text>
  <text x="72" y="130" font-family="Noto Sans SC, PingFang SC, Arial" font-size="22" fill="#475569">控制器负责身份、房间、网关、配置和容器；Manager 负责任务登记、通知、结果收集和人类同步。</text>
  {''.join(arrows)}
  {''.join(steps)}
  <rect x="80" y="590" width="1640" height="80" rx="18" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
  <text x="112" y="640" font-family="Noto Sans SC, PingFang SC, Arial" font-size="24" font-weight="700" fill="#075985">关键原则：先写共享文件，再 @mention；Worker 完成后 Manager 必须读取 result、更新 meta/state、写 memory，再通知人类。</text>
</svg>'''


def runtime_svg() -> str:
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="920" viewBox="0 0 1800 920" role="img" aria-labelledby="title desc">
  <title id="title">OpenClaw 与 Hermes 的协作关系</title><desc id="desc">展示 AgentTeams 中 OpenClaw、QwenPaw 和 Hermes 的角色分工。</desc>
  <rect width="1800" height="920" fill="#f8fafc"/>
  <text x="72" y="86" font-family="Noto Sans SC, PingFang SC, Arial" font-size="42" font-weight="800" fill="#0f172a">OpenClaw / QwenPaw / Hermes：不是替代，而是分工</text>
  <text x="72" y="126" font-family="Noto Sans SC, PingFang SC, Arial" font-size="22" fill="#475569">AgentTeams 用统一房间、文件、凭据和生命周期控制，把不同 runtime 组织成可协作的团队。</text>
  <g font-family="Noto Sans SC, PingFang SC, Arial">
    <rect x="110" y="220" width="390" height="520" rx="24" fill="#dbeafe" stroke="#2563eb" stroke-width="3"/>
    <text x="150" y="285" font-size="34" font-weight="800" fill="#1e3a8a">OpenClaw</text>
    <text x="150" y="335" font-size="24" font-weight="700" fill="#1e3a8a">适合：Manager / Team Leader</text>
    <text x="150" y="392" font-size="22" fill="#1e40af">多渠道入口</text>
    <text x="150" y="432" font-size="22" fill="#1e40af">Matrix 房间协议</text>
    <text x="150" y="472" font-size="22" fill="#1e40af">技能和任务管理</text>
    <text x="150" y="512" font-size="22" fill="#1e40af">Heartbeat 与恢复路径</text>
    <text x="150" y="552" font-size="22" fill="#1e40af">协调 Worker 和人类决策</text>

    <rect x="705" y="205" width="390" height="550" rx="24" fill="#ecfeff" stroke="#0891b2" stroke-width="3"/>
    <text x="745" y="270" font-size="34" font-weight="800" fill="#155e75">AgentTeams</text>
    <text x="745" y="320" font-size="24" font-weight="700" fill="#155e75">统一协作层</text>
    <text x="745" y="378" font-size="22" fill="#155e75">Matrix 身份和房间</text>
    <text x="745" y="418" font-size="22" fill="#155e75">MinIO/OSS 任务文件</text>
    <text x="745" y="458" font-size="22" fill="#155e75">Higress 模型和 MCP 网关</text>
    <text x="745" y="498" font-size="22" fill="#155e75">CRD + Reconciler</text>
    <text x="745" y="538" font-size="22" fill="#155e75">runtime.yaml / openclaw.json</text>
    <text x="745" y="578" font-size="22" fill="#155e75">Docker / Kubernetes backend</text>

    <rect x="1300" y="220" width="390" height="520" rx="24" fill="#fef3c7" stroke="#d97706" stroke-width="3"/>
    <text x="1340" y="285" font-size="34" font-weight="800" fill="#92400e">Hermes</text>
    <text x="1340" y="335" font-size="24" font-weight="700" fill="#92400e">适合：自治执行 Worker</text>
    <text x="1340" y="392" font-size="22" fill="#92400e">代码和自动化长任务</text>
    <text x="1340" y="432" font-size="22" fill="#92400e">容器内 YOLO 执行</text>
    <text x="1340" y="472" font-size="22" fill="#92400e">.hermes 状态与策略</text>
    <text x="1340" y="512" font-size="22" fill="#92400e">读取共享任务目录</text>
    <text x="1340" y="552" font-size="22" fill="#92400e">写 result / progress 回存储</text>

    <defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#334155"/></marker></defs>
    <path d="M500 445 H705" stroke="#334155" stroke-width="5" marker-end="url(#arrow)"/>
    <path d="M1095 445 H1300" stroke="#334155" stroke-width="5" marker-end="url(#arrow)"/>
    <path d="M1300 600 C1120 815 670 815 500 600" fill="none" stroke="#334155" stroke-width="5" marker-end="url(#arrow)"/>
    <text x="548" y="420" font-size="21" font-weight="700" fill="#334155">分解任务 / 协调</text>
    <text x="1138" y="420" font-size="21" font-weight="700" fill="#334155">统一协议 / 凭据</text>
    <text x="750" y="840" font-size="21" font-weight="700" fill="#334155">产物、进度和状态回流</text>
  </g>
</svg>'''


def write_assets() -> None:
    base = ROOT / "images/posts" / POST.slug
    write(base / "cover.svg", cover_svg())
    write(base / "architecture.svg", architecture_svg())
    write(base / "workflow.svg", workflow_svg())
    write(base / "runtime-collaboration.svg", runtime_svg())


def build_article_page() -> None:
    template_path = ROOT / PREV_EXISTING_URL.strip("/") / "index.html"
    template = template_path.read_text(encoding="utf-8")
    start = template.find('<article class="post">')
    end = template.find("</article>", start) + len("</article>")
    if start == -1 or end == -1:
        raise RuntimeError("article template not found")
    head, tail = template[:start], template[end:]
    replacements = {
        r"<title>.*?</title>": f"<title>{esc(POST.title)} - zcxGGmu's Blog</title>",
        r'<meta name="description" content="[^"]*">': f'<meta name="description" content="{esc(POST.desc)}">',
        r'<meta property="og:url" content="[^"]*">': f'<meta property="og:url" content="{esc(POST.full_url)}">',
        r'<meta property="og:title" content="[^"]*">': f'<meta property="og:title" content="{esc(POST.title)}">',
        r'<meta property="og:description" content="[^"]*">': f'<meta property="og:description" content="{esc(POST.desc)}">',
        r'<link rel="canonical" href="[^"]*">': f'<link rel="canonical" href="{esc(POST.full_url)}">',
    }
    for pattern, repl in replacements.items():
        head = re.sub(pattern, repl, head, count=1, flags=re.S)
    article = f'''<article class="post"><div class="post-head-wrapper" style="background-image:url('{POST.cover}')"><div class="post-title">{esc(POST.title)}<div class="post-subtitle">{esc(POST.desc)}</div><div class="post-meta"><time itemprop="datePublished">{DATE}</time>&nbsp;&nbsp;{meta_links(POST)}</div></div></div><div class="post-body-wrapper"><div class="post-body" v-pre>{POST.body}</div></div><nav class="post-pagination"><a class="newer-posts">下一篇<br>没有更新的文章</a><a class="older-posts" href="{PREV_EXISTING_URL}">上一篇<br>{esc(PREV_EXISTING_TITLE)}</a></nav>
    </article>'''
    tail = re.sub(r'<div class="toc-wrapper">.*?</div></div>', build_toc(POST.body), tail, count=1, flags=re.S)
    write(ROOT / "2026" / POST.slug / "index.html", head + article + tail)


def update_existing_previous() -> None:
    path = ROOT / PREV_EXISTING_URL.strip("/") / "index.html"
    text = path.read_text(encoding="utf-8")
    text = re.sub(
        r'<a class="newer-posts">下一篇<br>没有更新的文章</a>|<a class="newer-posts" href="[^"]+">下一篇<br>.*?</a>',
        f'<a class="newer-posts" href="{POST.url_path}">下一篇<br>{esc(POST.title)}</a>',
        text,
        count=1,
        flags=re.S,
    )
    write(path, text)


def home_card() -> str:
    return f'''<a href="{POST.url_path}" class="a-block">
      <div class="post-item-wrapper ">
        <div class="post-item post-item-no-divider">
          <div class="post-item-info-wrapper">
            <div class="post-item-title">{esc(POST.title)}</div>
            <div class="post-item-summary">{esc(POST.desc)}</div>
            <div class="post-item-meta">{DATE}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {POST.minutes} min&nbsp;&nbsp;</div>
          </div>
          <div class="post-item-image-wrapper"><div class="post-item-image" style="background-image:url('{POST.cover}')"></div></div>
        </div>
      </div>
    </a>'''


def update_home() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    text = re.sub(rf'<a href="{re.escape(POST.url_path)}" class="a-block">.*?</a>\s*', "", text, flags=re.S)
    pos = text.find(f'<a href="{PREV_EXISTING_URL}" class="a-block">')
    if pos == -1:
        raise RuntimeError("homepage insertion marker not found")
    write(path, text[:pos] + home_card() + "\n" + text[pos:])


def update_rss() -> None:
    path = ROOT / "index.xml"
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"<lastBuildDate>.*?</lastBuildDate>", f"<lastBuildDate>{format_datetime(BASE_DT)}</lastBuildDate>", text, count=1)
    text = re.sub(rf"<item>\s*<title>{re.escape(esc(POST.title))}</title>.*?</item>\s*", "", text, flags=re.S)
    item = f'''<item>
<title>{esc(POST.title)}</title>
<link>{POST.full_url}</link>
<guid>{POST.full_url}</guid>
<pubDate>{format_datetime(BASE_DT)}</pubDate>
<description>{esc(POST.desc)}</description>
</item>
'''
    write(path, text.replace("<item>", item + "<item>", 1))


def update_archive() -> None:
    path = ROOT / "archive/index.html"
    text = path.read_text(encoding="utf-8")
    inserted = POST.url_path not in text
    text = re.sub(rf'<div style="padding:8px 0;font-size:15px">\s*<span style="color:#999">{DATE}</span>&nbsp;\s*<a href="{re.escape(POST.url_path)}">.*?</div>\s*', "", text, flags=re.S)
    if inserted:
        text = re.sub(
            r'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">(\d+) 篇</span>',
            lambda m: f'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">{int(m.group(1)) + 1} 篇</span>',
            text,
            count=1,
        )
    item = f'''<div style="padding:8px 0;font-size:15px">
        <span style="color:#999">{DATE}</span>&nbsp;
        <a href="{POST.url_path}">{esc(POST.title)}</a>
        <span style="margin-left:10px"><span style="color:#999;font-size:12px">{esc(POST.category)}</span></span>
      </div> '''
    pos = text.find(f'<a href="{PREV_EXISTING_URL}">')
    start = text.rfind('<div style="padding:8px 0;font-size:15px">', 0, pos)
    if start == -1:
        raise RuntimeError("archive insertion marker not found")
    write(path, text[:start] + item + text[start:])


def tax_item() -> str:
    return f'''<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">
        <a href="{POST.url_path}" style="font-size:16px;text-decoration:none">{esc(POST.title)}</a>
        <span style="color:#999;font-size:13px;margin-left:10px">{DATE}</span>
      </div> '''


def update_term_index(kind: str, term: str, delta: int) -> None:
    if not delta:
        return
    path = ROOT / kind / "index.html"
    text = path.read_text(encoding="utf-8")
    hrefs = [f"/{kind}/{quote(term)}/", f"/{kind}/{term}/"]
    replaced = False
    for href in hrefs:
        if href in text:
            pattern = re.compile(rf'(<a href="{re.escape(href)}"[^>]*>{re.escape(esc(term))}<span[^>]*>\()(\d+)(\)</span></a>)')
            text, count = pattern.subn(lambda m: f"{m.group(1)}{int(m.group(2)) + delta}{m.group(3)}", text, count=1)
            if count:
                replaced = True
                break
    if not replaced:
        href = f"/{kind}/{quote(term)}/"
        if kind == "tags":
            item = f'<a href="{href}" style="display:inline-block;margin:5px 8px;padding:4px 12px;background:rgba(25,118,210,0.06);border-radius:4px;font-size:15px">{esc(term)}<span style="color:#999;font-size:12px;margin-left:4px">({delta})</span></a>\n'
        else:
            item = f'<a href="{href}" class="a-block" style="padding:8px 0;font-size:18px">{esc(term)}<span style="color:#999;margin-left:8px">({delta})</span></a>\n'
        pos = text.find("</div></div></div>")
        text = text[:pos] + item + text[pos:]
    write(path, text)


def update_term(kind: str, term: str, prefix: str, emoji: str) -> None:
    path = ROOT / kind / term / "index.html"
    if path.exists():
        original = path.read_text(encoding="utf-8")
        text = re.sub(rf'<div style="padding:12px 0;border-bottom:1px solid rgba\(128,128,128,0\.08\)">\s*<a href="{re.escape(POST.url_path)}".*?</div>\s*', "", original, flags=re.S)
        inserted = 1 if POST.url_path not in original else 0
        if inserted:
            text = re.sub(r"共 (\d+) 篇文章", lambda m: f"共 {int(m.group(1)) + inserted} 篇文章", text, count=1)
        marker = '<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">'
        first = text.find(marker)
        if first == -1:
            first = text.find("</div></div></div>")
        text = text[:first] + tax_item() + text[first:]
    else:
        inserted = 1
        label = f"{prefix}: {term}" if prefix else term
        h1 = f"{emoji} {term}" if emoji else label
        text = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#f8fafc"><meta name="description" content="{esc(label)}"><meta property="og:title" content="{esc(label)} - zcxGGmu's Blog"><link rel="canonical" href="{SITE}/{kind}/{quote(term)}/"><link rel="stylesheet" href="/scss/journal.min.css"><link rel="stylesheet" href="/scss/modern.min.css?v=20260607-sidebar-collapse"><title>{esc(label)} - zcxGGmu's Blog</title></head><body><div class="stream-container"><div class="post-list-container" style="min-height:100vh"><div style="padding:40px 35px"><h1 style="font-size:30px;font-weight:500;margin-bottom:10px">{esc(h1)}</h1><p style="color:#999;margin-bottom:30px">共 1 篇文章</p>{tax_item()}</div></div></div><script src="/js/journal.js"></script></body></html>'''
    write(path, text)
    update_term_index(kind, term, inserted)


def update_taxonomies() -> None:
    update_term("categories", POST.category, "分类", "")
    update_term("series", POST.series, "", "📚")
    for tag in POST.tags:
        update_term("tags", tag, "标签", "🏷️")


def copy_script_and_manifest() -> None:
    target = ROOT / "tasks" / SCRIPT_NAME
    shutil.copyfile(Path(__file__), target)
    rec(target)
    manifest = ROOT / "tasks" / MANIFEST_NAME
    manifest.write_text(json.dumps(sorted(CHANGED | {f"tasks/{MANIFEST_NAME}"}), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    rec(manifest)


def plain_text_len(body: str) -> int:
    text = re.sub(r"<[^>]+>", "", body)
    text = html.unescape(text)
    return len(re.sub(r"\s+", "", text))


def validate() -> None:
    article = ROOT / "2026" / POST.slug / "index.html"
    html_text = article.read_text(encoding="utf-8")
    assert POST.title in html_text
    assert plain_text_len(POST.body) > 6500
    h2_ids = re.findall(r'<h2 id="([^"]+)">', POST.body)
    toc_ids = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', html_text)
    assert h2_ids == toc_ids, (h2_ids, toc_ids)
    required = ["agentteams-controller", "WorkerReconciler", "Manager", "Worker", "Team", "Human", "Matrix", "Tuwunel", "Higress", "MinIO", "OpenClaw", "Hermes", "QwenPaw", "runtime.yaml", "AGENTS.md"]
    missing = [word for word in required if word not in html_text]
    assert not missing, missing
    forbidden = ["本文转述", "原视频", "视频里", "视频中", "UP主", "up主", "这期", "本期", "作者说", "他提到"]
    bad = [word for word in forbidden if word in html_text]
    assert not bad, bad
    for asset in ["cover.svg", "architecture.svg", "workflow.svg", "runtime-collaboration.svg"]:
        ET.parse(ROOT / "images/posts" / POST.slug / asset)
    ET.parse(ROOT / "index.xml")
    home = (ROOT / "index.html").read_text(encoding="utf-8")
    order = re.findall(r'<a href="(/2026/[^"]+/)" class="a-block">', home)[:7]
    expected = [
        "/2026/codeinsights-local-first-agent-workbench/",
        "/2026/what-you-need-to-learn-from-claw-code-repo/",
        "/2026/gaojingqi-investment-system/",
        "/2026/ai-revolution-permanent-underclass-career-selection/",
        "/2026/live-longer-than-earn-fast-investment-infinite-game/",
        POST.url_path,
        PREV_EXISTING_URL,
    ]
    assert order == expected, order
    for kind, terms in {
        "categories": [POST.category],
        "series": [POST.series],
        "tags": POST.tags,
    }.items():
        for term in terms:
            assert POST.url_path in (ROOT / kind / term / "index.html").read_text(encoding="utf-8"), (kind, term)
    manifest = json.loads((ROOT / "tasks" / MANIFEST_NAME).read_text(encoding="utf-8"))
    missing_files = [p for p in manifest if not (ROOT / p).exists()]
    assert not missing_files, missing_files
    pycache = list(ROOT.rglob("__pycache__")) + list(ROOT.rglob("*.pyc"))
    assert not pycache, [p.as_posix() for p in pycache[:5]]
    print(json.dumps({
        "article": POST.full_url,
        "title": POST.title,
        "chars": plain_text_len(POST.body),
        "h2_count": len(h2_ids),
        "manifest_count": len(manifest),
        "homepage_first_7": order,
    }, ensure_ascii=False, indent=2))


def main() -> None:
    if not (ROOT / PREV_EXISTING_URL.strip("/") / "index.html").exists():
        raise SystemExit(f"publish root is missing previous article: {ROOT}")
    write_assets()
    build_article_page()
    update_existing_previous()
    update_home()
    update_rss()
    update_archive()
    update_taxonomies()
    copy_script_and_manifest()
    validate()


if __name__ == "__main__":
    main()
