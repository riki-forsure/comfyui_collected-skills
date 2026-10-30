# 2026-10-31 每日社区发现

本页汇总社区作者公开分享的模型、工作流、提示词和实践经验。感谢原作者投入；以下为本库概述，欢迎通过原文入口阅读完整内容、使用说明和后续更新。

- 北京日期与实际检索时间：2026-10-31；2026-10-31 03:59 起，截至 2026-10-31 04:02:57 +08:00。
- 检索类型：无具体差距要求的每日广泛发现；无主动专题。
- 执行状态：进行中，已完成部分直接归档。
- 优先时间窗：自上轮 2026-10-30 02:26 后的新增与实质变化；贴吧上轮补查至14:40。首次收录的较早资料单独标明；当前仓库提交时间不作模型首发时间。
- 本次已保存 3 项分享／更新；未安装节点、下载权重、运行生图或验证收益。

## 今日值得阅读

- [Mossling：面向16GB显存的 MOSS 压缩实验](https://huggingface.co/AiArtLab/mossling)：作者将42层DiT压至30层，以小型编码器和适配器替换原编码器，并公开压缩、训练和失败路线；明确列出训练未收敛、文字布局与复杂结构退化，适合学习模型压缩的取舍。
- [MOSS-Image Reality LoRA Preview：日常手机人像](https://huggingface.co/Richarddzz/moss-image-reality-lora)：作者强调日常手机照片的柔和质感而非影棚锐度，并说明亚洲人像优化、横向多格拼图和已知手部／文字问题；公开训练信息与示例参数。
- [MOSS-Image-IDM-LoRA：密集文字训练与2步蒸馏记录](https://huggingface.co/akhaliq/MOSS-Image-IDM-LoRA)：作者发布一个有价值的有限／负结果：v1在50步基座上改进很小，叠加SFT并未解决8步文字乱码；v2改为直接训练2步学生，目前仅249次更新，作者称布局颜色已学到而文字仍弱。

## 分享速查

| 编号／分享与版本 | 原始日期／口径 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 读取状态 |
|---|---|---|---|---|---|
| [D01 Mossling：面向16GB显存的 MOSS 压缩实验](https://huggingface.co/AiArtLab/mossling) | 2026-10-30T14:20:54.000Z（仓库当前提交时间，非首发日） | 低显存研究·模型压缩｜了解剪枝、编码器替换及其画质取舍。 | — | [recoilme / AiArtLab Team](https://huggingface.co/AiArtLab/mossling) | 模型卡全文、提交列表；未看例图、未运行 |
| [D02 MOSS-Image Reality LoRA Preview：日常手机人像](https://huggingface.co/Richarddzz/moss-image-reality-lora) | 2026-10-30T18:34:00.000Z（仓库当前提交时间，非首发日） | 写实人像·风格LoRA｜用于MOSS-SFT的日常手机摄影表现。 | 手机摄影·柔和自然光｜按作者描述，保留轻微噪点、虚化和随手构图。 | [Richarddzz](https://huggingface.co/Richarddzz/moss-image-reality-lora) | 中英文模型卡全文及版本元数据；未看例图 |
| [D03 MOSS-Image-IDM-LoRA：密集文字训练与2步蒸馏记录](https://huggingface.co/akhaliq/MOSS-Image-IDM-LoRA) | 2026-10-30T19:04:49.000Z（仓库当前提交时间，非首发日） | 文字生成·蒸馏经验｜比较文字数据微调与少步蒸馏的作用。 | 设计思路：文字版面｜以菜单、海报和标牌等密集文字场景组织训练数据。 | [akhaliq（模型卡署名）](https://huggingface.co/akhaliq/MOSS-Image-IDM-LoRA) | 模型卡全文与公开版本元数据；未看评估拼图 |

## 当日分享

### D01 Mossling：面向16GB显存的 MOSS 压缩实验

**适用方向：** 低显存研究·模型压缩｜了解剪枝、编码器替换及其画质取舍。

- 原作者与原文：recoilme / AiArtLab Team；[Mossling：面向16GB显存的 MOSS 压缩实验](https://huggingface.co/AiArtLab/mossling)；2026-10-30T14:20:54.000Z（仓库当前提交时间，非首发日）。
- 本次性质与精确版本：首次收录；近期资料补录；alpha，30-block DiT＋Qwen3.5-0.8B；revision 3467e0feea450b77122832f759f2e8acf3257bd1。
- 原作者分享要点（本库概述）：作者将42层DiT压至30层，以小型编码器和适配器替换原编码器，并公开压缩、训练和失败路线；明确列出训练未收敛、文字布局与复杂结构退化，适合学习模型压缩的取舍。
- 公开资料与适用条件：作者报告1024px、30步时峰值12.4GB；示例50步、CFG 3、seed 7，VAE保持fp32，diffusers 0.41.0.dev0。新层数下默认关闭原版unconditional skip。英文描述为训练范围；属于非官方Apache-2.0衍生。
- 实际读取范围：模型卡全文、提交列表；未看例图、未运行。
- 信息范围与本库备注：显存、速度及评估均为作者报告；该alpha并非成熟替代品。最新提交为src，不把仓库更新时间当作权重首发；配方基于当前卡。
- 相关原始资料：https://huggingface.co/AiArtLab/mossling/blob/3467e0feea450b77122832f759f2e8acf3257bd1/README.md

### D02 MOSS-Image Reality LoRA Preview：日常手机人像

**适用方向：** 写实人像·风格LoRA｜用于MOSS-SFT的日常手机摄影表现。

**美术风格方向：** 手机摄影·柔和自然光｜按作者描述，保留轻微噪点、虚化和随手构图。

- 原作者与原文：Richarddzz；[MOSS-Image Reality LoRA Preview：日常手机人像](https://huggingface.co/Richarddzz/moss-image-reality-lora)；2026-10-30T18:34:00.000Z（仓库当前提交时间，非首发日）。
- 本次性质与精确版本：首次收录；近期版本；Preview step 73250；revision 821e95a1ca84f890768c1c0befd974100dfdbc1d。
- 原作者分享要点（本库概述）：作者强调日常手机照片的柔和质感而非影棚锐度，并说明亚洲人像优化、横向多格拼图和已知手部／文字问题；公开训练信息与示例参数。
- 公开资料与适用条件：必须配合OpenMOSS-Team/MOSS-Image-SFT；通用建议强度0.9–1.0、无触发词、较长中文自然语言。作者示例为50步、CFG 3、shift 5、负面词“畸形”，1088×1920或2176×960；例图来自72750–73000步，非本版73250的同图实值。键名前缀diffusion_model.；Diffusers可能需改transformer.。作者说明仅用于虚构成年人物，使用遵循模型卡条款。
- 实际读取范围：中英文模型卡全文及版本元数据；未看例图。
- 信息范围与本库备注：美术概括仅按作者文字；体型、五官和表情未作本库视觉观察。推荐参数与旧检查点例图参数分别保留，未验证加载兼容性或收益。
- 相关原始资料：https://huggingface.co/Richarddzz/moss-image-reality-lora/blob/821e95a1ca84f890768c1c0befd974100dfdbc1d/README.md

### D03 MOSS-Image-IDM-LoRA：密集文字训练与2步蒸馏记录

**适用方向：** 文字生成·蒸馏经验｜比较文字数据微调与少步蒸馏的作用。

**设计思路：** 文字版面｜以菜单、海报和标牌等密集文字场景组织训练数据。

- 原作者与原文：akhaliq（模型卡署名）；[MOSS-Image-IDM-LoRA：密集文字训练与2步蒸馏记录](https://huggingface.co/akhaliq/MOSS-Image-IDM-LoRA)；2026-10-30T19:04:49.000Z（仓库当前提交时间，非首发日）。
- 本次性质与精确版本：首次收录；2026-10-30训练记录；v1 step-500；v2 OPD step-249；revision b2ee564eb98808daabef1ca67e620f85e3e5ad63。
- 原作者分享要点（本库概述）：作者发布一个有价值的有限／负结果：v1在50步基座上改进很小，叠加SFT并未解决8步文字乱码；v2改为直接训练2步学生，目前仅249次更新，作者称布局颜色已学到而文字仍弱。
- 公开资料与适用条件：基座MOSS-Image-SFT；v1为100张自生成密集文字图、rank64、500步；v2采用50步CFG3教师与2步CFG1学生。opd_8step目录名遗留，实际为2步，需精确区分。社区实现只复用IDM的数据思路，未实现论文DMD与moment-matching损失，非官方IDM权重。
- 实际读取范围：模型卡全文与公开版本元数据；未看评估拼图。
- 信息范围与本库备注：论文原始分数仅为作者转述，本库未核论文或复跑；本条重点是作者公开的实验边界与失败经验，不推荐为已经成熟的提速方案。
- 相关原始资料：https://huggingface.co/akhaliq/MOSS-Image-IDM-LoRA/blob/b2ee564eb98808daabef1ca67e620f85e3e5ad63/README.md

## 实际平台覆盖

| 平台 | 实际入口、范围与状态 |
|---|---|
| 各固定来源 | 已开始逐项检索；完整覆盖结论待本轮结束时更新。 |

## 后续关注

- 模型与方法的速度、显存及效果数字保留作者条件；本库本次仅读取。后续若有实质版本变化，再增量报道并回链。
- 已读资料随批次保存；受限平台和未取得的图像、附件、字幕分别记录，不阻塞已完成内容。

[返回总索引](../../每日检索可速查总结.md)
