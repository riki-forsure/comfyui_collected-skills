# 2026-11-20 每日社区发现

本页是对社区作者公开成果的中文概述与导读，感谢模型、工具、教程及原画作者的投入。条目保留作者、原文、真实日期与读取范围，欢迎回原帖阅读完整说明、示范和后续更新，支持原作者。署名／链接不等于转载授权，第三方成果不作为本库原创。

- 北京日期与实际检索时间：2026-11-20，03:56起读取仓库最新规范，03:57起逐平台检查；本页记录归档前实际完成的阅读。
- 检索类型：无具体差距要求的每日广泛发现；没有另设主动搜索专题。
- 执行状态：精选11项主题，包含后训练／合并／解码研究、工作流、提示工具、画师标签与社区实践；部分平台入口或附件受限。
- 时间窗：接续[11月19日](../2026-11-19/README.md)约04:01起的成功读取水位，优先新增和实质变化；近期首次补录保留原始时间，不把修改日期、合并或量化称作新训练。
- 标注归属：适用方向、美术风格／设计思路为本库整理；作者说明、社区反馈、实际看图与运行验证分开。来源／配方未知的地方保持未知。
- 执行边界：仅研究与汇总，复用现有SDK、FFmpeg、OCR和缓存；未安装节点、下载生图权重、启动训练／生图／自动实验、增加服务或派发子代理。归档不等于收益验证。

## 今日值得阅读

- **后训练与模型路线**：[MOSS SFT四步蒸馏](https://huggingface.co/lvladikov/MOSS-SFT-Distill-4step-LoRA)公开专用噪声序列和加载条件；[Seedreamstyle H3 6K](https://huggingface.co/Nebsh/Seedreamstyle-H3-6K)给续训与场景对照；Anima turbo合并和Pixel Decoder需分清职责与版本。
- **修复与提示组织**：[MOSS LLLite](https://github.com/X-absurd/ComfyUI-MOSS-LLLite)区分细节控制和可选色彩反馈，另有皮肤质感、像素素材、多画幅与可保存的词库组合方法。
- **社区经验**：[Sena404第30期](https://www.bilibili.com/video/BV1DSsh6iEJv/)已核`@ebifurya`及片内40；[贴吧LoRA文字分工](https://tieba.baidu.com/p/11209654586)保留不同意见，按设计方法导读。

## 分享速查

| 类别 | 分享／资源与版本 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点／可学习经验 | 读取状态 |
|---|---|---|---|---|---|---|
| SFT蒸馏LoRA | [MOSS SFT四步蒸馏：模型文件与噪声序列一起核对](#n01) | 采样加速·模型选型｜查阅SFT专用四步LoRA及其噪声序列和精度条件。 | 设计思路：细节与色调分评｜兼顾纹理、用光和文字，不把高频纹理指标当整体质量。 | lvladikov／Reddit TimeTruth2490；OpenMOSS及相关作者；[固定模型卡](https://huggingface.co/lvladikov/MOSS-SFT-Distill-4step-LoRA/blob/2ec5241400bfedfc2441b35793bc0da1689ebba6/README.md) · [作者发布帖](https://www.reddit.com/r/StableDiffusion/comments/1y06n27/mossimage_sft_new_4step_distillation_lora_using/) | chk00015000；ComfyUI专用alpha与ManualSigmas分开记录 | 模型卡全文、基础JSON关键节点、1张对照；未运行 |
| Anima合并与解码研究 | [Anima turbo v4与Pixel Decoder：加速、画风和解码分开](#n02) | Anima选型·解码研究｜区分合并画风、四步采样与专用像素解码头。 | 设计思路：分清画风与解码职责｜画师组合改变画法，解码替换需另看纹理保留。 | sorryhyun；CircleStone、NVIDIA与相关研究作者；[turbo固定卡](https://huggingface.co/sorryhyun/anima-turbo-4step/blob/67a5ce82b01cd84a3913d3e6b6ded6c62e4c61a3/README.md) · [Pixel Decoder固定卡](https://huggingface.co/sorryhyun/anima-pixel-decoder/blob/ed9da688cfe1ed06c87c02b0154ced1e04879df9/README.md) | v4明确无新训练；当前解码头与旧头测速不可混用 | 两模型卡全文、版本文件列表；未看样图或运行 |
| 摄影风格后训练 | [Seedreamstyle H3 6K：摄影用光与人物场景续训](#n03) | 摄影人物·风格LoRA｜参考H3人物场景的用光、颗粒与双人叙事组织。 | 美术风格方向：电影摄影·冷暖实景光｜本例年长双人自然褶皱，冷雨窗光与暖灯形成层次。 | Nebsh／nebsh；StefTranquillin、GrootDEX及MiniMax作者；[固定模型卡](https://huggingface.co/Nebsh/Seedreamstyle-H3-6K/blob/5e1b48cd929da47a98e7a9ea426f20340ef92a0a/README.md) · [Civitai v2.0／3480133](https://civitai.com/models/3058591?modelVersionId=3480133) | 6K是累计6000训练步；不是6K分辨率或Seedream原模型 | 模型卡全文、场景15配置、1张四栏对照；未复跑 |
| 皮肤质感LoRA | [Real Skin MOSS v1.0：皮肤细节与人物变化分别观察](#n04) | 摄影人物·皮肤质感｜查阅MOSS SFT皮肤LoRA的景别、用光和版本条件。 | 美术风格方向：手机纪实·自然皮肤｜本组可见雀斑与泛红，窗光和日光保留不均匀肤色。 | SeedraAI／SEEDRAAI；MOSS基座与相关作者；[原作者固定卡](https://huggingface.co/SEEDRAAI/MOSS-Image-LoRA-RealSkin/blob/2407f95d4adb1323ae9a5d0f412e67057d57c7d1/README.md) · [Civitai原资源](https://civitai.com/models/3058565) | 仅SFT；看图同时记录姿态、取景与身份保留边界 | 原卡全文、2张对照；镜像合并，未复跑 |
| 细节修复控制与补偿 | [MOSS Tile V1与Color Guide：结构、纹理和颜色分层](#n05) | 图像修复·细节精修｜了解SFT专用Tile控制和可选颜色反馈的不同职责。 | 设计思路：先保结构·另管色偏｜细节生成与色彩补偿分开，局部纹理和对比度一起看。 | Xabsurd／X-absurd；ComfyUI、MOSS与Anima LLLite作者；[固定模型卡](https://huggingface.co/Xabsurd/MOSS-Image-Tile-Control/blob/4e7ae6883f36997bf68adf5849a66793236cb5b2/README.md) · [固定节点README](https://github.com/X-absurd/ComfyUI-MOSS-LLLite/blob/d22c920520d15c0799764d17946ca4a84eda068b/README.md) | V1、beta2／3不互换；颜色节点不是新权重 | HF与节点README全文；未看示范或审源码 |
| 原生像素小模型 | [LiliPixel V1：不同尺寸的透明与不透明素材](#n06) | 像素素材·提示组织｜按16／32／64像素分辨率选择透明精灵或小场景。 | 美术风格方向：原生像素画·块面塑形｜横幅示例含透明图标与不透明场景，明暗以像素色块组织。 | Pinkstack；MongoDB及Angais、azyg0s、Chan-Y等数据作者；[固定模型卡](https://huggingface.co/Pinkstack/LiliPixel-V1-190M/blob/0bf3ae78045543488067c3be06bcf9ca07244ab8/README.md) | 从头训练DiT；64像素模式不作透明素材保证 | 模型卡全文、横幅样例；未运行或查数据原卡 |
| 提示词组合节点 | [Smart Wildcards：手选优先、自动候选按种子组合](#n07) | 提示词组织·批量变化｜将服装、光线等词库按选择和顺序组合为提示。 | 设计思路：锁定片段·变化其余｜手选词优先，未锁定文件才参与有种子的随机组合。 | DropzoneNinja；ComfyUI社区作者；[固定README](https://github.com/DropzoneNinja/comfyui-smart-wildcards/blob/0a56624ca680c36e2dffce38ab38f9ec5e15b0ee/README.md) | 固定服务端词库路径；工作流状态不包含全部词库内容 | README全文；未读源码／操作界面 |
| 画幅批量节点 | [Dynamic Ratio Latent：提示中的画幅标签与内容分离](#n08) | 批量构图·画幅组织｜用一组比例生成多个画幅，并剥离非画面指令。 | 设计思路：画幅与内容分开｜比例标签控制尺寸，清理后的文字再进入条件编码。 | vcrparts；ComfyUI社区作者；[固定README](https://github.com/vcrparts/ComfyUI-DynamicRatioLatent/blob/a9a11119a2e93a5095d5a39d5eac4091167bac85/README.md) | 按像素面积计算多比例；seed输入只参与命名前缀 | README全文；未核源码／不同家族latent |
| Krea2工作流更新 | [areyouokay Krea2 v1.1：可选精修模块与新放大分支](#n09) | 工作流选型·局部精修｜按任务选择二采、面部修复、去物与后处理模块。 | 设计思路：分阶段精修｜起图、放大、脸部与后处理分块，按需要启用。 | areyouokay；SesquiLSR、RES4LYF、Impact等节点作者；[v1.1／3480006](https://civitai.com/models/3050466?modelVersionId=3480006) | v1.1将Ultimate SD Upscale换为SesquiLSR；作者个人取舍 | 资源全文、版本和依赖元数据；JSON附件401 |
| Sena404增量 | [Sena404第30期：ebifurya的圆润造型与光泽](#n10) | 人物插画·画师标签｜参考圆润造型、表情与光泽，并留意动作条件。 | 美术风格方向：圆润日漫·亮面厚涂｜本组大眼短圆脸、小鼻口，丰润体量与渐层高光鲜明。 | Sena404；ebifurya／えびふりゃ・豆乳軒及原画师；[原视频BV1DSsh6iEJv](https://www.bilibili.com/video/BV1DSsh6iEJv/) | 投稿30／片内40；@ebifurya已核，不套用邻期配置 | 完整简介、54秒媒体、13帧观察与OCR；未取逐图配方 |
| 贴吧风格组合讨论 | [画风LoRA与文字：线稿、上色和触发词的分工](#n11) | 画风组合·提示组织｜阅读LoRA已加载时文字还能承担哪些画法职责。 | 设计思路：画法拆分·组合表达｜把触发词、线稿、立体程度和上色方向分别理解。 | ll337；Arclite、Pixelllip及参与讨论吧友；[原讨论11209654586](https://tieba.baidu.com/p/11209654586) | 保留“只写触发词”和“继续用文字组合”两种意见 | 首楼及3条可见回复；无图／精确版本／对照 |

## 当日分享

<a id="n01"></a>

### MOSS SFT四步蒸馏：模型文件与噪声序列一起核对

**适用方向：采样加速·模型选型｜查阅SFT专用四步LoRA及其噪声序列和精度条件。**

**设计思路：细节与色调分评｜兼顾纹理、用光和文字，不把高频纹理指标当整体质量。**

- 原作者与原文：lvladikov；Reddit u/TimeTruth2490发布帖，搜索索引标11月19日，原页只显示相对时间，未独立核精确发布时间。HF仓北京11月19日16:45建仓、18:05更新；固定revision `2ec5241400bfedfc2441b35793bc0da1689ebba6`。卡片明确当前chk00015000产于11月19日，数字是15000训练样本，不直接改写成15000次优化器更新。
- 作者分享：在MOSS Image SFT上做eDMD＋LADD分布匹配蒸馏，用教师图与真实照片裁片辅助，rank64、252模块，四步CFG1；同一基座的Base权重不在已训练范围。作者给多尺寸、布局和编辑工作流，但编辑还需另外的Edit LoRA。
- 两文件身份：plain与`_comfyui`是同一适配器的两种加载版本，卡片说down/up张量相同，ComfyUI版本alpha加入实测1.18补偿（64→75.5）。plain用于作者的精确旁路加载，ComfyUI标准加载器用`moss_sft_4step_rank_64_lora_comfyui.safetensors`强度1.0；不是两个独立训练模型。本库未下载张量核实补偿实验。
- 关键配置：Euler、ManualSigmas `1.0, 0.91, 0.717, 0.024, 0.0`、BasicGuider／CFG1。作者明确不能用四步simple替换其训练噪声点；该路径不使用负向或SLG。ComfyUI补偿因子针对`moss_image_sft_bf16`，INT8版本未测，不把可加载当等价。
- 已读取固定revision的基础local JSON：核到bf16 SFT、上述LoRA强度1、Qwen3.5-9B w4a8编码器、Flux2小VAE、Euler与ManualSigmas控件；其默认2848×1600高于训练最大1824×1024／1024×1824，卡片例图另用BF16文本编码器。读控件不等于已运行并捕获最终扩写文本；其他7套JSON未读。
- 作者的22图任务计费GPU时间约14倍差、15组文字题14组全对、纹理指标1.22倍等，均来自其Cloud设置与小样本；纹理量不等于综合美学质量，单一硬件／任务耗时不作普遍性能承诺。
- 本库实际看图：[portrait_compare三栏](https://huggingface.co/lvladikov/MOSS-SFT-Distill-4step-LoRA/blob/2ec5241400bfedfc2441b35793bc0da1689ebba6/assets/portrait_compare.jpg)中右栏保有明显雀斑、发丝与侧窗光，中栏皮肤较平滑；三栏五官、取景仍有差异。仅看这一张缩放显示的对照，不声称核完279图或37提示，不把“同prompt／noise”当结果完全同构。Realism Enhancer是另一个作者的可选LoRA，原卡说所有统计／示范未使用它。
- 读取状态：Reddit正文、HF主卡全文、基础JSON关键节点及一张对照；Detailed Model Card、训练日志、其他配方和原生局部未读。模型卡声明Apache-2.0及非官方社区产品，其他编辑／PiD资源各自另有条件。未安装／下载权重／复跑。

<a id="n02"></a>

### Anima turbo v4与Pixel Decoder：加速、画风和解码分开

**适用方向：Anima选型·解码研究｜区分合并画风、四步采样与专用像素解码头。**

**设计思路：分清画风与解码职责｜画师组合改变画法，解码替换需另看纹理保留。**

- 原作者与原文：sorryhyun，两份HF模型卡首次收录。turbo仓6月建立，当前revision `67a5ce82b01cd84a3913d3e6b6ded6c62e4c61a3`于北京11月19日20:11更新；Pixel Decoder仓19日16:04建立、22:37更新，revision `ed9da688cfe1ed06c87c02b0154ced1e04879df9`。保留仓库／修改时间，不称两者都当天新训练。
- turbo区别：v3是作者所述1万步／单5070Ti约30小时的训练产物；v4将Anima上的画师LoRA组合与v3 turbo拼为一个rank256＋64的LoRA，没有进一步训练。卡片要求v4在原Anima底座强度1.0、CFG1、4步、shift3；其他强度不等于画风组合平滑插值。v3列er_sde，不擅自移植成v4已验证采样器。
- Pixel Decoder是约2500万参数的专用像素解码头，读取Anima最后一步DiT特征，直接输出RGB，代替VAE解码；不是另一个底模，也不是通用VAE文件。Base说明限定28-block anima-base-v1.0、Euler／shift3、20–50步／CFG4；turbo训练点指`anima_turbo_4step_v4_longer.safetensors`，不能只因名含v4就换成任意文件。
- 版本条件：当前头`anima_pixel_head.safetensors`与`old/`旧头分开。卡片明确测速、样图和held-out读数来自旧头，不能把旧头ComfyUI约1.13→1.00秒直接写为当前头性能；作者自己的推理器含VAE搬运，耗时口径也与驻留ComfyUI不同。
- 取舍：作者记录网点／密排线条会被平滑、纹理区偏暗、小字与速度线变软；这关系到漫画修复与单纯看总图的差别。×2 preview也是单独测试文件，不称成熟通用放大器。
- 读取状态：两主卡全文、API版本与文件列表；未看样图、读节点源码或论文全文，未核权重哈希／兼容／运行。许可证主卡明确CircleStone非商业权重条件并回链NVIDIA上游，turbo卡还更正了此前Apache声明；以原条款为准，不因旧标签继续当Apache资源。

<a id="n03"></a>

### Seedreamstyle H3 6K：摄影用光与人物场景续训

**适用方向：摄影人物·风格LoRA｜参考H3人物场景的用光、颗粒与双人叙事组织。**

**美术风格方向：电影摄影·冷暖实景光｜本例年长双人自然褶皱，冷雨窗光与暖灯形成层次。**

- 原作者与原文：Nebsh／Civitai nebsh，[Seedreamstyle — MiniMax H3 Image LoRA · 6K](https://huggingface.co/Nebsh/Seedreamstyle-H3-6K/blob/5e1b48cd929da47a98e7a9ea426f20340ef92a0a/README.md)。HF仓北京11月20日02:53创建、03:47更新；Civitai v2.0／3480133于03:24发布。本次首次收录，HF revision `5e1b48cd929da47a98e7a9ea426f20340ef92a0a`。
- 作者训练：最初43图2000步，扩为1134图／caption后续训至累计6000步，rank／alpha16／16、约1MP分桶。6K与2K在这里是训练步数；不是图像长边，也不说明取得或开放了Seedream5.5权重。作者说明这是独立H3适配器，并感谢社区赠图者。
- 使用示范：H3 Image pruned INT8 ConvRot，trigger `seedreamstyle.`首句、Model Only强度1.0、LCM、6步、CFG1、simple；KJ MiniMaxH3PromptWeight用text with empty image、0–25%。卡片建议6K，根目录6K与checkpoints/6000文件据作者为同一权重，不需双份下载；本库仅看manifest，没有下载核整文件SHA256。
- 对照边界：20场景目录提供每场提示和设置，H3用8448×4736约40MP，Seedream参考为2736×1536；同数字seed跨模型不等于相同噪声／构图。这是整体方案示范，不是等分辨率的细节基准。
- 本库实际看[场景15四栏](https://huggingface.co/Nebsh/Seedreamstyle-H3-6K/blob/5e1b48cd929da47a98e7a9ea426f20340ef92a0a/examples/15_Orage_Sous_La_Veranda/comparison.jpg)：年长双人坐谈，脸手褶皱、自然体量、相互视线，灰绿雨景和暖灯并用。画面中的6K栏明确标closed windows；对应settings.json确实额外增加所有窗门关闭的提示，故这栏不能当完全相同字面条件的单变量比较。
- 读取状态：HF主卡全文、Civitai描述与版本、场景15完整设置及训练文件manifest；只看这一组缩放四栏，未逐场观察20组、核其他改词重跑或读原生PNG。其余人物风格不由这一例推广。模型许可随MiniMax H3 Image Community License及上游条款；未下载权重／生图。

<a id="n04"></a>

### Real Skin MOSS v1.0：皮肤细节与人物变化分别观察

**适用方向：摄影人物·皮肤质感｜查阅MOSS SFT皮肤LoRA的景别、用光和版本条件。**

**美术风格方向：手机纪实·自然皮肤｜本组可见雀斑与泛红，窗光和日光保留不均匀肤色。**

- 原作者与原文：SeedraAI，[Real Skin](https://huggingface.co/SEEDRAAI/MOSS-Image-LoRA-RealSkin/blob/2407f95d4adb1323ae9a5d0f412e67057d57c7d1/README.md)，HF原仓北京11月20日02:32创建、02:33更新，revision `2407f95d4adb1323ae9a5d0f412e67057d57c7d1`。经cfgscale同名镜像发现，回到卡片署名的SEEDRAAI，合并为一条；不是两个独立模型。
- 作者目标：用100张未修饰皮肤照片训练雀斑、毛孔、色差、小泛红，减轻磨皮感。v1.0是4000步过程中选出的3000步权重；作者说4000步开始改变脸，所以版本数字与最后训练步不可混写。
- 作者推荐：MOSS Image SFT，文件`seedra_skin_moss.safetensors`，Model Only加载；trigger `r3alsk1n`，权重1.0，较轻效果0.7–0.8；1024×1536、35步、CFG3、euler／sgm_uniform。作者称Base上会变软褪色，暗景作用较弱，并提醒motion blur与皮肤细节目标冲突。
- 本库实际看[窗边对照](https://huggingface.co/SEEDRAAI/MOSS-Image-LoRA-RealSkin/blob/2407f95d4adb1323ae9a5d0f412e67057d57c7d1/images/00_before_after.jpg)和[街头对照](https://huggingface.co/SEEDRAAI/MOSS-Image-LoRA-RealSkin/blob/2407f95d4adb1323ae9a5d0f412e67057d57c7d1/images/01_before_after.jpg)：窗边右图面部／肩臂有可见雀斑泛红；两组还改变了头向、手势、发型或取景。街头有墨镜遮眼，不能据此比较眼部一致性。因而作者“不改变脸”的定位不当本库已核身份保证。
- 风格归纳范围是两张对照中的手机随拍质感、自然体量与用光，不推出所有年龄／体型的稳定画法。卡片声明同prompt／seed，但不能据此认定除皮肤外所有语义像素都保持。
- 读取状态：原作者模型卡全文、镜像卡、版本文件列表及两张原对照，未读训练照片／日志、样图完整元数据或运行。卡片标Apache-2.0且提醒跟随基座许可；外链会员平台与公开权重说明分别看，不把服务推广当已验证收益。

<a id="n05"></a>

### MOSS Tile V1与Color Guide：结构、纹理和颜色分层

**适用方向：图像修复·细节精修｜了解SFT专用Tile控制和可选颜色反馈的不同职责。**

**设计思路：先保结构·另管色偏｜细节生成与色彩补偿分开，局部纹理和对比度一起看。**

- 原作者与原文：Xabsurd／X-absurd，模型仓北京11月12日13:25建、19日23:17更新；模型revision `4e7ae6883f36997bf68adf5849a66793236cb5b2`。节点commit `d22c920520d15c0799764d17946ca4a84eda068b`于19日23:16提交。作为近期首次补录与颜色补偿更新收录，不称所有权重当天重训。
- 作者分路：V1是SFT上的LLLite Tile适配器，用RGB参照与attention输入补丁，推荐细节重绘；beta2是Base上的concat LoRA、偏保守保留；beta3是SFT residual适配器、作者称更快但易抹高频。数值强度相同不代表控制量相同，也不换加载节点硬套权重。
- V1原示范公开SFT INT8 ConvRot、Qwen3.5-9B BF16、Flux2 VAE和另一个Coffmeteor加速LoRA，15步、CFG5、Euler／SGM uniform、shift3等。这是历史V1示范设置，不把它与本日n01四步蒸馏组合成一套作者配方。
- 新颜色方法：v0.1.3+的Apply MOSS Color Guide用同一Flux2 VAE解码色彩反馈修正最终latent，接在Apply MOSS-LLLite后、sampler前。作者起点strength1、iterations2、grid8，独立于LLLite强度；默认strength0。两轮额外9次完整VAE decode＋6次小校准encode，有额外耗时及亮度／对比度变化。
- 与Reference Anchor分开：后者约束采样低频latent，会抑制生成细节，不推荐用于细节增强；作者建议颜色Guide开时关Anchor，普通VAE Decode用同一VAE。tiled解码与tiled采样还各有颜色／参照范围条件，不能只因名称含Tile就等同分块执行。
- 边界：现有V1权重不需重下，颜色补偿不是重新训练或精确RGB保证；旧例图早于该可选节点，不能当新Guide的效果图。图像修复可创造合理细节，不能声称恢复原始事实；MOSS Edit参考图／cached KV路径尚不支持，Anima LLLite权重也不互换。
- 读取状态：两份固定主卡／README全文，未读Research Report、源码、示范JSON或图像，以上视觉收益为作者说法。代码GPL-3.0与权重条款分别看，未安装节点／下载模型／运行。

<a id="n06"></a>

### LiliPixel V1：不同尺寸的透明与不透明素材

**适用方向：像素素材·提示组织｜按16／32／64像素分辨率选择透明精灵或小场景。**

**美术风格方向：原生像素画·块面塑形｜横幅示例含透明图标与不透明场景，明暗以像素色块组织。**

- 原作者与原文：Pinkstack，HF仓北京11月20日00:48建立、03:40更新，revision `0bf3ae78045543488067c3be06bcf9ca07244ab8`，首次收录。
- 作者路线：约1.91亿可训练参数、从头训练的单流DiT／rectified flow，冻结voyage-4-nano文本编码器另约3.46亿参数，不含在权重里，首次使用另取。不是昨日nomeda-lab的自回归小模型，也不是大扩散模型上只加像素风LoRA。
- 输入与输出：16／32像素训练有透明通道，提示末尾用`, transparent background`；64像素场景没有透明训练数据，作者前段与末段措辞有“unless prompted otherwise”等不一致，但实际限制明确不应用64模式求透明。64模式可前置realistic photo切向写实小图，并不保证所有输出维持离散像素美术。
- 提示条件：最多96 text tokens，超出截断，简单描述更合适；默认Euler、CFG3、30步，64模式建议50步。小尺寸复杂多主体、长字与小众对象受限，作者建议多seed挑选；这只是使用方法，不当本库成功率或近乎瞬时速度保证。
- 本库实际看原卡横幅：右侧杯糕、动物、方向箭头等以明显像素块组织轮廓，左侧有风景与近似写实小图；横幅是拼排预览，没有逐项原分辨率对照，不判断透明alpha正确性。
- 训练说明为132000步、单4080约126 GPU小时与多来源数据。卡标OpenMDW1.1，数据集有各自MIT／CC BY／CC0等条件；代码自定义pipeline与编码器下载也不是一个普通ComfyUI节点直接替换。本轮仅阅读，未运行remote code、下载编码器或权重。
- 读取状态：模型卡全文、文件元数据及横幅；未读全部数据卡、源码或原生精灵样本。与[11月19日像素小模型](../2026-11-19/README.md#n04)作为不同路线并列，不将相近数据来源视为同模型。

<a id="n07"></a>

### Smart Wildcards：手选优先、自动候选按种子组合

**适用方向：提示词组织·批量变化｜将服装、光线等词库按选择和顺序组合为提示。**

**设计思路：锁定片段·变化其余｜手选词优先，未锁定文件才参与有种子的随机组合。**

- 原作者与原文：DropzoneNinja，GitHub comfyui-smart-wildcards，北京11月19日07:47建仓，commit `0a56624ca680c36e2dffce38ab38f9ec5e15b0ee`于13:37提交。首次收录。
- 作者方法：表格里启用词库文件、选择固定一行或Automatic，并按目录内顺序拼提示。手选项始终优先，Automatic在Random关时取首项、开时按seed／路径／文件内容随机。目录顺序仍按字母排序，不是任意全局排序。
- 保存与迁移：工作流存启用、选择、排序和折叠状态；固定条目以字面文本保存而非行号。换服务器时真实词库仍取该服务器文件，旧选择不存在会回Automatic并提示，新增文件默认禁用、缺失文件保留设置。相同seed需要相同文件内容等条件，不把JSON保存当已封装词库。
- 条件：固定根路径`/basedir/wildcards`不可配置，需现有服务端目录可读写；Windows／容器路径不能当已自动适配。作者明确未完成真实浏览器拖拽／点击测试，Docker bind mount也未独立实测，并称尚未选择仓库许可。
- 读取状态：固定README全文，未审实现、PROJECT／TASKS或运行界面；只做导读，不复制代码、词库或部署服务，不将文档确定性声明当已捕获最终编码文本。

<a id="n08"></a>

### Dynamic Ratio Latent：提示中的画幅标签与内容分离

**适用方向：批量构图·画幅组织｜用一组比例生成多个画幅，并剥离非画面指令。**

**设计思路：画幅与内容分开｜比例标签控制尺寸，清理后的文字再进入条件编码。**

- 原作者与原文：vcrparts，北京11月19日09:26建仓，commit `a9a11119a2e93a5095d5a39d5eac4091167bac85`于09:34提交，首次收录。
- 作者方法：从提示解析`<ratio: 16:9, 4:5, 1:1>`等比例标签，移除后输出cleaned_prompt；按目标像素面积推宽高，再取指定倍数。比例换了并非同一1024长边，rounding后面积也仅接近目标。
- 节点将empty latents和文件名前缀输出成列表，让下游采样／解码／保存按比例循环；建议放在动态提示和LoRA标签处理之后，避免按比例重复上游加载。作为多画幅组织方法，不把其输出视作画面主体位置控制。
- 重要seed边界：可选seed字段只给文件名加标记；要同seed采样还须将同一seed另接KSampler，不是填入该节点就设置了采样seed。相同seed跨尺寸也不等于相同构图。
- 家族条件：文档列4通道SDXL／IL／SD1.5与16通道Flux／Krea／SD3两组选项，未证明所有新家族latent格式可由通道数独立决定，不外推到MOSS或任意Anima工作流。取整倍数也需具体VAE／模型约束。
- 读取状态：固定README全文；未审源码、JSON或实际多比例输出，没有部署／运行。此条仅总结比例／内容解耦和列表组织方法，不以加载成功或图像收益作结论。

<a id="n09"></a>

### areyouokay Krea2 v1.1：可选精修模块与新放大分支

**适用方向：工作流选型·局部精修｜按任务选择二采、面部修复、去物与后处理模块。**

**设计思路：分阶段精修｜起图、放大、脸部与后处理分块，按需要启用。**

- 原作者与原文：areyouokay，[Krea2_turbo workflow](https://civitai.com/models/3050466?modelVersionId=3480006)。v1.0于北京11月14日05:22发布；v1.1／3480006于20日01:41发布，首次收录并分版本记录，API列表旧v1.0在前不等于它仍是最新。
- 作者变化：把可选Ultimate SD Upscale换成SesquiLSR，原作者仅说自己更喜欢结果，没有给标准化优劣结论。原描述包括两段生成、放大续采、Face Detailer独立提示、LaMa蒙版去物、色彩／锐度／颗粒后期和Civitai元数据保存。
- 任务分工：需要较细脸部时开Face Detailer，需要去物时用LaMa，按需求选择处理模块，不以模块数量证明质量。作者称可删掉可选块，但CORE ROUTING和标准Save Image保留；这是其文档路由约定，本库未核删除后的有效接线。
- 依赖：rgthree、RES4LYF、Image Saver、SesquiLSR、Impact Pack／Subpack、Inpaint Nodes、CRT-Nodes、Krea2 Enhancer等，具体作用和版本需回原资源。作者以RTX5070 12GB／32GB RAM使用，不写成任意12GB设备保证。
- 读取状态：资源描述全文、v1.0／v1.1名称时间及约147KiB JSON附件元数据；实际附件请求401，未取得文件，因此不能列出同图完整参数、seed、有效分支和兼容结论。没有改签名、反复请求或用别人的工作流冒充。作者声明这是个人日用分享，本库保留其用途及原文入口。

<a id="n10"></a>

### Sena404第30期：ebifurya的圆润造型与光泽

**适用方向：人物插画·画师标签｜参考圆润造型、表情与光泽，并留意动作条件。**

**美术风格方向：圆润日漫·亮面厚涂｜本组大眼短圆脸、小鼻口，丰润体量与渐层高光鲜明。**

- 原作者与原文：Sena404（UID341674866），[anima画师串第三十期](https://www.bilibili.com/video/BV1DSsh6iEJv/)，北京11月19日18:27:06发布。封面内部第40期、2026.11.19，投稿编号与片内编号分别保存；接续[第29期](../2026-11-18/README.md#n11)。
- 字面标签：`@ebifurya`，已看2秒封面及多帧原卡核对；封面并列ebifurya／えびふりゃ・豆乳軒。OCR对别名拼写不稳，未把误识作为可用标签；图库数量和账号资料未独立核查，不作为质量证据。
- 作者卡片评价：圆润厚涂、皮肤高光强，大眼圆脸，脸型体量会一起偏向该画法；本组画风迁移较稳，与上一组不锁长相不同。卡片还偏向五官和静态手势，提到模型固有角色／服饰倾向。本库将这些作为其本组观察，不当所有角色成功率。
- 本库实际看图：9张定距帧＋末秒，再补2／31／35秒，共13帧。可见较短圆脸、大亮眼、简化小鼻口、明显脸颊泛红；含蓄侧视与张口微笑／指向镜头等不同表情并见。多数示范上半身轮廓有丰润体量与收腰，衣料和皮肤用平滑渐层与高光塑形；未据半身图推全身头身比。不同角色发色／服饰和单次表情不归成画风固定设定。
- 配方缺口：完整简介为“-”，未取得逐图正负词、精确底模／LoRA文件、seed及采样参数。片头“20图实测”是作者卡片说法，当前视频呈10页轮播且本轮抽读，不称核完20张原生图，也不继承29期或更早期参数。
- 工具范围：UID投稿页1成功，返回总数87、最新第30期；54秒480短边视频主地址567后，仅同一SDK响应一个备用200取得。无讲解深读需要，未下音轨／跑ASR；未读评论。系列水位推进投稿30／片内40，历史1–24与25–29范围保留。

<a id="n11"></a>

### 画风LoRA与文字：线稿、上色和触发词的分工

**适用方向：画风组合·提示组织｜阅读LoRA已加载时文字还能承担哪些画法职责。**

**设计思路：画法拆分·组合表达｜把触发词、线稿、立体程度和上色方向分别理解。**

- 原作者与原文：ll337，stablediffusion吧，[加了画风lora情况下](https://tieba.baidu.com/p/11209654586)，北京11月19日10:09:17发布，读首楼及3条可见回复。
- 原问题：已加载画风LoRA时，提示里还有没有必要写画风。Arclite认为写触发词即可；Pixelllip提出可让LoRA承担线稿，再由文字补二次元／立体程度与不同上色方向。保留分歧，不改写成必须加词或必须不加词的规则。
- 本库方法概述：这条讨论的价值在于把画法当作可分工的信息，而不是所有风格都只有一个名字。具体触发词与权重仍要按原模型作者说明；本帖没有给精确家族、LoRA版本、正负词或同图对照，不证明几种文字维度能互不干扰地独立控制。
- 不涉及某一种固定画风的总结，使用“设计思路”标注；未看图，不附五官、体型等无关待确认项。另一Anima姿态求助只提供一条文字建议，也未升级为通用姿态配方。
- 读取状态：aiotieba4.8.2共4条可见楼层，未读楼中楼／图片或实际成图。没有建立本地实验任务，读者可由原帖继续查反馈。

## 来源覆盖与检索记录

主要入口检查从北京时间11月20日03:57开始。实际范围如下，不以搜索成功或接口成功代替原文阅读，也不声称穷尽所有社区。

| 平台／吧名 | 实际入口／查询 | 读取范围和结果 | 限制与处理 |
|---|---|---|---|
| stablediffusion吧 | aiotieba4.8.2 CREATE页1／30；全站最新“工作流 提示词”页1／26 | 排除置顶后最新20日00:48，普通帖向前至17日19:13，跨昨日水位；深读LoRA文字讨论4条、Anima姿态讨论2条 | 未读楼中楼／图。姿态建议缺精确资源和对照，不当通用解法；无需要启用备用工具 |
| stable diffusion名称核对 | 同工具带空格名称页1／2 | 实际仍是stable吧2018公告，不是指定SD教程吧 | 不称已证实别名重定向；有效覆盖用stablediffusion吧，两个实际吧名分记 |
| comfyui吧 | CREATE页1／29 | 置顶另记，最新普通帖20日01:01，向前至13日23:51；读MMH3 Image采样组合帖11209337243共2楼 | 核心为图片颜色表格，文字没给完整组合、原制作者不明；本轮未读图片，不将“绿色最优”转成参数推荐，保留原帖线索 |
| bilibili广泛发现 | SDK17.4.2 pubdate：ComfyUI教程页1–4各20；生图模型、Anima生图、LoRA画风各页1／20 | ComfyUI页4范围18日21:12–19日11:24，已跨过昨日04:01起的水位；其他页分别18日12:57–19日23:57、10月28日–11月19日、9月13日–11月13日 | 该关键词已翻至窗口外；关键词分页仍不代表全平台穷尽覆盖。大量整合包／视频宣传不凭标题推荐；LoRA画风本页无新命中，不代表全站无新增 |
| Sena404作者跟踪 | UID341674866，页1／30，总数87 | 范围10月15日–11月19日，最新第30期／BV1DSsh6iEJv；完整简介／分P和54秒媒体、10常规／末秒帧＋3定点，共13帧 | 投稿30与片内40分别保存；历史媒体不重下，新作品“绝区零薇薇安”只读投稿元数据，不冒称教程已读；未取评论或逐图配方 |
| bilibili其他候选 | BV18qsm6SEm9 info | Doc_workBox模型横评：完整简介、单P1434秒；只有外链／网盘等简短说明 | 超600秒且未取得章节／字幕范围，本轮未下载全量视频，不按横评标题写模型排名。Sena短片无需口播转写，本轮无新ASR |
| Reddit | 两社区new.json各50／30；site域搜索11月19日model、LoRA、workflow、prompt、tutorial、guide | 最新列表均403；搜索后打开SFT四步作者帖与MOSS出图问题帖，正文及可见一级回复可读；再追到作者HF卡 | 原页多为相对时间，索引日期另记；没有把搜索当完整new覆盖。问题帖意见互有冲突，不拼成统一最优配方 |
| Hugging Face | text-to-image最新80、image-to-image最新30；Anima／Illustrious／NoobAI各最新15 | 读SFT蒸馏、Anima turbo／Pixel Decoder、H3风格、Real Skin原卡与镜像、Tile、LiliPixel；固定revision和模型卡列于详情，部分图与小JSON补读 | cfgscale与SEEDRAAI镜像合并；Base/SFT、合并／训练／解码分开。IL／Noob仅检查列表，未据更新日强行新增；未下载权重 |
| GitHub | comfyui workflow pushed>=2026-11-19最新25；comfyui prompt created>=2026-11-18最新15；跟进原作者仓 | 读MOSS LLLite、Dynamic Ratio、Smart Wildcards固定README；按源链接查候选 | Ollama Studio元数据可读但commits返回409空仓，未取得README，不按简介写实现；没有安装／编译／运行。SFT基础图只读公开JSON关键控件 |
| Civitai社区／论坛 | Newest模型40、文章30、Workflows15；具体文章39204、39185及资源3058591、3058538、3050466 | 文章正文、模型与版本描述／依赖可读；Seedreamstyle v2.0与HF同源合并；Krea2 v1.1依真实版本日期选取，不按API顺序判新旧 | areyouokay JSON附件401未取；Shiiro漫画风只给少量权重／CFG说明，本轮未看图不猜风格。Prompt Enhancer和LoRA Stacker两文正文很短，未取配套配置，不单独扩写教程；未读评论区／作品元数据 |
| Comfy社区论坛 | latest.json、topic4909公告JSON | 入口仍200；公告标题Nov18、正文说明Nov20下线，昨日已记录，未当新教程 | 当前可读不等于日后仍在线；未访问Discord，不声称覆盖其讨论，也未批量搬运论坛 |
| note.com补充 | ComfyUI最新搜索15 | 请求403，未取正文 | 访问受限，不能称无优质内容 |

## 后续关注与更正

- **Sena水位**：投稿30／片内40已增量保存，并回链[系列记录](../2026-11-09/notes/Sena404画师串与相关分享.md)。两种期号不合并；1–24历史读取和25–29增量范围保留。
- **具体兼容条件**：MOSS四步的BF16基座、专用alpha与ManualSigmas不能移成通用加速规则；Tile V1、颜色Guide与其他蒸馏／风格LoRA效果没有本库组合验证。
- **配方与比较**：Seedreamstyle场景15的6K是加“关窗”词的版本，已对照设置；Real Skin对照的人物姿态／取景也变，保留观察，不承诺身份像素不变。Anima Pixel Decoder公开测速属于旧头，当前头另记。
- **读取缺口**：B站ComfyUI关键词第4页已跨日期窗口，但未代表全平台穷尽覆盖；areyouokay工作流附件401、贴吧采样表图与原制作者未取。已读内容直接收录，不等待这些缺口，也不补称已读。
- **来源跟进**：论坛当前仍可读但正文写11月20下线，未来改用其作者指定公共入口时记录实际范围；本轮未进入Discord。工具／许可变化以新原文更正，原始条件保留。
- 本轮没有生图或迁移实验待办。原作者陈述、本库看图与实际执行分记，归档不替代生成器实现或收益验证。
