# 2026-11-18 每日社区发现

本页汇总社区作者公开分享，感谢模型、工具、教程与原画作者的投入。本文是本库的中文概述与导读，保留署名、原文及实际读取范围；欢迎回原帖阅读完整教程、示范、许可和后续更新，支持原作者。署名／链接不等于转载授权，相关成果不作为本库原创。

- 北京日期与实际检索时间：2026-11-18，04:04起读最新规范，04:05起逐平台查近期分享并补读原文；归档前完成下列所记阅读。
- 类型：无具体差距要求的每日广泛发现，本轮无另设主动专题。
- 状态：整理12项主题，含续训更新、近期首次收录及社区讨论；部分入口受限。未安装节点、下载生图模型、启动生成／训练、增加运行服务或派发子代理。
- 时间窗：优先接续11月17日各平台成功读取水位（约04:01起）以来的新增／实质变化；既有项目新阶段与旧建仓资料首次收录保留原始时间，不把最后修改当首发或训练完成。
- 标注：适用方向和美术／设计摘要属于本库整理；原作者说明、社区反馈、本库实际看图与运行验证分列，归档不等于成图或收益验证。

## 今日值得阅读

- **模型与后训练**：[GleamPalette v3](https://huggingface.co/Noginowa/GleamPalette-ANIMA)可看半写实人物与柔光示范；[HomeIMG新阶段](https://huggingface.co/cpral/HomeIMG-1.2B-PL-EN-epoch49.2-DanceOPD2048)公开续训／蒸馏条件；[GlyphAnchor](https://github.com/FireRedTeam/GlyphAnchor)提供字形与位置条件的不同基座版本。
- **工作流与边界**：H3 ControlNet迁移记录区分可加载和可控制，Turing FP16实践保留溢出条件；另有LM Studio提示分工、姿态衣装参考、H3训练入口与Pixaroma分任务教程。
- **画风与提示实践**：[Sena404第29期](https://www.bilibili.com/video/BV1v5sz6YEDV/)已核`@azasuke`和关键卡；[MOSS长提示词试验](https://www.bilibili.com/video/BV1YisB6bEST/)按信息增量理解，不把字数或像素变化直接当质量。

## 分享速查

| 类别 | 分享／资源与版本 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点／可学习经验 | 读取状态 |
|---|---|---|---|---|---|---|
| Anima合并模型 | [GleamPalette ANIMA v3：柔光与半写实人物](#n01) | 人物插画·模型选型｜参考柔光人物表现，并查阅v3合并来源。 | 美术风格方向：半写实日漫·柔光渐层｜两例大眼柔下颌、细眉小口，皮肤与衣料用光塑体。 | Noginowa；CyberRealistic、Vetehine、PrismPalette、Detail Tweaker及工具作者；[固定模型卡](https://huggingface.co/Noginowa/GleamPalette-ANIMA/blob/5fde367bf34ca47610ee4411e9e6b99d3734b731/README.md) | 合并资源而非新训练声明；两张v3示范已看 | 卡片全文、2张原示范；未运行 |
| 续训与蒸馏更新 | [HomeIMG epoch49.2 + DanceOPD2048：蒸馏仍用50步](#n02) | 后训练研究·双语模型｜跟踪小模型续训与on-policy蒸馏的真实设置。 | — | cpral／adamo1139；Poziomka、BFL与数据作者；[固定模型卡](https://huggingface.co/cpral/HomeIMG-1.2B-PL-EN-epoch49.2-DanceOPD2048/blob/09879f51b45e13f357e766705997a43a282fd85b/README.md) | 接续epoch46记录；新阶段不是少步蒸馏 | 波兰文卡片全文；未看网格／运行 |
| 文字渲染后训练 | [GlyphAnchor：把字形条件放到目标位置](#n03) | 文字排版·图像编辑｜了解中英文长文本与字形位置条件的接入方式。 | 设计思路：字形与布局锚定｜先确定文字形状和位置，再融合图像材质与风格。 | Qiang Xiang等；FireRedTeam／innerway及基座作者；[固定模型卡](https://huggingface.co/innerway/GlyphAnchor/blob/261d11769f53411b704d551b19672767b8530331/README.md) · [固定README](https://github.com/FireRedTeam/GlyphAnchor/blob/e31616b40c64e776d8e3819e25e8781fa256ada6/README.md) | 三种基座各有专用权重；文字保真与视觉质量分评 | HF卡片与GitHub README全文；未看图／运行 |
| 结构控制迁移／失败记录 | [H3 Image + Fun ControlNet：加载与控制分开核](#n04) | 结构控制·兼容排错｜阅读视频控制分支迁移到图片模型的失败边界。 | — | akhaliq；MiniMax、alibaba-pai、VideoX-Fun与P-H3工具作者；[固定模型卡](https://huggingface.co/akhaliq/MiniMax-H3-Image-Fun-Controlnet-Union-2.0/blob/18e5f8ddc3d5a07e65b55852df525ed16d58c0ac/README.md) | 后文修正前段归因；图片原生路径仍未证实控制 | 模型卡全文含后续试验；未读脚本／看图／运行 |
| 精度与低显存实践 | [MOSS Turing INT8+FP16：快路径与溢出取舍](#n05) | 资源选型·兼容排错｜查阅Turing上的FP16加载及高分辨率溢出条件。 | — | mkrgg；KBlueLeaf、OpenMOSS与ComfyUI作者；[固定模型卡](https://huggingface.co/mkrgg/MOSS-Image-Base-INT8-FP16-Turing/blob/166a9550d3a7de1a58ade7347a22e151d5d186ce/README.md) · [固定节点README](https://github.com/mkrgg/ComfyUI-MossFP16/blob/3957b56d3fce4e9b87d3bf24391e721da1fd2551/README.md) | 官方Base、folded Base与heal分开；clamp可能留伪影 | HF与节点README全文；未核源码／测速 |
| 提示组织节点／工作流 | [LD Prompt Writer 1.1.3：参考描述与图生图区分](#n06) | 提示词组织·参考分工｜按人物、姿态和光色选择参考信息，再切换模型写法。 | 设计思路：参考属性分工｜逐图选择身份、表情、镜头与色光，不把所有信息混写。 | damidero；Civitai发布者antonnfx；LM Studio及上游作者；[固定README](https://github.com/damidero/ComfyUI-LD-PromptWriter-LMStudio/blob/1419b0ca61f9a4b9f446bc3ea51c2b4409e7dee7/README.md) · [v1.1.3工作流](https://civitai.com/models/3055805?modelVersionId=3476397) | LLM参考与i2i底图是两条路径，LoRA按基座另选 | README与资源说明全文；未看图／读完整JSON |
| 姿态／服装参考管理 | [Pose & Outfit Reference：图像与描述独立复用](#n07) | 姿态参考·提示组织｜分别挑选姿态和服装，并输出可编辑描述。 | 设计思路：姿态与衣装拆分｜用两路参考管理动作和服装，再按任务接入条件节点。 | artokun；原图库ギア／@giaaibusi；中文整理Anhao；[固定README](https://github.com/artokun/ComfyUI_PoseGenerator/blob/b6d37f3257772dff1fba07305df8e34ae8eaf721/README.md) | 只是参考浏览／提示节点；公开包不附原图库 | README全文；未取图库／看截图／运行 |
| H3 LoRA训练工具导读 | [H3-Image LoRA Portable：实验流程与硬件边界](#n08) | LoRA训练·配置选型｜查阅Windows便携训练入口与已测硬件范围。 | — | damienjourdan；Civitai分享者PhotobAIt；Ostris、Fizgig与MiniMax作者；[固定README](https://github.com/damienjourdan/h3-image-lora-portable/blob/f4d6a0eb865bbe8cf7b8d4f0197fed333fe04bfe/README.md) · [社区原帖](https://civitai.com/articles/39015) | 已测Standard路线不代表全部实验选项已验证 | README与社区短文全文；未读手册／运行 |
| 社区工作流教程 | [Pixaroma Ep43：H3 Image与FIBO2分任务流程](#n09) | 工作流选型·局部编辑｜按文生图、参考组合和框选修图查教程入口。 | 设计思路：任务与提示形式匹配｜H3场景文字与FIBO结构化描述分别组织，明确保留项。 | pixaromadesign／Pixaroma；MiniMax、Bria及相关作者；[原帖](https://www.reddit.com/r/comfyui/comments/1xyogw8/minimax_h3_image_and_fibo_2_in_comfyui_14_free/) · [第43期原教程](https://workflows.pixaroma.com/ep/43/) | 两模型各7类任务；同场景比较采用各自提示并挑4中最佳 | 原帖正文、教程目录／条件及部分提示段；JSON未读 |
| B站长提示词实践 | [MOSS中文长提示词：信息增加与字数效果分开](#n10) | 提示词组织·比较方法｜阅读嵌套长描述试验，区分信息增量和长度结论。 | 设计思路：先补关键条件｜先说明人物、场景和用光，再按需求补材质细节。 | 星辰大海Rest；[原视频](https://www.bilibili.com/video/BV1YisB6bEST/) | 6场景×6档；像素差不是质量分，500字不作通用阈值 | 完整简介、41帧OCR、15帧观察与ASR草稿；未复跑 |
| Sena404画师串增量 | [Sena404第29期：azasuke的光泽与装饰材质](#n11) | 人物插画·画师标签｜参考本组人物与材质表现，保留动态结构局限。 | 美术风格方向：日漫厚涂·材质分层｜本组圆脸亮眼与厚重护甲并见，强光区分金属和织物。 | Sena404；azasuke／Azasuke Wind及原画师；[原视频](https://www.bilibili.com/video/BV1v5sz6YEDV/) | 投稿29／片内39分别记；字面标签@azasuke已核 | 完整简介、54秒媒体、13帧与OCR；未取逐图配方 |
| 贴吧打标经验讨论 | [近义标签打标：保留意见分歧与模型条件](#n12) | LoRA训练·标签整理｜阅读近义动作与表情标签的处理分歧。 | — | 贴吧用户_00ZEXC1；zhry02、◆旧梦◆、Steve12089、貓師傅等吧友；[原讨论](https://tieba.baidu.com/p/11204532695) | 社区建议互有分歧；不推出通用一对一或全打规则 | 首楼与4条可见回复；未取基座／日志 |

## 当日分享

<a id="n01"></a>

### GleamPalette ANIMA v3：柔光与半写实人物

**适用方向：人物插画·模型选型｜参考柔光人物表现，并查阅v3合并来源。**

**美术风格方向：半写实日漫·柔光渐层｜两例大眼柔下颌、细眉小口，皮肤与衣料用光塑体。**

- 原作者与原文：Noginowa，[GleamPalette ANIMA v3](https://huggingface.co/Noginowa/GleamPalette-ANIMA/blob/5fde367bf34ca47610ee4411e9e6b99d3734b731/README.md)。HF仓库7月18日建立，北京11月17日19:03更新；本次首次专题收录v3，未核v3权重首发时间，不以更新日冒称新训练。
- 作者定位：Anima系列合并模型，略偏半写实、柔和光线渐层与细致背景；v3比v2更偏写实。公开来源为CyberRealistic Anima v3.0、Vetehine Crimson Oath v0.2 ANM、Dreamland v0.1 ANM、PrismPalette ANIMA v3，加两种Detail Tweaker；未给合并比例，不补造配方。
- 本库实际看图：[示范1](https://huggingface.co/Noginowa/GleamPalette-ANIMA/resolve/5fde367bf34ca47610ee4411e9e6b99d3734b731/images/SampleImage_GleamPaletteANIMA_v3_01.jpeg)与[示范2](https://huggingface.co/Noginowa/GleamPalette-ANIMA/resolve/5fde367bf34ca47610ee4411e9e6b99d3734b731/images/SampleImage_GleamPaletteANIMA_v3_02.jpeg)。两例人物脸颊圆润、下颌柔收，大亮眼配睫毛、细眉和较小鼻口，含蓄微笑；发束细线高光，皮肤、袖褶和布料以柔和明暗塑体，背景木纹、植物、店面细节密。第一例托腮，第二例上半身正面，两例都不足以归纳全身体型／头身；棕发双马尾和衣装是示范角色设定，不当整个模型稳定特征。
- 作者通用推荐：Qwen3-0.6B base编码器与Qwen Image VAE，CFG4–5（4.5）、20–40步（32），ER SDE／Beta，柔软观感可选Euler A／Normal；正向示例含质量／评分／年份与scenery，可选realistic，负向列解剖与背景等约束。这些不是两图逐张原生参数，未取得各图seed、完整提示与元数据。
- 读取状态：固定卡片全文及两张作者原JPEG；未看v2/v3比较图、读完整JSON或权重。CircleStone Labs非商用v1.2与上游资源条件分别保留。与[PrismPalette v3](../2026-11-15/README.md#n03)存在合并来源关系，不是其重命名量化。

<a id="n02"></a>

### HomeIMG epoch49.2 + DanceOPD2048：蒸馏仍用50步

**适用方向：后训练研究·双语模型｜跟踪小模型续训与on-policy蒸馏的真实设置。**

- 原作者与原文：cpral，[HomeIMG-1.2B-PL-EN-epoch49.2-DanceOPD2048](https://huggingface.co/cpral/HomeIMG-1.2B-PL-EN-epoch49.2-DanceOPD2048/blob/09879f51b45e13f357e766705997a43a282fd85b/README.md)，北京11月17日00:47建仓、18日01:42更新。接续[11月10日epoch46](../2026-11-10/README.md#n03)：本次新增更高分辨率续训和Klein教师on-policy蒸馏阶段，不重报成从零首训。
- 结构与训练：1.24B DiT去噪器、72.1M可训练文本refiner，冻结Poziomka编码器，整管线不止1.2B。epoch49.2在256/512/1024分辨率续训，token比例1:1:4、shift1.5/3/6；随后2048步×48轨迹，共98304轨迹／教师查询，教师为FLUX.2 Klein base4B INT8、CFG4，学生波兰语／英语各半，教师用英文原文。
- 方法边界：学生以16步Euler轨迹产生状态，Beta(1,1)按步索引均匀取样，不等于shift后物理时间均匀；匹配教师velocity，不是直接学习教师最终图片。DanceOPD名称来自实现选项，作者明确不是严格复现论文默认Beta(5,2)。约14小时／7张3090Ti为作者训练记录，未独立核日志。
- 生成仍推荐**1024方图、Euler50步、CFG3、time shift6**。CFG1较省但不等同画质；此处不是1步／数步蒸馏。导出默认shift固定，不随分辨率自动缩放。需要custom pipeline与支持AutoencoderKLFlux2的Diffusers，不冒称原生ComfyUI开箱可用。
- 作者评估：公开8／36题网格，36题取自训练来源FLUX-Reason的前36例，不是独立新提示基准。承认重物体、计数、文字、小脸／手部问题，最终OPD MSE0.16–0.18不是画质分，本次未看网格或复算。
- 读取状态：固定波兰文卡片全文、本库中文概述；未读取训练源码、英文版全文或运行。去噪器／refiner代码Apache2.0，Poziomka另为openmdw1.1，组件与数据许可不合并推断。

<a id="n03"></a>

### GlyphAnchor：把字形条件放到目标位置

**适用方向：文字排版·图像编辑｜了解中英文长文本与字形位置条件的接入方式。**

**设计思路：字形与布局锚定｜先确定文字形状和位置，再融合图像材质与风格。**

- 原作者与原文：Qiang Xiang、Shuang Sun、Binglei Li、Yibo Chen、Xu Tang、Yao Hu、Junping Zhang，[GlyphAnchor](https://huggingface.co/innerway/GlyphAnchor/blob/261d11769f53411b704d551b19672767b8530331/README.md)；HF北京11月17日18:42建立、18:54更新，代码仓库10月已建立，本次首次收录，未当当天论文首发。
- [方法文档](https://github.com/FireRedTeam/GlyphAnchor/blob/e31616b40c64e776d8e3819e25e8781fa256ada6/README.md)：将渲染字形patch编码成视觉tokens，经基座原生位置编码锚定到目标布局，和提示／噪声目标／可选源图共同处理；分阶段监督训练从真实裁切过渡到渲染字形，再用DiffusionNFT的文字布局、风格与融合奖励后训练。此为作者方法介绍，未核实现或论文细则。
- 三路分别是Z-Image文生图、FireRed-Image-Edit-1.1编辑、Qwen-Image-Edit-2511编辑，不能把后者自动升级称Qwen2.1适配。权重并非一个通用LoRA跨三架构直接互换。
- 输入可用预定JSON布局：框为归一化`[left, top, width, height]`，参考路径相对JSON；也可接VLM规划。rewrite guess会补创画内文字，enrich要求保留既定文字再丰富视觉，这是两种不同任务。自动规划需自己的服务／API配置，非所有路径都离线无依赖。
- 作者评估按文字NED、词F1、短语命中与MLLM视觉分分别报告；InfoTextBench133例、每提示4图，中文罕见字另分级测，数字是作者／论文表格，不是本库验证。代码TODO仍将InfoTextBench列待发布，不把有结果表当测试集已完整公开。
- 读取状态：固定HF模型卡与固定GitHub README全文；没看teaser、模型输出、论文全文或JSON实例，未安装／运行。HF卡片标Apache2.0，使用仍需核对应基座许可与资产条件。

<a id="n04"></a>

### H3 Image + Fun ControlNet：加载与控制分开核

**适用方向：结构控制·兼容排错｜阅读视频控制分支迁移到图片模型的失败边界。**

- 原作者与原文：akhaliq，[MiniMax-H3-Image + Fun ControlNet-Union 2.0](https://huggingface.co/akhaliq/MiniMax-H3-Image-Fun-Controlnet-Union-2.0/blob/18e5f8ddc3d5a07e65b55852df525ed16d58c0ac/README.md)，北京11月17日13:52建立、18日02:57更新。本次按社区迁移／失败记录收录，不标为已经成功训练的H3 Image ControlNet。
- 作者最初记录：视频训练分支144 tensors可加载，scale0与基座逐像素一致；提高scale使输出变化，但Canny或左右圆形的空间结构没有跟随。接线、数值变化与真正控制是不同证据。
- **按文档后续段落读结论**：前段曾将障碍归为6步蒸馏轨迹；后续换非蒸馏原生image head、32步shift12，以及移植P-H3控制方案，仍没得到原生图片DiT的有效控制。因此作者把解释更新为视频到图片主干激活分布差异，不能只摘开头“唯一障碍是蒸馏”。该解释仍是作者分析，非本库独立机制验证。
- 可用与未可用分开：作者在视频管线用22帧重复控制图、40步、guidance1获得控制，开关对比由其提供；这依赖视频模型栈，不等于6步H3-Image工作流直接成功。P-H3-Image另有作者推荐的Comfy控制包，基座／分支v1和v2都须分清。本库未复核其“无训练路径不存在”等全称结论，只保留此轮所试路线失败。
- 作者提出冻结图片主干、继续训练控制分支的方案和成本估计，尚非已完成适配结果；没有启动训练或下载文档所涉巨量视频权重。非官方封装，许可沿MiniMax及ControlNet原条件。
- 读取状态：固定模型卡全文（含native与ph3后续段）；未读实验脚本、热图、原图或复算PSNR／edge-NCC。与[11月15日角色替换LoRA迁移](../2026-11-15/README.md#n10)不同：ControlNet是运行时并行分支，不按普通LoRA离线差量合并推理。

<a id="n05"></a>

### MOSS Turing INT8+FP16：快路径与溢出取舍

**适用方向：资源选型·兼容排错｜查阅Turing上的FP16加载及高分辨率溢出条件。**

- 原作者与原文：mkrgg，[MOSS-Image Base & heal on Turing (INT8 + FP16)](https://huggingface.co/mkrgg/MOSS-Image-Base-INT8-FP16-Turing/blob/166a9550d3a7de1a58ade7347a22e151d5d186ce/README.md)，北京11月17日11:08建仓、23:18更新；由Reddit当日检索发现同名实践线索后补读HF与[节点说明](https://github.com/mkrgg/ComfyUI-MossFP16/blob/3957b56d3fce4e9b87d3bf24391e721da1fd2551/README.md)。本条为量化／精度封装和加载实践，不是作者新训练基座。
- 作者方法：保留ConvRot INT8线性权重，其他路径使用FP16，在无原生BF16的Turing上避免相关FP32开销；节点在加载期间改允许dtype，并处理重载。作者给ComfyUI0.45、Triton3.2和PyTorch2.9.1+cu130条件，不能只加一个全局fp16参数就认为量化路径等价。
- 三种资源区别：官方Base未fold，FP16 residual接近上限；KBlueLeaf FP16-fixed的folded Base与heal另有数值条件。clamp将残差约束到±65504可避免某类NaN，却可能导致伪影；高分辨率叠LoRA会改变裕量，不能把“没黑图”当画质完整。
- 作者2MP／RTX2060SUPER记录官方Base约6.64s/it、folded INT8-FP16约4.78s/it；25步、seed614001632771110、1936×1088、CFG3、ER-SDE/simple、SLG关、无LoRA，另有指定编码器／VAE。单作者硬件与方案耗时，不推广到全部GPU或LoRA负载。
- 文档按分辨率拟合溢出边界和列举高分辨率失败，但作者也保留seed／提示波动；本库没重算曲线、核张量或比较图片，因此不固化约5.86MP为通用安全线。节点与README声明由AI辅助生成，相关机制／实测仍按作者报告记录。
- 读取状态：两份README全文、公开条件及报告表；未读源码／PR、看图或复跑，未下载模型。权重／衍生版本与上游许可分别查阅。

<a id="n06"></a>

### LD Prompt Writer 1.1.3：参考描述与图生图区分

**适用方向：提示词组织·参考分工｜按人物、姿态和光色选择参考信息，再切换模型写法。**

**设计思路：参考属性分工｜逐图选择身份、表情、镜头与色光，不把所有信息混写。**

- 原作者与原文：damidero，[LM Studio Prompt Writer (LD)](https://github.com/damidero/ComfyUI-LD-PromptWriter-LMStudio/blob/1419b0ca61f9a4b9f446bc3ea51c2b4409e7dee7/README.md)，北京11月16日14:56建仓、17日16:56更新；antonnfx发布的[Civitai工作流v1.1.3／3476397](https://civitai.com/models/3055805?modelVersionId=3476397)于17日14:55发布。保留两处账户署名，未据相似内容认定同一自然人。
- 作者方法：本地LM Studio将短想法或最多8张参考转成提示，Krea2用自然语言、Illustrious用Danbooru式标签；Config与Writer协作，已有正向文本时按原文使用，不再次调用LLM。
- 每图用Person／Expression／Pose／Camera／Lighting／Colors等开关选信息；改图或开关后重新描述，描述缓存绑定对应图和属性。**没有打开任何开关时默认使用除Camera外所有信息**，不是“没有贡献”。两轮模式是再次审阅全部条件，不是两次生图。
- 重要分路：Base Image i2i经VAE影响生成，LLM默认看不到该底图；若要其描述信息，需要另把同图加载到Writer参考并选属性。相机等控件和参考开关还有优先关系，不能把界面中放了一张图就认定视觉编码参与提示。
- 条件：视觉LLM必须有mmproj；作者建议固定Instruct模型、max_tokens2048，避免Thinking返回截断／空词。LLM seed和生图seed不是一回事。模型切换会静音不用分支，不会让Krea2 LoRA自动兼容Illustrious。
- Civitai列LD1.1.3+、LoRA Manager及具体Krea2／Illustrious、编码器／VAE条件；可选PlaySound不当核心生图依赖。读取状态为固定README全文和Civitai资源描述／版本元数据，未核完整工作流接线、最终编码文本或插件实现，未启动LM Studio／ComfyUI。

<a id="n07"></a>

### Pose & Outfit Reference：图像与描述独立复用

**适用方向：姿态参考·提示组织｜分别挑选姿态和服装，并输出可编辑描述。**

**设计思路：姿态与衣装拆分｜用两路参考管理动作和服装，再按任务接入条件节点。**

- 原作者与原文：artokun，[Pose & Outfit Reference for ComfyUI](https://github.com/artokun/ComfyUI_PoseGenerator/blob/b6d37f3257772dff1fba07305df8e34ae8eaf721/README.md)，北京11月17日13:24建立、14:09更新，首次收录。
- 来源归属：作者明确只做独立ComfyUI接入，原姿态／服装图库来自[ギア](https://ai-pose-gallery.pages.dev/)与[服装图库](https://ai-costume-gallery.pages.dev/)，中文项目来自[Anhao](https://github.com/anhao/ai-pose-gallery-zh)。图库、元数据及衍生描述不因接入代码MIT就变成可任意分发素材。
- 方法：独立选择pose和outfit，可覆盖文字而不更改图像；输出两路IMAGE、合并positive STRING、单独pose／outfit文本。模板`{subject}, {pose}, {outfit}, {extra}`是字面替换，不执行代码；实际图像控制还需接所选模型的条件节点，节点本身不生成成图。
- 公开包没有捆绑原图库；README称原站当前禁止批量下载／再分发，自动图库设置仍等许可，用户需放自己有权使用的图与catalog。研究目录统计的1439姿态／1407服装不当成随包可下载资源。
- 选None输出1×1黑占位，应留不接；不以黑图占位推断一个有效姿态输入。文字预览四节点示例无需模型，但不据此推断任意生成流程无需显存。
- 读取状态：固定README全文，未读取THIRD_PARTY完整条款、catalog、截图、JSON或源码，未批量抓取原图库，也未安装节点。

<a id="n08"></a>

### H3-Image LoRA Portable：实验流程与硬件边界

**适用方向：LoRA训练·配置选型｜查阅Windows便携训练入口与已测硬件范围。**

- 原作者与原文：damienjourdan，[H3-Image LoRA Portable](https://github.com/damienjourdan/h3-image-lora-portable/blob/f4d6a0eb865bbe8cf7b8d4f0197fed333fe04bfe/README.md)，北京11月17日18:19建仓、18日01:45更新；发现入口为PhotobAIt的[H3 image lora trainer](https://civitai.com/articles/39015)，平台发布时间17日04:16。两个平台时间分别保存，早发帖不等于当时此revision已存在。
- 工具定位：ai-toolkit训练后端，Gradio替代官方Next.js界面，Windows本目录准备工具和依赖；“便携”不等于没有模型／环境下载或磁盘开销。README列24GB NVIDIA、建议64GB RAM、约80GB磁盘、目录无空格，七语言手册另存。
- 已测范围：作者仅在Windows11／RTX3090用Standard、INT8基座、35%层卸载RAM验证；fast512和标实验选项未实测。表中1024+1536训练INT8约4–6.5秒/步、VRAM19.6–20.6GB；w4a8约15.2秒/步／19GB，说明更低精度不在其环境自动更快。
- 社区短文自述20张不同姿态、默认设置3000步与数小时训练，并给示范帖入口；完整caption、数据、seed和实际训练日志没取得，不能当通用人物LoRA配方或复现保证。
- 署名与许可：ai-toolkit来自Ostris，方法／设置借鉴Fizgig；本项目MIT不覆盖后端、模型及下载工具。读取状态为固定README和Civitai短文全文；没看示范作品、完整手册、训练配置、启动器或运行记录，无安装／训练。

<a id="n09"></a>

### Pixaroma Ep43：H3 Image与FIBO2分任务流程

**适用方向：工作流选型·局部编辑｜按文生图、参考组合和框选修图查教程入口。**

**设计思路：任务与提示形式匹配｜H3场景文字与FIBO结构化描述分别组织，明确保留项。**

- 原作者与原文：u/pixaromadesign，[MiniMax H3 Image and FIBO 2…Ep43](https://www.reddit.com/r/comfyui/comments/1xyogw8/minimax_h3_image_and_fibo_2_in_comfyui_14_free/)，平台日期11月17日；[Pixaroma第43期](https://workflows.pixaroma.com/ep/43/)标罗马尼亚时间11月17日18:00，约北京时间18日00:00，保留页面“Video coming soon”原显示，不据静态倒计时判断视频实际是否仍未上线。
- 教程目录：两模型各7种，文生图、提示扩写／质量模式、文字编辑、组合参考和局部框选／遮罩等。FIBO2由小助手将想法写为可查看JSON，H3用其场景扩写；不是同一工作流把所有模型文件替换即可通用。
- 阅读价值：编辑提示明确“改什么”和“保留什么”，例如人物换背景保脸／衣装／姿态，3D角色进真实环境仍保持原角色渲染，气球字换词保字形材质／位置／光线。按文字方法总结，不冒称本库看过输出对比。
- 比较条件：页面说明每模型同一场景、采用适合各自的提示格式和本集／旧集工作流，均2:3、seed1–4，视频选其中最好结果；所以是整套方案的示范比较，不是相同字面提示或随机样本成功率排名。
- 页面要求ComfyUI0.45+、Pixaroma节点1.4.250+，耗时来自4090 24GB。模型许可和免费工作流下载分别查；没有把免费附件当模型和生成用途均无许可条件。
- 读取状态：Reddit正文；课程总目录及第43期任务清单、依赖、许可说明、比较条件，文生图／编辑提示相关段。未下载1.8MB压缩包、读14套JSON、看视频／示范图或核每个模型原许可，本条是可查阅的教程导读。

<a id="n10"></a>

### MOSS中文长提示词：信息增加与字数效果分开

**适用方向：提示词组织·比较方法｜阅读嵌套长描述试验，区分信息增量和长度结论。**

**设计思路：先补关键条件｜先说明人物、场景和用光，再按需求补材质细节。**

- 原作者与原文：星辰大海Rest，[提示词到底要不要写长？我把MOSS模型从50字喂到2500字…](https://www.bilibili.com/video/BV1YisB6bEST/)，北京11月17日18:50:11，485秒。完整简介公开6场景、50/200/500/1000/1500/2500字六档、同场景同seed，短档为长档前缀，只往后补内容，36主图不挑不修。
- 作者观察：前几档人物／衣装与构图变化较大，约500字后更偏补材质／光线；像素差较后段趋小。据简介与画面，该文讨论怎样把想法写具体，不将长词串本身当美术质量保证。
- 本库整理边界：增加字数也在增加具体物件、人物外观、镜头和光线语义，所以并非隔离了“纯长度”因果。相邻像素差衡量画面变化，不能直接等同画质收益；每档的语义组织与场景有关，约500字是此组观察，不是全模型统一分界。
- token与编码范围：作者报告配套分词器32/137/319/646/959/1550 token递增，并用成图变化佐证提示不同。本库没有取得最终编码输入／上下文配置，仅靠分词计数和像素差不足以独立证明每个字都被模型利用；此处将“完整读完”保留为作者结论，本库尚未独立核最终编码。
- 其他章节另比草稿／正式／极致生成档和背影、人数、否定、手部、文字难例，属于不同对照组，不能与六档字数试验合成同一变量。截图中可见1088×1936与部分seed文字，但底模精确版本／哈希、整套工作流和完整字面配方未取得，不据MOSS标题猜Base或SFT。
- 读取状态：完整简介与分P资料；取得本分P485秒公开媒体和音轨，480短边。定距40帧及末秒共41帧OCR已读，人工看12张选定帧，另看第10／16／37帧核token、像素差和方法边界，共15帧；画面低清，未逐张原生查看36图，未核作者代码／像素差计算。平台字幕login_required，另用faster-whisper1.2.1 small／CPU INT8对约484.5秒音频生成并阅读时间轴草稿，MOSS、seed等术语有误识，关键数字／边界回原卡核。作者明确每档只跑一个seed、不保证换seed／分辨率同趋势；本库保留这一限制。ASR不冒充人工字幕或准确全文，素材与完整转录未入库。

<a id="n11"></a>

### Sena404第29期：azasuke的光泽与装饰材质

**适用方向：人物插画·画师标签｜参考本组人物与材质表现，保留动态结构局限。**

**美术风格方向：日漫厚涂·材质分层｜本组圆脸亮眼与厚重护甲并见，强光区分金属和织物。**

- 原作者与原文：Sena404（UID341674866），[anima画师串第二十九期](https://www.bilibili.com/video/BV1v5sz6YEDV/)，北京11月17日18:14:10；片内封面第39期、日期2026.11.17，投稿与内部编号分别保存，接续[第28期](../2026-11-16/README.md#n08)。
- 字面标签：`@azasuke`，2秒封面与多帧已人工核；卡片并列azasuke／Azasuke Wind，提到别名aza_wind／azasuke777、图库artist id4958。履历和图库计数未另核，不作为质量或身份额外证明。
- 作者卡片说明：写实向比例、强光泽厚涂，强调金属／皮革／织金的反光层次；称本组质感／用光较稳，但不锁脸型、长相随角色走，极端角度和大动态易崩，服饰可能偏离原设定。都是其示范评价，不当独立统计结论。
- 本库实际看图：定距9帧、末帧及2/31/35秒3定点，共13帧。可见柔收下颌、大亮眼、小鼻口与含蓄微笑的人物，也有整身厚重护甲／全遮面角色；金属亮边、铠甲分块、服装褶与织金装饰层次明确。护甲轮廓体量不等于人体肌肉比例，遮脸例不推五官；不同角色的脸型和发色不合并为统一人物设定。
- 配方缺口：简介“-”，未取每图完整正负词、底模／LoRA确切文件、seed与采样设置；不套上期配方。片头“20图实测”是作者卡片说法，本轮只看所列抽样，不称核完20张。
- 工具与水位：UID投稿接口NetworkException，经Sena404 pubdate搜索定位后，具体视频info／媒体成功；54秒480短边，主媒体地址567后仅用同一SDK响应的一个备用地址200成功；无需音轨或ASR。系列水位推进为投稿29／片内39，完整1–24期历史范围保持原记，未补称未读取的中间编号。

<a id="n12"></a>

### 近义标签打标：保留意见分歧与模型条件

**适用方向：LoRA训练·标签整理｜阅读近义动作与表情标签的处理分歧。**

- 原作者与原文：贴吧用户_00ZEXC1，[lora打标时怎么处理相同意思的标签？](https://tieba.baidu.com/p/11204532695)，stablediffusion吧，北京11月17日15:42:31，读首楼及4条可见回复。
- 问题是角色LoRA中`holding weapon, scythe`与`holding scythe`、`smile, open mouth`与`:d`是否混用，以及自动打标漏动作、堆重复词。作者没说明精确训练基座和caption设置，不能直接给跨模型统一答案。
- 社区反馈：有人建议全打／参考规范booru标签，有人认为基座能理解即可混用或用LLM清洗，也有人强调训练／使用标签对应和准确性。原帖没有对照训练或可核效果，保留分歧，不将其中一句升级为定论。
- 本库整理备注：这类标签兼有对象类别、动作及表情组合差异，文字看似近义不证明在目标编码器／训练集中等价。继续学习应回到精确模型的caption规则和真实图文对应，自动清洗也需保留所改词；本轮没有新增训练试验或代写私人配方。
- 读取状态：aiotieba4.8.2首楼及可见共5楼，未读楼中楼、图片、数据集或日志。另一[二采问题](https://tieba.baidu.com/p/11205548876)只读到问题和一句回复，未澄清两个采样分支如何加载加速LoRA，故不拼成推荐配置。

## 来源覆盖与检索记录

本轮检查从北京时间11月18日04:05开始；以下限实际页面与读取层级，不声称穷尽所有平台。

| 平台／吧名 | 实际入口／查询 | 读取范围与结果 | 限制及处理 |
|---|---|---|---|
| stable diffusion／stablediffusion吧 | aiotieba4.8.2 CREATE第1页30条 | 非置顶从18日03:03回到16日16:13，越过上次水位；读二采2楼、近义打标5楼、角色参考1楼 | 列表与正文可读。另核stable diffusion带空格入口2条，实际返回stable吧2018公告，不计为指定吧覆盖；规范吧名stablediffusion |
| comfyui吧 | 同工具CREATE第1页28条，含2置顶 | 非置顶18日03:18至12日11:45；读Z-Image作业帖2楼 | 帖子有硬件自述和鼓励回复，未取图片／配方，不从标题推画质结论；本轮无此吧新增精选，不推断全吧无更新 |
| 贴吧补搜 | 全站最新“工作流 提示词”第1页，29条 | 按实际论坛／tid／首发日期检查，指定两吧另有CREATE范围 | 跨吧和广告噪声不当本吧命中；主工具正常，未查／启用备用依赖 |
| bilibili广泛检索 | SDK17.4.2 pubdate“ComfyUI 教程”第1–5页各20条；“生图 模型”“Anima 生图”“LoRA 画风”各20条 | ComfyUI页范围17日23:42至16日17:30，越过水位；按BV去重，读MOSS长提示与设定视图完整简介，前者补媒体／OCR／ASR | 部分搜索为重复整合包广告；Anima加类别词降低歌曲同名噪声。未取得平台字幕，未自动登录、提取Cookie或重复启备用 |
| Sena404固定跟进 | UID341674866第1页实际失败；Sena404 pubdate第1页20条补查 | 搜到第29期11月17日18:14；具体BV完整简介、54秒媒体、10常规／末帧和3定点帧成功 | UID NetworkException单列，关键词补查不冒称完整投稿列表；本次真实收录推进投稿29／片内39，未伪造中间编号 |
| Reddit | r/StableDiffusion new50、r/comfyui new30；4组近期／模型交叉网页查询 | 两列表403；具体打开Pixaroma Ep43原帖正文，再沿原作者课程页读任务／比较条件 | 部分可读，不记作全平台不可用或完整新帖覆盖；其余检索摘要仅作线索，不当全文 |
| Hugging Face | text-to-image最新修改80项、image-to-image30项 | 读Gleam、HomeIMG、GlyphAnchor、H3ControlNet、Turing及Realem卡片；Gleam两原JPEG实际看图 | 大量学生作业／量化镜像与旧更新不自动算新后训练。Realem仅trigger与极短模板，未补造训练方式；无权重下载 |
| GitHub | comfyui workflow pushed≥17日25项、comfyui prompt created≥16日15项 | 读LD Writer、Pose、GlyphAnchor、H3 Portable、FP16节点README及对应元数据／revision | Sequential_prompt_Builder有仓库／提交但README404，只记缺口，不循环猜文件。未安装、启动服务或执行项目测试 |
| Civitai社区／论坛 | 最新文章30项、Newest模型40项、Workflows15项 | 读设计系列预告、角色设计讨论、Fibo2经验、H3训练分享全文；读LD Writer v1.1.3资源说明及版本元数据 | n06、n08追原项目；未看图库作品／评论及完整工作流JSON。预告不当已发布完整教程；作者评测数字未自行核验 |
| ComfyUI论坛／其他 | forum.comfy.org/latest.json约30主题；note.com ComfyUI最新15搜索；Pixaroma课程与EP43页面 | 论坛列表可读，有新Mac FFmpeg求助；note搜索403；Pixaroma任务／条件与相关提示段可读 | 新论坛帖正文未打开，不声称已查明问题；其他论坛仅限实际入口。未重复报道旧论坛下线公告 |

## 后续关注与更正

- [Sena404系列](../2026-11-09/notes/Sena404画师串与相关分享.md)本次补第29期，保留第1–24期历史及25–28期已读范围。长提示视频中500字、token／像素差等结论保留作者试验条件，不升级为所有MOSS版本规则。
- [CherryBoyHunter设计风格系列预告](https://civitai.com/articles/38939)（北京11月17日05:00）计划分享包豪斯、波普、拼贴、水彩等背景和模型实践；本轮已读预告，尚非这些专题的完整教程，后续有正文再按实际方法收录。[角色为何令人印象深刻](https://civitai.com/articles/39044)主要是作者交流题，未强作具体画风配方。
- [MOSS角色设定视图](https://www.bilibili.com/video/BV1mMs66xEzK/)（余小文AIGC，17日23:42、61秒）本次仅读完整简介；有网盘入口但没有取得公开配置／媒体，不与已读角色参考方法混成同一配方。
- GlyphAnchor的InfoTextBench仍待公开；H3 ControlNet迁移文档前后解释已有修正，应读完整后续段；Pose原图库未随包开放再分发，阅读工具说明不构成素材授权。
- 本轮保留受限入口与未读取部分；没有追加生图、训练或迁移实验计划。公开音视频、截图、完整OCR／ASR、原始响应与缓存均在仓库外，提交仅为摘要和来源入口。
