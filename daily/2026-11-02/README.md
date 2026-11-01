# 2026-11-02 每日社区发现

感谢社区作者公开分享。本页以本库概述保存分享要点、原作者和原文入口，欢迎回原文阅读完整教程、示范和后续更新。

- 北京日期／开始时间：2026-11-02 04:02（工具UTC时钟换算）。
- 检索类型：每日广泛发现；无具体差距要求，无主动专题。
- 优先时间窗：自2026-11-01晨间成功检索快照后的新增与实质更新。上轮午间是已读资料补存，未当作检索窗口结束。
- 执行状态：进行中；完成的资料先保存，其他来源继续整理。
- 已归档 3 项分享／实质更新；未安装节点、下载权重、启动生图或自动实验。

## 今日值得阅读

- [Anima：按时间步区间查看LoRA训练损失](https://civitai.com/articles/37807)：作者解释总loss会混合不同样本和时间步，按低、中、高噪声分别记录后，能发现总loss下降时细节区间仍波动的情况。文中强调训练步数与扩散时间步不同，分区作用也有重叠。
- [XeroDesign-1.0：Z-Image图形海报LoRA](https://huggingface.co/xerofounder/XeroDesign-1.0)：作者以696张整理海报训练Z-Image专用LoRA，给出基座revision、目标模块、触发词与Diffusers示例。适合查阅从图形设计素材到海报特化适配器的训练与使用入口。
- [Hammershoi FLUX 3 Klein LoRA：静谧室内绘画](https://huggingface.co/jejunepixels/Hammershoi-Flux3-LoRA)：作者用288幅裁切画作训练，并公开六提示／一个种子的有限测试、训练设置与使用限制。本库实际看了一张临窗女性示范：米灰色调、柔光与颗粒笔触，人物窄肩、盘发、长裙轮廓显得修长，侧背而立；阴影中的五官不作细分。

## 分享速查

| 编号／分享 | 日期／口径 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 读取状态 |
|---|---|---|---|---|---|
| [R01 Anima：按时间步区间查看LoRA训练损失](https://civitai.com/articles/37807) | 2026-11-02 00:27:38.411 +08:00（文章发表） | LoRA训练·检查点选择｜分别观察不同噪声区间的损失变化。 | — | [ame_la / amenorira](https://civitai.com/articles/37807) | 公开API中英文文章正文全文；未看曲线图、未读训练器实现 |
| [R02 XeroDesign-1.0：Z-Image图形海报LoRA](https://huggingface.co/xerofounder/XeroDesign-1.0) | 2026-11-02 03:47:50 +08:00（当前仓库提交，非首发日） | 海报设计·后训练LoRA｜面向网格排版、几何构成与字体布局。 | 瑞士平面·包豪斯几何｜按作者描述，强调非对称网格、字体与高对比构图。 | [xerofounder；数据来源xerocore/argonz-curated-design](https://huggingface.co/xerofounder/XeroDesign-1.0) | 模型卡全文及版本元数据；未看示范图、未读训练文件或推理服务代码 |
| [R03 Hammershoi FLUX 3 Klein LoRA：静谧室内绘画](https://huggingface.co/jejunepixels/Hammershoi-Flux3-LoRA) | 2026-11-02 00:23:26 +08:00（当前仓库提交，非首发日） | 室内插画·风格LoRA｜参考低饱和室内、孤立人物与窗光表现。 | 低饱和绘画·柔和窗光｜本例以长裙纵向轮廓、侧背姿态与留白营造静谧。 | [jejunepixels；借鉴Vilhelm Hammershøi画作，素材来源见原卡与数据集](https://huggingface.co/jejunepixels/Hammershoi-Flux3-LoRA) | 模型卡全文与版本元数据；实际查看hammershoi_woman_full_s42.jpg一张原生示范 |

## 当日分享

<a id="r01"></a>

### R01 Anima：按时间步区间查看LoRA训练损失

**适用方向：** LoRA训练·检查点选择｜分别观察不同噪声区间的损失变化。

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

- 原作者与原文：jejunepixels；借鉴Vilhelm Hammershøi画作，素材来源见原卡与数据集；[原文](https://huggingface.co/jejunepixels/Hammershoi-Flux3-LoRA)。
- 日期与精确版本：2026-11-02 00:23:26 +08:00（当前仓库提交，非首发日）；revision 22b7b8f5fddd6b49f0b6399bfc12960c44a6c8bb；FLUX3 Image Klein Base。
- 本次类型：首次收录；按已读来源归档。
- 原作者分享要点（本库概述）：作者用288幅裁切画作训练，并公开六提示／一个种子的有限测试、训练设置与使用限制。本库实际看了一张临窗女性示范：米灰色调、柔光与颗粒笔触，人物窄肩、盘发、长裙轮廓显得修长，侧背而立；阴影中的五官不作细分。
- 公开资料与条件：作者建议30步、guidance3.5、LoRA1.0、1024²，提示结尾hmrsh style；示范seed42、关闭prompt upsampler。更高权重可能增颗粒并改变人物衣着。作者未测试蒸馏版Klein、prompt upsampler或ComfyUI。FLUX Kommunity许可，需核基座访问条件。
- 实际读取范围：模型卡全文与版本元数据；实际查看hammershoi_woman_full_s42.jpg一张原生示范。
- 信息范围与本库备注：视觉观察只限本例，不概括整个模型的人体比例或表情倾向。原作者描述与本库看图区分；未复跑，单图、单seed测试不证明跨主体稳定。实际看图不等于本库生成或收益验证。
- 相关原始资料：https://huggingface.co/jejunepixels/Hammershoi-Flux3-LoRA/blob/22b7b8f5fddd6b49f0b6399bfc12960c44a6c8bb/README.md
- 相关原始资料：https://huggingface.co/jejunepixels/Hammershoi-Flux3-LoRA/blob/22b7b8f5fddd6b49f0b6399bfc12960c44a6c8bb/images/hammershoi_woman_full_s42.jpg

## 实际平台覆盖

| 平台 | 入口、范围与结果 |
|---|---|
| 固定来源 | 两吧、bilibili、Reddit、HF、GitHub、Civitai均已实际发起查询；完整范围随本轮归档更新。 |

[返回总索引](../../每日检索可速查总结.md)
