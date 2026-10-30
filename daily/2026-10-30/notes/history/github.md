# GitHub：近四个月历史分享

感谢原作者的公开分享。本分册为本库摘要整理，保留作者与原文入口；欢迎回原帖阅读完整教程与后续更新。

- 历史时间窗：2026-06-30至本次检索时刻（2026-10-30，北京时间）。
- 收录时间：2026-10-30 09:12:34 +08:00；研究执行：gpt-6.1-terra 子代理。
- 日期有原始依据：17条；待核线索：2条。
- 不同条目的读取深度见详情；日期已核不代表已完整观看或效果验证。
- [总览](README.md) · [覆盖记录](coverage.md) · [当天汇总](../../README.md)

## 分享速查

| 编号／原分享 | 原文／版本日期 | 适用方向（短标注） | 美术风格方向 | 原作者 | 详情与读取范围 |
|---|---|---|---|---|---|
| [GH-01 Anima Artist Mixer：post-adapter 混合与锚点](https://github.com/An1X3R/Anima-Artist-Mixer/commit/8e6c780cb1fd2cb3532efaa623ad5ae510b5a2d5) | 2026-07-27 | 画师混合·Anima｜26.8.1 已加入 post-LLMAdapter 多画师混合；26… | 风格参考｜作者涉及风格控制；例图未核，人物比例、五官、表情、姿态、线条及光色材… | An1X3R | [仓库历史 README 及提交列表；部分条目参考当前 RE…](github.md#gh-01) |
| [GH-02 Artist Mixer Forge：画师对照与诊断工作流](https://github.com/Rinne414/Anima-Artist-Mixer-Forge/commit/4bae5f5a95937bc32c4f07746f0e7a75cebcb90d) | 2026-07-17 | 画师混合·风格分析｜原项目的社区 fork 增加建议组合、画师相似性和对照图诊断；可对比单… | 风格参考｜作者涉及风格控制；例图未核，人物比例、五官、表情、姿态、线条及光色材… | Rinne414 | [仓库历史 README 及提交列表；部分条目参考当前 RE…](github.md#gh-02) |
| [GH-03 Anima Regional 0.3.3：人物与场景分区](https://github.com/An1X3R/ComfyUI-Anima-Regional/commit/bcaae88b2053ab470794c35ffd4ebfd08ff45561) | 2026-07-31 | 多主体·Anima·区域控制｜分别组织角色条件与空间归属，0.3.3 加入可选 shared_del… | —（不涉及具体画风） | An1X3R | [仓库历史 README 及提交列表；部分条目参考当前 RE…](github.md#gh-03) |
| [GH-04 Krea 2 单次采样区域提示与分区 LoRA](https://github.com/januspluto/ComfyUI-Krea2-Regional/commit/23f937b07e37920e6eec34482ddc6fe7a26aef2a) | 2026-07-08 | 多主体·区域 LoRA·Krea 2｜基于联合注意力掩码把不同提示词和 LoRA 路由到不同区域，使用共享底… | —（不涉及具体画风） | januspluto | [仓库历史 README 及提交列表；部分条目参考当前 RE…](github.md#gh-04) |
| [GH-05 Krea 2 Control LoRA 与结构图](https://github.com/facok/comfyui-krea2-controlnet/commit/5e10d80c018856c3991275714b32e63ba495ffbc) | 2026-07-04 | 结构控制·Control LoRA·Krea 2｜加载 Krea 2 Control LoRA，将由 VAE 编码的控制… | —（不涉及具体画风） | facok | [仓库历史 README 及提交列表；部分条目参考当前 RE…](github.md#gh-05) |
| [GH-06 FLUX.2 ControlNet：组合与图像控制](https://github.com/Damkohler/JLC-Flux2-ControlNet/commit/406e850c29f0db16d721837add26b284c899a433) | 2026-07-07 | 结构控制·FLUX.2｜FLUX.2 原生节点实现并提供多 ControlNet 组合；随后 … | —（不涉及具体画风） | Damkohler | [仓库历史 README 及提交列表；部分条目参考当前 RE…](github.md#gh-06) |
| [GH-07 Krea2 StyleBridge：内容提示和参考画风分离](https://github.com/sakugetu/comfyui-krea2-stylebridge-lmstudio/commit/23470d5f93c5130242bd9a328c11c8db9e7eed80) | 2026-07-05 | 风格参考·提示词自动化·Krea 2｜示范用 LM Studio 组织文字及内容参考，再通过 Untwist… | 风格参考｜作者涉及风格控制；例图未核，人物比例、五官、表情、姿态、线条及光色材… | sakugetu | [仓库历史 README 及提交列表；部分条目参考当前 RE…](github.md#gh-07) |
| [GH-08 Clio 风格词库与同主体画廊对照](https://github.com/lumenastrum/clio-style-preview/commit/41b6baf6bb226c4bf4f8e06da11e2c490a50c8dd) | 2026-07-20 | 画风分析·提示词·Krea 2｜首版提供 281 个长篇风格描述及同一主体的画廊、滑块对照，便于浏览和… | 风格参考｜作者涉及风格控制；例图未核，人物比例、五官、表情、姿态、线条及光色材… | lumenastrum | [仓库历史 README 及提交列表；部分条目参考当前 RE…](github.md#gh-08) |
| [GH-09 Krea2 Prompt Styler：风格与摄影参数](https://github.com/Gothdir/ComfyUI-Krea2-PromptStyler/commit/5c83169cdd3316a8a77116deea6d876f0d40eeaa) | 2026-07-24 | 提示词组织·摄影风格·Krea 2｜为 Krea 2／Flux 提供按类别选择的风格和焦距、光圈、镜头、胶… | 风格参考｜作者涉及风格控制；例图未核，人物比例、五官、表情、姿态、线条及光色材… | Gothdir | [仓库历史 README 及提交列表；部分条目参考当前 RE…](github.md#gh-09) |
| [GH-10 HiDream-O1 双 ControlNet 细节工作流](https://github.com/biosynthart/comfyui-HiDream-O1-Detailer/commit/77f2aafb94b8a10737d209513bfbaf42288e23ac) | 2026-07-06 | 采样精修·结构控制｜作者公开从 HiDream-O1 图像转至 Z-Image Turbo… | 风格参考｜作者涉及风格控制；例图未核，人物比例、五官、表情、姿态、线条及光色材… | biosynthart | [仓库历史 README 及提交列表；部分条目参考当前 RE…](github.md#gh-10) |
| [GH-11 MiniMax H3 Image Studio 静帧工作流](https://github.com/astropuzzo/ComfyUI-MiniMax-H3-Image-Studio/commit/6312094f3ef6ba5688a5f979a9f6d80011f93207) | 2026-08-03 | 图像生成·参考编辑·MiniMax H3｜针对 H3 静帧生成和参考图编辑组织条件、采样、分辨率及帧评分，附面向… | —（不涉及具体画风） | astropuzzo | [仓库历史 README 及提交列表；部分条目参考当前 RE…](github.md#gh-11) |
| [GH-12 Anima Remap：跨 28／40／52 层 LoRA 和模型合并](https://github.com/shin131002/ComfyUI-Anima-Remap/commit/a5d7b07aba96cdaaca7f3179d465548f3e8e9401) | 2026-08-24 | Anima·LoRA 兼容·模型合并｜按模型层索引重映射在不同 Anima 代际之间应用 LoRA 和合并模… | —（不涉及具体画风） | shin131002 | [仓库历史 README 及提交列表；部分条目参考当前 RE…](github.md#gh-12) |
| [GH-13 Anima LoRA 与 ControlNet 跨层数映射](https://github.com/INuBq8/ComfyUI-Anima-LoRA-ControlNet-Patch/commit/db28dfbd8e37a1f954611e44245791f4501bb785) | 2026-09-09 | Anima·ControlNet·LoRA 兼容｜统一处理 Anima 28、40、52 层模型间双向 LoRA 与 C… | —（不涉及具体画风） | INuBq8 | [仓库历史 README 及提交列表；部分条目参考当前 RE…](github.md#gh-13) |
| [GH-14 Visual Grid Regional Prompt 区域构图文本](https://github.com/bada-ya/ComfyUI-Visual-Regional-Prompt/commit/9e3f89f078a399a31e55e92aedb18117d6039d65) | 2026-09-01 | 构图·多主体·提示词组织｜通过网格框选区域并逐区填写描述，输出自然语言、结构化标签或 JSON … | —（不涉及具体画风） | bada-ya | [仓库历史 README 及提交列表；部分条目参考当前 RE…](github.md#gh-14) |
| [GH-15 Qwen Image 2.1 提示词改写节点](https://github.com/benjiyaya/ComfyUI-Qwen-Image-2.1-Prompt-Enhancer/commit/947468034a2b43d0a54321d31178dd058c68ecaa) | 2026-09-21 | 提示词自动化·图像编辑·Qwen｜作者提供 Qwen Image 2.1 的文生图与图像编辑提示词改写节… | —（不涉及具体画风） | benjiyaya | [仓库历史 README 及提交列表；部分条目参考当前 RE…](github.md#gh-15) |
| [GH-16 Qwen Image 2.1 Fun Union 多种结构控制](https://github.com/T8mars/Comfyui-Qwen-Image-2.1-Fun-Controlnet-Union-T8/commit/cdd06a42d51afeeff9448335dcca1a5e5827df5e) | 2026-09-25 | 结构控制·ControlNet·Qwen｜发布 Qwen Image 2.1 Union 节点与工作流，覆盖边缘… | —（不涉及具体画风） | T8mars | [仓库历史 README 及提交列表；部分条目参考当前 RE…](github.md#gh-16) |
| [GH-17 LuCiD VRP 可视化编辑与区域布局](https://github.com/EBEBEEBE/comfyui-lucid-vrp/commit/5c4e9f351a7e686b17325aa39bdc6fd7b58a5103) | 2026-10-29 | 区域控制·图像编辑·多主体｜公开 beta 源码，提供画布编辑、Anima 区域提示和 MOSS-… | —（不涉及具体画风） | EBEBEEBE | [仓库历史 README 及提交列表；部分条目参考当前 RE…](github.md#gh-17) |

## 条目详解

### GH-01

**原分享：** [Anima Artist Mixer：post-adapter 混合与锚点](https://github.com/An1X3R/Anima-Artist-Mixer/commit/8e6c780cb1fd2cb3532efaa623ad5ae510b5a2d5)

**适用方向：** 画师混合·Anima｜26.8.1 已加入 post-LLMAdapter 多画师混合；26…

**美术风格方向：** 风格参考｜作者涉及风格控制；例图未核，人物比例、五官、表情、姿态、线条及光色材…

- 原作者：An1X3R
- 原始日期：2026-07-26T21:25:23Z
- 时间口径：Git 提交作者时间（UTC）；非仓库创建时间
- 日期依据：GitHub commits API: commit.author.date=2026-07-26T21:25:23Z; commit.committer.date=2026-07-26T21:25:23Z; 完整 SHA 8e6c780cb1fd2cb3532efaa623ad5ae510b5a2d5; 提交信息：Release 26.8.2 automatic adapter anchor seeds。
- 类别：画师混合
- 精确版本：26.8.2
- 原作者分享要点（本库概述）：26.8.1 已加入 post-LLMAdapter 多画师混合；26.8.2 新增可自动生成或固定的 Adapter Q 锚点种子，以控制跨次复用。
- 公开资源：https://github.com/An1X3R/Anima-Artist-Mixer；https://github.com/An1X3R/Anima-Artist-Mixer/commit/8e6c780cb1fd2cb3532efaa623ad5ae510b5a2d5；https://github.com/An1X3R/Anima-Artist-Mixer/blob/8e6c780cb1fd2cb3532efaa623ad5ae510b5a2d5/README.md；https://github.com/An1X3R/Anima-Artist-Mixer/commit/572b773b27191e599c212daaec576112f077f52e
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：作者涉及风格控制；例图未核，人物比例、五官、表情、姿态、线条及光色材质待确认。
- 风格依据：作者文字，未实际看图
- 实际读取范围：仓库历史 README 及提交列表；部分条目参考当前 README；未运行
- 信息限制与本库备注：26.8.2 是作者版本号，不是日期；该提交作者和提交者时间均为 2026-07-26 UTC。仓库始于 5 月；后适配器混合首次属于 26.8.1，26.8.2 增量是自动锚点种子。性能和视觉效果未实测。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### GH-02

**原分享：** [Artist Mixer Forge：画师对照与诊断工作流](https://github.com/Rinne414/Anima-Artist-Mixer-Forge/commit/4bae5f5a95937bc32c4f07746f0e7a75cebcb90d)

**适用方向：** 画师混合·风格分析｜原项目的社区 fork 增加建议组合、画师相似性和对照图诊断；可对比单…

**美术风格方向：** 风格参考｜作者涉及风格控制；例图未核，人物比例、五官、表情、姿态、线条及光色材…

- 原作者：Rinne414
- 原始日期：2026-07-17T12:28:59Z
- 时间口径：Git 提交作者时间（UTC）；非仓库创建时间
- 日期依据：GitHub commits API: commit.author.date=2026-07-17T12:28:59Z; commit.committer.date=2026-07-17T12:28:59Z; 完整 SHA 4bae5f5a95937bc32c4f07746f0e7a75cebcb90d; 提交信息：feat: diagnostics close the loop - suggested chain, contact sheet, similarity。
- 类别：画师混合
- 精确版本：未知／见对应提交
- 原作者分享要点（本库概述）：原项目的社区 fork 增加建议组合、画师相似性和对照图诊断；可对比单画师与混合后的差异。
- 公开资源：https://github.com/Rinne414/Anima-Artist-Mixer-Forge；https://github.com/Rinne414/Anima-Artist-Mixer-Forge/commit/4bae5f5a95937bc32c4f07746f0e7a75cebcb90d；https://github.com/Rinne414/Anima-Artist-Mixer-Forge/blob/4bae5f5a95937bc32c4f07746f0e7a75cebcb90d/README.md；https://github.com/Rinne414/Anima-Artist-Mixer-Forge/blob/4bae5f5a95937bc32c4f07746f0e7a75cebcb90d/CHANGELOG.md
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：作者涉及风格控制；例图未核，人物比例、五官、表情、姿态、线条及光色材质待确认。
- 风格依据：作者文字，未实际看图
- 实际读取范围：仓库历史 README 及提交列表；部分条目参考当前 README；未运行
- 信息限制与本库备注：仓库继承上游较早提交；fork 自身独立贡献按本提交日期计。当前文档还包含后续版本；不可与原版同时安装，节点名冲突。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### GH-03

**原分享：** [Anima Regional 0.3.3：人物与场景分区](https://github.com/An1X3R/ComfyUI-Anima-Regional/commit/bcaae88b2053ab470794c35ffd4ebfd08ff45561)

**适用方向：** 多主体·Anima·区域控制｜分别组织角色条件与空间归属，0.3.3 加入可选 shared_del…

**美术风格方向：** —（不涉及具体画风）

- 原作者：An1X3R
- 原始日期：2026-07-31T04:41:28Z
- 时间口径：Git 提交作者时间（UTC）；非仓库创建时间
- 日期依据：GitHub commits API: commit.author.date=2026-07-31T04:41:28Z; commit.committer.date=2026-07-31T04:41:28Z; 完整 SHA bcaae88b2053ab470794c35ffd4ebfd08ff45561; 提交信息：Release 0.3.3 identity anchor。
- 类别：多主体
- 精确版本：0.3.3
- 原作者分享要点（本库概述）：分别组织角色条件与空间归属，0.3.3 加入可选 shared_delta 身份锚点，针对与 post-adapter 混合组合时的角色和服装细节。
- 公开资源：https://github.com/An1X3R/ComfyUI-Anima-Regional；https://github.com/An1X3R/ComfyUI-Anima-Regional/commit/bcaae88b2053ab470794c35ffd4ebfd08ff45561；https://github.com/An1X3R/ComfyUI-Anima-Regional/blob/bcaae88b2053ab470794c35ffd4ebfd08ff45561/README.md
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：不涉及具体画风
- 风格依据：不适用
- 实际读取范围：仓库历史 README 及提交列表；部分条目参考当前 README；未运行
- 信息限制与本库备注：注意力路由不等同精准几何控制；README 的 0.4.7 等功能为后续版本。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### GH-04

**原分享：** [Krea 2 单次采样区域提示与分区 LoRA](https://github.com/januspluto/ComfyUI-Krea2-Regional/commit/23f937b07e37920e6eec34482ddc6fe7a26aef2a)

**适用方向：** 多主体·区域 LoRA·Krea 2｜基于联合注意力掩码把不同提示词和 LoRA 路由到不同区域，使用共享底…

**美术风格方向：** —（不涉及具体画风）

- 原作者：januspluto
- 原始日期：2026-07-08T01:05:28Z
- 时间口径：Git 提交作者时间（UTC）；非仓库创建时间
- 日期依据：GitHub commits API: commit.author.date=2026-07-08T01:05:28Z; commit.committer.date=2026-07-08T01:05:28Z; 完整 SHA 23f937b07e37920e6eec34482ddc6fe7a26aef2a; 提交信息：Initial release: Krea2 regional prompting + per-region LoRA for ComfyUI。
- 类别：多主体
- 精确版本：未知／见对应提交
- 原作者分享要点（本库概述）：基于联合注意力掩码把不同提示词和 LoRA 路由到不同区域，使用共享底提示维持场景联系。
- 公开资源：https://github.com/januspluto/ComfyUI-Krea2-Regional；https://github.com/januspluto/ComfyUI-Krea2-Regional/commit/23f937b07e37920e6eec34482ddc6fe7a26aef2a；https://github.com/januspluto/ComfyUI-Krea2-Regional/blob/23f937b07e37920e6eec34482ddc6fe7a26aef2a/README.md
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：不涉及具体画风
- 风格依据：不适用
- 实际读取范围：仓库历史 README 及提交列表；部分条目参考当前 README；未运行
- 信息限制与本库备注：仓库创建时间为 7 月 8 日；列出时间为首个提交的作者时间。边界仍可能风格串扰，后续新功能另核版本。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### GH-05

**原分享：** [Krea 2 Control LoRA 与结构图](https://github.com/facok/comfyui-krea2-controlnet/commit/5e10d80c018856c3991275714b32e63ba495ffbc)

**适用方向：** 结构控制·Control LoRA·Krea 2｜加载 Krea 2 Control LoRA，将由 VAE 编码的控制…

**美术风格方向：** —（不涉及具体画风）

- 原作者：facok
- 原始日期：2026-07-03T19:06:40Z
- 时间口径：Git 提交作者时间（UTC）；非仓库创建时间
- 日期依据：GitHub commits API: commit.author.date=2026-07-03T19:06:40Z; commit.committer.date=2026-07-03T19:06:40Z; 完整 SHA 5e10d80c018856c3991275714b32e63ba495ffbc; 提交信息：Initial Krea2 Control LoRA nodes。
- 类别：结构控制
- 精确版本：未知／见对应提交
- 原作者分享要点（本库概述）：加载 Krea 2 Control LoRA，将由 VAE 编码的控制图注入采样；可接深度、边缘或姿态等已有预处理结果。
- 公开资源：https://github.com/facok/comfyui-krea2-controlnet；https://github.com/facok/comfyui-krea2-controlnet/commit/5e10d80c018856c3991275714b32e63ba495ffbc；https://github.com/facok/comfyui-krea2-controlnet/blob/5e10d80c018856c3991275714b32e63ba495ffbc/README.md
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：不涉及具体画风
- 风格依据：不适用
- 实际读取范围：仓库历史 README 及提交列表；部分条目参考当前 README；未运行
- 信息限制与本库备注：需匹配的模型、VAE 与预处理图；节点本身不生成控制图。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### GH-06

**原分享：** [FLUX.2 ControlNet：组合与图像控制](https://github.com/Damkohler/JLC-Flux2-ControlNet/commit/406e850c29f0db16d721837add26b284c899a433)

**适用方向：** 结构控制·FLUX.2｜FLUX.2 原生节点实现并提供多 ControlNet 组合；随后 …

**美术风格方向：** —（不涉及具体画风）

- 原作者：Damkohler
- 原始日期：2026-07-06T21:11:27Z
- 时间口径：Git 提交作者时间（UTC）；非仓库创建时间
- 日期依据：GitHub commits API: commit.author.date=2026-07-06T21:11:27Z; commit.committer.date=2026-07-06T21:11:27Z; 完整 SHA 406e850c29f0db16d721837add26b284c899a433; 提交信息：Initial release: JLC Flux2 ControlNet v0.1.0。
- 类别：结构控制
- 精确版本：未知／见对应提交
- 原作者分享要点（本库概述）：FLUX.2 原生节点实现并提供多 ControlNet 组合；随后 7 月 8 日提交加入多槽组织及参考 latent。
- 公开资源：https://github.com/Damkohler/JLC-Flux2-ControlNet；https://github.com/Damkohler/JLC-Flux2-ControlNet/commit/406e850c29f0db16d721837add26b284c899a433；https://github.com/Damkohler/JLC-Flux2-ControlNet/blob/406e850c29f0db16d721837add26b284c899a433/README.md
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：不涉及具体画风
- 风格依据：不适用
- 实际读取范围：仓库历史 README 及提交列表；部分条目参考当前 README；未运行
- 信息限制与本库备注：以首版提交日期为准；精确模型兼容与后续功能须参照对应版本。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### GH-07

**原分享：** [Krea2 StyleBridge：内容提示和参考画风分离](https://github.com/sakugetu/comfyui-krea2-stylebridge-lmstudio/commit/23470d5f93c5130242bd9a328c11c8db9e7eed80)

**适用方向：** 风格参考·提示词自动化·Krea 2｜示范用 LM Studio 组织文字及内容参考，再通过 Untwist…

**美术风格方向：** 风格参考｜作者涉及风格控制；例图未核，人物比例、五官、表情、姿态、线条及光色材…

- 原作者：sakugetu
- 原始日期：2026-07-05T08:59:39Z
- 时间口径：Git 提交作者时间（UTC）；非仓库创建时间
- 日期依据：GitHub commits API: commit.author.date=2026-07-05T08:59:39Z; commit.committer.date=2026-07-05T08:59:39Z; 完整 SHA 23470d5f93c5130242bd9a328c11c8db9e7eed80; 提交信息：Add Krea2 StyleBridge ComfyUI workflow。
- 类别：风格参考
- 精确版本：未知／见对应提交
- 原作者分享要点（本库概述）：示范用 LM Studio 组织文字及内容参考，再通过 Untwisting RoPE／RF Inversion 使用独立风格参考，提供可导入工作流。
- 公开资源：https://github.com/sakugetu/comfyui-krea2-stylebridge-lmstudio；https://github.com/sakugetu/comfyui-krea2-stylebridge-lmstudio/commit/23470d5f93c5130242bd9a328c11c8db9e7eed80；https://github.com/sakugetu/comfyui-krea2-stylebridge-lmstudio/blob/23470d5f93c5130242bd9a328c11c8db9e7eed80/README.md
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：作者涉及风格控制；例图未核，人物比例、五官、表情、姿态、线条及光色材质待确认。
- 风格依据：作者文字，未实际看图
- 实际读取范围：仓库历史 README 及提交列表；部分条目参考当前 README；未运行
- 信息限制与本库备注：非官方实验流程；依赖额外节点和本地语言模型，不能保证风格与构图完全隔离。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### GH-08

**原分享：** [Clio 风格词库与同主体画廊对照](https://github.com/lumenastrum/clio-style-preview/commit/41b6baf6bb226c4bf4f8e06da11e2c490a50c8dd)

**适用方向：** 画风分析·提示词·Krea 2｜首版提供 281 个长篇风格描述及同一主体的画廊、滑块对照，便于浏览和…

**美术风格方向：** 风格参考｜作者涉及风格控制；例图未核，人物比例、五官、表情、姿态、线条及光色材…

- 原作者：lumenastrum
- 原始日期：2026-07-19T20:05:16Z
- 时间口径：Git 提交作者时间（UTC）；非仓库创建时间
- 日期依据：GitHub commits API: commit.author.date=2026-07-19T20:05:16Z; commit.committer.date=2026-07-19T20:05:16Z; 完整 SHA 41b6baf6bb226c4bf4f8e06da11e2c490a50c8dd; 提交信息：Initial release: 281-style ComfyUI node + style preview gallery 💅。
- 类别：画风分析
- 精确版本：未知／见对应提交
- 原作者分享要点（本库概述）：首版提供 281 个长篇风格描述及同一主体的画廊、滑块对照，便于浏览和组合画风描述。
- 公开资源：https://github.com/lumenastrum/clio-style-preview；https://github.com/lumenastrum/clio-style-preview/commit/41b6baf6bb226c4bf4f8e06da11e2c490a50c8dd；https://github.com/lumenastrum/clio-style-preview/blob/41b6baf6bb226c4bf4f8e06da11e2c490a50c8dd/README.md
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：作者涉及风格控制；例图未核，人物比例、五官、表情、姿态、线条及光色材质待确认。
- 风格依据：作者文字，未实际看图
- 实际读取范围：仓库历史 README 及提交列表；部分条目参考当前 README；未运行
- 信息限制与本库备注：面向长上下文文本编码器，作者提示 CLIP 77 token 会截断；当前版本词库数量可能已增加。未核看例图。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### GH-09

**原分享：** [Krea2 Prompt Styler：风格与摄影参数](https://github.com/Gothdir/ComfyUI-Krea2-PromptStyler/commit/5c83169cdd3316a8a77116deea6d876f0d40eeaa)

**适用方向：** 提示词组织·摄影风格·Krea 2｜为 Krea 2／Flux 提供按类别选择的风格和焦距、光圈、镜头、胶…

**美术风格方向：** 风格参考｜作者涉及风格控制；例图未核，人物比例、五官、表情、姿态、线条及光色材…

- 原作者：Gothdir
- 原始日期：2026-07-24T09:38:57Z
- 时间口径：Git 提交作者时间（UTC）；非仓库创建时间
- 日期依据：GitHub commits API: commit.author.date=2026-07-24T09:38:57Z; commit.committer.date=2026-07-24T09:38:57Z; 完整 SHA 5c83169cdd3316a8a77116deea6d876f0d40eeaa; 提交信息：Add files via upload。
- 类别：提示词组织
- 精确版本：未知／见对应提交
- 原作者分享要点（本库概述）：为 Krea 2／Flux 提供按类别选择的风格和焦距、光圈、镜头、胶片及光照字段，输出自然语言提示。
- 公开资源：https://github.com/Gothdir/ComfyUI-Krea2-PromptStyler；https://github.com/Gothdir/ComfyUI-Krea2-PromptStyler/commit/5c83169cdd3316a8a77116deea6d876f0d40eeaa；https://github.com/Gothdir/ComfyUI-Krea2-PromptStyler/blob/5c83169cdd3316a8a77116deea6d876f0d40eeaa/README.md
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：作者涉及风格控制；例图未核，人物比例、五官、表情、姿态、线条及光色材质待确认。
- 风格依据：作者文字，未实际看图
- 实际读取范围：仓库历史 README 及提交列表；部分条目参考当前 README；未运行
- 信息限制与本库备注：作者说明有 300 多种风格，但具体风格与结果依模型而异；例图未核。 日期更正：首提交只有 README，本条改指包含节点与风格文件的后续实质提交。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### GH-10

**原分享：** [HiDream-O1 双 ControlNet 细节工作流](https://github.com/biosynthart/comfyui-HiDream-O1-Detailer/commit/77f2aafb94b8a10737d209513bfbaf42288e23ac)

**适用方向：** 采样精修·结构控制｜作者公开从 HiDream-O1 图像转至 Z-Image Turbo…

**美术风格方向：** 风格参考｜作者涉及风格控制；例图未核，人物比例、五官、表情、姿态、线条及光色材…

- 原作者：biosynthart
- 原始日期：2026-07-06T04:35:49Z
- 时间口径：Git 提交作者时间（UTC）；非仓库创建时间
- 日期依据：GitHub commits API: commit.author.date=2026-07-06T04:35:49Z; commit.committer.date=2026-07-06T04:35:49Z; 完整 SHA 77f2aafb94b8a10737d209513bfbaf42288e23ac; 提交信息：initial commit。
- 类别：采样精修
- 精确版本：未知／见对应提交
- 原作者分享要点（本库概述）：作者公开从 HiDream-O1 图像转至 Z-Image Turbo 的 Canny 与 Tile 两阶段细节工作流，目标是保留面部构图并补充皮肤纹理。
- 公开资源：https://github.com/biosynthart/comfyui-HiDream-O1-Detailer；https://github.com/biosynthart/comfyui-HiDream-O1-Detailer/commit/77f2aafb94b8a10737d209513bfbaf42288e23ac；https://github.com/biosynthart/comfyui-HiDream-O1-Detailer/blob/77f2aafb94b8a10737d209513bfbaf42288e23ac/README.md；https://github.com/biosynthart/comfyui-HiDream-O1-Detailer/blob/77f2aafb94b8a10737d209513bfbaf42288e23ac/HiDream_O1_Detailer_TwoPass_v2.json
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：作者涉及风格控制；例图未核，人物比例、五官、表情、姿态、线条及光色材质待确认。
- 风格依据：作者文字，未实际看图
- 实际读取范围：仓库历史 README 及提交列表；部分条目参考当前 README；未运行
- 信息限制与本库备注：目标效果来自作者描述；未实际复跑或核看例图。 日期更正：首提交只有 README 和许可，本条改指加入工作流 JSON 的提交。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### GH-11

**原分享：** [MiniMax H3 Image Studio 静帧工作流](https://github.com/astropuzzo/ComfyUI-MiniMax-H3-Image-Studio/commit/6312094f3ef6ba5688a5f979a9f6d80011f93207)

**适用方向：** 图像生成·参考编辑·MiniMax H3｜针对 H3 静帧生成和参考图编辑组织条件、采样、分辨率及帧评分，附面向…

**美术风格方向：** —（不涉及具体画风）

- 原作者：astropuzzo
- 原始日期：2026-08-03T14:28:32Z
- 时间口径：Git 提交作者时间（UTC）；非仓库创建时间
- 日期依据：GitHub commits API: commit.author.date=2026-08-03T14:28:32Z; commit.committer.date=2026-08-03T14:28:32Z; 完整 SHA 6312094f3ef6ba5688a5f979a9f6d80011f93207; 提交信息：feat: publish H3 image studio。
- 类别：图像生成
- 精确版本：未知／见对应提交
- 原作者分享要点（本库概述）：针对 H3 静帧生成和参考图编辑组织条件、采样、分辨率及帧评分，附面向图像的节点和工作流。
- 公开资源：https://github.com/astropuzzo/ComfyUI-MiniMax-H3-Image-Studio；https://github.com/astropuzzo/ComfyUI-MiniMax-H3-Image-Studio/commit/6312094f3ef6ba5688a5f979a9f6d80011f93207；https://github.com/astropuzzo/ComfyUI-MiniMax-H3-Image-Studio/blob/6312094f3ef6ba5688a5f979a9f6d80011f93207/README.md
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：不涉及具体画风
- 风格依据：不适用
- 实际读取范围：仓库历史 README 及提交列表；部分条目参考当前 README；未运行
- 信息限制与本库备注：首个提交为 v10；当前文档可能包含之后追加的精修功能。作者测试不等于本次复跑。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### GH-12

**原分享：** [Anima Remap：跨 28／40／52 层 LoRA 和模型合并](https://github.com/shin131002/ComfyUI-Anima-Remap/commit/a5d7b07aba96cdaaca7f3179d465548f3e8e9401)

**适用方向：** Anima·LoRA 兼容·模型合并｜按模型层索引重映射在不同 Anima 代际之间应用 LoRA 和合并模…

**美术风格方向：** —（不涉及具体画风）

- 原作者：shin131002
- 原始日期：2026-08-24T10:50:29Z
- 时间口径：Git 提交作者时间（UTC）；非仓库创建时间
- 日期依据：GitHub commits API: commit.author.date=2026-08-24T10:50:29Z; commit.committer.date=2026-08-24T10:50:29Z; 完整 SHA a5d7b07aba96cdaaca7f3179d465548f3e8e9401; 提交信息：Initial commit: Anima-Remap (28/40/52 support)。
- 类别：Anima
- 精确版本：未知／见对应提交
- 原作者分享要点（本库概述）：按模型层索引重映射在不同 Anima 代际之间应用 LoRA 和合并模型，含随机 LoRA 加载路线。
- 公开资源：https://github.com/shin131002/ComfyUI-Anima-Remap；https://github.com/shin131002/ComfyUI-Anima-Remap/commit/a5d7b07aba96cdaaca7f3179d465548f3e8e9401；https://github.com/shin131002/ComfyUI-Anima-Remap/blob/a5d7b07aba96cdaaca7f3179d465548f3e8e9401/README.md
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：不涉及具体画风
- 风格依据：不适用
- 实际读取范围：仓库历史 README 及提交列表；部分条目参考当前 README；未运行
- 信息限制与本库备注：这是层号兼容方法，加载不保证所有权重生效或视觉一致；与旧 Anima29B-Remap 有重复节点 ID。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### GH-13

**原分享：** [Anima LoRA 与 ControlNet 跨层数映射](https://github.com/INuBq8/ComfyUI-Anima-LoRA-ControlNet-Patch/commit/db28dfbd8e37a1f954611e44245791f4501bb785)

**适用方向：** Anima·ControlNet·LoRA 兼容｜统一处理 Anima 28、40、52 层模型间双向 LoRA 与 C…

**美术风格方向：** —（不涉及具体画风）

- 原作者：INuBq8
- 原始日期：2026-09-09T00:38:49Z
- 时间口径：Git 提交作者时间（UTC）；非仓库创建时间
- 日期依据：GitHub commits API: commit.author.date=2026-09-09T00:38:49Z; commit.committer.date=2026-09-09T00:38:49Z; 完整 SHA db28dfbd8e37a1f954611e44245791f4501bb785; 提交信息：Initial release: unified, bidirectional Anima LoRA/ControlNet block remapping。
- 类别：Anima
- 精确版本：未知／见对应提交
- 原作者分享要点（本库概述）：统一处理 Anima 28、40、52 层模型间双向 LoRA 与 ControlNet-LLLite 层索引映射，不要求修改工作流。
- 公开资源：https://github.com/INuBq8/ComfyUI-Anima-LoRA-ControlNet-Patch；https://github.com/INuBq8/ComfyUI-Anima-LoRA-ControlNet-Patch/commit/db28dfbd8e37a1f954611e44245791f4501bb785；https://github.com/INuBq8/ComfyUI-Anima-LoRA-ControlNet-Patch/blob/db28dfbd8e37a1f954611e44245791f4501bb785/README.md
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：不涉及具体画风
- 风格依据：不适用
- 实际读取范围：仓库历史 README 及提交列表；部分条目参考当前 README；未运行
- 信息限制与本库备注：与另一项目为独立实现；映射并不保证不同训练目标和模型的视觉效果一致。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### GH-14

**原分享：** [Visual Grid Regional Prompt 区域构图文本](https://github.com/bada-ya/ComfyUI-Visual-Regional-Prompt/commit/9e3f89f078a399a31e55e92aedb18117d6039d65)

**适用方向：** 构图·多主体·提示词组织｜通过网格框选区域并逐区填写描述，输出自然语言、结构化标签或 JSON …

**美术风格方向：** —（不涉及具体画风）

- 原作者：bada-ya
- 原始日期：2026-09-01T06:43:56Z
- 时间口径：Git 提交作者时间（UTC）；非仓库创建时间
- 日期依据：GitHub commits API: commit.author.date=2026-09-01T06:43:56Z; commit.committer.date=2026-09-01T06:43:56Z; 完整 SHA 9e3f89f078a399a31e55e92aedb18117d6039d65; 提交信息：Initial commit for ComfyUI-Visual-Regional-Prompt。
- 类别：构图
- 精确版本：未知／见对应提交
- 原作者分享要点（本库概述）：通过网格框选区域并逐区填写描述，输出自然语言、结构化标签或 JSON 布局提示。
- 公开资源：https://github.com/bada-ya/ComfyUI-Visual-Regional-Prompt；https://github.com/bada-ya/ComfyUI-Visual-Regional-Prompt/commit/9e3f89f078a399a31e55e92aedb18117d6039d65；https://github.com/bada-ya/ComfyUI-Visual-Regional-Prompt/blob/9e3f89f078a399a31e55e92aedb18117d6039d65/README.md
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：不涉及具体画风
- 风格依据：不适用
- 实际读取范围：仓库历史 README 及提交列表；部分条目参考当前 README；未运行
- 信息限制与本库备注：首版输出文本，不等于模型内部注意力掩码或精确空间约束。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### GH-15

**原分享：** [Qwen Image 2.1 提示词改写节点](https://github.com/benjiyaya/ComfyUI-Qwen-Image-2.1-Prompt-Enhancer/commit/947468034a2b43d0a54321d31178dd058c68ecaa)

**适用方向：** 提示词自动化·图像编辑·Qwen｜作者提供 Qwen Image 2.1 的文生图与图像编辑提示词改写节…

**美术风格方向：** —（不涉及具体画风）

- 原作者：benjiyaya
- 原始日期：2026-09-20T22:07:59Z
- 时间口径：Git 提交作者时间（UTC）；非仓库创建时间
- 日期依据：GitHub commits API: commit.author.date=2026-09-20T22:07:59Z; commit.committer.date=2026-09-20T22:08:18Z; 完整 SHA 947468034a2b43d0a54321d31178dd058c68ecaa; 提交信息：Add Qwen-Image-2.1 prompt rewrite nodes。
- 类别：提示词自动化
- 精确版本：未知／见对应提交
- 原作者分享要点（本库概述）：作者提供 Qwen Image 2.1 的文生图与图像编辑提示词改写节点，公开系统提示及模型说明。
- 公开资源：https://github.com/benjiyaya/ComfyUI-Qwen-Image-2.1-Prompt-Enhancer；https://github.com/benjiyaya/ComfyUI-Qwen-Image-2.1-Prompt-Enhancer/commit/947468034a2b43d0a54321d31178dd058c68ecaa；https://github.com/benjiyaya/ComfyUI-Qwen-Image-2.1-Prompt-Enhancer/blob/947468034a2b43d0a54321d31178dd058c68ecaa/README.md
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：不涉及具体画风
- 风格依据：不适用
- 实际读取范围：仓库历史 README 及提交列表；部分条目参考当前 README；未运行
- 信息限制与本库备注：精确依赖与使用条件见对应仓库；生成效果未验证。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### GH-16

**原分享：** [Qwen Image 2.1 Fun Union 多种结构控制](https://github.com/T8mars/Comfyui-Qwen-Image-2.1-Fun-Controlnet-Union-T8/commit/cdd06a42d51afeeff9448335dcca1a5e5827df5e)

**适用方向：** 结构控制·ControlNet·Qwen｜发布 Qwen Image 2.1 Union 节点与工作流，覆盖边缘…

**美术风格方向：** —（不涉及具体画风）

- 原作者：T8mars
- 原始日期：2026-09-24T16:28:20Z
- 时间口径：Git 提交作者时间（UTC）；非仓库创建时间
- 日期依据：GitHub commits API: commit.author.date=2026-09-24T16:28:20Z; commit.committer.date=2026-09-24T16:28:20Z; 完整 SHA cdd06a42d51afeeff9448335dcca1a5e5827df5e; 提交信息：Release Qwen Image 2.1 Fun Union ComfyUI nodes。
- 类别：结构控制
- 精确版本：未知／见对应提交
- 原作者分享要点（本库概述）：发布 Qwen Image 2.1 Union 节点与工作流，覆盖边缘、深度、线稿、姿态等输入；后续提交增加参考图编辑。
- 公开资源：https://github.com/T8mars/Comfyui-Qwen-Image-2.1-Fun-Controlnet-Union-T8；https://github.com/T8mars/Comfyui-Qwen-Image-2.1-Fun-Controlnet-Union-T8/commit/cdd06a42d51afeeff9448335dcca1a5e5827df5e；https://github.com/T8mars/Comfyui-Qwen-Image-2.1-Fun-Controlnet-Union-T8/blob/cdd06a42d51afeeff9448335dcca1a5e5827df5e/README.md
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：不涉及具体画风
- 风格依据：不适用
- 实际读取范围：仓库历史 README 及提交列表；部分条目参考当前 README；未运行
- 信息限制与本库备注：控制图需预先生成；参考编辑为 9 月 26 日更新；模型另受原许可约束。 对应提交已有八类控制流程；参考图编辑为后续提交。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### GH-17

**原分享：** [LuCiD VRP 可视化编辑与区域布局](https://github.com/EBEBEEBE/comfyui-lucid-vrp/commit/5c4e9f351a7e686b17325aa39bdc6fd7b58a5103)

**适用方向：** 区域控制·图像编辑·多主体｜公开 beta 源码，提供画布编辑、Anima 区域提示和 MOSS-…

**美术风格方向：** —（不涉及具体画风）

- 原作者：EBEBEEBE
- 原始日期：2026-10-29T08:21:07Z
- 时间口径：Git 提交作者时间（UTC）；非仓库创建时间
- 日期依据：GitHub commits API: commit.author.date=2026-10-29T08:21:07Z; commit.committer.date=2026-10-29T08:49:33Z; 完整 SHA 5c4e9f351a7e686b17325aa39bdc6fd7b58a5103; 提交信息：Prepare LuCiD VRP Beta 1 public source。
- 类别：区域控制
- 精确版本：未知／见对应提交
- 原作者分享要点（本库概述）：公开 beta 源码，提供画布编辑、Anima 区域提示和 MOSS-Image 布局提示；区域可在画布上移动、调整和填写文本。
- 公开资源：https://github.com/EBEBEEBE/comfyui-lucid-vrp；https://github.com/EBEBEEBE/comfyui-lucid-vrp/commit/5c4e9f351a7e686b17325aa39bdc6fd7b58a5103；https://github.com/EBEBEEBE/comfyui-lucid-vrp/blob/5c4e9f351a7e686b17325aa39bdc6fd7b58a5103/README.md
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：不涉及具体画风
- 风格依据：不适用
- 实际读取范围：仓库历史 README 及提交列表；部分条目参考当前 README；未运行
- 信息限制与本库备注：图像加载和画布可独立使用，模型与 latent 兼容依实际工作流；Beta 新发布，稳定性未知。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

## 待核线索（不计入正式条目）

### GH-C1

**原分享：** [ANe5s/ComfyUI-Krea2-Harness](https://github.com/ANe5s/ComfyUI-Krea2-Harness)

**适用方向：** 方向待确认｜首个 README 仅证实 moodboard，具体工作流出现日期和内…

**美术风格方向：** 风格待确认（例图未核）

- 原作者：ANe5s
- 原始日期：未取得／未说明
- 时间口径：未确认实质功能日期
- 日期依据：仓库搜索与当前 README；尚未逐功能核实历史提交
- 类别：候选
- 精确版本：未取得／未说明
- 原作者分享要点（本库概述）：首个 README 仅证实 moodboard，具体工作流出现日期和内容尚未充分核实。
- 公开资源：未取得／未说明
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：未知
- 风格依据：未看图
- 实际读取范围：搜索摘要及当前 README
- 信息限制与本库备注：首个 README 仅证实 moodboard，具体工作流出现日期和内容尚未充分核实。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。

### GH-C2

**原分享：** [lonecatone23/ComfyUI_LC123_nodes](https://github.com/lonecatone23/ComfyUI_LC123_nodes)

**适用方向：** 方向待确认｜当前版本包含大量节点，尚未把目标功能对应到可核实窗口内的首次实质提交。

**美术风格方向：** 风格待确认（例图未核）

- 原作者：lonecatone23
- 原始日期：未取得／未说明
- 时间口径：未确认实质功能日期
- 日期依据：仓库搜索与当前 README；尚未逐功能核实历史提交
- 类别：候选
- 精确版本：未取得／未说明
- 原作者分享要点（本库概述）：当前版本包含大量节点，尚未把目标功能对应到可核实窗口内的首次实质提交。
- 公开资源：未取得／未说明
- 作者参数／触发词及边界：未取得／未说明
- 风格说明与可见范围：未知
- 风格依据：未看图
- 实际读取范围：搜索摘要及当前 README
- 信息限制与本库备注：当前版本包含大量节点，尚未把目标功能对应到可核实窗口内的首次实质提交。
- 追溯链接：未取得／未说明
- 本库收录日期：2026-10-30，历史补录；未安装或运行工作流。
