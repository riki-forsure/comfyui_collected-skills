# 2026-11-24 每日生图社区发现

- **北京时间与时间窗**：11月24日04:03开始，主要列表与原文于04:04起检查，承接11月23日约04:03的成功检索水位。旧版本补读和实际更新分别注明。
- **检索类型**：每日广泛发现，无具体差距要求。
- **执行状态**：精选9项，部分列表、附件和字幕取得受限。正文记录实际取得的资料、原作者说明与本库看图范围。本轮执行为阅读归档，未安装节点、下载生成权重、启动生图或复跑。
- 感谢各位原作者、上游项目维护者与分享者。以下为本库中文概述与学习备注，请回原文阅读完整方法、配置和使用条件。

## 今日发现

H3作者对照把皮肤与发丝过锐、换种子的面孔差异和保留参考身份分开评估。MOSS新增骨架控制适配器及PNG布局回读入口。另有按幕编排的提示工具、公开领域画作选材方法、以情绪和色盘分控的漫画上色、Illustrious工作流更新、逐笔油画模拟及Sena404第32期。

## 分享速查

| 类别 | 分享／资源 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点 | 读取与验证状态 |
|---|---|---|---|---|---|---|
| 摄影采样 | [MiniMax H3 Image：人像锐化与种子多样性的对照](#n01) | 摄影人物·采样精修｜查看H3人像采样怎样影响毛发、肤质与换种子后的面孔。 | 设计思路：自然肤质·镜头描述｜作者用拍摄距离、用光和细小肤质信息控制照片感。 | Reddit u/Infamous_Campaign687／PixlStash · [原帖](https://www.reddit.com/r/comfyui/comments/1y3mbd6/minimax_h3_image_without_the_crunchy_hair_and/) · [完整方法与对照](https://pixlstash.dev/minimax-h3-image.html) · [文生图API配置](https://pixlstash.dev/assets/minimax-h3-image/workflows/minimax-h3-image-t2i.json) | LCM改善作者的人像样例，首步空图保留较多种子差异 | Reddit主帖、作者回复、报告文字与一份API图；未看图、未复跑 |
| 姿态控制LoRA | [MOSS SFT pose LoRA step 2400：骨架与人物描述分别输入](#n02) | 姿态控制·参考图编辑｜把DWPose骨架送入MOSS SFT编辑条件组织动作。 | 设计思路：动作与外貌分工｜用骨架给姿势，把人物、服装和场景留给文本描述。 | niuhesanlu；工作流借鉴thedeoxen · [固定模型卡及两套图](https://huggingface.co/niuhesanlu/MOSS-Image-SFT-pose-lora-step2400/blob/c1221b163d6a650b541f529f8ba500524a306fe8/README.md) · [骨架输入图](https://huggingface.co/niuhesanlu/MOSS-Image-SFT-pose-lora-step2400/blob/c1221b163d6a650b541f529f8ba500524a306fe8/workflows/skeleton_to_image.json) | 骨架直输／照片提骨架两入口，MOSS编辑格式ai-toolkit | 模型卡全文与一份JSON关键节点；未看成图、未验证兼容 |
| 布局节点 | [Layout Studio for MOSS-Image v1.1.1：从PNG取回可编辑布局](#n03) | 构图控制·多主体布局｜把MOSS框选提示导回画布，调整文字和角色位置。 | 设计思路：对象分框·版面复用｜把对象、文字和角色作为独立元素，保留各自位置与描述。 | Rexoplanets · [Civitai精确版本](https://civitai.com/models/3051607?modelVersionId=3484814) · [Web版release](https://github.com/Rexoplanets/layout-studio-moss-image/releases/tag/v1.1.1) · [Comfy节点文档](https://github.com/Rexoplanets/layout-studio-moss-image-comfy-node/blob/52d54c3fa3344264f1524e5f3ba1c5f74b945fd6/README.md) | 新增Comfy节点入口，含MOSS提示元数据的PNG可回编辑 | 资源页、release、节点文档、Reddit主帖与可见回复；未导入实测 |
| 视觉提示工具更新 | [Libretto v0.26.1122.1：按节目与幕组织场景](#n04) | 提示词组织·场景复用｜按节目、幕和场景复用提示预设并支持Klein模板。 | 设计思路：多场景编排｜将角色、服装、姿态和灯光做成可复用块，再按幕组织。 | Higeneko9／higeneko9 · [新版介绍](https://civitai.com/articles/39579) · [精确release](https://github.com/Higeneko9/Libretto/releases/tag/v0.26.1122.1) · [固定README](https://github.com/Higeneko9/Libretto/blob/7f4f96f373baa0220110a414622119019f91ab35/README.md) | 新增Show／Act层级，导入FLUX.2 Klein文生图模板 | 介绍全文、release及固定README相关段；未打开程序 |
| 风格训练方法 | [Tsumugi Lab：公开领域画作的风格LoRA筛选方法](#n05) | 画风搭配·数据选材｜看Illustrious如何兼顾媒介特征、人物数量和小主体。 | 设计思路：媒介选材·检查点筛选｜按媒介检索选图，固定提示与种子筛出可用早期检查点。 | Tsumugi_Lab；PD12M与Nova Anime XL等原作者 · [原文](https://civitai.com/articles/39574) · [浮世绘v1.0](https://civitai.com/models/3057572?modelVersionId=3478600) · [本例作品](https://civitai.com/images/149454657) | 限定素材来源与单作者上限，用固定内容检查失真 | 文章／浮世绘模型说明、1张示范与4条作品记录；未核数据许可清单 |
| 漫画上色 | [Sana Coloring：五类上色控制与42页示范](#n06) | 漫画上色·色彩控制｜用情绪、光照和色盘给黑白漫画建立上色方向。 | 设计思路：气氛分层·色盘控制｜按情绪、时段、用光、饱和度和调色板拆开上色选择。 | masterofaudio2077；Sana原作者与示范页原创作者 · [固定模型卡](https://huggingface.co/masterofaudio2077/sana-manga-coloring/blob/f2ac5248c547f37df8846e6f774771b8b992b0e6/README.md) · [42页拼图](https://huggingface.co/masterofaudio2077/sana-manga-coloring/blob/f2ac5248c547f37df8846e6f774771b8b992b0e6/results/grid.webp) | 旧训练权重公开，最新提交补6页示范 | 模型卡全文、提交记录、原版拼图缩览；未读个别图配方 |
| Illustrious工作流 | [Sequence7 Illustrious v1.1：提示组合与姿态分支](#n07) | 提示词组织·精修·姿态控制｜查阅Illustrious预览、二次采样和姿态分支。 | 设计思路：分阶段精修｜先看低成本预览，再放大补细节，需要时从参考图取姿态。 | Sequence7；LoRA Manager、Impact Pack及所列节点作者 · [普通版v1.1](https://civitai.com/models/3057070?modelVersionId=3485301) · [OpenPose版v1.1](https://civitai.com/models/3057070?modelVersionId=3485324) | 两版接入LoRA Manager Prompt并修正trigger切换连线 | 模型资源说明全文与版本元数据；附件端点返回HTML，作品检索为空 |
| 油画模拟实践 | [aibrush：把油画笔触拆成可记录的绘画动作](#n08) | 笔触设计·油画模拟｜了解如何按形体、用光和材质安排逐笔绘制。 | 设计思路：逐笔决策·边缘组织｜先安排主次与软硬边，再让颜料厚薄和笔触方向描述形体。 | neokrasav4ik；贴吧转介死历史 · [贴吧原帖](https://tieba.baidu.com/p/11223388232) · [固定项目README](https://github.com/neokrasav4ik/aibrush/blob/e6c998af7c0c9895c96837e83bb2032844ab2407/README.md) | 通过程序接口描述压力、笔触与湿画混色 | 贴吧2楼文字与固定README；未读引擎实现、未执行 |
| Anima画师串 | [Sena404投稿第32期：yoko juusuke](#n09) | 人物插画·画师标签｜查阅细线厚涂的人物表现和结构服饰受光示范。 | 美术风格方向：细线厚涂·高彩人物｜本组收下颌、大虹膜与收腰造型，细线结合柔亮皮肤和强反光服饰。 | Sena404；卡片标注画师yoko juusuke · [原视频](https://www.bilibili.com/video/BV1X9ySzsENy/) | 字面标签 @yoko juusuke，投稿32／片内42 | 53秒P1，封面、十页与末帧抽读；简介仅「-」，逐图配置未知 |

## 当日分享

<a id="n01"></a>

### MiniMax H3 Image：人像锐化与种子多样性的对照

**适用方向：摄影人物·采样精修｜查看H3人像采样怎样影响毛发、肤质与换种子后的面孔。**

**设计思路：自然肤质·镜头描述｜作者用拍摄距离、用光和细小肤质信息控制照片感。**

- 原作者与原文：Reddit u/Infamous_Campaign687／PixlStash · [原帖](https://www.reddit.com/r/comfyui/comments/1y3mbd6/minimax_h3_image_without_the_crunchy_hair_and/) · [完整方法与对照](https://pixlstash.dev/minimax-h3-image.html) · [文生图API配置](https://pixlstash.dev/assets/minimax-h3-image/workflows/minimax-h3-image-t2i.json)
- 原帖《MiniMax H3 Image without the crunchy hair and skin: A/B tests and stock-node workflows》索引标11月23日，原页显示相对时间。作者为PixlStash v2.0.2选择缺省配置，比较同提示、同种子、同画布的裁切，感谢20MP工作流作者LilBrownBebeShoes和Kijai公开的LCM及空图思路。
- 作者报告的设置是原版H3 Image int8 ConvRot去噪器与同系列int8文本编码器，FP16 H3 Image VAE。以SamplerLCM噪声1.10降到0.90、simple、6步、CFG 1缓解发丝与皮肤过锐。文生图再给第1步一张32×32空图作为图像条件。三句轻引导提示各12个固定种子、1024×1024下，作者用InsightFace比较跨种子相似度，LCM单独为0.21，全程空图为0.54，仅首步为空图为0.31。数值针对这组人像，作者也观察到空图会压窄面孔变化。
- 已读公开API图的连接为两个MiniMaxH3ImageConditioning共用文本，空图分支0–0.1，纯文字0.1–1，合并后接CFGGuider，负向取纯文字条件经ZeroOut，提交参数3552×4736、seed 1、denoise 1。这是该图文件当前值，与1024×1024多样性评估条件分开。Euler 1步＋LCM 5步的“保留种子人物”是作者另一路径，参考图角色表也独立，后两份JSON本轮未读。
- 作者的人像提示经验是用镜头、光线、肤质及飞散发丝来表达自然感，涉及分格时描述各视图而避开可能被画进图里的编号。读取主帖、作者可见回复、报告正文文字与一份API配置，无本库视觉对照、复跑或收益结论。

<a id="n02"></a>

### MOSS SFT pose LoRA step 2400：骨架与人物描述分别输入

**适用方向：姿态控制·参考图编辑｜把DWPose骨架送入MOSS SFT编辑条件组织动作。**

**设计思路：动作与外貌分工｜用骨架给姿势，把人物、服装和场景留给文本描述。**

- 原作者与原文：niuhesanlu；工作流借鉴thedeoxen · [固定模型卡及两套图](https://huggingface.co/niuhesanlu/MOSS-Image-SFT-pose-lora-step2400/blob/c1221b163d6a650b541f529f8ba500524a306fe8/README.md) · [骨架输入图](https://huggingface.co/niuhesanlu/MOSS-Image-SFT-pose-lora-step2400/blob/c1221b163d6a650b541f529f8ba500524a306fe8/workflows/skeleton_to_image.json)
- HF《MOSS-Image-SFT pose LoRA, step 2400》固定revision c1221b163d6a650b541f529f8ba500524a306fe8，11月23日19:47:52建仓、19:48:35更新。作者用128组照片、caption和DWPose骨架训练SimpleTuner LoRA，rank与alpha均64，更新172个注意力投影。
- 通用输入是黑底彩色骨架。照片入口先由DWPose生成骨架，作者建议检查漏关节。骨架入口直接从已有骨架图确定画布。本轮读取的骨架JSON使用MOSS SFT int8 ConvRot、qwen3.5_9b_w4a8_gptq、flux2-vae_small，ModelOnly LoRA 1.0，两个编辑编码器均取ai-toolkit，KSampler默认seed 42、30步、Euler/simple、CFG 4、denoise 1。正向示例是阳光车间里的蓝色工装自行车技师，实际执行未取得。
- 作者的SimpleTuner评估16个留出骨架里15个有可计分关节，匹配43.26%、换骨架基准5.38%，命中定义为关节位置落在参考人物框长边10%内。作者另报告ComfyUI导出接上172处更新，两个数字评价条件不同。
- 图借鉴thedeoxen，但本条权重为独立训练。另一个step 4500卡使用线性rank 64、卷积rank 16，本轮分别查阅，不合并成同一个权重。未读照片JSON、日志、原生例图或权重，卡未明示权重许可，工作流许可按仓内文件。

<a id="n03"></a>

### Layout Studio for MOSS-Image v1.1.1：从PNG取回可编辑布局

**适用方向：构图控制·多主体布局｜把MOSS框选提示导回画布，调整文字和角色位置。**

**设计思路：对象分框·版面复用｜把对象、文字和角色作为独立元素，保留各自位置与描述。**

- 原作者与原文：Rexoplanets · [Civitai精确版本](https://civitai.com/models/3051607?modelVersionId=3484814) · [Web版release](https://github.com/Rexoplanets/layout-studio-moss-image/releases/tag/v1.1.1) · [Comfy节点文档](https://github.com/Rexoplanets/layout-studio-moss-image-comfy-node/blob/52d54c3fa3344264f1524e5f3ba1c5f74b945fd6/README.md)
- 原帖《The Layout Studio for MOSS-Image v1.1.1 — now available as a ComfyUI node + import a prompt from a .PNG image》，Reddit索引标11月22日，当前版Civitai 3484814为北京时间11月23日04:40:37，GitHub Web版v1.1.1于04:18:19发布。
- Web版用于独立整理框选，组件包括text／object／character，导出MOSS中心坐标JSON或普通文本。PNG回读以图内含可识别的MOSS JSON元数据为前提，作者列ComfyUI、Civitai在线生成与Tensor Art三个来源。Comfy版的JSON Output接入正向提示节点。发布说明具体写修正部分撤销／重做，PNG功能在节点说明功能段标v1.1.0，节点ChangeLog则写初始发布与Web版对齐为v1.1.1，按三个来源各自原意呈现。
- 作者在[Reddit回复](https://www.reddit.com/r/StableDiffusion/comments/1y2z3i5/the_layout_studio_for_mossimage_v111_now/)澄清框只约束提示位置和内容，模型权重不受框控制。与[既有BBox Studio条目](../2026-11-14/README.md#n04)是两位作者的独立工具，入口保留。
- 已读文档及讨论文字，版本检出的两条作品记录meta均空，无逐图配方。未打开界面或测试跨平台兼容。节点README列GPL-3.0，未逐项核分发包许可。

<a id="n04"></a>

### Libretto v0.26.1122.1：按节目与幕组织场景

**适用方向：提示词组织·场景复用｜按节目、幕和场景复用提示预设并支持Klein模板。**

**设计思路：多场景编排｜将角色、服装、姿态和灯光做成可复用块，再按幕组织。**

- 原作者与原文：Higeneko9／higeneko9 · [新版介绍](https://civitai.com/articles/39579) · [精确release](https://github.com/Higeneko9/Libretto/releases/tag/v0.26.1122.1) · [固定README](https://github.com/Higeneko9/Libretto/blob/7f4f96f373baa0220110a414622119019f91ab35/README.md)
- 原帖《Libretto: A Visual Prompt Builder for ComfyUI v0.26.1122.1 Available now》。文章发布11月23日15:52:49，release发布15:10:58。相对[11月15日报v0.26.1111.2](../2026-11-15/README.md#n07)，明确新增Show／Act场景组织及FLUX.2 Klein文生图模板支持。
- README写明移动场景保ID、历史及生成结果，复制会给新ID、从空历史开始。输出路径按工作流默认、Show／Scene或Show／Act／Scene组织。工作流导入可展开子图，包括KSampler，或带RandomNoise、Guider、Sampler和相应Scheduler的SamplerCustomAdvanced路径。修改服务端工作流后需重新导入。
- 本库备注：该层级适合复用镜头提示及索引结果，实际生成仍依赖已有ComfyUI、模型与工作流。仅读文章、固定README的组织／导入段和release，未看英日视频、下载或运行，软件沿仓库MIT条款。

<a id="n05"></a>

### Tsumugi Lab：公开领域画作的风格LoRA筛选方法

**适用方向：画风搭配·数据选材｜看Illustrious如何兼顾媒介特征、人物数量和小主体。**

**设计思路：媒介选材·检查点筛选｜按媒介检索选图，固定提示与种子筛出可用早期检查点。**

- 原作者与原文：Tsumugi_Lab；PD12M与Nova Anime XL等原作者 · [原文](https://civitai.com/articles/39574) · [浮世绘v1.0](https://civitai.com/models/3057572?modelVersionId=3478600) · [本例作品](https://civitai.com/images/149454657)
- 原文《Style LoRAs trained only on public-domain art: how and why》11月23日13:07:11发布。按作者说明，素材取自PD12M的Public Domain及CC0记录，以CLIP按媒介选图、单作者最多120张、从caption移除作者名、短边至少768。系列每套约600张，单独浮世绘卡称约700张，两处范围不互相替代。
- Nova Anime XL v19、kohya-ss sd-scripts、rank 32、仅UNet、1200–1600步，每400步存档。作者固定五个提示和种子，比较双人数量、基座脸形是否仍相近、小主体能否保留，以最早满足这些条件且风格清楚的检查点为发布候选。铜版刻线样式没达到预期，因此未发。
- 浮世绘v1.0／3478600是11月19日02:20:09发布的旧资源，本轮首读并与新文章合并。模型卡给1200步、无trigger、权重0.5，并报告高于0.8时可能有面孔或双人融合变化，猫也易变成人。作者的系列筛选标准与个别LoRA的实际短板同时保留。
- 本库看图仅限浮世绘一张全身侧视示范：压低的眉眼和紧闭口形呈沉静侧望，上身宽袖、下身长褶拉开轮廓，红裙与靛蓝衣面以墨线分区，背景为米白留空与天际蓝渐层。属于这个例子的构图和服饰，系列还包含墨洗、水彩等独立媒介。样图未取得seed／权重实值，四条作品元数据均缺配方，其中一条关联多个版本。
- 本轮未逐张核训练素材、下载权重或审查底模政策，公开领域／CC0描述按作者声明，实际使用仍看具体原作及底模许可。

<a id="n06"></a>

### Sana Coloring：五类上色控制与42页示范

**适用方向：漫画上色·色彩控制｜用情绪、光照和色盘给黑白漫画建立上色方向。**

**设计思路：气氛分层·色盘控制｜按情绪、时段、用光、饱和度和调色板拆开上色选择。**

- 原作者与原文：masterofaudio2077；Sana原作者与示范页原创作者 · [固定模型卡](https://huggingface.co/masterofaudio2077/sana-manga-coloring/blob/f2ac5248c547f37df8846e6f774771b8b992b0e6/README.md) · [42页拼图](https://huggingface.co/masterofaudio2077/sana-manga-coloring/blob/f2ac5248c547f37df8846e6f774771b8b992b0e6/results/grid.webp)
- HF《Sana Coloring》基于Sana 600M 1024px Diffusers，作者卡列teacher phase的EMA step 30000，实际训练512px。11月24日00:31:30固定revision f2ac5248c547f37df8846e6f774771b8b992b0e6提交说明是新增6页示范，拼图由36页变42页，模型卡未报告这次提交重新训练。
- 黑白输入可选mood、time_of_day、lighting、saturation、palette，字段空值交给模型推断。作者Python例把短边缩到512、长宽取32对齐，演示vivid和bright primary colors组合。需作者的代码及Sana底模，未取得普通ComfyUI对应工作流。作者指出密集排线／网点可能变成斑块，衣服和肤色会混。
- 本库查看2336×3900拼图的缩览，多个页面层次从米棕暖调到蓝紫／青色冷调，近景脸与暗背景常以不同色面拉开，黑线与分格仍可见。漫画人物比例和神情来自各原页，未将它们归为上色模型统一造型。未逐页核对原黑白输入、线稿细节及每页控制值。卡标Apache-2.0，示范漫画页原作使用条件另计。

<a id="n07"></a>

### Sequence7 Illustrious v1.1：提示组合与姿态分支

**适用方向：提示词组织·精修·姿态控制｜查阅Illustrious预览、二次采样和姿态分支。**

**设计思路：分阶段精修｜先看低成本预览，再放大补细节，需要时从参考图取姿态。**

- 原作者与原文：Sequence7；LoRA Manager、Impact Pack及所列节点作者 · [普通版v1.1](https://civitai.com/models/3057070?modelVersionId=3485301) · [OpenPose版v1.1](https://civitai.com/models/3057070?modelVersionId=3485324)
- 原文《Sequence7's Custom Illustrious Workflows》。两版v1.1分别于11月23日13:12:51及13:18:56发布。作者列出改动：增加LoRA Manager Prompt、重接TriggerWord Toggle，整理节点布局。流程为首轮预览、低噪放大二采、Face Detailer，另有接OpenPose参考的版本。
- 作者列rgthree-comfy、Impact Pack／Subpack、LoRA Manager和controlnet_aux，脸检测为bbox_faceyolov8m.pt，姿态版说明用illustriousXL_openpose。适用范围按作者的Illustrious图理解，精确基座、采样值、旁路开关与逐图配置本轮未知。
- 两版可区分的版本号与附件文件名取得，读取OpenPose附件的HTTP响应实际为HTML，没拿到JSON。对应作品查询返回空列表，未读取页面社区评论或看示范图。原文仅作为工作流结构与更新入口收录。

<a id="n08"></a>

### aibrush：把油画笔触拆成可记录的绘画动作

**适用方向：笔触设计·油画模拟｜了解如何按形体、用光和材质安排逐笔绘制。**

**设计思路：逐笔决策·边缘组织｜先安排主次与软硬边，再让颜料厚薄和笔触方向描述形体。**

- 原作者与原文：neokrasav4ik；贴吧转介死历史 · [贴吧原帖](https://tieba.baidu.com/p/11223388232) · [固定项目README](https://github.com/neokrasav4ik/aibrush/blob/e6c998af7c0c9895c96837e83bb2032844ab2407/README.md)
- stablediffusion吧《一种用大语言模型使用画笔进行绘画的油画模拟器，aibrush》由死历史11月24日00:03:29发帖转介。GitHub原项目归neokrasav4ik，固定commit e6c998af7c0c9895c96837e83bb2032844ab2407于11月23日22:22:08更新，README自报内核8c5ef60。
- 分享的做法是先决定画面主次、作画顺序、笔触方向和边缘软硬，再用Python笔刷按压力模拟颜料与画布互动。README注明创作建议段由Claude Fable 5.2撰写。贴吧列出湿画混合、笔毛、刮刀等模拟能力，属于介绍，底层实现未核。
- 这条是程序化绘画思路补充，适用于研究画笔如何随形、控制厚度和颜色过渡。README列Python≥3.10、NumPy／SciPy，示例需Pillow，项目AGPL-3.0。仅读首楼及另1楼文字与固定README，未看实际绘画示例、审源码或运行模型。

<a id="n09"></a>

### Sena404投稿第32期：yoko juusuke

**适用方向：人物插画·画师标签｜查阅细线厚涂的人物表现和结构服饰受光示范。**

**美术风格方向：细线厚涂·高彩人物｜本组收下颌、大虹膜与收腰造型，细线结合柔亮皮肤和强反光服饰。**

- 原作者与原文：Sena404；卡片标注画师yoko juusuke · [原视频](https://www.bilibili.com/video/BV1X9ySzsENy/)
- 《anima画师串第三十二期》由Sena404于11月23日19:39:46发布，UID 341674866。封面原帧核字为“第42期”“2026.11.23”“20图实测”，B站投稿标题是第三十二期。上期已收投稿31且片内总期号未读出，本轮单独记载新视频所见，不补猜上期。
- 本组字面标签为 `@yoko juusuke`，首尾原帧已核，含空格，卡片未给权重。作者页04–09提出细线闭合、厚涂和柔雾高光，提及手部中等偏稳以及极端姿态／背面不稳。这些是作者对自己示范的总结。
- 本库看图范围为十页示范：多例集中于肩腰线条明显的半身或近景，脸部向下收，眼睛大且高光清楚，鼻口简化。视线见直视与侧看，微笑、严肃与腼腆随角色变化。制服和甲片靠较硬反光及暗色折面塑造体量，皮肤以软渐层上色。页03站姿、页08抱臂及页09坐姿显示不同体型和取景，不能由单图推断统一头身。视频展示归Sena404，原画师原作范围没有逐件核对。
- SDK完整简介和53秒P1，短边480；主媒体567，使用同SDK响应的一个备用200成功，1759786字节。以约5秒间隔抽11帧＋末帧，OCR辅助后对照封面和十页卡片。未取得字幕、音轨／ASR、评论、独立原图、权重、采样或逐图提示。媒体和OCR原文保存在临时研究目录。旧系列入口见[历史索引](../2026-11-09/notes/Sena404画师串与相关分享.md)。

## 平台覆盖与读取限制

| 入口 | 实际检查 | 结果与边界 |
|---|---|---|
| 百度贴吧 stablediffusion | aiotieba 4.8.2 CREATE第1页30条，最新普通帖11月24日00:30，页尾11月21日23:24，已跨昨日水位。置顶另辨。全站“工作流 提示词”“模型 LoRA”“教程 分享”各1页，实际27／30／28条。 | 带空格 `stable diffusion` 的SDK入口解析成stable吧，两条均为2018年公告，与本次规范吧名分开。按tid去重并读aibrush、ModelVault、镜头视角三帖楼主文字及当页回复。aibrush收录，ModelVault仍为测试版，作者计划正式版开源。镜头帖当页为提问和同问，未取得方法。未读图、楼中楼或启用Astron。 |
| 百度贴吧 comfyui | 同主工具独立CREATE第1页29条，最新普通帖11月24日01:11，页尾11月20日00:38，已跨昨日水位。以实际吧名筛全站词页。 | 可见当日安装／硬件求助、整合包介绍与造型可行性问题。本轮该范围未选正文条目，结论仅覆盖已查列表；未检查私域资料与图帖内页。 |
| bilibili | SDK 17.4.2 pubdate：“ComfyUI 教程”1–4页80条，首屏11月23日17:46至24日02:26，第3页最早22日20:22已过水位。“生图 模型”“Anima 生图”“LoRA 画风”各1页20条。 | 按BV去重查Sena及另两视频完整简介。另查[无限画布第八弹](https://www.bilibili.com/video/BV1mPyXzxEkM/)关联[源码固定README](https://github.com/YangShu2103/ComfyUI-Infinite-Canvas/blob/3560f049e717cf479bba317e4fa167d3e598d11a/README.md)，提交标v0.5.8并说明多轨时间线与导出，未读该视频画面。另一个节点对齐视频只给网盘，版本未知。 |
| bilibili Sena404 | UID341674866投稿第1页30条，总计90，最新为第32期，紧随已收第31期。 | 第32期成功取53秒P1和12帧，核画面标签与片内编号。zh-CN请求返回login_required，未配置会话。无音轨、ASR或评论读取，照片只按视频内所见记录。 |
| Reddit | r/StableDiffusion最新50、r/comfyui最新30的JSON均403。再用日期和类别词检索，两版打开具体原帖。 | H3主帖、作者回复、外链报告与一份API图可读。Layout Studio主帖及作者关于框选用途的可见回复可读。其余如工作流展示或提示词讨论仅读索引摘录，未称整社区列表或全评论已读。 |
| Hugging Face | 文生图最新80、编辑最新30，Anima／Illustrious／NoobAI各15。 | 固定pose 2400与另一个step 4500卡、Sana卡和示范、另读BudgetLatent与ICTone卡作为候选。Anima关键词混入Animation／Animal，按家族筛选。未下载模型。 |
| GitHub | 更新的ComfyUI工作流仓25项、提示相关新仓列表上限15，追原作者原仓、发布和固定README。 | 读Libretto release、Layout Web版release及Comfy节点README、aibrush、Infinite-Canvas。另读AusBoss文档入口；本轮精选看可确认新增内容。未安装项目或核运行表现。 |
| Civitai文章与社区 | Newest文章30篇。读公共领域选材、Libretto更新、TagDeck、Art Nouveau文章正文。 | TagDeck文章介绍从同名caption导入和kohya目录导出，保留为后续线索。公开领域选材与同作者浮世绘模型合并。其它评论未批量读取，本轮版本用途讨论从作者的Reddit原帖补读。 |
| Civitai模型／版本、工作流、作品 | Newest模型40、工作流15。查看Layout Studio、Illustrious v1.1、Super Simple Anima、BBox Studio和浮世绘具体资源／版本。 | 浮世绘示范1张已看，作品API四条meta为空；Layout两条meta为空，IL OpenPose版查询无记录。IL及Super Simple Anima附件响应为HTML，未取得可用JSON。工作流更新仍可读作者说明，未核逐图配方或全部版本讨论。 |
| 补充论坛与作者资料 | Comfy官方论坛latest.json HTTP 200，顶部为LTX求助及较旧主题，未深读；note.com ComfyUI最新15查询HTTP 403。PixlStash作者报告以直接HTTP取得。 | 论坛范围与note.com访问失败分别记载。没有以网页索引代替主工具的两吧和B站检查。 |

## 后续关注

- H3对照可按作者报告继续查阅参考图身份和固定种子的两份配置，保留独立测试条件。姿态LoRA的评估只说明作者的留出骨架集，进一步参考时核对应入口、骨架和输入图尺寸。
- Layout、Illustrious和浮世绘的逐图参数缺口待原作者补充。Sana后续如更新权重或有逐页元数据，再区分模型变化和示范图库更新。
- Sena水位推进投稿第32期／片内第42期。继续按UID、BV及投稿日期去重；本期画师标签已核，完整生成参数未知。
- 实际阅读、附件取得、复跑与收益分开记录，后续执行沿用单独授权。

[日期索引](../README.md) · [总索引](../../每日检索可速查总结.md)
