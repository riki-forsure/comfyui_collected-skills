# Hugging Face：近四个月历史分享

感谢原作者的公开分享。本分册为本库摘要整理，保留作者与原文入口；欢迎回原帖阅读完整教程与后续更新。

- 历史时间窗：2026-06-30至本次检索时刻（2026-10-30，北京时间）。
- 收录时间：2026-10-30 09:12:34 +08:00；研究执行：gpt-6.1-terra 子代理。
- 日期有原始依据：23条；待核线索：1条。
- 不同条目的读取深度见详情；日期已核不代表已完整观看或效果验证。
- [总览](README.md) · [覆盖记录](coverage.md) · [当天汇总](../../README.md)

## 分享速查

| 编号／原分享 | 原文／版本日期 | 适用方向（短标注） | 美术风格方向 | 原作者 | 详情与读取范围 |
|---|---|---|---|---|---|
| [HF-01 Sun-Direction-Lora-Flux2Klein9B v1](https://huggingface.co/eric-venti-seeds/Sun-Direction-Lora-Flux2Klein9B) | 2026-06-30 | 光照控制·FLUX.2｜以参考球改变室外太阳方向；作者建议先去除原有强光方向。 | —（不涉及具体画风） | eric-venti-seeds | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-01) |
| [HF-02 Qwen-Image-Flash 4-step](https://huggingface.co/nvidia/Qwen-Image-Flash) | 2026-07-02 | 蒸馏·快速采样｜Qwen-Image 的 DMD2 蒸馏四步文生图。 | —（不涉及具体画风） | nvidia | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-02) |
| [HF-03 Anima-Lightning step-400 更新](https://huggingface.co/aina-tech/Anima-Lightning) | 2026-10-02 | 蒸馏·Anima｜实质替换早期蒸馏模型与采样方案，需使用作者自定义 transforme… | 动漫插画｜作者称 anime 和 illustration；例图未核，人物造型… | aina-tech | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-03) |
| [HF-04 Anima-2.9B preview v1](https://huggingface.co/Gazingstars123/Anima-2.9B) | 2026-08-12 | 动漫插画·结构扩展｜Anima 扩层微调，从28层扩至40层，作者称增加约170万训练样本。 | 动漫插画｜作者称动漫及插画；例图未核，人物体型五官及光影待确认。 | Gazingstars123 | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-04) |
| [HF-05 Anima_Kawai_Inpaint_ControlNet-LLLite 12000-…](https://huggingface.co/kawaimasa/Anima_Kawai_Inpaint_ControlNet-LLLite) | 2026-08-15 | 局部修复·Anima｜Anima Base v1.0 的轻量局部重绘控制器。 | 动漫插画｜作者称动画与插画；例图未核，人物造型待确认。 | kawaimasa | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-05) |
| [HF-06 Anima-3.8B v1.1](https://huggingface.co/lylogummy/Anima-3.8B) | 2026-09-01 | 多主体·Anima·提示词｜扩展到52层并引入 Semantic Connector，作者面向人物… | 动漫插画｜作者称 Anima visual style；例图未核，人物造型待确… | lylogummy | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-06) |
| [HF-07 AniSee V2 Base/Aesthetic/Turbo](https://huggingface.co/SeeSee21/AniSee) | 2026-09-06 | 动漫插画·Anima·后训练｜旧仓库新发布V2三款权重；作者说明为单个 LoKr 合并，区别于 V1… | 动漫插画｜作者称更干净的动漫风；例图未核，人物造型及色彩光影待确认。 | SeeSee21 | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-07) |
| [HF-08 Qwen-Image-2.1 0919 checkpoint](https://huggingface.co/Qwen/Qwen-Image-2.1) | 2026-09-19 | 图像生成·编辑｜官方图像生成与编辑模型；9月19日提交实质替换权重并修正 VAE 空间… | —（不涉及具体画风） | Qwen | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-08) |
| [HF-09 Anima-Light-Lavender BF16/MXFP8](https://huggingface.co/Johnny-Z/Anima-Light-Lavender) | 2026-09-18 | 动漫插画·自然语言｜基于 Anima Base v1.0 后训练，关注长自然语言和结构化描… | 动漫插画｜作者称 Anima 插画；例图未核，人物造型待确认。 | Johnny-Z | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-09) |
| [HF-10 Qwen-Image-2.1-Natural-Exposure-LoRA 4000-st…](https://huggingface.co/prithivMLmods/Qwen-Image-2.1-Natural-Exposure-LoRA) | 2026-09-23 | 曝光调整·图像编辑｜针对 Qwen Image 2.1 的输入图曝光与色彩调整适配器。 | —（不涉及具体画风） | prithivMLmods | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-10) |
| [HF-11 Qwen-Image-2.1-Fun-Controlnet-Union Union](https://huggingface.co/alibaba-pai/Qwen-Image-2.1-Fun-Controlnet-Union) | 2026-09-24 | 结构控制·局部重绘｜一个控制分支支持边缘、深度、灰度、HED、线稿、MLSD、姿态、涂鸦及… | —（不涉及具体画风） | alibaba-pai | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-11) |
| [HF-12 texture-fix-vae-for-qwen-image-2.1 BF16](https://huggingface.co/madebyollin/texture-fix-vae-for-qwen-image-2.1) | 2026-09-25 | VAE·纹理修复｜针对 Qwen Image 2.1 VAE 的纹理棋盘格和 fp16 … | —（不涉及具体画风） | madebyollin | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-12) |
| [HF-13 Qwen-Image-2.1-Outpaint-LoRA v1 step1500](https://huggingface.co/ausboss/Qwen-Image-2.1-Outpaint-LoRA) | 2026-09-26 | 扩图·图像编辑｜用灰色填充画布与编辑指令扩展场景，作者工作流在末尾贴回原图。 | —（不涉及具体画风） | ausboss | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-13) |
| [HF-14 Qwen-Image-2.1-Consistency-LoRA v1](https://huggingface.co/ausboss/Qwen-Image-2.1-Consistency-LoRA) | 2026-09-28 | 图像编辑·一致性｜降低图像编辑时非目标区域变化与构图漂移；作者也提供不加载 LoRA 的… | —（不涉及具体画风） | ausboss | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-14) |
| [HF-15 Qwen-Image-2.1-Outfit-Swap-Consistency-LoRA …](https://huggingface.co/ausboss/Qwen-Image-2.1-Outfit-Swap-Consistency-LoRA) | 2026-10-04 | 换装·一致性｜对参考换装进行局部一致性训练，减少原图主体和背景漂移。 | —（不涉及具体画风） | ausboss | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-15) |
| [HF-16 Qwen-Image-2.1-Restore-LoRA LoRA](https://huggingface.co/ausboss/Qwen-Image-2.1-Restore-LoRA) | 2026-10-07 | 图像修复·放大｜作者为降低放大时额外锐化和漂移训练的修复适配器。 | —（不涉及具体画风） | ausboss | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-16) |
| [HF-17 Qwen-Image-2.1-Turbo Turbo](https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo) | 2026-10-09 | 图像生成·快速采样｜官方2.1加速权重，支持生成和图像编辑。 | —（不涉及具体画风） | Qwen | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-17) |
| [HF-18 Qwen-Image-2.1-Anime-Fusal FUSAL 原始 Base 系列](https://huggingface.co/MicksHF/Qwen-Image-2.1-Anime-Fusal) | 2026-10-09 | 动漫插画·Qwen·LoRA｜作者的动漫领域适配及结构化提示格式，包含文生图与参考图任务。 | 动漫插画｜作者称宽分布动漫插画；例图未核，人物比例五官与材质待确认。 | MicksHF | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-18) |
| [HF-19 Anima_ControlNet-LLLite regional 4335](https://huggingface.co/toyxyz/Anima_ControlNet-LLLite) | 2026-10-11 | 多主体·区域控制｜RGB 实例颜色图控制角色区域，颜色不固定对应语义类别，黑色表示未分配。 | —（不涉及具体画风） | toyxyz | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-19) |
| [HF-20 Anima_ControlNet-LLLite 3dpose 6200](https://huggingface.co/toyxyz/Anima_ControlNet-LLLite) | 2026-10-12 | 姿态控制·多主体｜使用阴影化 RGB 三维网格作为姿态输入，作者给出与区域控制联用实例。 | —（不涉及具体画风） | toyxyz | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-20) |
| [HF-21 FLUX-3-Image-Klein-Outpaint-LoRA v1.0 step10…](https://huggingface.co/ausboss/FLUX-3-Image-Klein-Outpaint-LoRA) | 2026-10-16 | 扩图·FLUX.3｜在灰色扩边上填充场景并配合工作流贴回原图。 | —（不涉及具体画风） | ausboss | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-21) |
| [HF-22 Moss-image-anime-lora 1500/2000-step](https://huggingface.co/axiomofmind/Moss-image-anime-lora) | 2026-10-20 | 动漫插画·MOSS｜MOSS 图像基座的青年向动画风 LoRA，提供两种训练步数和 Com… | 动漫插画｜作者称青年向动漫、戏剧照明与动态构图；例图未核，人物体型五官待确认。 | axiomofmind | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-22) |
| [HF-23 anima-ref-adapter v2 r64](https://huggingface.co/ElectronGirl/anima-ref-adapter) | 2026-10-29 | 参考图·Anima｜在 Anima 工作流中加入参考图适配器及双人物支持，作者提供单节点工… | 动漫插画｜作者以 Anima 动漫角色示范；例图未核，人物体型五官待确认。 | ElectronGirl | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-23) |

## 条目详解

### HF-01

**原分享：** [Sun-Direction-Lora-Flux2Klein9B v1](https://huggingface.co/eric-venti-seeds/Sun-Direction-Lora-Flux2Klein9B)

**适用方向：** 光照控制·FLUX.2｜以参考球改变室外太阳方向；作者建议先去除原有强光方向。

**美术风格方向：** —（不涉及具体画风）

- 原作者：eric-venti-seeds
- 原始日期：2026-06-29T20:11:31Z
- 时间口径：公开提交时间（UTC）
- 日期依据：HF commits/main: 2026-06-29T20:11:31Z “Upload Sun_direction_LoRA_Flux_2_Klein_9b_v1.safetensors”；不是仓库创建时间。；精确提交 0a438b0a8d03f1b94ff450a9af33a6eaea2ea1ee.
- 类别：模型与工作流
- 精确版本：v1
- 原作者分享要点（本库概述）：以参考球改变室外太阳方向；作者建议先去除原有强光方向。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：触发词 match the sun direction from the reference；基座 FLUX.2-klein-9B；提供球体渲染节点与工作流。
- 风格说明与可见范围：— 不涉及具体画风
- 风格依据：不涉及具体画风
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。 提交链接定位日期证据，模型卡内容读取的是当前版，未逐项验证这些参数当日已存在。
- 追溯链接：https://huggingface.co/eric-venti-seeds/Sun-Direction-Lora-Flux2Klein9B/commit/0a438b0a8d03f1b94ff450a9af33a6eaea2ea1ee；https://huggingface.co/eric-venti-seeds/Sun-Direction-Lora-Flux2Klein9B/blob/0a438b0a8d03f1b94ff450a9af33a6eaea2ea1ee/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-02

**原分享：** [Qwen-Image-Flash 4-step](https://huggingface.co/nvidia/Qwen-Image-Flash)

**适用方向：** 蒸馏·快速采样｜Qwen-Image 的 DMD2 蒸馏四步文生图。

**美术风格方向：** —（不涉及具体画风）

- 原作者：nvidia
- 原始日期：2026-07-01T20:59:48Z
- 时间口径：公开提交时间（UTC）
- 日期依据：HF commits/main: 2026-07-01T20:59:48Z “Add files using upload-large-folder tool”；不是仓库创建时间。；精确提交 20fe4b8496267ff510bfd0ef0875ec27676ce9a8.
- 类别：模型与工作流
- 精确版本：4-step
- 原作者分享要点（本库概述）：Qwen-Image 的 DMD2 蒸馏四步文生图。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：Qwen2.5-VL 编码器、Qwen-Image VAE、FlowMatch Euler；4步 true_cfg_scale 1；教师 CFG 4；英文训练。
- 风格说明与可见范围：— 不涉及具体画风
- 风格依据：不涉及具体画风
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。 提交链接定位日期证据，模型卡内容读取的是当前版，未逐项验证这些参数当日已存在。
- 追溯链接：https://huggingface.co/nvidia/Qwen-Image-Flash/commit/20fe4b8496267ff510bfd0ef0875ec27676ce9a8；https://huggingface.co/nvidia/Qwen-Image-Flash/blob/20fe4b8496267ff510bfd0ef0875ec27676ce9a8/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-03

**原分享：** [Anima-Lightning step-400 更新](https://huggingface.co/aina-tech/Anima-Lightning)

**适用方向：** 蒸馏·Anima｜实质替换早期蒸馏模型与采样方案，需使用作者自定义 transforme…

**美术风格方向：** 动漫插画｜作者称 anime 和 illustration；例图未核，人物造型…

- 原作者：aina-tech
- 原始日期：2026-10-02T14:05:34Z
- 时间口径：公开提交时间（UTC）
- 日期依据：HF commits/main: 2026-10-02T14:05:34Z “Replace transformer with selected step-400 TDM-Unify in BF16”；不是仓库创建时间。；精确提交 107aaf2c123f9dac346fc5d66d9e2e544913818d.
- 类别：模型与工作流
- 精确版本：step-400 更新
- 原作者分享要点（本库概述）：实质替换早期蒸馏模型与采样方案，需使用作者自定义 transformer。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：4步 CFG 1 shift 3；raw sigmas [1,.75,.5,.25]；自定义 K=4 分支；早期 shift 1 方案不可沿用。
- 风格说明与可见范围：作者称 anime 和 illustration；例图未核，人物造型待确认。
- 风格依据：作者文字描述；未看例图
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。 提交链接定位日期证据，模型卡内容读取的是当前版，未逐项验证这些参数当日已存在。
- 追溯链接：https://huggingface.co/aina-tech/Anima-Lightning/commit/107aaf2c123f9dac346fc5d66d9e2e544913818d；https://huggingface.co/aina-tech/Anima-Lightning/blob/107aaf2c123f9dac346fc5d66d9e2e544913818d/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-04

**原分享：** [Anima-2.9B preview v1](https://huggingface.co/Gazingstars123/Anima-2.9B)

**适用方向：** 动漫插画·结构扩展｜Anima 扩层微调，从28层扩至40层，作者称增加约170万训练样本。

**美术风格方向：** 动漫插画｜作者称动漫及插画；例图未核，人物体型五官及光影待确认。

- 原作者：Gazingstars123
- 原始日期：2026-08-12T07:33:29Z
- 时间口径：公开提交时间（UTC）
- 日期依据：HF commits/main: 2026-08-12T07:33:29Z “Upload Anima-2.9B-preview-v1.safetensors”；不是仓库创建时间。；精确提交 c2ef3f50236571437c0543127a7b2502305da204.
- 类别：模型与工作流
- 精确版本：preview v1
- 原作者分享要点（本库概述）：Anima 扩层微调，从28层扩至40层，作者称增加约170万训练样本。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：28–50步、CFG 3.5–5；建议 euler+sgm-uniform 或 res_multistep+linear-quadratic；角色及版权标签绑定；无 score 标签训练。
- 风格说明与可见范围：作者称动漫及插画；例图未核，人物体型五官及光影待确认。
- 风格依据：作者文字描述；未看例图
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。 提交链接定位日期证据，模型卡内容读取的是当前版，未逐项验证这些参数当日已存在。
- 追溯链接：https://huggingface.co/Gazingstars123/Anima-2.9B/commit/c2ef3f50236571437c0543127a7b2502305da204；https://huggingface.co/Gazingstars123/Anima-2.9B/blob/c2ef3f50236571437c0543127a7b2502305da204/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-05

**原分享：** [Anima_Kawai_Inpaint_ControlNet-LLLite 12000-step](https://huggingface.co/kawaimasa/Anima_Kawai_Inpaint_ControlNet-LLLite)

**适用方向：** 局部修复·Anima｜Anima Base v1.0 的轻量局部重绘控制器。

**美术风格方向：** 动漫插画｜作者称动画与插画；例图未核，人物造型待确认。

- 原作者：kawaimasa
- 原始日期：2026-08-14T23:12:02Z
- 时间口径：公开提交时间（UTC）
- 日期依据：HF commits/main: 2026-08-14T23:12:02Z “Upload 2 files”；不是仓库创建时间。；精确提交 bd9092ffa5f69c257c012d10ee133f7e273cdb65.
- 类别：模型与工作流
- 精确版本：12000-step
- 原作者分享要点（本库概述）：Anima Base v1.0 的轻量局部重绘控制器。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：发布 12000 步权重；约3.6万训练图片，512/768/1024/1536 多尺度；CFG 4；需四通道 inpaint 条件。
- 风格说明与可见范围：作者称动画与插画；例图未核，人物造型待确认。
- 风格依据：作者文字描述；未看例图
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。 提交链接定位日期证据，模型卡内容读取的是当前版，未逐项验证这些参数当日已存在。
- 追溯链接：https://huggingface.co/kawaimasa/Anima_Kawai_Inpaint_ControlNet-LLLite/commit/bd9092ffa5f69c257c012d10ee133f7e273cdb65；https://huggingface.co/kawaimasa/Anima_Kawai_Inpaint_ControlNet-LLLite/blob/bd9092ffa5f69c257c012d10ee133f7e273cdb65/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-06

**原分享：** [Anima-3.8B v1.1](https://huggingface.co/lylogummy/Anima-3.8B)

**适用方向：** 多主体·Anima·提示词｜扩展到52层并引入 Semantic Connector，作者面向人物…

**美术风格方向：** 动漫插画｜作者称 Anima visual style；例图未核，人物造型待确…

- 原作者：lylogummy
- 原始日期：2026-08-31T19:21:01Z
- 时间口径：公开提交时间（UTC）
- 日期依据：2026-08-31 19:21:01 UTC 上传 v6 权重；19:40:06 将同文件改名 v1.1；20:50:45 的模型卡说明 v1.1 与 Semantic Connector v2。上传与重命名两个提交共同建立关联。
- 类别：模型与工作流
- 精确版本：v1.1
- 原作者分享要点（本库概述）：扩展到52层并引入 Semantic Connector，作者面向人物绑定与空间关系。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：Qwen3.5 4B 与 Qwen3 0.6B 编码器、Qwen-Image VAE；建议28–50步 CFG 4–7；对每个角色用独立句子。
- 风格说明与可见范围：作者称 Anima visual style；例图未核，人物造型待确认。
- 风格依据：作者文字描述；未看例图
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。
- 追溯链接：https://huggingface.co/lylogummy/Anima-3.8B/commit/c55bfed3a694e61472c03625ad2b32646d6981ff；https://huggingface.co/lylogummy/Anima-3.8B/commit/8a6b3ab6fe4e201c02ecb53107516b89a263a2f3；https://huggingface.co/lylogummy/Anima-3.8B/blob/3ef641256377dc4e7efbf35d426ca31c1fe5180b/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-07

**原分享：** [AniSee V2 Base/Aesthetic/Turbo](https://huggingface.co/SeeSee21/AniSee)

**适用方向：** 动漫插画·Anima·后训练｜旧仓库新发布V2三款权重；作者说明为单个 LoKr 合并，区别于 V1…

**美术风格方向：** 动漫插画｜作者称更干净的动漫风；例图未核，人物造型及色彩光影待确认。

- 原作者：SeeSee21
- 原始日期：2026-09-05T19:02:03Z
- 时间口径：公开提交时间（UTC）
- 日期依据：HF commits/main: 2026-09-05T19:02:03Z “Add AniSee-V2-Base.safetensors — LoKr merge on anima-base-v1.0”；不是仓库创建时间。；精确提交 7fe8b617147a9e38335fc5121477ca886d54965f.
- 类别：模型与工作流
- 精确版本：V2 Base/Aesthetic/Turbo
- 原作者分享要点（本库概述）：旧仓库新发布V2三款权重；作者说明为单个 LoKr 合并，区别于 V1 全量微调。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：约24000步 LoKr 以强度1合并至 Anima Base v1.0、Aesthetic v1.1、Turbo v1.1；Qwen文本编码器及Qwen-Image VAE；Base 40步 CFG 4–5、Turbo 12步 CFG 1。
- 风格说明与可见范围：作者称更干净的动漫风；例图未核，人物造型及色彩光影待确认。
- 风格依据：作者文字描述；未看例图
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。 提交链接定位日期证据，模型卡内容读取的是当前版，未逐项验证这些参数当日已存在。
- 追溯链接：https://huggingface.co/SeeSee21/AniSee/commit/7fe8b617147a9e38335fc5121477ca886d54965f；https://huggingface.co/SeeSee21/AniSee/blob/7fe8b617147a9e38335fc5121477ca886d54965f/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-08

**原分享：** [Qwen-Image-2.1 0919 checkpoint](https://huggingface.co/Qwen/Qwen-Image-2.1)

**适用方向：** 图像生成·编辑｜官方图像生成与编辑模型；9月19日提交实质替换权重并修正 VAE 空间…

**美术风格方向：** —（不涉及具体画风）

- 原作者：Qwen
- 原始日期：2026-09-19T00:40:14Z
- 时间口径：公开提交时间（UTC）
- 日期依据：HF commits/main: 2026-09-19T00:40:14Z “Update to 0919 release checkpoint; fix vae scale_factor_spatial=16, remove transformer causal_block”；不是仓库创建时间。；精确提交 840b4adb1e2c21c7d77967203188b55b678c535f.
- 类别：模型与工作流
- 精确版本：0919 checkpoint
- 原作者分享要点（本库概述）：官方图像生成与编辑模型；9月19日提交实质替换权重并修正 VAE 空间倍率。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：官方示例40步；使用 Qwen3-VL 编码器；专用2.1 VAE；不同于旧版 Qwen-Image。
- 风格说明与可见范围：— 不涉及具体画风
- 风格依据：不涉及具体画风
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。 提交链接定位日期证据，模型卡内容读取的是当前版，未逐项验证这些参数当日已存在。
- 追溯链接：https://huggingface.co/Qwen/Qwen-Image-2.1/commit/840b4adb1e2c21c7d77967203188b55b678c535f；https://huggingface.co/Qwen/Qwen-Image-2.1/blob/840b4adb1e2c21c7d77967203188b55b678c535f/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-09

**原分享：** [Anima-Light-Lavender BF16/MXFP8](https://huggingface.co/Johnny-Z/Anima-Light-Lavender)

**适用方向：** 动漫插画·自然语言｜基于 Anima Base v1.0 后训练，关注长自然语言和结构化描…

**美术风格方向：** 动漫插画｜作者称 Anima 插画；例图未核，人物造型待确认。

- 原作者：Johnny-Z
- 原始日期：2026-09-18T10:43:56Z
- 时间口径：公开提交时间（UTC）
- 日期依据：HF commits/main: 2026-09-18T10:43:56Z “Upload folder using huggingface_hub”；不是仓库创建时间。；精确提交 28bffb64500395361020adc25d056a55ed1f48cc.
- 类别：模型与工作流
- 精确版本：BF16/MXFP8
- 原作者分享要点（本库概述）：基于 Anima Base v1.0 后训练，关注长自然语言和结构化描述。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：28层约2B；Qwen3-0.6B、Qwen-Image VAE；示例 Euler、25步 CFG 4；支持结构化 caption 和 512 token 描述。
- 风格说明与可见范围：作者称 Anima 插画；例图未核，人物造型待确认。
- 风格依据：作者文字描述；未看例图
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。 提交链接定位日期证据，模型卡内容读取的是当前版，未逐项验证这些参数当日已存在。
- 追溯链接：https://huggingface.co/Johnny-Z/Anima-Light-Lavender/commit/28bffb64500395361020adc25d056a55ed1f48cc；https://huggingface.co/Johnny-Z/Anima-Light-Lavender/blob/28bffb64500395361020adc25d056a55ed1f48cc/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-10

**原分享：** [Qwen-Image-2.1-Natural-Exposure-LoRA 4000-step](https://huggingface.co/prithivMLmods/Qwen-Image-2.1-Natural-Exposure-LoRA)

**适用方向：** 曝光调整·图像编辑｜针对 Qwen Image 2.1 的输入图曝光与色彩调整适配器。

**美术风格方向：** —（不涉及具体画风）

- 原作者：prithivMLmods
- 原始日期：2026-09-23T14:14:08Z
- 时间口径：公开提交时间（UTC）
- 日期依据：HF commits/main: 2026-09-23T14:14:08Z “Upload Qwen-Image-2.1-Natural-Exposure-LoRA”；不是仓库创建时间。；精确提交 43f62ce16ff9e2f87d4e13dc0ceaec0b4b844dfc.
- 类别：模型与工作流
- 精确版本：4000-step
- 原作者分享要点（本库概述）：针对 Qwen Image 2.1 的输入图曝光与色彩调整适配器。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：触发短句 Transform the image with balanced neutral exposure；4000训练步；作者描述适用过曝、欠曝与复杂光照。
- 风格说明与可见范围：— 不涉及具体画风
- 风格依据：不涉及具体画风
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。 提交链接定位日期证据，模型卡内容读取的是当前版，未逐项验证这些参数当日已存在。
- 追溯链接：https://huggingface.co/prithivMLmods/Qwen-Image-2.1-Natural-Exposure-LoRA/commit/43f62ce16ff9e2f87d4e13dc0ceaec0b4b844dfc；https://huggingface.co/prithivMLmods/Qwen-Image-2.1-Natural-Exposure-LoRA/blob/43f62ce16ff9e2f87d4e13dc0ceaec0b4b844dfc/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-11

**原分享：** [Qwen-Image-2.1-Fun-Controlnet-Union Union](https://huggingface.co/alibaba-pai/Qwen-Image-2.1-Fun-Controlnet-Union)

**适用方向：** 结构控制·局部重绘｜一个控制分支支持边缘、深度、灰度、HED、线稿、MLSD、姿态、涂鸦及…

**美术风格方向：** —（不涉及具体画风）

- 原作者：alibaba-pai
- 原始日期：2026-09-24T06:02:12Z
- 时间口径：公开提交时间（UTC）
- 日期依据：HF commits/main: 2026-09-24T06:02:12Z “Update Weights”；不是仓库创建时间。；精确提交 8a4702014d4dabb5f896fcba917e2ee0a961465f.
- 类别：模型与工作流
- 精确版本：Union
- 原作者分享要点（本库概述）：一个控制分支支持边缘、深度、灰度、HED、线稿、MLSD、姿态、涂鸦及蒙版修复。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：16注入点；control_context_scale 1；示例40步、guidance_scale 1；白色蒙版重绘；Qwen3-VL 和 RGBA VAE。
- 风格说明与可见范围：— 不涉及具体画风
- 风格依据：不涉及具体画风
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。 提交链接定位日期证据，模型卡内容读取的是当前版，未逐项验证这些参数当日已存在。
- 追溯链接：https://huggingface.co/alibaba-pai/Qwen-Image-2.1-Fun-Controlnet-Union/commit/8a4702014d4dabb5f896fcba917e2ee0a961465f；https://huggingface.co/alibaba-pai/Qwen-Image-2.1-Fun-Controlnet-Union/blob/8a4702014d4dabb5f896fcba917e2ee0a961465f/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-12

**原分享：** [texture-fix-vae-for-qwen-image-2.1 BF16](https://huggingface.co/madebyollin/texture-fix-vae-for-qwen-image-2.1)

**适用方向：** VAE·纹理修复｜针对 Qwen Image 2.1 VAE 的纹理棋盘格和 fp16 …

**美术风格方向：** —（不涉及具体画风）

- 原作者：madebyollin
- 原始日期：2026-09-24T17:25:57Z
- 时间口径：公开提交时间（UTC）
- 日期依据：HF commits/main: 2026-09-24T17:25:57Z “Add texture-fix VAE weights (diffusers + ComfyUI), README, demo images, LICENSE”；不是仓库创建时间。；精确提交 8b6801b3cb66523b8f277acccf50a687bc1030b6.
- 类别：模型与工作流
- 精确版本：BF16
- 原作者分享要点（本库概述）：针对 Qwen Image 2.1 VAE 的纹理棋盘格和 fp16 数值问题做微调；作者报告感知与重建指标权衡。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：ComfyUI 与 Diffusers 权重；适用 Qwen Image 2.1，作者称改善 fp16 NaN；rFID 及 LPIPS/PSNR 不同向。
- 风格说明与可见范围：— 不涉及具体画风
- 风格依据：不涉及具体画风
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。 提交链接定位日期证据，模型卡内容读取的是当前版，未逐项验证这些参数当日已存在。
- 追溯链接：https://huggingface.co/madebyollin/texture-fix-vae-for-qwen-image-2.1/commit/8b6801b3cb66523b8f277acccf50a687bc1030b6；https://huggingface.co/madebyollin/texture-fix-vae-for-qwen-image-2.1/blob/8b6801b3cb66523b8f277acccf50a687bc1030b6/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-13

**原分享：** [Qwen-Image-2.1-Outpaint-LoRA v1 step1500](https://huggingface.co/ausboss/Qwen-Image-2.1-Outpaint-LoRA)

**适用方向：** 扩图·图像编辑｜用灰色填充画布与编辑指令扩展场景，作者工作流在末尾贴回原图。

**美术风格方向：** —（不涉及具体画风）

- 原作者：ausboss
- 原始日期：2026-09-26T00:14:20Z
- 时间口径：公开提交时间（UTC）
- 日期依据：HF commits/main: 2026-09-26T00:14:20Z “Upload outpaint LoRA”；不是仓库创建时间。；精确提交 b96e7bb4ac2d387dbe7df78af9c79e3b46be961f.
- 类别：模型与工作流
- 精确版本：v1 step1500
- 原作者分享要点（本库概述）：用灰色填充画布与编辑指令扩展场景，作者工作流在末尾贴回原图。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：Qwen Image 2.1；样例25步 CFG 1；v1 约1MP训练；灰色填充及作者指令，原像素经 Stitch Inpaint 贴回。
- 风格说明与可见范围：— 不涉及具体画风
- 风格依据：不涉及具体画风
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。 提交链接定位日期证据，模型卡内容读取的是当前版，未逐项验证这些参数当日已存在。
- 追溯链接：https://huggingface.co/ausboss/Qwen-Image-2.1-Outpaint-LoRA/commit/b96e7bb4ac2d387dbe7df78af9c79e3b46be961f；https://huggingface.co/ausboss/Qwen-Image-2.1-Outpaint-LoRA/blob/b96e7bb4ac2d387dbe7df78af9c79e3b46be961f/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-14

**原分享：** [Qwen-Image-2.1-Consistency-LoRA v1](https://huggingface.co/ausboss/Qwen-Image-2.1-Consistency-LoRA)

**适用方向：** 图像编辑·一致性｜降低图像编辑时非目标区域变化与构图漂移；作者也提供不加载 LoRA 的…

**美术风格方向：** —（不涉及具体画风）

- 原作者：ausboss
- 原始日期：2026-09-27T21:30:27Z
- 时间口径：公开提交时间（UTC）
- 日期依据：HF commits/main: 2026-09-27T21:30:27Z “Consistency LoRA v1”；不是仓库创建时间。；精确提交 101455c36cb284a84f243353c54f3fe8bbf7ed59.
- 类别：模型与工作流
- 精确版本：v1
- 原作者分享要点（本库概述）：降低图像编辑时非目标区域变化与构图漂移；作者也提供不加载 LoRA 的对齐工作流。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：无触发词；强度1；25步 CFG 1 Euler/simple；作者指出可能限制需要大变化的编辑。
- 风格说明与可见范围：— 不涉及具体画风
- 风格依据：不涉及具体画风
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。 提交链接定位日期证据，模型卡内容读取的是当前版，未逐项验证这些参数当日已存在。
- 追溯链接：https://huggingface.co/ausboss/Qwen-Image-2.1-Consistency-LoRA/commit/101455c36cb284a84f243353c54f3fe8bbf7ed59；https://huggingface.co/ausboss/Qwen-Image-2.1-Consistency-LoRA/blob/101455c36cb284a84f243353c54f3fe8bbf7ed59/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-15

**原分享：** [Qwen-Image-2.1-Outfit-Swap-Consistency-LoRA LoRA](https://huggingface.co/ausboss/Qwen-Image-2.1-Outfit-Swap-Consistency-LoRA)

**适用方向：** 换装·一致性｜对参考换装进行局部一致性训练，减少原图主体和背景漂移。

**美术风格方向：** —（不涉及具体画风）

- 原作者：ausboss
- 原始日期：2026-10-04T04:41:03Z
- 时间口径：公开提交时间（UTC）
- 日期依据：HF commits/main: 2026-10-04T04:41:03Z “Add the outfit swap LoRA, card, research notes, workflow and figures”；不是仓库创建时间。；精确提交 a6d071cff66b2c8019d3b6beff264083ffbc6fb3.
- 类别：模型与工作流
- 精确版本：LoRA
- 原作者分享要点（本库概述）：对参考换装进行局部一致性训练，减少原图主体和背景漂移。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：Qwen Image 2.1；无触发词；强度1；作者样例25步 CFG 1 Euler/simple；作者亦报告部分服装细节复制不足。
- 风格说明与可见范围：— 不涉及具体画风
- 风格依据：不涉及具体画风
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。 提交链接定位日期证据，模型卡内容读取的是当前版，未逐项验证这些参数当日已存在。
- 追溯链接：https://huggingface.co/ausboss/Qwen-Image-2.1-Outfit-Swap-Consistency-LoRA/commit/a6d071cff66b2c8019d3b6beff264083ffbc6fb3；https://huggingface.co/ausboss/Qwen-Image-2.1-Outfit-Swap-Consistency-LoRA/blob/a6d071cff66b2c8019d3b6beff264083ffbc6fb3/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-16

**原分享：** [Qwen-Image-2.1-Restore-LoRA LoRA](https://huggingface.co/ausboss/Qwen-Image-2.1-Restore-LoRA)

**适用方向：** 图像修复·放大｜作者为降低放大时额外锐化和漂移训练的修复适配器。

**美术风格方向：** —（不涉及具体画风）

- 原作者：ausboss
- 原始日期：2026-10-07（确切发布日期未知）
- 时间口径：窗口内存在时间界限（非精确发布日期）
- 日期依据：API createdAt 2026-10-07 14:27:42 UTC；该日16:18:34 squash 快照已包含两份 Restore 权重、模型卡和工作流。仓库在窗口内创建且快照时已存在，足证资源在窗口内出现；无法确定首次上传或公开的确切时间，squash 本身不证明当时有新变更。
- 类别：模型与工作流
- 精确版本：LoRA
- 原作者分享要点（本库概述）：作者为降低放大时额外锐化和漂移训练的修复适配器。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：无触发词，强度1；模糊图建议0.5；可配 Viggle Turbo 8步或原模型25步；提交历史被 squash。
- 风格说明与可见范围：— 不涉及具体画风
- 风格依据：不涉及具体画风
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。
- 追溯链接：https://huggingface.co/ausboss/Qwen-Image-2.1-Restore-LoRA/tree/22dab373bf2c832dd19ee81449f5658b4209a244；https://huggingface.co/ausboss/Qwen-Image-2.1-Restore-LoRA/blob/22dab373bf2c832dd19ee81449f5658b4209a244/README.md；https://huggingface.co/api/models/ausboss/Qwen-Image-2.1-Restore-LoRA
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-17

**原分享：** [Qwen-Image-2.1-Turbo Turbo](https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo)

**适用方向：** 图像生成·快速采样｜官方2.1加速权重，支持生成和图像编辑。

**美术风格方向：** —（不涉及具体画风）

- 原作者：Qwen
- 原始日期：2026-10-09T05:19:14Z
- 时间口径：公开提交时间（UTC）
- 日期依据：HF commits/main: 2026-10-09T05:19:14Z “Upload Qwen-Image-2.1-Turbo model and model card”；不是仓库创建时间。；精确提交 066a07d448bc120b2d99d75f1935a76b8c80864b.
- 类别：模型与工作流
- 精确版本：Turbo
- 原作者分享要点（本库概述）：官方2.1加速权重，支持生成和图像编辑。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：8步；7B视觉生成架构；内置采样序列，单独修改步数不会覆盖其调度；模型卡含2K示例。
- 风格说明与可见范围：— 不涉及具体画风
- 风格依据：不涉及具体画风
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。 提交链接定位日期证据，模型卡内容读取的是当前版，未逐项验证这些参数当日已存在。
- 追溯链接：https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo/commit/066a07d448bc120b2d99d75f1935a76b8c80864b；https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo/blob/066a07d448bc120b2d99d75f1935a76b8c80864b/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-18

**原分享：** [Qwen-Image-2.1-Anime-Fusal FUSAL 原始 Base 系列](https://huggingface.co/MicksHF/Qwen-Image-2.1-Anime-Fusal)

**适用方向：** 动漫插画·Qwen·LoRA｜作者的动漫领域适配及结构化提示格式，包含文生图与参考图任务。

**美术风格方向：** 动漫插画｜作者称宽分布动漫插画；例图未核，人物比例五官与材质待确认。

- 原作者：MicksHF
- 原始日期：2026-10-09T08:15:19Z
- 时间口径：公开提交时间（UTC）
- 日期依据：HF commits/main: 2026-10-09T08:15:19Z “Add validated FUSAL merged BF16 transformer; all four adapters at 1.0”；不是仓库创建时间。；精确提交 c0492e98c2ab17990264f9b06c5754b3d8fc16d5.
- 类别：模型与工作流
- 精确版本：FUSAL 原始 Base 系列
- 原作者分享要点（本库概述）：作者的动漫领域适配及结构化提示格式，包含文生图与参考图任务。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：卡片当前建议原版 Base R56 强度0.7–1.0、CFG 1、触发 fusal style.；Turbo E6 为不同基座的独立预览，版本发表时间需再核。
- 风格说明与可见范围：作者称宽分布动漫插画；例图未核，人物比例五官与材质待确认。
- 风格依据：作者文字描述；未看例图
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。 提交链接定位日期证据，模型卡内容读取的是当前版，未逐项验证这些参数当日已存在。
- 追溯链接：https://huggingface.co/MicksHF/Qwen-Image-2.1-Anime-Fusal/commit/c0492e98c2ab17990264f9b06c5754b3d8fc16d5；https://huggingface.co/MicksHF/Qwen-Image-2.1-Anime-Fusal/blob/c0492e98c2ab17990264f9b06c5754b3d8fc16d5/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-19

**原分享：** [Anima_ControlNet-LLLite regional 4335](https://huggingface.co/toyxyz/Anima_ControlNet-LLLite)

**适用方向：** 多主体·区域控制｜RGB 实例颜色图控制角色区域，颜色不固定对应语义类别，黑色表示未分配。

**美术风格方向：** —（不涉及具体画风）

- 原作者：toyxyz
- 原始日期：2026-10-11T08:40:36Z
- 时间口径：公开提交时间（UTC）
- 日期依据：HF commits/main: 2026-10-11T08:40:36Z “Anima Regional LLLite public release”；不是仓库创建时间。；精确提交 e126fbb89a7abb29ba61ee9dbb07ea4300fdbcbf.
- 类别：模型与工作流
- 精确版本：regional 4335
- 原作者分享要点（本库概述）：RGB 实例颜色图控制角色区域，颜色不固定对应语义类别，黑色表示未分配。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：Anima Base 1.0；regional 4335 强度1、30步 CFG 4；作者另提示多人联合控制时可将区域控制 end_percent 设0.3。
- 风格说明与可见范围：— 不涉及具体画风
- 风格依据：不涉及具体画风
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。 提交链接定位日期证据，模型卡内容读取的是当前版，未逐项验证这些参数当日已存在。
- 追溯链接：https://huggingface.co/toyxyz/Anima_ControlNet-LLLite/commit/e126fbb89a7abb29ba61ee9dbb07ea4300fdbcbf；https://huggingface.co/toyxyz/Anima_ControlNet-LLLite/blob/e126fbb89a7abb29ba61ee9dbb07ea4300fdbcbf/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-20

**原分享：** [Anima_ControlNet-LLLite 3dpose 6200](https://huggingface.co/toyxyz/Anima_ControlNet-LLLite)

**适用方向：** 姿态控制·多主体｜使用阴影化 RGB 三维网格作为姿态输入，作者给出与区域控制联用实例。

**美术风格方向：** —（不涉及具体画风）

- 原作者：toyxyz
- 原始日期：2026-10-12T15:57:16Z
- 时间口径：公开提交时间（UTC）
- 日期依据：HF commits/main: 2026-10-12T15:57:16Z “Add final 6200-step Anima 3D pose LLLite adapter and documentation”；不是仓库创建时间。；精确提交 444c08e162763603e154395dbddc3e6f417163bd.
- 类别：模型与工作流
- 精确版本：3dpose 6200
- 原作者分享要点（本库概述）：使用阴影化 RGB 三维网格作为姿态输入，作者给出与区域控制联用实例。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：Anima Base 1.0；强度1、30步 CFG 4、flow shift 3；不同于10月16日独立训练的 outline 7000。
- 风格说明与可见范围：— 不涉及具体画风
- 风格依据：不涉及具体画风
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。 提交链接定位日期证据，模型卡内容读取的是当前版，未逐项验证这些参数当日已存在。
- 追溯链接：https://huggingface.co/toyxyz/Anima_ControlNet-LLLite/commit/444c08e162763603e154395dbddc3e6f417163bd；https://huggingface.co/toyxyz/Anima_ControlNet-LLLite/blob/444c08e162763603e154395dbddc3e6f417163bd/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-21

**原分享：** [FLUX-3-Image-Klein-Outpaint-LoRA v1.0 step1000 rank32](https://huggingface.co/ausboss/FLUX-3-Image-Klein-Outpaint-LoRA)

**适用方向：** 扩图·FLUX.3｜在灰色扩边上填充场景并配合工作流贴回原图。

**美术风格方向：** —（不涉及具体画风）

- 原作者：ausboss
- 原始日期：2026-10-15T23:41:04Z
- 时间口径：公开提交时间（UTC）
- 日期依据：HF commits/main: 2026-10-15T23:41:04Z “FLUX 3 Image Klein Outpaint LoRA v1.0”；不是仓库创建时间。；精确提交 1ff2070a12f26a153fff2e3906dc596856fa8d13.
- 类别：模型与工作流
- 精确版本：v1.0 step1000 rank32
- 原作者分享要点（本库概述）：在灰色扩边上填充场景并配合工作流贴回原图。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：基座训练为 FLUX.3 Image Klein base；作者测蒸馏版16步 CFG 1、LoRA 1.5；灰色 #808080；需指定扩图指令；官方模型许可门控。
- 风格说明与可见范围：— 不涉及具体画风
- 风格依据：不涉及具体画风
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。 提交链接定位日期证据，模型卡内容读取的是当前版，未逐项验证这些参数当日已存在。
- 追溯链接：https://huggingface.co/ausboss/FLUX-3-Image-Klein-Outpaint-LoRA/commit/1ff2070a12f26a153fff2e3906dc596856fa8d13；https://huggingface.co/ausboss/FLUX-3-Image-Klein-Outpaint-LoRA/blob/1ff2070a12f26a153fff2e3906dc596856fa8d13/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-22

**原分享：** [Moss-image-anime-lora 1500/2000-step](https://huggingface.co/axiomofmind/Moss-image-anime-lora)

**适用方向：** 动漫插画·MOSS｜MOSS 图像基座的青年向动画风 LoRA，提供两种训练步数和 Com…

**美术风格方向：** 动漫插画｜作者称青年向动漫、戏剧照明与动态构图；例图未核，人物体型五官待确认。

- 原作者：axiomofmind
- 原始日期：2026-10-20T07:07:16Z
- 时间口径：公开提交时间（UTC）
- 日期依据：HF commits/main: 2026-10-20T07:07:16Z “Publish MOSS Image anime LoRA checkpoints 1500 and 2000”；不是仓库创建时间。；精确提交 f03fe9589e17a8c369a5ec8c877abc7dc25ca005.
- 类别：模型与工作流
- 精确版本：1500/2000-step
- 原作者分享要点（本库概述）：MOSS 图像基座的青年向动画风 LoRA，提供两种训练步数和 ComfyUI 专用权重。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：训练 MOSS-Image-Base，作者推荐在 SFT 推理；2000步强度1、1500步0.7或1；moss_seinen_style 可省略；50步 CFG 3。
- 风格说明与可见范围：作者称青年向动漫、戏剧照明与动态构图；例图未核，人物体型五官待确认。
- 风格依据：作者文字描述；未看例图
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。 提交链接定位日期证据，模型卡内容读取的是当前版，未逐项验证这些参数当日已存在。
- 追溯链接：https://huggingface.co/axiomofmind/Moss-image-anime-lora/commit/f03fe9589e17a8c369a5ec8c877abc7dc25ca005；https://huggingface.co/axiomofmind/Moss-image-anime-lora/blob/f03fe9589e17a8c369a5ec8c877abc7dc25ca005/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### HF-23

**原分享：** [anima-ref-adapter v2 r64](https://huggingface.co/ElectronGirl/anima-ref-adapter)

**适用方向：** 参考图·Anima｜在 Anima 工作流中加入参考图适配器及双人物支持，作者提供单节点工…

**美术风格方向：** 动漫插画｜作者以 Anima 动漫角色示范；例图未核，人物体型五官待确认。

- 原作者：ElectronGirl
- 原始日期：2026-10-29T03:21:51Z
- 时间口径：公开提交时间（UTC）
- 日期依据：HF commits/main: 2026-10-29T03:21:51Z “v2: asymmetric attention adapter, one-node workflow, two characters”；不是仓库创建时间。；精确提交 1202b46fabffea77e0b696242daab1d63965fba6.
- 类别：模型与工作流
- 精确版本：v2 r64
- 原作者分享要点（本库概述）：在 Anima 工作流中加入参考图适配器及双人物支持，作者提供单节点工作流。
- 公开资源：原模型卡、公开文件与提交历史；以原链接为准
- 作者参数／触发词及边界：Anima Base v1.0、Qwen3-0.6B、Qwen-Image VAE；v2 r64；示例 er_sde 30步 CFG 4.5、ref_guidance 4.5；需专用节点。
- 风格说明与可见范围：作者以 Anima 动漫角色示范；例图未核，人物体型五官待确认。
- 风格依据：作者文字描述；未看例图
- 实际读取范围：模型卡正文、公开提交历史（选段）
- 信息限制与本库备注：未下载权重、未实际运行或视觉验证；现行模型卡可能包含首次发表后的更新，文中标明版本。 提交链接定位日期证据，模型卡内容读取的是当前版，未逐项验证这些参数当日已存在。
- 追溯链接：https://huggingface.co/ElectronGirl/anima-ref-adapter/commit/1202b46fabffea77e0b696242daab1d63965fba6；https://huggingface.co/ElectronGirl/anima-ref-adapter/blob/1202b46fabffea77e0b696242daab1d63965fba6/README.md
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

## 待核线索（不计入正式条目）

### HF-C01

**原分享：** [FLUX.3 Image Klein 官方模型](https://huggingface.co/black-forest-labs/flux-3-image-klein)

**适用方向：** 图像生成｜官方模型待授权读取

**美术风格方向：** 风格待确认（例图未核）

- 原作者：black-forest-labs
- 原始日期：未取得／未说明
- 时间口径：未知
- 日期依据：API createdAt 为 2026-10-13T10:58:40Z，仅证明仓库创建；模型卡及 commits 返回 401。
- 类别：基础模型
- 精确版本：Klein
- 原作者分享要点（本库概述）：搜索发现，未核原文与发布提交。
- 公开资源：模型卡门控
- 作者参数／触发词及边界：未知
- 风格说明与可见范围：待确认
- 风格依据：未取得
- 实际读取范围：公开搜索API；模型卡与提交访问401
- 信息限制与本库备注：创建时间不等于模型公开发布时间。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。
