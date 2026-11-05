# 2026-11-06 每日社区发现

本页汇总社区作者的公开分享，感谢原作者的投入。本库以中文概述与原文入口帮助查阅，欢迎前往原帖阅读完整教程、后续更新并支持作者；署名和链接不等同于转载授权。

- 北京日期：2026-11-06；本轮03:58开始检索，04:08完成整理（均为北京时间）。
- 检索类型：无具体差距要求的每日广泛发现。
- 执行状态：已完成本轮广泛筛选，9项首次收录；部分来源与证据层级受限。
- 时间窗：优先11月5日各来源快照之后新增与实质变化，补查11月3–5日近期首次收录；各来源分页窗口不同，不声称覆盖全部新增。
- 本页均为本库概述／学习备注；作者描述、社区反馈和本库判断分别标明。未安装节点、下载模型、生成图像或验证收益。

## 今日值得阅读

- [HaDeS MOSS Turbo](https://huggingface.co/DeVilDoNia/HaDeS-MOSS-Turbo)：少步适配器不只比速度，也分别记录文字布局、色彩、多样性与分辨率的取舍。
- [NitroFusion2](https://huggingface.co/ChenDY/NitroFusion2)：完整模型与去蒸馏LoRA职责不同，两步方案需要按步骤开关。
- [MOSS布局画布](https://civitai.com/articles/38095)：将对象、层级、坐标和准确文字组织为可编辑JSON。

## 分享速查

| 类别 | 分享／资源与版本 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点／可学习经验 | 读取状态 |
|---|---|---|---|---|---|---|
| 后训练／少步LoRA | [N01 HaDeS MOSS Turbo：分开选择文字布局、多样性与八步版本](#n01) | 少步生成·MOSS选型｜区分四步文字布局、多样性与八步使用条件。 | — | [DeVilDoNia／Devildonia；基座OpenMOSS团队](https://huggingface.co/DeVilDoNia/HaDeS-MOSS-Turbo) | 作者从SFT零起训练rank2局部层LoRA，分别提供Turbo、Diverse与8steps文件；公开小样本评估与未测条件。 | 模型卡全文；未看示范图、结果附录、实现或权重。 |
| 后训练／完整模型 | [N02 NitroFusion2：一至两步模型与首步去蒸馏LoRA](#n02) | 少步生成·Z-Image｜查阅一至两步模型及首步LoRA的不同职责。 | — | [Dar-Yen Chen、Yi-Zhe Song／ChenDY](https://huggingface.co/ChenDY/NitroFusion2) | Z-Image-Turbo衍生模型；两步方案只在第一步用0.5去蒸馏LoRA，第二步关闭。 | 模型卡全文；未读独立工作流JSON、论文、训练代码或例图。 |
| 构图／可视提示工具 | [N03 MOSS布局画布：拖拽区域后输出JSON提示](#n03) | 构图控制·文字排版｜将区域框、层级与文字整理为MOSS布局提示。 | 设计思路：布局与文字分层｜先安排对象区域和叠放顺序，再明确要渲染的文字。 | [g1ts](https://civitai.com/articles/38095) | 作者发布无后端画布，用框、标签、颜色和文字生成MOSS布局JSON，保留尺寸与坐标约束。 | 文章正文全文与内嵌JSON；未运行网页、读实现或看效果图。 |
| 特化LoRA／线条控制 | [N04 Line Weight Slider Anima v2：先辨认基座再调整线条](#n04) | 人物插画·线条控制｜按Anima或NoobAI版本区分线条权重方向。 | 设计思路：线条层级｜分离线条粗细控制，并考虑底模与其他风格LoRA的影响。 | [ABridgetooFar](https://civitai.com/models/2972655?modelVersionId=3453242) | Anima版正权重增粗、负权重变细，NoobAI／Illustrious版方向相反；v2作者称改进范围与一致性。 | 模型介绍全文、前两Anima版本说明及文件元数据；未看例图或取得同图参数。 |
| 工作流／LoRA管理 | [N05 LoRA Preset：把组合与强度保存在工作流里](#n05) | LoRA搭配·工作流管理｜将模型LoRA组合存入JSON并用下拉菜单切换。 | — | [RasmonT](https://github.com/RasmonT/comfyui-workflow-lora-presets) | 预设跟随工作流分享，文件和权重另备；Model-only节点不会提供CLIP LoRA作用。 | 固定commit README全文及最新提交说明；未读实现或运行节点。 |
| 提示词／设计方法 | [N06 视觉美学风格库：将风格、版式和配色分开组织](#n06) | 提示词组织·平面设计｜把主体、风格、版式与配色分层组织为文本。 | 设计思路：风格与版式解耦｜分别安排表现方式、信息层级和配色，主体描述另行补足。 | [爱折腾的摄影大叔／lovephoto588](https://github.com/lovephoto588/MYTX-vision-style-prompt) | 以可组合文本组织视觉设计方向；v1.9.2提醒主体信息不足不能只靠追加风格段弥补。 | 固定commit README全文与v1.9.2提交说明；未读数据集、渲染器、独立教程或运行脚本。 |
| 自动提示／分镜流程 | [N07 OnePromptStoryboard：共用台本组织四格分镜与后续动画](#n07) | 分镜设计·自动提示｜用共同台本生成四格分镜并保留后续编辑入口。 | 设计思路：台本共用·分镜复用｜先固定镜头内容与顺序，再单独调整动作和相机。 | [かみもと｜ローカルAI生成／sepiablue-ai](https://note.com/sepiablue/n/n532bc1496cde) | 日本作者介绍一条输入驱动MOSS分镜与H3；明确生成后不读图纠偏，并提供保留分镜的编辑分支。 | 免费公开文章正文全文；未看图／视频或读工作流JSON、实现。 |
| 社区实践／模型选型 | [N08 四类模型LoRA对照：保留作者的训练差异与社区讨论](#n08) | LoRA训练·模型选型｜参考跨模型练习，并留意训练与提示差异。 | 设计思路：风格学习分项观察｜比较细节、姿态与设定保留，同时记录数据和训练差异。 | [神秘哀嚎者；相关反馈见原帖](https://tieba.baidu.com/p/11169224284) | 作者展示MOSS、Krea2、Anima与光辉的LoRA练习，后续补充图片、提示和训练步数有差异；评论讨论控制变量。 | aiotieba读取首页首楼与2–8楼文字；未看图、楼中楼或取得训练／出图配置。 |
| 采样／已有LoRA迁移 | [N09 P-H3-Image少步用法：复用视频LoRA时检查实际调度](#n09) | 少步生成·H3适配｜区分已有视频LoRA复用与图像采样网格设置。 | — | [akhaliq；原LoRA larryvrh／InstantX；基座PrunaAI](https://huggingface.co/akhaliq/p-h3-image-turbo-lora) | 不是新训练权重；作者将已有H3视频LoRA用于P-H3-Image，并说明手动sigma网格不能只改步数字段。 | 模型卡全文；未看对照图、读独立脚本／工作流JSON、核验映射或复跑。 |

## 当日分享

<a id="n01"></a>

### N01 HaDeS MOSS Turbo：分开选择文字布局、多样性与八步版本

**适用方向：少步生成·MOSS选型｜区分四步文字布局、多样性与八步使用条件。**

- 原作者与原文：[DeVilDoNia／Devildonia；基座OpenMOSS团队](https://huggingface.co/DeVilDoNia/HaDeS-MOSS-Turbo)。
- 原文：《HaDeS MOSS Turbo》。原文与版本：模型卡快照 revision `241bb1fbaba2be9e5fcb4ba1e9bbf1375e354487`，仓库更新2026-11-06 03:49:02 +08:00；更新时间不作为首次发布证明。当前首次收录。
- 作者分享要点：针对MOSS-Image SFT训练少步适配器，rank2，仅24–41层，每文件约3.4MB。`HaDeS-MOSS-Turbo-v0.6.safetensors`侧重文字／布局，`HaDeS-MOSS-Turbo-Diverse-v0.6.safetensors`侧重开放提示的变化，`HaDeS-MOSS-Turbo-8steps-v0.7.safetensors`为八步版本；不是同一文件改名。
- 作者实测配置：`moss_image_sft_bf16`，CFG1、Euler/simple、shift5.0、LoRA1.0；前两文件4步，v0.7为8步。可用原生LoraLoaderModelOnly＋KSampler，HaDeS节点为可选路径，不要求另装。
- 取舍：作者在1024及以上发现四步版颜色偏淡；前两文件加至八步只测了色彩，不能套用四步文字测试结果。v0.7的1024成对审图仅每提示一个seed；2048的五例均偏好对照lodestones版本，作者把v0.7定位于不超过1024。上述为作者测量与审图，本库未复核。
- 训练说明：DMD加回归项，冻结SFT，从零训练生成LoRA；作者借鉴akhaliq配方但声明未使用其LoRA权重。其他基座、强度、编辑／低去噪质量未测；int8微调模型和img2img运行检查不证明质量兼容。许可标Apache2.0，回原页核对LICENSE／NOTICE。
- 读取范围：模型卡全文；未看示范图、结果附录、实现或权重。

<a id="n02"></a>

### N02 NitroFusion2：一至两步模型与首步去蒸馏LoRA

**适用方向：少步生成·Z-Image｜查阅一至两步模型及首步LoRA的不同职责。**

- 原作者与原文：[Dar-Yen Chen、Yi-Zhe Song／ChenDY](https://huggingface.co/ChenDY/NitroFusion2)。
- 原文：《NitroFusion2: Bringing Adversarial Loss to the Text Stream of Multimodal Diffusion Transformers》。原文与版本：revision `9845835ab4622031406d667b96d9bcd1140b6083`，仓库更新2026-11-05 16:01:49 +08:00；卡片News明示11月3日发布，属于近期首次补录，非今日首发。
- 作者分享要点：在Z-Image-Turbo上进行对抗蒸馏，将损失放到MMDiT的文本流与图像特征，发布一至两步文生图模型。完整transformer、去蒸馏LoRA与GGUF量化为不同用途，不把每种量化计作新训练。
- 公开用法：两步方案的`nf2-dedistill-lora.safetensors`仅首步0.5，第二步关闭；其作用是向Z-Image-Turbo方向去蒸馏以减轻部分伪影，并非全程挂载的通用细节LoRA。卡片Diffusers例为FlowMatchEulerDiscreteScheduler、shift6、sigmas=[1.0,0.5]、guidance_scale0；不可把此接口值直接当作ComfyUI CFG。
- 公开资料：卡片链接一／两步ComfyUI JSON及各自GGUF工作流、[代码仓库](https://github.com/ChenDarYen/NitroFusion2)、项目页与论文。模型卡标Apache2.0。示例与清晰文字、细节收益属于作者展示，本库尚未看图、下载权重、读取JSON或复跑。
- 读取范围：模型卡全文；未读独立工作流JSON、论文、训练代码或例图。

<a id="n03"></a>

### N03 MOSS布局画布：拖拽区域后输出JSON提示

**适用方向：构图控制·文字排版｜将区域框、层级与文字整理为MOSS布局提示。**

**设计思路：布局与文字分层｜先安排对象区域和叠放顺序，再明确要渲染的文字。**

- 原作者与原文：[g1ts](https://civitai.com/articles/38095)。
- 原文：[Draw the layout, paste the JSON — a visual prompt builder for MOSS Image](https://civitai.com/articles/38095)，2026-11-05 15:08:48.457 +08:00；近期首次收录。
- 作者分享要点：[MOSS-Image-SFT Canvas](https://g1ts.github.io/moss-image-sft-canvas/)提供浏览器画布，画对象框、编辑描述与文字、拖拽对象顺序，输出JSON；作者称静态网页无需账号或后端。[源仓库](https://github.com/g1ts/moss-image-sft-canvas)是原作者资源入口，本次未读其实现。
- 设计方法（按作者文字）：`summary.meta`承载整体风格标签，`summary.caption`描述场景，`items`放每对象描述与准确文字；列表顺序表达叠放关系。文章以680×384、七个区域的猫与告示牌为例，不把该例推广为固定画风。
- 公开条件：`abs_centralized`坐标、`yxyx`框顺序；画布尺寸须与输出宽高一致。作者SFT建议50步、CFG3，严格跟框时约5，属于其通用建议，不是本库已测最优值，也不是所有少步LoRA的设置。
- 本库整理备注：与[11月5日杂志布局经验](../2026-11-05/README.md#n09)互补：本篇重点是将空间安排变为可编辑输入；JSON有效或网页可用都不保证模型逐字、逐框实现。仅概述方法并回链原作者，不转载整段示例。
- 读取范围：文章正文全文与内嵌JSON；未运行网页、读实现或看效果图。

<a id="n04"></a>

### N04 Line Weight Slider Anima v2：先辨认基座再调整线条

**适用方向：人物插画·线条控制｜按Anima或NoobAI版本区分线条权重方向。**

**设计思路：线条层级｜分离线条粗细控制，并考虑底模与其他风格LoRA的影响。**

- 原作者与原文：[ABridgetooFar](https://civitai.com/models/2972655?modelVersionId=3453242)。
- 原文：《Line Weight Slider - Bridge Tools (NoobAI/Illustrious/Pony + Anima)》，当前Anima v2.0／3453242，2026-11-06 03:46:56.096 +08:00；旧Anima v1.0／3405741发布10月15日。本库首次收录，以当前v2为主，并非此前已报道版本的再次计数。
- 作者分享要点：把线条粗细作为独立调节维度；作者称v2扩大Anima滑块范围并改善一致性。作者同时提醒Anima结果仍较不稳定，效果随检查点自身线条与叠加画风LoRA变化。
- 作者通用建议：Anima正值增粗、负值变细，约+1.5／−1；NoobAI／Illustrious负值增粗、正值变细，约−0.5／+0.5。符号方向不同，不能只换模型文件沿用同一值；本次没有取得Pony分支的独立设置依据。
- 精确资源：`Line weight Anima v2.safetensors`，API报告文件SHA-256 `258A564DD9405BC965834A11923B458650107ECE9919DEBC83C4EB8B7710D7BB`。这是平台文件哈希，未下载或本地重算。作者称Anima版在Anima训练，NoobAI版在NoobAI XL训练并可用于Illustrious；不推为所有衍生底模完全兼容。
- 本库整理：本篇属于线条设计方法与特化资源，未看图，故不概括人物体型、五官或整体固定画风。配置是作者通用建议，不是某张例图的实值。
- 读取范围：模型介绍全文、前两Anima版本说明及文件元数据；未看例图或取得同图参数。

<a id="n05"></a>

### N05 LoRA Preset：把组合与强度保存在工作流里

**适用方向：LoRA搭配·工作流管理｜将模型LoRA组合存入JSON并用下拉菜单切换。**

- 原作者与原文：[RasmonT](https://github.com/RasmonT/comfyui-workflow-lora-presets)。
- 原文：《LoRA Preset (saved in workflow)》。固定提交 `b6d00079e7e45d7bc9526d7b5b7bbc87ade3673a`，2026-11-06 02:14:42 +08:00；最新提交仅新增publish.yml，不把全部预设功能描述为本次新增。首次收录。
- 作者分享要点：预设由LoRA文件名与强度组成，保存在节点／工作流内部，而非额外磁盘预设文件；下拉切换整套组合，`strength_multiplier`统一缩放，输出MODEL与实际应用清单info。
- 操作经验：右键收集启用的LoraLoaderModelOnly／LoraLoader，跳过已经流入本节点的上游LoRA，减少重复收集；支持JSON编辑、导入与复制。预设改动仍需保存工作流才持久化。
- 边界：本节点只作用MODEL，不加载CLIP部分；源图里使用LoraLoader不代表预设重现其CLIP改动。JSON不包含LoRA权重，接收者须另备同名文件，缺件按名称报告。MIT许可；本库仅读文档，不判定任意文件组合兼容。
- 读取范围：固定commit README全文及最新提交说明；未读实现或运行节点。

<a id="n06"></a>

### N06 视觉美学风格库：将风格、版式和配色分开组织

**适用方向：提示词组织·平面设计｜把主体、风格、版式与配色分层组织为文本。**

**设计思路：风格与版式解耦｜分别安排表现方式、信息层级和配色，主体描述另行补足。**

- 原作者与原文：[爱折腾的摄影大叔／lovephoto588](https://github.com/lovephoto588/MYTX-vision-style-prompt)。
- 原文：《视觉美学风格库 · vision-style-prompt》，固定提交 `10473536a15838ea87f2193c43e4b32b03ff3279`，2026-11-05 17:43:07 +08:00，提交标v1.9.2。首次收录，功能集不全是该次新增。
- 作者设计方法：将风格、排版、配色视为可独立选择的层；风格模板再拆色彩、构图、质感、光影、质量、风格标记、情绪，主体描述另写。按目标模型语法重排，输出提示词，不负责生成图像。
- 近期修改：作者从自有模板统计发现风格段相对固定，短稿常因主体信息过少；v1.9.2据此调整主体提示、草稿说明与篇幅反馈。这里的字数预算来自项目自身配置／启发式，不能推广成所有模型最佳词数，篇幅达标也不证明图像更好。
- 公开使用思路：先锁定模型与风格，再组合主体、排版及主题色；英文段需要提供对应翻译，缺译保留中文并提示。参考图隔离句是作者的提示写法，不保证模型一定只取风格而不带入其他内容。
- 资料与许可：README称含173风格、54版式、36色、17模型适配；数量仅说明组织规模，不作质量排名。代码MIT，风格文本／文档CC BY4.0并要求署名；参考图片明确不随库授权。外部模型许可须分别回源确认，本库不复制模板库或参考图。
- 读取范围：固定commit README全文与v1.9.2提交说明；未读数据集、渲染器、独立教程或运行脚本。

<a id="n07"></a>

### N07 OnePromptStoryboard：共用台本组织四格分镜与后续动画

**适用方向：分镜设计·自动提示｜用共同台本生成四格分镜并保留后续编辑入口。**

**设计思路：台本共用·分镜复用｜先固定镜头内容与顺序，再单独调整动作和相机。**

- 原作者与原文：[かみもと｜ローカルAI生成／sepiablue-ai](https://note.com/sepiablue/n/n532bc1496cde)。
- 原文：《【MOSS-Image × MiniMax H3】文章1つからストーリーボードと動画を作るノードを公開しました！（導入・使い方）》，2026-11-05 05:27:20 +08:00；API price0、can_read=true，正文完整取得。以下为本库中文概述，非逐字翻译。
- 作者分享要点：一段故事输入先由本地Qwen3.5生成共同台本，再转为MOSS静态分镜提示与H3动作／相机指令。当前限定横排或竖排四格、约14秒；不是任意格数、自由排版的图像解析系统。
- 可学习方法：台本同时保留每格场地、静态构图、动作与镜头，避免给两个生成阶段各写一份互不对应的指令；满意分镜保存后，可走只编辑H3的分支，复用图像并调整动作。台本seed与MOSS／H3seed不同；台本及H3提示目前需手动复制保存。
- 作者公开条件：ComfyUI0.42.0，MOSS SFT INT8、8step DMD LoRA／强度1、CFG1，Qwen共用；普通示例额外角色／画风LoRA关闭。MOSS-Storyboard0.1.2固定提交 `4d848d5854c7e39ef8cbb8b8163fec7d31963dd6`。这些是文章实测环境，不是本库安装或跨硬件保证。
- 边界：Qwen不看生成后的分镜，不能识别分镜偏离台本并自动修正；随意已有图也不会自动读成故事。额外角色触发词只追加到MOSS提示，不自动追加到H3。作者记录指尖与快动作缺陷，Ref2VA也非完全保持分镜画风。
- 资源入口：[ComfyUI-OnePromptStoryboard](https://github.com/sepiablue-ai/ComfyUI-OnePromptStoryboard)。GitHub最新提交快照 `c34967b5f0a7598c24bf46c1ba8e47314527112d`为10月27日英文／日文文档提交；本次主要依据11月5日文章，不将旧代码提交写成当天新增，也未独立核验文章涉及的整个依赖链。
- 读取范围：免费公开文章正文全文；未看图／视频或读工作流JSON、实现。

<a id="n08"></a>

### N08 四类模型LoRA对照：保留作者的训练差异与社区讨论

**适用方向：LoRA训练·模型选型｜参考跨模型练习，并留意训练与提示差异。**

**设计思路：风格学习分项观察｜比较细节、姿态与设定保留，同时记录数据和训练差异。**

- 原作者与原文：[神秘哀嚎者；相关反馈见原帖](https://tieba.baidu.com/p/11169224284)。
- 原帖：《目前主流模型学习能力对比，第1弹》，stablediffusion吧；楼主首楼2026-11-05 16:47:09 +08:00，2楼16:59补充。首次收录，原帖tid11169224284。
- 原作者分享：将MOSS、Krea2、Anima与光辉用于同一内容方向的LoRA练习并展示结果。楼主随即说明并非严格同数据／同提示：随时间有图片增减，为模型调整提示，Anima练得偏多并自述有过拟合。
- 公开细节：作者2楼报训练步数大约MOSS2000、Krea2 4000、Anima6000、光辉4000；没有给训练器、学习率、rank、精确底模、数据清单或完整出图参数，不能补成同条件对照。
- 社区反馈：4–5楼提出缺参考画风、变量较多；8楼分享自身经验，认为时间步策略也会改变效果。3楼给出个人细节／姿态偏好，属于评论者审图与经验，不转述成本库看图判断。
- 本库整理：这篇的阅读价值在跨路线尝试及参与者对比较条件的讨论。保留作者自述局限，不据这些图或步数排列整体学习能力，也不把角色服饰与单例差异概括为模型固定画风。
- 读取范围：aiotieba读取首页首楼与2–8楼文字；未看图、楼中楼或取得训练／出图配置。

<a id="n09"></a>

### N09 P-H3-Image少步用法：复用视频LoRA时检查实际调度

**适用方向：少步生成·H3适配｜区分已有视频LoRA复用与图像采样网格设置。**

- 原作者与原文：[akhaliq；原LoRA larryvrh／InstantX；基座PrunaAI](https://huggingface.co/akhaliq/p-h3-image-turbo-lora)。
- 原文：《P-H3-Image-Turbo LoRA》，revision `a3373d735c3d63dc56652d5b8f810bdc521d71cb`，仓库更新2026-11-06 03:12:57 +08:00，非首次发布证明。本次首次收录该适配器迁移文档；与[11月4日P-H3-Image基础介绍](../2026-11-04/README.md#d01)为不同资料；本次新增的是旧LoRA迁移与调度经验，不是新增一套训练权重。
- 权重来源：`minimax_h3_turbo_4step_ema_ckpt500_diffusers.safetensors`来自InstantX对larryvrh视频LoRA的转换；本仓库ComfyUI文件是同权重不同键名。作者称363个目标模块可对应到P-H3-Image；本库未读映射或独立检查，不以作者合并成功推断所有H3 LoRA完全兼容。
- 作者配置：主要推荐6步、LoRA1.0；ComfyUI将原工作流固定八步ManualSigmas替换为BasicScheduler／simple／6步／denoise1，Euler与Basic Guider，保留无CFG及无负向分支。Diffusers模块管线需显式传sigmas，作者指出只改num_inference_steps会仍走旧网格。
- 评估范围：H200、bf16、2912²下原八步约11.9秒，六步约9秒；作者四条提示的盲看偏好不能推广为所有场景。本库未看A/B。四步作者称更软；v4_step600是卡片建议的后续候选，没有进入上述验证，不能混成已测检查点。
- 附加分支：卡片另报pDMD2-NFE两步迁移，伴随构图漂移／伪文字；Realism0.5叠加的作者人物经验不能推广至文字图。具体分支调度与原六步不同，本篇不拼接为统一最优配置。
- 许可条件：原LoRA标Apache2.0，P-H3-Image及衍生使用另受MiniMax H3社区许可约束；不能仅凭适配器许可判断整个流程可商用或在所有地区可用，使用前回基座LICENSE核对。
- 读取范围：模型卡全文；未看对照图、读独立脚本／工作流JSON、核验映射或复跑。

## 来源覆盖

| 来源 | 实际入口／操作及范围 | 结果与限制 |
|---|---|---|
| stablediffusion吧 | aiotieba4.8.2，CREATE最新第一页30条；03:59快照，返回规范吧名stablediffusion；按首楼时间看有6条11月5日新主题，列表已跨至11月2日 | 读11169224284首页1–8楼，收录N08。未翻更多列表页、看图或楼中楼，跨过时间边界不等于全部回复增量已覆盖。 |
| comfyui吧 | 同一主工具，CREATE最新第一页28条；03:59快照，返回规范吧名comfyui；7条11月5日以来主题，列表已跨至11月2日 | 新主题以求助、配置疑问、整合包或远程部署分享为主，本轮未进一步读其正文，未选正式条目；不能称该吧无优质新增。 |
| 贴吧全站补搜 | 最新搜索“LoRA 工作流”第一页返回23条，结果跨多个吧并包含历史内容 | 按实际吧名、tid与日期筛选；一次复合词结果不能代表所有类别。主工具成功，未启用Astron备用、检查备用依赖或循环切换。用户“stable diffusion／stablediffusion”入口本次实际使用规范名stablediffusion，未把另一个stable吧当成它。 |
| bilibili | bilibili-api-python17.4.2只读脚本；ComfyUI按pubdate第1／2页各20条，另“生图 模型”第1页返回14条日期筛选结果、“Anima”返回6条；均按BV去重筛选 | 页间有重叠且日期边界不严格递进，不能由第二页推断完整回溯。详情取得[ControlNet笔记](https://www.bilibili.com/video/BV1Bk4b6nERH/)（学杂了的吴形，11月5日18:17）与[Anima提示词工具2.0](https://www.bilibili.com/video/BV1244b6hEZ3/)（Zove-try，11月5日19:49）的完整简介、作者／日期及分P元数据。未看画面、评论或工作流。 |
| bilibili筛选与字幕 | ControlNet简介只概述主题，未足以提炼实际步骤；Anima2.0简介称重做UI、检索收藏与修复0.8问题，可回看[11月4日同作者标签工具记录](../2026-11-04/README.md#d04) | 尚未读置顶链接确认2.0与旧项目的精确版本关系，不另算新模型或完整教程；保留视频入口待补。字幕调用返回login_required，未配置会话，未自动登录／提取Cookie／下载音视频／ASR，也未启用CLI备用。 |
| Reddit | r/StableDiffusion/new.json?limit=50与r/comfyui/new.json?limit=30均实际请求；另以MOSS／workflow和11月5日日期做两条站内定向网络搜索 | 最新JSON均403，日期定向搜索未命中；未读到本轮新帖正文，记录为访问受限与该查询无命中，不能声称社区无更新或已完整覆盖。 |
| Hugging Face | text-to-image按lastModified最新60项，动态发现少步训练、LoRA与转换资源；进一步读4张模型卡 | 正式选N01／N02／N09；Reflora短卡不足以说明具体实践，未选。三项均核对固定revision README与先前读到的正文相同；未读权重、原始图像、讨论或全部工作流。lastModified不是首发日期。 |
| GitHub | 搜索comfyui workflow pushed自11月5日20项、comfyui prompt created自11月1日15项；按用途与既往记录筛选 | N05／N06固定commit README全文与最新提交说明已读；N07仅取得关联仓库提交元数据，主体证据来自note文章。新提交不必然等于全套功能新增。未运行节点或脚本。 |
| Civitai文章／教程 | 最新文章列表30项；正文读取38095（布局画布）与38086（Moss-Image and fast illustrations） | 收录N03；38086作者比较插画与摄影的选型视角，涉及未看的示例，本轮未另立重复MOSS选型条目。列表与正文可读，不把接口成功写作已看图。 |
| Civitai模型／版本／配置线索 | Newest／Day模型列表40项；读取2972655模型介绍、前两Anima版本说明及文件元数据 | 收录N04并保留精确版本链接。文章内JSON是公开配方线索，不是已取得例图元数据；作品图、模型评论与版本讨论未专项读取，其他列表项也未逐个读全文。 |
| 其他作者资料 | note作者／RSS线索，读取n532bc1496cde免费公开全文与作者信息，沿文中GitHub资源定位版本 | 收录N07。未看嵌入视频、原尺寸图或工作流JSON；保留作者已说明的固定格数、版本与未做图像纠偏等限制。 |

以上为有界筛选与实际读取记录；“未选条目”“访问受限”“查询无命中”分别记录，不推断全网无新增。

## 后续关注与更正

- 以原文链接、资源版本与实质变化去重；全库检索本页原链接和资源名未发现已收录条目，当前均为首次收录，近期补录与今日发布不混称。
- 模型卡中的作者评估不代表本库独立验证；若后续读取配置或图像，再注明增量与日期。
- 后续优先补读Anima2.0视频置顶原仓库／版本链接；已有11月4日记录先回链，不据视频标题重复计数。Reddit恢复可读后从本次失败快照继续补查，不跳过这段时间。
- 同日记录：先归档3项已读内容与索引，再补至9项并完善来源覆盖；没有改写此前日期的执行状态。
