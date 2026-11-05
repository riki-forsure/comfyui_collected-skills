# 2026-11-06 每日社区发现

本页汇总社区作者的公开分享，感谢原作者的投入。本库以中文概述与原文入口帮助查阅，欢迎前往原帖阅读完整教程、后续更新并支持作者；署名和链接不等同于转载授权。

- 北京日期：2026-11-06；本轮从03:58开始检索。
- 检索类型：无具体差距要求的每日广泛发现。
- 执行状态：进行中：首批3项已读发现先行归档；其余来源正在整理。
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

## 当日分享

<a id="n01"></a>

### N01 HaDeS MOSS Turbo：分开选择文字布局、多样性与八步版本

**适用方向：少步生成·MOSS选型｜区分四步文字布局、多样性与八步使用条件。**

- 原作者与原文：[DeVilDoNia／Devildonia；基座OpenMOSS团队](https://huggingface.co/DeVilDoNia/HaDeS-MOSS-Turbo)。
- 原文与版本：模型卡快照 revision `241bb1fbaba2be9e5fcb4ba1e9bbf1375e354487`，仓库更新2026-11-06 03:49:02 +08:00；更新时间不作为首次发布证明。当前首次收录。
- 作者分享要点：针对MOSS-Image SFT训练少步适配器，rank2，仅24–41层，每文件约3.4MB。`HaDeS-MOSS-Turbo-v0.6.safetensors`侧重文字／布局，`HaDeS-MOSS-Turbo-Diverse-v0.6.safetensors`侧重开放提示的变化，`HaDeS-MOSS-Turbo-8steps-v0.7.safetensors`为八步版本；不是同一文件改名。
- 作者实测配置：`moss_image_sft_bf16`，CFG1、Euler/simple、shift5.0、LoRA1.0；前两文件4步，v0.7为8步。可用原生LoraLoaderModelOnly＋KSampler，HaDeS节点为可选路径，不要求另装。
- 取舍：作者在1024及以上发现四步版颜色偏淡；前两文件加至八步只测了色彩，不能套用四步文字测试结果。v0.7的1024成对审图仅每提示一个seed；2048的五例均偏好对照lodestones版本，作者把v0.7定位于不超过1024。上述为作者测量与审图，本库未复核。
- 训练说明：DMD加回归项，冻结SFT，从零训练生成LoRA；作者借鉴akhaliq配方但声明未使用其LoRA权重。其他基座、强度、编辑／低去噪质量未测；int8微调模型和img2img运行检查不证明质量兼容。许可标Apache2.0，回原页核对LICENSE／NOTICE。
- 读取范围：模型卡全文；未看示范图、结果附录、实现或权重。

<a id="n02"></a>

### N02 NitroFusion2：一至两步模型与首步去蒸馏LoRA

**适用方向：少步生成·Z-Image｜查阅一至两步模型及首步LoRA的不同职责。**

- 原作者与原文：[Dar-Yen Chen、Yi-Zhe Song／ChenDY](https://huggingface.co/ChenDY/NitroFusion2)。
- 原文与版本：revision `9845835ab4622031406d667b96d9bcd1140b6083`，仓库更新2026-11-05 16:01:49 +08:00；卡片News明示11月3日发布，属于近期首次补录，非今日首发。
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

## 来源覆盖

已读取Hugging Face模型卡与Civitai文章。贴吧、bilibili只读工具和其他来源结果已取得，尚在筛选；Reddit两个最新列表本轮均返回403。完整分页、筛选范围将在本轮完成后补记。

## 后续关注与更正

- 以原文链接、资源版本与实质变化去重；全库检索本页原链接和资源名未发现已收录条目，当前均为首次收录，近期补录与今日发布不混称。
- 模型卡中的作者评估不代表本库独立验证；若后续读取配置或图像，再注明增量与日期。
