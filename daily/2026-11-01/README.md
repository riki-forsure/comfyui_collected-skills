# 2026-11-01 每日社区发现

感谢社区作者公开分享模型、工作流、教程和实践经验。本页为本库概述与分类，原作者、原文和读取范围随条目保留，欢迎回原文阅读完整说明与更新。

- 检索类型：无具体差距要求的每日广泛发现；无主动专题。
- 实际开始时间：2026-11-01 04:01（北京时间；工具UTC时钟换算）。
- 优先时间窗：2026-10-31 04:08之后的新增与实质更新；必要的近期补录单列。
- 执行状态：进行中；已完成的阅读先行归档，其他来源继续补充。
- 已归档 3 项分享／实质更新。无节点安装、模型下载、生图或自动实验。

## 今日值得阅读

- [MOSS-Image-IDM-2-Steps：两步生成与属性编辑的新训练记录](https://huggingface.co/akhaliq/MOSS-Image-IDM-2-Steps)：相比上轮仅249次更新的OPD，作者另行发布数据空间8→4→2步路线，并加入参考图条件、DMD与特征矩匹配；当前root v2把编辑增量合入适配器。作者报告笑容和颜色编辑有进展，草图转照片、黑白上色仍失败。
- [Krea2 Turbo三步蒸馏LoRA：chk00030000](https://huggingface.co/lvladikov/Krea2-Turbo-Distill-3step-LoRA)：作者从四步适配器继续训练三步模型，公开三万训练样本、检查点与分辨率对照，并分别提供Diffusers和ComfyUI键名文件。适合学习少步模型对细节、颜色、教师相似性和耗时的取舍。
- [SnapRef v2a-pre2：多参考图与角色／画风分工](https://huggingface.co/0ppxnhximxr/snapref-v2a-pre2)：新增char模式尝试保留角色而弱化参考图画风；同一角色可提供上半身与全身等多参考并设置权重。作者也公开了cs模式的部分匹配指标略低于v1a，因此仍将v2a标为预览。

## 分享速查

| 编号／分享 | 原始日期／口径 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 读取状态 |
|---|---|---|---|---|---|
| [N01 MOSS-Image-IDM-2-Steps：两步生成与属性编辑的新训练记录](https://huggingface.co/akhaliq/MOSS-Image-IDM-2-Steps) | 2026-11-01 03:20:15 +08:00（当前仓库提交，非首发日） | 少步蒸馏·图像编辑｜区分文生图、属性编辑与结构改写的边界。 | — | [akhaliq](https://huggingface.co/akhaliq/MOSS-Image-IDM-2-Steps) | 当前模型卡全文、公开版本元数据；未看评估图、未读代码／日志或复跑 |
| [N02 Krea2 Turbo三步蒸馏LoRA：chk00030000](https://huggingface.co/lvladikov/Krea2-Turbo-Distill-3step-LoRA) | 2026-11-01 03:16:31 +08:00（当前仓库提交，非首发日） | 采样加速·后训练模型｜了解Krea2 Turbo从8步到3步的蒸馏用法。 | — | [lvladikov](https://huggingface.co/lvladikov/Krea2-Turbo-Distill-3step-LoRA) | 模型卡简介、文件、ComfyUI用法、Raw条件、检查点／分辨率与许可段落；中间训练细节和详细附卡未完整学习，未看图 |
| [N03 SnapRef v2a-pre2：多参考图与角色／画风分工](https://huggingface.co/0ppxnhximxr/snapref-v2a-pre2) | 2026-11-01 01:10:08 +08:00（当前仓库提交，非首发日） | 人物参考·画风控制｜组合角色多张参考并分别组织身份与画风。 | 设计思路：身份与画风分离｜参考图提供角色特征，提示词另选画风。 | [0ppxnhximxr / ArcAnima](https://huggingface.co/0ppxnhximxr/snapref-v2a-pre2) | 模型卡版本说明、参数、评估、训练与限制段落；未看示范图或训练配置文件 |

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

## 实际平台覆盖

| 平台 | 入口、实际范围与状态 |
|---|---|
| 固定来源 | 两吧、HF、GitHub、Civitai、B站、Reddit均已发起本轮查询；细节随后更新。 |

资料读取、作者报告、视觉观察与实际生成分别记录。本次归档不等于效果验证。

[返回总索引](../../每日检索可速查总结.md)
