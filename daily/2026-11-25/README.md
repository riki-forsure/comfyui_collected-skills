# 2026-11-25 每日生图社区发现

- **北京时间与时间窗**：11月25日04:01开始，主要列表04:02–04:03，随后读取原文、配置和图像。承接11月24日约04:04的成功列表水位。本文日期除另标均按北京时间。
- **检索类型**：每日广泛发现，无具体差距要求。
- **执行状态**：精选8项。部分列表、平台字幕、附件和逐图参数受限。阅读范围、作者测试与本库实际视读见各条。未安装节点、下载生成权重、复跑或验证收益。
- 本文为中文整理与导读。感谢原作者、维护者及社区分享者，请回原文阅读完整说明、例图与后续更新，使用遵循各来源的条件。

## 今日值得阅读

SenseNova U1.6 的修订模板可以区分实际自纠输出与普通解码。MOSS 的加速条目分别讨论蒸馏采样和低内存启动参数。RD Flow 64 与 Pixel32 展示不同分辨率的原生像素素材路线。另记录动作与外观分离研究、Krea 2 都市环境 LoRA、MiniMax H3 逐镜首帧与局部返工。

## 分享速查

| 类别 | 分享／资源 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点 | 读取与验证状态 |
|---|---|---|---|---|---|---|
| 模型与模板 | [SenseNova U1.6：原生文字自纠与 ComfyUI 开关修正](#n01) | 版面文字·图像编辑｜查阅文字自纠、Turbo 切换及修正版模板接线。 | 设计思路：先出图后校字｜用原提示核对成图的排版与文字，再提供修订图。 | OpenSenseNova／商汤；Comfy-Org 与模板维护者 · [固定模型指南](https://github.com/OpenSenseNova/SenseNova-U1/blob/d2d9bd1426670bc46b5a344b7da4b9a888b8d6df/docs/u1.6_model.md) · [模板修正 PR](https://github.com/Comfy-Org/workflow_templates/pull/1455) · [修正后的文生图模板](https://github.com/Comfy-Org/workflow_templates/blob/cf1048587a3a416d924dc2851701f1fde96978ca/templates/image_sensenova_u16_t2i.json) | 自纠回路、原始采样与8步 LoRA 分开核对 | 项目说明、模型元数据、修订JSON和官方预览两帧；未复跑 |
| 加速LoRA | [MOSS Fast-12 Turbo OPD v1.0：12／16步与持物细节](#n02) | 采样精修·LoRA搭配｜查阅 MOSS SFT 加速配置和复杂手部的步数取舍。 | 设计思路：笔触与持物细节｜比较加速后色调、笔纹和握持结构，复杂道具另看16步。 | lepetitprince716355；OpenMOSS-Team · [作者文章](https://civitai.com/articles/39708) · [精确版本 3487510](https://civitai.com/models/3063613?modelVersionId=3487510) · [持杯对照](https://civitai.com/images/150085763) | MOSS SFT，Euler／normal、CFG 1、shift 5、ModelOnly | 文章与版本正文、1张对照图、3条作品元数据；未解包或运行 |
| 原生像素模型与提示 | [RD Flow 64：按部位与留白写像素精灵提示](#n03) | 像素素材·提示词组织｜为原生64像素角色、道具和满幅场景写描述。 | 美术风格方向：低分辨率像素·有限色盘｜示范用阶梯轮廓与少量亮暗色块区分物件和场景。 | Retro Diffusion；Qwen 编码器作者 · [固定模型卡](https://huggingface.co/Retro-Diffusion/rd-flow-64/blob/f0577f17db52aa55bb318d0f558d4ee48b67cf6c/README.md) · [作者提示指南](https://github.com/Retro-Diffusion/rd-flow-64/blob/main/PROMPTING.md) · [21例展示](https://huggingface.co/Retro-Diffusion/rd-flow-64/blob/f0577f17db52aa55bb318d0f558d4ee48b67cf6c/samples/showcase.png) | 64×64 RGBA，可指定色盘，长英语描述匹配训练顺序 | 模型卡、提交、提示指南和1张展示拼图；未读权重或运行 |
| 双语像素模型 | [Pixel32 v1.5：中文文化素材续训与8步导出](#n04) | 像素素材·双语提示｜比较中文文化道具在不同检查点下的轮廓与辨识度。 | 美术风格方向：低色阶图标·块状轮廓｜对照中的灯笼、瓶罐和兵器以少色层表现形状。 | dlwj；Pixel32 作者列明的 SigLIP2 与数据上游 · [v1.5 固定发布卡](https://huggingface.co/dlwj/pixel32-bilingual/blob/6c5136289cb6ed4b97ee52bdaccda2b300fa9600/v1_5/README.md) · [中文主题对照](https://huggingface.co/dlwj/pixel32-bilingual/blob/6c5136289cb6ed4b97ee52bdaccda2b300fa9600/v1_5/pixel32-v15-cn-comparison.png) | v1.5 Turbo 8步，16选1检索分数与画风表现分开读 | 主卡、固定发布卡、提交记录、两张拼图；未运行 ONNX |
| 动作迁移研究 | [StaDy：从相邻帧提取动作并迁移到新外观](#n05) | 动作控制·跨主体迁移｜了解双帧动作表示如何减少参考外观混入。 | 设计思路：运动和外观分工｜将动作来源与承载动作的目标画面设为独立条件。 | Frank Fundel、Thomas Ressler-Antal、Malek Ben Alaya、Stefan Andreas Baumann、Björn Ommer（CompVis／LMU Munich、MCML） · [作者项目页](https://compvis.github.io/StaDy/) · [固定模型卡](https://huggingface.co/CompVis/StaDy/blob/81a5292dba39755650443cbeedd492bb3bd602fb/README.md) | 使用一对参考帧提动作，结合另一张图预测下一帧 | 模型卡与项目页机制、评估说明；未看视频或复核论文表 |
| 环境场景LoRA | [City Worlds 04 V1：Krea 2 城市布景与灯牌层次](#n06) | 场景背景·画风搭配｜参考 Krea 2 都市场景的灯牌、前景和空间层次。 | 美术风格方向：高密度都市·红蓝灯光｜本例把暖色招牌、冷色灯箱和悬空餐吧堆叠成街景。 | Z1os · [版本3487738](https://civitai.com/models/3063786?modelVersionId=3487738) · [本例作品](https://civitai.com/images/150102750) | Krea 2 场景风格 LoRA，trigger z1os | 版本正文、1张原始预览与4条作品元数据；配方为空 |
| B站低内存实践 | [MOSS-Image 低显存第3期：原生启动参数与 Spectrum 耗时](#n07) | 兼容排错·低内存运行｜查阅 MOSS 低内存启动参数及 Spectrum 测试范围。 | — | 我家猫猫Gemini；ComfyUI 与 Spectrum 相关作者 · [B站原视频](https://www.bilibili.com/video/BV1zr1czAEW4/) · [ComfyUI v0.42.0 参数定义](https://github.com/Comfy-Org/ComfyUI/blob/v0.42.0/comfy/cli_args.py) | 区分系统内存、显存余量与另一组40步提速对照 | 完整简介、P1抽13帧及OCR人工核字、上游CLI；平台字幕需会话 |
| 社区逐镜实践 | [MiniMax H3 音乐视频：逐镜首帧与局部返工](#n08) | 图像转视频·分镜精修｜参考角色表定首帧、按镜头回退二采并对拍剪辑。 | 设计思路：锁首帧·按镜头回退｜先筛角色表与姿态构图，局部出现伪字时单独返工。 | Reddit u/Cheap_Credit_3957；MiniMax 和相关节点作者 · [作者原帖](https://www.reddit.com/r/StableDiffusion/comments/1y45u4d/spent_2_days_directing_this_video_scene_by_scene/) | 作者公布首帧与两段采样条件，问题镜头单独重做 | 主帖、公开设置及可见评论片段；未观看原片、下载图或复跑 |

## 当日分享

<a id="n01"></a>

### SenseNova U1.6：原生文字自纠与 ComfyUI 开关修正

**适用方向：版面文字·图像编辑｜查阅文字自纠、Turbo 切换及修正版模板接线。**

**设计思路：先出图后校字｜用原提示核对成图的排版与文字，再提供修订图。**

- 原作者与原文：OpenSenseNova／商汤；Comfy-Org 与模板维护者 · [固定模型指南](https://github.com/OpenSenseNova/SenseNova-U1/blob/d2d9bd1426670bc46b5a344b7da4b9a888b8d6df/docs/u1.6_model.md) · [模板修正 PR](https://github.com/Comfy-Org/workflow_templates/pull/1455) · [修正后的文生图模板](https://github.com/Comfy-Org/workflow_templates/blob/cf1048587a3a416d924dc2851701f1fde96978ca/templates/image_sensenova_u16_t2i.json)
- 作者在项目公告标11月24日正式发布 SenseNova-U1.6-8B-MoT。核对其原始分片 BF16、Native 合并及量化、GGUF、4／8步 LoRA 的独立入口。固定指南给出 BF16 revision 8f582699bac7f1e5362df2a776397d0e1a963b6c；Comfy-Org 包的本轮 revision 1945bcc8fbd56b9ed09aee3e207ea269ad64858d 列 BF16、INT8 ConvRot 和8步 BF16 LoRA。指南注明权重 Apache 2.0。
- 自纠机制来自作者说明：先出图，以原提示审查文字与编号，再结合原提示及初图出修订图。训练范围重点在信息图，按作者公开样例理解对其他作品的迁移。官方动图抽看首尾两帧，首帧粉红玫瑰海报标出乱码长文，末帧红色饮料海报标出清楚的容量数字。这两帧对应不同样例，只作展示范围说明。
- 已读修订后 JSON，默认 checkpoint 是 U1.6 INT8 ConvRot，Turbo 关闭、提示增强 Enable PE 与 Self-Correction 打开。图中50步／CFG 4和8步／CFG 1由开关选取，8步 ModelOnly LoRA 强度1。作者的指南亦有独立4步权重，模板本身走8步。工作流模板 0.11.118 的 PR 说明早期文生图模板把两个输出接反。修订后打开自纠走 SenseNovaInterleaveDecode，关闭走普通 VAEDecode。这个差异影响用旧图判断自纠是否生效。
- 社区反馈：u/Electronic_Resort985 在[原测试帖](https://www.reddit.com/r/comfyui/comments/1y4fzfd/ran_the_sensenova_u16_comfyui_template_on_a_mac/)报告 M5 Ultra、ComfyUI 0.46 master、INT8 ConvRot 与关闭 PE 时，四张模板排版示例8步生成耗时24–27秒／张（已热载）。按发帖者观察，四个样例首次文字都正确。原页文字已读，测试图和运行日志未核，不外推文字正确率。

<a id="n02"></a>

### MOSS Fast-12 Turbo OPD v1.0：12／16步与持物细节

**适用方向：采样精修·LoRA搭配｜查阅 MOSS SFT 加速配置和复杂手部的步数取舍。**

**设计思路：笔触与持物细节｜比较加速后色调、笔纹和握持结构，复杂道具另看16步。**

- 原作者与原文：lepetitprince716355；OpenMOSS-Team · [作者文章](https://civitai.com/articles/39708) · [精确版本 3487510](https://civitai.com/models/3063613?modelVersionId=3487510) · [持杯对照](https://civitai.com/images/150085763)
- 作者《MOSS Image in ComfyUI: 3.25x Faster 12-Step OPD vs DMD2 Without Color Washout》于北京时间11月24日23:34:02发布，权重 v1.0（OPD s500，版本3487510）于23:04:13发布。rank 64，发布文件 BF16，作者称以50步 BF16 教师轨迹蒸馏。
- 作者给的起点适用 ComfyUI ≥0.42.0 和 MOSS-Image-SFT INT8／BF16，先 ModelOnly LoRA 1.0，若叠画风 LoRA 则在其后接作者建议0.75–0.90，再接 AuraFlow shift 5。采样 Euler／normal、12或16步、CFG 1，无触发词。按作者说明，normal 与蒸馏 sigma 对应。文件名 moss_opd_fast12_v1.safetensors，作者声明整文件 SHA-256 aefad581a59fed6f5d19e33a06ace9cb847b281b5887fc340cae8cbaece62da9，未下载校验。作者标 Apache 2.0。
- 作者 RTX 5080、INT8 SFT、1MP 暖缓存32条对照的均值是 SFT 25步9.02秒、12步2.77秒、16步3.46秒。三条量化行覆盖原SFT和OPD两档，DMD2 的色调描述在正文，缺少同表对应实验行。16步持乐器的12/12仅为作者样例计数。
- 本库看图限同 seed 标注的持杯对照拼图，两侧均为暖橙窗光和深色马甲，12步图的手抬杯更高、面孔角度也变。它能帮助观察材质与手部差异。图内8.6→2.3秒是本例标签，基准均值另见作者表。三件作品 meta 为空，公开 ZIP 有列出但未打开，逐图提示和实际配置未知。

<a id="n03"></a>

### RD Flow 64：按部位与留白写像素精灵提示

**适用方向：像素素材·提示词组织｜为原生64像素角色、道具和满幅场景写描述。**

**美术风格方向：低分辨率像素·有限色盘｜示范用阶梯轮廓与少量亮暗色块区分物件和场景。**

- 原作者与原文：Retro Diffusion；Qwen 编码器作者 · [固定模型卡](https://huggingface.co/Retro-Diffusion/rd-flow-64/blob/f0577f17db52aa55bb318d0f558d4ee48b67cf6c/README.md) · [作者提示指南](https://github.com/Retro-Diffusion/rd-flow-64/blob/main/PROMPTING.md) · [21例展示](https://huggingface.co/Retro-Diffusion/rd-flow-64/blob/f0577f17db52aa55bb318d0f558d4ee48b67cf6c/samples/showcase.png)
- 权重首个公开提交为11月25日01:04:15，固定模型卡更新为01:51:23。作者的270.9M绘图网络工作在原生64×64格点，输出可带二值透明度，可锁定色盘。文字端单独用约3.1B 的裁切 Qwen3-VL-4B-Instruct。作者的2GB GPU示例把文本端放CPU，读一次提示约19秒，4张绘图阶段0.8秒（bf16 测试行）。
- 提示指南建议约120–200个英文词，按主体、从上到下分部位、姿态／朝向、构图、背景、线条和光影排序。透明精灵写主体完整与四周留白，满幅场景用 --opaque 并描述环境。作者默认16步 Euler、guidance 4，提示指南建议3–4；其“少用风格标签”来自自身训练 caption 结构。
- 本库看21例展示：上两排道具、动物与角色用较硬像素边缘和有限色阶，猫厨师与挥手宇航员各有不同头身及重心。下排室内、海底和火山使用大色块与分层剪影。展示背景及视觉边缘已看，未检验每个 PNG 的 Alpha 数据。作者列字母与商标难生成、满幅场景易放大／裁切、重复提示构图变化较少。
- 权重 CC BY-NC 4.0，推理代码 MIT，Qwen 文本端 Apache 2.0，分别查作者列明的条件。示范没逐图核采样和提示。

<a id="n04"></a>

### Pixel32 v1.5：中文文化素材续训与8步导出

**适用方向：像素素材·双语提示｜比较中文文化道具在不同检查点下的轮廓与辨识度。**

**美术风格方向：低色阶图标·块状轮廓｜对照中的灯笼、瓶罐和兵器以少色层表现形状。**

- 原作者与原文：dlwj；Pixel32 作者列明的 SigLIP2 与数据上游 · [v1.5 固定发布卡](https://huggingface.co/dlwj/pixel32-bilingual/blob/6c5136289cb6ed4b97ee52bdaccda2b300fa9600/v1_5/README.md) · [中文主题对照](https://huggingface.co/dlwj/pixel32-bilingual/blob/6c5136289cb6ed4b97ee52bdaccda2b300fa9600/v1_5/pixel32-v15-cn-comparison.png)
- 作者发布提交 6c5136289cb6ed4b97ee52bdaccda2b300fa9600 为11月25日03:41:12，04:01:02另有 Stage 1A step 951 检查点提交，本条固定到 v1.5 发布。模型面向32×32透明素材，48.41M，512色 OKLab 色盘。作者称在v1 EMA上混合74,178张 HQ 精灵和3,440张 cn_factory 中文文化精灵，再做难例／轮廓打磨及蒸馏。
- v1.5发布卡的特定16选1中文文化组，v1为100%、v1.5 Teacher 75%、v1.5 Turbo 68.8%；英语组分别100%、93.8%、93.8%。作者还报告 Turbo FP16 导出 ORT top-1 parity 99.95% 和约53.72MB的INT8导出。检索结果是该样本集的分数，转化保真与图标识别是两种评价。
- 本库在发布卡中文文化拼图中看到多行道具的像素形状和色块变化，例如灯笼的提环／暖色光心、瓶罐轮廓在不同行被简化。主卡的中英并列是另张图，不能替代 v1.5 对照的版本条件。未核每格种子和走的是 FP16 或 INT8。主卡标 Apache 2.0，训练数据逐张授权未检查。

<a id="n05"></a>

### StaDy：从相邻帧提取动作并迁移到新外观

**适用方向：动作控制·跨主体迁移｜了解双帧动作表示如何减少参考外观混入。**

**设计思路：运动和外观分工｜将动作来源与承载动作的目标画面设为独立条件。**

- 原作者与原文：Frank Fundel、Thomas Ressler-Antal、Malek Ben Alaya、Stefan Andreas Baumann、Björn Ommer（CompVis／LMU Munich、MCML） · [作者项目页](https://compvis.github.io/StaDy/) · [固定模型卡](https://huggingface.co/CompVis/StaDy/blob/81a5292dba39755650443cbeedd492bb3bd602fb/README.md)
- 原项目《Factorizing the World into Static and Dynamic via Likelihood Matching》，HF 11月24日23:22:35建库，11月25日00:39:25更新至81a5292dba39755650443cbeedd492bb3bd602fb。作者列 NeurIPS 2026，提供 openworld 与 CelebV 权重和动作提取／迁移代码。
- 动作编码器从一对帧提取变化，flow-matching 解码器以另一源图及动作表示为输入预测下一帧。训练的约束旨在减少潜码直接携带目标帧外观。作者项目页讨论高维动作表征对动作准确与外观泄漏的影响。
- README 示例取参考视频第一对帧的 motion，再传给 model.transfer 生成目标轨迹的一步，示例50步。单步演示不能说明长片角色恒定；没有查到该卡提供普通 ComfyUI 模板或逐镜头参数。本轮查阅文字及入口，未观看演示、安装或下载权重，独立许可条款未核。

<a id="n06"></a>

### City Worlds 04 V1：Krea 2 城市布景与灯牌层次

**适用方向：场景背景·画风搭配｜参考 Krea 2 都市场景的灯牌、前景和空间层次。**

**美术风格方向：高密度都市·红蓝灯光｜本例把暖色招牌、冷色灯箱和悬空餐吧堆叠成街景。**

- 原作者与原文：Z1os · [版本3487738](https://civitai.com/models/3063786?modelVersionId=3487738) · [本例作品](https://civitai.com/images/150102750)
- 《City Worlds 04 - KREA 2》V1 于北京时间11月25日03:31:32发布，版本 API 标 Krea 2。作者定位为背景／风格 LoRA，称写实和动画路线可由提示决定。推荐触发词 z1os，试过0.8–1.2强度，Raw 40–52步或 Turbo 8步，属于通用建议。
- 本库实际看896×1152一张餐吧示范：楼体外墙压满灯牌和电缆，红橙招牌把餐吧与远楼分开，青蓝灯箱带出冷暖层次。人物通过背坐、侧身和相对交谈构成群像，面孔小，重点是空间与灯光。前景植被和近处结构遮挡、远处街楼虚化，这些是本例的构图处理。未核字牌拼写或跨图稳定性。
- 作品接口四项 meta 为空且同时关联版本3258954与3487738。本例基座精确文件、LoRA实值、seed 和完整提示未知，画面归整套生成。作者明确请勿转发权重文件，读者回 Civitai 原页查看与使用。

<a id="n07"></a>

### MOSS-Image 低显存第3期：原生启动参数与 Spectrum 耗时

**适用方向：兼容排错·低内存运行｜查阅 MOSS 低内存启动参数及 Spectrum 测试范围。**

- 原作者与原文：我家猫猫Gemini；ComfyUI 与 Spectrum 相关作者 · [B站原视频](https://www.bilibili.com/video/BV1zr1czAEW4/) · [ComfyUI v0.42.0 参数定义](https://github.com/Comfy-Org/ComfyUI/blob/v0.42.0/comfy/cli_args.py)
- 原视频《【MOSS-Image】ComfyUI动辄吃20G内存闪退？4个原生参数直接压进10G！附Spectrum 2倍提速插件+算子进阶指南》，11月24日20:31:49发布。作者为 ComfyUI ≥0.42.0 分享8GB显存主档：`--use-ck-attention --vram-headroom 0.6 --disable-pinned-memory --fast-disk`，6GB显存／16GB系统内存档把余量改0.8并加 `--cache-none`，配合其第2期。
- 依据上游 v0.42.0 CLI，这些参数分别选择 Comfy Kitchen attention、为 DynamicVRAM 指定以GB计的额外显存余量、停用 pinned memory、强制磁盘支持的动态加载／卸载，cache-none 可降内存使用但会重复执行各节点。硬件可用性和耗时需要各机判断。简介的“内存≤10GB”是作者系统内存口径。
- 约42–46秒的画面和烧录字幕写作者2.0MP、原生40步的 Spectrum 对照为176秒到88秒，和前面四项内存参数是两组说明。未取得完整机型、权重、Spectrum版本与系统日志。视频另提 Triton／SageAttention、离线 LoRA 融合和包内脚本，本库仅记原作者用途。
- SDK17.4.2元数据与完整简介成功。88秒P1，852×480，主媒体567后同响应备用200，1486955字节；约7秒间隔12张加末帧，OCR辅助后人工核对主要卡片。画面烧录字幕与平台字幕分开，zh-CN请求为login_required，未取音轨、ASR或评论。未打开网盘、运行批处理或插件。

<a id="n08"></a>

### MiniMax H3 音乐视频：逐镜首帧与局部返工

**适用方向：图像转视频·分镜精修｜参考角色表定首帧、按镜头回退二采并对拍剪辑。**

**设计思路：锁首帧·按镜头回退｜先筛角色表与姿态构图，局部出现伪字时单独返工。**

- 原作者与原文：Reddit u/Cheap_Credit_3957；MiniMax 和相关节点作者 · [作者原帖](https://www.reddit.com/r/StableDiffusion/comments/1y45u4d/spent_2_days_directing_this_video_scene_by_scene/)
- 原帖《Spent 2 days directing this video scene by scene... (MiniMax H3 + Video builder in ComfyUI)》，Reddit检索标11月24日，原页显示相对时间。作者使用 H3 Image 从角色参考表逐镜做首帧，先审姿态、表情、草稿，再让通过的镜头进入二采。称26个场景，约两天制作，渲染约14小时，手动剪辑时用音轨节拍点做 SRT 标记。
- 作者称本次首帧用 H3 Image pruned INT8 ConvRot、4步 LCM/simple、CFG 1、DMAD四步 LoRA 1.0及 MiniMaxH3_Enhancer epoch 10 为0.7。视频链用 H3 FL2VA pruned INT8 ConvRot，首段25步 res_multistep/simple，第二段2× latent upscaler，ref2v turbo 8step v1.1 768p BF16 LoRA 1.0、4步、denoise 0.30，同 sampler/scheduler，最后缩放1920×1080。参数来自作者声明，逐镜 seed 和完整图未知。
- 据作者，部分特写二采添光斑和伪字，就只重做这些镜头：以720p首段出结果，再用 RTX 放大替换。还对成片应用统一的曝光、对比度、锐度和颗粒预设。这是该作者在交付中处理异常的实践，不把小批案例写成模型基准。

## 来源覆盖与检索记录

| 平台 | 实际入口／覆盖 | 读取结果与限制 |
|---|---|---|
| 百度贴吧 stablediffusion | aiotieba 4.8.2 CREATE第1页30条。最新普通帖11月25日00:06，页末11月23日09:04，已跨上一期水位。全站最新“工作流 提示词”“模型 LoRA”“教程 分享”各1页，分别29、30、23条。 | 带空格“stable diffusion”入口解析到stable吧，两条为2018年公告，规范吧名另列。按tid去重并读[Anima单图玩法](https://tieba.baidu.com/p/11226427428)5楼、[Noob讨论](https://tieba.baidu.com/p/11225787443)13个可见楼及[MOSS出图](https://tieba.baidu.com/p/11225379673)5楼文字。Forge Neo帖说移植了两个插件，楼内文字仅列多视角等用途，读取范围未取得可核的精确链接或配方。Noob2帖子为试用意见，未确认所指版本或官方发布。图片与楼中楼未读，本范围暂未精选贴吧条目。 |
| 百度贴吧 comfyui | 同主工具独立 CREATE第1页28条。除置顶外最新11月25日03:29，页末11月20日14:27，已跨水位。 | 读[H3 R2V流水线进度](https://tieba.baidu.com/p/11226609571)楼主文字。作者提到4060 16GB、PromptQueue批量和提示词未刷新，未公开补丁或工作流实值。其它多为硬件／安装问题与网盘分享，本范围无精选。两吧主工具正常，未启用Astron。 |
| bilibili 广泛发现 | SDK 17.4.2 pubdate：ComfyUI教程页1–4共80条。页1为11月24日19:04至25日00:08，页4最早23日18:09，已过水位。生图模型、Anima生图、LoRA画风各页1／20。 | 按BV去重，完整简介四项：本日MOSS条目、[Anima入门](https://www.bilibili.com/video/BV1vhyDzFExJ/)、[7900 XTX H3 Image](https://www.bilibili.com/video/BV1QDyfzEEKm/)、[质感提示](https://www.bilibili.com/video/BV1h9yfzjE58/)。后3条只读元数据与简介，其画面、讲解、配置未核。LoRA画风本页命中偏旧。MOSS限一分P，实际证据见N07。 |
| bilibili Sena404 | UID341674866 最新投稿第1页30条，计数90。 | 最新仍为11月23日19:39:46投稿第32期 BV1X9ySzsENy，已归档片内42及标签，本日无作者增量。见[系列索引](../2026-11-09/notes/Sena404画师串与相关分享.md)。 |
| Reddit | r/StableDiffusion newest50与r/comfyui newest30 JSON均403，补以日期、workflow、LoRA、prompt等原帖搜索。 | 打开[U1.6社区发布讨论](https://www.reddit.com/r/comfyui/comments/1y42ms7/sensenova_u16_is_out_natively_supported_in_comfyui/)、Mac Studio测试和H3逐镜实践。实际读取主帖与页面可见回复片段，未全量读评论或视频。其它8GB动画管线与多主体H3仅作索引候选。 |
| Hugging Face | text-to-image最新80、image-to-image最新30，Anima／Illustrious／NoobAI各15。 | 精读RD Flow 64、Pixel32、StaDy和SenseNova指南／版本元数据，另读MiniT2I WebGPU与Geode转换卡。家族搜索含旧卡和误命中，未视为新发布。 |
| GitHub | 工作流更新搜索25项，提示与节点搜索12项，并追模型作者的固定commit、模板修订PR。 | 读取SenseNova正式指南、Comfy模板JSON及PR，Retro Diffusion提示指南、CompVis站点的项目入口。另读comfy-draftsman和FolderQueue文档作为候选，未验证服务、节点或兼容性。 |
| Civitai 文章与讨论 | Newest 30篇，正文检查39708、39676、39691、39707。 | OPD有可比较版本与参数，其他细节感想、数据来源记录及SD1.5实验作为筛选范围。模型网页的讨论入口部分受限，版本和文章正文经公开API可读，未取得完整版本评论。 |
| Civitai 模型、工作流和作品 | 最新模型40、工作流15。具体读OPD、City Worlds、Illustrious区域图、SenseNova社区图和Blink Anima v5。 | 已看OPD与City各1张。查询上述5个版本的作品元数据，返回3／4／3／4／1条，meta均空；部分作品关联多个或其它版本。Illustrious附件HTTP返回网页，未取得JSON。以已核配置和来源为准，没有用通用作者推荐补造作品配方。 |
| 其它来源 | Comfy论坛latest.json为200，顶部仍为LTX求助等较旧主题；note.com的ComfyUI最新搜索403。 | 补读CompVis项目页、Retro Diffusion作者文档及官方Comfy模板修订。论坛仅列表，note.com受限，二者分别记载。 |

## 后续关注与更正

- 参考 SenseNova 自纠结果时记录工作流模板版本与输出分支，尤其区分0.11.118修正前后。作者演示、社区样例与本地复跑各自保留条件。
- Pixel32 v1.5发布与同仓后续检查点分别记载。像素两路线都可参考作者公开示范，后续再按有明确逐图输入与输出元数据的资源补齐。
- MOSS OPD 与 Spectrum 的测试机器、图像大小和计时范围不同，报告各作者的原值。城市LoRA的逐图设置及B站平台字幕仍待可读资料。
- Sena404系列水位仍为投稿32。继续按UID、投稿日期与BV查增量。

[日期入口](../README.md) · [总索引](../../每日检索可速查总结.md)
