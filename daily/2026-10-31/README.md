# 2026-10-31 每日社区发现

本页汇总社区作者公开分享的模型、工作流、提示词和实践经验。感谢原作者投入；以下为本库概述，欢迎通过原文入口阅读完整内容、使用说明和后续更新。

- 北京日期与实际检索时间：2026-10-31；2026-10-31 03:59 起，截至 2026-10-31 04:08:27 +08:00。
- 检索类型：无具体差距要求的每日广泛发现；无主动专题。
- 执行状态：本轮已归档，固定来源均已尝试；Reddit及部分详情／图片入口受限。
- 优先时间窗：自上轮 2026-10-30 02:26 后的新增与实质变化；贴吧上轮补查至14:40。首次收录的较早资料单独标明；当前仓库提交时间不作模型首发时间。
- 本次已保存 13 项分享／更新；未安装节点、下载权重、运行生图或验证收益。

## 今日值得阅读

- [Anima CharRef＋LLLite：人物参考、姿态与分区组合](https://github.com/quinteroac/ComfyUI-Anima-CharRef-LLLite)：作者解释参考适配器引入额外参考帧后，普通LLLite补丁的token范围不匹配；实验节点只把控制施加于生成帧，并提供最简姿态、Pose Studio和区域绘制流程。新提交加入SnapRef与两种参考方法的切换。
- [KleinAttentionMask：从编辑预测差分估计掩码](https://github.com/774417678/ComfyUI_KleinAttentionMask)：作者在同latent、同噪声状态下比较编辑指令与保持原图的预测，输出影响热图和掩码；区分同状态中性配对、源latent和相邻预测等模式，公开额外计算开销与不适用条件。
- [MOSS Alpha LoRA：透明素材流程与社区试用反馈](https://note.com/kongo_jun/n/n439f8889b93a)：原作者以39张RGBA数据训练概念验证LoRA，配合RGBA VAE输出透明PNG；社区教程给出ComfyUI接线资源，并反馈画面有一定退化。两种来源的介绍与试用评价分别保留。

## 分享速查

| 编号／分享与版本 | 原始日期／口径 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 读取状态 |
|---|---|---|---|---|---|
| [D01 Mossling：面向16GB显存的 MOSS 压缩实验](https://huggingface.co/AiArtLab/mossling) | 2026-10-30T22:20:54+08:00（仓库当前提交时间，非首发日） | 低显存研究·模型压缩｜了解剪枝、编码器替换及其画质取舍。 | — | [recoilme / AiArtLab Team](https://huggingface.co/AiArtLab/mossling) | 模型卡全文、提交列表；未看例图、未运行 |
| [D02 MOSS-Image Reality LoRA Preview：日常手机人像](https://huggingface.co/Richarddzz/moss-image-reality-lora) | 2026-10-31T02:34:00+08:00（仓库当前提交时间，非首发日） | 写实人像·风格LoRA｜用于MOSS-SFT的日常手机摄影表现。 | 手机摄影·柔和自然光｜按作者描述，保留轻微噪点、虚化和随手构图。 | [Richarddzz](https://huggingface.co/Richarddzz/moss-image-reality-lora) | 中英文模型卡全文及版本元数据；未看例图 |
| [D03 MOSS-Image-IDM-LoRA：密集文字训练与2步蒸馏记录](https://huggingface.co/akhaliq/MOSS-Image-IDM-LoRA) | 2026-10-31T03:04:49+08:00（仓库当前提交时间，非首发日） | 文字生成·蒸馏经验｜比较文字数据微调与少步蒸馏的作用。 | 设计思路：文字版面｜以菜单、海报和标牌等密集文字场景组织训练数据。 | [akhaliq（模型卡署名）](https://huggingface.co/akhaliq/MOSS-Image-IDM-LoRA) | 模型卡全文与公开版本元数据；未看评估拼图 |
| [D04 Anima CharRef＋LLLite：人物参考、姿态与分区组合](https://github.com/quinteroac/ComfyUI-Anima-CharRef-LLLite) | 2026-10-31T03:46:16+08:00（提交） | 人物参考·姿态控制·多主体｜组合参考身份、3D姿态与区域布局。 | 设计思路：人物与布局分工｜参考图提供人物特征，姿态和区域图分别控制动作与位置。 | [quinteroac；参考适配器来自ElectronGirl，控制模型来自toyxyz](https://github.com/quinteroac/ComfyUI-Anima-CharRef-LLLite) | 当前README的方法、节点、工作流与限制段落及最近3次提交；未看图／视频 |
| [D05 MOSS QwenVL Layout：参考图转布局与自动提示](https://github.com/leroy989/ComfyUI-MOSS-QwenVL-Layout) | 2026-10-31T02:57:47+08:00（提交） | 自动提示·构图控制·多主体｜从参考图或文字生成MOSS区域提示。 | 设计思路：布局与风格分开组织｜将对象、文字与遮挡关系放入区域，另设整体风格。 | [leroy989](https://github.com/leroy989/ComfyUI-MOSS-QwenVL-Layout) | README主要方法、输入输出、坐标与Prompt Builder段落，最近3次提交；未看例图或工作流JSON |
| [D06 KleinAttentionMask：从编辑预测差分估计掩码](https://github.com/774417678/ComfyUI_KleinAttentionMask) | 2026-10-31T04:00:40+08:00（提交） | 局部编辑·自动掩码｜由Klein9B编辑指令估计需要贴回的区域。 | 设计思路：局部修改与原图保留｜比较编辑和中性预测，提取变化区域后合成。 | [774417678](https://github.com/774417678/ComfyUI_KleinAttentionMask) | README的原理、参数、工作流及环境／限制段落，最近2次提交；未读JSON或代码 |
| [D07 HaDeS Anima Suite：作者拆解分层合并与兼容处理](https://civitai.com/articles/37645) | 2026-10-30T09:32:10.412000+08:00（文章发表） | LoRA组合·模型合并·兼容排错｜学习Anima层映射与工作流边界。 | 设计思路：分层风格组合｜作者讨论桥接层保留、风格合并与逐级精修。 | [_HaDeS_ / Devildonia](https://civitai.com/articles/37645) | 公开API文章正文全文；原仓库README已取得但本条未逐段学习，代码和示例JSON未核 |
| [D08 MOSS Layout prompts：文字、人物与海报布局教程](https://civitai.com/articles/37610) | 2026-10-29T21:38:32.360000+08:00（文章发表） | 文字版面·多主体·提示词组织｜用区域框安排文字、人物和漫画气泡。 | 设计思路：版面与信息层级｜为标题、人物名称、对话和画面主体分别留位置。 | [PixelPeep；编辑器仓库jambavant](https://civitai.com/articles/37610) | 公开API文章正文全文与字面JSON示例；未看图、未启动编辑器 |
| [D09 Krea 2 Workflows V2：增加Style Reference与RTX放大](https://civitai.com/models/2896885?modelVersionId=3439706) | 2026-10-31T02:30:00+08:00（V2发布） | 自动化工作流·风格参考·采样精修｜按基础、标准和高级需求选择Krea流程。 | 设计思路：风格参考与精修分工｜高级流程加入参考画风与后续放大环节。 | [Legendaer](https://civitai.com/models/2896885?modelVersionId=3439706) | 模型卡、V2版本说明、文件元数据；未下载工作流或看图 |
| [D10 Krea2超分新版工作流分享（视频简介已读）](https://www.bilibili.com/video/BV1Smxv67E72/) | 2026-10-30T17:00:00+08:00（视频投稿） | 采样精修·Krea2工作流｜关注放大过程的内容偏移控制。 | 设计思路：细节与内容保持｜作者介绍将4x放大模型接入采样过程的思路。 | [DragonBro的日常](https://www.bilibili.com/video/BV1Smxv67E72/) | B站搜索API的标题、UP主、pubdate与公开简介；详情接口HTTP412，未看视频／字幕 |
| [D11 MOSS Alpha LoRA：透明素材流程与社区试用反馈](https://note.com/kongo_jun/n/n439f8889b93a) | 2026-10-30T23:01:51+08:00（note发表） | 透明素材·RGBA工作流｜了解MOSS直接输出透明通道的用法与局限。 | 设计思路：素材分层合成｜分别生成带透明通道的角色、道具和效果素材。 | [混合順（试用教程）；paralaif（LoRA与原模型卡）](https://note.com/kongo_jun/n/n439f8889b93a) | note正文全文；HF模型卡全文与元数据；未看结果图、未读工作流JSON |
| [D12 AniKawaXL V5：Illustrious系赛璐璐人物模型](https://civitai.com/models/1282887?modelVersionId=3439917) | 2026-10-31T03:31:41.857000+08:00（V5发布） | 人物插画·特化模型｜面向赛璐璐人物绘制与采样器选择。 | 赛璐璐动画｜按作者描述，面向可爱人物；不同采样器呈现不同柔和程度。 | [Qnuk](https://civitai.com/models/1282887?modelVersionId=3439917) | 模型卡全文、V5精确版本元数据；未看例图 |
| [D13 Anything-V5 Style：旧版动漫观感的Anima LoRA](https://civitai.com/models/3028580?modelVersionId=3439977) | 2026-10-31T03:48:47.818000+08:00（版本发布） | 画风迁移·LoRA搭配｜尝试在Anima中迁移旧版动漫模型观感。 | 旧版动漫观感｜作者用SD1.5样图训练，目标是迁移整体风格感受。 | [fominhavi](https://civitai.com/models/3028580?modelVersionId=3439977) | 模型卡与精确版本元数据；原例图CDN返回403，未看图 |

## 当日分享

<a id="d01"></a>

### D01 Mossling：面向16GB显存的 MOSS 压缩实验

**适用方向：** 低显存研究·模型压缩｜了解剪枝、编码器替换及其画质取舍。

- 原作者与原文：recoilme / AiArtLab Team；[Mossling：面向16GB显存的 MOSS 压缩实验](https://huggingface.co/AiArtLab/mossling)；2026-10-30T22:20:54+08:00（仓库当前提交时间，非首发日）。
- 本次性质与精确版本：首次收录；近期资料补录；alpha，30-block DiT＋Qwen3.5-0.8B；revision 3467e0feea450b77122832f759f2e8acf3257bd1。
- 原作者分享要点（本库概述）：作者将42层DiT压至30层，以小型编码器和适配器替换原编码器，并公开压缩、训练和失败路线；明确列出训练未收敛、文字布局与复杂结构退化，适合学习模型压缩的取舍。
- 公开资料与适用条件：作者报告1024px、30步时峰值12.4GB；示例50步、CFG 3、seed 7，VAE保持fp32，diffusers 0.41.0.dev0。新层数下默认关闭原版unconditional skip。英文描述为训练范围；属于非官方Apache-2.0衍生。
- 实际读取范围：模型卡全文、提交列表；未看例图、未运行。
- 信息范围与本库备注：显存、速度及评估均为作者报告；该alpha并非成熟替代品。最新提交为src，不把仓库更新时间当作权重首发；配方基于当前卡。
- 相关原始资料：https://huggingface.co/AiArtLab/mossling/blob/3467e0feea450b77122832f759f2e8acf3257bd1/README.md

<a id="d02"></a>

### D02 MOSS-Image Reality LoRA Preview：日常手机人像

**适用方向：** 写实人像·风格LoRA｜用于MOSS-SFT的日常手机摄影表现。

**美术风格方向：** 手机摄影·柔和自然光｜按作者描述，保留轻微噪点、虚化和随手构图。

- 原作者与原文：Richarddzz；[MOSS-Image Reality LoRA Preview：日常手机人像](https://huggingface.co/Richarddzz/moss-image-reality-lora)；2026-10-31T02:34:00+08:00（仓库当前提交时间，非首发日）。
- 本次性质与精确版本：首次收录；近期版本；Preview step 73250；revision 821e95a1ca84f890768c1c0befd974100dfdbc1d。
- 原作者分享要点（本库概述）：作者强调日常手机照片的柔和质感而非影棚锐度，并说明亚洲人像优化、横向多格拼图和已知手部／文字问题；公开训练信息与示例参数。
- 公开资料与适用条件：必须配合OpenMOSS-Team/MOSS-Image-SFT；通用建议强度0.9–1.0、无触发词、较长中文自然语言。作者示例为50步、CFG 3、shift 5、负面词“畸形”，1088×1920或2176×960；例图来自72750–73000步，非本版73250的同图实值。键名前缀diffusion_model.；Diffusers可能需改transformer.。作者说明仅用于虚构成年人物，使用遵循模型卡条款。
- 实际读取范围：中英文模型卡全文及版本元数据；未看例图。
- 信息范围与本库备注：美术概括仅按作者文字；体型、五官和表情未作本库视觉观察。推荐参数与旧检查点例图参数分别保留，未验证加载兼容性或收益。
- 相关原始资料：https://huggingface.co/Richarddzz/moss-image-reality-lora/blob/821e95a1ca84f890768c1c0befd974100dfdbc1d/README.md

<a id="d03"></a>

### D03 MOSS-Image-IDM-LoRA：密集文字训练与2步蒸馏记录

**适用方向：** 文字生成·蒸馏经验｜比较文字数据微调与少步蒸馏的作用。

**设计思路：** 文字版面｜以菜单、海报和标牌等密集文字场景组织训练数据。

- 原作者与原文：akhaliq（模型卡署名）；[MOSS-Image-IDM-LoRA：密集文字训练与2步蒸馏记录](https://huggingface.co/akhaliq/MOSS-Image-IDM-LoRA)；2026-10-31T03:04:49+08:00（仓库当前提交时间，非首发日）。
- 本次性质与精确版本：首次收录；2026-10-30训练记录；v1 step-500；v2 OPD step-249；revision b2ee564eb98808daabef1ca67e620f85e3e5ad63。
- 原作者分享要点（本库概述）：作者发布一个有价值的有限／负结果：v1在50步基座上改进很小，叠加SFT并未解决8步文字乱码；v2改为直接训练2步学生，目前仅249次更新，作者称布局颜色已学到而文字仍弱。
- 公开资料与适用条件：基座MOSS-Image-SFT；v1为100张自生成密集文字图、rank64、500步；v2采用50步CFG3教师与2步CFG1学生。opd_8step目录名遗留，实际为2步，需精确区分。社区实现只复用IDM的数据思路，未实现论文DMD与moment-matching损失，非官方IDM权重。
- 实际读取范围：模型卡全文与公开版本元数据；未看评估拼图。
- 信息范围与本库备注：论文原始分数仅为作者转述，本库未核论文或复跑；本条重点是作者公开的实验边界与失败经验，不推荐为已经成熟的提速方案。
- 相关原始资料：https://huggingface.co/akhaliq/MOSS-Image-IDM-LoRA/blob/b2ee564eb98808daabef1ca67e620f85e3e5ad63/README.md

<a id="d04"></a>

### D04 Anima CharRef＋LLLite：人物参考、姿态与分区组合

**适用方向：** 人物参考·姿态控制·多主体｜组合参考身份、3D姿态与区域布局。

**设计思路：** 人物与布局分工｜参考图提供人物特征，姿态和区域图分别控制动作与位置。

- 原作者与原文：quinteroac；参考适配器来自ElectronGirl，控制模型来自toyxyz；[Anima CharRef＋LLLite：人物参考、姿态与分区组合](https://github.com/quinteroac/ComfyUI-Anima-CharRef-LLLite)；2026-10-31T03:46:16+08:00（提交）。
- 本次性质与精确版本：新工作流组合／近期更新；与旧HF-23适配器区分；cce21bbfb804aacaa1a374e4c6f0ea52bc3bddbe。
- 原作者分享要点（本库概述）：作者解释参考适配器引入额外参考帧后，普通LLLite补丁的token范围不匹配；实验节点只把控制施加于生成帧，并提供最简姿态、Pose Studio和区域绘制流程。新提交加入SnapRef与两种参考方法的切换。
- 公开资料与适用条件：示范使用Anima Turbo、8步、CFG1和Ref Adapter v2；区域示范使用anima_regional_4335、0→0.3。作者说明LLLite原训练基座为Anima Base，搭Turbo为实验用法；两人有正式支持，三人可能混合特征。SnapRef路径不使用Safe PAG。
- 实际读取范围：当前README的方法、节点、工作流与限制段落及最近3次提交；未看图／视频。
- 信息范围与本库备注：本库未核节点代码或运行。与10月30日HF-23为同一适配器生态，本条新增的是LLLite组合、SnapRef切换和工作流，不重复计为适配器模型新版本。贴吧CptCharnam的同版本推荐仅作来源补充。
- 相关原始资料：https://github.com/quinteroac/ComfyUI-Anima-CharRef-LLLite/commit/cce21bbfb804aacaa1a374e4c6f0ea52bc3bddbe
- 相关原始资料：https://huggingface.co/ElectronGirl/anima-ref-adapter
- 相关原始资料：https://tieba.baidu.com/p/11151464424
- 相关原始资料：../2026-10-30/notes/history/huggingface.md#hf-23

<a id="d05"></a>

### D05 MOSS QwenVL Layout：参考图转布局与自动提示

**适用方向：** 自动提示·构图控制·多主体｜从参考图或文字生成MOSS区域提示。

**设计思路：** 布局与风格分开组织｜将对象、文字与遮挡关系放入区域，另设整体风格。

- 原作者与原文：leroy989；[MOSS QwenVL Layout：参考图转布局与自动提示](https://github.com/leroy989/ComfyUI-MOSS-QwenVL-Layout)；2026-10-31T02:57:47+08:00（提交）。
- 本次性质与精确版本：首次收录；近期更新；c7982bf428a94967a237ff78de2426d6748bebe6。
- 原作者分享要点（本库概述）：作者用Qwen VL识别参考图对象及文字，转换MOSS中心原点yxyx坐标；还提供无图自动规划、修改请求、深度顺序和独立的Krea/MOSS Prompt Builder。适合学习视觉理解、布局JSON与风格锁如何分工。
- 公开资料与适用条件：图片缩放后尺寸须与布局输出一致，MOSS尺寸按16对齐；hf_model路径需要transformers>=4.57，可关keep_loaded释放显存；CLIP路径需要近期ComfyUI且作者测试较少。From prompt为实验模式；文字需在targets中明确要求。
- 实际读取范围：README主要方法、输入输出、坐标与Prompt Builder段落，最近3次提交；未看例图或工作流JSON。
- 信息范围与本库备注：自动框、遮挡推断及长JSON可靠性均为作者说明。检查preview、raw_qwen_output等是作者使用建议，本库未验证自动生成布局的效果。
- 相关原始资料：https://github.com/leroy989/ComfyUI-MOSS-QwenVL-Layout/commit/c7982bf428a94967a237ff78de2426d6748bebe6

<a id="d06"></a>

### D06 KleinAttentionMask：从编辑预测差分估计掩码

**适用方向：** 局部编辑·自动掩码｜由Klein9B编辑指令估计需要贴回的区域。

**设计思路：** 局部修改与原图保留｜比较编辑和中性预测，提取变化区域后合成。

- 原作者与原文：774417678；[KleinAttentionMask：从编辑预测差分估计掩码](https://github.com/774417678/ComfyUI_KleinAttentionMask)；2026-10-31T04:00:40+08:00（提交）。
- 本次性质与精确版本：首次收录；近期节点方法；3b0936a63d73281461f76eec687f444d08f3d3ad。
- 原作者分享要点（本库概述）：作者在同latent、同噪声状态下比较编辑指令与保持原图的预测，输出影响热图和掩码；区分同状态中性配对、源latent和相邻预测等模式，公开额外计算开销与不适用条件。
- 公开资料与适用条件：仅面向ComfyUI原生FLUX.2 Klein 9B。作者推荐sparse_neutral、capture_start=0、capture_end=1、probe_steps=2、threshold=0.20；配套某工作流用probe_steps=1，不能混写成同一配置。中性模式要接CLIP，ControlNet中性重放未支持；调用序号不等于调度步号。
- 实际读取范围：README的原理、参数、工作流及环境／限制段落，最近2次提交；未读JSON或代码。
- 信息范围与本库备注：掩码在采样结束后输出，用于贴回，不约束刚才的采样。作者列的环境测试属作者记录；本库未复跑，也未核被引用论文或分割精度。
- 相关原始资料：https://github.com/774417678/ComfyUI_KleinAttentionMask/commit/3b0936a63d73281461f76eec687f444d08f3d3ad

<a id="d07"></a>

### D07 HaDeS Anima Suite：作者拆解分层合并与兼容处理

**适用方向：** LoRA组合·模型合并·兼容排错｜学习Anima层映射与工作流边界。

**设计思路：** 分层风格组合｜作者讨论桥接层保留、风格合并与逐级精修。

- 原作者与原文：_HaDeS_ / Devildonia；[HaDeS Anima Suite：作者拆解分层合并与兼容处理](https://civitai.com/articles/37645)；2026-10-30T09:32:10.412000+08:00（文章发表）。
- 本次性质与精确版本：新增文章；首次收录；文章37645；文中18节点套件，未给出与文章一一对应的代码tag。
- 原作者分享要点（本库概述）：作者介绍按Anima层数识别和映射的合并方法、Diffusers键名重映射、LoRA合并、负提示引导与渐进式精修，并提供四类示例流程。值得看其分工和作者提出的边界。
- 公开资料与适用条件：作者的合并节点默认锁定llm_adapter贡献，并讨论28／40／52层变体；该默认属于本套件设计，不提升为所有Anima训练／合并规则。文中部分速度、检测与效果表述未独立验证；示例工作流在原仓库examples/。
- 实际读取范围：公开API文章正文全文；原仓库README已取得但本条未逐段学习，代码和示例JSON未核。
- 信息范围与本库备注：文章中的“通用”“最优”“不改变”等主张均属作者说明，本库未验证全部LoRA格式兼容性或数值实现。与旧GH-12／GH-13层映射主题有关，是不同作者的套件介绍。
- 相关原始资料：https://github.com/Devildonia/HaDeS-Anima-Suite
- 相关原始资料：../2026-10-30/notes/history/github.md#gh-12

<a id="d08"></a>

### D08 MOSS Layout prompts：文字、人物与海报布局教程

**适用方向：** 文字版面·多主体·提示词组织｜用区域框安排文字、人物和漫画气泡。

**设计思路：** 版面与信息层级｜为标题、人物名称、对话和画面主体分别留位置。

- 原作者与原文：PixelPeep；编辑器仓库jambavant；[MOSS Layout prompts：文字、人物与海报布局教程](https://civitai.com/articles/37610)；2026-10-29T21:38:32.360000+08:00（文章发表）。
- 本次性质与精确版本：历史补录；上轮尚未收录的10月29日文章；文章37610；教程示例画布1216×832。
- 原作者分享要点（本库概述）：作者从海报、三格漫画、杂志封面三个用途讲解MOSS布局JSON；用独立文本框、角色归属描述与气泡尾部方向组织内容，并提供可视化编辑器。适用多种画风。
- 公开资料与适用条件：坐标为中心原点、绝对像素、yxyx；生成尺寸须与编辑器一致，示例均1216×832。建议短句、给文字留空间，保持seed后微调框；使用布局模板时关闭会改写JSON的prompt enhancer。原文称布局仍实验性，复杂区域越多越不稳定。
- 实际读取范围：公开API文章正文全文与字面JSON示例；未看图、未启动编辑器。
- 信息范围与本库备注：本库概括的是布局与提示组织方法，未据示范提示词推断实际成图画风。编辑器和完整示例请回原文，未复制整篇或完整配置入库。
- 相关原始资料：https://github.com/jambavant/SwarmUI-LayoutEditor
- 相关原始资料：https://jambavant.github.io/SwarmUI-LayoutEditor/standalone/index.html

<a id="d09"></a>

### D09 Krea 2 Workflows V2：增加Style Reference与RTX放大

**适用方向：** 自动化工作流·风格参考·采样精修｜按基础、标准和高级需求选择Krea流程。

**设计思路：** 风格参考与精修分工｜高级流程加入参考画风与后续放大环节。

- 原作者与原文：Legendaer；[Krea 2 Workflows V2：增加Style Reference与RTX放大](https://civitai.com/models/2896885?modelVersionId=3439706)；2026-10-31T02:30:00+08:00（V2发布）。
- 本次性质与精确版本：版本更新；首次收录本资源；V2 / 3439706；作者使用ComfyUI v0.43.0。
- 原作者分享要点（本库概述）：V2说明基础与标准流程替换部分Impact节点，高级流程新增Style Reference和RTX Upscale；标准流程保留元数据和LoRA Manager，适合比较不同复杂度的流程组织。
- 公开资料与适用条件：原文列rgthree、Image-Saver、KJNodes、Lora-Manager、Easy-Use与Nvidia RTX Nodes等依赖；高级RTX分支需适用的硬件与组件，本库未推定跨硬件兼容。采样实值以公开工作流为准，本次未取得。
- 实际读取范围：模型卡、V2版本说明、文件元数据；未下载工作流或看图。
- 信息范围与本库备注：仅元数据说明已公开附件，不等于本库已读取配置。V1→V2变化按作者说明保存，未把列表热度作为质量证据。

<a id="d10"></a>

### D10 Krea2超分新版工作流分享（视频简介已读）

**适用方向：** 采样精修·Krea2工作流｜关注放大过程的内容偏移控制。

**设计思路：** 细节与内容保持｜作者介绍将4x放大模型接入采样过程的思路。

- 原作者与原文：DragonBro的日常；[Krea2超分新版工作流分享（视频简介已读）](https://www.bilibili.com/video/BV1Smxv67E72/)；2026-10-30T17:00:00+08:00（视频投稿）。
- 本次性质与精确版本：新增视频；按简介收录；BV1Smxv67E72；简介未给出工作流版本号。
- 原作者分享要点（本库概述）：简介介绍以4x放大模型直接注入K采样器的Krea2超分方法，并讨论Qwen反推走CPU而非GPU的问题。适合作为后续观看与学习入口。
- 公开资料与适用条件：搜索接口取得作者当前简介与投稿日期；具体4x模型、节点连线、采样值和修复操作未公开在所读简介中，保持未知。
- 实际读取范围：B站搜索API的标题、UP主、pubdate与公开简介；详情接口HTTP412，未看视频／字幕。
- 信息范围与本库备注：减少内容偏移且保持质量是作者简介中的主张，本库未看到对比或完整教程步骤。原文标题中的模型分享和参数细节需回视频查看。
- 相关原始资料：https://www.bilibili.com/video/BV12v7z6YEFr/

<a id="d11"></a>

### D11 MOSS Alpha LoRA：透明素材流程与社区试用反馈

**适用方向：** 透明素材·RGBA工作流｜了解MOSS直接输出透明通道的用法与局限。

**设计思路：** 素材分层合成｜分别生成带透明通道的角色、道具和效果素材。

- 原作者与原文：混合順（试用教程）；paralaif（LoRA与原模型卡）；[MOSS Alpha LoRA：透明素材流程与社区试用反馈](https://note.com/kongo_jun/n/n439f8889b93a)；2026-10-30T23:01:51+08:00（note发表）。
- 本次性质与精确版本：新增实践分享；合并追溯原LoRA资料；moss_alpha_v1 / 发布step1000；HF revision fbe437d58410739807395389243a38674f00076f。
- 原作者分享要点（本库概述）：原作者以39张RGBA数据训练概念验证LoRA，配合RGBA VAE输出透明PNG；社区教程给出ComfyUI接线资源，并反馈画面有一定退化。两种来源的介绍与试用评价分别保留。
- 公开资料与适用条件：原模型需MOSS-Image-SFT、moss_alpha_v1与trmz/flux2-klein-alpha RGBA VAE及自定义加载／保存节点。提示结尾为“isolated on a transparent background”；作者建议强度1.0，8步DMD时CFG1、er_sde/simple；不带DMD示例28步CFG4。作者记录过拟合、边缘光晕、暗衣半透明和构图偏中。LoRA许可为非商业研究与评估用途。
- 实际读取范围：note正文全文；HF模型卡全文与元数据；未看结果图、未读工作流JSON。
- 信息范围与本库备注：note作者报告RTX4090环境下12秒／约16GB和主观退化，非本库测试，也不推广为所有显卡表现。RGBA跨模型VAE适配依作者方案，本库未验证加载或透明边缘。
- 相关原始资料：https://huggingface.co/paralaif/MOSS-Image-Alpha-LoRA
- 相关原始资料：https://huggingface.co/paralaif/MOSS-Image-Alpha-LoRA/blob/fbe437d58410739807395389243a38674f00076f/README.md

<a id="d12"></a>

### D12 AniKawaXL V5：Illustrious系赛璐璐人物模型

**适用方向：** 人物插画·特化模型｜面向赛璐璐人物绘制与采样器选择。

**美术风格方向：** 赛璐璐动画｜按作者描述，面向可爱人物；不同采样器呈现不同柔和程度。

- 原作者与原文：Qnuk；[AniKawaXL V5：Illustrious系赛璐璐人物模型](https://civitai.com/models/1282887?modelVersionId=3439917)；2026-10-31T03:31:41.857000+08:00（V5发布）。
- 本次性质与精确版本：版本更新；首次收录该作者与模型；V5 / 3439917；Illustrious。
- 原作者分享要点（本库概述）：作者明确定位为赛璐璐动画风的可爱人物模型；V5调整画质与饱和度，模型卡还区分DPM++2M、Euler a与Euler Smea的绘制倾向。
- 公开资料与适用条件：作者通用建议25–30步；DPM++2M为标准，Euler a更柔和，Euler Smea进一步柔和且背景简化。未取得该版本同图CFG、seed、VAE或完整提示词。
- 实际读取范围：模型卡全文、V5精确版本元数据；未看例图。
- 信息范围与本库备注：风格方向及采样器差异均按作者文字，未归纳人物体型、五官或表情的稳定特征；未验证兼容性或优于旧版。

<a id="d13"></a>

### D13 Anything-V5 Style：旧版动漫观感的Anima LoRA

**适用方向：** 画风迁移·LoRA搭配｜尝试在Anima中迁移旧版动漫模型观感。

**美术风格方向：** 旧版动漫观感｜作者用SD1.5样图训练，目标是迁移整体风格感受。

- 原作者与原文：fominhavi；[Anything-V5 Style：旧版动漫观感的Anima LoRA](https://civitai.com/models/3028580?modelVersionId=3439977)；2026-10-31T03:48:47.818000+08:00（版本发布）。
- 本次性质与精确版本：新增风格LoRA；首次收录；v1.0-anima / 3439977。
- 原作者分享要点（本库概述）：作者说明以SD1.5图片训练Anything-V5方向的Anima LoRA，强调并非精确复刻，并主动提示训练来源可能带来手部和结构缺陷。
- 公开资料与适用条件：基座Anima，触发词@any-v5；建议权重及同图完整参数未取得。使用遵循原模型页的具体条件；本库仅摘要和回链。
- 实际读取范围：模型卡与精确版本元数据；原例图CDN返回403，未看图。
- 信息范围与本库备注：本条只按作者定位描述风格迁移目标，不凭模型名补写线条、五官、体型或色彩特征。训练来源与局限不代表本库实际观察结果。

## 实际平台覆盖

| 平台 | 实际入口、范围与状态 |
|---|---|
| stablediffusion 吧 | aiotieba CREATE最新列表1页30条（含置顶），正文选读3帖；全站最新搜索2组并核对吧名。列表跨过上次补查时间。人物参考帖只补充旧HF-23来源；自然语言帖无公开完整提示，未单列推荐；10月29日提速帖主要为个人硬件与软件叠加报告，未作为新方法推荐。 |
| comfyui 吧 | aiotieba CREATE最新列表1页29条（含置顶），覆盖到旧日期；选读10月30日SD-PPP2帖首楼，主要为网盘推广，未收录为教程。两个吧规范入口分别为https://tieba.baidu.com/f?kw=stablediffusion 和 https://tieba.baidu.com/f?kw=comfyui；列表返回对应吧名；未测试带空格别名的浏览器重定向。 |
| bilibili | 两组按pubdate排序的公开搜索（ComfyUI教程／生图模型），各20条，选读Krea2等5条当前简介；推荐1条方法信息较明确的视频。三条单视频详情API均HTTP412；未看字幕、视频、评论或图。 |
| Reddit | www.reddit.com的StableDiffusion与comfyui最新列表均403；old.reddit.com虽200但返回登录页HTML，无帖子JSON。未取得可核实的新原帖内容，本轮受限；未据此判断无更新。 |
| Hugging Face | 按lastModified取得40个text-to-image模型候选，选读模型卡与版本元数据；Mossling、Reality、IDM三份卡与固定revision文本一致。Alpha LoRA由note线索追溯；其当前卡与元数据已读，未单独锁定历史正文。仅当前提交时间，不用createdAt宣称首发。 |
| GitHub | 两组仓库搜索：近期更新的ComfyUI工作流15项、10月新建提示词项目10项；读取3个选定仓库README及近期提交。提交SHA作为版本锚点，README读取当时默认分支；未逐文件核对代码、工作流或运行。 |
| Civitai 社区／论坛 | 公开API按Newest读取25篇文章列表、30个资源／版本列表；深入读取HaDeS文章、Layout教程、3个模型／工作流的原卡和指定版本。作品示范仅取得元数据，1张原图CDN403，未实际看图；未读取文章评论或模型讨论全文。 |
| 其他论坛／作者资料 | note.com搜索API403；ComfyUI标签RSS可读，检查最近8条线索，选读2篇公开note正文，收录MOSS透明素材实践1篇。16GB四倍放大文主要为视频开发，本轮不扩展为图片通用结论。 |
| 通用搜索补充 | Acumen已取得近期线索，但日期较早、部分离题，仅辅助确定来源；网页搜索工具两次返回空错误，无搜索摘要作为条目证据。实际结论来自上述平台原始公开接口。 |

## 已读但不另计新增的来源补充

- [CptCharnam：anima出了个新的质量不错人物参考lora](https://tieba.baidu.com/p/11151464424)，2026-10-30 18:12北京时间。首楼推荐ElectronGirl/anima-ref-adapter v2，无公开示范图或新配置；回链[上轮HF-23](../2026-10-30/notes/history/huggingface.md#hf-23)，不重复报道为模型新版本。
- [核氰合锂：Anima自然语言前后关系使用感受](https://tieba.baidu.com/p/11151854085)，2026-10-30 21:32北京时间。首楼提出长提示可能削弱角色特征的个人感受，未提供完整提示或对照，本次仅保留讨论线索。

## 后续关注

- 模型与方法的速度、显存及效果数字保留作者条件；本库本次仅读取。后续若有实质版本变化，再增量报道并回链。
- 已读资料随批次保存；受限平台和未取得的图像、附件、字幕分别记录，不阻塞已完成内容。

[返回总索引](../../每日检索可速查总结.md)
