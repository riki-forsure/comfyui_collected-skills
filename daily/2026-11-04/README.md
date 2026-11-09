# 2026-11-04 每日社区发现

本页整理社区作者的公开分享，感谢作者们提供模型、教程与经验。以下为本库概述，保留署名与原文链接，欢迎回原帖阅读完整内容和更新。

- 北京日期与实际检索时间：2026-11-04；03:59开始读取规范；04:00–04:10完成本轮平台检索与阅读，随后整理归档。
- 检索类型：无具体差距要求的每日广泛发现。
- 执行状态：已归档8项；Reddit近期列表、bilibili字幕及部分配置受限，实际覆盖见下表。含1项原始日期待核的Reddit历史补录，近期旧版本按真实日期另标。
- 优先时间窗：自11月3日各平台检索快照之后至本轮查询时点的新增与实质更新；近期旧资料首次收录另标原日期。保存时间不作为所有平台共同的检索边界。
- 仅阅读与摘要整理，未安装节点、下载大模型、运行生图或实验；本日没有另开主动画风专题。

## 今日值得阅读

- [P-H3-Image](https://huggingface.co/PrunaAI/P-H3-Image)：静态图像后训练与多参考编辑，区分完整模型、量化包和H3适配器路线。
- [Krea2 360 ERP](https://huggingface.co/mickmumpitz/Krea2-360-ERP-LoRAs)：将文字全景与单图投影扩展分为不同适配器，明确比例、接缝与放大条件。
- [RuiC PoseAtlas](https://github.com/shutong-queyue/ComfyUI-RuiC-PoseAtlas)：把人物、服装和姿势参考分开组织，输入顺序与降级状态写得具体。

## 分享速查

| 类别 | 分享／资源与版本 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点／可学习经验 | 读取状态 |
|---|---|---|---|---|---|---|
| 后训练／完整模型与适配器 | [D01 P-H3-Image：MiniMax-H3的静态生成与多参考编辑](#d01) | 多参考编辑·少步生成｜了解H3图像后训练、提示扩写与显存条件。 | 设计思路：修改与保留分开｜明确编辑对象、成品状态和需要保留的内容。 | [PrunaAI；基座MiniMaxAI；编码／扩写组件基于Qwen](https://huggingface.co/PrunaAI/P-H3-Image) | 作者发布基于MiniMax-H3的图像模型，提供8步生成、最多8图编辑和配套提示扩写器；另有ComfyUI完整模型、量化文件与供已有H3使用的LoRA。 | 两份模型卡全文与仓库revision；未读工作流JSON、训练实现或示范图。 |
| 后训练／用途特化LoRA | [D02 Krea2 360 ERP：文字与单图生成全景的两种LoRA](#d02) | 全景场景·扩图·Krea2｜区分文字生成与单图投影扩展的全景路线。 | 设计思路：投影与接缝处理｜使用2:1球面展开，保留地平线并整理左右接缝。 | [mickmumpitz；基座Krea；Ostris编辑补丁](https://huggingface.co/mickmumpitz/Krea2-360-ERP-LoRAs) | 作者将文字全景和单图全景扩展分为两个适配器；后者先将照片投影到等距柱状画布，以绿色标记待扩区域，再按专用指令补齐。 | 模型卡全文与revision；实际看图书馆示范1张；未读工作流JSON、未检查球面接缝。 |
| 参考图／姿态工作流 | [D03 RuiC PoseAtlas：分别选择人物、服装与姿势参考](#d03) | 人物参考·服装迁移·姿态｜分别选取三类图像并明确各自参考职责。 | 设计思路：三类参考分工｜人物管身份，衣装管穿着，姿势图管动作结构。 | [shutong-queyue；素材库HRuiCcc/RuiC-PoseAtlas；视频秝玖玟忻](https://github.com/shutong-queyue/ComfyUI-RuiC-PoseAtlas) | 作者将人像、衣装和姿势素材接成三路图像输出，配线稿／深度两套提示模板；文档明确图序、画布来源与深度转换降级状态。 | README全文及3条提交说明；视频完整简介／133秒元数据；未取得字幕、画面或实现。 |
| 提示词／标签组织 | [D04 Danbooru Anima Prompt：标签分类与多模型提示组织](#d04) | 提示词组织·标签检索｜将角色、画师和场景词分组后再组合输出。 | 设计思路：标签按职责分组｜区分身份、画师、动作与环境，保留可编辑文本。 | [Zove-try；外部标签表作者见仓库致谢](https://github.com/Zove-try/ComfyUI-Danbooru-Anima-Prompt) | 作者提供浏览、分类、映射、去重与组合节点，分别适配Anima、Noob、Aesthetic和NewBie的文本组织，支持查看最终输出。 | 固定提交README全文及3条提交说明；未调用图站、未读实现或运行节点。 |
| LoKr／训练经验 | [D05 RawSnap v3：按检查点与强度比较随拍观感](#d05) | LoKr训练·模型选型｜比较不同检查点的结构表现与随拍观感取舍。 | 设计思路：观感与结构分评｜同时观察手机随拍感和人物结构，避免只看训练步数。 | [juanjuanp](https://civitai.com/articles/37942) | 作者对749张素材训练的LoKr难以选择epoch，公开相同提示／种子的跨版本与强度比较，并邀请读者参与判断。 | 文章正文全文；未打开投票站、未看对照图或取得LoKr配置。 |
| 布局／工作流 | [D06 Compact BBox MOSS：用区域提示组织海报元素](#d06) | 多主体·海报排版·MOSS｜为人物、标题和图形分别安排区域与提示。 | 设计思路：版面与元素分区｜将人物、衣物、标题与标识拆成各自区域指令。 | [NeuralVandal](https://civitai.com/models/3035484?modelVersionId=3449147) | 作者分享紧凑的MOSS区域生成／编辑工作流，说明如何按元素分区，并特别提醒BBox交互需要Nodes 2.0。 | 模型／版本介绍与配置文件元数据；下载返回登录HTML，未读JSON或例图。 |
| 场景／Anima LoRA | [D07 Chinese Temple EE8：寺院环境的Anima适配器](#d07) | 环境插画·Anima LoRA｜查阅寺院木构、陈设与人物场景的表现案例。 | 美术风格方向：暖金寺院·动漫场景｜本例束发男子端坐，硬边衣褶与暖金木构相配。 | [MisterBones](https://civitai.com/models/3035405?modelVersionId=3449016) | 作者以寺院环境为主题发布Anima LoRA，说明用于丰富环境；首例将人物、木构、佛像和陈设放在同一室内空间。 | 模型／版本说明与文件元数据；实际看147829977一张例图；该图未返回配方。 |
| Reddit经验／局部编辑 | [D08 裁剪后重绘再拼回：小范围编辑的工作量取舍](#d08) | 局部重绘·采样精修｜只处理遮罩附近区域，再按原坐标拼回全图。 | 设计思路：编辑范围与融合分开｜采样遮罩决定重画范围，拼接边缘另管过渡。 | [Reddit u/Dave-C；AusBoss节点文档作者ausboss](https://www.reddit.com/r/comfyui/comments/1x5t61c/just_a_random_little_tip_i_want_to_throw_anyone/) | 社区作者分享裁剪遮罩周边、只编辑局部、利用stitcher拼回的方法；节点文档进一步区分采样遮罩、上下文和拼接融合。 | 帖子正文及5组相关可见回复；AusBoss README导论／遮罩局部修图章节与Crop For Inpaint帮助全文；未读实现或示例JSON。 |

## 当日分享

<a id="d01"></a>

### D01 P-H3-Image：MiniMax-H3的静态生成与多参考编辑

**适用方向：** 多参考编辑·少步生成｜了解H3图像后训练、提示扩写与显存条件。

**设计思路：修改与保留分开｜明确编辑对象、成品状态和需要保留的内容。**

- 原作者与原文：[PrunaAI / P-H3-Image](https://huggingface.co/PrunaAI/P-H3-Image)；[ComfyUI文件与使用文档](https://huggingface.co/PrunaAI/P-H3-Image-Comfy)。本库概述，首次收录。
- 日期／版本：主仓库本轮revision `7f98acef503cf2bcfba821a78cb1cf1a9928b2df`，提交2026-11-04 00:08:56 +08:00；Comfy版 `44a0fb73f299da1bb715bdb5ff59ce3fd3c6f543`，2026-11-03 23:55:08 +08:00。这些是当前版本时间，非首次发布日期。
- 作者分享要点：从视频家族派生出静态图像生成／编辑方案；8步、无CFG和负向提示，编辑时第一张为被编辑图，其余最多7张为参考。作者说明手、远处小人物和密集文字仍可能失真。
- 提示经验：编辑时指明对象与位置，描述完成后的样子，并说明人物、姿态、背景等哪些要保留；短请求可交给Qwen3.5-9B系扩写器。不能把这些专用规则推广成所有模型的通用词法。
- 配置与适用条件：Comfy文档称需已合入支持的master/nightly，稳定版尚待后续发布；没有把“原生节点”理解为任意旧版可用。量化最小模型／编码器／VAE组合约20GB下载、作者报告8MP峰值21GB显存，**另计提示扩写器文件**；扩写器在生成前后换入换出。已有MiniMax-H3 FL2VA可用另发的2GB LoRA、模型强度1.0路线，不是将量化打包另算一款新后训练。
- 读取状态：主模型卡与Comfy模型卡全文、元数据；未看示范图、未读训练实现／实际工作流JSON，所有速度、显存与质量陈述均为作者资料，未本地验证。模型卡列MiniMax H3社区许可及地域／署名条件；本轮未逐条审阅许可正文，使用前回原文核对。

<a id="d02"></a>

### D02 Krea2 360 ERP：文字与单图生成全景的两种LoRA

**适用方向：** 全景场景·扩图·Krea2｜区分文字生成与单图投影扩展的全景路线。

**设计思路：投影与接缝处理｜使用2:1球面展开，保留地平线并整理左右接缝。**

- 原作者与原文：[mickmumpitz / Krea2-360-ERP-LoRAs](https://huggingface.co/mickmumpitz/Krea2-360-ERP-LoRAs)；相关[SplatKit World流程](https://github.com/mickmumpitz/ComfyUI-SplatKit-World)。首次收录，当前revision `45b20236e1a2b98342f7db9f3a55f46b989425b2`，2026-11-03 22:31:59 +08:00；仓库创建于8月，当前提交不等于首发或本轮新增训练。
- 作者分享要点：`krea2_t2i_360_erp_lora_v1.safetensors`处理文字→360，触发 `img-txt-2-360`；`krea2_oedit_360_erp_outpaint_lora_v1.safetensors`处理照片→360，需要Ostris Edit补丁。每次选对应的一枚，不是两枚必叠。
- 作者配置：Krea2 Turbo，LoRA1.0，2048×1024，10步／CFG1，er_sde/simple。照片先投影到2:1画布并用纯绿色表示待填区；编辑补丁kv_cache开启，后接LoRA及ModelSamplingFlux（max_shift0.90625、base_shift0.5）。按卡片说明记录，未核实际JSON连接。
- 可学习经验：全景比例和投影条件先固定，再做接缝与放大；作者建议滚动画布180°处理左右接缝，分块放大提示保持中性，避免场景词在每块重复生成。采样／放大值均是此资源的建议，不是跨模型默认。
- 本库实际看图：[图书馆示范](https://huggingface.co/mickmumpitz/Krea2-360-ERP-LoRAs/blob/45b20236e1a2b98342f7db9f3a55f46b989425b2/images/text2pano_library.jpg)一张，呈现木质书架与旋梯、暖台灯和窗光，画面有球面展开形变；没有在360查看器核实左右接缝或宣称无缝已验证。
- 读取状态：模型卡全文、版本元数据、一张示范；未下载适配器、未读SplatKit实现与JSON。依Krea2社区许可，卡片提及商业规模条件；本轮仅链接，不搬运模型或图。

<a id="d03"></a>

### D03 RuiC PoseAtlas：分别选择人物、服装与姿势参考

**适用方向：** 人物参考·服装迁移·姿态｜分别选取三类图像并明确各自参考职责。

**设计思路：三类参考分工｜人物管身份，衣装管穿着，姿势图管动作结构。**

- 原作者与原文：[shutong-queyue / ComfyUI-RuiC-PoseAtlas](https://github.com/shutong-queyue/ComfyUI-RuiC-PoseAtlas)；感谢上游[HRuiCcc素材库](https://github.com/HRuiCcc/RuiC-PoseAtlas)。发现入口：[秝玖玟忻《零基础友好｜ComfyUI人像姿势库+脸型库，对着列表挑就行》](https://www.bilibili.com/video/BV1Ue4G6QEPf/)，2026-11-03 21:18:09 +08:00。
- 版本：提交 `b0799387bf4bf95cf961fd71d20e647c39c2db12`，2026-11-01 02:43:19 +08:00，修正图序并重做深度展示。本次为新视频发现后的近期资源首次收录，不把旧提交当今日更新。
- 原作者分享要点：人像→image_1、衣装→image_2、姿势→image_3，第一张人像图决定画布比例。线稿模板限制只取动作／朝向／重心；深度模板将第三图写为结构参考，避免带入人物身份与衣物。
- 配置与条件：文档使用Qwen-Image-Edit 2.1；DepthAnything V2 Small可将当前一张姿势参考转成深度。另有内置体积图／保持线稿降级路径，信息端口分别标明结果；三者不是同等证据。第三图作为编辑参考也不等于已经接入独立ControlNet硬约束。
- 实际读取范围：仓库README全文、最近3条提交说明；bilibili SDK取得完整简介、133秒时长与cid。字幕调用返回login_required，未取得字幕、画面、示范对比或节点实现，文档“更精准”等评价归原作者。
- 本库整理备注：阅读价值在参考图职责与输入顺序。素材许可独立于加载器MIT代码，回上游核对，本库未下载素材或安装插件。

<a id="d04"></a>

### D04 Danbooru Anima Prompt：标签分类与多模型提示组织

**适用方向：** 提示词组织·标签检索｜将角色、画师和场景词分组后再组合输出。

**设计思路：标签按职责分组｜区分身份、画师、动作与环境，保留可编辑文本。**

- 原作者与原文：[Zove-try / ComfyUI-Danbooru-Anima-Prompt](https://github.com/Zove-try/ComfyUI-Danbooru-Anima-Prompt)；本库概述，首次收录。[固定文档](https://github.com/Zove-try/ComfyUI-Danbooru-Anima-Prompt/blob/37fdd4b267698fadd8c10a083b1249d7edb2193a/README.md)。
- 版本：提交 `37fdd4b267698fadd8c10a083b1249d7edb2193a`，2026-11-04 03:08:42 +08:00；此次提交简化缩放节点UI，不把整个功能集说成当日新加。
- 作者分享要点：将标签拆成质量、数量、角色、系列、画师、通用与未分类，再细分身体、服装、姿势、表情和背景。按对应模型格式组合，Anima画师词加@；NewBie另有多角色创作器。去重保留原顺序，文本可编辑或透传。
- 适用条件：可选本地词表与E5-Small语义检索；文档称后者首次会下载模型并建缓存，本次未触发。不同组合器的输出规则来自作者文档，未核对每个后训练版本是否遵循同一格式。
- 读取状态：README全文、3条提交说明；未访问Danbooru／Gelbooru搜索、未看例图或读实现。插件GPL-3.0；作者明确部分随包第三方词库协议尚待核对，本库仅链接，不复制词库。

<a id="d05"></a>

### D05 RawSnap v3：按检查点与强度比较随拍观感

**适用方向：** LoKr训练·模型选型｜比较不同检查点的结构表现与随拍观感取舍。

**设计思路：观感与结构分评｜同时观察手机随拍感和人物结构，避免只看训练步数。**

- 原作者与原文：[juanjuanp《RawSnap v3 (LoKr) — help me pick the best epoch》](https://civitai.com/articles/37942)，2026-11-03 19:43:01.313 +08:00；文章37942，本次首次收录。
- 原作者分享要点：作者报告749张训练图、11,235步；部分epoch人物结构变差，另一些失去手机随拍观感，因此公开比较。文章称18组提示，每组35张，含基座Krea2、v1 ep7、v2 ep9，以及v3 ep8–15的1.0／1.2／1.5／2.0强度。
- 可学习经验：将作者要的“未修饰手机照片感”和人物结构分别观察，并在相同提示／seed下比较版本与强度。投票偏好和作者训练经验不是独立的通用画质结论，不能据步数或投票推断最佳训练配方。
- 公开程度／读取状态：API文章正文全文；投票入口由原文提供，本库未打开、未投票、未看630张比较图，也未取得精确训练器／基座revision、LoKr文件或完整超参。v3最终选择仍待作者后续公布，不写成已经发布的确定最佳epoch。

<a id="d06"></a>

### D06 Compact BBox MOSS：用区域提示组织海报元素

**适用方向：** 多主体·海报排版·MOSS｜为人物、标题和图形分别安排区域与提示。

**设计思路：版面与元素分区｜将人物、衣物、标题与标识拆成各自区域指令。**

- 原作者与原文：[NeuralVandal《Compact BBox T2I Moss Image》v1.0 / 3449147](https://civitai.com/models/3035484?modelVersionId=3449147)，发布2026-11-04 03:50:47.901 +08:00，本次新资源首次收录。
- 作者分享要点：为人物、衣服、Logo、标题、字体与图形分别写区域指令，适合杂志封面、电影海报和宣传设计；不是用一段总提示替代全部对象的分配。
- 适用条件：作者明确必须启用ComfyUI Nodes 2.0才能交互操作BBox；流程另含其Civitai Crybaby提示扫描通知节点。具体模型文件、依赖revision与采样参数尚未取得，不据资源页的MOSS分类补造。
- 公开文件：`compactBboxT2IMoss_v10.json`，文件ID3348757，元数据约30.3KiB。本次下载入口HTTP200返回标题为Civitai Login的HTML，**不是JSON取得成功**，未核实际节点图／有效分支，未将该文件保存到本库。
- 与以往关系：和[11月3日S06 MOSS YXBOX](../2026-11-03/README.md#s06)同属区域提示，但为不同作者的流程入口；本轮仅整理其文档条件，没有比较两者效果或断言节点互换。

<a id="d07"></a>

### D07 Chinese Temple EE8：寺院环境的Anima适配器

**适用方向：** 环境插画·Anima LoRA｜查阅寺院木构、陈设与人物场景的表现案例。

**美术风格方向：暖金寺院·动漫场景｜本例束发男子端坐，硬边衣褶与暖金木构相配。**

- 原作者与原文：[MisterBones《Enhanced Environment - Chinese Temple [EE 8 Anima]》V1 / 3449016](https://civitai.com/models/3035405?modelVersionId=3449016)，2026-11-04 03:54:51.488 +08:00；首次收录。
- 作者说明：Anima LoRA，目的为丰富生成图的环境，触发 `intricate environment`。文件 `EE8_Chinese_Temple.safetensors`，API约132MiB；作者未在文字中给推荐权重、精确基座或完整采样配方。
- 本库实际看图：[例图147829977](https://civitai.com/images/147829977)一张。木柱、窗棂、金色佛像和垫子组织室内纵深，暖金光与青绿窗外形成色彩层次。男子束发、眉眼偏窄长、下颌收束，盘坐衣袍用清楚阴影块塑形；仅为本例可见特征，不推广为该LoRA稳定人物画法。
- 读取范围：模型说明、版本／文件元数据与一张公开例图；所取得例图项未含提示／模型参数。不能将人物、光影与全部细节都归因于环境LoRA，未做同条件无LoRA比较。
- 本库整理备注：为广泛发现补充场景用途，资源名称与热度不单独证明环境改善；欢迎回原作者版本页查看更多示例与更新。

<a id="d08"></a>

### D08 裁剪后重绘再拼回：小范围编辑的工作量取舍

**适用方向：** 局部重绘·采样精修｜只处理遮罩附近区域，再按原坐标拼回全图。

**设计思路：编辑范围与融合分开｜采样遮罩决定重画范围，拼接边缘另管过渡。**

- 原作者与原帖：[u/Dave-C《Just a random little “tip” I want to throw anyone learning this.》](https://www.reddit.com/r/comfyui/comments/1x5t61c/just_a_random_little_tip_i_want_to_throw_anyone/)。**历史补录**：搜索索引显示2026-10-14，打开页却仅显示相对小时；本次未取得created_utc，不将其作为本轮新增或精确发布日期已核。
- 原作者经验：先画遮罩，将遮罩与周边裁出，再经Qwen等编辑／重绘模型生成局部，最后把生成局部与crop输出的stitcher接到Stitch Inpaint。提示只描述裁出区域，而非整幅画。作者在回复中报告自身小范围编辑耗时降低，未给本库可复核的整套硬件与同条件计时。
- 社区反馈：可见回复提供其他crop／stitch节点、ImageCompositeMasked和SAM3选区思路；关于Differential Diffusion兼容范围的评论未独立核验，不写成当前平台兼容结论。
- 对应原始文档：[ausboss / ComfyUI-AusBoss](https://github.com/ausboss/ComfyUI-AusBoss)；当前读取对应提交 `ded731859caeda1230182ca14d38d3645aba1a63`，2026-11-04 03:45:54 +08:00。[Crop For Inpaint帮助](https://github.com/ausboss/ComfyUI-AusBoss/blob/ded731859caeda1230182ca14d38d3645aba1a63/js/docs/AUSBOSS_NODES_CropForInpaint.md)全文已读，另读README导论与遮罩／局部修图章节；没有读整份README。最新提交为整数／浮点UI变化，不把crop功能说成今日新发。
- 作者文档解释：Context保留周边信息；mask grow／blur改变供模型采样的遮罩，Blend只影响粘回时的融合。显式目标宽高优先于像素面积设置。README称Stitch Inpaint在融合区外保留原像素，本文未读实现或实际对照，按文档陈述保留。
- 文档条件缺口：帮助正文建议Multiple32，但末尾起始值仍写8；不据此指定未经核对的“默认值”。裁剪能减少处理范围，并不自动保证接缝、色彩和人物结构。示例JSON、节点执行和视觉收益均未验证。


## 来源覆盖与检索记录

以下时间均为北京时间2026-11-04；列表计数只表示取得的发现范围，不能等同于每条正文／例图已读，也不表示平台全部新增已遍历。

| 平台／吧名 | 实际入口或查询 | 检查时间与读取范围 | 结果／限制 |
|---|---|---|---|
| stablediffusion吧 | aiotieba4.8.2／仓库只读脚本，CREATE列表第1页30条；API实际返回同名 | 04:00:19；除旧置顶外已到11月2日，跨过上轮晨间快照。读[白泽千岁MOSS训练感想](https://tieba.baidu.com/p/11163315077)第1–3楼 | 首楼11月3日18:50:19，仅说“上图”；回复求完整参数并谈个人训练习惯。未看帖子图片，未取得楼主具体rank／alpha／步数，不把回复当楼主配置。未形成可独立概括的新增训练方法，保留线索。 |
| comfyui吧 | 同工具CREATE列表第1页28条，实际返回comfyui | 04:00:19；除2条旧置顶外已到10月31日。读[Adam1213💫入门顺序求助](https://tieba.baidu.com/p/11163693915)首楼 | 求助发表于11月3日22:07:50，取得页未见解答，不写成已有入门教程。列表中的网盘整合包和纯求助未精选，不代表全吧无新增。 |
| 贴吧全站补充／别名核对 | 最新搜索“工作流 提示词 模型”“MOSS LoRA”各第1页，分别27／21条；按实际吧名筛选、tid去重 | 04:01起；关键词结果仍有10月旧帖，未当作完整时间线。04:06另用带空格“stable diffusion”做1条入口核对 | 该客户端请求实际返回**stable吧**2018年置顶，不是stablediffusion，也不是网页重定向证明；未计入目标吧覆盖。本轮目标覆盖来自单独请求的stablediffusion与comfyui。Astron未启动。 |
| bilibili | SDK17.4.2／仓库只读脚本，pubdate：“ComfyUI 教程”第1–2页、“Anima”第1页、“AI绘画 模型 提示词”第1页 | 04:00起；综合词40条范围11月3日15:13至11月4日02:19；Anima原页跨至11月2日，日期筛选后9条，排除汽车／录播等同名噪声。D03视频详情已读 | 综合词未翻到整日窗口末端，不声称穷尽。模型类别词原页只到10月31日，筛后0条是该查询无近期命中，非接口失败。D03字幕返回login_required；未取得视频画面。两个新画风标题见后续关注，仅标题／简介不补写配方。CLI未启动。 |
| Reddit | r/StableDiffusion最新50条、r/comfyui最新30条JSON；含日期的model／workflow／LoRA搜索，再以MOSS／Kroma／AusBoss等补查 | 04:00起；两列表均403，定向搜索未取得可靠本轮新帖；打开D08取得正文及5组相关可见回复 | D08为历史补录，原始日期未核。搜索给出旧日期，打开页给相对小时，明确保留冲突。未以此宣称已覆盖Reddit最新列表或平台无更新。 |
| Hugging Face | text-to-image按lastModified最新60条 | 04:00:56列表；读P-H3主卡／Comfy卡、全景卡、Kroma打包卡、MOSSArt卡；P-H3主卡及全景卡对固定revision重读一致 | 精选D01／D02；只把量化、转换打包当发布形式，非独立新训练。读图书馆示范1张；没有逐项读60份模型卡或下载权重。 |
| GitHub | ComfyUI workflow、pushed>=11月3日20条；ComfyUI prompt、created>=10月29日15条 | 04:00:57发现；D03／D04 README全文＋各3条提交说明，固定commit重读一致；AusBoss导论、遮罩／局部修图章节及Crop帮助全文 | 具体读取见D03／D04／D08；未读全部仓库、实现、示例JSON或宣称新push均为功能更新。 |
| Civitai社区／论坛 | 最新文章30条、模型／版本40条，按原链接与精确版本去重 | 04:00:56发现；RawSnap、MOSS t2i/i2i文章全文，D06／D07模型说明及版本／文件元数据；实际看D07首例 | D05／D06／D07正式精选。MOSS文章37927正文短且附件请求400，另留线索。BBox下载200实际为登录HTML，未取得JSON。未读模型评论／版本讨论，不将列表返回当作全部讨论已读。 |
| 其他论坛／作者资料 | note ComfyUI近期RSS，按主题选读两篇原文API | 04:02:58 RSS；[CHANGE/PRESERVE文章](https://note.com/tseichi/n/n800165249e44)仅公开导言，price100且can_read=false；[MOSS/Anima整合日记](https://note.com/ai_nemui/n/nb01f5737a049)免费公开正文已读 | 前者不称完整教程；后者作者たのしくねむい，11月3日19:09:54发，仍在设计整合／未公开本轮可读工作流，未精选。note站内搜索API403，RSS与单篇可读分别记录。 |

Acumen时效线索检索也已调用，返回主要为9月以前工具／版本信息；本轮未将其作为11月新增社区成果或用来替代各平台原文。

## 后续关注与更正

- [白泽千岁MOSS训练感想](https://tieba.baidu.com/p/11163315077)：首楼与两条回复已读，但图中参数未取得；图片、楼中楼和完整训练配置另核。本次没有将评论者个人“1600步／rank16”等写成楼主实值。
- bilibili[Sena404《anima画师串第二十二期》](https://www.bilibili.com/video/BV1UQ4u6kENU/)（11月3日18:18:32）、[超级无极醒目靓仔《k2接力anima形成新的画风》](https://www.bilibili.com/video/BV1j24K6JEeG/)（09:49:29）在最新搜索中发现，简介均为“-”；尚未取得视频、画师串或配方，不从标题推断实际画风和兼容性。
- 2026-11-09补充：上述Sena404第二十二期已通过用户授权的视频工具试运行取得画师标签与示范参数，见[11月9日N11](../2026-11-09/README.md#n11)及[读取范围](../2026-11-09/notes/b站云端工具试运行.md)。11月4日仅读简介的历史状态保留；另一作者视频与Sena404全系列仍未据此补称已读。
- [ccooccoo《moss image workflow! t2i and i2i》](https://civitai.com/articles/37927)，11月3日16:06:31.094发表。正文全文说明i2i需遮罩、右键进入Mask Editor；附件请求返回400，未取得实际JSON。与D06是不同作者、不同入口，不合并成已读完整工作流。
- [VD123DV / Krea-2-Kroma-v0.3.1](https://huggingface.co/VD123DV/Krea-2-Kroma-v0.3.1)模型卡全文已读：将lodestones/Kroma既有v0.3.1转换为Diffusers，且仅transformer改变。其11月3日新提交不代表Kroma当日新训练；正文明确源revision与文件SHA256，本轮不将转换仓库列为独立新后训练。
- [bunnycore / MOSSArt](https://huggingface.co/bunnycore/MOSSArt)短模型卡全文已读，基座MOSS-Image-SFT、作者建议0.2–0.4，称使用多种艺术／动漫／webtoon素材；未看例图或取得更多训练说明，不根据名称或素材类别猜人物画法。
- D05等待作者公布最终epoch；D06待公开配置可读；D08原始时间与文档Multiple默认值存在待核项。缺口不影响当前已读资料归档，也不构成已安排实验。
- 本轮先保存3项，再补成8项及完整覆盖记录；未重复报道11月3日已收录Wardrobe V5。读取、运行和效果验证分别记录，均无本地生成／复跑记录。


[返回总索引](../../每日检索可速查总结.md)
