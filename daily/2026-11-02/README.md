# 2026-11-02 每日社区发现

感谢社区作者公开分享。本页以本库概述保存分享要点、原作者和原文入口，欢迎回原文阅读完整教程、示范和后续更新。

- 北京日期／开始时间：2026-11-02 04:02（工具UTC时钟换算）。
- 检索类型：每日广泛发现；无具体差距要求，无主动专题。
- 优先时间窗：自2026-11-01晨间成功检索快照后的新增与实质更新。上轮午间是已读资料补存，未当作检索窗口结束。
- 执行状态：本轮已完成整理并归档10项；Reddit、bilibili接口受限，部分来源仅完成列表或文字阅读，详见覆盖表。
- 已归档 10 项分享／实质更新；未安装节点、下载权重、启动生图或自动实验。

## 今日值得阅读

- [XeroDesign-1.0：Z-Image图形海报LoRA](https://huggingface.co/xerofounder/XeroDesign-1.0)：作者以696张整理海报训练Z-Image专用LoRA，给出基座revision、目标模块、触发词与Diffusers示例。适合查阅从图形设计素材到海报特化适配器的训练与使用入口。
- [MOSS多语言实践：SFT、少步方案与LoRA组合的同场景记录](https://civitai.com/articles/37809)：作者以英、乌克兰、捷克三种语言和六个场景，对照原始MOSS-SFT、DMD八步及自定义LoRA组合。主集72张，加混合语言附加集共84张；固定seed并记录复用的试验图、失败和评价波动，值得参考的是任务组织和对照边界。
- [分色草图处理多人动作：从背负姿态到比例修正](https://note.com/ullstudio/n/n5585bce3e280)：作者分享文字无法稳定表达背负动作时，使用红／黑分色草图区分两人及遮挡关系。草图腿长错误曾被生成结果补偿为奇怪姿态，经过两次修正才接近意图；背靠背抱臂仍失败，文章保留了这些过程。

## 分享速查

| 编号／分享 | 日期／口径 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 读取状态 |
|---|---|---|---|---|---|
| [R01 Anima：按时间步区间查看LoRA训练损失](https://civitai.com/articles/37807) | 2026-11-02 00:27:38.411 +08:00（文章发表） | LoRA训练·检查点选择｜分别观察不同噪声区间的损失变化。 | — | [ame_la / amenorira](https://civitai.com/articles/37807) | 公开API中英文文章正文全文；未看曲线图、未读训练器实现 |
| [R02 XeroDesign-1.0：Z-Image图形海报LoRA](https://huggingface.co/xerofounder/XeroDesign-1.0) | 2026-11-02 03:47:50 +08:00（当前仓库提交，非首发日） | 海报设计·后训练LoRA｜面向网格排版、几何构成与字体布局。 | 瑞士平面·包豪斯几何｜按作者描述，强调非对称网格、字体与高对比构图。 | [xerofounder；数据来源xerocore/argonz-curated-design](https://huggingface.co/xerofounder/XeroDesign-1.0) | 模型卡全文及版本元数据；未看示范图、未读训练文件或推理服务代码 |
| [R03 Hammershoi FLUX 3 Klein LoRA：静谧室内绘画](https://huggingface.co/jejunepixels/Hammershoi-Flux3-LoRA) | 2026-11-02 00:23:26 +08:00（当前仓库提交，非首发日） | 室内插画·风格LoRA｜参考低饱和室内、孤立人物与窗光表现。 | 低饱和绘画·柔和窗光｜本例以长裙纵向轮廓、侧背姿态与留白营造静谧。 | [jejunepixels；借鉴Vilhelm Hammershøi画作，素材来源见原卡与数据集](https://huggingface.co/jejunepixels/Hammershoi-Flux3-LoRA) | 模型卡全文与版本元数据；实际查看hammershoi_woman_full_s42.jpg一张原生示范 |
| [R04 ZuperWorkflow：模块化Z-Image工作流与三段风格组织](https://github.com/martin-rizzo/ZuperWorkflow) | 2026-11-02 01:44:01 +08:00（本轮最新提交） | 自动化工作流·风格组织｜用模块模板维护基础和高级Z-Image流程。 | 设计思路：风格与布局分层｜以Core、Layout、Final组织基础表现、构图和最终观感。 | [martin-rizzo](https://github.com/martin-rizzo/ZuperWorkflow) | README全文及最近3条提交说明；未读工作流JSON、生成器实现或节点源码 |
| [R05 YP TagForge Plus：本地标签检索、别名补全与提示词整理](https://github.com/OsanRey/ComfyUI-YP-TagForge-Plus) | 2026-11-02 01:40:03 +08:00（本轮最新提交） | 提示词组织·标签检索｜从本地词库查找标签、别名与关联词。 | — | [OsanRey](https://github.com/OsanRey/ComfyUI-YP-TagForge-Plus) | README全文及最近3条提交说明；未读扩展实现、词库或UI实际行为 |
| [R06 8GB显存实践：六组模型配置的耗时与占用记录](https://civitai.com/articles/37784) | 2026-11-01 17:06:31.860 +08:00（文章发表） | 低显存·资源选型｜参考同一设备下不同模型配置的运行成本。 | — | [tinytensor](https://civitai.com/articles/37784) | 公开API文章正文全文；未看对比图、未取得作者提及的工作流文件 |
| [R07 MOSS多语言实践：SFT、少步方案与LoRA组合的同场景记录](https://civitai.com/articles/37809) | 2026-11-02 02:14:40.489 +08:00（文章发表） | 多主体关系·提示词语言｜参考三种语言在同场景约束中的表现记录。 | 设计思路：内容归属与空间约束｜用相同场景检查对象、文字和空间关系的表达。 | [JSKrueger](https://civitai.com/articles/37809) | 公开API正文中方法、配置、评价规则及六场景评述的前约9500字符，另读末尾约4300字符提示词附录；未读全部正文和全部提示、未看84张图 |
| [R08 从Illustrious素材到Krea2角色LoRA：数据转换与标注经验](https://civitai.com/articles/37802) | 2026-11-01 23:16:08.593 +08:00（文章发表） | 角色LoRA·训练数据·图像编辑｜参考跨媒介素材转换与角色特征标注。 | 设计思路：角色识别与媒介迁移｜保留发色与辨识特征，再整理写实训练素材。 | [Angelure；起始模型Illust-Asian_coser_Realism作者Ray3780](https://civitai.com/articles/37802) | 公开API文章正文全文（约3164字符）；未看示范图、未取得数据集或训练配置文件 |
| [R09 贴吧社区分享：离线HTML提示词分类与检索页](https://tieba.baidu.com/p/11156654577) | 2026-11-01 13:52:56 +08:00（楼主首楼） | 提示词组织·资源检索｜按类别、中英文和首字母浏览提示词。 | — | [宇宙恶魔萝什💝](https://tieba.baidu.com/p/11156654577) | aiotieba读取该帖第1–12楼文字；核对楼主、首楼日期与第8楼更新；未下载或运行HTML |
| [R10 分色草图处理多人动作：从背负姿态到比例修正](https://note.com/ullstudio/n/n5585bce3e280) | 2026-11-01 22:19:35 +08:00（原文23:19:35 +09:00） | 多主体·构图姿态·草图控制｜用分色草稿说明遮挡、动作与人物比例。 | 设计思路：遮挡关系与形体草稿｜分色区分人物，先修正草图比例再约束动作。 | [underplay / ULL Studio](https://note.com/ullstudio/n/n5585bce3e280) | note公开文章API全文约3978日文字符；未看插图或视频、未读软件实现 |

## 当日分享

<a id="r01"></a>

### R01 Anima：按时间步区间查看LoRA训练损失

**适用方向：** LoRA训练·检查点选择｜分别观察不同噪声区间的损失变化。

- 原文标题：Anima：按时间步区间查看LoRA训练损失。
- 原作者与原文：ame_la / amenorira；[原文](https://civitai.com/articles/37807)。
- 日期与精确版本：2026-11-02 00:27:38.411 +08:00（文章发表）；文章37807；lora-scripts-anima的log_timestep_loss选项，代码提交未核。
- 本次类型：首次收录；按已读来源归档。
- 原作者分享要点（本库概述）：作者解释总loss会混合不同样本和时间步，按低、中、高噪声分别记录后，能发现总loss下降时细节区间仍波动的情况。文中强调训练步数与扩散时间步不同，分区作用也有重叠。
- 公开资料与条件：公开选项log_timestep_loss，可在TensorBoard查看分区曲线；重点是各自随训练变化，不直接比较不同区间的数值高低。作者仍以同提示、同seed的不同检查点出图作为选择参考。
- 实际读取范围：公开API中英文文章正文全文；未看曲线图、未读训练器实现。
- 信息范围与本库备注：本文是作者训练记录与分析方法，不把某段loss单独当成画质评分。未取得精确模型、数据和训练超参，不据此给出用户训练参数。
- 相关原始资料：https://github.com/amenorira/lora-scripts-anima
- 相关原始资料：https://github.com/kohya-ss/sd-scripts/blob/main/docs/timestep_sampling_offset.md

<a id="r02"></a>

### R02 XeroDesign-1.0：Z-Image图形海报LoRA

**适用方向：** 海报设计·后训练LoRA｜面向网格排版、几何构成与字体布局。

**美术风格方向：** 瑞士平面·包豪斯几何｜按作者描述，强调非对称网格、字体与高对比构图。

- 原文标题：XeroDesign-1.0：Z-Image图形海报LoRA。
- 原作者与原文：xerofounder；数据来源xerocore/argonz-curated-design；[原文](https://huggingface.co/xerofounder/XeroDesign-1.0)。
- 日期与精确版本：2026-11-02 03:47:50 +08:00（当前仓库提交，非首发日）；rank32；revision c84a8aefb69bae16694c384a25f5da67b07f8216。
- 本次类型：首次收录；按已读来源归档。
- 原作者分享要点（本库概述）：作者以696张整理海报训练Z-Image专用LoRA，给出基座revision、目标模块、触发词与Diffusers示例。适合查阅从图形设计素材到海报特化适配器的训练与使用入口。
- 公开资料与条件：基座Tongyi-MAI/Z-Image，文中基座revision为04cc4abb7c5069926f75c9bfde9ef43d49423021；r/alpha32，目标to_q/k/v、to_out.0。触发argonz_design poster；示例832×1216、28步、guidance4.0。模型卡许可Apache-2.0，训练素材使用条件另核。
- 实际读取范围：模型卡全文及版本元数据；未看示范图、未读训练文件或推理服务代码。
- 信息范围与本库备注：本库仅按作者文字归纳设计方向；未验证具体排版遵循、字体清晰度或ComfyUI兼容性。卡中量化训练描述和推理示例分别记录，不拼成某张示范的实值。
- 相关原始资料：https://huggingface.co/xerofounder/XeroDesign-1.0/blob/c84a8aefb69bae16694c384a25f5da67b07f8216/README.md

<a id="r03"></a>

### R03 Hammershoi FLUX 3 Klein LoRA：静谧室内绘画

**适用方向：** 室内插画·风格LoRA｜参考低饱和室内、孤立人物与窗光表现。

**美术风格方向：** 低饱和绘画·柔和窗光｜本例以长裙纵向轮廓、侧背姿态与留白营造静谧。

- 原文标题：Hammershoi FLUX 3 Klein LoRA：静谧室内绘画。
- 原作者与原文：jejunepixels；借鉴Vilhelm Hammershøi画作，素材来源见原卡与数据集；[原文](https://huggingface.co/jejunepixels/Hammershoi-Flux3-LoRA)。
- 日期与精确版本：2026-11-02 00:23:26 +08:00（当前仓库提交，非首发日）；revision 22b7b8f5fddd6b49f0b6399bfc12960c44a6c8bb；FLUX3 Image Klein Base。
- 本次类型：首次收录；按已读来源归档。
- 原作者分享要点（本库概述）：作者用288幅裁切画作训练，并公开六提示／一个种子的有限测试、训练设置与使用限制。本库实际看了一张临窗女性示范：米灰色调、柔光与颗粒笔触，人物窄肩、盘发、长裙轮廓显得修长，侧背而立；阴影中的五官不作细分。
- 公开资料与条件：作者建议30步、guidance3.5、LoRA1.0、1024²，提示结尾hmrsh style；示范seed42、关闭prompt upsampler。更高权重可能增颗粒并改变人物衣着。作者未测试蒸馏版Klein、prompt upsampler或ComfyUI。FLUX Kommunity许可，需核基座访问条件。
- 实际读取范围：模型卡全文与版本元数据；实际查看hammershoi_woman_full_s42.jpg一张原生示范。
- 信息范围与本库备注：视觉观察只限本例，不概括整个模型的人体比例或表情倾向。原作者描述与本库看图区分；未复跑，单图、单seed测试不证明跨主体稳定。实际看图不等于本库生成或收益验证。
- 相关原始资料：https://huggingface.co/jejunepixels/Hammershoi-Flux3-LoRA/blob/22b7b8f5fddd6b49f0b6399bfc12960c44a6c8bb/README.md
- 相关原始资料：https://huggingface.co/jejunepixels/Hammershoi-Flux3-LoRA/blob/22b7b8f5fddd6b49f0b6399bfc12960c44a6c8bb/images/hammershoi_woman_full_s42.jpg

<a id="r04"></a>

### R04 ZuperWorkflow：模块化Z-Image工作流与三段风格组织

**适用方向：** 自动化工作流·风格组织｜用模块模板维护基础和高级Z-Image流程。

**设计思路：** 风格与布局分层｜以Core、Layout、Final组织基础表现、构图和最终观感。

- 原文标题：ZuperWorkflow。
- 原作者与原文：martin-rizzo；[原文](https://github.com/martin-rizzo/ZuperWorkflow)。
- 日期与精确版本：2026-11-02 01:44:01 +08:00（本轮最新提交）；提交bc2bbe7508428a13027a7c403510ed3ab31ef091；README当前分支快照。
- 本次类型：首次收录；按已读来源归档。
- 原作者分享要点（本库概述）：作者将基础／高级工作流从模块模板生成，配合流程内说明，方便查阅各环节和维护不同组合。三段风格组织也提供了一种将整体表现、布局与收尾分开管理的思路。最新提交涉及适配新ComfyUI APP的模板与zmakefile代码。
- 公开资料与条件：README要求ComfyUI v0.27+、Z-Image Power Nodes v2.1.2+；使用GGUF时才需要对应加载器。列出的权重组合为z_image_turbo_int8_convrot_bf16emixed.safetensors、qwen3-4b_int8_convrot_fp16emixed.safetensors、Z-Image_half_natural_vae.safetensors。风格来源src/STYLES.sty.txt，生成器zmake.py；项目CC0，权重使用条件另核。
- 实际读取范围：README全文及最近3条提交说明；未读工作流JSON、生成器实现或节点源码。
- 信息范围与本库备注：版本条件和分层方法按作者文档整理；未核对每个模板分支、实际编码文本与采样数值，未安装或运行，兼容性未验证。
- 相关原始资料：https://github.com/martin-rizzo/ZuperWorkflow/commit/bc2bbe7508428a13027a7c403510ed3ab31ef091

<a id="r05"></a>

### R05 YP TagForge Plus：本地标签检索、别名补全与提示词整理

**适用方向：** 提示词组织·标签检索｜从本地词库查找标签、别名与关联词。

- 原文标题：ComfyUI YP TagForge Plus。
- 原作者与原文：OsanRey；[原文](https://github.com/OsanRey/ComfyUI-YP-TagForge-Plus)。
- 日期与精确版本：2026-11-02 01:40:03 +08:00（本轮最新提交）；README列0.1.8；提交e33375db73b8d95044d00f2ff5d59a42093d70c4。
- 本次类型：首次收录；按已读来源归档。
- 原作者分享要点（本库概述）：作者提供本地CSV标签、别名、画师和角色检索，可将blueeyes匹配为blue_eyes，并配置空格、分隔符和前缀。关联词使用共现Jaccard，首查建立SQLite索引，后续复用；俄语翻译可在界面修改并写回词库。
- 公开资料与条件：支持Danbooru／e621词库，但关联词仅来自Danbooru，稀有词、画师或e621独有词可能没有关联。作者说明格式化会保护权重、转义括号、LoRA和通配符，代码类只读字段跳过；默认不自动下载或要求实时API。
- 实际读取范围：README全文及最近3条提交说明；未读扩展实现、词库或UI实际行为。
- 信息范围与本库备注：0.1.8的已审词条及修订数量仅是作者维护记录，不证明全词库质量。@等前缀是工具可选格式，不据此推断所有目标模型都需要。节点／前端兼容与提示词保护功能未实测。
- 相关原始资料：https://github.com/OsanRey/ComfyUI-YP-TagForge-Plus/commit/e33375db73b8d95044d00f2ff5d59a42093d70c4

<a id="r06"></a>

### R06 8GB显存实践：六组模型配置的耗时与占用记录

**适用方向：** 低显存·资源选型｜参考同一设备下不同模型配置的运行成本。

- 原文标题：What actually runs on 8 GB of VRAM — six models, measured。
- 原作者与原文：tinytensor；[原文](https://civitai.com/articles/37784)。
- 日期与精确版本：2026-11-01 17:06:31.860 +08:00（文章发表）；文章37784；ComfyUI 0.42.1 portable；各权重精确哈希未取得。
- 本次类型：首次收录；按已读来源归档。
- 原作者分享要点（本库概述）：作者在RTX3070Ti笔记本8GB上，记录Qwen Image2.1、NoobAI-XL、MOSS2.5D、Z-Image与FLUX等六组配置。固定方形尺寸、提示词和seed，预热一次后测三次取中位数；适合了解低显存环境中的可运行组合与迭代耗时。
- 公开资料与条件：Windows11、Ryzen7 6800H、32GB内存、1024²。作者记录Qwen2.1四步Lightning方案16.0秒、NoobAI-XLv1.1二十八步18.3秒、MOSS2.5D二十五步38.2秒；其余Qwen八步48.4秒、Z-Image INT8三十步58.4秒、FLUX.1-dev Q4_K_S二十步72.5秒。各组采样器／CFG／加速LoRA不同，非同计算量测试；显存峰值约6983–7675MB含约1.2GB桌面占用。
- 实际读取范围：公开API文章正文全文；未看对比图、未取得作者提及的工作流文件。
- 信息范围与本库备注：耗时是作者特定笔记本与环境的报告，不能推广到所有8GB显卡或作为统一画质排名。纵向画幅数据是单次运行，不能与方图三次中位数混为一组统计。作者的审美评价及负面词作用说明未在本库验证。

<a id="r07"></a>

### R07 MOSS多语言实践：SFT、少步方案与LoRA组合的同场景记录

**适用方向：** 多主体关系·提示词语言｜参考三种语言在同场景约束中的表现记录。

**设计思路：** 内容归属与空间约束｜用相同场景检查对象、文字和空间关系的表达。

- 原文标题：MOSS across English, Ukrainian and Czech: SFT, Turbo and a custom LoRA stack。
- 原作者与原文：JSKrueger；[原文](https://civitai.com/articles/37809)。
- 日期与精确版本：2026-11-02 02:14:40.489 +08:00（文章发表）；文章37809；四条管线A–D；各latest权重的文件哈希未核。
- 本次类型：首次收录；按已读来源归档。
- 原作者分享要点（本库概述）：作者以英、乌克兰、捷克三种语言和六个场景，对照原始MOSS-SFT、DMD八步及自定义LoRA组合。主集72张，加混合语言附加集共84张；固定seed并记录复用的试验图、失败和评价波动，值得参考的是任务组织和对照边界。
- 公开资料与条件：共同条件为Qwen3.5-9B INT8、Flux2 VAE、832×1216、Euler/simple、denoise1、shift5、seed104729、空负面词。A：SFT INT8 convrot，50步／CFG3／SLG22；B：同基座加DMD8 LoRA0.7，8步／CFG1／关闭SLG；C：PrimeLust SFT FP16加context0.25与lighting0.15，50步／CFG3.5／SLG22；D：C的组合再用B的少步设置。作者环境RX9070XT、ComfyUI0.43.0；细节见原文。
- 实际读取范围：公开API正文中方法、配置、评价规则及六场景评述的前约9500字符，另读末尾约4300字符提示词附录；未读全部正文和全部提示、未看84张图。
- 信息范围与本库备注：单seed和少量场景不能判定通用语言优劣。各方案同时改变步数、CFG、SLG、精度和LoRA，只能讨论整套方案；AI辅助、标签遮蔽评价不等于人类盲评。作者自己记录同图复评波动，细小分差不能作稳定收益结论。乌克兰语文章37812是同作者译文，合并为一项。
- 相关原始资料：https://civitai.com/articles/37812
- 相关原始资料：https://huggingface.co/lodestones/MOSS-Image-SFT-8-steps-dmd/blob/f95df83b5e90ae91ea412434b3f9b7f1c8c6314f/README.md

<a id="r08"></a>

### R08 从Illustrious素材到Krea2角色LoRA：数据转换与标注经验

**适用方向：** 角色LoRA·训练数据·图像编辑｜参考跨媒介素材转换与角色特征标注。

**设计思路：** 角色识别与媒介迁移｜保留发色与辨识特征，再整理写实训练素材。

- 原文标题：From Illustrious to photo: how I made an adult, realistic Raphtalia LoRA for Krea 2。
- 原作者与原文：Angelure；起始模型Illust-Asian_coser_Realism作者Ray3780；[原文](https://civitai.com/articles/37802)。
- 日期与精确版本：2026-11-01 23:16:08.593 +08:00（文章发表）；文章37802；Krea2 Raw训练记录，资源版本ID与权重哈希未取得。
- 本次类型：首次收录；按已读来源归档。
- 原作者分享要点（本库概述）：作者以明确成年、SFW的虚构角色同人素材，记录从Illustrious系生成18张不同服装／场景图，经Krea2图生图转换、局部修色，再训练角色LoRA的过程。文末发现提示工具偷偷加入发色词而影响结果，也提示排查实际输入文本的价值。
- 公开资料与条件：作者案例的转换设置为Krea2 CyberRealistic、8步、CFG1、Euler/simple配Detailer LoRA；denoise0.25仍像玩偶，0.35较平衡，0.45开始漂移。Lab仅拷贝颜色恢复眼色。训练用ai-toolkit、Krea2 Raw、18图加裁切、rank32、lr1e-4、1024px、1380步，每300步保存；触发词rphtlv2_perso。作者保留固定发色描述，不标耳尾以让触发词承载身份。
- 实际读取范围：公开API文章正文全文（约3164字符）；未看示范图、未取得数据集或训练配置文件。
- 信息范围与本库备注：这些数值与打标取舍是作者单一角色案例，不能当跨模型默认参数。作者称16GB设备约75分钟，不代表本库已复现。尊重原素材作者及角色权利人，文章的署名与链接不等于素材可任意转载或训练授权。

<a id="r09"></a>

### R09 贴吧社区分享：离线HTML提示词分类与检索页

**适用方向：** 提示词组织·资源检索｜按类别、中英文和首字母浏览提示词。

- 原文标题：小白自己（大嘘）做了个提示词大全的html。
- 原作者与原文：宇宙恶魔萝什💝；[原文](https://tieba.baidu.com/p/11156654577)。
- 日期与精确版本：2026-11-01 13:52:56 +08:00（楼主首楼）；tid11156654577；第8楼作者更新入口，旧压缩包入口已被作者替换。
- 本次类型：首次收录；按已读来源归档。
- 原作者分享要点（本库概述）：楼主分享离线HTML提示词浏览页，介绍类别检索、中文／英文首字母筛选与可选AI接口。第8楼补充分类和常用提示词模板，并改用共享文件夹更新；适合了解社区将词条组织为可浏览资料页的做法。
- 公开资料与条件：第8楼保留作者当前分享入口和变更说明，推荐先回原帖查看更新。作者自述词库由大模型辅助整理，数量未经本库核验；AI接口功能作者当时也未实际使用。
- 实际读取范围：aiotieba读取该帖第1–12楼文字；核对楼主、首楼日期与第8楼更新；未下载或运行HTML。
- 信息范围与本库备注：未检查词库来源、词条准确性、许可或接口行为，不把作者宣称的词条数作为质量证明。旧分享链接不再当当前资源入口；精确适配模型与收益未知。

<a id="r10"></a>

### R10 分色草图处理多人动作：从背负姿态到比例修正

**适用方向：** 多主体·构图姿态·草图控制｜用分色草稿说明遮挡、动作与人物比例。

**设计思路：** 遮挡关系与形体草稿｜分色区分人物，先修正草图比例再约束动作。

- 原文标题：言葉で出ない構図は、ラフで決める：おんぶを色分けのラフで（Photo Director 1.3.18）。
- 原作者与原文：underplay / ULL Studio；[原文](https://note.com/ullstudio/n/n5585bce3e280)。
- 日期与精确版本：2026-11-01 22:19:35 +08:00（原文23:19:35 +09:00）；Photo Director1.3.18；文末说明使用MiniMax H3；精确模型文件版本未公开取得。
- 本次类型：首次收录；按已读来源归档。
- 原作者分享要点（本库概述）：作者分享文字无法稳定表达背负动作时，使用红／黑分色草图区分两人及遮挡关系。草图腿长错误曾被生成结果补偿为奇怪姿态，经过两次修正才接近意图；背靠背抱臂仍失败，文章保留了这些过程。
- 公开资料与条件：该版本让草图优先控制姿态／布局，文字补服装、场景与表情，草图面部只作标记而非身份依据。支持保留草图、暂时停用和重画；这些是作者应用内流程，不是通用ComfyUI参数。
- 实际读取范围：note公开文章API全文约3978日文字符；未看插图或视频、未读软件实现。
- 信息范围与本库备注：本文带作者自有应用的产品介绍背景；方法摘要按文字整理，不声称观看成功样图。白边重试和seed观察属于作者记录，本库未执行自动重试；运行变慢的显存解释是作者推测。未取得通用工作流和权重，不推断其他模型直接兼容。
- 相关原始资料：https://www.ullstudio.com/local

## 实际平台覆盖

| 平台 | 入口、范围与结果 |
|---|---|
| 百度贴吧：stablediffusion吧 | aiotieba4.8.2主工具／仓库只读脚本。CREATE最新列表1页30条，接口实际吧名stablediffusion、fid27893765；本页已出现早于上轮快照的记录，置顶旧帖单独识别。打开HTML提示词帖并核对首楼与更新楼，收录R09。另于04:12补查带空格的“stable diffusion”入口1条，实际返回stable吧的2018年置顶公告：此结果不属于指定吧，排除；不能把带空格名称当作已核实的自动重定向。每日使用无空格stablediffusion实际入口。 |
| 百度贴吧：comfyui吧 | 同一主工具，CREATE最新列表1页29条，实际吧名comfyui、fid28034273；本页也见早于上轮快照的记录。读取图生图求助帖11156558938首楼，无已读解决方法；不当成新教程。另读漫画帖11157861203第1–3楼，未查看漫画图片，未据此评价角色一致性。 |
| 贴吧补充搜索 | 全站最新搜索“生图 工作流 分享”返回16条、“LoRA 提示词 教程”20条；按实际吧名、tid及首楼日期筛选，其他吧或旧帖不冒充指定两吧新增。本轮无主工具失败，未启动Astron备用；一次分页不声称覆盖所有历史。 |
| bilibili | 工作流／模型两组公开搜索API均HTTP412；补充网页检索返回较旧教程与无关结果，本轮未取得值得独立推荐的新详情。状态为接口受限＋网页补查未选出新增，不推断平台无更新。 |
| Reddit | r/StableDiffusion与r/comfyui最新JSON均HTTP403；补充网页检索与一次原帖打开。实际读到2025-11-28的Z-Image历史讨论正文和部分评论，未取得本轮增量全貌；旧帖不冒充近期新帖。 |
| Hugging Face | text-to-image按lastModified读取40条，阅读全文卡4份：精选两个实际风格LoRA（R02／R03）；一份官方Qwen量化打包不记为新后训练，一份Civitai镜像不重复计。R03实际看原生示范一张，其他条目未看图。 |
| GitHub | 近期ComfyUI工作流仓库搜索15条、提示词相关新仓库搜索10条；完整读取ZuperWorkflow与TagForge README及各3条提交说明，收录R04／R05。未读其JSON与实现，不把搜索命中或提交时间当作已验证的新功能。 |
| Civitai社区 | 最新文章列表25条、模型／版本列表30条；读取Anima时间步、8GB显存、角色训练文章全文与shift短文，MOSS多语言长文仅读方法／配置／场景评述和部分附录（R07注明范围）。精选R01／R06–R08，双语重复合并；模型评论、工作流文件及带配方作品未深入，本轮不声称这些分区均已读。 |
| 其他作者论坛：note.com | 站内搜索HTTP403，但RSS成功读取10个标题，进一步取得分色草图文章全文，收录R10。搜索受限和原文可读分别记录；未看文章插图／视频。 |

## 后续关注与来源补充

- 后训练模型本轮已实际检索并阅读全文卡：Z-Image海报LoRA与FLUX 3绘画LoRA；另有Anima训练分析、Krea2角色训练案例和MOSS少步组合记录。官方模型的量化打包与资源镜像没有冒充新的训练成果。
- 已读但未单列推荐：[HAMWN的MOSS shift短讨论](https://civitai.com/articles/37775)提供粗略区间经验，配套条件不足；保留原文供查阅，不转写为通用推荐值。
- Reddit补充读到的历史原帖：[u/Whipit，Z-Image Best Practices for Maximum Detail & Clarity（2025-11-28）](https://www.reddit.com/r/StableDiffusion/comments/1p8xtln/zimage_best_practices_for_maximum_detail_clarity/)。只读首帖和部分可见评论，未读全部1157行；回复对分辨率、采样与文字效果有不同经验，不把旧版设置移作当前各模型的默认配方。
- 本轮只进行公开资料研究与摘要整理。所有方法均未在本库运行；文字阅读、看图观察、软件加载、复跑成图和用户认可分别记录。后续关注以原作者更新与已记录的读取缺口为线索，不自动生成实验任务。
- 本日目录先归档3项，再补齐7项及真实覆盖；仅新增／合并已读来源，保留既有日期历史。
- 入口更正：带空格“stable diffusion”的本轮接口补查返回stable吧，不能计入stablediffusion覆盖；指定吧的有效覆盖来自无空格入口。本轮未因此切换工具或把旧置顶当作近期唯一结果。

[返回总索引](../../每日检索可速查总结.md)
