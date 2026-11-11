# 2026-11-12 每日社区发现

感谢社区作者公开分享模型、工具、教程与实践经验。本页为本库中文概述和学习备注，逐条保留原作者与原文入口，欢迎回原帖阅读完整资料和后续更新。第三方成果归原作者；署名与链接不等同额外转载授权。

- 北京日期与实际读取时间：2026-11-12，03:56起检索，约04:04完成本轮主要来源读取，随后整理与核对归档。
- 类型：无具体差距要求的每日广泛发现；没有另立主动专题。
- 状态：归档10项主题，包含新资源、同作者新路线和实质版本说明；部分平台入口受限，按实际范围记录，不推断全网无新增。
- 时间窗：优先自11月11日03:59–04:12各平台成功检索快照之后的新增／实质变化，至本轮各入口读取时。版本发布时间、仓库创建、提交和本次阅读时间分开，历史入口只作回链。
- 本轮仅研究与汇总。复用既有B站SDK、FFmpeg和OCR读取一条54秒视频；未安装生图节点、下载大权重、调用生图／LLM API、启动服务或新增实验。资料读取、作者声明、实际看图与收益验证分别记录。

## 今日值得阅读

- [MOSS BAStyle](https://huggingface.co/nekoshrimp/MOSS-Image-BAStyle-v1)：风格LoRA训练、人物五官局限及无人背景提示有具体说明；[HaDeS v0.9.4](https://huggingface.co/DeVilDoNia/HaDeS-MOSS-v0.9.4-Turbo)则介绍Base合并权重和八步取舍。
- [Sena404第26期](https://www.bilibili.com/video/BV1hgWm65EEC/)：本轮补读circle anco标签、卡片和可见人物示范，保留投稿／内部编号差异。
- [BBox Studio](https://civitai.com/articles/38561)、[无缝贴图方法](https://civitai.com/models/3043425?modelVersionId=3459547)和[裁切再重绘](https://civitai.com/articles/38566)：分别参考布局表达、边缘修补和景别调整。

## 分享速查

| 类别 | 分享／资源与版本 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点／可学习经验 | 读取状态 |
|---|---|---|---|---|---|---|
| 风格LoRA／后训练 | [N01 MOSS BAStyle v1.0：清透赛璐璐与人物／背景分开提示](#n01) | 人物插画·背景设计｜在MOSS-Base上组织清透赛璐璐人物和学院空景。 | 美术风格方向：清透赛璐璐·柔光层次｜已看两例以大眼简鼻口、细肩轮廓和明净色面为主。 | [nekoshrimp](https://huggingface.co/nekoshrimp/MOSS-Image-BAStyle-v1) | 58张插画的风格适配；光环和无人背景另写条件，作者也说明五官还原的局限。 | 固定模型卡主要章节、完整示例提示段、工作流JSON及样张1／5；未核权重或运行。 |
| 合并checkpoint／少步适配 | [N02 HaDeS MOSS v0.9.4：Base合并checkpoint与八步取舍](#n02) | 模型选型·采样精修｜了解Base合并八步模型与SFT加LoRA路线的差异。 | — | [HaDeS／DeVilDoNia；OpenMOSS及上游适配作者](https://huggingface.co/DeVilDoNia/HaDeS-MOSS-v0.9.4-Turbo) | 新单文件包含三项适配，不能继续额外套同一Turbo；作者公开相反偏好与小样本限制。 | 固定模型卡简介、构建、设置、评估和限制；未读评测日志、看例图或核权重。 |
| 固定作者／画师标签增量 | [N03 Sena404第26期：circle anco的赛璐璐人物示范](#n03) | 画师标签·人物插画｜参考circle anco标签及人物立绘的表现取舍。 | 美术风格方向：利落赛璐璐·柔和过渡｜按作者说明，匀称人物配简净线条，平涂保留明暗层次。 | [Sena404；circle anco与原画师](https://www.bilibili.com/video/BV1hgWm65EEC/) | 字面标签为@circle anco；投稿第26期、封面内部第36期分别保留，不补造中间期数。 | 完整简介、54秒P1，10张常规／末帧与8张定点帧，人工核标签和卡片；未读评论或完整逐图配置。 |
| 构图／提示编辑工具 | [N04 BBox Studio：可视化编辑MOSS布局提示与坐标](#n04) | 构图控制·多主体关系｜以框选方式组织MOSS对象、人物和文字布局。 | 设计思路：布局先行·对象分工｜先安排对象位置与说明，再导出结构化提示。 | [plk／pflky](https://civitai.com/articles/38561) | 坐标为画布中心原点、向下Y轴、yxyx；编辑项目与模型提示导出分别保存。 | 发布短文及固定GitHub README全文；未读实现、查看输出示例或运行。 |
| 无缝贴图／全景工作流 | [N05 Krea2 Seamless Tile：把接缝移到中间再局部重绘](#n05) | 材质贴图·全景接缝｜用半幅换位与遮罩重绘修补Krea2边缘。 | 设计思路：接缝内移·局部修补｜将旧边缘移到画面中间，只重绘柔化带后换回。 | [Azimondious](https://civitai.com/models/3043425?modelVersionId=3459547) | 贴图修两轴，全景只修左右；接缝分数与球面几何、重复主体分别判断。 | 完整资源说明、版本元数据与作者测量范围；未读压缩包JSON、看输出或运行。 |
| 场景设计／天空盒工具 | [N06 Firmament：全景生成、接缝修补与天空盒导出](#n06) | 场景背景·天空盒｜参考Krea2全景LoRA到立方体贴图的处理流程。 | 设计思路：球面构图·环绕预览｜结合全景条件、边缘修补与环绕视角检查场景。 | [CursedPrograms／Cursed Entertainment](https://github.com/CursedPrograms/Firmament) | 2:1全景、wrap修补和cube导出分工清楚；模型／VAE兼容性仍需按实际文件核对。 | 固定README全文及文生图API JSON节点／参数；未读所有处理实现、看输出或运行服务。 |
| 提示库／LoRA配方工具 | [N07 FRAME 0.2.4：LoRA触发词、提示库与手填补充](#n07) | 提示词组织·LoRA管理｜分开保存触发词、库条目、手填补充与图片种子。 | 设计思路：提示来源分工·配方固定｜按明确顺序组合提示，并把换提示与换seed分开。 | [Coffmeteor](https://civitai.com/models/3046838?modelVersionId=3463972) | 0.2.4将手填补充改为显式开关；旧配方仍保留旧行为，需另存同步。 | 完整资源说明、0.2.4版本说明及固定GitHub README；未核Registry实况、读实现、看图或运行。 |
| 反推／标签工作流 | [N08 Anima反推简化工作流：识别、分类与提示格式分开](#n08) | 图像反推·提示词组织｜从图像识别标签并整理为Anima使用格式。 | 设计思路：识别与编排分工｜先取得图像描述和标签，再按用途分类与整理。 | [Zovetry／Zove-try](https://civitai.com/models/3046587?modelVersionId=3463640) | 本次分享Gelbooru与Danbooru两版，区别是标签浏览来源，不是两套后训练模型。 | 完整资源说明、v1.0元数据与外链定位；未读飞书完整教程、附件JSON或运行。 |
| 构图／图生图经验 | [N09 Zooming In：裁切、缩放后重绘的景别调整](#n09) | 构图调整·图像精修｜裁切已有画面，再以受控重绘取得更近景别。 | 设计思路：取景优先·变化取舍｜先选择想强调的区域，再控制重绘引入的新细节。 | [kotojima_junichi](https://civitai.com/articles/38566) | 作者同时举出新增头发、灯罩纹样变化；精修与保留原细节有取舍。 | 文章正文全文及发布日期／更新元数据；未看示范作品、读作者工作流或运行。 |
| Reddit发现／参考工作流 | [N10 H3 Image＋Pose Studio v1.1：参考与姿态入口合在一图](#n10) | 角色参考·姿态控制｜查阅新H3-Image的参考输入和Pose Studio入口。 | 设计思路：参考与姿态分工｜把角色参考、姿态和目标场景分别组织到流程。 | [foxydits／foxdit（Foxfuressence）](https://civitai.com/models/3045966?modelVersionId=3462838) | 资源明确针对新Image模型；本图最多9路参考是流程条件，不改写成官方模型上限。 | Reddit作者导读评论、Civitai完整说明与v1.1元数据；未读附件JSON、全部评论或看生成结果。 |

## 当日分享

<a id="n01"></a>

### N01 MOSS BAStyle v1.0：清透赛璐璐与人物／背景分开提示

**适用方向：人物插画·背景设计｜在MOSS-Base上组织清透赛璐璐人物和学院空景。**

**美术风格方向：清透赛璐璐·柔光层次｜已看两例以大眼简鼻口、细肩轮廓和明净色面为主。**

- 原作者与原文：[MOSS-Image-BAStyle-v1](https://huggingface.co/nekoshrimp/MOSS-Image-BAStyle-v1)，nekoshrimp；[固定模型卡](https://huggingface.co/nekoshrimp/MOSS-Image-BAStyle-v1/blob/50c30f98f6de924e0cb796c7a252a2427113112f/README.md)。仓库北京时间11月12日03:49创建，03:52更新，首次收录。
- 作者定位为非官方《蔚蓝档案》清透赛璐璐风格研究：MOSS-Image-Base 5B，冻结Qwen3.5-9B，仅训练DiT；58张图、rank32／alpha16、500步。风格权重与角色设定分工，不是官方素材或角色LoRA；使用按CC BY-NC 4.0及原作者说明，限非商业学习和同人创作。
- 提示方法：以`bastyle,`开头接完整自然语言；需要光环时另写颜色和形状，不需要时省略。无人建筑／天空开头用`2D anime background illustration`，避免只写摄影shot带出写实先验；多人场景按左右顺序分别交代人物。作者说明这些用法，不作为所有MOSS LoRA的通用格式。
- **美术观察归属**：本库实际看样张1图书馆半身、样张5三人街景。两例可见收窄下颌、偏大眼睛与简化鼻口、细肩颈轮廓，表情偏含蓄；衣褶以清楚色面和少量柔和明暗塑形。三人例各人的发型、眼镜和光环属于角色设定，不能当固定画风特征；所见非完整全身，不概括完整头身比例或原作整体还原率。
- 作者坦言近脸样本少，单独生成原创角色时仍可能带底模较旧式的脸眼比例；建议明确五官或配自己的角色LoRA。这是作者说明，未由两例扩展成普遍评价。
- [固定JSON](https://huggingface.co/nekoshrimp/MOSS-Image-BAStyle-v1/blob/50c30f98f6de924e0cb796c7a252a2427113112f/MOSS-Image-BAStyle-v1-ComfyUI-Workflow.json)可见Base int8 ConvRot、LoRA0.95、1344×896、shift5、SLG single layer22／0–1、Euler／simple28步、CFG3、denoise1；正向从PrimitiveStringMultiline接入图书馆样例，负向空，seed20261121且生成后randomize。以上是该JSON字段，不能据同一示例提示断言已取得每张样图真实运行seed。
- 实际读取范围：模型卡定位、提示、限制、训练与许可段及示例提示；JSON节点和连接；原样张1／5实际看图。未核权重哈希、读训练实现或复跑。

<a id="n02"></a>

### N02 HaDeS MOSS v0.9.4：Base合并checkpoint与八步取舍

**适用方向：模型选型·采样精修｜了解Base合并八步模型与SFT加LoRA路线的差异。**

- 原作者与原文：[HaDeS-MOSS-v0.9.4-Turbo](https://huggingface.co/DeVilDoNia/HaDeS-MOSS-v0.9.4-Turbo)，[固定模型卡](https://huggingface.co/DeVilDoNia/HaDeS-MOSS-v0.9.4-Turbo/blob/80a6dde4aae3a2d387220f659d033d0fe90a17c0/README.md)。11月11日19:04创建，19:07更新；本资源首次收录，与[11月6日少步LoRA记录](../2026-11-06/README.md#n01)建立谱系联系。
- 这是以**MOSS-Image-Base**为起点、合入三项LoRA的BF16去噪checkpoint，不是SFT换名，也不是整条管线只需一个文件。作者保存路径为Base→Multi-LoRA→Model Saver；依次应用data_expanded0.30、color/detail0.60、未单独发布的Turbo v0.9强度1.0。其中color/detail内部合并系数与外部0.60是两层数值，不混为一个权重。
- 作者参考配置为1152×1536、8步、CFG1、Euler／simple、shift5、denoise1、SLG关，配MOSS专用Qwen3.5-9B int8 ConvRot与flux2 VAE，ComfyUI0.43.0；Suite中Prompt Enhancer设as written，采样器额外Turbo输入留空，避免重复加载已合入适配。作者文件头里的steps4不能覆盖本checkpoint按8步评估的事实。
- 评估保持每对提示、seed和尺寸等相同，但模型与LoRA应用路线成组变化，不能单独归因某一LoRA。八对图中作者与两个模型评审多数偏好本版，另一个审阅者仅0／8或1／8偏好；部分比较复用熟悉图，非完全盲评。原卡将其定位为SFT之外的选择，不宣称通用胜出。
- 作者记录提高CFG会增饱和／近裁切并增耗时，不能当质量提升指标；BF16对照也不证明另存的int8视觉等价。权重SHA256在原卡给出，本库未下载计算，不把文件头或作者检查写成本库验证。
- 实际读取范围：固定模型卡各主要章节；未看六张预览或评测原图、读RESULTS日志和合并实现、核权重或运行。代码／权重条款分别回原文查看。

<a id="n03"></a>

### N03 Sena404第26期：circle anco的赛璐璐人物示范

**适用方向：画师标签·人物插画｜参考circle anco标签及人物立绘的表现取舍。**

**美术风格方向：利落赛璐璐·柔和过渡｜按作者说明，匀称人物配简净线条，平涂保留明暗层次。**

- 原作者与原文：[anima画师串第二十六期](https://www.bilibili.com/video/BV1hgWm65EEC/)，Sena404／UID341674866，11月11日18:31:17发布，P1为54秒；完整简介为“-”。在[第25期水位](../2026-11-10/README.md#n08)之后增量收录，[系列历史索引](../2026-11-09/notes/Sena404画师串与相关分享.md)保留原有读取范围。
- 封面字面标签是 **`@circle anco`**，显示Circle Anco／サークルアンコ，后续卡片介绍主笔トリ（Tori）。这是作者介绍的社团／画师资源，不把一个社团名自动等同单个画师的全部作品。投稿标题第26期，封面写第36期、2026.11.11和20图实测；两种编号并记，不能据内部编号补称27–36期已收录。
- 作者卡片说明：干净闭合线条的赛璐璐路线，平涂加柔和明暗，约6–7头身、体型匀称、少夸张变形，擅长突出人物的立绘构图；复杂手部、极端角度及放大细节仍可能松散。图库张数、20张无脸部融合／错位等均是作者本组说明，本库未独立核查其20张原图或图库统计。
- 本库实际看图：视频可见示范以收窄下颌、大眼、小鼻口和含蓄微笑／侧视为主；躯干、腰线和衣褶体积用明确明暗块塑形，局部加柔光过渡。姿态包括回头、侧身、伸手；猫耳、礼帽和制服等是各图设定，不归为画风必备元素。全体头身判断主要来自作者卡片，不由单张裁切图重算总体比例。
- 已用公开媒体抽样10帧（含末秒），另对2、28、31、33–37秒补8帧，含过渡黑帧；2秒封面和34–37秒第7卡人工核字。读到的10页卡片没有完整模型版本、正负提示、采样／seed和每图LoRA配方，**不沿用上一期10步设置补成本期实值**。无需ASR；平台字幕、评论未读。
- 作者投稿列表本轮返回NetworkException，但“Anima”最新搜索命中这条具体投稿，详情与媒体可读。因此将已收录水位推进到第26期，仍不声称作者全部最新投稿已覆盖。媒体、截图、OCR原件不提交仓库。

<a id="n04"></a>

### N04 BBox Studio：可视化编辑MOSS布局提示与坐标

**适用方向：构图控制·多主体关系｜以框选方式组织MOSS对象、人物和文字布局。**

**设计思路：布局先行·对象分工｜先安排对象位置与说明，再导出结构化提示。**

- 原作者与原文：[BBox Studio](https://civitai.com/articles/38561)，plk，11月11日04:30发布、07:26更新；[pflky/BBox-Studio](https://github.com/pflky/BBox-Studio)固定提交`30c5d5414391fbf7c2377bb1db8ca9db478aae2c`于21:09更新。仓库11月7日已创建，本轮按新发布文章／当前文档首次收录。
- 作者提供独立Python／Tkinter布局提示编辑器：框选、移动／缩放、复制和位置锁定，为object、character、text element分别填标签与说明；支持背景图、画布尺寸、构图辅助线。用途是整理布局提示，不能把画布框选直接当像素级生成约束或已验证多主体隔离。
- 导出坐标约定明确为`bbox_coord_space=abs_centralized`、`bbox_format=yxyx`，原点在画布中心、Y向下，顺序`[y_min,x_min,y_max,x_max]`。导入支持其他约定不等于输出自动采用另一套；应按目标MOSS编码路径核对，不能与左上角起点的xyxy混用。
- `.bbox`保存编辑状态、颜色、锁定、缩放等；`.json`是供兼容MOSS流程使用的布局提示。仅拿JSON不能假设完整恢复编辑项目，导出成功也不证明生成结果遵循全部框选。
- 作者“零依赖”指无额外Python包，仍需Python与Tkinter支持。仓库末尾写All rights reserved，本库仅摘要与链接，不替作者补开源许可证或复制程序；代码有Grok辅助说明，运行／效果声明保持原作者归属。
- 实际读取范围：文章短文、固定README全文与提交／创建日期；未读实现、看UI生成示例、验证编码接法或运行。

<a id="n05"></a>

### N05 Krea2 Seamless Tile：把接缝移到中间再局部重绘

**适用方向：材质贴图·全景接缝｜用半幅换位与遮罩重绘修补Krea2边缘。**

**设计思路：接缝内移·局部修补｜将旧边缘移到画面中间，只重绘柔化带后换回。**

- 原作者与原文：[Krea 2 Seamless Tile: Make Any Render Repeat](https://civitai.com/models/3043425?modelVersionId=3459547)，Azimondious，v1.0／3459547，11月11日23:00发布；首次收录，和[前日PBR多通道](../2026-11-11/README.md#n07)属于不同用途。
- 两个图分别处理材质两轴和2:1全景左右换位：把旧边缘移入中心，用原提示重绘柔带再换回，作者称带外保留原像素。图像宽高须偶数，输入半宽／半高；全景只需半宽。原提示描述应与待修图一致，避免重绘带引入不相关物体。
- 作者测试RedCraft3.0 Krea2 INT8 ConvRot；Qwen3-VL 4B编码器type krea2、Qwen Image VAE，8步、CFG1、er_sde／simple、分块VAE512／64，模型前置DifferentialDiffusion。贴图denoise0.7，全景0.85；256px实心带两侧各128px淡化。都是该工作流参数，不替其他模型补默认值。
- 作者用首尾行／列差除以相邻差中位数评估接缝，1.5是其此次判线；六张材质中砖缝会导致换seed成败不同，六张1440×720全景在0.85才全部低于判线。这不证明每张素材一次成功，也不衡量审美或真实球面投影。
- 方法边界：大焦点物即使无缝仍会重复；带内物体可能被改写；全景只修wrap，不能自动修正地平线和极区几何。作者UI JSON由脚本生成并按节点定义检查，非浏览器实跑保存；其ROCm环境描述不代替本库加载或CUDA验证。
- 实际读取范围：完整说明和版本元数据；未读附件JSON、看测量原图或运行。以设计方法收录，不把作者“可加载”提升为跨版本完全兼容。

<a id="n06"></a>

### N06 Firmament：全景生成、接缝修补与天空盒导出

**适用方向：场景背景·天空盒｜参考Krea2全景LoRA到立方体贴图的处理流程。**

**设计思路：球面构图·环绕预览｜结合全景条件、边缘修补与环绕视角检查场景。**

- 原作者与原文：[Firmament](https://github.com/CursedPrograms/Firmament)，CursedPrograms／Cursed Entertainment；仓库11月12日00:37创建，固定提交`c361cf08f7423f7bfb55f145776b3c0c0db36c27`的作者提交时间为00:31，早于仓库公开创建，不能混作同一时间。首次收录。
- 作者组织Krea2 Turbo＋[mickmumpitz 360 ERP LoRA](https://huggingface.co/mickmumpitz/Krea2-360-ERP-LoRAs)生成2:1全景，提供球面预览、半幅换位修缝、环绕padding放大、六面cube或cross导出。原LoRA链接本轮仅定位，未深读其训练卡；不把前端工具算作另一套后训练权重。
- 作者路线从2048×1024生成，再以4x-UltraSharp V2 Lite输出4096×2048或8192×4096；“8K”是后续放大，不是8K原生生成。左右边缘接缝分数与球面极区／地平线合理性分开判断。代码MIT与所用模型／LoRA条款也分开。
- 固定[文生图JSON](https://github.com/CursedPrograms/Firmament/blob/c361cf08f7423f7bfb55f145776b3c0c0db36c27/workflows/krea2_360_t2i_api.json)可见GGUF Q4_0、360LoRA1.0、2048×1024、Euler SDE类`er_sde`／simple10步、CFG1、denoise1，提示前缀`img-txt-2-360`。这是模板字段，不是全部成图实值；运行时可怎样改写尚未读实现。
- **配置条件**：README与模板均字面引用`wan_2.1_vae.safetensors`，与上一条RedCraft方法的`qwen_image_vae.safetensors`不同。本库未核实际VAE权重结构／来源和加载路径，不能凭文件名认定兼容、等价或替读者换一个文件后称原样复现。作者RTX2060耗时也是其设备记录。
- 实际读取范围：固定README全文、workflows目录与文生图JSON；未看项目示范、核模型／VAE、读修缝／导出实现或启动应用。本轮仅整理流程，未新增本地服务。

<a id="n07"></a>

### N07 FRAME 0.2.4：LoRA触发词、提示库与手填补充

**适用方向：提示词组织·LoRA管理｜分开保存触发词、库条目、手填补充与图片种子。**

**设计思路：提示来源分工·配方固定｜按明确顺序组合提示，并把换提示与换seed分开。**

- 原作者与原文：[FRAME Krea2 for ComfyLink](https://civitai.com/models/3046838?modelVersionId=3463972)，Coffmeteor，0.2.4／3463972于11月11日21:03发布；[GitHub](https://github.com/Coffmeteor/ComfyUI-FRAME)固定提交`70c08ce41fc5992a55d9b156a27b005a9ac3f78f`于23:21更新。首次收录，并明确本版行为变化。
- 桌面设模型、LoRA分组／model与CLIP强度、应用阶段和手机开关名，再生成ComfyLink流程；自动trigger只读明确sidecar元数据或`modelspec.trigger_phrase`，无元数据时按原作者资料手填或none，不从文件名／训练标签猜trigger。完整配方面向Krea2、ComfyUI≥0.43。
- 提示顺序为启用LoRA触发词→选中的完整库条目→手填补充。0.2.4里在线／本地库默认忽略手填，须开Append manual text；manual-only仍用手填。老配方保留原追加行为，重存并同步才采用新行为。关LoRA只移除自动注入，不删除用户自己文本。
- “Reuse current”与“Random each generation”决定提示条目；固定图片seed是另一件事。共享后端／同配方可能共享当前提示选择，跨重启保存也不等于每位用户独立状态。生成快照引用本地不可变recipe，不是可独立搬家的完整模型／配置包，应分享portable starter让接收者配置自己的资源。
- 作者给示范实值：Moody Krea Mix Premium、无启用LoRA、8步、CFG1、Euler a／beta、1184×1760，无重绘／脸修／SeedVR2。桌面截图里的风格适配仅为可配置例子，不倒推已用于示范；63位大seed需看Seed exact或PNG参数，网站数值可能舍入。本轮未读图片元数据。
- 实际读取范围：完整Civitai说明、0.2.4改动与固定README；Registry收录／网络行为等保持作者说明归属，未独立审计。未读实现、看例图、安装或运行。

<a id="n08"></a>

### N08 Anima反推简化工作流：识别、分类与提示格式分开

**适用方向：图像反推·提示词组织｜从图像识别标签并整理为Anima使用格式。**

**设计思路：识别与编排分工｜先取得图像描述和标签，再按用途分类与整理。**

- 原作者与原文：[Anima Reverse Prompt Simplified Workflow](https://civitai.com/models/3046587?modelVersionId=3463640)，Zovetry／Zove-try，v1.0／3463640于11月11日18:00发布。作者既有[10月4日B站反推教程](../2026-10-30/notes/history/bilibili.md#bv1s1hl6ve8q)已收录，本次记录新资源发布页与当前依赖说明，不将同源旧视频当新投稿。
- 作者将输入图像→反推／标签识别→自动分类→Anima格式输出串起来。列出[Danbooru-Anima-Prompt](https://github.com/Zove-try/ComfyUI-Danbooru-Anima-Prompt)、[TaggerPlus](https://github.com/Zove-try/ComfyUI-TaggerPlus)、本地llama-TE等8项节点依赖，涉及Anima Base v1.0、Turbo v0.1、Qwen视觉反推GGUF及投影文件、PixAI Tagger等资源。节点库和模型在此是作者用法清单，不表示本轮已逐一深读或安装。
- “6G显存可跑”是作者标题／路线说明，模型分阶段占用、设备内存与有效卸载图未核，不能由标题保证任意6GB机器都可同时装载。反推得到的标签也不能证明原图私有底模、LoRA组合或原始提示就是这些文本。
- v1.0附Gelbooru和Danbooru两个图，作者称只有浏览节点不同。原文提示Danbooru当时不可用并建议另一版；本轮没有独立访问站点或核事件原因，只记录来源切换条件，不转述未核的事故细节。
- [作者详细教程](https://icn01wg02kz3.feishu.cn/wiki/GrCtwn5tSignWokefrycOxe8nNf)本轮仅定位；没有取得附件JSON的有效分支、最终编码文本或同图完整配方。Anima非商业条款等请按各资源原文查看，不把工作流整理当新许可。
- 实际读取范围：完整发布说明、版本元数据、插件／模型／教程直达链接；B站“Anima 反推”近期搜索仅返回既有旧教程，本轮无新视频深读。未取得附件JSON、读全部外链正文、运行反推或生成。

<a id="n09"></a>

### N09 Zooming In：裁切、缩放后重绘的景别调整

**适用方向：构图调整·图像精修｜裁切已有画面，再以受控重绘取得更近景别。**

**设计思路：取景优先·变化取舍｜先选择想强调的区域，再控制重绘引入的新细节。**

- 原作者与原文：[Zooming In](https://civitai.com/articles/38566)，kotojima_junichi，11月11日05:52发布、19:19更新；首次收录。
- 作者分享简单流程：裁出原图想强调的部分，可换宽高比，缩放后作为img2img输入，并复用／调整原提示。用于模型不易按文字安排景别或主体位置时；图太小或几乎裁全图则意义有限。GIMP只是作者使用的工具，ComfyUI的裁切和缩放节点也可做相同准备。
- 作者提醒denoise小于1以保留输入，其个人工作流则把start_step设大于0，常接近4；二者由实际调度和总步数决定，**不把start_step=4当通用denoise数值换算**。想更贴近原图可降低重绘量，细节随重绘新增，也可能改变原图特征。
- 原文举出额外头发、反射灯罩图案改变等例子，提示“更近／更丰富”不等同原细节保真。作者修订了此前对Krea2尺寸的说法：1024–2048不再当硬性要求，32倍数也改为16即可的经验说明。本库保留这些修订，不重新固化为全模型尺寸规则。
- 保存裁切输入时关注压缩痕迹，因为它可能被带入后续生成。文中未提供完整采样／模型版本与各例图实值；不为每张图补一套通用推荐配置。
- 实际读取范围：文章正文全文与时间元数据；未打开所链接示范作品、看图或读其个人工作流。方法概括依据作者文字，本库未裁图、复跑或验证收益。

<a id="n10"></a>

### N10 H3 Image＋Pose Studio v1.1：参考与姿态入口合在一图

**适用方向：角色参考·姿态控制｜查阅新H3-Image的参考输入和Pose Studio入口。**

**设计思路：参考与姿态分工｜把角色参考、姿态和目标场景分别组织到流程。**

- 原作者与原文：[H3 Image w/ Pose Studio & Other Advanced Features](https://civitai.com/models/3045966?modelVersionId=3462838)，foxydits／Foxfuressence，v1.1／3462838于11月11日08:56发布；发现入口为[foxdit的Reddit导读](https://www.reddit.com/r/comfyui/comments/1xt7k7p/h3_image_allinone_workflow_w_pose_studio_lots_of/)。搜索显示11月11日，打开页仅相对时间，版本页绝对日期单独保留。首次收录。
- 作者说明此图用于新**H3 IMAGE**，支持文生图、图生图、参考图生成及Pose Studio开关，还含多来源比较和从视频选择单帧作图片参考的入口。本轮依原文概述用途，不因菜单存在就称所有功能已由本库验证。
- 资源页列最多9路参考；这是该工作流的入口条件，与[11月11日官方模型卡](../2026-11-11/README.md#n01)所述模型最多16图分开。页面列新Image去噪器、H3共享文本编码器、另一个Qwen编码器及Image VAE等链接，但未读JSON，不能推断每个编码器在有效分支中的角色或全部同时必需。
- Reddit作者导读可读，部分评论在搜索摘要中出现，但本轮未展开全部讨论，尤其不把用户询问的“连续20多图一致性”改写成作者确认。未取得完整提示、姿态输入、逐图采样与最终编码文本。
- 实际读取范围：Reddit作者短导读及原资源直链、Civitai完整说明与v1.1元数据；未看示范图、读JSON或复跑。与官方资源和早期H3视频静帧方案按具体权重／用途去重，不因都叫H3重复合并。

## 来源覆盖与检索记录

以下为北京时间本轮快照。列表筛选、正文阅读、配置／元数据、评论和看图分别计范围，不宣称平台全量覆盖。

| 平台／吧名 | 实际入口或查询 | 检查时间与读取范围 | 结果／限制 |
|---|---|---|---|
| stable diffusion／stablediffusion吧 | aiotieba4.8.2，CREATE最新第1页30项 | 03:57列表；置顶单列，非置顶日期从11月12日01:53回过11月11日晨间水位；读[训练讨论](https://tieba.baidu.com/p/11186755928)2楼、[少步LoRA疑问](https://tieba.baidu.com/p/11188007314)1楼 | 正文可读。训练首楼只称100多图、18轮每轮6次，缺基座／优化器／例图读取，回复关于人像可行性的泛论不作定论；少步帖只有提问，不当教程。 |
| comfyui吧 | aiotieba CREATE第1页28项 | 03:57核吧名，2024置顶与新帖分开，列表跨过上轮水位；读[分享贴子](https://tieba.baidu.com/p/11186748960)1楼 | 取得文字仅“分享贴子”，未看图／附件，不能概述未知分享内容；无足够可读细节的候选与平台失败分开。 |
| 贴吧别名与全站补充 | “stable diffusion”第1页1项；全站最新“工作流 提示词”第1页26项 | 03:57–03:58；带空格入口仍返回stable吧旧公告，规范入口采用stablediffusion；全站结果核实际吧名与原始日期 | 别名返回的无关论坛不计生图吧覆盖。全站搜索只作补充，未启用或检查Astron备用依赖，无循环切换／重试。 |
| bilibili广泛发现 | SDK17.4.2按pubdate搜“ComfyUI 教程”1–5页共100条返回项；“生图 模型”“Anima”“LoRA 画风”各第1页20项；“Anima 反推”第1页 | 03:57–04:03；ComfyUI页从11月12日00:24回到11月10日22:25，跨过上轮水位；按BV去重并排除无关音乐、重复推广等 | 原标题与摘要先筛选；具体深读Sena26。反推查询最新匹配仍是10月4日旧教程，不能据此称全站没有新反推分享。未启用备用CLI／yt-dlp。 |
| Sena404固定跟进 | UID341674866最新投稿第1页；Anima最新搜索命中BV1hgWm65EEC | 03:57投稿入口NetworkException；03:58详情，03:59媒体，随后定点补帧与看图 | 完整简介、54秒P1媒体、OCR与18张抽样／定点帧可读；无平台字幕／评论／完整逐图配方。已收录水位由第25期推进到11月11日18:31第26期；仍不声称作者最新投稿全部覆盖。 |
| Reddit | r/StableDiffusion latest new.json50、r/comfyui new.json30；日期／model／workflow／LoRA／H3 Image类别补搜 | 约03:57两个列表均403；打开[Pose Studio导读](https://www.reddit.com/r/comfyui/comments/1xt7k7p/h3_image_allinone_workflow_w_pose_studio_lots_of/)、[H3高分辨率经验](https://www.reddit.com/r/StableDiffusion/comments/1xtlj1t/minimaxh3image_at_16_mp_6_steps_20_s_per_image/)及[动漫人物＋写实背景](https://www.reddit.com/r/StableDiffusion/comments/1xrv40z/anime_characters_realistic_backgrounds_winter/)可见正文／评论段 | 具体原帖部分可读；N10追到Civitai原资源。另两帖分别读到设置／少量评论和配方评论，但原始绝对日期与打开页相对时间不一致，未取得其图片／完整配置；保留为线索，不改写本日已验证新方法。 |
| Hugging Face | text-to-image按lastModified最新80，image-to-image最新30；追新作者／模型家族候选 | 03:57入口及随后固定模型卡，BAStyle示例JSON与两张原样张 | N01、N02分别记录风格后训练与Base合并；列表含大量H3量化／转换、重复镜像和不相关项目，未把每份包装当新模型。API成功不等同全部文件／图像已读。 |
| GitHub | comfyui workflow pushed:>=2026-11-11按updated25；comfyui prompt created:>=2026-11-10按updated15；文章追作者仓库 | 03:57起读取固定README、创建／提交元数据；BBox、Firmament、FRAME深入；Firmament只读文生图JSON | 新前端、提示工具与训练权重分开；未启动应用、安装节点或把文档测试声明当本库运行结果。未深读的候选不称全文阅读。 |
| Civitai社区／教程／资源版本 | 最新模型40、文章30、Workflows15；打开本文所列文章与版本 | 约03:57入口，随后读文章38561／38566和具体版本说明；跟随Reddit定位3045966 | N04、N05、N07–N10有已读正文／版本条件。也浏览HDR VAE文章及说明，只有作者重建特性概述，未核转换脚本／图像；不据标题确认质量改善。带配方作品与版本评论本轮未逐项深读。 |
| 其他有效论坛与作者资料 | forum.comfy.org/latest.json前30；[IPAdapter报错话题](https://forum.comfy.org/t/4845)；note.com ComfyUI最新查询 | 03:57列表、约04:02读取该论坛首楼；原作者GitHub资料见上列 | 论坛首楼只是求助，无可读解决回复，不当修复教程；旧PhotoDeblur已报道，未重复收录。note查询403；不将其他平台替代为已读note。 |

本环境未配置B站会话，未取得平台字幕；Sena无必要口播内容，本轮未跑ASR。媒体、截图、完整转录、凭据和签名地址不提交GitHub。没有自动登录、提取Cookie或修改网络路由；访问受限、关键词无命中和候选信息不足分别记录。

## 后续关注与维护

- BAStyle的脸部近景后续版本、角色LoRA条件与实际样张配方；HaDeS的Base合并、SFT适配和不同量化版本保持各自证据，不把小样本偏好提升为通用优劣。
- BBox坐标约定与目标编码路径、Firmament模板VAE来源、全景极区几何，以及原作者JSON实际有效分支，尚需有资料再补；本轮不因加载器名称推断完全兼容。
- FRAME旧配方／新补充开关、反推模板的最终编码文本和各站点可用状态保留版本条件；“可编辑／能导出”与实际生成遵循分别记录。
- Sena系列已新增投稿第26期入口，保留第25期以及1–24历史基础；内部36不是投稿缺号证明。作者列表仍受限，下轮继续按UID查询，并利用可用搜索保存已经读到的具体投稿。
- 本轮全部内容未在本库执行生图、原样复跑或获得用户效果认可。方法与风格摘要是资料整理；后续实际执行沿用明确授权与停止点，不由归档触发实验。

归档记录：2026-11-12首次整理10项主题；先保存本文，再更新总索引、作者系列增量入口与首页。阅读不足或工具受限不推断全网无更新。
