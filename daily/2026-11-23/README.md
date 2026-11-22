# 2026-11-23 每日生图社区发现

- **北京时间／执行时间**：2026-11-23，04:02开始；列表主要04:03–04:11，正文、配置与画面随后补读；归档前已核最新文件与SHA。
- **类型／时间窗**：每日广泛发现，无具体差距要求。接续11月22日约04:00的实际检索水位，优先其后新增和实质变化，旧仓本日有更新者按具体版本首收；非连续全网监控。
- **执行状态**：已完成本轮固定来源的实际检查与精选10项；部分入口／证据层受限，范围见覆盖表。本文为阅读归档，未安装节点、下载大模型、编译、训练、复跑或生图，未验证收益。
- **信息归属**：正文为本库中文概述／学习备注；作者建议、作者评估、社区反馈、本库实际看图分别标明。感谢社区作者，请回原文阅读完整教程、版本变化和使用条件；链接与署名不等同转载授权。

## 今日发现

本轮可读方向包括Anima可爱合并版、蓝晒与Krea平涂LoRA、MOSS摄影细节LoRA、直接像素解码、多参考与配方阅读工具、角色数据集设计和个人训练经验。Sena404补至投稿第31期。参数多少、热度与速度标题均不单独作为质量依据。

## 分享速查

| 类别 | 分享／资源 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点 | 读取与验证状态 |
|---|---|---|---|---|---|---|
| Anima合并模型 | [SugarPalette ANIMA v2：可爱插画的细节调整版](#n01) | 人物插画·模型选型｜阅读Anima合并版的可爱定位、采样建议和来源。 | 美术风格方向：甜美日漫·柔亮上色｜本例大圆眼与小鼻口，细线柔影配发束亮边和暖色环境。 | Noginowa／のぎのわ；所列父模型、LoRA与工具作者；[固定模型卡](https://huggingface.co/Noginowa/SugarPalette-ANIMA/blob/4f1ce58dd2d62917fa2bdce95c1581a789cf327b/README.md) | v2调整整体细节；公布父模型，未给融合系数 | 模型卡全文、1张v2示范；未读对比图／运行 |
| MOSS特化LoRA | [MOSS FRAME SFT Detail Sixteen：16步摄影细节新训练](#n02) | 摄影质感·采样精修｜查阅MOSS SFT十六步LoRA的专用采样与补丁顺序。 | 设计思路：皮肤细节·高光控制｜按作者筛选结果，在近景纹理和鼻梁高光之间取舍。 | Coffmeteor；FRAME与OpenMOSS相关作者；[固定版本说明](https://huggingface.co/Coffmeteor/MOSS-Image-Turbo/blob/e7de9a63635fa803b7f3bf9c321dd2b077491bc4/frame-sft-detail-16step-cfg1/README.md) | 新训3035 updates；不能套旧16步Euler配方 | 主卡、新版卡、release、examples及API图关键节点；未看例图 |
| Anima风格LoRA | [CyBlue v1(e08)：普鲁士蓝与暖色点缀](#n03) | 人物插画·双色设计｜参考Anima蓝晒风格与暖色点缀的提示组织。 | 美术风格方向：蓝晒线描·暖色点睛｜本例蓝白发丝与衣褶成块，橙色眼睛和红日突出焦点。 | lepetitprince716355；Anima相关作者；[精确版本](https://civitai.com/models/3061745?modelVersionId=3484732) · [本例作品](https://civitai.com/images/149889947) | 有trigger及完整通用采样；加载后不写trigger也会偏蓝 | 模型／版本全文、1张原图、3条作品元数据；meta为空 |
| Krea风格LoRA | [Krea 2 CS Flat Palette Anime：从2.5D到平涂的权重取舍](#n04) | 画风搭配·平涂上色｜按Krea2 LoRA权重区分保留光泽与海报化处理。 | 美术风格方向：平涂海报·明快色块｜本例修长歌者仰头闭眼，细轮廓配硬边阴影和网点背景。 | cloudseaside；Krea相关作者；[精确版本](https://civitai.com/models/3061750?modelVersionId=3484739) · [本例作品](https://civitai.com/images/149889831) | 低权重保留2.5D；高权重可漂移颜色和构图 | 模型／版本全文、1张原图、3条作品元数据；未看权重对照组 |
| 解码组件 | [Krea-2 Bridged PixelHead：直接像素读出与解码阶段加速](#n05) | 解码优化·兼容排错｜了解Krea2像素读出头的接线、测量范围与适用声明。 | — | pocis／Wither033；FastFrames与Krea相关作者；[固定模型卡](https://huggingface.co/pocis/Krea-2-PixelHead/blob/2261f5f1a88f6038b8f9c870f0192855d931d5ca/README.md) · [配套节点](https://github.com/Wither033/ComfyUI-Krea2-PixelHead) | 24.7×是L4的768²解码比较，不是全流程倍率 | 卡全文、1张四组对比拼图；未审节点实现／运行 |
| 多参考工作流 | [Krita／ComfyUI套件：主体、风格与场景三槽参考](#n06) | 多图编辑·风格参考｜阅读Klein三槽参考与Krita图层工作流的输入边界。 | 设计思路：参考分工·图层衔接｜按主体、风格和场景分配输入，并用开关控制条件链。 | ZKGASMAS；Acly、BFL、SAM、SeedVR2及相关节点作者；[固定README](https://github.com/ZKGASMAS/krita-ai-diffusion-workflows/blob/571ab306334a38c93da26bd9e552e7f323a80a27/README.md) · [三槽API图](https://github.com/ZKGASMAS/krita-ai-diffusion-workflows/blob/571ab306334a38c93da26bd9e552e7f323a80a27/KCG/FLUX.2%20Klein%20Multi-Reference%20%26%20Style%20Transfer.json) | API图默认风格开、场景关；三槽不等于全启用 | README、依赖全文与一张API图关键节点；未运行 |
| 工作流阅读工具 | [Workflow Reader：将ComfyUI图读成提示、模型和节点清单](#n07) | 配方阅读·工作流整理｜从公开工作流查找提示、模型和被旁路节点的参数。 | — | a5ah1；ComfyUI、marked与DOMPurify相关作者；[固定README](https://github.com/a5ah1/comfy-workflow-reader/blob/e703813625244c03f8eaab1d37b3a7f4189a530a/README.md) · [作者页面](https://a5ah1.github.io/comfy-workflow-reader/) | 显示bypass／mute；自定义控件名可能需object_info | README全文；未打开应用／审隐私实现 |
| 角色数据集方法 | [Casting Call：分开固定身份、变化镜头和训练caption](#n08) | 角色训练·提示词组织｜区分身份特征、镜头覆盖与可变化内容的标注。 | 设计思路：身份与变量·景别覆盖｜固定角色外貌，按景别调整提示与训练caption职责。 | eehedth；Forge Neo与扩展相关作者；[原文章](https://civitai.com/articles/39535) · [作者源码入口](https://g.vkom.top/vadim/sd-forge-casting-call.git) | 生成prompt≠训练caption；人物一致性仍需筛图 | 文章正文全文及附件元数据；未读zip／源码／例图 |
| 社区训练经验 | [Krea2日系福瑞LoRA实践：Raw预融合与标注变化一起看](#n09) | LoRA训练·标注方法｜阅读Krea2角色训练经历，保留多项变化和未完训条件。 | — | 贴吧「想飞的鱼&」及参与讨论的吧友；[原帖与楼层](https://tieba.baidu.com/p/11219715117) | 个人未完训经验；架构解释与模型胜负未证实 | 首楼及1–16楼文字；未看图／楼中楼／训练文件 |
| Sena404增量 | [Sena404第31期：nel-zel formula标签与华丽材质示范](#n10) | 人物插画·画师标签｜参考高彩材质与装饰表现，区分标签和完整配方。 | 美术风格方向：高彩日漫·镜面材质｜本组大眼柔下颌，收腰体量配硬亮金属、分块发光与服饰层次。 | Sena404；画面署名nel-zel formula／ねるぜるF；[原视频](https://www.bilibili.com/video/BV13DyVzQExR/) · [系列历史索引](../2026-11-09/notes/Sena404画师串与相关分享.md) | 字面标签@nel-zel formula；未展示完整参数卡 | 53秒媒体，10张抽样／定点／末帧，十页卡片已看；无完整配方 |

## 当日分享

<a id="n01"></a>

### SugarPalette ANIMA v2：可爱插画的细节调整版

**适用方向：人物插画·模型选型｜阅读Anima合并版的可爱定位、采样建议和来源。**

**美术风格方向：甜美日漫·柔亮上色｜本例大圆眼与小鼻口，细线柔影配发束亮边和暖色环境。**

- 原作者与原文：Noginowa／のぎのわ；所列父模型、LoRA与工具作者；[固定模型卡](https://huggingface.co/Noginowa/SugarPalette-ANIMA/blob/4f1ce58dd2d62917fa2bdce95c1581a789cf327b/README.md)。
- 作者分享：SugarPalette ANIMA是Anima系列的合并模型，定位可爱插画；当前v2说明为调整整体细节。HF仓9月15日建立，本次固定revision `4f1ce58dd2d62917fa2bdce95c1581a789cf327b`于北京11月22日13:26:52更新；该时刻是仓库更新，不冒称权重首次发布日期。
- 公开来源：v2列FiaMix Reboot Cute1.7、Vetehine0.2 ANM、ClearPalette v1 Cute、PrismPalette v3，以及Anima Detail Tweaker的context_detailer_base10／rendering_detailer_base10；未给完整融合系数。不是独立新架构或证明优于父模型的实验。
- 作者通用建议：qwen_3_06b_base编码器、qwen_image_vae；CFG4–5（推荐4.5），20–40步（推荐32），ER-SDE/beta偏细节，Euler A/normal偏柔和。模型卡有正负提示模板及basic／advanced工作流入口，未把通用模板当下面咖啡馆图的逐图设置。
- 本库看图：[v2示范01](https://huggingface.co/Noginowa/SugarPalette-ANIMA/blob/4f1ce58dd2d62917fa2bdce95c1581a789cf327b/images/SampleImage_SugarPaletteANIMA_v2_01.jpeg)，实际查看1440×1136单张。女孩双手托脸，短圆脸、较宽眼距和大亮瞳，小鼻口与张口笑，肩部及上身以圆润体量塑造；发束细线和分块高光、肤色轻柔渐层，与木质咖啡馆暖光结合。仅据这一半身例归纳，不推断全身比例或v2相对v1.1收益。
- 读取与条件：主卡全文和该图已读，v2/v1.1 plot、第二张图、JSON和权重未取。按卡片沿用CircleStone Labs Non-Commercial License v1.2；父资源条款仍需分别遵守。感谢作者保留父资源署名。

<a id="n02"></a>

### MOSS FRAME SFT Detail Sixteen：16步摄影细节新训练

**适用方向：摄影质感·采样精修｜查阅MOSS SFT十六步LoRA的专用采样与补丁顺序。**

**设计思路：皮肤细节·高光控制｜按作者筛选结果，在近景纹理和鼻梁高光之间取舍。**

- 原作者与原文：Coffmeteor；FRAME与OpenMOSS相关作者；[固定版本说明](https://huggingface.co/Coffmeteor/MOSS-Image-Turbo/blob/e7de9a63635fa803b7f3bf9c321dd2b077491bc4/frame-sft-detail-16step-cfg1/README.md)。
- 作者分享：FRAME SFT Detail 16step-cfg1以4591张不同FRAME照片和原始SFT指导目标重新训练3035 updates，强调摄影皮肤细节与高光取舍。固定revision `e7de9a63635fa803b7f3bf9c321dd2b077491bc4`，北京11月22日23:49更新；旧的16step-cfg1仍在另一个目录，并非两个目录同名就同权重。
- 新版通用配方：原始OpenMOSS-Team/MOSS-Image-SFT，BF16 LoRA rank128/alpha128，强度1.0，16步、CFG1、ER-SDE/beta、shift5、无trigger、空负向。旧目录的Euler/simple建议不覆盖新版ER-SDE/beta。
- 已读[API图](https://huggingface.co/Coffmeteor/MOSS-Image-Turbo/blob/e7de9a63635fa803b7f3bf9c321dd2b077491bc4/frame-sft-detail-16step-cfg1/workflows/MOSS-FRAME-SFT-Detail-16step-cfg1-api.json)关键连接：MOSSImageHFLoader→LoraLoaderModelOnly→ModelSamplingSD3 shift5→KSampler→原loader的VAE→保存。图中1344×2368、seed1310437052、denoise1，正向为近景摄影描述，空负向；这是公开示范图设置，不是本库补值。未运行节点核对实际行为。
- 作者筛选：先在两条提示筛8组采样，再用另两条确认3组；RTX5080、1344×2368、固定16步／CFG1条件下，ER-SDE/beta中位41.35秒。它比同表ER-SDE/simple的41.29秒略慢，选中理由是作者报告的视觉取舍；不能写成普遍最快或人体修复模型。
- [release](https://huggingface.co/Coffmeteor/MOSS-Image-Turbo/blob/e7de9a63635fa803b7f3bf9c321dd2b077491bc4/frame-sft-detail-16step-cfg1/release.json)公布完整权重文件SHA-256 `31d435137a20311d4277e7b3b73d5b5927eb9d46d2869c7147a47a1fcac51e59`；本库只读声明，未下载权重计算。examples.json有两张完整提示和seed；LoRA Stack另有可选叠加图，本轮未读它的有效分支。主卡Apache-2.0，底模条件另看。
- 读取状态：主卡与新版卡全文、release、examples全文、API图关键节点；未查看两张原图／训练日志，不把作者描述作为本库视觉或性能验证。

<a id="n03"></a>

### CyBlue v1(e08)：普鲁士蓝与暖色点缀

**适用方向：人物插画·双色设计｜参考Anima蓝晒风格与暖色点缀的提示组织。**

**美术风格方向：蓝晒线描·暖色点睛｜本例蓝白发丝与衣褶成块，橙色眼睛和红日突出焦点。**

- 原作者与原文：lepetitprince716355；Anima相关作者；[精确版本](https://civitai.com/models/3061745?modelVersionId=3484732) · [本例作品](https://civitai.com/images/149889947)。
- 作者分享：《[Anima] CyBlue - Cyanotype Prussian Blue & Warm Spot-Color Style》，v1(e08)／版本3484732，北京11月23日03:22:50发布。作者以蓝晒、纸白高光和可控暖色点缀为目标，称在56次OOD渲染中选epoch8；这是作者评估说明。
- 通用推荐：`@cyblue`置首，随后空格分隔标签，不用下划线；作者建议略去masterpiece等质量填充词。强度0.85–1（推荐1），Anima base v1.0＋qwen_3_06b_base＋qwen_image_vae，40步、CFG4.5、ER-SDE/simple、shift3；896×1152或1344×896。作者提醒仅挂载就强烈偏普鲁士蓝；该规则不推广为其他Anima LoRA的通则。
- 本库看图：实际查看896×1344一张竖版人物像；本例尖收下颌、大而细长的眼、小鼻口、平静回望；胸肩以上被高领外套包裹，脸与发用蓝白清楚分区，细发线和硬边衣褶突出图形感，暖橙虹膜与红色日轮呼应。未由头像推断头身、肩胯和腿长；日轮是本图内容，不认定每张都出现。
- 训练公开：45图×3 repeats，rank32/alpha32，12epochs中选8（1080/1620steps）。卡片给完整文件SHA-256，未下载验证。权重沿Anima CircleStone Non-Commercial License v1.2，非官方背书。
- 读取状态：模型／版本说明全文、原图1张；另查该版本作品API3条，meta均null、modelVersionIds空，不能从关联检索结果补成逐图完整提示／配方。眼前图的尺寸也不改写成作者通用推荐尺寸。评论与评估原始记录未读。

<a id="n04"></a>

### Krea 2 CS Flat Palette Anime：从2.5D到平涂的权重取舍

**适用方向：画风搭配·平涂上色｜按Krea2 LoRA权重区分保留光泽与海报化处理。**

**美术风格方向：平涂海报·明快色块｜本例修长歌者仰头闭眼，细轮廓配硬边阴影和网点背景。**

- 原作者与原文：cloudseaside；Krea相关作者；[精确版本](https://civitai.com/models/3061750?modelVersionId=3484739) · [本例作品](https://civitai.com/images/149889831)。
- 作者分享：《Krea 2 CS Flat Palette Anime》，v1.0／3484739，北京11月23日03:46:04发布。目标是清楚赛璐璐阴影、锐边及明亮海报色盘，同时保留复杂背景内容。
- 作者方法：一般0.75–1为平涂范围，0.5较轻，1.25–1.5更强但会漂移服装／发色及构图。若配2.5D半写实提示和材质／轮廓光描述，0.25–0.5可保留人物光泽而背景趋于色块／网点；0.75–1则趋于全平涂。这是作者对其模型的建议，并非本库同seed扫权重结果。
- 公开测试条件：Krea2 Turbo int8，8步、CFG1、ER-SDE/simple，标签和长自然语言均测试；列848×1536、864×1520、1008×1296、992×1328、1152×1152。可选trigger `flt_style`。训练42图、30epochs／1260steps，batch1，dim32/alpha32，LR1e-4 constant，AdamW8bit，BF16、FP8底座和1024bucket。
- 本库看图：实际查看单张864×1520舞台歌者；本例窄肩收腰、修长四肢，脸轮廓简洁，下巴略尖，闭眼仰头张口唱歌，双手扶麦。细线、大片珊瑚红裙面与硬边暗部，青绿／黄粉色块和网点构成背景，光泽集中于耳机、麦克风及鞋。具体短发、裙装和表情只属于本例。
- 读取状态：卡全文及这一张原图已读，未查看作者称同seed／prompt的权重整组对照；作品API另3条meta均null、关联版本字段空，不补造此例强度、seed或正负词。版本API没有展开独立许可正文，后续使用需回资源页核权利条件，不把可下载视为任意再分发许可。

<a id="n05"></a>

### Krea-2 Bridged PixelHead：直接像素读出与解码阶段加速

**适用方向：解码优化·兼容排错｜了解Krea2像素读出头的接线、测量范围与适用声明。**

- 原作者与原文：pocis／Wither033；FastFrames与Krea相关作者；[固定模型卡](https://huggingface.co/pocis/Krea-2-PixelHead/blob/2261f5f1a88f6038b8f9c870f0192855d931d5ca/README.md) · [配套节点](https://github.com/Wither033/ComfyUI-Krea2-PixelHead)。
- 作者分享：27.49M参数、52.6MiB BF16的bridged直接像素头，从Krea2 SingleStreamDiT进入last.linear前的6144维目标图像token及去噪2×2 latent patch读出RGB；需剥离文本／风格参考token。HF仓北京11月23日00:52建立，revision `2261f5f1a88f6038b8f9c870f0192855d931d5ca`于02:48更新。
- 使用入口：作者要求MODEL线在KSampler前接Pixel Head Tap，以Pixel Decode替代VAEDecode；列支持Krea2、Turbo、Raw、FP8/INT8/GGUF及微调、风格参考输入。它不是可随意套给其他家族的通用VAE；本轮未审源码／实际加载，兼容性仅按作者声明。
- 指标边界：NVIDIA L4、768×768、40张留出fine-art样本，读出中位59.55ms对原qwen_image_vae的1468.9ms，24.7倍是解码阶段；PSNR33.33dB、LPIPS0.23也不表示逐像素相同。未在本库测总耗时、峰值显存或脸手质量。
- 本库看图：查看作者四组1:1裁切对比拼图的1500px缩览，肖像、手／织物、彩色插画和蚀刻均保留主色与布局，精细线条／纹理可见差异。缩览不足以独立复核像素指标或极细花纹，未将作者数值包装为本库实测。
- 读取与许可：主卡全文、hero拼图；节点README／实现、单组原生裁切、JSON未读。模型卡MIT；配套节点和基础模型许可需分别看，MIT不覆盖基础权重条件。权重未下载。

<a id="n06"></a>

### Krita／ComfyUI套件：主体、风格与场景三槽参考

**适用方向：多图编辑·风格参考｜阅读Klein三槽参考与Krita图层工作流的输入边界。**

**设计思路：参考分工·图层衔接｜按主体、风格和场景分配输入，并用开关控制条件链。**

- 原作者与原文：ZKGASMAS；Acly、BFL、SAM、SeedVR2及相关节点作者；[固定README](https://github.com/ZKGASMAS/krita-ai-diffusion-workflows/blob/571ab306334a38c93da26bd9e552e7f323a80a27/README.md) · [三槽API图](https://github.com/ZKGASMAS/krita-ai-diffusion-workflows/blob/571ab306334a38c93da26bd9e552e7f323a80a27/KCG/FLUX.2%20Klein%20Multi-Reference%20%26%20Style%20Transfer.json)。
- 作者分享：《Krita AI Diffusion & ComfyUI Workflows Suite》，仓库北京11月23日01:54建立；固定commit `571ab306334a38c93da26bd9e552e7f323a80a27`。包括Krita参数面板API图、Comfy可视图、上游参考图与波斯语指南，不把节点数或“production-ready”称谓当质量验证。
- 重点读三槽FLUX.2 Klein图：主体、风格、场景分别编码ReferenceLatent，先主体，再按开关串接风格及场景；默认风格True、场景False。CFGGuider从最终开关输出取条件，LoRA开关默认False；因此“有第三张输入”“有LoRA强度”不等于当前分支生效。
- 图以参考主体缩放结果GetImageSize驱动EmptyFlux2LatentImage／Flux2Scheduler尺寸，并有BasicScheduler/Flux2Scheduler分支。Krita参数和ETN_Krita输入／输出依赖tooling-nodes，直接移到Comfy需按作者说明换普通LoadImage、SaveImage；不能只凭JSON可读写成独立运行成功。
- 相关入口：README还列六槽SAM3.1角色／脸部编辑、SeedVR2画布RGB与独立图层RGBA、姿态迁移与风格重绘。这些仅按README概括，本轮未追其全部图或确认alpha修复实现。distilled与Base的CFG建议分开，依赖文档列4B/9B编码器和VAE，不推断所有模型任意互换。
- 读取状态：README及docs/DEPENDENCIES.md全文，三槽API图参数／条件／采样关键节点；未读波斯语长指南、其他JSON、源码或预览图。仓库MIT，附带上游模型／节点各自许可仍适用。未安装、编译、跑作者验证器或生图。

<a id="n07"></a>

### Workflow Reader：将ComfyUI图读成提示、模型和节点清单

**适用方向：配方阅读·工作流整理｜从公开工作流查找提示、模型和被旁路节点的参数。**

- 原作者与原文：a5ah1；ComfyUI、marked与DOMPurify相关作者；[固定README](https://github.com/a5ah1/comfy-workflow-reader/blob/e703813625244c03f8eaab1d37b3a7f4189a530a/README.md) · [作者页面](https://a5ah1.github.io/comfy-workflow-reader/)。
- 作者分享：《Workflow Reader》，仓库北京11月23日03:30:39建立，固定commit `e703813625244c03f8eaab1d37b3a7f4189a530a`。把JSON/API图及含工作流的媒体整理为可滚动文本，可复制提示、模型／LoRA强度、尺寸和节点参数，显示分组、子图与bypassed/muted标记。
- 学习价值：读别人工作流时先区分已连接、旁路和静音节点，再追踪提示正负关系；工具声称沿图标注正／负向，不等于它已证明生成时有效编码文本。损坏文件只回收可恢复内容，不能以部分解析当完整配方。
- 自定义节点往往只保存控件值列表；作者建议加载自己ComfyUI的object_info.json补名称。未提供节点定义时，不把推定控件名写成无歧义真实配置；定义和工作流版本也可能不同。
- 读取范围／许可：README全文，未操作网页、检查网络、导入样本或执行作者测试。浏览器本地处理、无上传／追踪为作者声明，未独立隐私审计。项目MIT，并说明内置标识来源于ComfyUI frontend GPL-3.0及依赖许可；不能把该工具作为本库新增已实现的校验体系。

<a id="n08"></a>

### Casting Call：分开固定身份、变化镜头和训练caption

**适用方向：角色训练·提示词组织｜区分身份特征、镜头覆盖与可变化内容的标注。**

**设计思路：身份与变量·景别覆盖｜固定角色外貌，按景别调整提示与训练caption职责。**

- 原作者与原文：eehedth；Forge Neo与扩展相关作者；[原文章](https://civitai.com/articles/39535) · [作者源码入口](https://g.vkom.top/vadim/sd-forge-casting-call.git)。
- 作者分享：《Casting Call: a Forge Neo extension that builds character LoRA datasets》，北京11月22日22:38:59发布、23日02:37:50更新。扩展把一次角色设定展开成多景别图与.txt caption，方便交给训练器，不是本库新训练流程。
- 方法要点：固定身份外貌与trigger，变化衣服、地点、光照、姿态和表情；默认30张分肖像12、半身9、膝上5、全身4，可改比例。近景prompt只提可见服装上部，避免用鞋等镜头外元素把画面拉远。
- Caption职责：默认只写变化内容，让固定外貌归入trigger；若希望之后用提示改变某个特征，可选Full模式。生成用的LoRA／embedding／style词不自动写入caption；wildcard需先展开，使标注对应当张生成请求。作者的规则是可学习取舍，并非所有人物LoRA都必须删除全部外貌词。
- 公开示范设置：附件Anna Volkova set9，作者报告SICK OLLIE Krea2 FP8、8步、CFG1、Euler/simple、无LoRA，30张及字符／运行记录，部分膝上镜头另换衣景重做。_run.txt和JPEG参数可回看，但本轮未下载验证图片一致性、caption质量或训练收益。
- 实用细节：按set版本保留模型／参数，删除不满意图后Skip existing只补缺图；可以txt2img Script接ADetailer/ControlNet。按同名稳定选择设定字段不等于保证像素身份一致，仍要看图筛选。
- 读取状态：文章正文全文、约9.8MB示例zip的元数据；源码入口、zip、图片与评论未读，精确扩展commit和许可未知。署名／可访问链接不构成打包转载或商业使用授权，本库仅作中文概述并引回原文。

<a id="n09"></a>

### Krea2日系福瑞LoRA实践：Raw预融合与标注变化一起看

**适用方向：LoRA训练·标注方法｜阅读Krea2角色训练经历，保留多项变化和未完训条件。**

- 原作者与原文：贴吧「想飞的鱼&」及参与讨论的吧友；[原帖与楼层](https://tieba.baidu.com/p/11219715117)。
- 作者分享：《这就是你的为什么应该用krea2爽炼lora》，实际规范吧名stablediffusion，首楼北京11月22日18:10:50。作者叙述从Anima full fine-tune转到Krea2角色／概念LoRA后的早期体会，值得参考其标注与资源组合变化。
- 按作者自述：先把未给精确版本的txtfusion／txtfussion LoRA融进Raw，再以约2.5万张图、dim128训练；从tag＋自然语言混合改成自然语言加一行概念tag。预计6epochs／约30万samples，发帖时约4万samples、尚不到1epoch；作者称常见角色及部分长尾角色开始响应。没有公开底模／预融合LoRA哈希、alpha、LR、训练器版本或完整caption。
- 本库学习备注：底模、预融合、训练方式、数据及标注同时变化，Anima原方案还是全参而Krea为LoRA，不能归因于单一编码器或判定家族全面优劣。首楼对Anima文本架构的个人解释未经源码核对，不作为架构事实转述。
- 社区反馈：可见回复既有类似体验，也指出Raw训练显存、素材质量和动作／分辨率问题；均为个人意见，不合并成通用硬件门槛或量化成功率。
- 读取状态：aiotieba4.8.2读取首楼日期／吧名与1–16楼文字，has_more=false；图片尤其二楼五角色合照、楼中楼、训练文件均未读，不写本库视觉还原判断。保留作者及吧友署名，回原帖看展示与后续。

<a id="n10"></a>

### Sena404第31期：nel-zel formula标签与华丽材质示范

**适用方向：人物插画·画师标签｜参考高彩材质与装饰表现，区分标签和完整配方。**

**美术风格方向：高彩日漫·镜面材质｜本组大眼柔下颌，收腰体量配硬亮金属、分块发光与服饰层次。**

- 原作者与原文：Sena404；画面署名nel-zel formula／ねるぜるF；[原视频](https://www.bilibili.com/video/BV13DyVzQExR/) · [系列历史索引](../2026-11-09/notes/Sena404画师串与相关分享.md)。
- 原视频《anima画师串第三十一期》，UID341674866，北京11月22日13:43:40发布，53秒；完整简介仅“-”。UID最新页总数89，系列从投稿30推进31；页面01/10–10/10是本片卡片页数，不当总期号。片内总期数字样被水印遮挡，本轮未可靠辨认，不据前几期自行补41；卡片日期可读2026.11.22。
- 字面标签：`@nel-zel formula`，封面／多个末页原帧已核，含连字符与中间空格，没有括号或数值权重。作者将ねるぜるF称为同人插画作者，列ONE PIECE等主题和图库统计；履历、图库量与作者原作风格未独立核验。
- 作者卡片要点：高饱和和镜面高光、金属／宝石锐利反光，装饰密度与胸腰对比突出，称画风迁移较强、强光源配华丽服饰适合；也提示极端动作和手部风险。“五官最稳”“回眸仰视完整”是作者对其组图的评价，不写成标签效果保证。
- 本库看图范围：10张独立抽样／定点／末帧覆盖01–10页；多例可见大眼、简化鼻口和柔收下颌，视线有直视／侧看，轻笑较多；腰身收束、胸部体量及长腿在部分角色更突出，另有更幼态比例，不能称全组同一头身。金属／宝石高光硬亮，头发亮边和织物褶层分明，海天／舞台等背景跟随高彩调性。不同角色装备、体型和姿态仍属各例设定，不当原画师全作品鉴定。
- 公开配置：本期画面没有完整底模、LoRA、编码器、VAE、seed、采样或正负提示卡；不继承第23／30期资源，单个标签不足以复现整组。媒体480×852是视频观看分辨率，不是生成图尺寸。
- 读取状态：SDK17.4.2完整元数据／简介，FFmpeg每10秒5张＋末秒1张，再9.5/19.5/29.5/39.5秒4张；OCR只作定位，人工对照十页和标签原帧。媒体主址567后仅用同一SDK一个备用，HTTP200、2472243bytes。平台zh-CN字幕login_required；未取音频／ASR、评论、原图或完整逐图配置。媒体／截图／OCR全文不提交。
- 与旧记录关系：增量回链[11月20日第30期](../2026-11-20/README.md#n10)及[历史基础索引](../2026-11-09/notes/Sena404画师串与相关分享.md)；旧期不重复统计。本轮仅整理分享，感谢Sena404及原画师，不把示范资源当可任意使用素材。

## 来源覆盖与检索记录

下面记录真实范围，不将一次列表、关键词无命中或API成功当作全平台／全文覆盖；主工具成功，本轮没有启动、查询或检查贴吧／B站备用工具依赖。

| 平台／入口 | 实际检查 | 读取与筛选结论 | 限制／未完成 |
|---|---|---|---|
| stablediffusion吧 | aiotieba4.8.2 CREATE页1／30；最新普通帖23日02:15，向前至20日13:15，跨上次成功水位 | 精读11219715117首楼及16楼文字，收N09；11219230791《今日moss》读取9个可见楼层文字 | 今日moss关键内容在图片，未看，不用点赞／光影好评充当本库看图结论；楼中楼未读 |
| stable diffusion别名 | 同工具带空格名称页1／2核入口 | 仍返回stable吧2018公告，名称解析异常 | 不当正确重定向、不据此说SD吧无新增 |
| comfyui吧 | CREATE页1／30；最新普通帖23日00:21，向前至18日14:13，跨上次水位；读11220363513 | h3 sigmas首楼公式可读，但约束段丢失／不完整，且只是作者拟合，没有成图证据，保留覆盖不精选 | 未将几何步距公式当H3通用最优采样；整合包推广不按标题收录；其他求助图片未读 |
| 贴吧全站最新补充 | “工作流 提示词”“模型 LoRA”“教程 分享”各页1，30／30／27条 | 核吧名与首楼日期，按tid去重；旧置顶、跨吧营销与重发混杂，相关原帖按需读 | 搜索返回并非全按首楼日期单调，不能用一条旧帖宣称分页完整；两吧CREATE水位另核 |
| bilibili广泛搜索 | SDK17.4.2 pubdate：“ComfyUI 教程”页1–5各20；“生图 模型”“Anima 生图”“LoRA 画风”各页1／20 | ComfyUI页1为22日18:15–23日01:09，页3到21日20:48，已跨上次22日04:00；页4–5额外回看到21日13:56。模型页有23日新稿；Anima、LoRA页含较旧命中 | 完整搜索description只作候选，不冒称视频正文；大量重复营销剔除，未宣称全站穷尽 |
| bilibili具体原文 | Sena UID341674866页1／30，总数89，最新第31期；读BV13DyVzQExR与BV16jyjzrEym完整简介 | Sena媒体／十页卡片见N10；蓝色多脑盒《moss-image高清修复》23日01:09、670秒，简介说明部分工作流需会员解锁提取码，暂留线索 | 后者未取章节／字幕／媒体／网盘，不凭“1600w像素”“完美质感”标题推荐；Sena字幕需登录，本轮无ASR／评论读取 |
| Reddit | r/StableDiffusion/new.json 50、r/comfyui/new.json 30；英文类别＋Nov21/22日期域名搜索 | 两个列表403；打开metalfans的Qwen Omni Turbo发布帖及subject/environment showcase帖的可见正文，后者标明Claude协助解释 | 当前选择不重复把个人测试当本库收益；4步MOSS检索命中Nov19旧帖。未读全评论、云盘JSON、示范媒体或核作者benchmark，列表受限与具体页可读分开 |
| Hugging Face | 文生图最新80、图像编辑最新30，Anima／Illustrious／NoobAI各latest15；按线索取固定卡 | SugarPalette、MOSS FRAME、KreaPixelHead三卡与精选小JSON；Sugar／Pixel示范已看；跨家族NPU／量化等按信息量筛选 | Anima包含animal等误匹配；IL／Noob有镜像／旧资源，未据检索数声称有同量新品；不下载权重 |
| GitHub | comfyui workflow pushed>=11月22日最新25；comfyui prompt created>=11月21日最新15 | 固定commit读Workflow Reader和Krita套件，后者补依赖全文及三槽图关键连接 | README的隐私／兼容／性能为作者声明，未运行网页、审完整实现或执行测试；不安装其服务 |
| Civitai文章／教程 | Newest文章30；39535、39491、39484具体正文 | Casting Call全文精选；Tips for creating LoRAs把观察他人作品推为多阶段训练，缺验证，不当教程事实；Quick Reference的实质表格在图中未读 | Casting附件仅元数据，没读取zip／源码；作者评论区未读，不称已覆盖全部经验讨论 |
| Civitai模型／版本 | Newest模型40；3061764、3061745、3061750完整说明及版本 | CyBlue／Krea Flat精选；AniDetail MBW IL读到base/in/mid/out权重与输出块细纹／背景噪点局限，未取配置或看对照，暂不作为已证实增强教程 | 版本讨论／评论未读；父资源许可声明不代替逐项核权利；模型名称不是视觉证据 |
| Civitai工作流／作品 | Newest Workflows15；3061641说明全文；CyBlue／Flat各作品API3条及各1张原图 | Universal Conditioner依赖自定义hidden_states端点与常驻27B，仅适合已运行大LLM的条件，README式说明不足以推为低显存通用法，未精选；两张实际看图见N03／N04 | 作品API meta均null、版本字段空，带配方作品未取得完整配方；不把通用设置拼成某图实值，没读所有作品 |
| 其他来源 | Comfy论坛latest.json，note.com ComfyUI最新15 | 论坛200、最新列表含22日Ltxv求助和旧主题；note.com403 | 未把下线公告当本轮HTTP失败；没读论坛主题正文／Discord，note是访问受限，非无优质新增 |

Reddit具体入口：[metalfans发布帖](https://www.reddit.com/r/comfyui/comments/1y2fuu9/release_8step_turbo_lora_for_qwenimage21/)、[subject/environment工作流帖](https://www.reddit.com/r/comfyui/comments/1y2whvb/updated_my_subjectenvironment_showcase_workflow/)。后者搜索索引标11月22日，原页读取限可见正文，不写精确首发时刻。Civitai未精选原文：[39491](https://civitai.com/articles/39491)、[39484](https://civitai.com/articles/39484)、[AniDetail MBW v1.0](https://civitai.com/models/3061764?modelVersionId=3484755)、[Universal Conditioner工作流](https://civitai.com/models/3061641?modelVersionId=3484597)。

## 后续关注与维护

- Sena系列推进至投稿31；此次片内总期号被水印遮挡，没有沿编号规律补写。优先跟进作者补充的逐图prompt／精确模型与新期，旧期历史冻结记录保持。
- Sugar v2的融合比例／对比组、MOSS FRAME的采样样本与训练日志、风格LoRA同seed权重组、Krita其他图及Reader解析实现，均属于尚未读取范围；有实质新增再补，不安排自动生图实验。
- PixelHead倍率仅限作者指定解码基准，MOSS时间表仅限指定显卡／四个提示；不把加载／解析／归档成功当效果、兼容性或用户认可。
- 本轮保存为中文概述与必要参数索引，媒体、截图、完整转录、凭据与签名URL不入库。当天正文先保存，再更新总索引、日期入口与Sena跟踪水位；保存后以远端读取核对为准。

[返回日期索引](../README.md) · [返回总索引](../../每日检索可速查总结.md)
