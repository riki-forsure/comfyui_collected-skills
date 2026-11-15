# 2026-11-16 每日社区发现

本页汇总社区作者公开的模型、工作流、提示词教程与实践经验，感谢原作者的创作和分享。本文为本库概述／导读，保留署名、原文和实际读取范围；欢迎前往原帖看完整示范、配置、许可与更新，支持原作者。署名和链接不等于额外转载授权。

- 北京日期与检索时间：2026-11-16，03:57开始读取规范，03:58起查近期列表与原文，归档前持续补读。
- 类型：无具体差距要求的每日广泛发现；本轮没有另设主动专题。
- 执行状态：整理9项主题，部分入口受限；没有节点安装、模型下载、生成／实验或运行服务新增。
- 时间窗：优先接续11月15日各平台上次成功读取（约04:00附近）以来的新增／实质变化；近期首次收录的旧建仓资料另写原始日期，不把卡片更新当新训练完成日。
- 标注：适用方向与美术／设计摘要为本库分类；原作者说明、社区反馈、本库看图和运行验证各自记载。本次归档不等于生图效果验证。

## 今日值得阅读

- **模型与参考**：[Raehoshi MOSS](https://huggingface.co/Raelina/Raehoshi-Moss-Image)公开微调＋SFT差量合并条件；[Role Ref KV](https://huggingface.co/AnticPan/Anima-Role-Ref-KV)区分有无姿态图的v3／v2选择。
- **上色与场景训练**：[Manga Colorist](https://huggingface.co/moonrailgun/MOSS-MangaColorist-v1)说明漫画上色的重绘风险；[BB Channel制作日志](https://civitai.com/articles/38871)比较三维／二维化样本对布局与画法的影响。
- **设计与实践**：[H3 LayoutKit](https://github.com/benjiyaya/ComfyUI-H3Image-LayoutKit)将框选转为场景语言，[Sena第28期](https://www.bilibili.com/video/BV1wAsE6nE7A/)已核标签与关键画面；另有超现实摄影启发和角色拆部建模。

## 分享速查

| 类别 | 分享／资源与版本 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点／可学习经验 | 读取状态 |
|---|---|---|---|---|---|---|
| 后训练模型 | [Raehoshi MOSS v1.0：人物知识微调与SFT差量合并](#n01) | 人物插画·后训练选型｜查阅角色知识微调与该版本SLG配置。 | 美术风格方向：清爽日漫·分层柔影｜两例大眼小鼻口、柔和下颌，利落轮廓配色块明暗和发束亮边。 | Raelina；OpenMOSS及上游作者；[固定模型卡](https://huggingface.co/Raelina/Raehoshi-Moss-Image/blob/5a22cdd68458ee12af30fa88593301dd01c675ac/README.md) | Base微调后另合并SFT提取LoRA，配置范围单列 | 卡片全文、两张作者示范已看；未复跑 |
| 参考条件LoRA | [MOSS Manga Colorist v1：上色也可能重绘原画](#n02) | 漫画上色·参考工作流｜了解专用参考条件与原线稿保留的取舍。 | 设计思路：上色与重绘分开看｜参考整页明暗和色彩，同时检查脸部、线条与文字变化。 | moonrailgun；OpenMOSS、sorryhyun；示范漫画原作者空知英秋等；[固定模型卡](https://huggingface.co/moonrailgun/MOSS-MangaColorist-v1/blob/2b8a0fe5ddcc84abac270c0fdf43dd5aa6d302af/README.md) | 专用reference-conditioning，不等于普通img2img挂LoRA | 卡片、训练／参数JSON、一组比较图；未运行 |
| 角色／姿态参考 | [Anima Role Ref KV v3：姿态输入与身份输入分工](#n03) | 角色参考·姿态控制｜按有无姿态图选择v2或v3的参考路径。 | 设计思路：身份与姿态分工｜参考图给身份，姿态图给位置和体型，提示补服装场景。 | AnticPan；CircleStone、姿态资料与示范原作者；[固定模型卡](https://huggingface.co/AnticPan/Anima-Role-Ref-KV/blob/4a8990345f0f4932f643e1422a42aca2eeeca2ac/README.md) | v3新增姿态图；无姿态时作者仍推荐v2 | 卡片全文、案例文字与工作流节点；例图未看 |
| 背景LoRA训练实践 | [BB Channel：三维多机位与二维化数据的折中](#n04) | 背景训练·场景还原｜从单视角参考扩充多机位，并平衡画法与布局。 | 设计思路：几何锚定·画法转换｜用三维渲染保布局，用二维化样本教背景画法。 | RHU_AIstudio；Fate/Grand Order原场景作者及相关工具作者；[制作日志](https://civitai.com/articles/38871) · [精确版本](https://civitai.com/models/3052267?modelVersionId=3471267) | 10原渲染＋10二维化，发布选择v3而非v4 | 日志全文、资源版本元数据；例图／配置附件未读 |
| 设计思路随笔 | [超现实摄影：从暗房拼合到AI场景构思](#n05) | 摄影创意·视觉设计｜参考不可能场景、实体布景与图像拼合的思路。 | 设计思路：真实质感·不可能关系｜用摄影的可信外观组织漂浮、尺度错置和梦境空间。 | Maridizzle；文中致意的摄影与视觉艺术家；[原分享](https://civitai.com/articles/38921) | 方法与创作启发随笔，无具体模型／参数配方 | 正文全文；未核艺术史、作品图或LoRA合集 |
| 多主体布局节点 | [H3 Image LayoutKit：把框选位置翻译成场景语言](#n06) | 多主体关系·构图控制｜按参考图槽位与框的位置组织H3场景提示。 | 设计思路：位置与动作分写｜框选给相对位置，人物动作写在各自描述，场景保持连续。 | benjiyaya；MiniMax与ComfyUI上游作者；[固定README](https://github.com/benjiyaya/ComfyUI-H3Image-LayoutKit/blob/8e78c78dccfba7b07e4fd2a42e64a0101ad8a1e4/README.md) | 默认模板无需LLM，仍处开发中 | README全文；未运行节点或看示范 |
| 图像转3D工作流 | [PixelArtistry拆角色：局部解析度与接缝遮挡一起设计](#n07) | 角色资产·图像转3D｜将人物分部生成，再按相机与接缝组装低模。 | 设计思路：分部细化·接缝遮挡｜提高头手等局部占比，让胡须、护腕或布料覆盖拼接处。 | pixelartistry；Qwen、Microsoft、MostAadTech、UltraTex等作者；[固定README](https://github.com/pixelartistry/PixelArtistry-Split-Character/blob/4c90caf818abbae75f3a7a11a0815a8c98266df7/README.md) | Qwen拆部件→TRELLIS.2／贴图→Blender组装 | README全文；未读全套JSON或实际成品图 |
| Sena404增量／画风示范 | [Sena404第28期：butcha-u的体量、脸形与光泽](#n08) | 人物插画·画师标签｜参考本组体量与光泽表现，并保留易失误部位。 | 美术风格方向：圆润日漫·丰润体量｜本组圆脸大眼与收腰体量突出，渐层明暗配明确发束亮边。 | Sena404；butcha-u及原画师；[原视频](https://www.bilibili.com/video/BV1wAsE6nE7A/) | 投稿第28期／片内第38期分别记录 | 完整简介、54秒媒体、13张帧及OCR；标签已核 |
| 贴吧比较与实践 | [社区LoRA横评与MOSS提示探索：保留整套条件](#n09) | 模型比较·训练经验｜阅读跨家族LoRA实践，并核清比较条件差异。 | 设计思路：方案整体比较｜把训练数据、提示和过拟合一并记录，不只按模型名字排名。 | 神秘哀嚎者；青竹ddd及参与吧友；[训练比较](https://tieba.baidu.com/p/11199533253) · [MOSS实践](https://tieba.baidu.com/p/11198199578) | 不同数据／提示与私人LoRA不拼成通用配方 | 两帖首楼与可见楼层；图片／附件未看 |

## 当日分享

<a id="n01"></a>

### Raehoshi MOSS v1.0：人物知识微调与SFT差量合并

**适用方向：人物插画·后训练选型｜查阅角色知识微调与该版本SLG配置。**

**美术风格方向：清爽日漫·分层柔影｜两例大眼小鼻口、柔和下颌，利落轮廓配色块明暗和发束亮边。**

- 原作者与原文：Raelina，[Raehoshi Moss Image v1.0](https://huggingface.co/Raelina/Raehoshi-Moss-Image/blob/5a22cdd68458ee12af30fa88593301dd01c675ac/README.md)，固定`5a22cdd68458ee12af30fa88593301dd01c675ac`。北京时间11月15日20:18建立，20:43更新；本次首次收录。
- 原作者说明：MOSS-Image Base微调，称约1万张图、四种caption长度／格式，补充至2026年10月的鸣潮、绝区零、星铁及原神角色知识；训练末期另合并从MOSS SFT通过SVD提取的rank128 LoRA。训练路线与后期合并分开记录，不把整个资源称为仅换文件名的量化版。数据与训练规模未另核日志。
- 作者推荐：ER SDE／SGM Uniform、30–50步、CFG4–5，SLG单层`22,24,26`、开始0、结束0.5。作者特别强调SLG，但这属于本版本条件，不升级为MOSS全家族必须值；未取得两张示范各自的原生参数、seed、精确编码器／VAE文件。
- 本库实际看图：模型卡前两张作者示范（由卡片直达原图）。两例都是大眼、较厚上睫、小鼻口与柔和收窄下颌，细肩／手臂与清楚服装分区，轻笑或张口笑，手势增强互动。轮廓利落、色块明暗加轻渐层，头发成束高光，背景相对柔化。发色、饰物、服装及各次表情属于角色／示范设定；只见局部至大腿取景，不推断全身体型与头身。
- 读取状态：完整模型卡和两张公开示范；没有读取另外两图、权重、训练日志或图像元数据，也未做兼容／效果验证。画风短标注是这两例的本库归纳，训练与“增强角色知识”的说法属于原作者。

<a id="n02"></a>

### MOSS Manga Colorist v1：上色也可能重绘原画

**适用方向：漫画上色·参考工作流｜了解专用参考条件与原线稿保留的取舍。**

**设计思路：上色与重绘分开看｜参考整页明暗和色彩，同时检查脸部、线条与文字变化。**

- 原作者与原文：moonrailgun，[MOSS Manga Colorist v1](https://huggingface.co/moonrailgun/MOSS-MangaColorist-v1/blob/2b8a0fe5ddcc84abac270c0fdf43dd5aa6d302af/README.md)，固定`2b8a0fe5ddcc84abac270c0fdf43dd5aa6d302af`。11月14日04:12建仓、16日00:16更新，近期首次收录；不以更新日冒称训练首发日。
- 作者公开训练：2134对黑白／合成上色漫画页、42部作品，统一caption `comic`，rank32／alpha128、Muon、lr5e-5，共6402更新。元数据中的4268只计续训阶段；续接权重但重置优化器。以上由卡片和training_summary核对，未独立审计训练数据。
- 原配方：MOSS Base，`comic`文本提示及checkpoint的`sure`尾部行为，强度1、30步、CFG3、seed7、ER-SDE／shift5，负向分支skip层22；INT8 Transformer、FP32 residual、BF16文本编码器。参考图路径含对齐、隔离和时刻等条件，已在[anima_lora指定revision](https://github.com/sorryhyun/anima_lora/tree/83b8d6d582dd2e8d6cfea3494350b705098a3f81)验证，普通文生图LoRA加载器或一般img2img不足以重现。
- 本库实际看图：[《银魂》比较图](https://huggingface.co/moonrailgun/MOSS-MangaColorist-v1/resolve/2b8a0fe5ddcc84abac270c0fdf43dd5aa6d302af/examples/01_gintama/comparison.jpg)，原漫画作者空知英秋。右列出现暖色室内光、较强体积与毛发／脸部重绘，分镜和多处气泡仍可辨；不是只给原线条涂色。没有逐字校对文字或核原生PNG像素。
- 比较边界：Base列为BF16、50步、denoise0.7、逐页长提示，LoRA列为专用参考条件、INT8、30步、固定短提示；尺寸也不同。因此这是一组完整工作流比较，不支持把所有变化单独归因LoRA。作者6页展示为定性示范、不同程度接触过相关系列，不等于跨作品成功率。
- 读取范围：模型卡全文、training_summary、银魂parameters及上述比较JPEG；其他五页与完整推理配置／实现未继续读，未生图。权重Apache2.0不重新授权漫画作品；原漫画及出版方权利仍依原文署名与NOTICE理解。

<a id="n03"></a>

### Anima Role Ref KV v3：姿态输入与身份输入分工

**适用方向：角色参考·姿态控制｜按有无姿态图选择v2或v3的参考路径。**

**设计思路：身份与姿态分工｜参考图给身份，姿态图给位置和体型，提示补服装场景。**

- 原作者与原文：AnticPan，[Anima Role Ref KV v3.0](https://huggingface.co/AnticPan/Anima-Role-Ref-KV/blob/4a8990345f0f4932f643e1422a42aca2eeeca2ac/README.md)，固定`4a8990345f0f4932f643e1422a42aca2eeeca2ac`。仓库10月26日建立，11月15日23:00更新；当前读取v3.0，版本首发时间未单独核，按近期首次收录记载。
- 作者方法：身份图与可选姿态图分开；姿态画布按输出比例整理，运行器会整体拉伸。姿态图的体型、比例、衣物可能传入结果，不能把它仅当骨架角度信号。作者建议单角色清晰参考，粗姿态文字与图一致；改变服装、表情、环境仍由文本说明。
- 版本选择：v3专用于带姿态图的任务；无姿态图时作者仍建议v2，v3对服装／表情修改的遵循可能较低。“版本更高”不是所有任务更合适。开发集自动评判、一个训练seed的相似度／姿态命中数，不视为本库验证或普遍成功率。
- 接入条件：Anima Base v1.0、`qwen_3_06b_base`、Qwen Image VAE与随附runtime／节点；这些适配器不是可独立使用的普通LoRA。新权重要用支持pose_image的新runtime。Apply节点路径保留标准KSampler；内置采样节点另有自己的Euler循环，不能混为一条实现。
- 公开示例工作流已读取节点／连线：v3 Apply + KSampler，832×1216、28步、CFG4、Euler/simple、denoise1，ModelSamplingSD3 shift3，角色图与姿态图分别进入Apply。其他LoRA在Apply前，作者给的兼容说明不延伸到未核的扩层Anima。
- 读取状态：完整卡片、[v3案例文字及署名](https://huggingface.co/AnticPan/Anima-Role-Ref-KV/blob/4a8990345f0f4932f643e1422a42aca2eeeca2ac/assets/v3.0/CASES.md)、公开工作流JSON节点与连线；示范图、EVALUATION细则及源码未进一步读，无成图观察／运行。负向去白背景建议也可能使图更暗、更饱和，是作者提醒的取舍。

<a id="n04"></a>

### BB Channel：三维多机位与二维化数据的折中

**适用方向：背景训练·场景还原｜从单视角参考扩充多机位，并平衡画法与布局。**

**设计思路：几何锚定·画法转换｜用三维渲染保布局，用二维化样本教背景画法。**

- 原作者与原文：RHU_AIstudio，[How I Made the BB Channel LoRA](https://civitai.com/articles/38871)，11月15日06:26:51；[BB Channel模型版本3471267](https://civitai.com/models/3052267?modelVersionId=3471267)显示MOSS-sft03，原发布时间05:50:53。文章以v1–v4描述试验，发布选v3；保留模型站显示名与实验编号，不自作同名版本推断。
- 方法：目标是一个有固定家具、标志与屏幕的具体演播室，而非泛化“新闻厅”类别。作者从游戏截图出发，用Blender重建，再取得10个机位渲染；标志、樱花图案和沙发相对位置分别修正。这是原作者的制作记录，本库未参与其建模／工具调用。
- 训练取舍：v1只用渲染，布局较准但CG感明显；v2只用二维化转换，画法变化但家具漂移；v3合用10原渲染＋10二维转换、对应机位同caption。v4改用另一绘画化插件仍有残余立体感／桌位漂移，作者选择v3。属于其整套方案比较，不是本库复验的单变量定律。
- 公开配置：MOSS SFT INT8，kohya sd-scripts，rank/alpha16，lr5e-5恒定、adamw8bit、1024、batch1、1000步、seed42，20图各10repeats；触发`bb_channel_(fate)`，作者推荐强度1。NEWS文字最脆弱、家具位置仍可变，不承诺像素级场景重建。
- 读取状态：文章全文、原资源作者与精确版本时间，未看示范图、渲染源、完整训练JSON或权重。原场景来自Fate/Grand Order，本文感谢并保留原场景来源，不把社区重建或本库摘要称为官方资产／原创场景。

<a id="n05"></a>

### 超现实摄影：从暗房拼合到AI场景构思

**适用方向：摄影创意·视觉设计｜参考不可能场景、实体布景与图像拼合的思路。**

**设计思路：真实质感·不可能关系｜用摄影的可信外观组织漂浮、尺度错置和梦境空间。**

- 原作者与原文：Maridizzle，[Surreal Photography: Dreaming With a Camera, From the Darkroom to the Machine](https://civitai.com/articles/38921)，11月16日00:01:53发布。
- 原分享内容：作者从暗房叠印、扫描／数字拼合、实体大布景等路线谈自己的AI超现实摄影灵感，并向Man Ray、Lee Miller、Jerry Uelsmann、Maggie Taylor、David LaChapelle、Tim Walker等创作者致意。本条为设计随笔导读，不强改为参数教程。
- 本库概述：画面可同时保持摄影材质的可信感和关系上的不可能——漂浮空间、器物与人体尺度错置、不同来源物体的梦境组合；数字拼合和实体造景是不同的实现选择。适合先构思对象关系／场景隐喻，再决定媒介与制作方式，不要求只有一种具体画风。
- 读取边界：正文全文；文中艺术史日期、人物履历和“28次拍摄”等轶事未独立求证，本文不将其复述为考据结论。作者提及个人LoRA合集，但未给本轮可核的精确权重、参数和示范元数据，本库未继续取图，也没有视觉／生图收益判断。
- 来源与尊重：具体艺术家的作品与方法归原作者，本文只总结社区分享中的设计启发，引导读者回原文及原艺术家资料继续阅读。

<a id="n06"></a>

### H3 Image LayoutKit：把框选位置翻译成场景语言

**适用方向：多主体关系·构图控制｜按参考图槽位与框的位置组织H3场景提示。**

**设计思路：位置与动作分写｜框选给相对位置，人物动作写在各自描述，场景保持连续。**

- 原作者与原文：benjiyaya，[ComfyUI-H3Image-LayoutKit](https://github.com/benjiyaya/ComfyUI-H3Image-LayoutKit/blob/8e78c78dccfba7b07e4fd2a42e64a0101ad8a1e4/README.md)，11月15日19:59建仓，固定`8e78c78dccfba7b07e4fd2a42e64a0101ad8a1e4`提交于16日00:34。作者明确仍在开发／优化。
- 方法：BBox Canvas产生布局JSON，Prompt Builder把框翻译成左／右区域、宽度占比、相邻间距等关系文字；默认不需要LLM。统一环境、地面、机位与光线的声明用于减少分屏倾向，人物动作各写到该框的description，extra_brief只管全场景。
- 位置表达：relational默认不输出坐标数字；both／coords保留0–1000原始坐标。作者称实测数字可能被画成网格标尺，这是其项目经验，本库没有A/B。输出仍是文本约束，不能称模型内部硬性区域隔离。
- 参考槽位：干净环境图直接进入指定Picture槽，人物参考依实际image_N匹配；空描述时框按左到右自动绑定后续人物图。env_picture必须指向真正环境，不因默认1而忽略现有接线。README明确preview只作检查、不送H3条件图，不能把画框预览等同有效参考。
- 可选LLM重写若带入box／panel等导引词或生成失败会回退模板；这描述软件防护，不证明生成一定不分屏。适用旧LiteGraph／Nodes1.0前端，其他前端未核。
- 读取范围：固定README全文与接线文字；没有运行应用、取得示范／工作流JSON、检查源码或图像效果。代码MIT，模型与其他依赖许可另看各来源。

<a id="n07"></a>

### PixelArtistry拆角色：局部解析度与接缝遮挡一起设计

**适用方向：角色资产·图像转3D｜将人物分部生成，再按相机与接缝组装低模。**

**设计思路：分部细化·接缝遮挡｜提高头手等局部占比，让胡须、护腕或布料覆盖拼接处。**

- 原作者与原文：pixelartistry，[PixelArtistry Split Character](https://github.com/pixelartistry/PixelArtistry-Split-Character/blob/4c90caf818abbae75f3a7a11a0815a8c98266df7/README.md)，仓库11月11日01:22建立，所读提交`4c90caf818abbae75f3a7a11a0815a8c98266df7`为16日03:34，本次首次收录。
- 方法：Qwen Image2.1从正面角色图裁切并独立处理头、身体、护腕手臂、腿等，部件尽量填满画面；TRELLIS.2配合WTiVo／LODTailor／Bake Forger／UltraTex得到带纹理低模，最后Blender对齐。清晰度来自整套分部流程，不直接归因为某一个节点。
- 可学习的设计取舍：保留同一相机／尺度并明确哪些外观不能重设计；每个部件携带遮缝物，胡须盖颈、护腕／绑带盖肢体接缝。换角色时裁切框、遮挡物和提示要重定，不能照抄独眼角色的像素坐标。
- 原作者配置示例：身体1536、局部1024；局部relative_voxel_size0.005，避免过细导致碎片，分辨率盲目升高可能带来巨量面。Qwen例为25步、CFG1、Euler/simple、seed56；TRELLIS结构／形状／放大／贴图另有独立seed，不当作同一个采样过程。
- 适用条件：作者测试Windows、RTX5080 16GB及特定ComfyUI／Blender版本，3D链路需额外模型和工具。README对TRELLIS与另一工具的差异属于其案例，不推断所有图像转3D系统必然如此。
- 读取状态：README全文、公开部件设置和故障处理文字；未看图片、打开完整工作流／提示文件、安装或生成／组装。工作流／文档MIT与各模型许可分开，原示范角色也不因此成为本库资产。

<a id="n08"></a>

### Sena404第28期：butcha-u的体量、脸形与光泽

**适用方向：人物插画·画师标签｜参考本组体量与光泽表现，并保留易失误部位。**

**美术风格方向：圆润日漫·丰润体量｜本组圆脸大眼与收腰体量突出，渐层明暗配明确发束亮边。**

- 原作者与原文：Sena404（UID341674866），[anima画师串第二十八期](https://www.bilibili.com/video/BV1wAsE6nE7A/)，11月15日12:20:43发布。封面内部第38期，日期2026.11.15，两种编号分列；接续[投稿第27期](../2026-11-14/README.md#n08)，不据编号补造中间期。
- 字面标签：`@butcha-u`，2秒封面已对照；卡片将Butcha-U与“勇虫”并列介绍，履历和图库数量未另核，不将卡片统计当质量依据。
- 原作者卡片概述：油润浓艳的厚涂渐变、明确轮廓光／高光，人物比例扎实、丰润体型与圆脸大眼；也称角色长相趋同，列出仰视全身多余手部和复杂道具缠绕等失败。所谓“迁移最强／稳定”等是其本组评价，本库没有核20张完整样本或比较统计。
- 本库实际看图：常规／末秒10帧，加2、31、35秒3定点帧。可见收腰且肩胸／腰胯体量明显的角色、圆润脸颊、大眼、小鼻口，微笑／眨眼及举手互动；立体渐层与亮边突出服装、皮肤和发束。制服、具体服饰与角色发色属于内容设定；被头盔／取景遮住的部位不推断，未把此组等同原画师全部创作倾向。
- 配方缺口：简介为“-”，这批帧没有取得完整逐图正负提示、底模／LoRA精确文件、seed与采样设置；不继承第27或更早期的参数。未取得平台字幕、评论、作者附件或原生示范PNG。
- 工具与水位：UID最新投稿接口NetworkException，经Anima最新搜索找到具体BV，SDK媒体／FFmpeg与中英OCR成功并人工核关键卡；没有ASR。收录水位推进至投稿28／片内38，系列索引随之更新；媒体取得不等于逐帧阅读。

<a id="n09"></a>

### 社区LoRA横评与MOSS提示探索：保留整套条件

**适用方向：模型比较·训练经验｜阅读跨家族LoRA实践，并核清比较条件差异。**

**设计思路：方案整体比较｜把训练数据、提示和过拟合一并记录，不只按模型名字排名。**

- 原作者与原文：神秘哀嚎者，[目前主流模型学习能力对比，第2弹](https://tieba.baidu.com/p/11199533253)，stablediffusion吧，11月15日21:30:47；另读青竹ddd，[感觉我已经玩明白moss image了](https://tieba.baidu.com/p/11198199578)，11:02:44。
- 横评帖分享：作者尝试MOSS、Krea2、Anima、Illustrious的LoRA训练与生成，主动补充说明训练图随时间有增减、提示按模型优化，Anima一项训练过拟合。因此可作为社区方案记录，不能称完全相同数据／提示的严格架构横评，也不从标题推出哪个家族学习能力绝对更高。
- MOSS实践：楼主说明使用自己训练的两个LoRA，以及通过Gemini反复调整选出的提示；完整词串、LoRA文件与版本没有取得。其他吧友提到商业插画／背景用途和高步数耗时，这是其个人反馈，不是楼主每张图的实际配置。
- 本库整理备注：比较应保留训练集差异、解析方式、参数、所用资源和失败例；私人配置不拿公开推荐补齐。字数较长或“感觉玩明白”不单独证明效果。本库未看图，故本条概括比较／探索方法，不给具体美术视觉判断。
- 读取范围：横评帖可见2楼、MOSS帖可见6楼文字；未看图片、楼中楼、外部LoRA下载或原作者配置。原文用途／使用限制保留在原帖，不将未核下载名当精确版本链接。

## 实际平台覆盖与未精选线索

| 来源 | 本轮实际入口与范围 | 结果／限制 |
|---|---|---|
| stablediffusion吧 | aiotieba4.8.2，CREATE第1页30项，去置顶后日期跨上次窗口；补读3候选 | 两帖组成N09；[Anima画师提示不生效](https://tieba.baidu.com/p/11198319315)读3楼，回复涉及版本／底模影响但未给可核配置／对照，作为问题线索，不称已解决。未看主题图片与全部楼中楼。 |
| comfyui吧 | 同工具CREATE第1页28项，2024置顶另记，窗口内3个新主题；读[H3三合一分享](https://tieba.baidu.com/p/11199642020)首楼 | 正文为网盘／整合包推广及资源简介，未取得可核原作者工作流或配置，不精选。另两条为硬件／口型提问，仅列表，不假称已读正文。 |
| 吧名／全站 | `stable diffusion`空格入口实测仍转stable旧公告，实际规范吧名stablediffusion；全站最新“工作流 提示词”第1页26项 | 按实际吧名和tid去重；不同吧／推广不冒充两吧覆盖。无新精选与接口失败分开，未启用Astron或检查其依赖。 |
| bilibili广泛发现 | SDK17.4.2，pubdate排序：“ComfyUI 教程”3页各20，页3到11月14日20:49，跨上次窗口；“生图 模型”“Anima”“LoRA 画风”各1页20 | 按BV去重并排除无关音乐与整合包广告。Sena28与[余小文AIGC《MOSS-Image图片参考生图》](https://www.bilibili.com/video/BV14EsW6yEBX/)完整简介已读，后者59秒、简介只称参考／反推，未取得有效节点，不能当作已确认图像参考注入方案。 |
| Sena404与媒体 | UID341674866最新投稿NetworkException；Anima搜索定位BV1wAsE6nE7A；info／公开媒体／FFmpeg／中英OCR成功 | 54秒媒体，10常规／末帧＋3定点帧已看；水位28／片内38。未取平台字幕、评论或ASR；已有工具复用，没有自动登录或Cookie提取，未启用备用下载器。 |
| Reddit | r/StableDiffusion new50和r/comfyui new30均403；2条英文类别／日期站内发现查询，打开[Minute-Art-8313工作流求助](https://www.reddit.com/r/comfyui/comments/1xwpyca/help_me_improve_my_workflow/) | 正文及可见一组回复可读：楼主使用Anime Screenshot Merge IL v4，询问转模型；回复是通用建议，未看目标图／工作流，不把转到Anima／MOSS自动当收益。搜索标11月15日、原页相对时间，精确时刻未核；最新列表仍受限。 |
| Hugging Face | 最近修改text-to-image80项、image-to-image30项；读取5份候选卡，精选3份并补关键JSON／图 | Raehoshi、Manga Colorist、Role Ref KV归档；ARAZmixKREA卡明确无额外训练的合并，正文多为分发说明，Reflora仅短提示／训练线索，未取得充分方法细节。镜像、量化和同源副本不重复算新训练。 |
| GitHub | 工作流／节点更新25项、提示相关新仓库15项；打开LayoutKit、PixelArtistry与Prompt Workbench README入口 | 前两份全文归档；Prompt Workbench仓库／提交可得，但README端点404，未循环试路径或当作已读教程。没有安装、测试或完整源码审计。 |
| Civitai社区 | 最新模型40、文章30、工作流15；打开BB制作日志、超现实摄影随笔、摄影比较文章及BB精确版本 | 精选文章方法与模型版本实际读取；[yellorn的MOSS／FLUX摄影比较](https://civitai.com/articles/38915)只读摘要／硬件与方法前段，未核全部图／结果／配置，不采纳“冠军／8.7倍”作为本库结论。模型列表与工作流列表成功不等于每项正文、作品配方或评论都已读。 |
| 其他论坛 | ComfyUI Forum最新30主题列表成功；note.com近期ComfyUI入口403 | 新主题主要为界面／扩展求助，未深读其正文；无新精选。论坛旧下线公告的标题／正文日期冲突沿用[11月15日来源记录](../2026-11-15/README.md)，本轮未重读正文，不称已核最新变化。note.com为受限，不写无新增。 |

## 后续关注与维护

- 关注Role Ref KV运行器与姿态输入条件、漫画上色对原画／文字的改动、Raehoshi训练与合并版本。当前只有作者说明与有限示范，不扩大为跨任务稳定收益。
- 背景LoRA的数据几何与画法取舍、布局工具的图片槽位、拆部建模的相机与遮缝方法都值得回原文细读；未取得的图／配置留缺口，不补造。
- Sena404推进至投稿第28期／片内第38期，BV1wAsE6nE7A，系列索引及工具跟进水位同步。UID列表本轮仍失败，不将搜索定位成功包装为作者所有新稿已覆盖。
- 已读正文及时归档，缺字幕、附件或访问限制不阻塞其他资料保存；同日补读更新此目录，版本变化回链旧记录。
- 本页先保存，再更新总索引、首页与每日入口。原媒体、截图、完整OCR／ASR、凭据和临时签名链接不提交GitHub；没有生成／训练、运行服务或子代理派发。

[返回总索引](../../每日检索可速查总结.md) · [每日归档说明](../README.md)
