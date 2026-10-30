# Civitai 模型与版本：近四个月历史分享

感谢原作者的公开分享。本分册为本库摘要整理，保留作者与原文入口；欢迎回原帖阅读完整教程与后续更新。

- 历史时间窗：2026-06-30至本次检索时刻（2026-10-30，北京时间）。
- 收录时间：2026-10-30 09:12:34 +08:00；研究执行：gpt-6.1-terra 子代理。
- 日期有原始依据：21条；待核线索：0条。
- 不同条目的读取深度见详情；日期已核不代表已完整观看或效果验证。
- [总览](README.md) · [覆盖记录](coverage.md) · [当天汇总](../../README.md)

## 分享速查

| 编号／原分享 | 原文／版本日期 | 适用方向（短标注） | 美术风格方向 | 原作者 | 详情与读取范围 |
|---|---|---|---|---|---|
| [CV-01 Anima Text to Image ［ControlNet (3D Pose, Re…](https://civitai.com/models/2742675?modelVersionId=3084634) | 2026-06-30 | Anima·工作流·画师混合｜初版工作流；该资源后续扩展到区域提示与姿态控制。 | —（不涉及具体画风） | Marui_Melons | [公开 API 模型卡正文及指定版本元数据；未读取图片与工作…](civitai.md#cv-01) |
| [CV-02 Anima Text to Image ［ControlNet (3D Pose, Re…](https://civitai.com/models/2742675?modelVersionId=3428980) | 2026-10-25 | Anima·区域控制·工作流｜v1.3 增加 LoRA 高低噪声分段、split condition… | —（不涉及具体画风） | Marui_Melons | [公开 API 模型卡正文及指定版本元数据；未读取图片与工作…](civitai.md#cv-02) |
| [CV-03 Anima Style Explorer & Prompt Workflow ／ Sty…](https://civitai.com/models/2640250?modelVersionId=3106443) | 2026-07-07 | Anima·提示词·画师混合｜风格探索及自动画师提示工作流；页面当前说明模板和节点更新。该版本接口基… | —（不涉及具体画风） | airi_mizuki17 | [公开 API 模型卡正文及指定版本元数据；未读取图片与工作…](civitai.md#cv-03) |
| [CV-04 Expression Sheet - Turn Your OC Into an Emot…](https://civitai.com/models/2748901?modelVersionId=3092279) | 2026-07-03 | Illustrious·表情·角色设定｜作者分享同一角色多表情参考表的概念 LoRA；建议先描述角色并简化设计。 | 动漫表情表｜作者称可输出彩色表情表或黑白线稿；例图未核，体型五官与姿态待确认。 | Booyaka | [公开 API 模型卡正文及指定版本元数据；未读取图片与工作…](civitai.md#cv-04) |
| [CV-05 Anima style: d3u1](https://civitai.com/models/2721188?modelVersionId=3058066) | 2026-07-03 | Anima·画师风格·精修｜作者以 Anima base v1.0 训练，附样图使用参数。 | 画师风格｜作者未充分文字描述外观；例图未核，人物及线条上色待确认。 | N0VA39 | [公开 API 模型卡正文及指定版本元数据；未读取图片与工作…](civitai.md#cv-05) |
| [CV-06 ［Anima & ILL］ Machi/马吉- Artist Style](https://civitai.com/models/2474368?modelVersionId=3134456) | 2026-07-16 | Anima·画师风格·LoRA｜Machi 风格适配器的 Anima 版，作者给出权重范围。 | 画师风格｜作者仅指向画师风格；例图未核，人物体型、五官、线条及色彩未知。 | flyx3 | [公开 API 模型卡正文及指定版本元数据；未读取图片与工作…](civitai.md#cv-06) |
| [CV-07 (Anima Style) Front Lighting (face focus) / …](https://civitai.com/models/2771660?modelVersionId=3120651) | 2026-07-12 | Anima·人物光照·LoRA｜脸部正面补光 LoRA；作者提示较高权重可能改变纹理。 | —（不涉及具体画风） | Akiseki | [公开 API 模型卡正文及指定版本元数据；未读取图片与工作…](civitai.md#cv-07) |
| [CV-08 shitty watercolor style](https://civitai.com/models/1030872?modelVersionId=3112712) | 2026-07-16 | Krea 2·水彩·LoRA｜水彩风格模型的 Krea 2 版，附该版本示范参数。 | 水彩｜依作者命名为水彩风格；例图未核，体型五官、笔触与色彩未知。 | Yofaraway | [公开 API 模型卡正文及指定版本元数据；未读取图片与工作…](civitai.md#cv-08) |
| [CV-09 Workflow for your "ART"](https://civitai.com/models/2730327?modelVersionId=3265977) | 2026-08-26 | Krea 2·工作流·构图控制｜V4 添加 ControlNet 和 moodboard，作者称提升速… | —（不涉及具体画风） | mr1morcellini | [公开 API 模型卡正文及指定版本元数据；未读取图片与工作…](civitai.md#cv-09) |
| [CV-10 Workflow for your "ART"](https://civitai.com/models/2730327?modelVersionId=3369637) | 2026-09-30 | Qwen 2.1·工作流·图像编辑｜V2.7 与 V2.5 为 Qwen 工作流分支；作者称 V2.7 较… | —（不涉及具体画风） | mr1morcellini | [公开 API 模型卡正文及指定版本元数据；未读取图片与工作…](civitai.md#cv-10) |
| [CV-11 Artist Style: Yoneyama Mai/米山舞](https://civitai.com/models/330218?modelVersionId=3225992) | 2026-08-14 | Anima·画师风格·LoRA｜作者的多基座画师风格 LoRA 中的 Anima 1.0 版本。 | 画师风格｜模型卡未具体描述视觉；例图未核，人物及媒介特征未知。 | silvermoong | [公开 API 模型卡正文及指定版本元数据；未读取图片与工作…](civitai.md#cv-11) |
| [CV-12 Artist Style: Rei_17/老累/sanbonzakura](https://civitai.com/models/538535?modelVersionId=3240697) | 2026-08-18 | Anima·画师风格·LoRA｜作者的多基座风格 LoRA 中的 Anima 1.0 版本；页面说明其… | 画师风格｜模型卡未具体描述视觉；例图未核，人物及媒介特征未知。 | silvermoong | [公开 API 模型卡正文及指定版本元数据；未读取图片与工作…](civitai.md#cv-12) |
| [CV-13 Anima style: Habeli](https://civitai.com/models/2949844?modelVersionId=3340766) | 2026-09-20 | Anima·线稿与上色·LoRA｜作者介绍平色与赛璐璐风格 LoRA，并给出基座、建议设置及示例所用模型。 | 平色·赛璐璐｜本例大眼、简化鼻口、粗轮廓与块面阴影 | Habeli | [公开 API 模型卡及指定版本元数据；查看一张公开例图](civitai.md#cv-13) |
| [CV-14 Krea 2 Geometric Composition Style Slider Kr…](https://civitai.com/models/2927993?modelVersionId=3313473) | 2026-09-10 | Krea 2·构图·风格滑块｜概念验证滑块在写实摄影与几何构成两个方向调节，作者提示可能不稳定。 | 摄影→几何构成｜本例由柔焦转硬边块面、五官简化 | baizuobusi | [公开 API 模型卡及指定版本元数据；查看一张公开例图](civitai.md#cv-14) |
| [CV-15 Krea 2 Tilted Composition Control Slider Kre…](https://civitai.com/models/2930423?modelVersionId=3316511) | 2026-09-11 | Krea 2·构图·滑块｜作者通过正负权重在倾斜构图和规整构图之间调整。 | —（不涉及具体画风） | baizuobusi | [公开 API 模型卡正文及指定版本元数据；未读取图片与工作…](civitai.md#cv-15) |
| [CV-16 Expression Slider ／ KREA 2 ［Zero-Train］](https://civitai.com/models/2956697?modelVersionId=3349249) | 2026-09-29 | Krea 2·人物表情·滑块｜作者以闭式求解制作表情强度滑块，提醒较高权重可能损害面部对称。 | —（不涉及具体画风） | Ai_Art_Vision | [公开 API 模型卡正文及指定版本元数据；未读取图片与工作…](civitai.md#cv-16) |
| [CV-17 V67 Artist Style](https://civitai.com/models/2969806?modelVersionId=3365286) | 2026-09-28 | Krea 2·画风·提示词｜作者分享绘画风格 LoRA 和可组合的风格提示方向。 | 油画·超现实｜据作者提示词描述，含厚涂笔触、画布质感和戏剧明暗；例图未核，人物比例… | angelomaiota | [公开 API 模型卡正文及指定版本元数据；未读取图片与工作…](civitai.md#cv-17) |
| [CV-18 Aesthetic composition ／ 美学构图](https://civitai.com/models/2972997?modelVersionId=3428286) | 2026-10-25 | Anima·构图·光影｜作者称 v1 对比 v0.8 改进细节与色调平衡，强调训练结果不一定全… | —（不涉及具体画风） | aiseaK | [公开 API 模型卡正文及指定版本元数据；未读取图片与工作…](civitai.md#cv-18) |
| [CV-19 构图自控 ／ Composition Self-Control - 生图设计 ／ Raw…](https://civitai.com/models/2985382?modelVersionId=3406510) | 2026-10-15 | Anima·构图·LoRA 搭配｜V1 以主次构图词引导设计；作者提醒混合构图会冲突，搭配风格 LoRA… | —（不涉及具体画风） | aiseaK | [公开 API 模型卡正文及指定版本元数据；未读取图片与工作…](civitai.md#cv-19) |
| [CV-20 Anima-style-梦幻柔光（nai5其五）](https://civitai.com/models/3006622?modelVersionId=3411401) | 2026-10-17 | Anima·画风·LoRA 搭配｜作者分享柔光风格 LoRA 单用和多 LoRA 组合的不同提示策略。 | 柔光·日式插画｜作者描述梦幻光影、清新人物线条及柔和粉彩；例图未核，体型五官及表情未… | hardworkingsaltedfish | [公开 API 模型卡正文及指定版本元数据；未读取图片与工作…](civitai.md#cv-20) |
| [CV-21 Portrait2CharRef,头像转角色卡-Qwen Image 2.1](https://civitai.com/models/2954346?modelVersionId=3346353) | 2026-09-21 | Qwen 图像编辑·角色设定·工作流｜作者分享从单张头像编辑生成多视角角色设定图的提示词；可附服装参考图。 | —（不涉及具体画风） | b675051045971 | [公开 API 模型卡正文及指定版本元数据；未读取图片与工作…](civitai.md#cv-21) |

## 条目详解

### CV-01

**原分享：** [Anima Text to Image ［ControlNet (3D Pose, Regional) + High/Low Noise Lora + Split Conditioning + Regional Prompting + Artist Mix + Tiled Diffusion］](https://civitai.com/models/2742675?modelVersionId=3084634)

**适用方向：** Anima·工作流·画师混合｜初版工作流；该资源后续扩展到区域提示与姿态控制。

**美术风格方向：** —（不涉及具体画风）

- 原作者：Marui_Melons
- 原始日期：2026-06-30T11:56:21.660Z
- 时间口径：版本发布
- 日期依据：公开模型 API modelVersions[id=3084634].publishedAt = 2026-06-30T11:56:21.660Z；https://civitai.com/api/v1/models/2742675
- 类别：Workflows
- 精确版本：v1；API baseModel=Anima
- 原作者分享要点（本库概述）：初版工作流；该资源后续扩展到区域提示与姿态控制。
- 公开资源：https://civitai.com/api/v1/models/2742675；https://civitai.com/models/2742675?modelVersionId=3084634
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：不涉及具体画风。
- 风格依据：不涉及具体画风
- 实际读取范围：公开 API 模型卡正文及指定版本元数据；未读取图片与工作流文件
- 信息限制与本库备注：页面原帖以浏览工具打开失败；未看图、未下载配置、未安装或复跑。版本发布日期不等于模型首次创建日期。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### CV-02

**原分享：** [Anima Text to Image ［ControlNet (3D Pose, Regional) + High/Low Noise Lora + Split Conditioning + Regional Prompting + Artist Mix + Tiled Diffusion］](https://civitai.com/models/2742675?modelVersionId=3428980)

**适用方向：** Anima·区域控制·工作流｜v1.3 增加 LoRA 高低噪声分段、split condition…

**美术风格方向：** —（不涉及具体画风）

- 原作者：Marui_Melons
- 原始日期：2026-10-25T13:58:00.474Z
- 时间口径：版本发布
- 日期依据：公开模型 API modelVersions[id=3428980].publishedAt = 2026-10-25T13:58:00.474Z；https://civitai.com/api/v1/models/2742675
- 类别：Workflows
- 精确版本：v1.3；API baseModel=Anima
- 原作者分享要点（本库概述）：v1.3 增加 LoRA 高低噪声分段、split conditioning、3D 姿态及区域控制；作者提醒部分功能组合需自行改接。
- 公开资源：https://civitai.com/api/v1/models/2742675；https://civitai.com/models/2742675?modelVersionId=3428980
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：不涉及具体画风。
- 风格依据：不涉及具体画风
- 实际读取范围：公开 API 模型卡正文及指定版本元数据；未读取图片与工作流文件
- 信息限制与本库备注：页面原帖以浏览工具打开失败；未看图、未下载配置、未安装或复跑。版本发布日期不等于模型首次创建日期。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### CV-03

**原分享：** [Anima Style Explorer & Prompt Workflow ／ Style Blending & Automated Artist Prompting](https://civitai.com/models/2640250?modelVersionId=3106443)

**适用方向：** Anima·提示词·画师混合｜风格探索及自动画师提示工作流；页面当前说明模板和节点更新。该版本接口基…

**美术风格方向：** —（不涉及具体画风）

- 原作者：airi_mizuki17
- 原始日期：2026-07-07T06:48:09.062Z
- 时间口径：版本发布
- 日期依据：公开模型 API modelVersions[id=3106443].publishedAt = 2026-07-07T06:48:09.062Z；https://civitai.com/api/v1/models/2640250
- 类别：Workflows
- 精确版本：workflow-Thinking-v3.5；API baseModel=SD 1.5
- 原作者分享要点（本库概述）：风格探索及自动画师提示工作流；页面当前说明模板和节点更新。该版本接口基座标作 SD 1.5，实际兼容范围需核。
- 公开资源：https://civitai.com/api/v1/models/2640250；https://civitai.com/models/2640250?modelVersionId=3106443
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：不涉及具体画风。
- 风格依据：不涉及具体画风
- 实际读取范围：公开 API 模型卡正文及指定版本元数据；未读取图片与工作流文件
- 信息限制与本库备注：页面原帖以浏览工具打开失败；未看图、未下载配置、未安装或复跑。版本发布日期不等于模型首次创建日期。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### CV-04

**原分享：** [Expression Sheet - Turn Your OC Into an Emotion Reference Sheet (Original)](https://civitai.com/models/2748901?modelVersionId=3092279)

**适用方向：** Illustrious·表情·角色设定｜作者分享同一角色多表情参考表的概念 LoRA；建议先描述角色并简化设计。

**美术风格方向：** 动漫表情表｜作者称可输出彩色表情表或黑白线稿；例图未核，体型五官与姿态待确认。

- 原作者：Booyaka
- 原始日期：2026-07-02T18:15:14.484Z
- 时间口径：版本发布
- 日期依据：公开模型 API modelVersions[id=3092279].publishedAt = 2026-07-02T18:15:14.484Z；https://civitai.com/api/v1/models/2748901
- 类别：LORA
- 精确版本：v1.0；API baseModel=Illustrious
- 原作者分享要点（本库概述）：作者分享同一角色多表情参考表的概念 LoRA；建议先描述角色并简化设计。
- 公开资源：https://civitai.com/api/v1/models/2748901；https://civitai.com/models/2748901?modelVersionId=3092279
- 作者参数／触发词及边界：触发 expsheet；权重 0.7–0.9，推荐 0.8；Euler a、30–32 步、CFG 6–7；示例横向 1216×832，均为作者建议。
- 风格说明与可见范围：作者称可输出彩色表情表或黑白线稿；例图未核，体型五官与姿态待确认。
- 风格依据：作者文字；例图未核
- 实际读取范围：公开 API 模型卡正文及指定版本元数据；未读取图片与工作流文件
- 信息限制与本库备注：页面原帖以浏览工具打开失败；未看图、未下载配置、未安装或复跑。版本发布日期不等于模型首次创建日期。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### CV-05

**原分享：** [Anima style: d3u1](https://civitai.com/models/2721188?modelVersionId=3058066)

**适用方向：** Anima·画师风格·精修｜作者以 Anima base v1.0 训练，附样图使用参数。

**美术风格方向：** 画师风格｜作者未充分文字描述外观；例图未核，人物及线条上色待确认。

- 原作者：N0VA39
- 原始日期：2026-07-02T17:45:29.638Z
- 时间口径：版本发布
- 日期依据：公开模型 API modelVersions[id=3058066].publishedAt = 2026-07-02T17:45:29.638Z；https://civitai.com/api/v1/models/2721188
- 类别：LORA
- 精确版本：v1.4；API baseModel=Anima
- 原作者分享要点（本库概述）：作者以 Anima base v1.0 训练，附样图使用参数。
- 公开资源：https://civitai.com/api/v1/models/2721188；https://civitai.com/models/2721188?modelVersionId=3058066
- 作者参数／触发词及边界：触发 @d3u1；样图 CFG 4–5、er_sde、30–40 步；1024×1536、40 步并 1.25× 高分辨率。
- 风格说明与可见范围：作者未充分文字描述外观；例图未核，人物及线条上色待确认。
- 风格依据：作者文字；例图未核
- 实际读取范围：公开 API 模型卡正文及指定版本元数据；未读取图片与工作流文件
- 信息限制与本库备注：页面原帖以浏览工具打开失败；未看图、未下载配置、未安装或复跑。版本发布日期不等于模型首次创建日期。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### CV-06

**原分享：** [［Anima & ILL］ Machi/马吉- Artist Style](https://civitai.com/models/2474368?modelVersionId=3134456)

**适用方向：** Anima·画师风格·LoRA｜Machi 风格适配器的 Anima 版，作者给出权重范围。

**美术风格方向：** 画师风格｜作者仅指向画师风格；例图未核，人物体型、五官、线条及色彩未知。

- 原作者：flyx3
- 原始日期：2026-07-16T08:32:51.803Z
- 时间口径：版本发布
- 日期依据：公开模型 API modelVersions[id=3134456].publishedAt = 2026-07-16T08:32:51.803Z；https://civitai.com/api/v1/models/2474368
- 类别：LORA
- 精确版本：Anima_v1.0；API baseModel=Anima
- 原作者分享要点（本库概述）：Machi 风格适配器的 Anima 版，作者给出权重范围。
- 公开资源：https://civitai.com/api/v1/models/2474368；https://civitai.com/models/2474368?modelVersionId=3134456
- 作者参数／触发词及边界：触发 Machi Style；作者推荐权重 0.6–1.5。
- 风格说明与可见范围：作者仅指向画师风格；例图未核，人物体型、五官、线条及色彩未知。
- 风格依据：作者文字；例图未核
- 实际读取范围：公开 API 模型卡正文及指定版本元数据；未读取图片与工作流文件
- 信息限制与本库备注：页面原帖以浏览工具打开失败；未看图、未下载配置、未安装或复跑。版本发布日期不等于模型首次创建日期。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### CV-07

**原分享：** [(Anima Style) Front Lighting (face focus) / Flash photo ／ 脸部正面补光 / 闪光灯](https://civitai.com/models/2771660?modelVersionId=3120651)

**适用方向：** Anima·人物光照·LoRA｜脸部正面补光 LoRA；作者提示较高权重可能改变纹理。

**美术风格方向：** —（不涉及具体画风）

- 原作者：Akiseki
- 原始日期：2026-07-11T22:26:39.707Z
- 时间口径：版本发布
- 日期依据：公开模型 API modelVersions[id=3120651].publishedAt = 2026-07-11T22:26:39.707Z；https://civitai.com/api/v1/models/2771660
- 类别：LORA
- 精确版本：v1.0；API baseModel=Anima
- 原作者分享要点（本库概述）：脸部正面补光 LoRA；作者提示较高权重可能改变纹理。
- 公开资源：https://civitai.com/api/v1/models/2771660；https://civitai.com/models/2771660?modelVersionId=3120651
- 作者参数／触发词及边界：无必需触发词；作者建议必要时降低权重。
- 风格说明与可见范围：不涉及具体画风。
- 风格依据：不涉及具体画风
- 实际读取范围：公开 API 模型卡正文及指定版本元数据；未读取图片与工作流文件
- 信息限制与本库备注：页面原帖以浏览工具打开失败；未看图、未下载配置、未安装或复跑。版本发布日期不等于模型首次创建日期。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### CV-08

**原分享：** [shitty watercolor style](https://civitai.com/models/1030872?modelVersionId=3112712)

**适用方向：** Krea 2·水彩·LoRA｜水彩风格模型的 Krea 2 版，附该版本示范参数。

**美术风格方向：** 水彩｜依作者命名为水彩风格；例图未核，体型五官、笔触与色彩未知。

- 原作者：Yofaraway
- 原始日期：2026-07-16T10:16:03.737Z
- 时间口径：版本发布
- 日期依据：公开模型 API modelVersions[id=3112712].publishedAt = 2026-07-16T10:16:03.737Z；https://civitai.com/api/v1/models/1030872
- 类别：LORA
- 精确版本：Krea2 v1；API baseModel=Krea 2
- 原作者分享要点（本库概述）：水彩风格模型的 Krea 2 版，附该版本示范参数。
- 公开资源：https://civitai.com/api/v1/models/1030872；https://civitai.com/models/1030872?modelVersionId=3112712
- 作者参数／触发词及边界：示范：Turbo、768×1152、Euler/simple、10 步、CFG 1、LoRA 1。
- 风格说明与可见范围：依作者命名为水彩风格；例图未核，体型五官、笔触与色彩未知。
- 风格依据：作者文字；例图未核
- 实际读取范围：公开 API 模型卡正文及指定版本元数据；未读取图片与工作流文件
- 信息限制与本库备注：页面原帖以浏览工具打开失败；未看图、未下载配置、未安装或复跑。版本发布日期不等于模型首次创建日期。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### CV-09

**原分享：** [Workflow for your "ART"](https://civitai.com/models/2730327?modelVersionId=3265977)

**适用方向：** Krea 2·工作流·构图控制｜V4 添加 ControlNet 和 moodboard，作者称提升速…

**美术风格方向：** —（不涉及具体画风）

- 原作者：mr1morcellini
- 原始日期：2026-08-25T17:52:07.775Z
- 时间口径：版本发布
- 日期依据：公开模型 API modelVersions[id=3265977].publishedAt = 2026-08-25T17:52:07.775Z；https://civitai.com/api/v1/models/2730327
- 类别：Workflows
- 精确版本：Krea 2 V4-Control；API baseModel=Krea 2
- 原作者分享要点（本库概述）：V4 添加 ControlNet 和 moodboard，作者称提升速度并增加真实感开关；效果为作者判断。
- 公开资源：https://civitai.com/api/v1/models/2730327；https://civitai.com/models/2730327?modelVersionId=3265977
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：不涉及具体画风。
- 风格依据：不涉及具体画风
- 实际读取范围：公开 API 模型卡正文及指定版本元数据；未读取图片与工作流文件
- 信息限制与本库备注：页面原帖以浏览工具打开失败；未看图、未下载配置、未安装或复跑。版本发布日期不等于模型首次创建日期。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### CV-10

**原分享：** [Workflow for your "ART"](https://civitai.com/models/2730327?modelVersionId=3369637)

**适用方向：** Qwen 2.1·工作流·图像编辑｜V2.7 与 V2.5 为 Qwen 工作流分支；作者称 V2.7 较…

**美术风格方向：** —（不涉及具体画风）

- 原作者：mr1morcellini
- 原始日期：2026-09-29T18:57:45.895Z
- 时间口径：版本发布
- 日期依据：公开模型 API modelVersions[id=3369637].publishedAt = 2026-09-29T18:57:45.895Z；https://civitai.com/api/v1/models/2730327
- 类别：Workflows
- 精确版本：Qwen 2.1 V2.7；API baseModel=Qwen 2.1
- 原作者分享要点（本库概述）：V2.7 与 V2.5 为 Qwen 工作流分支；作者称 V2.7 较慢并建议后处理时使用 4k 放大。
- 公开资源：https://civitai.com/api/v1/models/2730327；https://civitai.com/models/2730327?modelVersionId=3369637
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：不涉及具体画风。
- 风格依据：不涉及具体画风
- 实际读取范围：公开 API 模型卡正文及指定版本元数据；未读取图片与工作流文件
- 信息限制与本库备注：页面原帖以浏览工具打开失败；未看图、未下载配置、未安装或复跑。版本发布日期不等于模型首次创建日期。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### CV-11

**原分享：** [Artist Style: Yoneyama Mai/米山舞](https://civitai.com/models/330218?modelVersionId=3225992)

**适用方向：** Anima·画师风格·LoRA｜作者的多基座画师风格 LoRA 中的 Anima 1.0 版本。

**美术风格方向：** 画师风格｜模型卡未具体描述视觉；例图未核，人物及媒介特征未知。

- 原作者：silvermoong
- 原始日期：2026-08-13T20:49:15.461Z
- 时间口径：版本发布
- 日期依据：公开模型 API modelVersions[id=3225992].publishedAt = 2026-08-13T20:49:15.461Z；https://civitai.com/api/v1/models/330218
- 类别：LORA
- 精确版本：v5.2 [Anima1.0]；API baseModel=Anima
- 原作者分享要点（本库概述）：作者的多基座画师风格 LoRA 中的 Anima 1.0 版本。
- 公开资源：https://civitai.com/api/v1/models/330218；https://civitai.com/models/330218?modelVersionId=3225992
- 作者参数／触发词及边界：未列触发词或同图参数。
- 风格说明与可见范围：模型卡未具体描述视觉；例图未核，人物及媒介特征未知。
- 风格依据：作者文字；例图未核
- 实际读取范围：公开 API 模型卡正文及指定版本元数据；未读取图片与工作流文件
- 信息限制与本库备注：页面原帖以浏览工具打开失败；未看图、未下载配置、未安装或复跑。版本发布日期不等于模型首次创建日期。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### CV-12

**原分享：** [Artist Style: Rei_17/老累/sanbonzakura](https://civitai.com/models/538535?modelVersionId=3240697)

**适用方向：** Anima·画师风格·LoRA｜作者的多基座风格 LoRA 中的 Anima 1.0 版本；页面说明其…

**美术风格方向：** 画师风格｜模型卡未具体描述视觉；例图未核，人物及媒介特征未知。

- 原作者：silvermoong
- 原始日期：2026-08-18T03:54:57.936Z
- 时间口径：版本发布
- 日期依据：公开模型 API modelVersions[id=3240697].publishedAt = 2026-08-18T03:54:57.936Z；https://civitai.com/api/v1/models/538535
- 类别：LORA
- 精确版本：v5.2 [Anima1.0]；API baseModel=Anima
- 原作者分享要点（本库概述）：作者的多基座风格 LoRA 中的 Anima 1.0 版本；页面说明其版本命名方法。
- 公开资源：https://civitai.com/api/v1/models/538535；https://civitai.com/models/538535?modelVersionId=3240697
- 作者参数／触发词及边界：未列触发词或同图参数。
- 风格说明与可见范围：模型卡未具体描述视觉；例图未核，人物及媒介特征未知。
- 风格依据：作者文字；例图未核
- 实际读取范围：公开 API 模型卡正文及指定版本元数据；未读取图片与工作流文件
- 信息限制与本库备注：页面原帖以浏览工具打开失败；未看图、未下载配置、未安装或复跑。版本发布日期不等于模型首次创建日期。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### CV-13

**原分享：** [Anima style: Habeli](https://civitai.com/models/2949844?modelVersionId=3340766)

**适用方向：** Anima·线稿与上色·LoRA｜作者介绍平色与赛璐璐风格 LoRA，并给出基座、建议设置及示例所用模型。

**美术风格方向：** 平色·赛璐璐｜本例大眼、简化鼻口、粗轮廓与块面阴影

- 原作者：Habeli
- 原始日期：2026-09-19T19:43:47.335Z
- 时间口径：版本发布
- 日期依据：公开模型 API modelVersions[id=3340766].publishedAt = 2026-09-19T19:43:47.335Z；https://civitai.com/api/v1/models/2949844
- 类别：LORA
- 精确版本：v4.0；API baseModel=Anima
- 原作者分享要点（本库概述）：作者介绍平色与赛璐璐风格 LoRA，并给出基座、建议设置及示例所用模型。
- 公开资源：https://civitai.com/api/v1/models/2949844；https://civitai.com/models/2949844?modelVersionId=3340766
- 作者参数／触发词及边界：触发 habeli_flat_style；推荐权重 0.7–0.9；样图 anima_aestheticV11、0.85；其余为作者建议：24–36 步、CFG 4.5–6.5、DPM++ 2M。
- 风格说明与可见范围：作者文字：粗清线条、平色与克制阴影。本库查看一张双人分栏半身例图：两人均大眼、鼻口简化，左侧直视、右侧眨眼，黑色粗轮廓与块面阴影，紫红衣色；未见全身体型。
- 风格依据：作者描述及本库实际查看单张公开例图；不推广为稳定画风
- 实际读取范围：公开 API 模型卡及指定版本元数据；查看一张公开例图
- 信息限制与本库备注：未下载工作流、安装或复跑；单张例图不能说明稳定性。版本发布时间不等于模型首次创建时间。
- 追溯链接：https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/cc1a7c79-8e53-4732-8b76-32aa9acd04ac/original=true/143244774.jpeg
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### CV-14

**原分享：** [Krea 2 Geometric Composition Style Slider Krea 2 几何构成风格滑块](https://civitai.com/models/2927993?modelVersionId=3313473)

**适用方向：** Krea 2·构图·风格滑块｜概念验证滑块在写实摄影与几何构成两个方向调节，作者提示可能不稳定。

**美术风格方向：** 摄影→几何构成｜本例由柔焦转硬边块面、五官简化

- 原作者：baizuobusi
- 原始日期：2026-09-10T10:36:41.179Z
- 时间口径：版本发布
- 日期依据：公开模型 API modelVersions[id=3313473].publishedAt = 2026-09-10T10:36:41.179Z；https://civitai.com/api/v1/models/2927993
- 类别：LORA
- 精确版本：v1.0；API baseModel=Krea 2
- 原作者分享要点（本库概述）：概念验证滑块在写实摄影与几何构成两个方向调节，作者提示可能不稳定。
- 公开资源：https://civitai.com/api/v1/models/2927993；https://civitai.com/models/2927993?modelVersionId=3313473
- 作者参数／触发词及边界：样图测试权重 -10 至 30，作者建议从 10 开始；无必需触发词。
- 风格说明与可见范围：作者描述写实至几何构成滑块。本库查看一张五格权重示范：左侧柔焦摄影，中间逐步转绘画，右侧呈硬边块面和简化几何；同一取景人物低头嗅花，五官随风格变形，身体大部未见。
- 风格依据：作者描述及本库实际查看单张公开例图；不推广为稳定画风
- 实际读取范围：公开 API 模型卡及指定版本元数据；查看一张公开例图
- 信息限制与本库备注：未下载工作流、安装或复跑；单张例图不能说明稳定性。版本发布时间不等于模型首次创建时间。
- 追溯链接：https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/1e1bb891-7ab1-4fb1-bf14-556da49ff8c3/original=true/142365085.jpeg
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### CV-15

**原分享：** [Krea 2 Tilted Composition Control Slider Krea 2 倾斜构图控制滑块](https://civitai.com/models/2930423?modelVersionId=3316511)

**适用方向：** Krea 2·构图·滑块｜作者通过正负权重在倾斜构图和规整构图之间调整。

**美术风格方向：** —（不涉及具体画风）

- 原作者：baizuobusi
- 原始日期：2026-09-11T12:24:29.046Z
- 时间口径：版本发布
- 日期依据：公开模型 API modelVersions[id=3316511].publishedAt = 2026-09-11T12:24:29.046Z；https://civitai.com/api/v1/models/2930423
- 类别：LORA
- 精确版本：v1.0；API baseModel=Krea 2
- 原作者分享要点（本库概述）：作者通过正负权重在倾斜构图和规整构图之间调整。
- 公开资源：https://civitai.com/api/v1/models/2930423；https://civitai.com/models/2930423?modelVersionId=3316511
- 作者参数／触发词及边界：作者说明正权重趋向倾斜，负权重趋向规整；未列具体建议权重。
- 风格说明与可见范围：不涉及具体画风。
- 风格依据：不涉及具体画风
- 实际读取范围：公开 API 模型卡正文及指定版本元数据；未读取图片与工作流文件
- 信息限制与本库备注：页面原帖以浏览工具打开失败；未看图、未下载配置、未安装或复跑。版本发布日期不等于模型首次创建日期。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### CV-16

**原分享：** [Expression Slider ／ KREA 2 ［Zero-Train］](https://civitai.com/models/2956697?modelVersionId=3349249)

**适用方向：** Krea 2·人物表情·滑块｜作者以闭式求解制作表情强度滑块，提醒较高权重可能损害面部对称。

**美术风格方向：** —（不涉及具体画风）

- 原作者：Ai_Art_Vision
- 原始日期：2026-09-29T14:12:13.788Z
- 时间口径：版本发布
- 日期依据：公开模型 API modelVersions[id=3349249].publishedAt = 2026-09-29T14:12:13.788Z；https://civitai.com/api/v1/models/2956697
- 类别：LORA
- 精确版本：V1；API baseModel=Krea 2
- 原作者分享要点（本库概述）：作者以闭式求解制作表情强度滑块，提醒较高权重可能损害面部对称。
- 公开资源：https://civitai.com/api/v1/models/2956697；https://civitai.com/models/2956697?modelVersionId=3349249
- 作者参数／触发词及边界：作者建议 +1.0–1.5 自然增强，+1.5–2.0 加强表情；大于 +2 可能失真。
- 风格说明与可见范围：不涉及具体画风。
- 风格依据：不涉及具体画风
- 实际读取范围：公开 API 模型卡正文及指定版本元数据；未读取图片与工作流文件
- 信息限制与本库备注：页面原帖以浏览工具打开失败；未看图、未下载配置、未安装或复跑。版本发布日期不等于模型首次创建日期。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### CV-17

**原分享：** [V67 Artist Style](https://civitai.com/models/2969806?modelVersionId=3365286)

**适用方向：** Krea 2·画风·提示词｜作者分享绘画风格 LoRA 和可组合的风格提示方向。

**美术风格方向：** 油画·超现实｜据作者提示词描述，含厚涂笔触、画布质感和戏剧明暗；例图未核，人物比例…

- 原作者：angelomaiota
- 原始日期：2026-09-28T07:11:26.033Z
- 时间口径：版本发布
- 日期依据：公开模型 API modelVersions[id=3365286].publishedAt = 2026-09-28T07:11:26.033Z；https://civitai.com/api/v1/models/2969806
- 类别：LORA
- 精确版本：V1 KREA-2；API baseModel=Krea 2
- 原作者分享要点（本库概述）：作者分享绘画风格 LoRA 和可组合的风格提示方向。
- 公开资源：https://civitai.com/api/v1/models/2969806；https://civitai.com/models/2969806?modelVersionId=3365286
- 作者参数／触发词及边界：作者建议风格提示置于提示词开头；具体长提示词见原模型卡。
- 风格说明与可见范围：据作者提示词描述，含厚涂笔触、画布质感和戏剧明暗；例图未核，人物比例、五官及表情未知。
- 风格依据：作者文字；例图未核
- 实际读取范围：公开 API 模型卡正文及指定版本元数据；未读取图片与工作流文件
- 信息限制与本库备注：页面原帖以浏览工具打开失败；未看图、未下载配置、未安装或复跑。版本发布日期不等于模型首次创建日期。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### CV-18

**原分享：** [Aesthetic composition ／ 美学构图](https://civitai.com/models/2972997?modelVersionId=3428286)

**适用方向：** Anima·构图·光影｜作者称 v1 对比 v0.8 改进细节与色调平衡，强调训练结果不一定全…

**美术风格方向：** —（不涉及具体画风）

- 原作者：aiseaK
- 原始日期：2026-10-25T09:23:48.894Z
- 时间口径：版本发布
- 日期依据：公开模型 API modelVersions[id=3428286].publishedAt = 2026-10-25T09:23:48.894Z；https://civitai.com/api/v1/models/2972997
- 类别：LORA
- 精确版本：anima base v1.0；API baseModel=Anima
- 原作者分享要点（本库概述）：作者称 v1 对比 v0.8 改进细节与色调平衡，强调训练结果不一定全面优于基座。
- 公开资源：https://civitai.com/api/v1/models/2972997；https://civitai.com/models/2972997?modelVersionId=3428286
- 作者参数／触发词及边界：作者测试权重 1.0；正向词 masterpiece, best quality, very aesthetic。
- 风格说明与可见范围：不涉及具体画风。
- 风格依据：不涉及具体画风
- 实际读取范围：公开 API 模型卡正文及指定版本元数据；未读取图片与工作流文件
- 信息限制与本库备注：页面原帖以浏览工具打开失败；未看图、未下载配置、未安装或复跑。版本发布日期不等于模型首次创建日期。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### CV-19

**原分享：** [构图自控 ／ Composition Self-Control - 生图设计 ／ Raw image design](https://civitai.com/models/2985382?modelVersionId=3406510)

**适用方向：** Anima·构图·LoRA 搭配｜V1 以主次构图词引导设计；作者提醒混合构图会冲突，搭配风格 LoRA…

**美术风格方向：** —（不涉及具体画风）

- 原作者：aiseaK
- 原始日期：2026-10-15T09:11:35.377Z
- 时间口径：版本发布
- 日期依据：公开模型 API modelVersions[id=3406510].publishedAt = 2026-10-15T09:11:35.377Z；https://civitai.com/api/v1/models/2985382
- 类别：LORA
- 精确版本：anima-base V1；API baseModel=Anima
- 原作者分享要点（本库概述）：V1 以主次构图词引导设计；作者提醒混合构图会冲突，搭配风格 LoRA 可能削弱控制。
- 公开资源：https://civitai.com/api/v1/models/2985382；https://civitai.com/models/2985382?modelVersionId=3406510
- 作者参数／触发词及边界：触发 cmpctrl；其后先写主构图，再写次构图；V1 增加 horizontal split composition。
- 风格说明与可见范围：不涉及具体画风。
- 风格依据：不涉及具体画风
- 实际读取范围：公开 API 模型卡正文及指定版本元数据；未读取图片与工作流文件
- 信息限制与本库备注：页面原帖以浏览工具打开失败；未看图、未下载配置、未安装或复跑。版本发布日期不等于模型首次创建日期。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### CV-20

**原分享：** [Anima-style-梦幻柔光（nai5其五）](https://civitai.com/models/3006622?modelVersionId=3411401)

**适用方向：** Anima·画风·LoRA 搭配｜作者分享柔光风格 LoRA 单用和多 LoRA 组合的不同提示策略。

**美术风格方向：** 柔光·日式插画｜作者描述梦幻光影、清新人物线条及柔和粉彩；例图未核，体型五官及表情未…

- 原作者：hardworkingsaltedfish
- 原始日期：2026-10-17T14:14:00.468Z
- 时间口径：版本发布
- 日期依据：公开模型 API modelVersions[id=3411401].publishedAt = 2026-10-17T14:14:00.468Z；https://civitai.com/api/v1/models/3006622
- 类别：LORA
- 精确版本：v1.0；API baseModel=Anima
- 原作者分享要点（本库概述）：作者分享柔光风格 LoRA 单用和多 LoRA 组合的不同提示策略。
- 公开资源：https://civitai.com/api/v1/models/3006622；https://civitai.com/models/3006622?modelVersionId=3411401
- 作者参数／触发词及边界：触发 @softglow_anime；作者建议单用约 1.2，多 LoRA 约 0.7，并提示避免加速 LoRA。
- 风格说明与可见范围：作者描述梦幻光影、清新人物线条及柔和粉彩；例图未核，体型五官及表情未知。
- 风格依据：作者文字；例图未核
- 实际读取范围：公开 API 模型卡正文及指定版本元数据；未读取图片与工作流文件
- 信息限制与本库备注：页面原帖以浏览工具打开失败；未看图、未下载配置、未安装或复跑。版本发布日期不等于模型首次创建日期。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### CV-21

**原分享：** [Portrait2CharRef,头像转角色卡-Qwen Image 2.1](https://civitai.com/models/2954346?modelVersionId=3346353)

**适用方向：** Qwen 图像编辑·角色设定·工作流｜作者分享从单张头像编辑生成多视角角色设定图的提示词；可附服装参考图。

**美术风格方向：** —（不涉及具体画风）

- 原作者：b675051045971
- 原始日期：2026-09-21T15:21:39.512Z
- 时间口径：版本发布
- 日期依据：公开模型 API modelVersions[id=3346353].publishedAt = 2026-09-21T15:21:39.512Z；https://civitai.com/api/v1/models/2954346
- 类别：LORA
- 精确版本：v1.0；API baseModel=Qwen 2
- 原作者分享要点（本库概述）：作者分享从单张头像编辑生成多视角角色设定图的提示词；可附服装参考图。
- 公开资源：https://civitai.com/api/v1/models/2954346；https://civitai.com/models/2954346?modelVersionId=3346353
- 作者参数／触发词及边界：作者建议图像比例 3:2；完整中文提示见原卡。
- 风格说明与可见范围：不涉及具体画风。
- 风格依据：不涉及具体画风
- 实际读取范围：公开 API 模型卡正文及指定版本元数据；未读取图片与工作流文件
- 信息限制与本库备注：页面原帖以浏览工具打开失败；未看图、未下载配置、未安装或复跑。版本发布日期不等于模型首次创建日期。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。
