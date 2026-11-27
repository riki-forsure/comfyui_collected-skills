# 2026-11-28 每日生图社区发现

- **北京时间与时间窗**：11 月 28 日 04:05 起查，主要列表和补查集中于 04:05–04:07，随后阅读原文、配置和抽样画面。承接 11 月 27 日约 04:05–04:07 的成功检索水位，旧资源的新增演示及首次补读另标。日期除另注均用北京时间。
- **检索类型**：无具体差距要求的每日广泛发现。
- **执行状态**：精选 8 项。两个贴吧可读取，Reddit 原生最新列表、Sena404 投稿接口、B 站指定字幕及部分 Civitai 评论和逐图配方受限。已读范围逐项注明。未安装节点、加载权重、复跑、生成或验证收益，未取得用户认可。
- 本文为中文整理。感谢社区作者、维护者及上游项目，请回原文阅读完整说明、示范和更新，并遵循各来源许可。

## 今日值得阅读

Anima Role Ref KV 的社区续训公开了带参数的姿态示范。ZoeJoe 的漫画案例把角色提示、画风和排字分开，Nyx_x 则分享了标签组织、固定种子对照和 NoobAI EPS 草稿流程。另收录 Ming 设计模型及社区试用、MOSS 小编码器、Persona Director、双基座风格 LoRA 与 MOSS 表情局部精修。

## 分享速查

| 类别 | 分享／资源与版本 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点／可学习经验 | 读取状态 |
|---|---|---|---|---|---|---|
| 设计模型 | [Ming-Image-0.2-Design：版面、文字和设计草稿](#n01) | 版面文字·商品视觉｜用结构化提示组织商品图、界面和空间稿。 | 设计思路：版面分区·字面文本｜在提示中写清区块层次、元素位置与实际文案。 | inclusionAI；社区试用 AI产品狙击手 · [固定模型卡](https://huggingface.co/inclusionAI/Ming-Image-0.2-Design/blob/3538f4c311cf8f5256d631ddb7f47793f741aa2e/README.md) · [B站实测](https://www.bilibili.com/video/BV1go1WzHEzk/) | 6B DiT 用于视觉设计，社区演示提供版面和文字的反例。 | 模型卡、提交、完整视频简介及 P1 抽样画面 |
| 文字编码适配更新 | [MOSS Smaller Encoder：4B 推荐，2B／0.8B 实验支持](#n02) | 资源选型·兼容排错｜按显存预算选择编码器并留意复杂构图。 | — | BakaPotatoLord／PotatoForge，参考 ComfyUI-ClipProj · [作者帖子](https://www.reddit.com/r/StableDiffusion/comments/1y6tyhk/moss_image_use_qwen354b_instead_of_9b_as_the_text/) · [固定 README](https://github.com/bakapotatolord/moss-image-smaller-encoder/blob/05b0354f433b0fbe57785f63a8de26321d2d7dff/README.md) · [1600 提示训练发布](https://github.com/bakapotatolord/moss-image-smaller-encoder/releases/tag/adapter-1600-train) | 在 CLIP 编码前接投影适配器，让较小 Qwen3.5 接入 MOSS 的 9B 条件空间。 | 原帖、作者回复、固定图、对照参数 JSON 和发布记录 |
| 人物姿态参考 | [Anima Role Ref KV 社区续训：分开人物图与 SDPose 骨架](#n03) | 角色参考·姿态控制｜将角色图和骨架分路，尝试保留造型。 | 设计思路：身份与动作分工｜角色图提供服饰与轮廓，骨架图引导肢体和朝向。 | clkara／Internal_Answer_6866，基于 AnticPan 与 CircleStone Labs · [Put any character in any pose with Anima!](https://www.reddit.com/r/StableDiffusion/comments/1y6vq6s/put_any_character_in_any_pose_with_anima/) · [固定模型卡](https://huggingface.co/clkara/Unofficial_Anima-Role-Ref-KV/blob/30946eb143950a298fc4a5f7d710d26cff025592/README.md) | 基于官方 v3 续训约 300 对，输入姿态图限定 SDPose 格式。 | 主帖、可见回复、模型卡、海报及示范 PNG 内嵌图 |
| 自动提示更新 | [Persona Director 1.1.0：用状态字段维护连贯场景](#n04) | 提示词组织·角色连贯｜分字段改服装、动作和场景并保留身份。 | 设计思路：状态化提示·局部改写｜把身份、服装、灯光存为字段，每镜只更新需要改变的项。 | 18yz153／Glittering-Ad-1338 · [社区更新与作者示范说明](https://www.reddit.com/r/comfyui/comments/1y6uir0/persona_director_update_the_state_machine_node/) · [1.1.0 固定提交](https://github.com/18yz153/ComfyUI-Persona-Director/blob/cd92beee8e9fda986ab55997ccad81d2cbc51f4f/README.md) | 新增自然语言 DiT 分支及工具调用的局部字段更新。 | 主帖、作者回复、固定文档及配置文件树 |
| 漫画制作案例 | [一套画风 LoRA 维持六格漫画，排字在成图之后](#n05) | 漫画分镜·画风搭配｜用固定角色标记和后期排字组织多格漫画。 | 设计思路：分镜连续性·独立排字｜固定发型、服饰与点色，把气泡定位放到成图后。 | ZoeJoe · [Making a Visually Consistent AI Comic with One Style LoRA](https://civitai.com/articles/39958) · [作者漫画](https://civitai.com/comics/4989/the-frost-line-courier) · [IceBrush MOSS v1](https://civitai.com/models/3061816?modelVersionId=3485642) | 角色关键词各格复用，用景别、动作和灯光描述当格变化。 | 正文、资源版本和风格样例；漫画格图未逐张读 |
| 画风 LoRA 新演示 | [Astrae Oratio 双基座画风 LoRA：Anima 与 Krea 2 的不同写法](#n06) | 画风搭配·人物插画｜查阅双基座触发词、上色和跨题材示例。 | 美术风格方向：赛璐珞人物·清透光晕｜细轮廓结合块面阴影，近景眼睛明亮，数例以星芒点光。 | 贝果_Official／bag3l · [跨题材原视频](https://www.bilibili.com/video/BV1ZQ1tzgE7t/) · [Anima v1.0](https://civitai.com/models/3057111?modelVersionId=3477942) · [Krea 2 v1.0](https://civitai.com/models/3057111?modelVersionId=3477947) | 本轮补读 11 月 18 日的两份权重及新发布的跨题材视频。 | 两版正文、作品元数据、完整简介、P1 10 张及 OCR 对照 |
| 标签与精修教程 | [Illustrious／NoobAI 标签提示，以及 reForge 的 NoobAI EPS 草稿流程](#n07) | 提示词组织·采样精修｜将构图、材质和放大安排成可比较的步骤。 | 设计思路：按层写词·先定构图｜分开主体、取景、衣着和光照，挑完草稿才放大。 | Nyx_x · [Tag prompting for Illustrious and NoobAI](https://civitai.com/articles/39923) · [NoobAI EPS reForge 实践](https://civitai.com/articles/39920) · [同作者 A/B 对照方法](https://civitai.com/articles/39922) | 同一组作者教程合并，保留标签语法及实际模型条件。 | 三篇教程正文、发布时间与评论计数；未视读配图 |
| 表情编辑更新 | [MOSS Pro Grade v8.1：加入 LivePortrait 表情调整](#n08) | 表情设计·局部精修｜对已生成的脸调整视线、眉眼与口部。 | 设计思路：表情拆分·局部回贴｜分别调整眼眉、嘴角和头部角度，局部回贴面部。 | lonecatone23；LivePortrait 上游 KwaiVGI、权重整理 Kijai · [v8.1 资源](https://civitai.com/models/3009154?modelVersionId=3491773) · [Lonecat’s Expression Editor](https://civitai.com/articles/39341) | 更新引入既有表情编辑器，适合小幅调整，脸部遮挡是作者指出的限制。 | 版本说明、编辑器教程与作品元数据 |

## 当日分享

<a id="n01"></a>

### Ming-Image-0.2-Design：版面、文字和设计草稿

**适用方向：版面文字·商品视觉｜用结构化提示组织商品图、界面和空间稿。**

**设计思路：版面分区·字面文本｜在提示中写清区块层次、元素位置与实际文案。**

- 原作者与原文：inclusionAI；社区试用 AI产品狙击手 · [固定模型卡](https://huggingface.co/inclusionAI/Ming-Image-0.2-Design/blob/3538f4c311cf8f5256d631ddb7f47793f741aa2e/README.md) · [B站实测](https://www.bilibili.com/video/BV1go1WzHEzk/)
- 作者说明：11 月 25 日已有上传记录，11 月 26 日 20:14 的固定提交补 DiT 参数量。卡片标 0.2-Design 为 6B DiT，MIT，面向商品主图、UI 草稿、空间效果图；可用自然语言或 Figma 式分区描述，另链提示扩写及下游设计技能。卡片将 0.1-Design-Layer 单列为分层模型，0.2 权重表的明确用途为设计生成。
- 公开设置：作者示范 BF16、12 步、CFG 1，默认 2048×2048，可用 1024×1024 加快方图预览。配对输入宽高后从内部尺寸桶选择并可末端缩放。80 GiB CUDA 显卡是作者列出的验证配置。卡片榜单是特定时间与评测版本的快照。
- 社区案例：AI产品狙击手 11 月 27 日 14:52 发布《Ming‑Image‑0.2‑Design 生图模型实测翻车现场！》。P1 169 秒，短边 480，每 16 秒及片尾抽 12 张。可见三栏行程、多视角人物和饼图案例，饼图有多处数字文字散在图外，无法据此核准数据。社区演示的模型文件和逐图设置未取得，无法判断与作者建议的关系。平台字幕需登录，已对照画面内文字，音频、评论及官方展示图未读。

<a id="n02"></a>

### MOSS Smaller Encoder：4B 推荐，2B／0.8B 实验支持

**适用方向：资源选型·兼容排错｜按显存预算选择编码器并留意复杂构图。**

- 原作者与原文：BakaPotatoLord／PotatoForge，参考 ComfyUI-ClipProj · [作者帖子](https://www.reddit.com/r/StableDiffusion/comments/1y6tyhk/moss_image_use_qwen354b_instead_of_9b_as_the_text/) · [固定 README](https://github.com/bakapotatolord/moss-image-smaller-encoder/blob/05b0354f433b0fbe57785f63a8de26321d2d7dff/README.md) · [1600 提示训练发布](https://github.com/bakapotatolord/moss-image-smaller-encoder/releases/tag/adapter-1600-train)
- 作者说明：4B 投影文件的发布标签已有 10 月记录。11 月 28 日 01:26 的提交加入 2B／0.8B，01:55 的提交明确推荐 4B。1600 训练版 4B 适配约 21 MB，投影 2560→4096；作者列同族 INT8 ConvRot 编码器文件由 9.75 GB 降至 4.82 GB。该数值是文件大小，实际显存用量另计。
- 公开配置：Load CLIP 用 moss_image，接相同尺寸的 MOSS Smaller Encoder Adapter，再接 CLIP Text Encode。作者对照 JSON 的模型为 moss_image_sft_int8_convrot_attn.safetensors、VAE moss_vae.safetensors，640×960、8 步 Euler／simple、CFG 1、shift 5、DMD LoRA 0.8。仓库示例工作流的 VAE 字段写 flux2-vae.safetensors，两份公开文件分别记载。 [对照 JSON](https://github.com/bakapotatolord/moss-image-smaller-encoder/blob/05b0354f433b0fbe57785f63a8de26321d2d7dff/images/comparisons.json)
- 作者结果与本库读取：400 个留出提示的特征余弦相似度为 0.9126。作者在原帖回复补了多主体、位置与遮挡的失败案例。2B／0.8B 目前只有特征级评估，编辑和其它量化未立据。读了原帖、配置与更新，未视读成图或测定质量、速度与显存。

<a id="n03"></a>

### Anima Role Ref KV 社区续训：分开人物图与 SDPose 骨架

**适用方向：角色参考·姿态控制｜将角色图和骨架分路，尝试保留造型。**

**设计思路：身份与动作分工｜角色图提供服饰与轮廓，骨架图引导肢体和朝向。**

- 原作者与原文：clkara／Internal_Answer_6866，基于 AnticPan 与 CircleStone Labs · [Put any character in any pose with Anima!](https://www.reddit.com/r/StableDiffusion/comments/1y6vq6s/put_any_character_in_any_pose_with_anima/) · [固定模型卡](https://huggingface.co/clkara/Unofficial_Anima-Role-Ref-KV/blob/30946eb143950a298fc4a5f7d710d26cff025592/README.md)
- 版本与作者说明：11 月 27 日 21:53 建库，23:07 更新。相比[此前收录的 AnticPan v3](../2026-11-16/README.md#n03)，此社区版用带骨架的约 300 对数据续训。作者称角色图或目标图部分为合成，复杂姿态对较少。沿用原项目的节点，权重许可按 CircleStone Labs 非商业许可。
- 同图公开配置：读作者示范 PNG 的 prompt 和 workflow 字段。Anima base v1.0，权重 Anima-v3-SDPose-Complex-00180-ComfyUI.safetensors，输入 basori.jpg、pose.jpg，cond only、ref_megapixels 0.67、sigma auto、strength 1.0；1280×848，Euler／simple、32 步、CFG 4.5、denoise 1、seed 965338042228260。正向有加权仰头与闭眼项。图与参数均来自作者原文件。 [带图内元数据示范](https://huggingface.co/clkara/Unofficial_Anima-Role-Ref-KV/blob/30946eb143950a298fc4a5f7d710d26cff025592/Anima-Role-Ref-KV-v3.0_00047_.png)
- 本库观察与社区反馈：海报一例从参考的交臂改成抬臂张手，发髻和浅蓝服装仍可辨，仰头闭眼令眼部线条更难辨。可见回复也质疑头部和表情，作者解释闭眼来自提示并承认少样本限制。当前证据限这一组合，未对同人物多角度或其它骨架预处理器复跑。

<a id="n04"></a>

### Persona Director 1.1.0：用状态字段维护连贯场景

**适用方向：提示词组织·角色连贯｜分字段改服装、动作和场景并保留身份。**

**设计思路：状态化提示·局部改写｜把身份、服装、灯光存为字段，每镜只更新需要改变的项。**

- 原作者与原文：18yz153／Glittering-Ad-1338 · [社区更新与作者示范说明](https://www.reddit.com/r/comfyui/comments/1y6uir0/persona_director_update_the_state_machine_node/) · [1.1.0 固定提交](https://github.com/18yz153/ComfyUI-Persona-Director/blob/cd92beee8e9fda986ab55997ccad81d2cbc51f4f/README.md)
- 作者说明：11 月 27 日 23:33 提交 1.1.0。保留 SDXL／Pony 标签节点，新增面向 FLUX、Anima、SD3.5 等的自然语言输出。一次改动可以通过工具调用提交局部字段，由 JSON schema 检查，再按配置渲染为提示。项目 Apache 2.0。
- 公开条件：仓库提供 nl.json、anima.json 等 profile 及示例图。按 README 可选择 tool_mode 的 auto、tool 或 json_only。本地 LLM 不稳定时，作者有 JSON 兼容路径。原帖例把领口或配饰、服装、光照和机位分别管理，换场时只提交需要变化的项。示范的准确图像模型版本、逐图 seed 和采样未知。 [示例工作流目录](https://github.com/18yz153/ComfyUI-Persona-Director/tree/cd92beee8e9fda986ab55997ccad81d2cbc51f4f/assets)
- 读取状态：查了项目、文件目录和作者回复中的三步文字，未视读示例图、验证不同语言模型的状态保留或运行节点。

<a id="n05"></a>

### 一套画风 LoRA 维持六格漫画，排字在成图之后

**适用方向：漫画分镜·画风搭配｜用固定角色标记和后期排字组织多格漫画。**

**设计思路：分镜连续性·独立排字｜固定发型、服饰与点色，把气泡定位放到成图后。**

- 原作者与原文：ZoeJoe · [Making a Visually Consistent AI Comic with One Style LoRA](https://civitai.com/articles/39958) · [作者漫画](https://civitai.com/comics/4989/the-frost-line-courier) · [IceBrush MOSS v1](https://civitai.com/models/3061816?modelVersionId=3485642)
- 作者分享：11 月 27 日 17:37 发布。两部漫画对照中，作者重做了分镜与横版封面的画风。另一部六格漫画采用统一 IceBrush 风格，固定发型、眼色、外套、围巾及一道饱和点色，再逐格改动作、景别、光线。先预留字区，审完眼睛及持物位置再用 Pillow 写对白和旁白。
- 公开配置：作者列 MOSS Image SFT INT8 ConvRot 或 BF16，按顺序加载 [Fast-12 OPD v1.0](../2026-11-25/README.md#n02) 1.0、IceBrush MOSS 0.85，再设 AuraFlow shift 5、Euler／normal、CFG 1、16 步、1248×1872 与 FLUX.2 Small VAE。这是作者列的六格流程参数，逐图 seed、实际权重精度和完整文本未逐格取得。图中手与道具表现的步数对照来自作者。
- 本库读取：读文章和 Civitai 资源版本，漫画入口返回页面。实际看了 IceBrush 资源的一张风格样例，人物有冷青黑色块、压暗外套与锐利边线；该图是否用于漫画未知，逐格图和排字文件未读。 [IceBrush 作品示例](https://civitai.com/images/149957832)

<a id="n06"></a>

### Astrae Oratio 双基座画风 LoRA：Anima 与 Krea 2 的不同写法

**适用方向：画风搭配·人物插画｜查阅双基座触发词、上色和跨题材示例。**

**美术风格方向：赛璐珞人物·清透光晕｜细轮廓结合块面阴影，近景眼睛明亮，数例以星芒点光。**

- 原作者与原文：贝果_Official／bag3l · [跨题材原视频](https://www.bilibili.com/video/BV1ZQ1tzgE7t/) · [Anima v1.0](https://civitai.com/models/3057111?modelVersionId=3477942) · [Krea 2 v1.0](https://civitai.com/models/3057111?modelVersionId=3477947)
- 版本与作者说明：两版于 11 月 18 日 13:56／13:59 发布，本轮因 11 月 27 日 21:21 的跨题材演示首次补录。Anima base v1.0 训练至 step 1350，Krea 2 RAW 到 step 3000，两版 rank 32／alpha 32。版本说明均以 astrae_oratio 开头，Anima 接逗号分隔的标签，Krea 2 接主体计数与自然语言。作者称视频演示权重为 1.0，并提到冷海蓝、青绿与星芒。
- 本库观察：同一 P1 的巫女、雪地与室内自拍例都有清楚的线与成块阴影。多张近景呈较大的虹膜、收窄下颌和较小鼻口。自拍例是正视眯眼笑，雪地例有收肩或前伸手。服装与景别变化较大，头身、肩胯和体量无法从这组抽样概括成固定比例。部分场景偏蓝，巫女与法术例亦使用明确暖色。
- 读取状态：P1 67 秒，短边 480，约每 7 秒及片尾取 10 张。主媒体地址 567，SDK 备用地址成功。字幕需登录，未读取声音、评论。两版本各查询 4 条作品，所读元数据无逐图配置；视频未取得完整提示、种子和实际采样实值。

<a id="n07"></a>

### Illustrious／NoobAI 标签提示，以及 reForge 的 NoobAI EPS 草稿流程

**适用方向：提示词组织·采样精修｜将构图、材质和放大安排成可比较的步骤。**

**设计思路：按层写词·先定构图｜分开主体、取景、衣着和光照，挑完草稿才放大。**

- 原作者与原文：Nyx_x · [Tag prompting for Illustrious and NoobAI](https://civitai.com/articles/39923) · [NoobAI EPS reForge 实践](https://civitai.com/articles/39920) · [同作者 A/B 对照方法](https://civitai.com/articles/39922)
- 作者分享：三篇于 11 月 27 日约 05:17–05:18 发表。标签文建议用已存在的标准标签，按主体、取景、衣着、姿态、场景、打光和风格组织。示例中 WebUI 标签括号用反斜线转义，取景时显式写全身并避免特写。各模型家族的质量词和权重宜按 checkpoint 分开比较。
- 公开配置：作者的实际 reForge 方法限 NoobAI XL EPS 底模或基于它的合并。草稿用 Euler a／Karras、25 步、CFG 5、896×1152，Clip Skip 1 或 2。选中后用 1.5× Hires fix、10 步、denoise 0.4、CFG 5，并在终尺寸使用 ADetailer。V-Pred 不在这篇经验的适用范围。
- 学习备注：作者建议固定种子修改一个词块，再随机出变体；比较标签时保留相同种子集合、写清成功和伪影判据。标注为作者方法，未视读对照图、未复跑，也未核通用表现。此前同作者的节点教程见 [Style Grid](../2026-11-27/README.md#n06)。

<a id="n08"></a>

### MOSS Pro Grade v8.1：加入 LivePortrait 表情调整

**适用方向：表情设计·局部精修｜对已生成的脸调整视线、眉眼与口部。**

**设计思路：表情拆分·局部回贴｜分别调整眼眉、嘴角和头部角度，局部回贴面部。**

- 原作者与原文：lonecatone23；LivePortrait 上游 KwaiVGI、权重整理 Kijai · [v8.1 资源](https://civitai.com/models/3009154?modelVersionId=3491773) · [Lonecat’s Expression Editor](https://civitai.com/articles/39341)
- 作者说明：11 月 28 日 00:14 发布工作流 V8.1 Expression Edit，版本 3491773。新版说明列的变化是接入表情编辑器，机制细节来自 11 月 21 日 06:39 发布的原教程。作者以 LivePortrait 重定向面部，预览可拖眉眼、嘴角、视线点及头部方向，编辑后局部回贴。
- 公开条件：教程要求 LC MaskMaker 0.29.23+，表达强度可在预设控制中调整，protect_mask 可交给后续处理保护脸区。作者说手、杯子、话筒等遮挡可能随脸一同扭曲，适合小改。原教程列了首次运行的下载依赖，本次仅阅读。 [节点作者仓库](https://github.com/lonecatone23/ComfyUI_LC_MaskMaker_nodes)
- 读取状态：查到最新与前版说明、教程正文及 4 条作品元数据。未读 v8.1 完整图、版本评论或配方，没有观察成图或检验变形边界。

## 来源覆盖与检索记录

| 平台 | 实际覆盖 | 结果与边界 |
|---|---|---|
| 百度贴吧 stablediffusion | aiotieba 4.8.2 CREATE 第 1 页 30 条，去置顶后最新 11 月 28 日 00:16，页末 25 日 16:19，跨上次水位。带空格 stable diffusion 入口解析为 stable 吧，返回 27 条，去置顶后首条为 2026 年 2 月。 | 全站最新“工作流 提示词”“模型 LoRA”“教程 分享”各 1 页，分别 24／28／24 条，含其它吧或旧帖。按 tid 合并，读了 [Nibbles 内测预览](https://tieba.baidu.com/p/11235180736)13 楼与 [NAI 精确参考反馈](https://tieba.baidu.com/p/11236152652)2 楼文字。前者讨论未完成训练的内测，未查到可核的公开发布；后者回帖评价相反，V5 适用版本与正式更新未核实。未读图及楼中楼，本范围未精选。 |
| 百度贴吧 comfyui | CREATE 第 1 页 27 条，去置顶后最新 11 月 27 日 23:26，页末 22 日 16:42，跨上次水位。 | 读 [8GB 显存讨论](https://tieba.baidu.com/p/11235571985)及 [模板下载超时](https://tieba.baidu.com/p/11236087809)各 3 楼。前者的 H3 运行时间为用户报告，精确量化、配置和机器条件未取得；后者未见已解决证据。未启用 Astron，本范围未精选。 |
| bilibili 广泛发现 | SDK 17.4.2 pubdate。“ComfyUI 教程”页 1–6 共 120 个原始条目，跨度 11 月 26 日 17:35 到 28 日 01:00，已跨前一水位。另查“生图 模型”“Anima 生图”“LoRA 画风”“AI生图 提示词”，各第 1 页 20 条。 | 按 BV 去重并读 9 条完整简介，其中训练工具介绍的简介为空。N01／N06 抽帧深读。另核[CharRef v2 视频](https://www.bilibili.com/video/BV1CR1szrEd5/)的简介、P1 72 秒的 11 张抽帧和资源版本 3476383，仍是[已有 Recipe V2](../2026-11-17/README.md#n05)，作为已知版本的新演示，本轮不另计。3 条指定 zh-CN 轨均需登录。其余如 [Anima 多阶段提示](https://www.bilibili.com/video/BV1cz1xzrEVJ/)、[摄影提示 Skill](https://www.bilibili.com/video/BV1391Hz1EZm)、[Kandinsky 超分](https://www.bilibili.com/video/BV1F21tzyEZM)、[MOSS 汇总流](https://www.bilibili.com/video/BV1RR1xz8EAk)只读简介或元数据，未检查网盘、音视频或评论。 |
| bilibili Sena404 | UID 341674866 最新接口返回 NetworkException。补查 pubdate “Sena404 anima 画师串”页 1，20 条，再读取已知 BV 完整简介。 | 关键词范围最新仍为 [BV1ogykzrEHB](https://www.bilibili.com/video/BV1ogykzrEHB/)，11 月 25 日投稿第 33 期，片内 43 已在[系列索引](../2026-11-09/notes/Sena404画师串与相关分享.md)核过。此次未取得完整投稿列表，仅在关键词范围未发现更晚期数。 |
| Reddit | r/StableDiffusion 最新 50、r/comfyui 最新 30 的 JSON 入口均为 403。按近期日期、workflow、LoRA、prompt、构图及姿态类别补搜。 | 读 N02／N03／N04 原帖与可见关键回复，另读 [Moss-Frame 1.0](https://www.reddit.com/r/comfyui/comments/1y6nxqe/mossframe_10_photography_anime_and_ink_wash_in_4/)及 [Krea 2 编辑工作流](https://www.reddit.com/r/comfyui/comments/1y6adlo/dead_simple_image_edit_workflow_and_guide_krea_2/)正文。未取得两版面完整最新列表和完整评论。 |
| Hugging Face | text-to-image 最新 70、image-to-image 最新 35，Anima、Illustrious、NoobAI 各 15，再查固定模型及文件。 | 核 Ming、MOSS 编码器和 Anima 续训，读取 Anima 示范 PNG 参数。另读 [FameVTON](https://huggingface.co/PAIR/FameVTON/blob/1bd95e4d0873ffdec7bf672cbf36f37cc577b37e/README.md)、[Anima 韩文文字](https://huggingface.co/raspie/RS-Anima-Korean-Text/blob/50d99fb3d483b827221fe598dfbd9f7925339632/README.md)和 Moss-Frame 模型卡作筛选。Illustrious 和 NoobAI 家族入口含镜像、旧卡及误命中，未把它们视为官方新发。 |
| GitHub | 更新工作流搜索 25 项，提示与节点搜索 20 项，另追作者固定提交和 release。 | 已读 Persona Director 1.1.0、MOSS 小编码器的源码仓库说明与公开 JSON，另读 [MOSS BBox](https://github.com/esbe1175/comfyui-moss-bbox)和 [Booru 提示库](https://github.com/Mexes-GM/comfyui-booru-prompt-gallery)的文档。未安装、验证兼容性或运行节点。 |
| Civitai 文章与讨论 | Newest 30 篇，读漫画、标签、A/B、NoobAI EPS、表情教程，以及 [SDXL 面部微调经验](https://civitai.com/articles/39973)、[交叠与双曝光](https://civitai.com/articles/39959)、[十字绣材质实践](https://civitai.com/articles/39967)正文。 | 漫画及 Nyx_x 所读篇的元数据评论计数为 0；MOSS Pro Grade 资源计数可读，具体 v8.1 评论正文未取得。计数仅属元数据。 |
| Civitai 模型、工作流和作品 | 最新模型 40、最新工作流 20。精读双基座风格、IceBrush、CharRef、MOSS 表情版，补读 [HaDeS 两阶段](https://civitai.com/models/3065720?modelVersionId=3491563)、[Krea 2 v6.7](https://civitai.com/models/2735869?modelVersionId=3492010)、[Klein v10.3](https://civitai.com/models/2359912?modelVersionId=3491970)、[Z-Image Turbo v11.2](https://civitai.com/models/2221604?modelVersionId=3491982)。 | 作品查询 Krea 2／Klein／Z-Image 各 1 条，HaDeS 2 条，MOSS 表情 4 条。另查 Astrae 两版本、IceBrush、CharRef 各 4 条，逐图 meta 为空。已视读 IceBrush 1 张；漫画页仅打开入口，未逐格读，MOSS 表情版预览未完成读取。 |
| 补充来源 | ComfyUI 论坛 latest.json 返回 200，首屏主要为较早 LTX 等主题；note.com 的 ComfyUI 最新搜索返回 403。 | [NovelAI 精确参考文档](https://docs.novelai.net/en/image/precisereference/)可取得，含 V4.5 局部重绘限定，未找到可核对贴吧所称此次 V5 上线的版本记录，官方博客起始页受限。 |

## 后续关注与更正

- Sena404 可靠已收录水位为投稿第 33 期／片内第 43 期。待 UID 投稿页恢复后再确认关键词搜索之外的增量。
- Anima 续训保留 SDPose 输入和原图内参数；复杂姿态、手部和头部角度仍需另查。MOSS 小编码器的显存和复杂提示效果以实际模型、量化和条件为准。
- 漫画案例配方保留作者标出的顺序、精度范围和版面处理。表情工作流的 v8.1 附件、评论与演示的逐图配置待补。
