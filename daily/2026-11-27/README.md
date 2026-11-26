# 2026-11-27 每日生图社区发现

- **北京时间与时间窗**：11 月 27 日 04:05 起检查列表，补查至约 04:07，随后读原文、配置与抽样画面。承接 11 月 26 日约 04:00–04:02 的成功列表水位，早期发布的资源保留原始日期，仅记此次实质更新或首次补读。日期除另标均按北京时间。
- **检索类型**：无具体差距要求的每日广泛发现。
- **执行状态**：精选 9 项。Reddit 最新列表、B 站字幕与部分 Civitai 逐图配方和评论受限。已读范围见各条。安装、加载、复跑、实际成图和收益验证均未进行，未取得用户认可。
- 感谢原作者、社区分享者及上游维护者。本文为中文整理，请回原文阅读完整说明、例图、配置和更新，并遵循各来源许可。

## 今日值得阅读

World Streets v2 更新建筑底稿并加入 Krea 2 深度工作流。Anima 批量预览的实测拆开计时，可区分批处理与快速解码的作用。两条 B 站教程分别示范如何从定妆照展开全身造型，以及在超分、分块和 Tile 重绘之间选择。另有 MOSS 39K、建筑精修、透明解码和两种提示词组织实践。

## 分享速查

| 类别 | 分享／资源 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点 | 读取与验证状态 |
|---|---|---|---|---|---|---|
| 后训练更新 | [MOSS-Image SFT 四步蒸馏更新至 39K](#n01) | 采样加速·版本选型｜核对四步采样、补偿权重和新检查点的条件。 | 设计思路：色调与细节分评｜将人物纹理、色调、文字和构图分别与教师图对照。 | lvladikov、OpenMOSS-Team · [MOSS-Image SFT - Update - Checkpoint 39K](https://www.reddit.com/r/StableDiffusion/comments/1y5lsc7/mossimage_sft_update_checkpoint_39k_4step/) · [39K 固定卡](https://huggingface.co/lvladikov/MOSS-SFT-Distill-4step-LoRA/blob/a8e3d03a8b3450bda45112f8b1d77c3fa48e59c0/README.md) | 从 30K 继续训练，并用更多超采样教师图。文件名沿用，检查点已变。 | 主帖、卡片、检查点说明、两份图和对照拼图 |
| Anima 工作流 | [Blind-Box Draft v0.1.0：异提示批处理与快速预览](#n02) | 批量工作流·LoRA搭配｜固定角色后浏览多种画法，再精修选中的草图。 | 设计思路：先选草图再精修｜按提示与 LoRA 分组出草图，保留潜图供选中后恢复。 | lepetitprince716355 · [Multi-Prompt Batching, Bypass LoRAs, and Wan2.1 VAE Bottlenecks for Anima in ComfyUI](https://civitai.com/articles/39881) · [公开节点与工作流](https://github.com/lepetitprince716-prog/comfyui-blindbox-draft/tree/6c6b3628acdad1ad51a4615d67f04f3b0adc2f88) | 同一次前向处理不同提示，预览走轻解码，选中后再用完整解码。 | 正文、初版提交、README 和一份 API JSON |
| 深度控制更新 | [World Streets v2.0：补全街区并加入 Krea 2](#n03) | 构图控制·街景生成｜用更新的深度底稿约束街道和地标布局。 | 设计思路：街景布局·招牌设计｜用深度固定街道视角，提示词补材质和大号招牌。 | Tsumugi_Lab · [v2.0 原资源与版本说明](https://civitai.com/models/3064332?modelVersionId=3489811) · [街景示例](https://civitai.com/images/150256766) | 补入 Overture 建筑和 GHSL 高度，新增 Krea 2 Depth 工作流。 | 资源及版本正文、6 条作品元数据、3 张预览 |
| 特化编辑 LoRA | [bvfinish v1：MiniMax H3 建筑渲染精修](#n04) | 建筑可视化·图像编辑｜用一张建筑渲染图细化材质与光线。 | 设计思路：保构图精修·写实材质｜沿用原渲染的镜头，细化玻璃、草地和室内光感。 | BrickMomen、MiniMax H3 Image 作者 · [固定模型卡与示例](https://huggingface.co/BrickMomen/bvfinish-h3-image-lora/blob/b5164b31a7ac342ac086e6d16c31ffee6d319c58/README.md) | 只给一张建筑渲染，围绕已有对象润色材质与用光。 | 卡片、版本元数据及 2 对留出图 |
| 像素解码更新 | [Anima Pixel Decoder：×2 v3 与 RGBA 预览](#n05) | 解码研究·透明素材｜查阅直出两倍图与白底到透明预览的限制。 | 设计思路：轮廓与透明细节｜用纯浅色背景试轮廓分离，细栏杆和半透明材质另查。 | sorryhyun、CircleStone Labs · [固定模型卡](https://huggingface.co/sorryhyun/anima-pixel-decoder/blob/6db0ba4242ee0c43c206cf4d69af45a01afbfddb/README.md) · [RGBA 样例](https://huggingface.co/sorryhyun/anima-pixel-decoder/blob/6db0ba4242ee0c43c206cf4d69af45a01afbfddb/samples/rgba_preview.png) | 从采样末步特征直读像素，新增独立的透明预览和 ×2 v3 权重。 | 固定卡、提交记录及 1 张透明预览拼图 |
| 提示词组织教程 | [Style Grid for ComfyUI：把风格卡变成可组合提示](#n06) | 提示词组织·画风搭配｜用卡片、通配词和预设管理正负提示。 | 设计思路：风格模块化·词项检查｜把风格词分卡组织，合用时显式检查正负词冲突。 | Nyx_x／KazeKaze93 · [Style Grid for ComfyUI: the complete guide](https://civitai.com/articles/39893) · [Civitai v2.0](https://civitai.com/models/2794903?modelVersionId=3486312) · [GitHub 0.0.17](https://github.com/KazeKaze93/sd-comfyui-style-organizer/releases/tag/0.0.17) | 用正负 STRING 输出接编码器，显式区分随机抽样与无放回抽样。 | 教程正文、版本元数据、README 与 release |
| 多视角实操 | [Qwen Image 2.1：一张定妆照展开全身参考](#n07) | 人物参考·多视角｜从定妆照补齐全身造型并检查转身一致性。 | 设计思路：分阶段定造型｜先固定身材和衣着，再用全身锚点扩展侧背面。 | 暴躁小白兔学AI、Qwen Image 团队；示例金毛原照署名 Mtlchung · [【暴躁小白兔】B046 ComfyUI × Qwen Image 2.1｜一张定妆照，做出六张全身参考图](https://www.bilibili.com/video/BV1i91jzgESQ/) | 先确定身高与裙摆，再带脸部和全身参考处理不同视角。 | 完整简介、P1 抽样 17 张及 OCR 对照 |
| 放大教程 | [ComfyUI 高清放大全攻略：Anima Tile 与普通二采](#n08) | 采样精修·细节表现｜按需选择纯放大、二采分块或结构约束。 | 设计思路：分层加细节｜先明确保留轮廓的程度，再选择二采和 Tile 重绘。 | 屑魔女的炼金失败手札、Kohya 与 Ultimate SD Upscale 作者 · [画好的图发糊怎么办？ComfyUI 高清放大全攻略（含 Tile 锁图 0.85 高重绘）【ComfyUI 零基础 04】](https://www.bilibili.com/video/BV11RyCz8EjU/) · [Anima LLLite 文档](https://github.com/kohya-ss/ComfyUI-Anima-LLLite/blob/b7495bd8eb876e334509976896702484ed19cdbb/README.md) | 对比纯超分、VAE 重编二采、分块以及 Anima 2B Tile。 | 完整简介、P1 抽样 15 张及 OCR 对照 |
| 提示词实践 | [GeneGen：在分栏中锁定、重排和改写提示](#n09) | 提示词组织·方案探索｜固定主体或服装，只改指定栏位探索变体。 | 设计思路：局部改词·方案迭代｜把提示切成可锁定的栏位，每轮只改计划中的描述。 | pasta116 · [GeneGen: Prompt Breeding](https://civitai.com/articles/39828) | 公开按栏继承、跨提示组合、只换顺序的案例，工具仍在开发。 | 文章正文与发布时间，示范图未视读 |

## 当日分享

<a id="n01"></a>

### MOSS-Image SFT 四步蒸馏更新至 39K

**适用方向：采样加速·版本选型｜核对四步采样、补偿权重和新检查点的条件。**

**设计思路：色调与细节分评｜将人物纹理、色调、文字和构图分别与教师图对照。**

- 原作者与原文：lvladikov、OpenMOSS-Team · [MOSS-Image SFT - Update - Checkpoint 39K](https://www.reddit.com/r/StableDiffusion/comments/1y5lsc7/mossimage_sft_update_checkpoint_39k_4step/) · [39K 固定卡](https://huggingface.co/lvladikov/MOSS-SFT-Distill-4step-LoRA/blob/a8e3d03a8b3450bda45112f8b1d77c3fa48e59c0/README.md)
- 作者说明：Reddit 标注 11 月 25 日。Hugging Face 于北京时间 11 月 26 日 06:53 提交 39K，精确检查点 chk00039000，rank 64。和[上次报道的 30K](../2026-11-21/README.md#n01)相比，训练样本累计到 39,000，后段加入以较大尺寸渲染再缩回的教师图。文件名不含检查点，固定提交、元数据和 SHA-256 都可查。 [作者检查点记录](https://huggingface.co/lvladikov/MOSS-SFT-Distill-4step-LoRA/blob/a8e3d03a8b3450bda45112f8b1d77c3fa48e59c0/moss_sft_4step_rank_64_lora_checkpoint_info.md)
- 公开配置：MOSS-Image SFT BF16，ComfyUI 补偿版 LoRA 1.0，Euler，BasicGuider，CFG 1，Manual Sigmas 为 1.0、0.91、0.717、0.024、0.0。作者示范用 BF16 文字编码器，所读的本地布局与 PiD 图在 MOSS 段用 qwen3.5_9b_w4a8_gptq。补偿版 alpha 70.4、普通版 alpha 64。带负向的 CFG 2 另列为实验工作流。发布许可为 Apache 2.0。
- 作者测试与本库观察：作者报告 Comfy Cloud 同组 22 张 1024×1024 的任务计费 GPU 时间 26.6 对 387.3 秒。本库只看一张人像三列拼图，三列均见窗侧光和红棕色长发，39K 列可辨雀斑及发丝，头部角度有差异。作者说同提示与噪声，完整逐图 seed 未取得，本库未复跑。 [作者拼图](https://huggingface.co/lvladikov/MOSS-SFT-Distill-4step-LoRA/blob/a8e3d03a8b3450bda45112f8b1d77c3fa48e59c0/assets/portrait_compare.jpg)

<a id="n02"></a>

### Blind-Box Draft v0.1.0：异提示批处理与快速预览

**适用方向：批量工作流·LoRA搭配｜固定角色后浏览多种画法，再精修选中的草图。**

**设计思路：先选草图再精修｜按提示与 LoRA 分组出草图，保留潜图供选中后恢复。**

- 原作者与原文：lepetitprince716355 · [Multi-Prompt Batching, Bypass LoRAs, and Wan2.1 VAE Bottlenecks for Anima in ComfyUI](https://civitai.com/articles/39881) · [公开节点与工作流](https://github.com/lepetitprince716-prog/comfyui-blindbox-draft/tree/6c6b3628acdad1ad51a4615d67f04f3b0adc2f88)
- 作者说明：11 月 26 日 19:17 首个公开提交，19:59 发布 Civitai 文章。Anima 每批拼接最多 4 组独立条件，按 LoRA 组合编组，用 bypass 装载及内存缓存。预览用轻量 TAEHV，成品可从保存的 latent 取回。作者观察同种子批跑和逐张跑仍有像素差异。
- 公开配置：32 格 API 图设置 576×768、6 步、er_sde／simple、micro_batch 4、auto_fast_wall，Turbo 强度 0.9。仓库说明模型文件名为示例占位。示例 API 的 VAE 字段为 qwen_image_vae.safetensors，文章计时的完整解码写的是 Wan2.1 VAE，两个来源的字段各自保留，实际计时图未知。 [固定 API 工作流](https://github.com/lepetitprince716-prog/comfyui-blindbox-draft/blob/6c6b3628acdad1ad51a4615d67f04f3b0adc2f88/workflows/01_anima_blindbox_32_draft_and_enhance.api.json)
- 作者测试：RTX 5080 16 GB、ComfyUI 0.46.0。4 个不同提示在 512×640、8 步下的 DiT 用时 1.63 秒，4 次暖机单跑合计 1.82 秒。32 格方案从 38.48 秒／峰值 15.85 GB 到 24.69 秒／7.5–8.1 GB，同时更动步数、尺寸和解码，归因限整个方案。项目 Apache 2.0。本库未看结果画面或执行。

<a id="n03"></a>

### World Streets v2.0：补全街区并加入 Krea 2

**适用方向：构图控制·街景生成｜用更新的深度底稿约束街道和地标布局。**

**设计思路：街景布局·招牌设计｜用深度固定街道视角，提示词补材质和大号招牌。**

- 原作者与原文：Tsumugi_Lab · [v2.0 原资源与版本说明](https://civitai.com/models/3064332?modelVersionId=3489811) · [街景示例](https://civitai.com/images/150256766)
- 作者说明：11 月 26 日 15:55 发布版本 3489811。相较[昨日归档的 v1.0](../2026-11-26/README.md#n05)，同一地点沿用机位，Overture 补入 OSM 缺失建筑，GHSL 辅助估高；阿姆斯特丹、苏黎世、日内瓦和三处东京视角有官方 3D 屋顶数据。小招牌仍有错字，实际用图应逐字复核。
- 公开配置：Krea 2 Turbo FP8 scaled 配 Patil/Krea-2-depth-controlnet、facok 节点，灰阶、每图 minmax、近白故关闭反转，作者以 LoRA 1.0、8 步、CFG 1、Euler／simple、1024×768 或 1344×1008 为起点。作者 10 视角 × 8 设置测试，用深度排序相关测布局贴合。Krea 强度 1.0／1.2 平均 0.87／0.91，Z-Image Turbo 0.75 为 0.76。作者强调高强度仍可能压变细长地标。Krea 2 和 Control-LoRA 依其社区许可。
- 本库观察：看了国会大厦及两张沿街图。一张沿街示例由两侧店面和斜向招牌围出街道消失点，另一张由行道树与车道线强调纵深。未读取压缩附件里的实际 JSON，6 个元数据项的 meta 为空，三图的模型和逐图配置未知。 [地标示例](https://civitai.com/images/150256739) · [第二张沿街图](https://civitai.com/images/150256760)

<a id="n04"></a>

### bvfinish v1：MiniMax H3 建筑渲染精修

**适用方向：建筑可视化·图像编辑｜用一张建筑渲染图细化材质与光线。**

**设计思路：保构图精修·写实材质｜沿用原渲染的镜头，细化玻璃、草地和室内光感。**

- 原作者与原文：BrickMomen、MiniMax H3 Image 作者 · [固定模型卡与示例](https://huggingface.co/BrickMomen/bvfinish-h3-image-lora/blob/b5164b31a7ac342ac086e6d16c31ffee6d319c58/README.md)
- 作者说明：11 月 27 日 03:07 建库、03:32 更新到 b5164b3。h3img_bvfinish_v1_2k.safetensors 为 rank 32、step 3000，MiniMax H3 Image 的编辑 LoRA，用于外观、庭院与室内。输入为一张原渲染，无需掩模。作者说明训练缺少以人物为主要内容的场景。
- 公开配置：作者示范 strength 1.0、6 步、CFG 1、Euler／simple、空负向、seed 42，长边约 2K，两边为 32 的倍数。提示从 bvfinish 开始，描述输入里已有建筑、材质和天气，再描述所需的成片质感。四张示范的各自完整提示见卡片。
- 本库观察：看了 0020 外观和 0047 室内两对。外观的红砖入口与白色楼体和原图位置接近，前景草叶尺度及玻璃反光有变化。室内的白色圆桌、木格和墙面大体保持，椅面和地毯纹理有变化。观察限两对，未做像素几何或许可的独立复核，未复跑。

<a id="n05"></a>

### Anima Pixel Decoder：×2 v3 与 RGBA 预览

**适用方向：解码研究·透明素材｜查阅直出两倍图与白底到透明预览的限制。**

**设计思路：轮廓与透明细节｜用纯浅色背景试轮廓分离，细栏杆和半透明材质另查。**

- 原作者与原文：sorryhyun、CircleStone Labs · [固定模型卡](https://huggingface.co/sorryhyun/anima-pixel-decoder/blob/6db0ba4242ee0c43c206cf4d69af45a01afbfddb/README.md) · [RGBA 样例](https://huggingface.co/sorryhyun/anima-pixel-decoder/blob/6db0ba4242ee0c43c206cf4d69af45a01afbfddb/samples/rgba_preview.png)
- 版本变化：在[11 月 20 日早期记录](../2026-11-20/README.md#n02)之后，11 月 24 日增加 x1/anima_pixel_decoder_rgba_preview.safetensors，11 月 26 日 21:42 提交 x2/anima_pixel_head_x2_v3.safetensors。提交说明列重叠输出与 GAN 收尾。模型卡中带有旧 ×2 名字的性能和裁切样例，保留其原版本条件。
- 公开配置与条件：Anima base v1.0 28-block，在 KSampler 前接 Pixel Head Tap，再用 Pixel Decode。作者要求 ×2 节点 0.3.1+、RGBA 0.4.0+、DiT fp32 stream。RGBA 示范用白背景、Euler 28 步、shift 3、CFG 4。×2 与 RGBA 只在 base 采样点训练，turbo 下会有警告。权重遵循 CircleStone Labs 非商业许可。
- 本库观察：一张棋盘底的 12 格透明预览中，巫师和马轮廓较清楚，水母的浅色垂帘看起来偏实。作者指出鸟笼细缝有块状混合 alpha，半透明材质偏不透明。本库仅视读拼图，未检查实际 PNG alpha 或运行新版解码。

<a id="n06"></a>

### Style Grid for ComfyUI：把风格卡变成可组合提示

**适用方向：提示词组织·画风搭配｜用卡片、通配词和预设管理正负提示。**

**设计思路：风格模块化·词项检查｜把风格词分卡组织，合用时显式检查正负词冲突。**

- 原作者与原文：Nyx_x／KazeKaze93 · [Style Grid for ComfyUI: the complete guide](https://civitai.com/articles/39893) · [Civitai v2.0](https://civitai.com/models/2794903?modelVersionId=3486312) · [GitHub 0.0.17](https://github.com/KazeKaze93/sd-comfyui-style-organizer/releases/tag/0.0.17)
- 作者说明：11 月 27 日 01:04 发布教程，01:09 更新。所核 Civitai 版本为 3486312（v2.0），GitHub 最新发布为 0.0.17，两处版本号按发布入口记录。点风格卡可把标签写入正、负文本字段，多选时界面报告可见冲突，用户选择移除哪一张或保留两张。
- 公开配置：Style Grid 的 positive 和 negative 是 STRING，连进各自文字编码节点文本框。作者建议先用 CSV 组织名字、正负词、描述和分类。通配词 sg 同类有放回，sgd 按队列运行逐次无放回，一次 queue 中整批共享抽取结果。正向通配词选中预设时，该预设的负词也会追加到负向输出。作者的截图使用演示库和占位图，项目为 AGPL-3.0。
- 读取状态：查了作者教程正文、资源版本和项目文档。未装节点或使用第三方风格包，未核实际模型输出。

<a id="n07"></a>

### Qwen Image 2.1：一张定妆照展开全身参考

**适用方向：人物参考·多视角｜从定妆照补齐全身造型并检查转身一致性。**

**设计思路：分阶段定造型｜先固定身材和衣着，再用全身锚点扩展侧背面。**

- 原作者与原文：暴躁小白兔学AI、Qwen Image 团队；示例金毛原照署名 Mtlchung · [【暴躁小白兔】B046 ComfyUI × Qwen Image 2.1｜一张定妆照，做出六张全身参考图](https://www.bilibili.com/video/BV1i91jzgESQ/)
- 作者分享：11 月 26 日 22:07 发布，Qwen Image 2.1，作者简介标出整合包 202611_v0462。约 00:12 的卡片把正面定妆照、全身比例、上衣剪裁、裙摆长度和开叉分别列为核对项。约 00:37 的脸部特写卡片并列定妆照和正面全身图两张参考，后续展示不同方向的造型。
- 本库观察：抽读的人像例里，深色方领上衣和暗红裙在正、侧、背各视角可辨，侧视卡用作检查衣物和姿态的例子。另见人物、道具及金毛的多角度组图。结果画面仅供理解作者流程；实际权重文件、六视角逐条提示、seed 和整套生效节点未可靠读全。
- 读取状态：P1 402 秒，短边 480，间隔 25 秒加末帧共 17 张。OCR 用于定位，关键卡片人工核对。zh-CN 轨要求登录，未读取音频、评论或网盘。原素材及授权见作者简介。

<a id="n08"></a>

### ComfyUI 高清放大全攻略：Anima Tile 与普通二采

**适用方向：采样精修·细节表现｜按需选择纯放大、二采分块或结构约束。**

**设计思路：分层加细节｜先明确保留轮廓的程度，再选择二采和 Tile 重绘。**

- 原作者与原文：屑魔女的炼金失败手札、Kohya 与 Ultimate SD Upscale 作者 · [画好的图发糊怎么办？ComfyUI 高清放大全攻略（含 Tile 锁图 0.85 高重绘）【ComfyUI 零基础 04】](https://www.bilibili.com/video/BV11RyCz8EjU/) · [Anima LLLite 文档](https://github.com/kohya-ss/ComfyUI-Anima-LLLite/blob/b7495bd8eb876e334509976896702484ed19cdbb/README.md)
- 作者分享：11 月 26 日 18:00 发布，依次演示 4× 纯超分、放大 1.5× 后经 VAE 重编码二采、Ultimate SD Upscale 分块和 Anima Tile。第一种保留原图布置，后两种用于不同重绘需求。简介对 Tile 分支明确限定 2B Anima，并标注 2.9B 不适配。Tile 文件名 animaTileRepair_v20.safetensors。
- 公开设置与本库观察：约 04:22 的同屏标题标示普通二采 0.35，Tile 分支 1.22×／Tile 强度 0.7／重绘 0.85。两侧画面保留蓝发人物及窗边构图，衣领纹样和发丝局部不同。不同分支改动成组，本库未分离单个参数收益。实际模型 checkpoint、完整提示词及种子未知。
- 读取状态：P1 347 秒，短边 480，每 25 秒抽样加末帧共 15 张，OCR 结果按卡片核字。主媒体入口返回 567，SDK 同响应的备用地址成功。zh-CN 轨要求登录，未读 ASR、评论或完整可运行工作流。

<a id="n09"></a>

### GeneGen：在分栏中锁定、重排和改写提示

**适用方向：提示词组织·方案探索｜固定主体或服装，只改指定栏位探索变体。**

**设计思路：局部改词·方案迭代｜把提示切成可锁定的栏位，每轮只改计划中的描述。**

- 原作者与原文：pasta116 · [GeneGen: Prompt Breeding](https://civitai.com/articles/39828)
- 作者说明：11 月 26 日 11:50 发布，27 日 00:20 更新页面。将提示词切为 8 个可定义栏位，示范锁定宇航员主体与服装，由 LLM 改写其它内容。也可逐代选出变体，按父代顺序在对象、场景与材质之间分配保留项。
- 公开条件：作者在文中称示范用原版 Krea 2 Turbo BF16 单次采样，无 LoRA 或放大。相同词元和 seed 的重排观察仍属作者报告。作者称工具可用本地 LLM 或 API，ComfyUI 后端仍在开发，工具尚未发布。具体工作流、采样器和逐图 seed 未公开于本次所读正文。
- 本库学习备注：可以借鉴按栏固定、按栏比较的记录方式。读了正文和版本日期，未视读示范图、运行生成或验证提示词顺序的影响。

## 来源覆盖与检索记录

| 平台 | 实际覆盖 | 结果与边界 |
|---|---|---|
| 百度贴吧 stablediffusion | aiotieba 4.8.2 CREATE 第 1 页 30 条，去置顶后最新 11 月 27 日 02:45，页末 24 日 20:22，已跨上次水位。带空格 stable diffusion 入口返回 stable 吧 26 条，含两条 2018 年置顶公告，最新普通帖为 2026 年 2 月。 | 全站最新“工作流 提示词”“模型 LoRA”“教程 分享”各查 1 页，28／29／21 条，包含它吧与旧帖。按 tid 去重，核对 [MOSS 风格求推荐](https://tieba.baidu.com/p/11233273380)首楼与 [漫画嵌字](https://tieba.baidu.com/p/11233100471)两楼，后者只有软件名回应，未形成流程。两帖图片、楼中楼未读，本范围未精选。 |
| 百度贴吧 comfyui | 同一主工具独立查 CREATE 第 1 页 27 条，去置顶后最新 11 月 26 日 15:06，页末 22 日 13:54，已跨水位。 | 核对 [H3 四视角求助](https://tieba.baidu.com/p/11231208193)首楼及 [启动故障](https://tieba.baidu.com/p/11231778832)5 楼文字。四视角仅有提问，启动贴有运行库建议但未核截图、环境与解决结果，本范围未精选。未启用 Astron。 |
| bilibili 广泛发现 | SDK 17.4.2 pubdate，“ComfyUI 教程”页 1–5 共 100 条，日期范围 11 月 25 日 18:13 至 26 日 23:58，已跨上次水位。另按“生图 模型”“Anima 生图”“LoRA 画风”“AI生图 提示词”各取第一页 20 条。 | 按 BV 去重，读取 8 条完整简介。精选 N07／N08 另核 P1 画面，字幕两条均要求登录。其它包括 [8GB 分层卸载对照](https://www.bilibili.com/video/BV1HYyBz3EMR/)、[SenseNova 实测](https://www.bilibili.com/video/BV1jbyrz6Eew/)、[IceBrush](https://www.bilibili.com/video/BV1Y9y6zeEbg)、[MOSS 概览](https://www.bilibili.com/video/BV1AsymzqErg)、[提示词工具](https://www.bilibili.com/video/BV1611jz1E2R/)与 [Oil 欧呦](https://www.bilibili.com/video/BV1Jm1jz5Eth/)。这 6 条仅读视频元数据和简介，未读音视频或评论。部分是旧作，Anima 及 LoRA 词组页首早于上期水位。 |
| bilibili Sena404 | UID 341674866 投稿页 1，30 条，时间跨度 10 月 18 日至 11 月 25 日。 | 最新仍为 [BV1ogykzrEHB](https://www.bilibili.com/video/BV1ogykzrEHB/)，已归档投稿 33／片内 43。本范围无新增，沿用[系列索引](../2026-11-09/notes/Sena404画师串与相关分享.md)。 |
| Reddit | r/StableDiffusion newest50、r/comfyui newest30 JSON 返回 403。补以日期、workflow、LoRA、prompt 搜索，打开可用原帖。 | 读 39K 发布帖、[H3 参考和首末帧排错](https://www.reddit.com/r/comfyui/comments/1y5zcs2/minimax_h3_in_comfy_the_7_gotchas_that_keep/)、[ComfyLens 1.3](https://www.reddit.com/r/comfyui/comments/1y676zl/comfylens_v13/)及[电影静帧 LoRA](https://www.reddit.com/r/StableDiffusion/comments/1y5y22g/pure_cinema_music_videocinematic_stills_lora_for/)主帖和可见片段。电影 LoRA 帖有配套提示访问讨论，本轮未核配套流程，只作候选。未读取两版面完整最新列表或评论。 |
| Hugging Face | 最新 text-to-image 70、image-to-image 35，Anima／Illustrious／NoobAI 各 15。 | 固定版本查 39K、Pixel Decoder、bvfinish，另读 [RawMoment](https://huggingface.co/yscript/RawMoment/blob/de41a27199f4156f62f19d045fd9057f0119d04b/README.md)、[Kandinsky 社区转换卡](https://huggingface.co/NidAll/Kandinsky-ImageSR-2.0-ComfyUI/blob/ef3617aac78a14bf15a2d1d7d2e945724eea171b/README.md)及 Matte Skin Illustrious。NoobAI 搜索含旧版镜像，未认作官方更新。 |
| GitHub | 工作流更新搜索 25 项，提示与节点 20 项，另按作者追固定提交及 release。 | 读 Blind-Box 项目文档与一份 API 图、Style Grid 0.0.17、Anima LLLite，另读 KandinskySRGlue、Danbooru 组合器和 Prompt Studio 文档作候选，未核实际运行。 |
| Civitai 文章与讨论 | Newest 30 篇，读 Style Grid、Anima 批量、GeneGen、[低延迟模型切换](https://civitai.com/articles/39880)、[中文提示词入门](https://civitai.com/articles/39859)与 [Singularity](https://civitai.com/articles/39885)正文。 | World Streets 页面与公开 API 返回版本说明。精选的三篇文章与 World Streets 元数据评论计数为 0，其它版本评论正文未取得。没有将计数当作完整评论读取。 |
| Civitai 模型、工作流及作品 | 查最新模型 40、工作流 20。读 World Streets、[AnyPaint v1.0](https://civitai.com/models/3065662?modelVersionId=3490449)、[Aer0 Lite v0.1](https://civitai.com/models/3065579?modelVersionId=3490325)、[MOSS＋Klein](https://civitai.com/models/3065351?modelVersionId=3489986)、[区域工作流 MOSS v2](https://civitai.com/models/3063630?modelVersionId=3490356)、[Aurixoc Anima](https://civitai.com/models/3062681?modelVersionId=3486080)。 | 作品元数据依次返回 6／1／3／6／0／1，本次视读 World Streets 新版的 3 张作品，所读三个条目的 meta 为空。区域图作品查询为 0，其它版本完整配方及资源压缩包未取得。 |
| 补充来源 | ComfyUI 论坛 latest.json 200，顶部仍为较早 LTX 等主题；note.com 的 ComfyUI 搜索 403。 | 同作者的 [Oil Book](https://book.oiloil.org/articles/ai-image-generation-guide)服务器返回文章文字，页面标注 Pro，本次仅检查文章结构和相关文字，未核示范配图。论坛只查列表，本轮未精选。 |

## 后续关注

- Sena404 水位维持投稿 33／片内 43，按下次实际投稿列表更新。
- World Streets v2 保留 Krea 2 设置和招牌可读性限制。MOSS 39K 以检查点号、固定提交及 SHA-256 辨别，原 30K 条件继续见旧档。
- Anima 批量草图的 API 字段与测速文注明的 VAE 目前各自有据。需要使用时应核对作者实际计时图、VAE 和预览解码分支。透明预览与 ×2 v3 的效果仍限作者示例。
