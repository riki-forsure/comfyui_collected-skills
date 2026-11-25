# 2026-11-26 每日生图社区发现

- **北京时间与时间窗**：11 月 26 日 04:00 开始。承接 11 月 25 日约 04:02–04:03 的列表水位至本次 04:00–04:02 抽查，随后补读原文、版本和画面。日期除另标均按北京时间。
- **检索类型**：无具体差距要求的每日广泛发现。
- **执行状态**：已执行，精选 8 项。Reddit 最新列表、B 站字幕与部分作品配方受限。查阅与视读范围见各条。编译／加载、复跑、成图、收益验证及用户认可均未执行或未取得。
- 本文为中文整理与导读。感谢原作者、维护者及社区分享者，请回原文阅读完整配置、例图和后续更新，并遵循来源条款。

## 今日值得阅读

SnapRef v2s PRE1 新增纯画风参考。Krea 工作流用文字表达重心、视线与机位，World Streets 则直接用深度底稿约束街景布局。另收录 MOSS 两阶段采样、MiniMax H3 扩图、Kandinsky 分块放大、NVIDIA 首发模型，以及 Sena404 的葵渚标签实测。

## 分享速查

| 类别 | 分享／资源 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点 | 读取与验证状态 |
|---|---|---|---|---|---|---|
| 模型发布 | [Nemotron-Labs-Image-30B-A3B 首发范围](#n01) | 模型选型·图像生成｜查清栅格模型与官方基准的发布范围。 | — | NVIDIA Nemotron Labs · [固定模型卡](https://huggingface.co/nvidia/Nemotron-Labs-Image-30B-A3B/blob/d7c2ba6a59a384080f0bdd5b1e846da03804cdd1/README.md) · [许可证](https://huggingface.co/nvidia/Nemotron-Labs-Image-30B-A3B/blob/d7c2ba6a59a384080f0bdd5b1e846da03804cdd1/LICENSE) | 30B 总参数、约 3B 激活参数的自回归图像模型，首发开放栅格生成组件。 | 固定模型卡、提交及许可 |
| 放大模型 | [Kandinsky ImageSR 2.0 单步分块放大](#n02) | 图像放大·边缘衔接｜比较同一权重的两倍和四倍分块放大。 | 设计思路：分块融合｜以重叠分块和加权融合处理大画幅接缝。 | Kandinsky Lab · [固定模型卡](https://huggingface.co/kandinskylab/Kandinsky-ImageSR-2.0/blob/7d5b5ed7def0b45b98f398c0b295a6b1658863db/README.md) | 同一权重支持 ×2／×4，用预计算的条件表替代文字条件。 | 模型卡、元数据和公开示例配置 |
| 扩图 LoRA | [MiniMax H3 Image Outpaint LoRA v1 与原图回贴](#n03) | 扩图修图·构图控制｜在原图四周补画并保留可回贴的区域。 | 设计思路：边缘扩展·构图校正｜灰底标出补绘边界，校正画幅后回贴原图。 | AusBoss · [固定模型卡](https://huggingface.co/ausboss/MiniMax-H3-Image-Outpaint-LoRA/blob/213b3deffbcc9b899c078595588b78ddb8e22f08/README.md) | 从灰底画布扩图，重点处理源图位置漂移。 | 模型卡、工作流 JSON、森林示范输入 |
| 采样工作流 | [MOSS-Image 双阶段加速 v0.1.0](#n04) | 采样精修·工作流｜拆分基础出图和高分精修两段采样。 | — | lepetitprince716355 · [教程](https://civitai.com/articles/39805) · [工作流 v0.1.0](https://civitai.com/models/3064697?modelVersionId=3489069) · [固定 API JSON](https://github.com/lepetitprince716-prog/comfyui-moss-accel/blob/08852480389a1203b5007be870febf13f59c19a5/workflows/moss_accel_two_pass.api.json) | 分开加速 fast 基础出图与 refine 精修，给出同配置和不同精修步数对照。 | 教程、版本、API JSON、一个作品画面 |
| 深度控制资源 | [World Streets underdrawings v1.0：街景深度底稿](#n05) | 构图控制·街景生成｜用地点深度底稿约束街道和地标布局。 | 设计思路：街景空间·文字组织｜深度图约束街道布局，提示词补天气与招牌。 | Tsumugi_Lab · [v1.0 资源页](https://civitai.com/models/3064332?modelVersionId=3488565) · [埃菲尔铁塔示例](https://civitai.com/images/150169727) | 386 张依据 OSM 在 Blender 搭建的深度底稿，附地点与通用招牌提示。 | 版本说明、公开设置和一张示例 |
| 姿态提示词 | [Krea Modeling Photography：把姿态写进提示词](#n06) | 构图/姿态控制·提示词组织｜把参考图或随机姿态扩写为摄影提示。 | 设计思路：姿态文字化｜把重心、四肢角度、视线和取景拆成文字约束。 | Reddit u/Intelligent-Dog9152，工作流由 zeryabshahid-ui 发布 · [原帖](https://www.reddit.com/r/StableDiffusion/comments/1y55af3/krea_modeling_photography/) · [工作流快照](https://github.com/zeryabshahid-ui/Comfyui-Workflows/tree/0b6d7471e27fc1b3929041a2a32c6bd89f2d5135) | 两份图分别从参考图／自动导演模式和姿势通配词生成姿态描述。 | 主帖、1 条可见回复、固定 JSON |
| 参考图适配器 | [SnapRef v2s PRE1：纯画风模式与多参考实践](#n07) | 人物参考·画风控制｜按参考图与文字分配角色和画风信息。 | 设计思路：人物与画风分工｜按任务切换角色模式或仅提取参考画法。 | 0ppxnhximxr／ArcAnima，视频作者技术探客 · [固定模型卡](https://huggingface.co/0ppxnhximxr/snapref-v2s/blob/c6545c1c278fe15018c5a8bf3a23c6e99810a6cb/README.md) · [实践视频](https://www.bilibili.com/video/BV1eLykzMEzL/) | 较 v2a 新增 Style 模式，视频讨论参考图数量与角色可编辑性的取舍。 | 模型卡、完整简介、P1 抽样画面 |
| 画师标签实测 | [Sena404 Anima 画师串投稿第 33 期／片内第 43 期](#n08) | 人物插画·画风搭配｜观察葵渚标签在角色服饰和光照中的表现。 | 美术风格方向：二次元人物·细线厚涂·高光材质｜大眼窄下颌，轮廓清楚，皮肤与衣料高光各异。 | Sena404，涉及画师葵渚（Aoi Nagisa） · [视频](https://www.bilibili.com/video/BV1ogykzrEHB/) · [系列索引](../2026-11-09/notes/Sena404画师串与相关分享.md) | 片头标注 20 图实测，分享葵渚标签、角色服装和结构表现。 | 完整简介、12 张 P1 抽帧、OCR 与人工对照 |

## 当日分享

<a id="n01"></a>

### Nemotron-Labs-Image-30B-A3B 首发范围

**适用方向：模型选型·图像生成｜查清栅格模型与官方基准的发布范围。**

- 原作者与原文：NVIDIA Nemotron Labs · [固定模型卡](https://huggingface.co/nvidia/Nemotron-Labs-Image-30B-A3B/blob/d7c2ba6a59a384080f0bdd5b1e846da03804cdd1/README.md) · [许可证](https://huggingface.co/nvidia/Nemotron-Labs-Image-30B-A3B/blob/d7c2ba6a59a384080f0bdd5b1e846da03804cdd1/LICENSE)
- 作者说明：11 月 25 日 05:55 提交初始发布快照，26 日 02:57 的修订 d7c2ba6 更新展示 GIF。该仓库提供图像模型、视觉 tokenizer 和推理代码。完整 VisualCreation 调度框架的发布仍待作者许可流程。
- 公开配置与条件：推理示例使用四张 H100 80GB，最低硬件要求未知。官方基准表同时报告整套系统和不同生成路径，应按表头对应。许可证的使用条款限定研究与评估。 [作者论文](https://huggingface.co/papers/2611.31358)
- 读取状态：读了发布说明、配置、基准及许可。展示图未视读，未跑推理或核实基准收益。

<a id="n02"></a>

### Kandinsky ImageSR 2.0 单步分块放大

**适用方向：图像放大·边缘衔接｜比较同一权重的两倍和四倍分块放大。**

**设计思路：分块融合｜以重叠分块和加权融合处理大画幅接缝。**

- 原作者与原文：Kandinsky Lab · [固定模型卡](https://huggingface.co/kandinskylab/Kandinsky-ImageSR-2.0/blob/7d5b5ed7def0b45b98f398c0b295a6b1658863db/README.md)
- 作者说明：11 月 24 日 16:51 建库，25 日 23:15 更新至 7d5b5ed。Diffusers 0.41 或更新版本使用 Kandinsky 5 transformer。作者预计算各时间步的条件，从推理路径移除文字编码器及对应的交叉注意力。按输出 1024 像素分块，用考虑边界的 Hanning 权重融合重叠区域。
- 公开配置：单步 one_step_t 默认 ×2 为 0.15，×4 为 0.244。作者在 H100 80GB、BF16、单块批量条件下报告 1K→2K 中位 2.78 秒、1K→4K 7.80 秒。变换器与管线为 MIT，随包的 FLUX.1 schnell VAE 来源为 Apache-2.0。
- 读取状态：读了模型卡、元数据与示例配置。示例图未视读，未核图像锐度或接缝收益。

<a id="n03"></a>

### MiniMax H3 Image Outpaint LoRA v1 与原图回贴

**适用方向：扩图修图·构图控制｜在原图四周补画并保留可回贴的区域。**

**设计思路：边缘扩展·构图校正｜灰底标出补绘边界，校正画幅后回贴原图。**

- 原作者与原文：AusBoss · [固定模型卡](https://huggingface.co/ausboss/MiniMax-H3-Image-Outpaint-LoRA/blob/213b3deffbcc9b899c078595588b78ddb8e22f08/README.md)
- 作者说明：11 月 25 日 15:41 发布 v1，23:00 补视频链接。主权重 minimax-h3-image-outpaint.safetensors 为 rank 16、step 1500。作者另提供 step 2000，称它在一张测试图上移动并重绘了原图。
- 公开配置：MiniMax H3 Image 的 Picture 1 接填 #808080 的画布。作者建议 LoRA 1.0、约 4 MP、短边 2048 像素或以下，必要时回贴原像素。工作流保存了加载强度 1.0 和 H3 专用 VAE。作者要求 AusBoss nodes 2.21.2 或以上，LoRA 沿用 H3 社区许可。
- 作者结果及本库读取：16 张留出照片中，基础模型有 6 张移动超过 2 像素，LoRA 组为 0 张。森林例的 133 像素偏移来自作者测量。本库看了该 GIF 的灰底输入画面和虚线标出的源图边界，未独立测量偏移或验证接缝。

<a id="n04"></a>

### MOSS-Image 双阶段加速 v0.1.0

**适用方向：采样精修·工作流｜拆分基础出图和高分精修两段采样。**

- 原作者与原文：lepetitprince716355 · [教程](https://civitai.com/articles/39805) · [工作流 v0.1.0](https://civitai.com/models/3064697?modelVersionId=3489069) · [固定 API JSON](https://github.com/lepetitprince716-prog/comfyui-moss-accel/blob/08852480389a1203b5007be870febf13f59c19a5/workflows/moss_accel_two_pass.api.json)
- 作者说明：11 月 26 日 01:49 发布工作流 v0.1.0，01:50 发布教程。节点分别使用 fast 与 refine 预设，依采样阶段跳步、复用或外推结果。作者把 refine 用在低去噪精修尾段。前一日另有一项 [OPD 蒸馏采样](../2026-11-25/README.md)。
- 公开配置：API JSON 的 1024×1024 基础图采 25 步，经 Lanczos 放至 1456×1456。精修 7 步、denoise 0.35，两段 CFG 2.5、er_sde／simple，保存的 seed 都是 2026102717。作者要求 ComfyUI 0.46.0 或以上，项目许可 Apache-2.0。逐图实值未知。
- 作者测试：RTX 5080、INT8 ConvRot 条件下，25+9 的常规流程中位 16.20 秒，加速后 11.36 秒。发布的 25+7 工作流为 10.58 秒，对原基线约省 35% 时间，图像相对 L2 为 0.0645。数值限于其测试条件。
- 本库读图：仅看一张暮色坐姿人物例图。本例有偏冷紫的服装、暖色轮廓光和失焦城市灯点。作品元数据未提供逐图参数，未做同种子复跑。 [作品图](https://civitai.com/images/150199716)

<a id="n05"></a>

### World Streets underdrawings v1.0：街景深度底稿

**适用方向：构图控制·街景生成｜用地点深度底稿约束街道和地标布局。**

**设计思路：街景空间·文字组织｜深度图约束街道布局，提示词补天气与招牌。**

- 原作者与原文：Tsumugi_Lab · [v1.0 资源页](https://civitai.com/models/3064332?modelVersionId=3488565) · [埃菲尔铁塔示例](https://civitai.com/images/150169727)
- 作者说明：11 月 25 日 18:35 发布 v1.0（3488565），包含 58 个国家的 90 座城市以及 30 处知名视角。作者用 OSM 建筑占地、高度标签或估值构建街道空间，以 prompts.json 组织地点和当地语言的通用招牌词。
- 公开配置：作者仅测试 Z-Image Turbo + Z-Image-Turbo-Fun-Controlnet-Union 1.0，strength 0.75、8 步、CFG 1、res_multistep／simple、1024×768。小招牌及部分语言易错，建筑高度和地标几何为近似。人物、材质和店面由模型生成。原文注明 OSM ODbL Produced Work、部分东京地标来自 PLATEAU、Noto Sans CJK 为 SIL OFL 1.1。
- 本库读图：仅看埃菲尔铁塔示例，本例有居中地标、横向河岸和逆光前景剪影。该张的深度底稿及逐图提示未取得，作品元数据未提供生成实值。未读底稿压缩包。

<a id="n06"></a>

### Krea Modeling Photography：把姿态写进提示词

**适用方向：构图/姿态控制·提示词组织｜把参考图或随机姿态扩写为摄影提示。**

**设计思路：姿态文字化｜把重心、四肢角度、视线和取景拆成文字约束。**

- 原作者与原文：Reddit u/Intelligent-Dog9152，工作流由 zeryabshahid-ui 发布 · [原帖](https://www.reddit.com/r/StableDiffusion/comments/1y55af3/krea_modeling_photography/) · [工作流快照](https://github.com/zeryabshahid-ui/Comfyui-Workflows/tree/0b6d7471e27fc1b3929041a2a32c6bd89f2d5135)
- 作者说明：11 月 25 日检索到原帖，原页显示相对时间。GitHub 配套提交同日 15:29，固定版本 0b6d747。Krea Model 的 Custom Pose 启用时由 Qwen3-VL 4B 读参考图的动作与机位，关闭时从人物、服装、场景生成动作。另一份图用 __modelposes__ 随机抽取姿势，再用 VLM 扩写。两份图都用语言条件引导，作者提醒复杂手部姿态误差更明显。
- 公开配置：Krea 2 Turbo INT8 ConvRot、4-step LoRA、Qwen3-VL 4B FP8 scaled、Qwen Image VAE、4 步／CFG 1／Euler simple／1024×1024。两份 JSON 的采样器设置相符，均为随机种子模式。逐图 seed 未取得。依赖和可编辑的系统提示见原帖及工作流。
- 社区反馈及读取：一条可见回复认可用 VLM 组织动作文字的做法，未提供复跑证据。读了主帖和两份工作流 JSON，未视读出图或验证姿态精度。

<a id="n07"></a>

### SnapRef v2s PRE1：纯画风模式与多参考实践

**适用方向：人物参考·画风控制｜按参考图与文字分配角色和画风信息。**

**设计思路：人物与画风分工｜按任务切换角色模式或仅提取参考画法。**

- 原作者与原文：0ppxnhximxr／ArcAnima，视频作者技术探客 · [固定模型卡](https://huggingface.co/0ppxnhximxr/snapref-v2s/blob/c6545c1c278fe15018c5a8bf3a23c6e99810a6cb/README.md) · [实践视频](https://www.bilibili.com/video/BV1eLykzMEzL/)
- 作者说明：11 月 24 日 00:11 建库，14:47 更新到 c6545c1。v2s PRE1 新增 Style 模式，让人物来自文字，参考图影响线条、颜色和光影。Character & Style 与 Character 延续 v2a 行为，Style 多图未纳入作者的正式评估。此前版本见 [v2a stable](../2026-11-09/README.md) 与 [v2a 社区教程](../2026-11-14/README.md)。
- 公开配置：卡片示范是 Anima base v1.0、CFG 4.5、Euler／simple、28 步、Fidelity 1.0。权重名 snapref_v2s_pre1.safetensors，另有 FP8 版本，作者提示 Style 模式下两者可能略有差别。
- 视频作者说明：11 月 25 日 20:10 投稿称多图可能增强风格约束，也可能加大换衣难度。这次视频示范省略质量标签。P1 05:44 抽 11 张短边 480 的画面，OCR 辅助辨识节点并对照画面。约 01:45 可见 Character & Style／Character 两张参考图并列，Strength 与 Fidelity 面板显示 1.00。逐图完整提示与采样实值未取得。
- 读取状态：读了完整简介、模型卡及抽样节点画面。平台字幕、ASR、评论和附件未读，未复跑角色、换衣或画风对照。

<a id="n08"></a>

### Sena404 Anima 画师串投稿第 33 期／片内第 43 期

**适用方向：人物插画·画风搭配｜观察葵渚标签在角色服饰和光照中的表现。**

**美术风格方向：二次元人物·细线厚涂·高光材质｜大眼窄下颌，轮廓清楚，皮肤与衣料高光各异。**

- 原作者与原文：Sena404，涉及画师葵渚（Aoi Nagisa） · [视频](https://www.bilibili.com/video/BV1ogykzrEHB/) · [系列索引](../2026-11-09/notes/Sena404画师串与相关分享.md)
- 日期与作者说明：11 月 25 日 20:41:01，BV1ogykzrEHB，P1 CID 43916198250。投稿标题编号 33，片头编号 43。片头与中段画面对照核对标签 `@aoi nagisa \(metalder\)`。片内文字称测试 20 图，并提到正脸与半正脸较稳，极端姿态、背面与交叠手部容易出错。
- 本库观察：以 00:00–00:52 抽帧覆盖到的不同角色为范围。多帧可见醒目的虹膜和较窄下颌，鼻口相对小。有克制的正视表情，也有约 00:05 的夸张张口。多张半身或近全身示例强调胸腰体量和收腰，短裤与裙装示例显示较有体量的大腿。前倾、交腕、转身等按画面角色变化。可见较细轮廓和块面阴影，几例可见皮肤与亮面衣料的不同高光。头身及肩胯数值未测量。
- 读取状态：完整简介为短横线。P1 53 秒，480×852，每 5 秒抽帧加片尾共 12 张。OCR 仅辅助，标签及期号经画面对照。请求 zh-CN 平台轨收到登录要求。音频／ASR、评论、实际模型文件、采样参数和完整正负提示均未取得。

## 来源覆盖与检索记录

| 平台 | 实际入口／覆盖 | 读取结果与限制 |
|---|---|---|
| 百度贴吧 stablediffusion | aiotieba 4.8.2 CREATE 第 1 页 30 条。去置顶后最新 11 月 26 日 01:11，页末 24 日 00:03，跨上期水位。带空格 stable diffusion 入口解析到 stable 吧，返回两条 2018 年公告。 | 全站最新补查“工作流 提示词”“模型 LoRA”“教程 分享”，各 1 页分别 26、30、26 条，含其它吧及旧帖。按 tid 合并，再读 [Anima 局部重绘](https://tieba.baidu.com/p/11228030331)、[Krea 多主体讨论](https://tieba.baidu.com/p/11229520931) 与 [个人 LoRA](https://tieba.baidu.com/p/11229899208) 首楼和可见回复。多人帖有 OpenPose 建议，配置与结果未取得。图与楼中楼未读，本范围未精选。 |
| 百度贴吧 comfyui | 同主工具独立查 CREATE 第 1 页 27 条。去置顶后最新 11 月 26 日 02:29，页末 21 日 10:07，跨上期水位。 | 读 [H3 模型路径求助](https://tieba.baidu.com/p/11227066899) 5 楼文字，回帖建议先识别截图中的 Z-Image Turbo 与 H3，未取得可归档的作者完整配置，本范围未精选。两吧主工具成功，未启用 Astron。 |
| bilibili 广泛发现 | SDK 17.4.2 pubdate：ComfyUI 教程页 1–8 共 160 个原始条目，最早至 11 月 25 日 15:30，未到上期约 04:03 水位。Anima 生图、生图模型、LoRA 画风各查第 1 页 20 条，覆盖不同日期范围。 | 按 BV 去重，读 N07、N08 和 [MOSS 低显存训练第 4 段](https://www.bilibili.com/video/BV1BAy6zBEea/)及 [H3 视频教程](https://www.bilibili.com/video/BV1LqyazVEMa/)完整简介。MOSS 的 2.47G 峰值仅见作者简介，后一视频仅简介。两条未核画面、参数或准确讲解。LoRA 画风结果偏旧。按需抽帧 N07／N08，未读取平台评论或音频。 |
| bilibili Sena404 | UID 341674866 最新投稿第 1 页 30 条，跨度 10 月 18 日至 11 月 25 日。本次取到上期已收录水位之后的 1 条新投稿。 | 最新 BV1ogykzrEHB。已读 P1 53 秒的抽帧和 OCR，核对葵渚标签和双编号，指定字幕轨请求要求登录。见 [系列索引](../2026-11-09/notes/Sena404画师串与相关分享.md)。 |
| Reddit | r/StableDiffusion、r/comfyui 原生 newest JSON 都返回 403，改用索引交叉查 workflow、LoRA、prompt 和近期模型，按可用原帖读取。 | Krea 原帖及 1 条可见回复可读。另检索到 [NVIDIA 使用讨论](https://www.reddit.com/r/StableDiffusion/comments/1y5fb75/for_anyone_wondering_about_nvidia/)作为线索，本轮以官方卡为模型记录依据。两版面完整最新列表和评论未取得。 |
| Hugging Face | text-to-image 最新 80、image-to-image 最新 30，Anima／Illustrious／NoobAI 各 15，随后追官方与作者准确版本。 | 读 NVIDIA、Kandinsky、H3、SnapRef 卡与版本，另查看 SDMatte、Pixel32。Pixel32 已有上期条目，家族搜索含部分旧卡和误命中。 |
| GitHub | 工作流搜索 25 项，提示与节点搜索 13 项。查看作者仓库树和固定提交。 | 核对 Krea 两份工作流和 MOSS 双阶段 API JSON，另读提示节点项目文档作候选。运行器、节点兼容性和成图未验证。 |
| Civitai 文章与讨论 | Newest 30 篇。读 MOSS 双阶段、[低内存启动](https://civitai.com/articles/39799)、[唱片封套合成](https://civitai.com/articles/38589)、[ComfyVault](https://civitai.com/articles/39780)正文。 | 精选 MOSS 作者教程。公开返回了版本说明，版本评论未取得，未作评论覆盖结论。 |
| Civitai 模型、工作流和作品 | 最新模型 40、工作流 15。读 World Streets、MOSS 两阶段、[区域提示 MOSS 分支](https://civitai.com/models/3063630?modelVersionId=3488908)、[Mac 图转提示](https://civitai.com/models/3064725?modelVersionId=3489110)、[Krea Hires v2.1](https://civitai.com/models/3038832?modelVersionId=3489154)说明。 | 上述版本分别返回 4／4／0／2／1 个作品元数据项。从前两资源各看一张，未取得所视读作品的逐图元数据。区域分支的作品查询为 0，平台其它作品与配方仍未知。 |
| 补充来源 | ComfyUI 官方论坛 latest.json 返回 200，顶部仍为较旧的 LTX 等主题。note.com 的 ComfyUI 搜索返回 403。 | 论坛只读列表，本范围未精选。另循原作者模型卡、论文和仓库链接核对固定来源。 |

## 后续关注

- Sena404 最新水位为投稿第 33 期／片内第 43 期。按投稿日和 BV 去重，期号保留两列的语义。
- B 站 ComfyUI 教程仍有上次水位至 11 月 25 日 15:30 之间的分页缺口。SnapRef 多图留意模式与权重，World Streets 留意作者预告的招牌更新。
- MOSS 报告保留显卡、量化与精修步数。Krea 姿态和 H3 回贴保留输入条件；本次未验证重复性。
