# 2026-11-09 每日社区发现

感谢社区作者公开分享模型、工作流、教程与实践。本页为本库中文概述，保留作者与原文直达链接，欢迎阅读原帖完整内容、更新并支持作者。第三方成果不作为本库原创，署名和链接不等于额外转载授权。

- 北京日期：2026-11-09；本轮03:57–04:09检索与整理，随后完成保存核对。
- 检索类型：无具体差距要求的每日广泛发现。
- 执行状态：本轮归档完成：9项汇总，其中7项本库首次收录、2项旧资源发布／功能更新；部分平台及媒体内容受限，逐项列明。
- 覆盖时间窗：优先11月8日各平台快照之后新增与实质变化，近期首次补录另记真实日期；不把新镜像、同资源更名或文档更新当作新训练。
- 方向与美术／设计摘要为本库整理；作者说明、实际看图、元数据与未读范围分开。未安装节点、下载模型权重、启动生图或实验。

## 今日值得阅读

- [角色LoRA标注实验](https://civitai.com/articles/38061)：类别与身份特征如何分工，要连同测试提示及混合变量一起看。
- [SnapRef v2a stable](https://huggingface.co/0ppxnhximxr/snapref-v2a)：记录相对旧预览版的发布文件差异，区分逐图权重与全局参考强度。
- [Juggernaut Moss V1](https://huggingface.co/Kandoo/Juggernaut-Moss)：全量微调及照片提示方法，注意作者推荐与展示参数不同。
- [FLUX3 RGBA套件](https://huggingface.co/DenRakEiw/FLUX3-Image-Klein-Native-RGBA-Transparent-LoRA)：透明生成、前景提取与RGBA VAE各有职责，保存链也要保留alpha。

## 分享速查

| 类别 | 分享／资源与版本 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点／可学习经验 | 读取状态 |
|---|---|---|---|---|---|---|
| LoRA训练／标注经验 | [N01 角色LoRA标注：类别词、身份特征与触发词分别承担什么](#n01) | 角色LoRA·提示词组织｜比较类别词与身份特征如何分配到标注和提示。 | 设计思路：类别与身份分工｜明确耳尾等类别，把辨识特征留给角色，并同时检查推理提示。 | [lepetitprince716355](https://civitai.com/articles/38061) | 作者比较三种角色标注方案，强调触发词单独仍会失败、训练标注与测试提示存在混合变量，不把单角色经验写成普遍规律。 | 文章正文全文；未看对照图、读取训练配置或复跑。 |
| 参考适配器／版本更新 | [N02 SnapRef v2a stable：参考适配器发布更新与参数分层](#n02) | 人物参考·多参考图｜区分逐图贡献、全局参考强度和画风模式。 | 设计思路：身份与画风分开｜用同角色不同视图补充可见信息，再按模式选择参考画法或提示画法。 | [0ppxnhximxr／ArcAnima](https://huggingface.co/0ppxnhximxr/snapref-v2a) | 相对库中v2a-pre2，本轮确认stable发布文件不同，并记录简单／高级节点的Strength含义；不把stable标签当全面指标提升。 | 固定revision模型卡全文、SHA256SUMS及两版本LFS元数据；未看示范图、读取tensor或运行。 |
| 后训练LoRA／透明素材 | [N03 FLUX3 RGBA套件：透明生成与前景提取是两枚不同LoRA](#n03) | 透明素材·前景提取｜区分文生RGBA与参考提取，并保留四通道保存链。 | 设计思路：主体生成与透明通道并管｜分别选择生成或提取任务，让alpha经过匹配VAE与保存节点。 | [DenRakEiw；RGBA VAE原作者Xavier Jara／trmz](https://huggingface.co/DenRakEiw/FLUX3-Image-Klein-Native-RGBA-Transparent-LoRA) | 作者发布两种FLUX3 Klein专用LoRA；RGBA VAE来自trmz镜像，不把改名VAE算作本作者新训练。 | 固定revision模型卡全文；未读节点实现、工作流JSON、看透明例图或核验alpha。 |
| 后训练模型／全量微调 | [N04 Juggernaut Moss V1：全量微调、照片提示与展示参数的边界](#n04) | 写实人像·模型选型｜参考MOSS全量微调，并分清推荐与展示配置。 | 美术风格方向：高调写实·细肤质｜本例浅色眉睫与含蓄直视，柔光保留雀斑和皮肤纹理。 | [KandooAI；支持RunDiffusion；基座OpenMOSS](https://huggingface.co/Kandoo/Juggernaut-Moss) | V1为MOSS Base的transformer全量微调；量化版不是另一次训练，作者盲测比例不作为本库质量验证。 | 固定revision模型卡全文与文件目录；实际看1张人像示范，未读工作流或复跑。 |
| 画风LoRA／构图提示 | [N05 Dizzle's Art Nouveau-ish v1：装饰边框与主体留白的配合](#n05) | 装饰插画·画风LoRA｜参考Illustrious新艺术资源与边框留白写法。 | 美术风格方向：新艺术·装饰童话｜按作者描述，流线轮廓、拱圆边框与柔和复古色相结合。 | [Maridizzle](https://civitai.com/models/3042358?modelVersionId=3458228) | 作者用清楚的单主体和周围留白容纳装饰框；高强度可能使脸部细节变软。 | 完整资源说明与版本元数据；例图CDN未取得，未实际看图、读取图配方或运行。 |
| 合成工作流／色彩管理 | [N06 Nuke ComfyBridge：往返ComfyUI时保留色彩与元数据边界](#n06) | 合成流程·色彩管理｜区分显示变换、数据通道与EXR回传中的损失。 | — | [David Borrull／dborrull](https://github.com/dborrull/nuke-comfy-pipe) | 色彩plate经Viewer变换成8-bit PNG，回EXR不自动恢复高光；深度等数据通道走另一条路径。 | 固定README的简介、色彩、输入、序列与元数据章节及提交信息；未读全部实现或运行。 |
| 多参考图／自动提示节点 | [N07 P-H3 Image Tools：图片槽位、Picture编号与原图职责分开](#n07) | 多参考图·自动提示｜整理P-H3扩写输入，保留原图并映射图片编号。 | 设计思路：参考编号与输入职责分开｜整理扩写用图与原始参考，并核对最终Picture编号。 | [jalberty2018](https://github.com/jalberty2018/ComfyUI-P-H3-Image-Tools) | 最多9张按有效输入压紧编号；扩写LLM用图与P-H3原始conditioning不能混作同一路输出。 | 固定README全文和提交信息；未读示例JSON、代码实现或运行节点。 |
| 提示词教程／参考图设计 | [N08 图生3D参考图：先把视角、轮廓、背景和材质写清楚](#n08) | 3D参考图·提示词设计｜以视角、轮廓、背景和材质组织建模用输入图。 | 设计思路：参考图面向形体读取｜先让主体轮廓与体积清楚，再交给下游图生3D。 | [Reneelry](https://www.bilibili.com/video/BV1JkWH64E9n/) | 以海马参考图说明建模输入的四个要素；简介可读，视频示范与完整提示尚未取得。 | 专用工具完整简介、作者与发布时间；字幕需登录未取得，未看视频画面。 |
| 提示词工具／旧条目更新 | [N09 Wardrobe V6／6.7.0：勾选池随机与特写收紧的更新](#n09) | 提示词组织·批量变化｜用勾选池安排场景变化，并保留角色和取景约束。 | 设计思路：场景随机与取景约束联动｜从选定池生成场景，特写同步减少画外信息干扰。 | [灵冻不冻；上游ANIMA提示词生成器作者飞蓬](https://www.bilibili.com/video/BV1PVWn6tEyJ/) | V6视频说明优化UI与场景；固定源码显示6.7.0，新增勾选池自动随机，区别于库中已收录V5。 | 视频完整简介；固定README全文、changelog近期段及入口相关代码片段；未看视频、安装或出图。 |

## 当日分享

<a id="n01"></a>

### N01 角色LoRA标注：类别词、身份特征与触发词分别承担什么

**适用方向：角色LoRA·提示词组织｜比较类别词与身份特征如何分配到标注和提示。**

**设计思路：类别与身份分工｜明确耳尾等类别，把辨识特征留给角色，并同时检查推理提示。**

- 原作者与原文：[lepetitprince716355](https://civitai.com/articles/38061)。
- 原文：《Trigger-Only and Full-Description Captions Both Failed Our Character LoRA; Class Words Worked》，2026-11-09 00:01:54.578 +08:00发布；首次收录。本库中文概述，非全文翻译。
- 作者实验：在42–43张同一狐耳角色图上，比全部特征交给trigger、把外观全写进caption、只写类别词三条路线。后一方案在caption与测试提示保留fox ears／fox tail等类别，发色、尾尖色等识别细节留给trigger；trigger独用仍失败。
- 变量与边界：Anima前后还改变测试提示是否带类别词，v3删一图；大部分仅四场景、每场景一个seed，Krea2 v3未测。不能将成功只归于caption变化，更不能说每个角色都应采用同一标注规则。
- 作者给的检查思路：同seed比较trigger-only、类别词加新服装、无LoRA完整描述和无trigger几行，分别看角色保持、底模已有能力与特征泄漏。对某角色，姓名与trigger都需要；这是个案，非所有模型都要加角色全名。
- 其他实践：按实际图片标注而非生成用词，检查角落印记／伪字；改caption后用新训练目录避免旧文本缓存。作者把机制解释与观察分开；本库也未验证文字缓存行为或视觉评分。
- 与旧文关系：同作者[11月8日四基座风格训练文](../2026-11-08/README.md#n01)关注风格数据与检查点，本篇新增角色类别／身份标注的尝试，不重复计其既有LoRA权重。
- 读取范围：文章正文全文；未看对照图、读取训练配置或复跑。

<a id="n02"></a>

### N02 SnapRef v2a stable：参考适配器发布更新与参数分层

**适用方向：人物参考·多参考图｜区分逐图贡献、全局参考强度和画风模式。**

**设计思路：身份与画风分开｜用同角色不同视图补充可见信息，再按模式选择参考画法或提示画法。**

- 原作者与原文：[0ppxnhximxr／ArcAnima](https://huggingface.co/0ppxnhximxr/snapref-v2a)。
- 原文：《SnapRef v2a》，revision `2ca5eca5fd2f0e6f01af33cc7f4c6b6f2b9414cb`，2026-11-08 22:40:19 +08:00更新，仓库创建20:38:08；stable文件`snapref_v2a.safetensors`。这是[11月1日v2a-pre2](../2026-11-01/README.md#n03)的发布更新；char模式和多参考在旧记录中已有，不说本次首创。
- 文件核对：stable与pre2主文件均381,821,960字节，但HF LFS报告的整文件SHA-256分别为`8a22fc28d060447544eda283b36efe2dcdbad7422cbc0b8d42828d55a8a61ab4`与`1c9794ac626551654aa0bf08028e70a451eda4229878a7ea00490b4cc72edaa8`；stable的SHA256SUMS相符。仅确认发布文件不同，未下载／重算或比较tensor，不凭文件哈希断言新训练步数或收益。
- 作者用法：Anima base1.0配专用节点，简单节点支持同角色最多8张图；高级节点可选separate／stitch。简单逐图Strength1.0起步、0关闭；高级全局strength是对数尺度，0不是关闭。逐图权重只在separate有效，参考同人多视图与两人拼接是不同任务。
- 模式与配置：cs同时参考人物与画法，char由底模／提示词主导画法。作者示范CFG4.5、Euler/simple、Fidelity1；高级ref_in_uncond或额外ref_guidance启用时fidelity会被忽略。不能按普通LoraLoader加载，即使文件放loras目录也仍需专用节点。
- 评价范围：作者64用例×2seed的v1a对照中，appearance recall略升，但extra tags、部分头部相似度／CCIP等未同步提高；不是对pre2的独立对照。明亮脸部、细配饰／领口仍可能变化，头像不提供看不见的下半身设定。权重为CircleStone非商业许可；六份工作流与例图尚未由本库运行验证。
- 读取范围：固定revision模型卡全文、SHA256SUMS及两版本LFS元数据；未看示范图、读取tensor或运行。

<a id="n03"></a>

### N03 FLUX3 RGBA套件：透明生成与前景提取是两枚不同LoRA

**适用方向：透明素材·前景提取｜区分文生RGBA与参考提取，并保留四通道保存链。**

**设计思路：主体生成与透明通道并管｜分别选择生成或提取任务，让alpha经过匹配VAE与保存节点。**

- 原作者与原文：[DenRakEiw；RGBA VAE原作者Xavier Jara／trmz](https://huggingface.co/DenRakEiw/FLUX3-Image-Klein-Native-RGBA-Transparent-LoRA)。
- 原文：《FLUX 3 Image Klein – Native 4-Channel RGBA Transparency Suite》，revision `e0271a72fd7ada54593b9e9f4d86acaccb4f7149`，2026-11-08 21:35:54 +08:00更新，非首发证明。首次收录。
- 作者任务分工：`flux3_klein_transparent_lora.safetensors`是文本到透明RGBA；`flux3_klein_extract_lora.safetensors`借ReferenceLatent／image_cond做前景提取与抠图。两者不是同一开关，不能只凭transparent词推定任意普通模型会输出alpha。
- VAE与署名：`vae/flux2_3_rgba_vae.safetensors`是Xavier Jara／trmz的flux2-klein-alpha四通道VAE镜像改名，作者声明未改权重；本库未下载验证。模型潜通道128与解码RGBA四通道是不同维度，不把4通道VAE说成4通道latent。
- 公开条件：需DenRakEiw_Nodes的RGBA加载／编解码、预览与保存路径；普通RGB处理链可能丢alpha。作者推荐蒸馏／量化FLUX3 Klein8步、CFG1、LoRA0.95–1；非蒸馏Base20步、CFG3.5、1.0，Euler/simple。它们是作者建议，不是本库已测兼容或例图参数。
- 提示与证据：文本路线用透明背景与独立前景等描述；提取路线指定主主体或特定对象。卡片宣称背景alpha0，但本库没取得透明PNG统计，不能把棋盘预览当真实alpha验证。仓库标Apache2.0，基座、VAE、节点及上游说明分别回源。
- 读取范围：固定revision模型卡全文；未读节点实现、工作流JSON、看透明例图或核验alpha。

<a id="n04"></a>

### N04 Juggernaut Moss V1：全量微调、照片提示与展示参数的边界

**适用方向：写实人像·模型选型｜参考MOSS全量微调，并分清推荐与展示配置。**

**美术风格方向：高调写实·细肤质｜本例浅色眉睫与含蓄直视，柔光保留雀斑和皮肤纹理。**

- 原作者与原文：[KandooAI；支持RunDiffusion；基座OpenMOSS](https://huggingface.co/Kandoo/Juggernaut-Moss)。
- 原文：《Juggernaut Moss》，revision `24c1d8f87c5fa0b4e2ecc5cef28e03eb967ba26f`，2026-11-09 03:20:20 +08:00更新；首次收录，更新时间不等于首次训练日期。
- 训练说明：在MOSS-Image Base上全量微调transformer，而非LoRA；Diffusers其他组件沿用SFT。作者称精选2万余照片／电影静帧，混用长中短标注、1MP分桶、学习率6e-6、有效batch64、6epochs，使用KohakuMossTrainer。中途约4–5epoch盲选，后期手部和文字反而退化，是值得关注的选点经验。
- 精确文件：`diffusion_models/juggernaut_moss_v1_bf16.safetensors`约10.2GB，`juggernaut_moss_v1_int8_convrot.safetensors`约5.4GB；后者为前者量化，不计成新微调。4bit仍是计划。权重未下载。
- 作者通用建议：30步（范围25–50）、CFG3、shift5、负分支SLG22、约2MP，Qwen3.5_9b BF16／w4a8文本编码器与flux2-vae_small。展示部分则使用BF16、50步；不能把通用30步写成每张示范的实际配置。
- 提示写法：照片按主体、行动、光线、镜头组织；转绘画时去掉照片特有的镜头用词，以及会压制绘画／CG的负向词。需要文字时明确字面内容。手部、拥挤人群和小字仍有局限，风景建筑作者称与Base接近。
- 作者报告胜73%、Base18%、平9%；排除平局才接近80%，本库未独立核验评审与抽样。展示图经挑选，不将其等同随机输出成功率。
- 本库看图仅限[固定版本人像j005_s8005](https://huggingface.co/Kandoo/Juggernaut-Moss/blob/24c1d8f87c5fa0b4e2ecc5cef28e03eb967ba26f/images/showcase/j005_s8005.jpg)：近景直视、闭口含蓄神态、浅色眉睫、鼻颊雀斑与柔和亮调；这是单例可见特征，不能由头像概括全身体型或模型稳定倾向。具体图的完整实际参数未取得。
- 卡片标Apache-2.0，使用仍分别回源核对基座、编码器、VAE与工作流条件。
- 读取范围：固定revision模型卡全文与文件目录；实际看1张人像示范，未读工作流或复跑。

<a id="n05"></a>

### N05 Dizzle's Art Nouveau-ish v1：装饰边框与主体留白的配合

**适用方向：装饰插画·画风LoRA｜参考Illustrious新艺术资源与边框留白写法。**

**美术风格方向：新艺术·装饰童话｜按作者描述，流线轮廓、拱圆边框与柔和复古色相结合。**

- 原作者与原文：[Maridizzle](https://civitai.com/models/3042358?modelVersionId=3458228)。
- 原文：《Dizzle's Art Nouveau-ish (A Dabble Blend)》，Illustrious LoRA v1，版本ID `3458228`，2026-11-09 03:30:08.287 +08:00发布；首次收录。
- 按作者描述：结合新艺术流动线、类似Mucha的装饰拱框与圆形、柔和复古配色，面向故事书小景、藏书票、塔罗面板，也可做人物或风景。该概括来自已读文字，并非本库已看例图归纳。
- 公开用法：触发词`dzgreen`，作者通用强度0.8–0.9；主体清楚、周围给边框留空间。强度偏高可能柔化脸部，作者建议配合柔和／复古色词。这些不是指定示范图的实际设置。
- 标题称Dabble Blend，未取得混合比例或完整训练配方，不推定独立从头训练。图片元数据入口虽可读，但图像下载失败、meta为空；不凭资源名补造人物比例、五官或采样参数。
- 读取范围：完整资源说明与版本元数据；例图CDN未取得，未实际看图、读取图配方或运行。

<a id="n06"></a>

### N06 Nuke ComfyBridge：往返ComfyUI时保留色彩与元数据边界

**适用方向：合成流程·色彩管理｜区分显示变换、数据通道与EXR回传中的损失。**

- 原作者与原文：[David Borrull／dborrull](https://github.com/dborrull/nuke-comfy-pipe)。
- 原文：《Nuke ComfyBridge》，README版本0.11.1，固定commit `fb9b964c2e0d131c302fd3d27aeddb96ce099c63`，2026-11-09 02:20:35 +08:00提交；该最新提交主要调整README标题横幅，不把提交时间当新功能首发。首次收录。
- 作者流程：Nuke画面／遮罩进入ComfyUI API格式工作流，结果回传EXR，按版本保留输出。作者记录Windows Nuke17.1 Non-commercial、ComfyUI0.38 portable等环境；Linux与云端验证范围有限，不能推定跨环境完全兼容。
- 色彩关键点：普通plate先经当前Viewer OCIO／LUT转换成8-bit PNG，再在返回时逆变换到scene-linear EXR。显示变换已裁掉的高光不能靠逆变换恢复，8-bit也可能引入色阶；文件最终是EXR不代表全程浮点无损。
- 作者给出发送曝光调整等办法，把需要的范围保留在可显示区间；局部处理时保留原plate再按mask合成。深度、法线、matte等数据图采用原始浮点EXR，不应套上Viewer色彩变换。
- 归档提醒：输出EXR可写提示与工作流信息，但Nuke Write默认可能丢弃exr/*字段；ComfyUI也不能直接把EXR当含工作流PNG打开，仍需旁侧JSON。版本化输出与保存配置有参考价值，未由本库验证遮罩外像素保持或序列时序稳定。
- 读取范围：固定README的简介、色彩、输入、序列与元数据章节及提交信息；未读全部实现或运行。

<a id="n07"></a>

### N07 P-H3 Image Tools：图片槽位、Picture编号与原图职责分开

**适用方向：多参考图·自动提示｜整理P-H3扩写输入，保留原图并映射图片编号。**

**设计思路：参考编号与输入职责分开｜整理扩写用图与原始参考，并核对最终Picture编号。**

- 原作者与原文：[jalberty2018](https://github.com/jalberty2018/ComfyUI-P-H3-Image-Tools)。
- 原文：《ComfyUI P-H3 Image Tools》，固定commit `fa501aad0cfff3891e1680124ada0fb73d74230a`，2026-11-08 20:13:48 +08:00更新示例说明；首次收录。README注明ComfyUI0.44.0接口条件，MIT许可。
- 作者把提示文本、最多9张总输入（包括batch展开）组织为LLM视觉消息。空槽、None、零batch忽略，但全黑图是有效图片；槽位会自动扩展与清理末尾空输入。
- 编号按有效图片压紧：输入槽1和5实际成为Picture1和Picture2。`reference_image`找不到指定槽时会回退第一张可用图并记录日志，控件可能仍显示原选择，因此要核对生成的EditPictureN，而不是凭槽号猜文本指向。
- 扩写图按参考尺寸约1MP缩放，其余图适配并白底居中填充；RGBA会合到白底，不适合作为保留alpha的透明处理链。图片顺序不因选参考而自动提前。
- 批次节点的`upsampler_prompt`接GenerateText.prompt、`images`接GenerateText.image，LLM仍由GenerateText另行执行。用于P-H3本身的conditioning原图还要独立保留并接线；不要误把扩写用缩放图当唯一原始参考。
- 分图节点输出1–9与未用None，已含完整聊天模板时按作者说明关闭GenerateText的`use_default_template`。ResolutionSelector只给取整后的尺寸和原始参考，不自行缩放原图。上述来自文档，不等于本库已测兼容或收益。
- 读取范围：固定README全文和提交信息；未读示例JSON、代码实现或运行节点。

<a id="n08"></a>

### N08 图生3D参考图：先把视角、轮廓、背景和材质写清楚

**适用方向：3D参考图·提示词设计｜以视角、轮廓、背景和材质组织建模用输入图。**

**设计思路：参考图面向形体读取｜先让主体轮廓与体积清楚，再交给下游图生3D。**

- 原作者与原文：[Reneelry](https://www.bilibili.com/video/BV1JkWH64E9n/)。
- 原文：《【AI建模教程】图生3D总翻车？一张完美参考图让Tripo生成完美模型》，2026-11-08 22:51:16 +08:00发布，时长154秒；首次收录。
- 作者简介以海马案例，把图生3D输入整理为视角、主体、背景、材质四要素：偏侧的立体视角、完整可辨轮廓、纯色背景与清晰材质。可学习之处是围绕下游任务准备输入，而不只追求独立插画的装饰效果。
- 简介提到用Codex准备参考图再交给Tripo。视频标题和简介中关于完美模型、面数与无破面的说法属于作者宣传／个案陈述；未取得网格、具体Tripo版本、完整提示与设置，本库不据此确认几何质量或普适成功率。
- 未配置可用字幕会话，专用工具返回登录要求；未自动登录、下载媒体或做ASR。此条是简介范围的教程导读，完整演示请回原视频。
- 读取范围：专用工具完整简介、作者与发布时间；字幕需登录未取得，未看视频画面。

<a id="n09"></a>

### N09 Wardrobe V6／6.7.0：勾选池随机与特写收紧的更新

**适用方向：提示词组织·批量变化｜用勾选池安排场景变化，并保留角色和取景约束。**

**设计思路：场景随机与取景约束联动｜从选定池生成场景，特写同步减少画外信息干扰。**

- 原作者与原文：[灵冻不冻；上游ANIMA提示词生成器作者飞蓬](https://www.bilibili.com/video/BV1PVWn6tEyJ/)。
- 原文：《ComfyUI自动提示词插件继续更新，免费给大家使用，V6版本开源》，灵冻不冻，2026-11-08 18:17:28 +08:00发布；[GitHub原仓库](https://github.com/lingdongbudong/Comfyui-Anima-Wardrobe-V6)。作为[11月3日V5记录](../2026-11-03/README.md#s10)的更新，不重复计入V5已有的自然语言／人物服装绑定思路。
- 版本核对：固定commit `682bb622e2f6b3559defbcde235ef4f525169a15`（提交时间2026-11-08 02:24:42 +08:00），README、changelog与`__init__.py`均标6.7.0。视频泛称V6，不能把视频发布日期当各个子版本的发布日期。
- 新增方法：6.7.0允许姿势、艺术构图、特写三个勾选池中任选一个，每次运行从已选集合抽取；勾选池优先于全库场景随机，抽取结果只写报告、不改面板选择。作者称固定非负seed可复现，但全局服装、角色覆盖、收藏等状态也须一致，不能只留seed。
- 特写不只是加一个close-up词：作者把取景裁减规则同步到引擎，减少画外段落和角色描述把镜头拉回脸部的干扰。6.6.x还处理双人缺一位时的角色补位、预设服装单句保留等；它们是文本组织改动，不证明图像必能正确绑定两人。
- 读取代码片段确认入口版本与roll请求传递`pick_pool_mode`／`pick_pool_ids`等字段；未逐行审计抽取引擎或跑作者测试。README所称旧V5/V4/V3别名兼容是作者说明，本库未加载旧工作流验证。
- 该工具只生成文本，不生成图像。库内含成人分级词表；本条只概述通用场景、角色和构图组织，用普通插画时按作者说明使用sfw并检查实际输出。未展开成人词表、下载头像或工作流包。
- 署名与许可：灵冻不冻在飞蓬公开脚本基础上工程化重写；上游授权状态按作者声明，本仓库标GPL-3.0。资源数量或自检数量不作为图像质量依据。
- 读取范围：视频完整简介；固定README全文、changelog近期段及入口相关代码片段；未看视频、安装或出图。

## 来源覆盖

| 来源 | 实际查找与读取 | 本轮结果／边界 |
|---|---|---|
| 百度贴吧：stablediffusion吧 | aiotieba4.8.2、CREATE第1页30条，含置顶；返回吧名stablediffusion，非把stable吧当指定入口。非置顶日期已跨到11月7日。另读[机翻MOSS开发者帖](https://tieba.baidu.com/p/11177543116)10个可见楼层。 | 两个指定吧分开核对；本轮未重新测试带空格别名的重定向。该帖11月8日转载，7楼指出内容较旧，已追溯Reddit原文，不按转载日把旧计划改称新发布。 |
| 百度贴吧：comfyui吧 | 同工具CREATE第1页27条（含2024年置顶），返回吧名comfyui，非置顶日期跨过本轮窗口；另以全站“工作流 提示词”最新搜索第1页30条补线索，按tid去重。 | 列表中求助、硬件、宣传等未强行收录；这部分为列表筛选，未声称所有帖子正文已读。主工具可用，未启动Astron备用。 |
| bilibili | bilibili-api-python17.4.2游客态、pubdate：“ComfyUI 教程”第1–3页（原页共60条，日期从11月9日00:41跨到11月7日23:12），“生图 模型”与“Anima”第1页筛出2、14条11月8日以来结果；以BV去重，读取N08、N09完整简介。 | 过滤无关动画／泛安装宣传；只有两个视频详情作为导读／更新。字幕未配置现有会话、未取得；没有画面、评论或音视频下载。只读主工具可用，备用CLI未启动。 |
| Reddit | r/StableDiffusion最新50条与r/comfyui最新30条列表均403；日期及MOSS关键词网页检索，跟进贴吧原始短链，打开[开发者AMA原帖](https://www.reddit.com/r/StableDiffusion/comments/1x7zf1r/hey_guys_im_one_of_the_core_developers_of/)。 | 已读导言和部分作者回复，页面标23d ago，绝对日期未核，未读全部讨论。核到加载器／VAE兼容提醒；CFG10为单次反馈、作者自己也不确定原因，编辑模型是考虑方向。未把它计为本轮新AMA或全量覆盖。 |
| Hugging Face | text-to-image按lastModified取60条，跟进模型卡、精确revision和文件列表，读取SnapRef、FLUX3 RGBA、Juggernaut；另核对SnapRef两版LFS元数据。 | 模型卡正文可读，N04实际看1张示范；没有下载权重或验证训练效果。已报道Genesis的更名／镜像不重复计新训练。更新时间与首发日期分开。 |
| GitHub | “comfyui workflow pushed:>=2026-11-08”20项、“comfyui prompt created:>=2026-11-05”15项，跟进Nuke、P-H3及视频指向Wardrobe的原仓库、固定提交和文档。 | 文档／标题改动不当新模型或新功能首发；各条说明已读章节或片段，未安装与跑上游测试。 |
| Civitai社区／论坛 | 新文章30项、新资源40项，另查Workflows类型最新10项；读取角色标注文章、Dizzle v1完整说明／版本数据及指定图片元数据，其他工作流只筛列表。 | 覆盖文章、模型／LoRA、工作流与例图元数据入口；未单独读取完整版本讨论或评论，不声称论坛所有栏目已覆盖。Dizzle例图CDN失败，风格只按作者文字概括，不作本库视觉观察。 |
| 补充作者资料：note | 访问Pixubus4.0作者页及公开预览；搜索接口403。 | 该文标980日元且can_read=false，仅有预览，未当付费正文已读，也未纳入9项精选。 |

## 后续关注与更正

- 按全库原始链接、精确版本与实质变化去重；更新回链旧记录，历史日期和执行状态保留。
- 作者测试、机制解释、资料读取与本库验证分别理解，缺失数据不补造。

- 后续可补：Juggernaut公开工作流及同图配置、Dizzle原图配方、Wardrobe V6视频示范与旧工作流兼容；读取缺口未补齐前沿用当前边界。
- 归档说明：首批3项已于本轮先行保存，本次增补N04–N09并完成来源覆盖；没有把未执行日期补称已检索。
