# 2026-11-29 每日生图社区发现

- **北京时间与时间窗**：11 月 29 日 04:05 起查。承接 11 月 28 日约 04:05–04:07 的列表水位，补分页、原文、资源版本与画面。日期除另注均用北京时间。
- **检索类型**：无具体差距要求的每日广泛发现。
- **执行状态**：精选 9 项。Reddit 最新列表、Sena404 投稿入口、B 站指定字幕及部分 Civitai 评论、附件和逐图配方受限。已读范围见各条。未安装节点、加载模型、复跑、生成或验证收益，未取得用户认可。
- 感谢社区创作者、工具作者和上游维护者。本文为中文整理，请回原文查看完整说明、示范、使用条件及版本更新。

## 今日值得阅读

World Streets v3／v4 增加街道高程、二次精修和虚构招牌。Krea 2 人像实测按年龄段比较提示偏差，Impact Pack 工作流则把多个 LoRA 检查点和权重排在同一对照中。另收录 PiD 像素解码、旧照批修、H3 动作扩写、角色短片经验及 Sena404 的 piromizu 标签实测。

## 分享速查

| 类别 | 分享／资源与版本 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点／可学习经验 | 读取状态 |
|---|---|---|---|---|---|---|
| 街景深度更新 | [World Streets v3／v4：实地地形、二次精修与虚构招牌](#n01) | 构图控制·街景生成｜用同机位深度保布局，再细化路面和招牌。 | 设计思路：地形和字牌分层｜用地形承载街区布局，再单独组织大招牌文案。 | Tsumugi_Lab · [v3.0](https://civitai.com/models/3064332?modelVersionId=3491227) · [v4.0](https://civitai.com/models/3064332?modelVersionId=3492719) · [作品示例](https://civitai.com/images/150454569) | v3 新增高程与 Krea 2 精修。v4 保留同机位并改为虚构店名。 | 版本说明、两版作品元数据和 v4 两张图 |
| 人像实测 | [Krea 2 Turbo 成年人像的年龄偏差与 Human Diversity v3](#n02) | 摄影人物·提示词组织｜按年龄段观察数字和肤质词的人像偏差。 | 设计思路：年龄与肤质分评｜把要求年龄、可见纹理和估计年龄分别记入对照。 | Tsumugi_Lab · [作者实测](https://civitai.com/articles/40019) · [Human Diversity v3.0](https://civitai.com/models/3066424?modelVersionId=3491445) | 作者用固定成年肖像提示与种子比较年龄估计、多出人物和提示符合度。 | 文章正文和模型版本说明，未视读图 |
| 像素解码 | [PiD-EfficientGen：同一四步解码器的两种 QDM 写步长](#n03) | 像素解码·图像放大｜比较四步像素解码和稀疏状态写入配置。 | — | ChangyiGan／gcy-hub；NVIDIA PiD 与 PiD-QDM Halo2 作者 · [固定模型卡](https://huggingface.co/ChangyiGan/PiD-EfficientGen/blob/03e5a66f64ef13aaa6ae23fb14263987bb26f25d/README.md) · [固定运行器](https://github.com/gcy-hub/PiD-EfficientGen/tree/61fe9001e21e9c1995a1a814db83f32ca42f2c19) | Z-Image Turbo 供给低分辨率潜图，PiD 解码成宽高各四倍的 RGB。 | 固定卡、版本、稀疏 YAML 与许可说明 |
| 角色 LoRA 经验 | [Krea 2 人物 LoRA：从选图到叠加权重排查](#n04) | 人物参考·LoRA搭配｜用姿态和服装覆盖减少身份与造型绑定。 | 设计思路：形象与附属物分开｜保留稳定识别特征，让服装、机位与用光有变化。 | maxBedroom；贴吧楼主 hh131466654 与可见回帖作者 · [Creating Character LoRAs for Krea2](https://civitai.com/articles/40041) · [MOSS Base 叠加讨论](https://tieba.baidu.com/p/11238890745) | 作者分享从头像与全身配比、固定预览到风格权重排查的个人流程。 | 文章正文及独立贴吧 6 楼文字 |
| 对照工作流 | [Impact Pack 自动遍历 LoRA 检查点与强度](#n05) | 自动化工作流·LoRA搭配｜固定词和种子扫描多档权重与检查点。 | 设计思路：成组对照｜同组固定构图输入，把检查点和强度标在文件名里。 | HightekPresha；Impact Pack 作者 ltdrdata · [Automated LoRA Testing v1.0](https://civitai.com/models/3067135?modelVersionId=3492453) · [作者节点图](https://civitai.com/images/150435317) | 用倒计数器更新强度和输出命名，按检查点保留对照。 | 工作流说明与截图，附件未取得 |
| 旧照批修 | [FIBO 2 Batch Photo Restore & Upscale v1.0](#n06) | 旧照修复·批量工作流｜逐张检查方向、裁边、修复并保留目录结构。 | 设计思路：先校方向再修图｜双判定纠偏，修完再放大并逐张查小脸。 | juiceman868／Juiceman8686；基于 Pixaroma、Bria、SeedVR2 上游 · [资源 v1.0](https://civitai.com/models/3067685?modelVersionId=3493300) · [固定项目](https://github.com/Juiceman8686/ComfyUI-Fibo2-Batch-Photo-Restore/tree/574f4e05a49f6e2cbc064bb2f502ab7bc31e979a) | 两次方向一致才转图，批处理保留文件名和子目录。 | 版本说明、固定 JSON 和一张前后图 |
| 动态提示实践 | [H3 视频提示扩写：回查被改写的关键动作](#n07) | 提示词组织·动作设计｜扩写镜头和声音后回查关键动词。 | 设计思路：动作与镜头分工｜保留不可丢的动作，再扩写机位、环境声和配乐。 | 三六条666 · [Gemma4 12B 扩写与一句话直出对比](https://www.bilibili.com/video/BV1s21pzuEh3/) | 同首帧和种子示例里，扩写影响跟拍，也把颠勺改成了锅铲翻炒。 | 完整简介、P1 12 张抽帧和 OCR 人工核字 |
| 独立短片流程 | [Last Light：用视频帧补角色数据，再按景别调 LoRA](#n08) | 关键帧·角色连贯｜从角色片段取训练帧，按景别调低限制。 | 设计思路：按景别调整身份强度｜近景优先保脸，动作远景留出肢体自由度。 | Reddit u/ideatoreels；配乐 Kevin MacLeod · [Last Light 原帖](https://www.reddit.com/r/comfyui/comments/1y7af2v/last_light_a_30s_photoreal_short_made_with_only/) | 用虚构角色生成转头和表情训练帧，并按镜头选择人物约束。 | 作者主帖与公开配置说明；未读视频 |
| 画师标签实测 | [Sena404 Anima 画师串投稿第 34 期／片内第 44 期](#n09) | 人物插画·画风搭配｜观察 piromizu 标签的细线、体型和材质。 | 美术风格方向：二次元人物·高饱和赛璐珞｜多例大眼尖颌、收腰，发束、金属与亮面布衣的高光分明。 | Sena404；画师 piromizu · [anima画师串第三十四期](https://www.bilibili.com/video/BV1Ba1KzyEPN/) | 核对字面标签 @piromizu。作者以不同角色展示服饰受光和面部倾向。 | 完整简介、P1 12 张抽帧和 OCR 人工核字 |

## 当日分享

<a id="n01"></a>

### World Streets v3／v4：实地地形、二次精修与虚构招牌

**适用方向：构图控制·街景生成｜用同机位深度保布局，再细化路面和招牌。**

**设计思路：地形和字牌分层｜用地形承载街区布局，再单独组织大招牌文案。**

- 原作者与原文：Tsumugi_Lab · [v3.0](https://civitai.com/models/3064332?modelVersionId=3491227) · [v4.0](https://civitai.com/models/3064332?modelVersionId=3492719) · [作品示例](https://civitai.com/images/150454569)
- 版本变化：11 月 27 日 19:49 发布 v3.0，28 日 15:01 发布 v4.0。相较[已收录的 v2](../2026-11-27/README.md#n03)，v3 加入各地区高程、逐楼估高和更多日本 PLATEAU 建筑，同名底稿沿用机位。v4 沿用 v3 几何，改写招牌和 prompts.json，使用由通用字词组合的虚构本地店名。数据与许可见源页 CREDITS 说明。
- 作者公开配置与结果：Krea 2 Turbo 先走 Patil 深度 Control-LoRA 1.0，在 1024×768 采 8 步，再放大 1.5×、重编码，以同词和 seed 做 denoise 0.35 的精修，二采不接深度。作者报告 10 个视角的深度一致性 0.871→0.864，细节指标约增 42%。12 条日本街道的 v4 对照中，作者说大招牌约半数完全正确，小远招牌仍可能乱码。
- 本库观察：两张 v4 样例都以路面透视带出街廓，一张是和式商店街及两侧竖牌，另一张为砖墙街段与暖色店面。版本作者注明通用生成条件，作品 meta 为空，逐图 seed 未取得。未下载底稿压缩包或复跑。 [第二张作品](https://civitai.com/images/150454587)

<a id="n02"></a>

### Krea 2 Turbo 成年人像的年龄偏差与 Human Diversity v3

**适用方向：摄影人物·提示词组织｜按年龄段观察数字和肤质词的人像偏差。**

**设计思路：年龄与肤质分评｜把要求年龄、可见纹理和估计年龄分别记入对照。**

- 原作者与原文：Tsumugi_Lab · [作者实测](https://civitai.com/articles/40019) · [Human Diversity v3.0](https://civitai.com/models/3066424?modelVersionId=3491445)
- 作者说明：文章于 11 月 28 日 17:37 发布，适配器 v3.0（3491445）于 27 日 19:20 发布。以 80 条成年肖像提示和固定种子对比，用另一模型估计外观年龄，挪掉部分标签与皮肤纹理词做补测。文题的 3000+ 是作者报告的累计规模，具体主对照按所列的 80 条看。
- 作者结果：底模平均估计偏差 +9.9 岁、MAE 10.8。LoRA v2 分别为 +8.9 和 9.3，v3 的总体年龄偏差近似 v2；作者另报未要求的雀斑在 70 例中由 v2 的 51 例减到 v3 的 42 例。数字多样性、肤质风格和估计器偏差均会影响读数。作者在 48 条子集里试过明确强调数字年龄，未改善该组偏差。
- 本库备注：估计器结果用于同条件比较。实际感知年龄、其它模型或特征群体外推仍未知。本次只读文章、版本说明与计数，未读例图或复跑。

<a id="n03"></a>

### PiD-EfficientGen：同一四步解码器的两种 QDM 写步长

**适用方向：像素解码·图像放大｜比较四步像素解码和稀疏状态写入配置。**

- 原作者与原文：ChangyiGan／gcy-hub；NVIDIA PiD 与 PiD-QDM Halo2 作者 · [固定模型卡](https://huggingface.co/ChangyiGan/PiD-EfficientGen/blob/03e5a66f64ef13aaa6ae23fb14263987bb26f25d/README.md) · [固定运行器](https://github.com/gcy-hub/PiD-EfficientGen/tree/61fe9001e21e9c1995a1a814db83f32ca42f2c19)
- 作者说明：11 月 28 日 22:07 建库，22:31 更新。保留原像素块，更改 14 个 PixelDiT patch block 的注意力，加入滑窗和 QDM。权重分为 25 步 VDN（需官方 PiD v1.5 FLUX 未蒸馏权重）与完整 4 步 DMD2 学生。
- 公开配置：DMD2 SDE／CFG 1，模型卡列噪声序列 0.999、0.866、0.634、0.342、0.0。稀疏 YAML 使用同一学生权重，QDM 每隔一列写一次，保留 K/V 卷积；示例 BF16 单 CUDA 卡、4096×4096、seed 1045，步骤与 CFG 字段为空、由配置层解析，作者总则见模型卡。另需 Gemma 2 2B IT。权重基于 NVIDIA NSCLv1，仅非商业研究或评估。
- 读取边界：读了稀疏配置、模型卡及来源说明。示例未运行，未视读图，也未核精修耗时、显存或 ComfyUI 兼容性。 [稀疏 YAML](https://huggingface.co/ChangyiGan/PiD-EfficientGen/blob/03e5a66f64ef13aaa6ae23fb14263987bb26f25d/configs/pid-hybrid-dmd2-sparse.yaml)

<a id="n04"></a>

### Krea 2 人物 LoRA：从选图到叠加权重排查

**适用方向：人物参考·LoRA搭配｜用姿态和服装覆盖减少身份与造型绑定。**

**设计思路：形象与附属物分开｜保留稳定识别特征，让服装、机位与用光有变化。**

- 原作者与原文：maxBedroom；贴吧楼主 hh131466654 与可见回帖作者 · [Creating Character LoRAs for Krea2](https://civitai.com/articles/40041) · [MOSS Base 叠加讨论](https://tieba.baidu.com/p/11238890745)
- 作者分享：11 月 28 日 23:30 发布。作者用自选参考做约 40 张数据，约半数头像，半数身体，变光照、机位、表情与衣着，并删近重复。持续出现的饰物可能变成身份特征，作者以项链举例。对作者的虚构角色，特定纹样等确需稳定的标记会在数据上保持一致。
- 公开条件：作者使用 Fizgig、RTX 3080 12 GB、0.5 MP，约 40 张一轮约 90 分钟。作者按固定预览挑检查点，常取 18 或 21 epoch，未公开所有 rank、学习率与原始数据。叠用其它 LoRA 干扰外貌时，文章建议先降风格强度再比较，本库未验证其权重适用性。
- 社区对照：同日 stablediffusion 原帖是 MOSS Base，楼主的角色和画风 LoRA 合用时风格发生变化。回帖建议分别降权、用多画风数据减弱身份绑定。只读 6 楼文字，未取得配方、对照图或确认解决情况。两个来源的基座与现象分别记录。

<a id="n05"></a>

### Impact Pack 自动遍历 LoRA 检查点与强度

**适用方向：自动化工作流·LoRA搭配｜固定词和种子扫描多档权重与检查点。**

**设计思路：成组对照｜同组固定构图输入，把检查点和强度标在文件名里。**

- 原作者与原文：HightekPresha；Impact Pack 作者 ltdrdata · [Automated LoRA Testing v1.0](https://civitai.com/models/3067135?modelVersionId=3492453) · [作者节点图](https://civitai.com/images/150435317)
- 作者说明：11 月 28 日 10:14 发布 v1.0（3492453）。用 Queue Trigger (Countdown)、String Selector、ImpactConvertDataType 和 Set Widget Value 串成循环。起始组合先写入节点，列表供后续轮次。Node ID 与 widget 名从界面或工作流字段核对。
- 作者示范：以 Krea 2 风格 LoRA 的三个 epoch、六组提示及 0.1 至 1.0 强度为例，作者列 60 轮、180 张。三版共用每组提示、seed 与采样条件。输出名写提示编号和强度，便于按组核对。
- 读取边界：看了工作流截图，可见并行对照支路。附件端点返回 HTML，完整 JSON、逐图参数和采样默认值未知。本轮只整理作者方法，未建立测试或执行。 [Impact Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)

<a id="n06"></a>

### FIBO 2 Batch Photo Restore & Upscale v1.0

**适用方向：旧照修复·批量工作流｜逐张检查方向、裁边、修复并保留目录结构。**

**设计思路：先校方向再修图｜双判定纠偏，修完再放大并逐张查小脸。**

- 原作者与原文：juiceman868／Juiceman8686；基于 Pixaroma、Bria、SeedVR2 上游 · [资源 v1.0](https://civitai.com/models/3067685?modelVersionId=3493300) · [固定项目](https://github.com/Juiceman8686/ComfyUI-Fibo2-Batch-Photo-Restore/tree/574f4e05a49f6e2cbc064bb2f502ab7bc31e979a)
- 作者说明：GitHub 11 月 28 日 20:26 提交，Civitai 22:57 发布 v1.0（3493300）。先对扫描件判向、裁边，再用 FIBO 2 处理褪色与划痕，最后用 SeedVR2 放大。作者保留黑白图黑白，按输出名跳过已恢复文件。作者提醒第一段约 1 MP 重绘，小脸可能变化。
- 公开配置：所查 28 节点图载入 fibo2_edit_turbo_bf16，FIBO 段 LCM／sgm_uniform、4 步、CFG 1，固定 seed 1。保存节点设 JPEG 质量 95，可选 PNG 或按原名保存。作者要求 ComfyUI 0.44.0+，FIBO 权重依 CC BY-NC 4.0 或另行授权。
- 本库观察：一张改装卡车合影的前后图中，后图的蓝黄色块、车胎与草地纹理更清楚，人物和车体轮廓大致在原位置。作品条目的 meta 为空，具体运行图、面孔一致性及真实细节仍未知。 [作品示例](https://civitai.com/images/150490529)

<a id="n07"></a>

### H3 视频提示扩写：回查被改写的关键动作

**适用方向：提示词组织·动作设计｜扩写镜头和声音后回查关键动词。**

**设计思路：动作与镜头分工｜保留不可丢的动作，再扩写机位、环境声和配乐。**

- 原作者与原文：三六条666 · [Gemma4 12B 扩写与一句话直出对比](https://www.bilibili.com/video/BV1s21pzuEh3/)
- 作者分享：11 月 27 日 20:00 发布 EP57，H3 图生视频对比里使用 20 步，Gemma4 12B BF16 扩写。作者报告滑板例的侧向跟拍更稳定，炒饭例却遗漏抛锅动作。只改动作描述后，按作者叙述恢复了多次颠勺。
- 本库视读：约 00:52 可见两条炒饭结果并排，约 00:59 的提示卡显示从锅铲动作改为握锅并向上翻抛。短边 480、每 7 秒和片尾取 12 张，核了画面文字。这些是片中案例，未取得 H3 精确权重、种子实值、完整动作时间轴及节点图。
- 读取状态：P1 78 秒，平台 zh-CN 轨需要登录。主媒体返回 567、SDK 备用接口下载成功。实际音轨、ASR 与评论未读。

<a id="n08"></a>

### Last Light：用视频帧补角色数据，再按景别调 LoRA

**适用方向：关键帧·角色连贯｜从角色片段取训练帧，按景别调低限制。**

**设计思路：按景别调整身份强度｜近景优先保脸，动作远景留出肢体自由度。**

- 原作者与原文：Reddit u/ideatoreels；配乐 Kevin MacLeod · [Last Light 原帖](https://www.reddit.com/r/comfyui/comments/1y7af2v/last_light_a_30s_photoreal_short_made_with_only/)
- 作者分享：Reddit 日期标作 11 月 28 日。先从 8 张人像挑一张做虚构角色，用 Wan 2.2 补转头、表情与后退，再取 32 帧训练 SDXL LoRA。作者称高强度会把奔跑收束成站姿，于是近景用 0.85，远景或动作镜头 0.45–0.5。
- 公开配置：首帧 RealVisXL V5、DPM++ 2M SDE／Karras、30 步、CFG 4.5、1344×768。视频用 Wan 2.2 I2V A14B FP8 和 lightx2v 四步适配，两段 2+2 步、CFG 1、shift 5，832×480、81 帧，另接 Real-ESRGAN 2×。有些镜头用首末帧；作者称在 RTX 3090 上约 3 分钟每段。
- 读取范围：只读主帖，逐镜提示、工作流 JSON、全片和各镜头元数据未取得。作者自述跨屋顶跳跃与城市熄灯未呈现清楚，费用为该次租用记录。配乐许可见主帖。

<a id="n09"></a>

### Sena404 Anima 画师串投稿第 34 期／片内第 44 期

**适用方向：人物插画·画风搭配｜观察 piromizu 标签的细线、体型和材质。**

**美术风格方向：二次元人物·高饱和赛璐珞｜多例大眼尖颌、收腰，发束、金属与亮面布衣的高光分明。**

- 原作者与原文：Sena404；画师 piromizu · [anima画师串第三十四期](https://www.bilibili.com/video/BV1Ba1KzyEPN/)
- 原作者说明：11 月 28 日 10:50:28 发布，BV1Ba1KzyEPN，P1 CID 43984618018。投稿编号 34，片头编号 44，片头与卡片核对字面标签 @piromizu。片头称 20 图实测，卡片提示细线闭合、高饱和上色，背面和侧脸五官有时退化。
- 本库观察：在抽看的铠甲、制服、围裙和街服人物例里，大眼、小鼻口与收窄下颌多次出现。多张半身或中全身强化胸腰体量对比，裙装示例可见大腿体量，完整头身与肩胯比例未量化。常见微笑或克制神情，持盘、比手势及低头侧视为画面各例。冷蓝背景与暖金边光并存，发束高光较细，金属反光与皮肤柔光区分明显。观察限本视频画面。
- 读取状态：完整简介为短横线。P1 54 秒，480×852，间隔 5 秒取帧加片尾 12 张。指定字幕轨要求登录，未读音频、评论、逐图参数和完整提示。此前一期见[第 33 期记录](../2026-11-26/README.md#n08)。

## 来源覆盖与检索记录

| 平台 | 实际覆盖 | 结果与边界 |
|---|---|---|
| 百度贴吧 stablediffusion | aiotieba 4.8.2 CREATE 第 1 页 30 条。去置顶后最新 11 月 29 日 03:37，页末 27 日 16:21，跨上次水位。带空格 stable diffusion 解析到 stable，27 条，去置顶后最新条目为 2026 年 2 月。 | 全站最新“工作流 提示词”“模型 LoRA”“教程 分享”各 1 页，27／30／24 条，含其它吧和旧帖。按 tid 去重后读 [LoRA 叠加](https://tieba.baidu.com/p/11238890745)6 楼，作为 N04 的独立讨论。另读 [Easy Use 逐张保存](https://tieba.baidu.com/p/11239117554)首楼，仅有问题与提示列表用法，未得解决。未读图、楼中楼。 |
| 百度贴吧 comfyui | CREATE 第 1 页 28 条，去置顶后最新 11 月 29 日 01:52，页末 23 日 12:43，跨上次水位。 | 读 [浏览器最小化与 H3 用时](https://tieba.baidu.com/p/11239206585)、[固定人物](https://tieba.baidu.com/p/11238489663)、[黑斑](https://tieba.baidu.com/p/11238559928)首楼及可见回复。浏览器现象是个案，未取得监控或隔离变量。黑斑帖文字正文为空，图未视读。本范围未精选，未启用 Astron。 |
| bilibili 广泛发现 | SDK 17.4.2 pubdate，“ComfyUI 教程”页 1–9 共 180 个原始条目，11 月 26 日 18:00 至 29 日 02:08，跨上次水位。另查“生图 模型”“Anima 生图”“LoRA 画风”“AI生图 提示词”各第 1 页 20 条。 | 按 BV 去重后读 [H3 扩写](https://www.bilibili.com/video/BV1s21pzuEh3/)、[服装批量](https://www.bilibili.com/video/BV1nE1Pz1E1t)、[摩尔线程 S4000](https://www.bilibili.com/video/BV1Di13zjE3f)、[SenseNova 介绍](https://www.bilibili.com/video/BV17v1MznExx)简介与元数据。S4000 简介为空，服装视频单 P 605 秒，只读简介。H3 抽帧及字幕状态见 N07。SenseNova 与此前发布内容重复，未单列。 |
| bilibili Sena404 | UID 341674866 最新投稿失败，NetworkException。以 SDK pubdate 补查“Sena404 anima 画师串”页 1，20 条，本页命中 11 月 28 日新投稿。 | BV1Ba1KzyEPN 已读完整简介和 P1 12 张画面，原作者 UID、期号及字面标签已核。平台指定字幕要求登录。按此增量推进至投稿 34／片内 44，UID 完整投稿列表仍未取得。 |
| Reddit | r/StableDiffusion newest50 与 r/comfyui newest30 原生列表均 403，辅以日期、workflow、LoRA、提示和编辑等类别搜索。 | 读 [Last Light](https://www.reddit.com/r/comfyui/comments/1y7af2v/last_light_a_30s_photoreal_short_made_with_only/)、[PI-H3／HyperFlow 耗时](https://www.reddit.com/r/comfyui/comments/1y7lygq/hyperflow_in_comfyui_2x_faster_minimax_h3/)、[AMD MOSS 经验](https://www.reddit.com/r/comfyui/comments/1y7t1hf/got_around_to_testing_moss_image_on_7900xtx/)及 [H3 蒙版问答](https://www.reddit.com/r/StableDiffusion/comments/1y7jcl9/minimax_h3_image_editing_using_mask/)正文或可见片段。HyperFlow 跨版重复按源帖合并，主帖的单机器对照不支持普遍倍率。未取得完整最新评论。 |
| Hugging Face | text-to-image 最新 70、image-to-image 最新 35，Anima／Illustrious／NoobAI 各 15。 | 固定版本查 PiD、[Nano-RestoreNet-2](https://huggingface.co/FlameF0X/Nano-RestoreNet-2/blob/731bc681c58e385f899f3b8569f2d2e0fa27fb7c/README.md)及 Hiraya 模型卡，核 PiD YAML 和许可。家族关键词含镜像及误命中，未视为官方发布。 |
| GitHub | 工作流更新搜索返回 25 项，提示与节点搜索实际 12 项。依项目追精确 commit。 | 读 FIBO 2 固定工作流及 [Creative Prompt Enhancer](https://github.com/CjBloodZ/ComfyUI-Creative-Prompt-Enhancer)、[TK-Prompt-Canvas](https://github.com/Ararararararaki/TK-Prompt-Canvas)、PPC Shot Isolation 的项目说明。未安装、编译或运行。 |
| Civitai 文章与讨论 | Newest 30 篇，读年龄、Krea 人物选材、[色板并排](https://civitai.com/articles/40060)、[卡通稿实践](https://civitai.com/articles/40030)、[Qwen 2.1 训练](https://civitai.com/articles/40018)与 [周更新讨论](https://civitai.com/articles/40021)正文。 | 年龄文章和周讨论有评论计数，未取回复正文。周讨论转给的更新条目页已打开，未把社区解读当平台全部更新。 |
| Civitai 模型、工作流及作品 | 最新模型 40、工作流 20。核 World Streets 两新版、FIBO 2、Impact Pack、[HaDeS 固定姿态](https://civitai.com/models/3065720?modelVersionId=3493583)、[Illustrious Prompt Palette](https://civitai.com/models/3067183?modelVersionId=3492510)、[Krea 鱼眼 v4](https://civitai.com/models/3047600?modelVersionId=3490362)、[AIKSK Anima Preview 3 图](https://civitai.com/models/3067893?modelVersionId=3493602)及草图转照片。 | 作品查询依次为 4+4／3／1／4／3／4／1／4，meta 都为空。实际看 World Streets v4 两图、FIBO 一图、Impact 节点图及 HaDeS 海报。Impact 和 HaDeS 附件入口返回 HTML。Preview 3 是社区图版本，未认作底模发布。 |
| 补充来源 | ComfyUI 官方论坛 latest.json 返回 200，首条为安装求助，其后为较旧 LTX 主题。note.com ComfyUI 最新搜索 403。 | 论坛读列表，本范围未精选。 |

## 后续关注与更正

- Sena404 已核水位推进至投稿第 34 期／片内第 44 期，完整 UID 投稿入口恢复后再查关键词范围之外的增量。
- World Streets v3、v4 保留同一机位和版本入口。招牌逐字检查、二采和逐图实值仍按原文线索补查。
- Krea 年龄对照保留估计器限制。旧照批修需关注小脸重绘。Impact 工作流的实际 JSON 和完整可设置项待作者可读附件。
