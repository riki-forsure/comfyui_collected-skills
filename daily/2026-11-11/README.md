# 2026-11-11 每日社区发现

感谢社区作者公开分享模型、工作流、提示词与实践经验。本页为本库中文概述，保留原作者与原文入口，欢迎回原帖阅读完整内容和后续更新。署名与链接不代表额外转载授权，第三方成果不作为本库原创。

- 北京日期与检索时间：2026-11-11，03:58起检索，04:12前完成主要来源读取，随后整理并核对归档。
- 检索类型：无具体差距要求的每日广泛发现；本轮没有额外主动专题。
- 执行状态：已整理10项首次收录主题；部分平台／作者入口受限，实际范围见覆盖表。不推断全网无更新。
- 时间窗：优先自11月10日晨间约04:03–04:09各平台成功检索之后的新增与实质变化，至本轮各来源读取快照。GitHub创建、草稿创建、公开发布和revision更新时间分别记录；早于窗口的仓库创建时间不替代本次版本日期。
- 本轮仅研究与归档。复用既有SDK、FFmpeg、OCR和ASR环境补读一条视频；未安装生图节点、下载生图权重、启动服务、出图或开展实验。读取、作者自述与运行／收益验证分别记录。

## 今日值得阅读

- [官方H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)与[社区pDMD两步适配](https://huggingface.co/akhaliq/minimax-h3-image-pdmd-2step)：一起看推理条件与上游来源，避免把格式转换当独立训练。
- [水彩防脏色块](https://civitai.com/articles/38537)与[草图转成稿](https://civitai.com/models/3043427?modelVersionId=3459553)：参考笔触／噪斑取舍、色块布局与人物比例预设。
- [MOSS姿态编辑LoRA](https://huggingface.co/thedeoxen/MOSS-Image-pose-controlnet)及[B站提示词增强教程](https://www.bilibili.com/video/BV1eDWM6CEAk/)：分别检查控制图接法和自动重写规则，不用标题代替配置阅读。

## 分享速查

| 类别 | 分享／资源与版本 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点／可学习经验 | 读取状态 |
|---|---|---|---|---|---|---|
| 官方图像模型／提示指南 | [N01 MiniMax-H3-Image：官方六步图像模型与多图提示组织](#n01) | 模型选型·多图编辑｜区分六步推理约束，并按参考图分配编辑职责。 | 设计思路：参考分工·关系描述｜先说明每张参考的用途，再描述目标关系与改动。 | [MiniMaxAI／MiniMax-AI](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image) | 文生图与多参考编辑共用图像checkpoint；服务接口的步数、CFG和最小画布规则要分别核对。 | 固定模型卡架构／文件／部署／参数段、官方提示指南部分章节、B站导读简介与贴吧发布讨论；未看模型例图或运行。 |
| 社区蒸馏LoRA／转换与合并 | [N02 H3-Image pDMD两步适配：追溯原LoRA与不同格式](#n02) | 蒸馏适配·采样配置｜追溯两步LoRA来源，按原生或Diffusers格式选用。 | — | [akhaliq；pdmd2026、Iwannapose等上游作者](https://huggingface.co/akhaliq/minimax-h3-image-pdmd-2step) | 收录上游两步LoRA的原生转换、镜像和预合并包，不将每份包装计作独立训练。 | 固定模型卡文件／ComfyUI／采样／许可／致谢段；未读合并实现、看网格或核权重。 |
| 后训练／结构控制LoRA | [N03 MOSS-Image姿态与Canny：经编辑编码器输入控制图](#n03) | 姿态控制·边缘控制｜在MOSS-Image-SFT编辑路径接入专用控制LoRA。 | 设计思路：结构与外观分工｜控制图约束姿态或边缘，文字安排材质、主体与场景。 | [thedeoxen](https://huggingface.co/thedeoxen/MOSS-Image-pose-controlnet) | 本页名称含ControlNet，但作者实现是ControlNet-style edit LoRA；编码格式和基座须匹配。 | 两份固定模型卡全文及各自示例JSON的节点／参数；未看示范图、核权重或运行。 |
| 上色／提示词实践 | [N04 水彩防脏色块：把透明层次与噪斑分开取舍](#n04) | 水彩表现·细节处理｜参考Krea2水彩叠加中斑驳与笔触的取舍。 | 设计思路：透明罩染·干净边缘｜保留水彩颗粒与层次，减少无意引入的脏斑描述。 | [xiarimu；V67 Watercolor soft原作者angelomaiota](https://civitai.com/articles/38537) | 作者用A–H方案说明提示、CFG和多LoRA的组合取舍，不把最低纹理指标等同最好的水彩。 | 文章中文正文、公开设置及A–H比较说明；未看对照图、读取指标实现或复跑。 |
| 草图转成稿／工作流 | [N05 Krea2 Sketch to Render：色块布局与三档重绘](#n05) | 草图转成稿·构图保留｜从平涂色块比较Krea2三档重绘强度。 | 设计思路：色块先行·比例预设｜先用轮廓与体量安排主体，再选择成稿变化程度。 | [Azimondious](https://civitai.com/models/3043427?modelVersionId=3459553) | 测试输入为三张平涂色块，不是全部线稿或照片；同seed三档denoise供选择。 | 完整模型说明及v1.0版本元数据；未读附件JSON、看对照图或运行。 |
| Illustrious工作流／提示教程 | [N06 ILL Image Simple：十块提示、精修和元数据分层](#n06) | 人物插画·提示词组织｜按十块组织Illustrious提示并区分各次采样。 | 设计思路：描述分工·分段精修｜主体、画风和光景分别填写，再区分底图与后处理。 | [Azimondious](https://civitai.com/models/3045260?modelVersionId=3461875) | 基础图、放大与脸部精修有各自参数；最终PNG元数据不一定描述全部后处理。 | 完整模型说明与v1.0元数据；未读指南正文、词典全部标签、附件JSON或运行。 |
| 材质工作流／技术美术 | [N07 PBR Studio Free v2.1：无缝材质与多通道估计](#n07) | 材质制作·无缝贴图｜参考SDXL生成材质及法线、粗糙度和ORM分工。 | 设计思路：表面分层·通道分工｜将底色、凹凸与反射属性分别整理供材质使用。 | [TexelForge／texelforgestudio563](https://civitai.com/models/3045529?modelVersionId=3462243) | 图生材质的height、AO和roughness为估计，不等同物理扫描或真实测量。 | 完整模型说明、v2.1元数据及固定GitHub README；未读节点实现、工作流JSON或验证贴图。 |
| 镜头提示预设／原型 | [N08 Camera Prompt Presets：把摄影后缀与主体分开](#n08) | 摄影提示·预设组织｜以独立镜头后缀整理主体之外的拍摄表达。 | 设计思路：主体与机位分工｜保留基础描述，单独切换镜头和摄影语汇。 | [cyberdeliaAI](https://github.com/cyberdeliaAI/ComfyUI-Camera-Prompt-Presets) | 可学习主体提示与摄影预设的分工；项目仍自述尚未在运行编辑器验证。 | 固定README与仓库公开性／创建／提交元数据；未读全部JSON、实现或运行。 |
| 参数探索／工作流工具 | [N09 SweepKit：把参数遍历、拼图与记录关联起来](#n09) | 参数比较·自动化工作流｜了解成组遍历与结果记录，控制组合规模。 | — | [bi-toru-to](https://github.com/bi-toru-to/ComfyUI-SweepKit) | 区分笛卡尔积和配对轴；多轴组合数量相乘，整组比较不能冒充单变量归因。 | 固定README需求、用法、轴分组、去重、后台执行及CSV段；未读全部文档／实现或运行。 |
| B站教程／提示扩写节点 | [N10 Gemini提示词增强：先核重写规则，再接编码器](#n10) | 提示词组织·自动扩写｜按任务核对Gemini重写规则再接图像编码器。 | 设计思路：表达整理·身份保留｜区分纯标签和混合表达，检查重写是否改变人物设定。 | [4evergr8](https://www.bilibili.com/video/BV1eDWM6CEAk/) | 视频与开源节点一起读；模板可能删除角色／画师字段，免费与确定性均有条件。 | 完整简介、P1的18张抽样画面／OCR、200秒音频ASR草稿及固定README功能／参数／模板段；未取得平台字幕、读评论或运行API。 |

## 当日分享

<a id="n01"></a>

### N01 MiniMax-H3-Image：官方六步图像模型与多图提示组织

**适用方向：模型选型·多图编辑｜区分六步推理约束，并按参考图分配编辑职责。**

**设计思路：参考分工·关系描述｜先说明每张参考的用途，再描述目标关系与改动。**

- 原作者与原文：[MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)，[固定模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image/blob/492fd8c4eca666f1085f57e30738c1e0d86b3439/README.md)。本轮首次收录；该revision于北京时间11月11日00:21更新，仓库创建于11月3日，不把创建时间写成正式首发时间。
- 作者介绍：约33.1B DiT，文生图和多参考编辑使用同一图像checkpoint；官方权重蒸馏为6次去噪评估、无需CFG。模型卡列出约16MP直接生成尺寸及最多16张参考的能力说明，本库未验证大幅面或多图一致性。编码器与VAE另计，权重文件大小不能换算为整条管线最低显存。
- **已读服务接口的限定**：`num_inference_steps`省略或6、`guidance_scale`省略或1，其他值返回400；不接受negative_prompt。`min_generation_area`默认4194304，小尺寸请求可先在同宽高比的大画布生成再LANCZOS缩回，设1024关闭最低面积约束。因此返回图片尺寸不一定等于实际去噪画布。这些是作者列出的部署接口规则，不直接推及所有ComfyUI封装。
- [官方提示指南](https://github.com/MiniMax-AI/MiniMax-H3-Image/tree/6ea7b9e55523a2177e4f759db372065ba6089510/skills/h3-image-prompt-writing)介绍具体可见的主体、布局、光线、材质描述；编辑先定义各参考，再说明目标关系和改动，维持参考编号与上传顺序。人物身份、姿态和材质来源可以分别说明，不把未见细节补成参考图事实。这里只整理作者的写法，不把外部SKILL文本作为本次执行指令。
- 同源导读：[mugicha-AI，BV1b3WV61EHi](https://www.bilibili.com/video/BV1b3WV61EHi/)，11月11日01:49发布，41秒；本轮仅取得完整简介与元数据。社区发布讨论：[-eziohx，贴吧原帖](https://tieba.baidu.com/p/11184920138)，11月10日22:39发帖，本轮读到14条可见楼层。楼中约28G的量化资源估计属于个人讨论，不是官方最低显存结论。
- 本库整理备注：旧[H3静帧工作流记录](../2026-10-30/notes/history/github.md#gh-11)基于此前H3视频生态；不能仅凭H3名称把它与本次官方Image权重视为同一资源。新模型与下一条pDMD适配分开记录。使用遵循原模型Community License，未完整审查所有授权条件。
- 实际读取范围：模型卡架构、文件、部署与请求参数段；官方提示SKILL及文生图／编辑指南前段；B站简介与贴吧可见讨论。未看官方示范图、核权重、加载或生成。

<a id="n02"></a>

### N02 H3-Image pDMD两步适配：追溯原LoRA与不同格式

**适用方向：蒸馏适配·采样配置｜追溯两步LoRA来源，按原生或Diffusers格式选用。**

- 原作者与原文：[akhaliq/minimax-h3-image-pdmd-2step](https://huggingface.co/akhaliq/minimax-h3-image-pdmd-2step)，[固定模型卡](https://huggingface.co/akhaliq/minimax-h3-image-pdmd-2step/blob/756956d562be30c8b4ba0119493030280ef9ac13/README.md)。仓库于11月10日23:21创建，本轮revision更新至11月11日03:57；首次收录。
- 作者明确追溯到[pdmd2026/pdmd_2NFE_lora](https://huggingface.co/pdmd2026/pdmd_2NFE_lora)，rank128、覆盖50个block的attention和FFN；原生命名转换由[Iwannapose](https://huggingface.co/Iwannapose/minimax_h3_pdmd_2nfe_comfyui)提供。本页整理Diffusers权重、原生LoRA及基于Comfy-Org权重的预合并checkpoint。上游蒸馏适配与后续转换／合并是不同工作，不把三种文件称作三轮新训练。
- 作者给出的ComfyUI路线：基座＋原生LoRA强度1.0，或已预合并checkpoint；接`MiniMaxH3SigmaShift`的`shift_video=12`、BasicGuider、euler／simple、2步、denoise1，单帧latent。**两步依赖相应LoRA或合并权重，不是把官方六步服务的步数任意改成2。** 原生和Diffusers键名不同，不能只靠改文件名互换。
- Diffusers的N次去噪评估使用N+1个时间点；不据此把ComfyUI步数改成3。模型卡中H200耗时、显存及可选精修属于作者指定设备和整套路线，本库未测速，不能外推消费显卡表现。额外精修还引入其他资源，不等同于最简两步方案。
- LoRA及转换代码的Apache条款不取消基座／合并权重的MiniMax Community License。对本页的“已加载／渲染”描述保持作者声明归属；本库未下载或验证。
- 实际读取范围：固定模型卡文件说明、ComfyUI用法、样例参数说明、部分精修介绍、Diffusers用法、许可与致谢；未读全部精修实现、看网格或复跑。上游链接用于追溯，未在本轮逐一深读。

<a id="n03"></a>

### N03 MOSS-Image姿态与Canny：经编辑编码器输入控制图

**适用方向：姿态控制·边缘控制｜在MOSS-Image-SFT编辑路径接入专用控制LoRA。**

**设计思路：结构与外观分工｜控制图约束姿态或边缘，文字安排材质、主体与场景。**

- 原作者与原文：[姿态LoRA](https://huggingface.co/thedeoxen/MOSS-Image-pose-controlnet)、[Canny LoRA](https://huggingface.co/thedeoxen/MOSS-Image-canny-controlnet)。11月10日12:09–12:10创建，分别于14:59、15:52更新；首次合并收录同作者同类方法，两个资源仍分别保留版本。
- 固定revision：Pose `e7d16fcb8eb81b4a0ab3d3a5bb3b17119d834307`；Canny `39f20bab9237b28b6dffd9600f7bec927c4b975f`。作者称两者均基于**MOSS-Image-SFT**、选训练step4500，linear rank64／conv rank16，是ControlNet式编辑LoRA，不是官方color／depth的concat控制器。
- 接法为Model Only加载LoRA，把一张控制图送入`Text Encode MOSS-Image Edit`；正、负编码都设`edit format=ai-toolkit`，作者训练时开KV cache。姿态输入为黑底彩色DWPose骨架，Canny为黑底白边，示例预处理100／200。不能把白边图当普通参考照片，或把其他控制类型直接替换进来后称兼容。
- 两份示例JSON均见30步、CFG4、euler／simple、denoise1、seed42固定、LoRA1.0；作者建议过硬时可向0.7调整。参数是作者用法／示例，不是本库确认的最优值。
- **例图与配置分开**：两个JSON的正向示例都在描述铬色水壶向蛋糕倒巧克力，不能拿它补作模型卡中人物showcase的完整提示。姿态控制与角色身份、画风绑定也不是同一能力。
- 实际读取范围：两卡全文，两个14节点JSON的加载器、编码与采样字段；未查看showcase图、核权重或运行。HF列表还出现同作者其他控制图类型，本轮只深入以上两种，不推断全套已验证。

<a id="n04"></a>

### N04 水彩防脏色块：把透明层次与噪斑分开取舍

**适用方向：水彩表现·细节处理｜参考Krea2水彩叠加中斑驳与笔触的取舍。**

**设计思路：透明罩染·干净边缘｜保留水彩颗粒与层次，减少无意引入的脏斑描述。**

- 原作者与原文：[How to Fix Watercolor "Dirty Blotches" with V67 Watercolor soft](https://civitai.com/articles/38537)，xiarimu，11月10日21:12发布、21:26更新；首次收录。作者说明自己仍在学习，文字总结有DeepSeek辅助；本库概述保留其试验范围。
- 作者路线是Krea2 Turbo INT8 ConvRot，配相应Qwen编码器与Qwen Image VAE；核心[V67 Watercolor soft](https://civitai.red/models/2530668/v67-watercolor-soft)为angelomaiota的资源。作者用0.60，并列TextFusion0.70、AnimeArtEnhanced0.46、EktachromeFade0.20、AestheticMasterpiece0.22等组合；不能将整组结果单独归因于一个LoRA。
- 方法要点：需要清洁透明的水彩时，少用会主动要求尘点、模糊水滴、渗脏边缘的描述；改用透明罩染、浅洗、白纸、清楚边缘及受控色彩。目标是笔触与层次的平衡，不能把颗粒全部当坏纹理清除。
- 作者所列1536×2048、Euler／simple、18步、CFG1.35属于该路线；CFG1时负向影响弱、1.25–1.35的比较也是作者此次经验，不推广为所有Turbo模型的规则。完整字面提示与各组变化请回原文，不把通用建议补成任何单张图的实值。
- A–H按作者说明使用相同seed，以Lab色度高频量和热点比例辅助比较；作者反而认为最低指标的A过平、G更保留水彩感。指标实现和完整变量控制未读，多项变化只能评价整套方案。本库未看对照图，因此不复述为已确认的视觉优劣。
- 实际读取范围：中文正文、参数与A–H说明，部分英文对应段及文章元数据；未看图、读工作流JSON或核对精确LoRA版本。设计思路依据作者文字整理。

<a id="n05"></a>

### N05 Krea2 Sketch to Render：色块布局与三档重绘

**适用方向：草图转成稿·构图保留｜从平涂色块比较Krea2三档重绘强度。**

**设计思路：色块先行·比例预设｜先用轮廓与体量安排主体，再选择成稿变化程度。**

- 原作者与原文：[Krea 2 Sketch to Render: Flat Colour Blocking to Finished Illustration](https://civitai.com/models/3043427?modelVersionId=3459553)，Azimondious，v1.0／3459553，11月10日23:00公开发布；创建草稿早于发布时间。
- 作者在RedCraft3.0 Krea2 INT8 ConvRot上，以三张约1MP的平涂色块输入、同一seed，对照denoise0.55／0.62／0.70。文字按物体、材质／媒介和场景描述，先由大轮廓与配色安排构图，再在三档中选择；未确认原始Krea／Turbo或其他基座有相同结果。
- 已公开设置：8步、CFG1、er_sde／simple；分块VAE512、overlap64，负向ConditioningZeroOut。作者的粗分辨率亮度布局相似度0.91–0.99只反映所用指标，不能等同语义一致、姿态精确或线稿保真；边缘数量增加也不是画质分。
- 人物设计方法：大头短躯干的色块会影响成品比例；若想画成人，应先改输入体量与头身再明确描述。这里是比例预设思路，不将某个头身值推广为所有成年角色画风。
- 作者说明工作流由脚本生成、依据节点定义检查，**并非从ComfyUI浏览器中保存的实跑图**；需含`resolution_steps`的ImageScaleToTotalPixels。其ROCm／7900XTX记录不能代替CUDA或本库环境验证。
- 实际读取范围：完整说明、版本发布时间与作者测试范围；未看示范图、读附件JSON或复跑。真实手绘线稿、照片及更多seed仍在作者列出的未测范围，不能补称已支持同等效果。

<a id="n06"></a>

### N06 ILL Image Simple：十块提示、精修和元数据分层

**适用方向：人物插画·提示词组织｜按十块组织Illustrious提示并区分各次采样。**

**设计思路：描述分工·分段精修｜主体、画风和光景分别填写，再区分底图与后处理。**

- 原作者与原文：[ILL Image Simple: ten-block Illustrious workflow](https://civitai.com/models/3045260?modelVersionId=3461875)，Azimondious，v1.0／3461875，11月11日00:00公开发布。首次收录，和上一条是不同模型家族的工作流。
- 十块分别组织质量、主体、角色、画风、外貌、服饰、姿态、镜头、背景、光效，也可切为一段完整提示。作者附[词典](https://illustrious-tag-dictionary.surge.sh)和[分组指南](https://civitai.com/articles/38538)；词典约1200标签、61负向词、73子表，但只明确测了六套起步配方，不能称全部标签已逐一测试。两个链接本轮只定位，未深读。
- 作者仅在WAI-Illustrious v16、ComfyUI0.44.0实际出图。公开基础采样896×1152、28步、CFG6、Euler ancestral／simple；hires以4x AnimeSharp后缩0.38，最终1360×1744，20步、denoise0.35；脸部精修20步、CFG6、denoise0.4，另有采样器，仅seed共用。均为作者路线，不套到Anima。
- 需留意有效种子为seed加increment；示例increment9982，想按所见旧seed复用应核对增量是否为0。作者说明最终PNG普通元数据仍可能记录基础pass，后处理细节在嵌入工作流里；不能仅读PNG顶层字段就称获得最终整图实值。
- 依赖包括Comfyroll、Image Saver≥1.23、Efficiency、twriStyler、Impact Pack及Subpack。缺少模型／embedding可能即使分组Off仍阻止排队，要按原文设None或移除相应引用；本库未检查整个有效分支，作者关于mute的说明不当作运行证明。
- 实际读取范围：完整说明和版本元数据；未看示范图、读附件JSON或执行。分块提示属于写作组织方法，词数与节点数不单独证明更好的画面。

<a id="n07"></a>

### N07 PBR Studio Free v2.1：无缝材质与多通道估计

**适用方向：材质制作·无缝贴图｜参考SDXL生成材质及法线、粗糙度和ORM分工。**

**设计思路：表面分层·通道分工｜将底色、凹凸与反射属性分别整理供材质使用。**

- 原作者与原文：[PBR Studio Free: Text to Seamless PBR Material (SDXL)](https://civitai.com/models/3045529?modelVersionId=3462243)，TexelForge，v2.1／3462243于11月11日00:14发布；[作者代码与说明](https://github.com/texelforgestudio-prog/pbr-studio-free)，本轮固定README提交`235e9401d07ae8516889976cfdb341781716fb6a`。
- 作者把SDXL模型及VAE的循环padding用于无缝生成；去光照处理得到albedo，再以DepthAnythingV2和底色细节估计height，派生OpenGL／DirectX法线、AO、粗糙度等。ORM通道是R=AO、G=roughness、B=metallic；metallic默认0，不是从照片可靠识别金属度。
- 表面设计的参考价值是把底色、起伏和反射通道分开观察，避免把渲染灯光直接当作底色。单图推断的height／AO／roughness仍是估计，不应称为扫描级物性；无缝和不同渲染器的法线方向也需分别核对。
- 作者列ComfyUI-DepthAnythingV2及ComfyUI-seamless-tiling等依赖，设备与用时为其RTX5060笔记本条件。本库未安装、测速或看贴图渲染，不能据此确认8GB环境均可达到相同体验。
- 作者另列不要转售／重新分发工作流或节点包等使用说明。本库仅摘要与链接，不复制其JSON或节点包；如需使用，请回原页查看当前完整条款。
- 实际读取范围：Civitai完整说明、v2.1元数据、固定GitHub短README；未读节点实现、工作流JSON、看纹理输出或运行。

<a id="n08"></a>

### N08 Camera Prompt Presets：把摄影后缀与主体分开

**适用方向：摄影提示·预设组织｜以独立镜头后缀整理主体之外的拍摄表达。**

**设计思路：主体与机位分工｜保留基础描述，单独切换镜头和摄影语汇。**

- 原作者与原文：[ComfyUI-Camera-Prompt-Presets](https://github.com/cyberdeliaAI/ComfyUI-Camera-Prompt-Presets)，cyberdeliaAI，11月10日19:19创建，固定提交`0b1361c92a1d07795a9897335ca2969e01284dba`于21:20更新；首次收录。
- 作者用基础提示＋两个换行＋摄影后缀，分别输出final、suffix、title；一次选择一个摄影预设，避免互相冲突的机位和灯光描述。None保留基础描述。预置8份JSON库，101个可选项包含有意重复，作者说明独立预设85个，不能把101当独立风格数。
- 可学习方法是将“画什么”与“如何拍”分开管理。库中有Krea2摄影提示与独立SDXL后缀；其中`sdxl_tag_suffixes.json`的6项明确未针对Krea2优化，不能将局部限定套给全部8库，也不能推及所有家族。本轮未逐条查看后缀，不按名称猜人物比例或实际画面。
- 自定义库需要随使用环境保存；已有workflow的JSON引用不代表预设文件自动内嵌。非None的缺库／缺预设按作者说明会验证失败，不能默默声称自动回退。
- 状态差异：本轮GitHub API的`private=false`且可读，但README仍写private／未发布Registry，并说明尚未在运行编辑器中验证。按实际公开可读记录，不把文档中的本地检查当正式发布或运行验证。
- 实际读取范围：固定README全文、创建／提交／公开元数据；未读所有JSON、实现或看例图、运行。作为原型设计思路收录，不作为已经验证的成品推荐。

<a id="n09"></a>

### N09 SweepKit：把参数遍历、拼图与记录关联起来

**适用方向：参数比较·自动化工作流｜了解成组遍历与结果记录，控制组合规模。**

- 原作者与原文：[ComfyUI-SweepKit](https://github.com/bi-toru-to/ComfyUI-SweepKit)，bi-toru-to，11月10日12:04创建，本轮固定提交`79ef82383d94d739200b63b17c5c5b1c822aea7b`于19:04更新；首次收录。
- 作者将计划、逐项生成、收集与网格预览分开，可配置seed、CFG、提示、LoRA强度、采样器、模型等轴；值域可作笛卡尔积，也可按组配对，支持跳过重复、CSV manifest关联参数与图片。还提供整合式入口及不依赖浏览器前台的执行方式。
- 本库整理备注：多个独立轴的组合数相乘，配对轴与全组合不是同一覆盖范围；同时改模型、提示、采样等只能比较整套配置，不能只凭拼图把变化归到某一个参数。manifest有助追溯，但不证明作者或本库完成了审美验收。
- 作者列测试环境ComfyUI0.31、frontend1.48.7，部分例子依赖ListUtils；与当前其他版本的完整兼容性未核。文档中的测试／开发描述仍属于作者记录，本库没有据此称已运行成功。
- 实际读取范围：固定README的安装需求、quick start、计划与收集机制、轴分组、去重和后台执行／CSV说明；未读全部外链文档、实现或生成结果。本次仅收录工具，不新增自动实验或运行任务。

<a id="n10"></a>

### N10 Gemini提示词增强：先核重写规则，再接编码器

**适用方向：提示词组织·自动扩写｜按任务核对Gemini重写规则再接图像编码器。**

**设计思路：表达整理·身份保留｜区分纯标签和混合表达，检查重写是否改变人物设定。**

- 原作者与原文：[ComfyUI提示词增强节点，免费用Gemini优化提示词](https://www.bilibili.com/video/BV1eDWM6CEAk/)，4evergr8，11月10日18:54发布，P1为200秒；[开源节点PythonComfyUIGemini](https://github.com/4evergr8/PythonComfyUIGemini)，固定README提交`caa27ac0a36e341ead8feb271c5dcd85ed01c9d7`。首次收录，同作者既有采样比较不重复计算。
- 作者示范把Danbooru标签或自然语言交给Gemini／Gemma，按可编辑系统提示重写，再接CLIP Text Encode。文档默认纯tag，也提供自然语言＋tag混合模板；“约50–60标签”是模板策略，不是质量定律或所有模型的最佳长度。
- **值得先核对的规则**：混合模板示例会去掉角色名、发色／瞳色、光环和画师名等字段；对需要保留角色身份、设定和画风的任务，不能照搬后声称等价改写。应先看重写文本实际保留了什么，再谈画面改善。
- 本库实际看图：18张约12秒间隔并含末帧的抽样覆盖仓库、节点参数和三组前后示范；约1:14可见输入／输出，约2:49起进入第一组比较。画面显示提示文本和作品随重写变化，但未取得同seed、完整有效采样与资源配置，不能单独归因于LLM。人物与场景不同的示范不归纳成统一具体画风。
- 视频“免费”对应作者展示的账户／模型额度，不能承诺人人持续免费；需可用API权限、网络与配额。README“零依赖”的实际前提是环境已有`google-genai`，固定API seed也不保证未来远端模型完全确定。本库未设置密钥、调用LLM或安装节点。
- 实际读取范围：完整简介（仅“-”）、P1公开媒体、18张抽样画面与OCR，faster-whisper base生成200秒ASR时间轴草稿；术语／数字以画面和README交叉核对，ASR不是平台字幕或准确全文。固定README读功能、输入输出、参数、纯tag／混合模板与依赖条件；未读实现、评论或完整逐图配方。媒体、截图和转录仅留临时研究目录，不提交仓库。

## 来源覆盖与检索记录

以下均为北京时间本轮快照，记录实际读取范围，不等于完整读取平台全部新帖。搜索摘要、正文、评论、配置与图像观察不互相替代。

| 平台／吧名 | 实际入口或查询 | 检查时间与读取范围 | 结果／限制 |
|---|---|---|---|
| stable diffusion／stablediffusion吧 | aiotieba4.8.2，CREATE最新第1页30项；[H3发布原帖](https://tieba.baidu.com/p/11184920138) | 03:59列表核对规范吧名stablediffusion，除置顶外日期跨过上轮晨间水位；约04:01读取候选14条可见楼层 | 正文可读，本次不沿用昨日503结论。04:09额外核对带空格的stable diffusion入口，返回stable吧的无关旧公告，故不计该别名为另一个已覆盖生图吧，实际采用stablediffusion。发布讨论并入N01。 |
| comfyui吧 | aiotieba CREATE最新第1页27项；[缺DiffusionModelLoaderKJ讨论](https://tieba.baidu.com/p/11184926631) | 03:59列表，两个2024置顶与近期帖分开；非置顶日期跨过上轮水位；约04:01读取候选2楼 | 正文可读；回复“更新本体”只是社区建议，未见楼主验证，不写成确认修复教程。 |
| 贴吧全站补充 | 最新搜索“工作流 提示词”第1页25项 | 03:59，按tid去重并核对实际吧名、楼主日期 | 含其他吧与早于窗口的结果，补充线索，不冒称指定两吧全量搜索；未启动备用Astron。 |
| bilibili广泛发现 | SDK17.4.2按pubdate搜“ComfyUI 教程”1–4页共80条返回项；“生图模型”“Anima”“LoRA 画风”各1页20项 | 03:59–04:11，ComfyUI页日期由11月11日02:28回至11月9日21:32，跨过上轮水位；按BV去重筛选；两条候选取得完整简介 | 先过滤无关视频、重复整合包推广和泛变现标题；深入N10的画面／OCR／ASR，N01导读仅简介。各关键词有检索范围，不宣称覆盖全站；本轮未读评论。 |
| Sena404固定跟进 | UID341674866投稿第1页；补搜“Sena404 画师串”和“画师串” | 03:59投稿返回NetworkException；前一关键词0项，04:03后者20项可读，最新匹配仍为已存[第25期](https://www.bilibili.com/video/BV1mFWt6JEZn/) | 作者投稿入口未成功覆盖，不能据关键词结果断言没有更新。收录水位保持11月9日20:33第25期，不改成“已跟完”。 |
| Reddit | r/StableDiffusion new.json50、r/comfyui new.json30；中英文模型／LoRA／教程／工作流与H3新发布补搜 | 03:59左右两个最新列表均403；搜索多为早期H3视频／静帧流程；另打开[旧MOSS经验帖](https://www.reddit.com/r/StableDiffusion/comments/1xe1nmu/a_few_tips_for_moss/)的正文要点与首条评论片段 | 最新列表受限，原帖部分可读；旧帖绝对／相对日期显示不一致，未确定真实日期，不当本日新增。也未把旧H3视频流程写成新Image模型教程；未读全部评论或看图。 |
| Hugging Face | text-to-image按lastModified最新80，image-to-image最新30；随后按H3、pDMD和MOSS控制线索打开原卡 | 03:59列表，至04:08读取固定模型卡与两份小型示例JSON | N01–N03来源可读，分别标明卡片章节／JSON范围；不把API成功等同所有文件／图像已读，不下载大权重。 |
| GitHub | comfyui workflow pushed:>=2026-11-10按updated25；comfyui prompt created:>=2026-11-08按updated15；跟随原文追作者仓库 | 03:59起，读取候选README、创建／提交元数据和固定版本提示指南 | N07–N10及N01原作者资料；未安装项目。公开性、作者测试声明与本库实际运行状态分开；外部SKILL作为研究内容阅读。 |
| Civitai社区／模型／工作流 | 最新模型40、文章30、Workflows15；打开具体文章38537与版本3459553／3461875／3462243 | 03:59入口可读，随后读取正文／版本元数据 | N04–N07。文章、资源版本与方法说明可读；未看这些项目例图、读作品逐图配方／全部讨论，不能称全类别已深读。无优质新增与未取得图片分开处理。 |
| 其他有效论坛／作者资料 | forum.comfy.org/latest.json前30话题；note.com ComfyUI最新检索；原文外链 | 约03:59列表筛选 | Comfy论坛列表可读，部分已收录话题未有值得新增的已读内容，本轮未逐帖深读；note检索403。作者原始GitHub资料已按条目列出，不以列表标题冒称论坛正文已读。 |

B站没有配置可用登录会话，本轮未取得平台字幕；ASR明确为本库工具生成草稿。游客态限制按接口分别记录。未自动登录、提取Cookie、启用备用CLI或循环重试。音视频、抽帧、OCR原件、完整转录、凭据与带签名媒体地址不入库。

## 后续关注

- 继续区分官方H3-Image、上游pDMD训练成果和不同格式的包装；后续若版本或方法实质更新，回链本日，不把同源镜像反复算新增。
- MOSS控制LoRA的编码格式、参考图类型与具体模型分支，以及H3服务请求参数在各ComfyUI实现中的差异，须看各版本依据；未因能加载就认定完全兼容。
- 水彩与草图分享的参考价值先按作者方法保存；多组变化、粗指标和单seed范围不作为普遍美术定律。后续取得例图或精确配置再注明补读范围，不填私人配方。
- Sena404仍以第25期为已收录水位；作者投稿接口失败与关键词没有新匹配分开，下一轮继续按UID查询。Reddit、note与平台字幕的限制保留，不推断全网无更新。
- 本页为资料汇总；本轮全部条目均未在本库原样复跑、生成图片或获得用户效果认可。未来实际执行沿用明确授权与停止点，不由归档触发自动试验。

归档记录：2026-11-11首次整理10项主题；先保存本文，再同步总索引与阅读入口。详细读取与配置条件以各条原文和上述范围为准。
