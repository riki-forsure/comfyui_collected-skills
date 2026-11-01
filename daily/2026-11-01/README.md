# 2026-11-01 每日社区发现

感谢社区作者公开分享模型、工作流、教程和实践经验。本页为本库概述与分类，原作者、原文和读取范围随条目保留，欢迎回原文阅读完整说明与更新。

- 检索类型：无具体差距要求的每日广泛发现；无主动专题。
- 实际开始时间：2026-11-01 04:01（北京时间；工具UTC时钟换算）。
- 读取与续存：主要平台API快照为04:01:58–04:05:59；网页／贴吧补读另按本轮记录。12:47起继续整理已取得资料；续存时间不替代原帖日期，也不扩大已检索时间窗。
- 优先时间窗：2026-10-31 04:08之后的新增与实质更新；必要的近期补录单列。
- 执行状态：本轮已完成归档；各固定来源均已实际查询，B站及Reddit列表接口受限，部分网页可读。
- 已归档 11 项分享／实质更新（含1项Reddit历史分享，精确日期待核）。无节点安装、模型下载、生图或自动实验。

## 今日值得阅读

- [MOSS-Image-IDM-2-Steps：两步生成与属性编辑的新训练记录](https://huggingface.co/akhaliq/MOSS-Image-IDM-2-Steps)：相比上轮仅249次更新的OPD，作者另行发布数据空间8→4→2步路线，并加入参考图条件、DMD与特征矩匹配；当前root v2把编辑增量合入适配器。作者报告笑容和颜色编辑有进展，草图转照片、黑白上色仍失败。
- [PromptMaker 5.0：按模型组织提示词、角色与区域](https://civitai.com/articles/37715)：作者介绍本地提示词工作台，按目标模型生成标签或自然语言，并把角色、服装、LoRA、触发词与参考图集中管理；可对接已有图像后端。5.0新增分镜、草图及可选LoRA训练入口，适合参考界面组织与模块分工。
- [SnapRef v2a-pre2：多参考图与角色／画风分工](https://huggingface.co/0ppxnhximxr/snapref-v2a-pre2)：新增char模式尝试保留角色而弱化参考图画风；同一角色可提供上半身与全身等多参考并设置权重。作者也公开了cs模式的部分匹配指标略低于v1a，因此仍将v2a标为预览。

## 分享速查

| 编号／分享 | 原始日期／口径 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 读取状态 |
|---|---|---|---|---|---|
| [N01 MOSS-Image-IDM-2-Steps：两步生成与属性编辑的新训练记录](https://huggingface.co/akhaliq/MOSS-Image-IDM-2-Steps) | 2026-11-01 03:20:15 +08:00（当前仓库提交，非首发日） | 少步蒸馏·图像编辑｜区分文生图、属性编辑与结构改写的边界。 | — | [akhaliq](https://huggingface.co/akhaliq/MOSS-Image-IDM-2-Steps) | 当前模型卡全文、公开版本元数据；未看评估图、未读代码／日志或复跑 |
| [N02 Krea2 Turbo三步蒸馏LoRA：chk00030000](https://huggingface.co/lvladikov/Krea2-Turbo-Distill-3step-LoRA) | 2026-11-01 03:16:31 +08:00（当前仓库提交，非首发日） | 采样加速·后训练模型｜了解Krea2 Turbo从8步到3步的蒸馏用法。 | — | [lvladikov](https://huggingface.co/lvladikov/Krea2-Turbo-Distill-3step-LoRA) | 模型卡简介、文件、ComfyUI用法、Raw条件、检查点／分辨率与许可段落；中间训练细节和详细附卡未完整学习，未看图 |
| [N03 SnapRef v2a-pre2：多参考图与角色／画风分工](https://huggingface.co/0ppxnhximxr/snapref-v2a-pre2) | 2026-11-01 01:10:08 +08:00（当前仓库提交，非首发日） | 人物参考·画风控制｜组合角色多张参考并分别组织身份与画风。 | 设计思路：身份与画风分离｜参考图提供角色特征，提示词另选画风。 | [0ppxnhximxr / ArcAnima](https://huggingface.co/0ppxnhximxr/snapref-v2a-pre2) | 模型卡版本说明、参数、评估、训练与限制段落；未看示范图或训练配置文件 |
| [N04 ComfyUI Prompt Library：文件夹形式的提示词收藏](https://github.com/mitchfmartin/ComfyUI-Prompt-Library) | 2026-11-01 03:28:02 +08:00（提交作者时间） | 提示词组织·工作流复用｜命名保存并跨流程复用手动提示词。 | — | [mitchfmartin](https://github.com/mitchfmartin/ComfyUI-Prompt-Library) | 晨间快照README全文及最近3次提交；未读实现代码或运行 |
| [N05 Local LLM Prompt：进程内GGUF提示词扩写节点](https://github.com/telgip/comfyui-local-llm-prompt) | 2026-11-01 02:36:15 +08:00（提交作者时间） | 自动提示·本地LLM｜用GGUF模型将短想法扩写成提示词。 | — | [telgip](https://github.com/telgip/comfyui-local-llm-prompt) | 晨间快照README全文、2次公开提交说明；未读代码或运行 |
| [N06 PromptMaker 5.0：按模型组织提示词、角色与区域](https://civitai.com/articles/37715) | 2026-10-31 20:57:57.890 +08:00（文章发表） | 提示词组织·角色设定·多主体｜管理角色、服装及不同模型的提示格式。 | 设计思路：角色与场景分开组织｜复用外观设定，按服装、区域和目标模型组合提示。 | [Maohime；仓库Kisahime/promptmaker](https://civitai.com/articles/37715) | 公开API文章的简介、提示词、角色、参考图、自动评分、LoRA训练及FAQ选段；未读全部UI细节、仓库代码或安装 |
| [N07 Stop Merging Yourself：递归融合与LoRA叠加强度讨论](https://civitai.com/articles/37692) | 2026-10-31 07:19:17.820 +08:00（发表；07:27:55.363更新） | 模型选型·LoRA搭配｜关注检查点来源与重复叠加强度。 | 设计思路：保持风格组合的可追溯性｜作者讨论递归融合与已烘焙LoRA带来的选择问题。 | [catlover1937](https://civitai.com/articles/37692) | 文章英文论点、建议及部分中文对照；未读取所引第三方扫描材料 |
| [N08 RealAnime v1.0：Krea2半写实插画LoRA](https://civitai.com/models/3030253?modelVersionId=3442290) | 2026-11-01 03:39:28.346 +08:00（版本发布） | 插画·风格LoRA｜查阅Krea2半写实插画资源与用法。 | 半写实插画｜按作者定位，面向半写实表现并提供风格前缀。 | [Konan](https://civitai.com/models/3030253?modelVersionId=3442290) | 公开API模型卡全文、精确版本及触发词元数据；未看例图 |
| [N09 Feralux：从Illustrious风格来源到Anima的LoRA分享](https://civitai.com/models/3030264?modelVersionId=3442307) | 2026-11-01 03:50:42.835 +08:00（版本发布） | 画风迁移·LoRA搭配｜追溯Anima风格训练的素材与来源。 | 设计思路：跨基座风格迁移｜作者列出多种Illustrious风格来源用于Anima训练。 | [SlopDemon；各来源模型与LoRA作者见原卡](https://civitai.com/models/3030264?modelVersionId=3442307) | 公开API模型卡全文、精确版本与公开元数据；未看图 |
| [N10 Prompt Studio：社区作者的多模型提示词工作台](https://www.reddit.com/r/comfyui/comments/1wp6l43/prompt_studio_a_multimodel_prompt_writer/) | 绝对发布日期未取得；读取页相对显示28d ago，未倒推日期 | 自动提示·模型选型｜按目标模型组织自然语言与参考资料。 | 设计思路：内容意图与模型格式分工｜先写创作想法，再输出目标模型适用的提示。 | [u/tngklp；原项目duckyshell/ComfyUI-MiniMaxH3-Prompt-Writer](https://www.reddit.com/r/comfyui/comments/1wp6l43/prompt_studio_a_multimodel_prompt_writer/) | 搜索工具打开的原帖正文及可见部分评论；不是API完整评论树，未取得代码或媒体 |
| [N11 MOSS LoRA训练打标：画风与角色触发词的社区讨论](https://tieba.baidu.com/p/11154769701) | 2026-10-31 21:05:12 +08:00（楼主首楼create_time） | LoRA训练·标注经验｜区分画风和角色训练中的触发词经验。 | 设计思路：角色与风格条件分开考虑｜讨论不同训练目标下触发词与正则数据的作用。 | [楼主耶合鸟没有鸽▫；回帖◆旧梦◆、Brier🌿](https://tieba.baidu.com/p/11154769701) | aiotieba读取第1–3楼文字及首楼日期；未读楼中楼、图像或训练文件 |

## 当日分享

<a id="n01"></a>

### N01 MOSS-Image-IDM-2-Steps：两步生成与属性编辑的新训练记录

**适用方向：** 少步蒸馏·图像编辑｜区分文生图、属性编辑与结构改写的边界。

- 原作者与原文：akhaliq；[原文](https://huggingface.co/akhaliq/MOSS-Image-IDM-2-Steps)。
- 日期与版本：2026-11-01 03:20:15 +08:00（当前仓库提交，非首发日）；root v2编辑／T2I适配器；revision 03bb0384b12cd7aca4e8dae4011a14443d7df21d。
- 本次性质：实质更新；回链上一轮D03，保留旧OPD／SFT结果。
- 原作者分享要点（本库概述）：相比上轮仅249次更新的OPD，作者另行发布数据空间8→4→2步路线，并加入参考图条件、DMD与特征矩匹配；当前root v2把编辑增量合入适配器。作者报告笑容和颜色编辑有进展，草图转照片、黑白上色仍失败。
- 公开资料与适用条件：适配器由lora、time_embedding、dataspace三个文件组成；作者推荐bf16 MOSS-SFT。ComfyUI文生图需rapid-moss的专用加载／采样路径，普通LoRA加载不等价；v2参考编辑仅有Python路径，ComfyUI编辑节点尚未完成。发布export750；不能把旧opd_8step目录当当前root版本。
- 实际读取范围：当前模型卡全文、公开版本元数据；未看评估图、未读代码／日志或复跑。
- 信息范围与本库备注：训练方法、模块合入与四例效果均为作者记录；没有本库LongText分数或收益验证。“首个”等优先性主张未核，不据此推荐替代成熟编辑流程。旧卡仍保留以供版本比较。
- 相关原始资料：https://huggingface.co/akhaliq/MOSS-Image-IDM-2-Steps/blob/03bb0384b12cd7aca4e8dae4011a14443d7df21d/README.md
- [相关旧记录](../2026-10-31/README.md#d03)

<a id="n02"></a>

### N02 Krea2 Turbo三步蒸馏LoRA：chk00030000

**适用方向：** 采样加速·后训练模型｜了解Krea2 Turbo从8步到3步的蒸馏用法。

- 原作者与原文：lvladikov；[原文](https://huggingface.co/lvladikov/Krea2-Turbo-Distill-3step-LoRA)。
- 日期与版本：2026-11-01 03:16:31 +08:00（当前仓库提交，非首发日）；chk00030000，rank64／228模块；revision d6c863bfa47bfeb7c7648562866297faa49f09d4。
- 本次性质：首次收录；持续训练中的社区适配器。
- 原作者分享要点（本库概述）：作者从四步适配器继续训练三步模型，公开三万训练样本、检查点与分辨率对照，并分别提供Diffusers和ComfyUI键名文件。适合学习少步模型对细节、颜色、教师相似性和耗时的取舍。
- 公开资料与适用条件：ComfyUI通用建议3步、CFG1、euler/simple、LoRA1.0；此pipeline的Diffusers guidance_scale=0.0对应无引导，不能抄成ComfyUI CFG0。主训练基座Krea2 Turbo，Raw路线只是作者额外实验。遵循Krea2 Community License。
- 实际读取范围：模型卡简介、文件、ComfyUI用法、Raw条件、检查点／分辨率与许可段落；中间训练细节和详细附卡未完整学习，未看图。
- 信息范围与本库备注：2.6倍仅作者去噪计时，排除文本编码和VAE；1.11倍为22个测试提示上的纹理指标，不是整体画质评分。量化、MLX或Raw兼容说法保留作者条件，本库未验证。
- 相关原始资料：https://huggingface.co/lvladikov/Krea2-Turbo-Distill-3step-LoRA/blob/d6c863bfa47bfeb7c7648562866297faa49f09d4/README.md

<a id="n03"></a>

### N03 SnapRef v2a-pre2：多参考图与角色／画风分工

**适用方向：** 人物参考·画风控制｜组合角色多张参考并分别组织身份与画风。

**设计思路：** 身份与画风分离｜参考图提供角色特征，提示词另选画风。

- 原作者与原文：0ppxnhximxr / ArcAnima；[原文](https://huggingface.co/0ppxnhximxr/snapref-v2a-pre2)。
- 日期与版本：2026-11-01 01:10:08 +08:00（当前仓库提交，非首发日）；v2a-pre2，训练step15000；revision f47b1251310e82ccdf69df675bb1d4149bcb4608。
- 本次性质：模型预览更新；与上轮工作流中的v1b区分。
- 原作者分享要点（本库概述）：新增char模式尝试保留角色而弱化参考图画风；同一角色可提供上半身与全身等多参考并设置权重。作者也公开了cs模式的部分匹配指标略低于v1a，因此仍将v2a标为预览。
- 公开资料与适用条件：面向Anima Base v1.0，需SnapRef专用节点，不是普通LoRA加载。多图同角色应保留solo；两个不同角色使用侧向拼接专用流程。weight仅multi_layout=separate生效；strength是对数尺度，0不等于关闭。CircleStone非商业许可。
- 实际读取范围：模型卡版本说明、参数、评估、训练与限制段落；未看示范图或训练配置文件。
- 信息范围与本库备注：同角色多图与双人同框是不同输入方式。v1a仍为作者日常推荐；char模式部分衣物可能改变，实际风格分离和人物相似性未由本库验证。
- 相关原始资料：https://huggingface.co/0ppxnhximxr/snapref-v2a-pre2/blob/f47b1251310e82ccdf69df675bb1d4149bcb4608/README.md
- [相关旧记录](../2026-10-31/README.md#d04)

<a id="n04"></a>

### N04 ComfyUI Prompt Library：文件夹形式的提示词收藏

**适用方向：** 提示词组织·工作流复用｜命名保存并跨流程复用手动提示词。

- 原作者与原文：mitchfmartin；[原文](https://github.com/mitchfmartin/ComfyUI-Prompt-Library)。
- 日期与版本：2026-11-01 03:28:02 +08:00（提交作者时间）；5147de4485c4bd76bcdc01ea74e77f892a67d8b9。
- 本次性质：首次收录；当日新节点与更新。
- 原作者分享要点（本库概述）：作者把提示词保存为UTF-8文本，以目录组织库，并把收藏控件嵌入现有可编辑提示词节点。工作流保存的是当时的文字快照，选择收藏才加载文件，保存收藏与排队生图分开，适合学习轻量提示词整理方式。
- 公开资料与适用条件：普通STRING输出；可接文本编码器或AutoPrompt的brief。外部文件变化由Refresh读取，不后台轮询。作者说明保留Unicode、多行与字面花括号，保存时检查文件冲突；默认位置在ComfyUI用户目录。
- 实际读取范围：晨间快照README全文及最近3次提交；未读实现代码或运行。
- 信息范围与本库备注：作者称无需额外运行包、模型或GPU，本库未验证前端版本兼容性。文件收藏与工作流快照的关系按原文记录，不把收藏更新当成已有工作流自动变更。
- 相关原始资料：https://github.com/mitchfmartin/ComfyUI-Prompt-Library/commit/5147de4485c4bd76bcdc01ea74e77f892a67d8b9

<a id="n05"></a>

### N05 Local LLM Prompt：进程内GGUF提示词扩写节点

**适用方向：** 自动提示·本地LLM｜用GGUF模型将短想法扩写成提示词。

- 原作者与原文：telgip；[原文](https://github.com/telgip/comfyui-local-llm-prompt)。
- 日期与版本：2026-11-01 02:36:15 +08:00（提交作者时间）；cf22f4b1a61639a14064a3675520a6952d38792b。
- 本次性质：实质更新／首次收录；增加参数、嵌入聊天模板及RAM预载。
- 原作者分享要点（本库概述）：作者通过llama-cpp-python在ComfyUI进程中加载GGUF，输出可接文本编码器的字符串；本次更新增加采样选项、使用模型内嵌聊天模板和RAM预载，并提供生成后卸载以腾出显存的设置。
- 公开资料与适用条件：GGUF放models/llm-gguf；unload_after默认开，n_ctx默认4096；模型需适用的聊天模板与llama-cpp-python架构支持。文档旧0.2.68示例不支持较新Gemma3/Qwen3，不能仅按示例轮子推定兼容；不支持的可选参数可能被忽略。
- 实际读取范围：晨间快照README全文、2次公开提交说明；未读代码或运行。
- 信息范围与本库备注：作者测试模型为Promptmaster-Mistral-7B Q8_0；扩写质量、显存释放和速度未由本库验证。RAM预载是操作系统文件缓存，不等于锁页或一直驻留。
- 相关原始资料：https://github.com/telgip/comfyui-local-llm-prompt/commit/cf22f4b1a61639a14064a3675520a6952d38792b

<a id="n06"></a>

### N06 PromptMaker 5.0：按模型组织提示词、角色与区域

**适用方向：** 提示词组织·角色设定·多主体｜管理角色、服装及不同模型的提示格式。

**设计思路：** 角色与场景分开组织｜复用外观设定，按服装、区域和目标模型组合提示。

- 原作者与原文：Maohime；仓库Kisahime/promptmaker；[原文](https://civitai.com/articles/37715)。
- 日期与版本：2026-10-31 20:57:57.890 +08:00（文章发表）；5.0.0；文章37715。
- 本次性质：新增教程与版本介绍。
- 原作者分享要点（本库概述）：作者介绍本地提示词工作台，按目标模型生成标签或自然语言，并把角色、服装、LoRA、触发词与参考图集中管理；可对接已有图像后端。5.0新增分镜、草图及可选LoRA训练入口，适合参考界面组织与模块分工。
- 公开资料与适用条件：提示词功能支持Anima、Illustrious/NoobAI、FLUX、Qwen等作者列出的目标。文章明确SDXL IP-Adapter、scribble ControlNet和内置训练器面向SDXL/Illustrious，不能扩展为Anima全功能支持。训练器另驱动sd-scripts；AI评分依赖视觉模型，分数不是本库成图评价。
- 实际读取范围：公开API文章的简介、提示词、角色、参考图、自动评分、LoRA训练及FAQ选段；未读全部UI细节、仓库代码或安装。
- 信息范围与本库备注：文章中的兼容性、效果、平台支持均为作者介绍；本库没有安装、连接后端或执行评分／训练。后端与模块范围按原文分开，不能用提示词支持列表代替训练或参考图兼容清单。
- 相关原始资料：https://github.com/Kisahime/promptmaker/releases/tag/v5.0.0
- 相关原始资料：https://github.com/Kisahime/promptmaker

<a id="n07"></a>

### N07 Stop Merging Yourself：递归融合与LoRA叠加强度讨论

**适用方向：** 模型选型·LoRA搭配｜关注检查点来源与重复叠加强度。

**设计思路：** 保持风格组合的可追溯性｜作者讨论递归融合与已烘焙LoRA带来的选择问题。

- 原作者与原文：catlover1937；[原文](https://civitai.com/articles/37692)。
- 日期与版本：2026-10-31 07:19:17.820 +08:00（发表；07:27:55.363更新）；文章37692；作者观点文章，无统一模型版本。
- 本次性质：新增社区经验讨论。
- 原作者分享要点（本库概述）：作者以个人观察讨论检查点之间反复融合、已有LoRA再次叠加及画风趋同的风险，倡议自愿说明来源，并建议融合时留意基座谱系。可作为理解配方透明度与资源选型的讨论入口。
- 公开资料与适用条件：文章提及社区扫描与混合系数，但本库未取得原始扫描数据、判定方法或权重，未转述为已确认的组件检测结果。基座融合建议属于作者经验，不视为所有训练／融合任务的通则。
- 实际读取范围：文章英文论点、建议及部分中文对照；未读取所引第三方扫描材料。
- 信息范围与本库备注：原题和个别评价措辞较强，本库只概括技术观点。未采纳对具体创作者训练来源的指控，也不以风格相似反推模型谱系或配方。

<a id="n08"></a>

### N08 RealAnime v1.0：Krea2半写实插画LoRA

**适用方向：** 插画·风格LoRA｜查阅Krea2半写实插画资源与用法。

**美术风格方向：** 半写实插画｜按作者定位，面向半写实表现并提供风格前缀。

- 原作者与原文：Konan；[原文](https://civitai.com/models/3030253?modelVersionId=3442290)。
- 日期与版本：2026-11-01 03:39:28.346 +08:00（版本发布）；v1.0 / 3442290；Krea 2。
- 本次性质：新增风格资源；首次收录。
- 原作者分享要点（本库概述）：作者分享在Krea2上训练的半写实风格LoRA，公开建议权重与提示词起始短语。资料篇幅较短，适合作为风格资源入口，完整示范请回原页。
- 公开资料与适用条件：作者通用建议权重0.8–1.3，起始短语semi-realistic illustration of。基座为Krea2；同图seed、采样、VAE及完整正负提示未取得。
- 实际读取范围：公开API模型卡全文、精确版本及触发词元数据；未看例图。
- 信息范围与本库备注：风格概括按作者文字，本库未归纳人物比例、五官、表情或材质的稳定倾向。建议权重不当作某张示范的实际值，也未验证收益。

<a id="n09"></a>

### N09 Feralux：从Illustrious风格来源到Anima的LoRA分享

**适用方向：** 画风迁移·LoRA搭配｜追溯Anima风格训练的素材与来源。

**设计思路：** 跨基座风格迁移｜作者列出多种Illustrious风格来源用于Anima训练。

- 原作者与原文：SlopDemon；各来源模型与LoRA作者见原卡；[原文](https://civitai.com/models/3030264?modelVersionId=3442307)。
- 日期与版本：2026-11-01 03:50:42.835 +08:00（版本发布）；页面版本v1.0 / 3442307；正文称恢复的Feralux v3，命名差异原样保留。
- 本次性质：新增资源／恢复发布；首次收录。
- 原作者分享要点（本库概述）：作者列出训练用检查点和多枚风格LoRA来源，并说明原始数据为59张768×768图像。分享价值在于保留来源谱系与跨基座风格训练思路，而非仅给一个无法追溯的资源名。
- 公开资料与适用条件：目标基座Anima；卡中列出的Illustrious来源不等于这些权重能直接跨架构加载。当前卡未提供完整训练过程、推理权重、触发词或同图参数；本库未下载权重／数据。
- 实际读取范围：公开API模型卡全文、精确版本与公开元数据；未看图。
- 信息范围与本库备注：正文v3与页面v1.0不擅自统一；训练来源和59图信息为作者说明。各来源使用条件须分别遵循，署名和链接不代替授权；本库不凭这些来源名猜最终线条、五官或色彩。

<a id="n10"></a>

### N10 Prompt Studio：社区作者的多模型提示词工作台

**适用方向：** 自动提示·模型选型｜按目标模型组织自然语言与参考资料。

**设计思路：** 内容意图与模型格式分工｜先写创作想法，再输出目标模型适用的提示。

- 原作者与原文：u/tngklp；原项目duckyshell/ComfyUI-MiniMaxH3-Prompt-Writer；[原文](https://www.reddit.com/r/comfyui/comments/1wp6l43/prompt_studio_a_multimodel_prompt_writer/)。
- 日期与版本：绝对发布日期未取得；读取页相对显示28d ago，未倒推日期；Reddit原帖；未取得对应发行版本或提交SHA。
- 本次性质：历史分享补录／日期待核，不计为当天新发布。
- 原作者分享要点（本库概述）：作者说明项目基于duckyshell原工作扩展，把单一目标提示写作推广为多目标工作台；可输入自然语言和可选媒体参考，输出可编辑提示词。原帖明确它是UI扩展，负责写提示，不负责加载生图模型或排队生成。
- 公开资料与适用条件：原帖列Anima、Krea2文生图及Qwen Image 2.1生成／编辑等图像目标；提示写作依赖所接LLM。评论中自定义端点媒体能力识别问题与后续修复是用户／作者各自反馈，不作为本库兼容测试。
- 实际读取范围：搜索工具打开的原帖正文及可见部分评论；不是API完整评论树，未取得代码或媒体。
- 信息范围与本库备注：直接最新列表API仍403，但本帖正文已通过网页读取。原页面相对时间不足以确认具体发布日期，不冒称本轮新增；LLM偏好和视觉能力评价仅属于回帖者经验。
- 相关原始资料：https://github.com/tngklp/ComfyUI-Prompt-Studio
- 相关原始资料：https://github.com/duckyshell/ComfyUI-MiniMaxH3-Prompt-Writer

<a id="n11"></a>

### N11 MOSS LoRA训练打标：画风与角色触发词的社区讨论

**适用方向：** LoRA训练·标注经验｜区分画风和角色训练中的触发词经验。

**设计思路：** 角色与风格条件分开考虑｜讨论不同训练目标下触发词与正则数据的作用。

- 原作者与原文：楼主耶合鸟没有鸽▫；回帖◆旧梦◆、Brier🌿；[原文](https://tieba.baidu.com/p/11154769701)。
- 日期与版本：2026-10-31 21:05:12 +08:00（楼主首楼create_time）；stablediffusion吧；未给出精确底模、训练器或LoRA版本。
- 本次性质：新增社区实践讨论。
- 原作者分享要点（本库概述）：楼主反馈沿用旧模型的独特触发词方式，在MOSS画风LoRA上效果不明显；回帖◆旧梦◆分享其画风训练不设触发词、角色触发词仍有效的个人经验，并提出其他画风不加触发词的正则集思路。
- 公开资料与适用条件：本帖仅公开描述，没有完整数据、超参、编码文本或对照配方。正则集做法是回帖建议，未取得作者对照结果；不写成MOSS通用训练规则。
- 实际读取范围：aiotieba读取第1–3楼文字及首楼日期；未读楼中楼、图像或训练文件。
- 信息范围与本库备注：区分楼主疑问与回帖经验，不能据单帖断言触发词无效或所有画风LoRA无需触发。本文记录可学习线索，不替用户设计或启动训练实验。

## 实际平台覆盖

| 平台 | 入口、实际范围与状态 |
|---|---|
| stablediffusion 吧 | aiotieba 4.8.2 CREATE列表1页30条，吧名返回stablediffusion；列表跨过上轮窗口，置顶旧帖单独跳过。两组全站最新查询“lora 训练”“工作流 提示词”共取得39条跨吧结果，再核吧名。选读触发词帖第1–2楼、MOSS打标帖第1–3楼；后者收录N11。未把单个旧帖当作完整历史边界。 |
| comfyui 吧 | aiotieba CREATE列表1页29条，吧名返回comfyui，标题范围跨过上轮时间。窗口内主要为整合包与求助；未逐帖读正文，未称全吧无优质更新。规范入口https://tieba.baidu.com/f?kw=comfyui；stable diffusion规范别名为stablediffusion，未测试带空格入口的浏览器重定向。 |
| bilibili | “ComfyUI 教程”“生图 模型”两组pubdate搜索API均HTTP412。补充两组网页搜索，发现MOSS训练与社区玩法视频；两原视频页均412，只有搜索摘录，未当作已读教程收录。未读视频、字幕或评论。 |
| Reddit | r/StableDiffusion与r/comfyui最新JSON接口均403，未配置OAuth。网页检索可取得部分历史原帖；实际打开Prompt Studio原文与部分评论，按历史分享收录N10；另一篇Prompt Creator旧工作流已读作补充。搜索近期过滤仍返回旧内容，未称覆盖最近24小时全量更新。 |
| Hugging Face | 按lastModified取得40个text-to-image候选；选读IDM两步、Krea2三步、SnapRef预览卡，并核元数据revision。另取得ZYI-Flash短卡，未入选。当前仓库提交与卡中训练版本分别记录，不用仓库创建时间充当首发。未下载权重或看图。 |
| GitHub | 两组仓库搜索：10月31日以来更新的ComfyUI工作流15项、10月新建提示词项目10项；读取Prompt Library与Local LLM Prompt README和近期提交。SHA定位相关提交，正文为晨间默认分支快照，未逐文件比较代码或运行。 |
| Civitai 社区／论坛 | Newest文章25项、模型／版本30项；选读PromptMaker5、递归融合讨论、Illustrious训练反馈，以及RealAnime／Feralux原卡与精确版本。文章／模型评论和带配方作品未深入覆盖，原卡图片未实际看过；附件和可下载配置元数据不等于本库已读文件。 |
| 其他论坛／作者资料 | note.com搜索API403；ComfyUI标签RSS完整取得，检查12条近期标题，未进一步读其正文或断言无优质新增。额外资料主要沿原作者GitHub与模型卡追溯；不以转载代替原作者证据。 |
| 日期、去重与范围 | 相较10月31日报，N01明确区分旧SFT／OPD与新root编辑适配器；N03与旧工作流使用的SnapRef版本分开。N10为历史补录且日期未核，不计为当天发布。各平台覆盖为抽样阅读，未声明穷尽全站。 |

## 来源补充与后续关注

- [NanashiAnon：AI Toolkit for Illustrious LoRAs: It just doesn't work!](https://civitai.com/articles/37731)，2026-11-01 01:44:33北京时间发表；文章正文已读。作者报告两次训练的角色、衣物与结构问题，未给出完整可对照配置。本库保留负面使用反馈，不据标题判定整个工具对Illustrious无效。
- [Anima触发词下划线讨论](https://tieba.baidu.com/p/11155032871)，2026-10-31 23:52:42北京时间；第1–2楼文字已读。楼主与回帖缺少控制条件，不能概括成所有LoRA都无需触发词，相关经验与N11分别看待。
- [Prompt Creator Workflow旧教程](https://www.reddit.com/r/comfyui/comments/1vyf5s4/prompt_creator_workflow/)正文与可见回帖已读，保留本地提示词生成、模型卸载及缺失依赖的学习线索；未下载Pastebin配置，不机械拆成第二套相似提示词工具推荐。
- 风格标签按原作者文字与实际读取范围概括；本轮没有本库看图观察。后续遇实质更新再补充原帖、版本与具体变化。

资料读取、作者报告、视觉观察与实际生成分别记录。本次归档不等于效果验证。

[返回总索引](../../每日检索可速查总结.md)
