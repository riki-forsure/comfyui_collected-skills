# 2026-11-19 每日社区发现

本页汇总社区作者公开的模型、教程、工具与实践经验，感谢原作者的投入。正文是本库中文概述与导读，保留作者、原文、版本与读取范围；欢迎回到原帖阅读完整教程、查看示范与更新，支持原作者。署名／链接不等于额外转载授权，第三方成果不作为本库原创。

- 北京日期与实际检索时间：2026-11-19，04:00起读取仓库最新规范，04:01起查各平台，04:09前完成下列原文与抽样画面阅读。
- 检索类型：无具体差距要求的每日广泛发现；本轮没有另设主动搜索专题。
- 执行状态：整理11项主题，含编辑／贴图特化LoRA、新版本、专用小模型、工作流、提示工具与社区经验；部分入口／图片受限。
- 时间窗：接续[11月18日](../2026-11-18/README.md)成功读取水位（约04:05起），优先新增与实质变化；近7日首次收录及旧工具的新教程保留原日期。建仓、提交、发布与训练完成日期不互换。
- 边界：仅读取与汇总；未安装节点、下载生图权重、启动训练／生成／自动实验、增加运行服务或派发子代理。视频深读只复用现有工具与ASR缓存。归档、阅读、看图和收益验证分别记录。
- 浏览标注：适用方向、美术风格／设计思路属于本库整理，帮助选择用途，不等于效果已验证。

## 今日值得阅读

- **局部编辑与后训练**：[RMS两类Klein LoRA](https://huggingface.co/rmstools/RMSedit-FLUX.2-klein-9B-fill-replace-lora)区分“遮白重建”和“保留物体做融合”；[Sint Albedo MOSS 1.1](https://civitai.com/models/3049124?modelVersionId=3476030)按材料诚实记录接缝局限。
- **工作流与组合方法**：[PotatCat局部重绘教程](https://civitai.com/articles/39134)讲裁切、padding、软边和局部框；[Krea2 SVD合并](https://civitai.com/articles/39126)区分固定组合、降秩与误差；OmniLoRA提供图内训练流程的beta方案。
- **提示与社区实践**：新增梧桐提示词站与NL2Prompt导读，以及[H3多图参考分工](https://www.bilibili.com/video/BV13BsS6oEgV/?p=1)视频／文字经验。Sena404投稿页本次可读，最新仍第29期，保持既有水位。

## 分享速查

| 类别 | 分享／资源与版本 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点／可学习经验 | 读取状态 |
|---|---|---|---|---|---|---|
| 编辑特化LoRA | [RMSedit与RMSharmonize：填补和光影融合各有分工](#n01) | 局部编辑·合成修整｜用Klein 9B专用LoRA分别填补区域与协调光影。 | 设计思路：遮去旧内容·保留融合对象｜替换时遮白目标，融合时保留物体并留出阴影空间。 | RMS／rmstools；BFL与Ostris等上游作者；[RMSedit模型卡](https://huggingface.co/rmstools/RMSedit-FLUX.2-klein-9B-fill-replace-lora/blob/1f2810260e51e19b286abb732edb1d124233a93c/README.md) · [RMSharmonize模型卡](https://huggingface.co/rmstools/RMSharmonize-FLUX.2-klein-9B-harmonization-lora/blob/e7d2857e65d5e67b811d5b3ad1c4ce930dc3deb6/README.md) | 两项独立训练的适配器；遮白输入与工作流蒙版并非同一条件 | 两份卡片全文、各1张原对照图；未复跑 |
| 游戏贴图LoRA更新 | [Sint Albedo MOSS 1.1：按材料记录接缝表现](#n02) | 游戏贴图·材质生成｜查阅MOSS与Krea专用版本的平面albedo用途。 | 设计思路：平面材质·接缝训练｜去除烘焙光照，并通过跨边界样本学习纹理延续。 | AriaMaiven；MOSS／Krea基座作者；[MOSS 1.1／3476030](https://civitai.com/models/3049124?modelVersionId=3476030) | 不是完整PBR，也不保证所有材料原生无缝 | 资源描述、3版本说明与元数据；图片403 |
| 场景风格LoRA | [Big Cities：巨构城市提示方法与新ZIT版本](#n03) | 场景背景·空间尺度｜用建筑类型、气象和视点组织巨构城市提示。 | 美术风格方向：巨构奇观·层叠雾景｜按作者描述，以山岳尺度建筑和微小人群表现纵深。 | AriaMaiven；Krea／Z-Image基座作者；[Krea 1.0／3473431](https://civitai.com/models/3053843?modelVersionId=3473431) · [ZIT 1.0／3478356](https://civitai.com/models/3053843?modelVersionId=3478356) | Krea文字教程可读；新ZIT未提供独立参数 | 资源描述、2版本元数据；图片403 |
| 专用小模型 | [Tiny Pixel-Art：英阿双语16×16 RGBA精灵](#n04) | 像素素材·双语提示｜了解16×16透明像素精灵的原生小模型入口。 | 美术风格方向：低分辨率像素画｜按模型卡，以固定调色板生成16×16 RGBA精灵。 | nomeda-lab；数据作者Angais与Krea相关作者；[固定模型卡](https://huggingface.co/nomeda-lab/pixel-art-tiny-adaptive/blob/1f3d878bf8a23e2c334a727568dc802720d0bdda/README.md) | 自定义自回归模型；不是扩散LoRA或现成Comfy节点 | 模型卡全文、文件元数据；无例图观察 |
| 局部重绘教程更新 | [PotatCat MOSS inpaint 1.1：裁切、蒙版与区域提示](#n05) | 局部重绘·区域提示｜按修改范围选择裁切或整图，并组织局部提示。 | 设计思路：保留上下文·分区说明｜用padding与软边衔接，再以框选描述不同修改。 | PotatCat；MOSS与节点作者；[原教程39134](https://civitai.com/articles/39134) · [Moss V1.1／3478634](https://civitai.com/models/128556?modelVersionId=3478634) | 新加bounding boxes和Spectrum；参数职责分开 | 教程全文、版本描述／元数据；未取JSON或看图 |
| LoRA组合工具导读 | [Krea2 SVD Merger：固定组合与秩截断分开看](#n06) | LoRA组合·资源整理｜查阅CPU合并、固定系数与降秩误差说明。 | 设计思路：固定组合·保留取舍｜将已选搭配固化为一份权重，压缩误差另行评价。 | dbodik242238／dbodik-git；相关LoRA作者；[社区教程39126](https://civitai.com/articles/39126) · [固定README](https://github.com/dbodik-git/Krea2_SVD_LoRA_Merger/blob/5e751e63c0f17d3f7772c7578ae828cf4550651b/README.md) | 仅2D线性LoRA；不支持LoKr／LoHa／Conv | 文章全文、README方法与限制；未读源码／运行 |
| 图内训练工具分享 | [OmniLoRA：数据预缓存、训练与观察接入节点图](#n07) | LoRA训练·工作流组织｜了解图内数据准备、分段训练与检查点的组织方式。 | — | pente5／cyberterm及贡献者；ComfyUI与基座作者；[Reddit作者帖](https://www.reddit.com/r/StableDiffusion/comments/1xypn77/introducing_omnilora_train_any_model_on_any_gpu/) · [固定README](https://github.com/cyberterm/ComfyUI-OmniLoRA/blob/5c913f5b705a18af8bc62cd0bd7313294e50c4d9/README.md) | 广泛兼容是beta目标；作者明确尚未遍测全部硬件 | 原帖与可见回复、README入门／模板／节点段；未运行 |
| 提示组织节点 | [NL2Prompt：提示拼装与LoRA真正加载分两步](#n08) | 提示词组织·LoRA管理｜从自然语言组织提示，并区分推荐列表和实际加载。 | 设计思路：角色与风格分库｜分别维护触发词和权重，再检查最终提示及加载状态。 | GQLI-VC及贡献者；ComfyUI与所用LLM作者；[固定README](https://github.com/GQLi-VC/ComfyUI-NL2Prompt/blob/83ff353ae0967a308b82c6ebf9184b1e96915e4b/README.md) | 可不接LLM；lora_stack推荐不等于模型已打补丁 | README功能／接线／限制段；未读源码或运行 |
| 贴吧工具分享 | [梧桐提示词站4.0.7：选词、资源和配方分别保存](#n09) | 提示词组织·资源管理｜集中整理标签、画师串与LoRA，再连接既有引擎。 | 设计思路：文字与资源独立｜替换提示片段时保留LoRA设置，画风资料记录原来源。 | Juu_Suzuko；GitHub发布者xialing114514及致谢作者；[贴吧原帖](https://tieba.baidu.com/p/11208431241) · [固定README](https://github.com/xialing114514/mioha-prompt-station/blob/18c116f71dae5adfe12c0c43908f85e2221e8c7b/README.md) | 公开安装包、规则与文档；程序源码暂未公开 | 首楼与2条可见回复、GitHub README全文；未运行 |
| 多图编辑与提示实践 | [H3多图编辑：参考图分工与保留程度](#n10) | 多图编辑·提示组织｜分别指定人物、衣装、场景与动作的参考职责。 | 设计思路：逐图分工·保留程度｜明确每图贡献和允许改动，再说明最终场景关系。 | MiniMaxH3image；Reddit u/Subushie与参与讨论者；模型和节点作者；[B站首P教程](https://www.bilibili.com/video/BV13BsS6oEgV/?p=1) · [Reddit原讨论](https://www.reddit.com/r/comfyui/comments/1xz07b3/h3_image_edit_model_is_wild_tips_on_usage_based/) | 视频输入区与文字组织相互参考；不是同一配置的两次验证 | 完整简介、首P16抽样帧／OCR、ASR草稿；原帖及可见回复 |
| 贴吧采样实践 | [MOSS加速双采：低分辨率起图后放大续采](#n11) | 采样精修·效率取舍｜参考低分辨率起图与放大续采的社区设置。 | — | 鲜虾云吞面豪赤；参与讨论吧友；[原帖11208322549](https://tieba.baidu.com/p/11208322549) | 保留作者记录与未说明项，不作完整复现配方 | 首楼及1条可见回复；图片／硬件／完整参数未取 |

## 当日分享

<a id="n01"></a>

### RMSedit与RMSharmonize：填补和光影融合各有分工

**适用方向：局部编辑·合成修整｜用Klein 9B专用LoRA分别填补区域与协调光影。**

**设计思路：遮去旧内容·保留融合对象｜替换时遮白目标，融合时保留物体并留出阴影空间。**

- 原作者与日期：RMS／rmstools，Hugging Face，两仓分别创建于北京11月18日14:34、14:38；卡片最后更新分别23:09、15:22。本次首次收录，固定revision分别为`1f2810260e51e19b286abb732edb1d124233a93c`、`e7d2857e65d5e67b811d5b3ad1c4ce930dc3deb6`，不将卡片更新时间当训练完成时间。
- 作者分享：RMSedit针对输入中涂成纯白的区域训练Fill／Replace两种任务；Fill延续周围纹理，Replace按文字重建新内容。局部应用还需要匹配的工作流蒙版，白色像素负责视觉引导，蒙版负责限定修改／合成范围，二者分开。
- RMSharmonize则先把物体按目标位置与比例贴入，保留物体图像信息，再协调照明、阴影与色调；局部蒙版需包含投影和邻近用光区域。不要套用RMSedit的“把物体涂白”做法。
- 公开条件：两者均在FLUX.2 Klein Base 9B上用作者本地生成／整理数据、Ostris AI Toolkit训练，作者说明没有混入第三方LoRA。文件分别`flux2_klein_rmsedit.safetensors`与`flux2_klein_rmsharmonize.safetensors`，触发词`rmsedit`／`rmsharmonize`，建议强度1.0。示例使用Klein 9B INT8 ConvRot、2步；这是示范条件，未给出完整采样器、seed和实际工作流，不能外推到所有9B变体。
- 本库实际看图：RMSedit的[greenery三栏对照](https://huggingface.co/rmstools/RMSedit-FLUX.2-klein-9B-fill-replace-lora/blob/1f2810260e51e19b286abb732edb1d124233a93c/images/greenery.png)中，右栏植物沿上方与左侧原白区组织，保留室内空间；RMSharmonize的[ball三栏对照](https://huggingface.co/rmstools/RMSharmonize-FLUX.2-klein-9B-harmonization-lora/blob/e7d2857e65d5e67b811d5b3ad1c4ce930dc3deb6/images/ball.png)右栏球面明暗和落地投影更明确。只观察各一例的布局和用光，不据此统计成功率或声称所有细节不变。
- 边界与署名：作者提醒复杂边缘、小细节、文字／logo及物体几何可能改变；权重遵循FLUX Non-Commercial License v2.1及基座条件。本库为中文概述，未复制完整提示词、下载权重或执行生图。

<a id="n02"></a>

### Sint Albedo MOSS 1.1：按材料记录接缝表现

**适用方向：游戏贴图·材质生成｜查阅MOSS与Krea专用版本的平面albedo用途。**

**设计思路：平面材质·接缝训练｜去除烘焙光照，并通过跨边界样本学习纹理延续。**

- 原作者与原文：AriaMaiven，Civitai，[Sint Albedo · Tileable Game Textures - Krea/MOSS](https://civitai.com/models/3049124?modelVersionId=3476030)。MOSS 1.1版本3476030于北京11月19日03:43发布；MOSS 1.0版本3475443于16日发布，Krea 1.0版本3467205于13日发布。本轮首次收录并记录1.1变化。
- 作者定位：俯视、平面、无烘焙高光／投影的albedo图，按材料及局部变化写提示；法线、粗糙度和高度图另由其他工具生成。只用正方形，宽图会破坏重复；用large stones、close-up等说明尺度。
- 实质变化：作者说1.1重新训练，将一半训练图的接缝置于画面中间，以学习跨边界连续。其2×2检查中，岩浆与裂土两颗seed都有延续但仍留细线；石头、水晶和锁子甲仅一颗seed较好；人字木地板与手绘草地仍断裂。此为作者小样本反馈，不能简化为“无缝已解决”。
- 作者设置：MOSS 1.1在Base上训练、示范用MOSS Image SFT，30步、CFG3、euler/simple、1024²、强度1.0，首词`sintalbedo`；Krea版另列Krea2 Turbo、10步、CFG1。两个基座有独立权重，不互换。
- 读取状态：已读资源全文与MOSS 1.1／1.0描述、版本元数据。尝试读取1.1两张示范均403，未实际看图，以上接缝结果和材质方向按作者描述；未取图像元数据、权重、工作流或运行。本库不搬运例图；作者要求重传权重或用输出训练需先取得其许可。

<a id="n03"></a>

### Big Cities：巨构城市提示方法与新ZIT版本

**适用方向：场景背景·空间尺度｜用建筑类型、气象和视点组织巨构城市提示。**

**美术风格方向：巨构奇观·层叠雾景｜按作者描述，以山岳尺度建筑和微小人群表现纵深。**

- 原作者与原文：AriaMaiven，Civitai，Big Cities · Colossal Cityscapes。Krea 1.0于北京11月16日21:55发布，作为近期首次补录；新ZIT 1.0／3478356在19日03:59发布，baseModel标ZImageTurbo，另记新版本，不能沿用标题认定两版都是Krea。
- 作者设计方法：先写建筑传统、混入的现代设施、天气、时刻和观察位置，再用一句朴素尺度描述加强。作者建议用建筑类型而非著名地标名字，避免模型回到熟悉的明信片尺度；远景／高视点更能呈现体量，室内与街面视角较受限。
- Krea原文推荐：`bgctysint`放首词，强度1.3（1.0雾与纵深较弱），Krea2 Turbo、10步、CFG1、euler/simple、1344×768。作者称工作流在该版本附件中；本轮未取JSON或seed。
- ZIT版仅核到版本、基座和同名触发词；资源正文仍写Krea条件，不能据此推定ZIT也采用相同强度／步数／CFG或同等视觉表现。
- 风格概述按作者对巨大建筑、层叠雾气、暖光与微小人群的文字说明。Krea版本两张示范请求403，本库未看图，不附人物／五官推断。权重重传或以输出另训需按作者许可；本轮只做链接导读。

<a id="n04"></a>

### Tiny Pixel-Art：英阿双语16×16 RGBA精灵

**适用方向：像素素材·双语提示｜了解16×16透明像素精灵的原生小模型入口。**

**美术风格方向：低分辨率像素画｜按模型卡，以固定调色板生成16×16 RGBA精灵。**

- 原作者与原文：nomeda-lab，[Tiny Arabic/English Pixel-Art Generator](https://huggingface.co/nomeda-lab/pixel-art-tiny-adaptive/blob/1f3d878bf8a23e2c334a727568dc802720d0bdda/README.md)，仓库创建北京11月17日19:52，更新11月19日00:22；revision为`1f3d878bf8a23e2c334a727568dc802720d0bdda`。首次收录，不将建仓等同公开首训日。
- 作者说明：约2449.7万活跃参数的条件自回归模型，支持英语、现代标准阿拉伯语、埃及阿拉伯语及混合短提示；输出256个原生调色板索引，组成16×16 RGBA，不是先生成大图再缩小。
- 使用条件：自定义PyTorch checkpoint与随仓`pixelgen`推理包，config／model.pt／tokenizer／palette组合使用；不是diffusers pipeline，也没有核到ComfyUI加载节点。适合作为极小透明素材路线参考，不按参数量推断质量优于其他模型。
- 数据与许可：卡片称训练数据Angais/pixel-art-atlas-1.4m由Krea2 Turbo生成，标CC0但有来源说明；代码MIT不自动消除数据与基座相关条件。数据卡和样本尚未补读，不能据本条概述承诺任意商用。
- 读取状态：模型卡全文、公开文件列表与版本元数据；未读数据集原卡、源码或看精灵样图，没有下载权重／运行。文中的验证loss只是作者训练指标，不当美术质量评价。

<a id="n05"></a>

### PotatCat MOSS inpaint 1.1：裁切、蒙版与区域提示

**适用方向：局部重绘·区域提示｜按修改范围选择裁切或整图，并组织局部提示。**

**设计思路：保留上下文·分区说明｜用padding与软边衔接，再以框选描述不同修改。**

- 原作者与原文：PotatCat，Civitai，[How to use potatcats MOSS inpainting workflow](https://civitai.com/articles/39134)，北京11月19日02:38发布、02:57更新；Moss V1.1／3478634同日02:38发布，旧MOSSimage v1／3416665是10月20日资料。此次按新教程和新版本收录，不将整个多年前建仓资源称新工作流。
- 作者流程：Load Image后清空旧蒙版再重画；Cut gen裁出蒙版附近区域，Full gen送全图。Pixel size控制生成latent的正方形尺寸；Expand mask扩大修改区域；Padding增加周围上下文；Blur软化边缘；Color match另管颜色衔接。
- 作者特别说明Mask opacity与采样denoise不同。希望细微变化又保留构图时，作者倾向降低mask opacity并用denoise1；普通重绘依修改量调denoise。教程的猫加礼帽／微笑例另用0.75 denoise，不能把两种建议混成单一固定配方。
- 新增区域框可分别放局部提示，也可完全不用框而只写正向；切换图片或模式后需刷新背景参照，避免按旧图摆框。版本说明另加Spectrum加速，但原文没有提供其独立效果对照，不把“加速”作为本库测试结果。
- 读取状态：教程正文全文、资源描述、两个MOSS版本元数据；没有读取节点图JSON、完整依赖版本或示范图，不能确认最终编码分支和每个补丁默认是否启用。保留原文作为完整操作入口，未安装／运行。

<a id="n06"></a>

### Krea2 SVD Merger：固定组合与秩截断分开看

**适用方向：LoRA组合·资源整理｜查阅CPU合并、固定系数与降秩误差说明。**

**设计思路：固定组合·保留取舍｜将已选搭配固化为一份权重，压缩误差另行评价。**

- 原作者与原文：dbodik242238于北京11月18日19:21在Civitai分享[Krea2 SVD LoRA Merger](https://civitai.com/articles/39126)；GitHub dbodik-git项目当前commit为`5e751e63c0f17d3f7772c7578ae828cf4550651b`，提交时间11月9日17:59。新的是教程发现／发布，不称11月18日新发布算法。
- 作者方法：各LoRA先按系数及alpha/rank还原权重增量，加和后通过QR和小核心SVD压成统一目标秩，CPU执行，支持GUI／CLI。固定人物、风格、细节组合后可存单个文件；这属于合并／压缩，不是新的训练过程。
- 条件：仅2D线性层，支持kohya down/up及PEFT A/B命名。Conv、LoKr、LoHa不支持；层名和维度必须匹配。缺alpha时按rank处理，作者提醒若真实alpha另藏训练元数据则比例可能不符。
- 误差边界：报告的是逐层被截断奇异值的相对Frobenius误差，未包含最终保存dtype量化误差，也不是图像相似度／美学分。多个推理时LoRA补丁未必只涉及同一种线性加法，不能仅凭文件可合并保证跨节点行为等价。
- Forge Neo sidecar的触发／负向词可合并去重，preferred weight平均只是起点，不能当作者原来分别使用的权重；合并系数已经写入权重。工具元数据默认标Krea2，不据格式检验推断任意家族兼容。
- 读取状态：Civitai文章全文，固定README的功能、输入约定、合并公式、误差及限制；未审源码、下载EXE或权重、合并文件或做输出比较。具体LoRA许可仍需各自遵守。

<a id="n07"></a>

### OmniLoRA：数据预缓存、训练与观察接入节点图

**适用方向：LoRA训练·工作流组织｜了解图内数据准备、分段训练与检查点的组织方式。**

- 原作者与原文：u/pente5，Reddit作者发布帖及cyberterm/ComfyUI-OmniLoRA。搜索索引列11月17日，原帖当前文本仅显示相对时间，未独立核到绝对发布时间；GitHub建仓北京17日08:15，固定commit`5c913f5b705a18af8bc62cd0bd7313294e50c4d9`提交18日20:48，本次首次收录。
- 作者分享价值：把资料夹或IMAGE/MASK训练数据、VAE／文本条件预缓存、LoRA训练、保存和loss观察放在图内。模板包括普通资料夹、分段训练后KSampler观察、蒙版样本、续训检查点及双网络／时间段分工；读者可学习流程组织，不需要本轮实际训练。
- 作者声称支持多架构、量化与CPU层流送，但发布帖明确称beta，无法遍测全部模型与GPU。可见回复说尚无多GPU支持；作者给过8GB Krea2 Q4约23秒/步的个人结果，缺完整GPU型号／尺寸／batch等，不能作可比较性能保证。
- README列bucket、caption回退和trigger自动前缀、前景加权、预缓存后卸载编码器等行为；这些是文档说明，本库未审实际实现。README推荐的人物／画风图片数与步数仅为作者起点，不推广为跨基座通用配方。
- 注意力条件：评论提醒推理用attention可能影响训练，当前README说训练时切为可微PyTorch SDPA并恢复，同时建议默认PyTorch attention作为基线。保留两处时间层级，不将新版文档说法写成早期评论已验证修复。
- 读取状态：原帖正文与可见一级回复；固定README入门、模板、预缓存／训练参数及量化说明相关段。未核测试报告、源码、JSON接线或任何硬件实跑。标题“any model／GPU”为作者目标，不当无条件兼容结论。

<a id="n08"></a>

### NL2Prompt：提示拼装与LoRA真正加载分两步

**适用方向：提示词组织·LoRA管理｜从自然语言组织提示，并区分推荐列表和实际加载。**

**设计思路：角色与风格分库｜分别维护触发词和权重，再检查最终提示及加载状态。**

- 原作者与原文：GQLI-VC，[ComfyUI-NL2Prompt](https://github.com/GQLi-VC/ComfyUI-NL2Prompt/blob/83ff353ae0967a308b82c6ebf9184b1e96915e4b/README.md)，北京11月18日23:30建仓，当前文档commit`83ff353ae0967a308b82c6ebf9184b1e96915e4b`，23:34提交。首次收录。
- 作者方法：中英自然语言拆解主体、动作、场景与镜头，结合角色／服装／风格库的触发词和建议权重拼装提示；可输出正负字符串或CONDITIONING。LLM改写可选，规则组装可以独立使用；“无需两个CLIPTextEncode节点”不等于无需匹配的CLIP／文本编码器。
- 重要职责：主节点产出`lora_stack`清单，真正作用到MODEL和CLIP由单独LoRA Stack Loader承担。文档称缺失／失败的LoRA会记录并跳过，所以整个生成完成也不证明所选LoRA都已生效。
- 约束：文档提供GGUF、本地transformers与兼容API路径，但显存数字仅为作者建议；复杂描述可能丢信息、嵌套权重检查有限。现成示例的接线、最终编码文本、模型家族专有提示格式未本地核验，不能承诺适配所有Anima／MOSS／IL版本。
- 署名与读取：已读README功能、接线、示例文件索引、配置和已知限制相关段；未读全部源码、JSON或许可原文。项目声明AGPL-3.0＋商业双许可，使用以原条款为准；未安装节点／LLM或发起API调用。

<a id="n09"></a>

### 梧桐提示词站4.0.7：选词、资源和配方分别保存

**适用方向：提示词组织·资源管理｜集中整理标签、画师串与LoRA，再连接既有引擎。**

**设计思路：文字与资源独立｜替换提示片段时保留LoRA设置，画风资料记录原来源。**

- 原作者与原文：Juu_Suzuko，stablediffusion吧，[内置免费AI、五万标签提示词的提示词工作台](https://tieba.baidu.com/p/11208431241)，北京11月18日22:39:22发布；6楼给GitHub地址，删除显式“【删除】”占位后核对到[xialing114514/mioha-prompt-station](https://github.com/xialing114514/mioha-prompt-station)。保留两个账户署名，不认定为已核实的同一自然人。
- 作者分享：标签中英搜索、正负与权重编辑、角色配方／画师风格库、LoRA目录与触发词管理，提示文字与LoRA配置独立；可接NeoForge／ComfyUI及自己的NovelAI账户。原帖提“约五万条”是作者资料规模说明，不是质量分。
- 当前文档：Windows4.0.7、Android4.0.2、模型规则v24；commit`18c116f71dae5adfe12c0c43908f85e2221e8c7b`于18日22:09提交，新增图解／文字教程。公开的是安装包、APK、模型规则与说明，**程序源码暂未公开**，因此本条不称开源程序。
- 参考价值：常用画师串、触发词和权重保留原来源快照，已提交生成使用提交时参数，编辑下一条不改上一条。已有生成元数据可回填；没有元数据时视觉反推只是估计，不能作为原图真实配置。
- 使用条件：桌面Windows/WebView2为主，内置在线AI通道限额由服务方决定，免费选词不等于无限免费生图；运行模型及引擎需要另外已有资源。本轮未下载安装包、连接引擎、登录或读取个人账户。
- 读取状态：aiotieba首楼及6、7楼共3条可见内容，未读楼中楼或图片；固定README全文，未读PDF／全部手册、发行附件或程序实现。原帖通用“全兼容”说法不升级为本库兼容保证。

<a id="n10"></a>

### H3多图编辑：参考图分工与保留程度

**适用方向：多图编辑·提示组织｜分别指定人物、衣装、场景与动作的参考职责。**

**设计思路：逐图分工·保留程度｜明确每图贡献和允许改动，再说明最终场景关系。**

- 原作者与原文：MiniMaxH3image，[INT8版多图编辑4案例](https://www.bilibili.com/video/BV13BsS6oEgV/?p=1)，北京11月18日18:45:12发布；首P151秒，整条共5P／2562秒，本次只深读首P。Reddit u/Subushie的[H3 Image edit…tips](https://www.reddit.com/r/comfyui/comments/1xz07b3/h3_image_edit_model_is_wild_tips_on_usage_based/)另作独立文字经验，索引日期11月17日、原页仅相对时间，绝对发布时间未独立核定。
- 视频作者讲解：人物图、项链／包、场景／泳圈、持物姿势、衣服与沙发等分图输入；红色区最多8个参考位，另有画幅与提示优化开关。四个案例展示如何指派属性，不能据8个输入位证明任意8图关系都稳定。
- 本库实际看图：15张10秒间隔抽帧和末秒共16帧均在联系表观察，见配饰、模特持产品与粉裙／沙发／环境组合。末例是坐卧在浅色沙发上的人物；这是一组任务示范，不概括为模型稳定的人体／脸型画风。低分辨率画面不足以独立确认所有产品小字完全保留。
- 原作者说INT8权重体积约20多G、BF16约60多G；不是峰值运行显存测量。作者报告约16MP时颜色容易改变，调至约10MP并后接SeedVR2放大；145秒硬字幕可核“约10MP生成→SeedVR2放大”，不是所有量化模型的通用上限。未取得INT8精确文件／revision、完整工作流、提示扩写后文本、seed及采样值。
- Reddit文字方法：先为每个主体／图像定义保留身份、服装、环境／光线等职责与强弱，再写一句场景摘要及细节描述。OP采用JSON组织，但可见回复明确JSON并非必需；其作用更适合概括为关系清晰的写法。OP的lcm、bong_tangent、8步／18MP只是个人设置，硬件、模型与节点版本未知，不拼入B站实际配方。
- 社区反馈分开：有人讨论3×3分镜与提示扩写，也有人对质量／参考能力持保留意见，没有控制变量对照；“JSON更好”“快速高分辨率”均未被本库验证。
- 读取状态：SDK17.4.2完整简介／分P，首P公开480短边媒体；16帧OCR与实际画面。平台字幕需登录、未取得；复用faster-whisper1.2.1 small CPU INT8读取约150.8秒音轨并生成时间轴草稿，术语如INT8／ComfyUI／SeedVR2有误识，关键操作结合简介与硬字幕核对。视频流主址200，音轨主址567后同一SDK一个备用200，未循环重试；原始媒体／全转录未入库。Reddit读正文及可见一级回复，没读折叠楼层或作品原图。两份独立分享合并主题导读，不当同图复现证据。

<a id="n11"></a>

### MOSS加速双采：低分辨率起图后放大续采

**适用方向：采样精修·效率取舍｜参考低分辨率起图与放大续采的社区设置。**

- 原作者与原文：鲜虾云吞面豪赤，stablediffusion吧，[moss加速版双采](https://tieba.baidu.com/p/11208322549)，北京11月18日21:36:25，读首楼及一条询问采样器的回复。
- 作者实践：8步加速LoRA，一采约0.3MP／8步，再双线性放大、降噪0.8续采；给出1K／2K对应放大系数2.6／3.6，并列50步、12步、8+6步、8+16步的计时记录。其参考意义是先在较低尺寸确定内容，再分配后段采样预算。
- 条件与缺口：首楼最后统一写“六步”，但前面2K计时行写8+16，不能擅自改成一套无矛盾配置。MOSS精确底模、加速LoRA文件／版本、硬件、seed、各分支CFG与采样器／调度均未取得；回复正在问这些字段，尚未看到回答。
- 本库概述：作者称约1K的8+6步比50步更快且质量相近；本轮仅文字读取，没有看其对照图或核计时条件，不沿用其“更好”作为本库评价，也不推出跨硬件速度结论。未要求作者补完整配方才收录，保留经验及可查原帖。

## 来源覆盖与检索记录

本轮主要检查时间为北京时间11月19日04:01–04:09；下列是实际页面范围，不声称穷尽所有帖子。

| 平台／吧名 | 实际入口／查询 | 读取范围与结果 | 限制及处理 |
|---|---|---|---|
| stablediffusion吧 | aiotieba4.8.2，CREATE第一页30条；全站最新“工作流 提示词”第一页30条 | 排除置顶旧帖后最新至19日02:59，普通帖子向前至17日12:09，跨过昨日水位；深读提示词站3条、双采2条、训练求助1条 | 训练求助仅提280图／3000步，无可学到的明确回应，列关注而不补造答案；图片／楼中楼没读 |
| stable diffusion名称核对 | 同工具用带空格名称第一页2条 | 实际返回stable吧的2018公告，并非stablediffusion教程入口 | 分开记录实际吧名，不称已证实入口互相重定向；有效SD覆盖采用stablediffusion吧 |
| comfyui吧 | CREATE第一页30条 | 最新普通帖18日17:23，向前至13日10:44，跨昨日水位；本窗口多OOM、入门和整合包索引 | 已检查列表，本轮未选出新增生图教程；没有称平台无更新，未深读这些候选正文 |
| bilibili广泛发现 | SDK17.4.2，pubdate：ComfyUI教程页1–6（每页20）；生图模型、Anima生图、LoRA画风各页1／20 | ComfyUI查询页5跨至17日19:19，页6至17日17:28；其余页范围分别18日08:39–23:25、10月28日–11月18日、9月13日–11月13日。BV去重，读2个候选完整简介与分P，精选H3首P媒体深读 | LoRA画风关键词本页无昨日以后新结果，不代表全站无新增；大量整合包／视频宣传不作生图教程质量凭据；Tiny Anima简介仅研究演示，未取公开配方，不另列推荐 |
| Sena404作者跟踪 | uploader UID341674866，页1／30，接口总数85 | 页范围10月14日–11月17日；最新BV1v5sz6YEDV，第29期，已在18日日报／系列索引收录 | 本次UID成功，水位仍投稿29／片内39；不重读旧媒体、不增加新增计数；只检查最新一页，不声称核完85条 |
| bilibili具体读取 | BV13BsS6oEgV info／subtitle／deep，首P151秒；另BV1nZsm6KEYR info | H3完整简介、5P元数据、首P16帧与OCR、约150.8秒ASR草稿；媒体主／备用范围见n10 | 平台字幕login_required。其余4P未读取；无评论读取。视频、音轨、截图、全转录／签名地址未提交 |
| Reddit | r/StableDiffusion/new.json50与r/comfyui/new.json30；两组站内域搜索模型／LoRA／workflow／prompt／guide及11月18日 | 列表403；搜索后打开OmniLoRA和H3编辑具体原帖，正文及可见一级回复可读 | 搜索索引与原页相对时间分记，折叠回复未展开；未以API失败推断原帖不可读，未以搜索当近期列表完整覆盖 |
| Hugging Face | text-to-image最新80、image-to-image最新30；另Anima／MOSS各20、Illustrious10按修改时间 | 打开RMS两卡、像素小模型等候选；列出revision／时间并去重。覆盖编辑、贴图、场景、像素与多家族训练路线 | IrisVenus仅少量触发说明、Lotus仅短测试卡、Illustrious候选需订阅，未凑数推荐；Tiny Anima仓无README（404），不拼B站标题为同一权重。MOSS armV5是LoRA合并描述，未冒称新训 |
| GitHub | comfyui workflow pushed>=2026-11-18最新25；comfyui prompt created>=2026-11-17最新15；跟进原文仓库 | 阅读OmniLoRA、NL2Prompt、梧桐、Krea2 Merger对应固定README相关范围；Flanorama README亦读但本轮未精选 | 文档声明与源码核验分开；未安装／运行仓库程序。Flanorama等作为已查候选，不作新增强行占位 |
| Civitai社区／论坛 | Newest模型40、文章30、Workflows15；打开两篇教程、城市／贴图模型与PotatCat版本 | 文章、模型及版本描述可读，保留作者、时间、版本ID与直达入口；城市新ZIT与Krea参数分开 | 额外Checkpoint分类查询403；城市Krea与贴图MOSS各2张原图均403，按作者文字概括，未称看过例图。评论区／作品级配方未取得 |
| Comfy社区论坛 | latest.json列表；公告topic4909正文JSON | 列表可读，最新帖17日；读取下线公告，署名MrSwazzy／Joshua Jones | 标题仍写Nov18，正文写Nov20下线，以实际读到的差异记录；不据标题认定已下线。未访问Discord，不声称覆盖其讨论 |
| note.com补充 | ComfyUI近期搜索15条 | 请求403，无正文取得 | 访问受限，不能写无优质新增 |

## 后续关注与更正

- **Sena404**：继续接续[系列索引](../2026-11-09/notes/Sena404画师串与相关分享.md)，本次最新仍投稿29／片内39，不补称有第30期。
- **后训练路线**：本日实际读了Klein编辑LoRA、MOSS／Krea贴图LoRA、城市风格LoRA与自定义像素模型。训练、合并、量化和文档更新分别说明；没有把量化文件或已报道资源的更新时间统称新训练。
- **视频与配置缺口**：H3首P未取得精确INT8权重／工作流与最终扩写提示；以后有明确需要再补，不自动下载后续长P。MOSS双采帖子里8+16与末尾六步尚未澄清，保留原意和缺口。
- **版本与许可**：Big Cities新ZIT缺独立设置；Sint Albedo接缝结果为作者小样本。RMS权重有基座非商业条件；梧桐程序源码未公开。后续更正写明日期和原文依据，不覆盖成已验证。
- **论坛入口**：[原公告](https://forum.comfy.org/t/4909)正文说明11月20日下线，并引导Discord与对应GitHub issues。未来访问变化另记；本轮只保留摘要和原帖链接，没有批量搬运论坛。
- 本轮未设生图或实验待办。读取限制集中在各条状态和来源覆盖，设计文章的摘要仍概括作者方法。
