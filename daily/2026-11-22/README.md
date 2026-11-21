# 2026-11-22 每日社区发现

感谢模型、教程、工具与示范素材作者的公开分享。本页为中文概述与导读，保留原文、作者、版本和读取范围，欢迎回原帖阅读完整说明、更新及讨论并支持原作者。署名／链接不等于转载授权，第三方成果不作为本库原创。

- 北京日期与检索时间：2026-11-22，03:56起读取仓库规范与近期归档，03:57起逐平台检索；本页记录保存前已完成的阅读。
- 检索类型：无具体差距要求的每日广泛发现；未另设主动专题。
- 时间窗：接续[11月21日](../2026-11-21/README.md)清晨04:00–04:07实际检索水位，优先新增与实质变化。昨日午后是归档时间，不用它跳过清晨后的新增；近期首次补录标真实日期。
- 执行状态：精选10项，涵盖独立模型／适配器、漫画上色、GLM与Illustrious训练经验、布局、角色预设、景别和抠图；部分列表、原图、附件及平台字幕受限。
- 标注归属：适用方向、美术风格／设计思路为本库整理；作者说明、社区反馈、本库看图与运行／收益验证分开。未知配置不补造。
- 执行边界：仅研究与归档，复用现有SDK、FFmpeg、OCR及环境；未安装节点、下载生图大模型、启动推理／训练／自动实验、增加服务／测试体系或派发子代理。资料保存不等于生成器实现或效果验证。

## 今日值得阅读

- **新路线与后训练**：[dflow预览](https://huggingface.co/data-archetype/dflow_2b)、[AlphaAnything透明适配器](https://huggingface.co/WLuLi/AlphaAnything)与[MOSS漫画上色](https://huggingface.co/sorryhyun/MOSS-I2I-LORAs)各自限定输入、基座和版本；示范所属旧版也保留。
- **训练经验**：[CAME等时比较](https://civitai.com/articles/39357)看角色特征而不只看loss；[GLM漫画线条教程](https://civitai.com/articles/39340)提醒先确认实际训练组件，保留单案例边界。
- **工作流与设计实践**：[Canvas2.0](https://civitai.com/articles/39402)和[问秋月](https://tieba.baidu.com/p/11217209569)是两套布局组织方式；另有角色预设、SDXL景别滑块与[RMBG抠图视频](https://www.bilibili.com/video/BV19TyizJEK9/)抽读。

## 分享速查

| 类别 | 分享／资源与版本 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点／可学习经验 | 读取状态 |
|---|---|---|---|---|---|---|
| 新家族预览 | [dflow_2b 0.215：自然语言、布局转换与旧示范分开](#n01) | 模型选型·版式生成｜查阅独立2B模型的摄影定位、布局输入与版本条件。 | 美术风格方向：复古平面海报·剪影｜本例蓝绿底配橙色日轮和米白标题，纸纹统一大色块。 | Data Archetype／Reddit u/quantiler；T5Gemma与相关作者；[固定模型卡](https://huggingface.co/data-archetype/dflow_2b/blob/0957ad94ba0a6986eae87a4ea41f6c60a63c4b57/README.md) · [作者发布帖](https://www.reddit.com/r/StableDiffusion/comments/1y1upwu/dflow_2b_small_indie_t2i_model/) | 0.215与0.21同权重，改布局转换；海报图仍标0.2 | 主卡、release、默认JSON关键节点、海报段与1图；未运行 |
| RGBA适配器 | [AlphaAnything：透明素材生成与对象提取的两套入口](#n02) | 透明素材·分层合成｜区分文生RGBA、图像提取和各基座适配器条件。 | 设计思路：透明材质·独立图层｜本例玻璃鸟保留轮廓高光，腹部透出棋盘预览。 | Qijie Wang、Zhixin Xu等／WLuLi；Tsinghua、ByteDance、PKU及基座作者；[固定模型卡](https://huggingface.co/WLuLi/AlphaAnything/blob/dce736ec46a4c2e90bccfb8adf385b333db15987/README.md) · [固定代码README](https://github.com/WLuLi/AlphaAnything/blob/56e97676c2d275c91a7a758d8b0e5337ef009247/README.md) | transformer LoRA＋alpha decoder成套；四步迁移有可靠性取舍 | 主卡、README主要方法／用法、1张棋盘示范；未读论文／运行 |
| MOSS漫画后训练 | [MOSS i2i colorize v5：角色颜色框与原页文字分别处理](#n03) | 漫画上色·区域提示｜阅读MOSS Base专用颜色框、参考latent及文字保留方法。 | 设计思路：角色分区·文字保留｜用角色框指定颜色，原页文字不再依赖OCR逐字重写。 | sorryhyun；MOSS、anima_lora与示范原画作者；[固定模型卡](https://huggingface.co/sorryhyun/MOSS-I2I-LORAs/blob/d2c1274e09acc48c9006fbb963c7c7f30bcf415c/README.md) · [v5公开工作流](https://huggingface.co/sorryhyun/MOSS-I2I-LORAs/blob/d2c1274e09acc48c9006fbb963c7c7f30bcf415c/colorize/moss-i2i-colorize-v5.json) | Base参考条件；v5不带OCR文本，v4仍是OCR-caption版本 | 主卡全文、v5 JSON关键节点、1张三组横幅；未复跑 |
| Illustrious训练比较 | [CAME与AdamW8bit：等训练时间比较角色特征](#n04) | LoRA训练·比较方法｜参考等时刻、固定提示与多景别观察角色学习差异。 | — | tboilettrauma；数据作者abbuibuibui与优化器／基座作者；[原文章39357](https://civitai.com/articles/39357) | loss相似不等于角色相同；等时间与等步数是不同口径 | 正文全文、技术附录与附件元数据；对照图403、附件400 |
| GLM风格训练教程 | [GLM-Image漫画线条：先核训练的是AR还是解码器](#n05) | 画风训练·线条表现｜阅读GLM双阶段训练中笔触未被学到的排查经验。 | 设计思路：线条粗细·排线｜按作者经验，将构图学习与解码笔触训练分别检查。 | tobalaseabegunde3494；GLM-Image、JoyCaption及相关作者；[原教程39340](https://civitai.com/articles/39340) · [GLM官方固定卡](https://huggingface.co/zai-org/GLM-Image/blob/2c433cc0cbc293bde2ac8ca9624f279b5d23fcf4/README.md) | 单案例：AR epoch25＋decoder epoch3；不是已验证通用训练方案 | 教程正文、官方架构段、附件元数据；未看图／取得脚本 |
| 布局工具更新 | [MOSS Canvas 2.0：多场景与布局编辑，生成连接另看](#n06) | 构图控制·版式提示｜按场景整理元素框、可见文字和布局JSON。 | 设计思路：场景与元素分层｜全场景描述与每框内容分开，隐藏框不进入生成布局。 | g1ts；OpenMOSS与stable-diffusion.cpp作者；[2.0原文章39402](https://civitai.com/articles/39402) · [固定README](https://github.com/g1ts/moss-image-sft-canvas/blob/9eb02db61336ff56d16debe0044e4d3622077aa6/README.md) | 接续11月6日；项目保存与用于生成的layout不同 | 文章全文、README布局／连接段；未操作界面／运行 |
| 贴吧Agent布局分享 | [问秋月MOSS画板：对话改布局与本地ComfyUI联动](#n07) | 提示词组织·布局协作｜阅读Agent与手工画框结合的MOSS提示组织方法。 | 设计思路：逐框描述·保留约束｜先定人物、物体与文字位置，再限定允许改动的元素。 | 火星539／SAkizuki及问秋月贡献者；MOSS、ComfyUI等上游作者；[贴吧原帖11217209569](https://tieba.baidu.com/p/11217209569) · [固定Space说明](https://huggingface.co/spaces/SAkizuki/WenQiuYue/blob/45585bd43089a24e783d1949e2705d9ac235c208/README.md) | 在线Agent与本地生成分开；浏览器绑定API工作流，不自动执行 | 15楼文字、Space元数据与相关README段；未看示范或调用Agent |
| 角色预设节点 | [Manga Character Preset：角色提示与三组LoRA一起切换](#n08) | 角色管理·提示词组织｜将重复人物的正负提示与LoRA设置保存在工作流。 | — | UNfukashigi；ComfyUI、Anima与各LoRA作者；[固定README](https://github.com/UNfukashigi/ComfyUI-Manga-Character-Preset/blob/50aa8b9d702aa0458edb7a11989330d30e11b708/README.md) | 每工作流独立预设；切换人物不等于区域隔离或身份保证 | README全文、commit与许可元数据；未读示例JSON／运行 |
| SDXL构图LoRA | [Near／Far：主体距离滑块与提示词约束的冲突](#n09) | 构图控制·景别组织｜查阅SDXL距离滑块如何受衣装、动作和景别文字约束。 | 设计思路：景别留白·内容约束｜放宽镜头外细节要求，区分接近动作和接近人脸。 | DetroitWobbly；SDXL及Juggernaut XL作者；[v1.0／3483049](https://civitai.com/models/3060559?modelVersionId=3483049) | 非物理相机推进；近远不对称，可能改变姿态／身份 | 资源全文、版本、3条作品元数据；原图403、配方未取 |
| B站抠图实践 | [RMBG3.0视频实践：生成蒙版、透明输出与发丝边缘](#n10) | 图像抠图·边缘精修｜参考RMBG3.0蒙版流程和不同素材的边缘检查。 | 设计思路：蒙版与原图分开｜先估计灰度遮罩，再合成透明输出并检查细边缘。 | AIwood爱屋研究室；BRIA及ComfyUI作者；[原视频BV19TyizJEK9](https://www.bilibili.com/video/BV19TyizJEK9/) · [重打包固定卡](https://huggingface.co/briaai/RMBG-3.0-Comfy/blob/63880aa074782b09e7ae17184960dfd6de70ab85/README.md) | 视频示例4步CFG1；原始卡401，重打包卡不等于完整教程 | 完整简介、286秒媒体、15常规／末帧＋2原帧核字；无字幕／ASR |

## 当日分享

<a id="n01"></a>

### dflow_2b 0.215：自然语言、布局转换与旧示范分开

**适用方向：模型选型·版式生成｜查阅独立2B模型的摄影定位、布局输入与版本条件。**

**美术风格方向：复古平面海报·剪影｜本例蓝绿底配橙色日轮和米白标题，纸纹统一大色块。**

- 原作者与原文：Data Archetype／Reddit u/quantiler；T5Gemma与相关作者；[固定模型卡](https://huggingface.co/data-archetype/dflow_2b/blob/0957ad94ba0a6986eae87a4ea41f6c60a63c4b57/README.md) · [作者发布帖](https://www.reddit.com/r/StableDiffusion/comments/1y1upwu/dflow_2b_small_indie_t2i_model/)。
- 作者分享：Data Archetype从头训练的2B文生图预览，主要面向摄影和古典艺术，使用小型T5Gemma文本编码器及自有dinac3_96自编码器；支持自然描述与JSON布局。HF仓11月18日建立，固定revision `0957ad94ba0a6986eae87a4ea41f6c60a63c4b57`于北京11月22日00:08更新。Reddit作者u/quantiler的发布帖索引标11月21日，原页仅显示相对时间，未独立核精确时刻。
- 版本实质：[release说明](https://huggingface.co/data-archetype/dflow_2b/blob/0957ad94ba0a6986eae87a4ea41f6c60a63c4b57/RELEASES.md)写0.21是训练583000步的EMA；0.215沿用它，新增MOSS布局／草稿的内部转换，并给无panel的布局补全画布panel。不是新训练权重，也不是MOSS文件改名。模型仍在训练，作者明确质量与seed不稳定、手部／小字与约1MP以上输出有局限。
- 输入与条件：自然描述支持主体、环境、光线、媒介；原生layout的box_2d为0–1000的yxyx，MOSS中心原点像素格式通过转换接入。两种格式不得只因都叫JSON就直接混写。作者要求Python≥3.12、PyTorch2.13、支持BF16的NVIDIA及约7GB空闲显存；4090约10秒和首次编译30–45秒均为作者条件内报告。
- 本库看图：[爵士海报](https://huggingface.co/data-archetype/dflow_2b/blob/0957ad94ba0a6986eae87a4ea41f6c60a63c4b57/assets/gallery/poster_jazz.png)中人形剪影、橙日轮、米白窄体标题形成清晰分区；只看此例，不外推摄影、解剖或通用文字准确率。画廊该图设置明确写模型0.2，seed42、832×1216、50步ER-SDE、PDG2.5、CFG关闭；不是0.215新图对照。底部日期与prompt也不宜仅凭总图认定逐字无误。
- 已读默认JSON关键控件含832×1216、DFlowGuider、ER-SDE、50步及专用时间计划；未执行／审源码捕获最终编码文本。该家族的PDG不直接改写为通用CFG值，旧图配方不与新版默认混成一份实测配置。
- 读取状态：HF主卡全文、release、默认JSON关键节点及画廊海报段，Reddit主帖和少量可见回复；未读技术报告／训练日志。权重、包、文档为MG-BY-NC-2.0；Comfy节点GPL-3.0，编码器依Gemma条款，自编码器另有许可。未下载权重或复跑。

<a id="n02"></a>

### AlphaAnything：透明素材生成与对象提取的两套入口

**适用方向：透明素材·分层合成｜区分文生RGBA、图像提取和各基座适配器条件。**

**设计思路：透明材质·独立图层｜本例玻璃鸟保留轮廓高光，腹部透出棋盘预览。**

- 原作者与原文：Qijie Wang、Zhixin Xu等／WLuLi；Tsinghua、ByteDance、PKU及基座作者；[固定模型卡](https://huggingface.co/WLuLi/AlphaAnything/blob/dce736ec46a4c2e90bccfb8adf385b333db15987/README.md) · [固定代码README](https://github.com/WLuLi/AlphaAnything/blob/56e97676c2d275c91a7a758d8b0e5337ef009247/README.md)。
- 作者分享：AlphaAnything把已有RGB生成器扩展为RGBA，发布的是transformer LoRA与alpha decoder分支，不是完整新底模。HF于北京11月21日22:25建立，revision `dce736ec46a4c2e90bccfb8adf385b333db15987`；GitHub固定commit `56e97676c2d275c91a7a758d8b0e5337ef009247`于22日01:34提交。README时间线写11月22日代码／数据／检查点公开、10月26日论文公开，两种时间分别保留。
- 四个任务包分别针对FLUX.2 Klein Base9B文生／图生RGBA、Qwen-Image-2512文生RGBA、Qwen-Image-Edit-2511图生RGBA；不是任意Qwen2.1或FLUX名字相近的权重都兼容。模型卡明确每包同时需要LoRA与alpha_decoder，RGB基座另行加载。
- 作者用法：文生描述目标素材，图生可用description指定提取对象或完整prompt；Klein Base示例50步／guidance4，已训练在Base上的适配器可接蒸馏Klein9B，示例4步／CFG1。README同时提醒四步偶尔不如Base可靠，不能把能加载等同于所有场景效果等价。
- 本库看图：只看固定commit的[glass-bird-checker预览](https://github.com/WLuLi/AlphaAnything/blob/56e97676c2d275c91a7a758d8b0e5337ef009247/assets/qualitative/glass-bird-checker.png)，鸟体用透明玻璃轮廓、蓝色反光与橙喙组织，内部可见棋盘。该图是棋盘合成示范，不是本库检查过原始输出alpha数值，也未据单图确认折射与背景替换的正确性。
- 读取状态：HF主卡全文，固定README的任务、推理、训练默认与方法说明；论文、数据原文件、权重和推理未读／未执行。Klein适配器为FLUX Non-Commercial，Qwen两包Apache-2.0；GitHub代码许可与各权重条件分开，不以代码开放推断所有权重可商用。未复制其数据或整套素材。

<a id="n03"></a>

### MOSS i2i colorize v5：角色颜色框与原页文字分别处理

**适用方向：漫画上色·区域提示｜阅读MOSS Base专用颜色框、参考latent及文字保留方法。**

**设计思路：角色分区·文字保留｜用角色框指定颜色，原页文字不再依赖OCR逐字重写。**

- 原作者与原文：sorryhyun；MOSS、anima_lora与示范原画作者；[固定模型卡](https://huggingface.co/sorryhyun/MOSS-I2I-LORAs/blob/d2c1274e09acc48c9006fbb963c7c7f30bcf415c/README.md) · [v5公开工作流](https://huggingface.co/sorryhyun/MOSS-I2I-LORAs/blob/d2c1274e09acc48c9006fbb963c7c7f30bcf415c/colorize/moss-i2i-colorize-v5.json)。
- 作者分享：MOSS-I2I-LORAs按上色、文字清理、换字等任务分文件夹；本条重点colorize v5。仓10月23日建立，当前revision `d2c1274e09acc48c9006fbb963c7c7f30bcf415c`于北京11月21日08:10更新。首次收录此作者任务包，不与[11月16日另一作者Manga Colorist](../2026-11-16/README.md#n02)混为同一权重。
- 上色方法：输入作为clean VAE参考latent送入DiT；v5使用角色颜色框与仅带位置的文字框，直接从原页保留字形，不把OCR全文塞回caption。漫画用comic与character items，只有comic时作者说真实黑白页上色偏少；插画可提供颜色／系列标签。v4文件仍保留，采用OCR-caption路径。
- 条件：基座MOSS-Image-Base。v5 helper需Toolkit≥0.13.0、anime-tools≥0.9.4；卡片顶部≥0.6.1是较早通用门槛，不能覆盖v5特定要求。JSON的bbox为画布中心原点、yxyx像素，作者要求紧凑单行；不与N01原生0–1000 box_2d混用。
- 作者公开训练为3334对、rank32、10000步、Muon＋EMA；上色推理写50步、CFG3、ER-SDE、负向分支skip22。已读v5 JSON核到moss_colorize_v5强度1、resolution1024、helper任务colorize_v5、comic、Spectrum采样控件及Loader选择。模型元数据触发的ref_isolate／ref_timestep0来自作者说明，未下载权重核实，也未执行确定最终有效分支。
- 本库看图：[仓库横幅](https://huggingface.co/sorryhyun/MOSS-I2I-LORAs/blob/d2c1274e09acc48c9006fbb963c7c7f30bcf415c/assets/showcase.webp)上色组可见给黑白角色发色、肤色和场景加入颜色，文字布局仍可辨；另两组展示清字与英文化。横幅没有逐图版本／完整配方，不当v5较v4的对照，也不宣称文字像素完全一致。示范漫画原作者未在本轮主卡逐一核清，不转载图片。
- 读取状态：主卡全文、上色v5 JSON关键节点和一张缩放横幅；sanitize／swap_text只读卡片，未复跑或审节点实现。韩文换字的helper条件与上色普通CLIP编码不同，不混成通用步骤。卡片Apache-2.0，原作素材权利另行保留。

<a id="n04"></a>

### CAME与AdamW8bit：等训练时间比较角色特征

**适用方向：LoRA训练·比较方法｜参考等时刻、固定提示与多景别观察角色学习差异。**

- 原作者与原文：tboilettrauma；数据作者abbuibuibui与优化器／基座作者；[原文章39357](https://civitai.com/articles/39357)。
- 原作者与原文：tboilettrauma，CAME vs AdamW8bit on Illustrious XL: Character LoRAs Compared at Equal Training Time，北京11月21日14:57发布。作者在Mariabelle角色训练中发现换优化器后相近loss未对应相近身份表现，进一步用Alya与Suzune比较。
- 作者设置：同一4060、同角色固定图片和caption，Illustrious XL v0.1、U-Net-only、rank8／alpha4、768桶、batch1、训练seed1729；共四组LR：AdamW8bit 1e-4／3e-4，CAME 1e-4／5e-5。记录训练5／10分钟后首个完成step，时间排除加载、cache和写检查点；不把不同优化器在等时间里看到的数据量说成相等。
- 可学习内容：用同prompt／生成seed查发色、眼色、衣装及未被要求的配饰，早期检查点也保存；相似loss下作者仍看到角色特征学习差异。文中蝴蝶结换色、换WAI基座与双人服装归属并非都成功，单人细节出现不代表多主体分配已学会。不是“CAME一律更好”的排名。
- 条件边界：Alya82张、Suzune36张；Mariabelle另20张、1024桶／batch3和余弦计划，约19分钟比较，不能把两系列的分辨率／时间混成同组。每配方仅一个训练seed，WAI场景在看过IL结果后选择，作者也明确未证明768结论可直接迁移1024。
- 作者推理比较写LoRA1、Euler22步、CFG5、768×960；这是该系列比较条件，不是所有IL训练的推荐默认。文中update norm与方向用于定位参数变化，不能直接归因某一层学到了辫子或蝴蝶结。
- 读取状态：API正文全文与技术附录；首张比较图403，configs_and_results.zip公开附件请求400，未取得对照原图／配置包，未视觉确认或审日志。保留数据与原文章入口，未下载角色训练集或运行训练。

<a id="n05"></a>

### GLM-Image漫画线条：先核训练的是AR还是解码器

**适用方向：画风训练·线条表现｜阅读GLM双阶段训练中笔触未被学到的排查经验。**

**设计思路：线条粗细·排线｜按作者经验，将构图学习与解码笔触训练分别检查。**

- 原作者与原文：tobalaseabegunde3494；GLM-Image、JoyCaption及相关作者；[原教程39340](https://civitai.com/articles/39340) · [GLM官方固定卡](https://huggingface.co/zai-org/GLM-Image/blob/2c433cc0cbc293bde2ac8ca9624f279b5d23fcf4/README.md)。
- 原作者分享：How to Train a Style LoRA on GLM-Image (AR + Decoder) and Fix Flat, Uniform Lines，北京11月21日06:38发布。作者希望得到手工漫画墨线，描述用所选官方脚本训练AR约27epochs后仍线条平整，后来发现decoder未训练；另训decoder后自述线重与排线更接近目标。
- 可学习排查：先确认训练触及哪些组件，用原稿经过基础tokenizer／decoder回绘检查是否已损失笔触，再决定是否继续训练AR。作者说AR epochs13与25相近，并承认最终AR25＋decoder3只检了一个prompt／seed，不能把它写成跨画风稳定规律。
- 配置归属：作者628张原尺寸图，宽高需32整除；decoder rank32／alpha32、LR1e-4，称L40S约19分钟每epoch、需约40GB以上。其示例生成1024²、50步、guidance1.5、seed7是该脚本设置，非GLM全场景默认值。caption策略按内容描述而去掉风格用语，是作者这份风格训练做法，不提升为所有角色LoRA打标规则。
- 官方对照：固定GLM卡的架构段确认9B AR＋7B diffusion decoder及Glyph Encoder；这支持两组件需分别理解，不独立证明作者所有训练／caption解释。未核官方finetune脚本的具体revision，文中对其他模型指令编辑能力的个人表述不外推为整个家族不支持编辑。
- 读取状态：教程正文全文、官方卡架构段，未看封面／例图。作者附decoder训练脚本与生成脚本，所请求的训练脚本附件400未取，生成脚本未请求；未审实现、训练、回绘或复跑。文章的“paste below”等草稿字样仅是原文内容，不作为本库执行指令。

<a id="n06"></a>

### MOSS Canvas 2.0：多场景与布局编辑，生成连接另看

**适用方向：构图控制·版式提示｜按场景整理元素框、可见文字和布局JSON。**

**设计思路：场景与元素分层｜全场景描述与每框内容分开，隐藏框不进入生成布局。**

- 原作者与原文：g1ts；OpenMOSS与stable-diffusion.cpp作者；[2.0原文章39402](https://civitai.com/articles/39402) · [固定README](https://github.com/g1ts/moss-image-sft-canvas/blob/9eb02db61336ff56d16debe0044e4d3622077aa6/README.md)。
- 更新关系：接续[11月6日可视化布局编辑器](../2026-11-06/README.md#n03)的同源项目。新文章北京11月22日00:48发布；固定commit `9eb02db61336ff56d16debe0044e4d3622077aa6`于21日23:45提交。相比原先画框／复制JSON，2.0增加多scene文档、逐scene撤销、对齐吸附、隐藏／锁定／复制与meta选择。
- 方法：summary写全场景，items分别写对象、文字与框；隐藏框从生成JSON剔除，但project文件保留hidden状态。多scene项目导出不等于模型已一次生成连贯多页漫画，也不把编辑器z-order当已核模型遮挡控制。
- 坐标：README明确中心原点像素、abs_centralized／yxyx，画布尺寸与输出尺寸对应。N01的dflow可转换MOSS格式，是该模型代码功能，不代表所有JSON工作流都无条件互通。
- 新增生成入口通过stable-diffusion.cpp服务接收布局JSON；托管HTTPS页面可做布局导入导出，直连普通HTTP生成服务会遇mixed-content限制，作者说明生成需本地运行页面或由服务托管页面。不能把静态网页可开当生图已连接。
- 作者仍列SFT50步、CFG3，约5用于更严格框遵循；未提供所有场景对照，不自动移到四步蒸馏LoRA。此项目与N07问秋月是不同作者／项目，不能因都叫MOSS Canvas合并版本。
- 读取状态：2.0正文全文、固定README的功能、layout、生成连接与许可段；未操作／启动服务、审实现或生成。MIT代码，基座与其他依赖条件独立保留。

<a id="n07"></a>

### 问秋月MOSS画板：对话改布局与本地ComfyUI联动

**适用方向：提示词组织·布局协作｜阅读Agent与手工画框结合的MOSS提示组织方法。**

**设计思路：逐框描述·保留约束｜先定人物、物体与文字位置，再限定允许改动的元素。**

- 原作者与原文：火星539／SAkizuki及问秋月贡献者；MOSS、ComfyUI等上游作者；[贴吧原帖11217209569](https://tieba.baidu.com/p/11217209569) · [固定Space说明](https://huggingface.co/spaces/SAkizuki/WenQiuYue/blob/45585bd43089a24e783d1949e2705d9ac235c208/README.md)。
- 原作者与原文：火星539，stablediffusion吧《WenQiuYue在线Agent已支持MOSS交互式编辑》，北京11月21日20:42:49首发。用aiotieba核真实吧名与首楼日期，读取15条可见楼层（到16楼，页内has_more=true），未读后页／楼中楼。对应Space更新于21日16:07，固定revision `45585bd43089a24e783d1949e2705d9ac235c208`。
- 作者方法：手画对象／文字框，或让Agent先提布局，再通过对话与拖拽改位置、尺寸、内容，输出MOSS layout。帖子还介绍导入ComfyUI API格式工作流、绑定prompt／宽高／结果节点与网页参数控制，要求先核实际模型文件名与节点绑定，不是任意普通UI JSON都可直接提交。
- README说明：浏览器维护左上原点abs／xyxy草稿，服务端转换为模型用的中心原点abs_centralized／yxyx；选中局部和锁定布局有不同允许修改范围。文档规则未由本库审实现或实际编辑验证，不能据“锁定”一词承诺成图其他像素不变。
- 边界：本地MOSS推理与在线Agent／标签检索不是同一环节；README含外部LLM API、标签服务及可选联网搜索。其视觉迭代会将当前图供后续模型对照，不能因生成在本机就称所有内容离线。帖子每月免费额度是作者当时说明，未核可用余额或服务承诺。
- 作者的冷门角色逐轮修正属于其示范，缺本库看图／配方复跑，不把“替代某闭源模型”当等效结论。帖中generate_canvas_trial与迭代开关仅作功能导读，本次未启用、访问推理接口或自动出图。
- 读取状态：帖子正文／部分回复，Space公开元数据及README工作台、坐标、联动和API相关段；未读全部源码、参考API图／示范图片、后续楼层或运行界面。主说明未核到明确整体许可证，不因回复称开源就擅自给代码／素材授权。

<a id="n08"></a>

### Manga Character Preset：角色提示与三组LoRA一起切换

**适用方向：角色管理·提示词组织｜将重复人物的正负提示与LoRA设置保存在工作流。**

- 原作者与原文：UNfukashigi；ComfyUI、Anima与各LoRA作者；[固定README](https://github.com/UNfukashigi/ComfyUI-Manga-Character-Preset/blob/50aa8b9d702aa0458edb7a11989330d30e11b708/README.md)。
- 作者分享：为漫画等重复角色项目，把正负提示与最多三组LoRA的MODEL／CLIP强度、开关保存在一个预设中。仓北京11月21日06:34建立，固定commit `50aa8b9d702aa0458edb7a11989330d30e11b708`于07:21提交，首次收录。
- 组织方法：选择人物后一起切换词与LoRA，修改自动写入当前人物；关闭某LoRA仍保留文件名与强度。12个日文快捷按钮追加文字，文档提示可先悬停看全文；不将自动追加词当已经核过的最终编码文本。
- 保存范围：预设嵌入工作流，不是所有工作流共享数据库；复制节点后两份独立。分享JSON同时可能分享提示和LoRA文件名，但不包含模型权重。实际需要兼容的底模与编码器，不能凭Anima分类菜单判断任意LoRA兼容。
- 作者示例明确Anima Base v1.0、Qwen3 0.6B、Qwen-Image VAE，896×1152、32步、CFG4.5、ER-SDE／normal；示例仅两个通用角色且无LoRA。此为文档样例，未读JSON或验证多角色一致性，不把预设切换当多主体区域隔离。
- 读取状态：英日README全文、日期和Apache-2.0许可元数据，未审代码／界面、安装或生成。模型及LoRA按各自条件提供，未复制第三方预设与词库。

<a id="n09"></a>

### Near／Far：主体距离滑块与提示词约束的冲突

**适用方向：构图控制·景别组织｜查阅SDXL距离滑块如何受衣装、动作和景别文字约束。**

**设计思路：景别留白·内容约束｜放宽镜头外细节要求，区分接近动作和接近人脸。**

- 原作者与原文：DetroitWobbly；SDXL及Juggernaut XL作者；[v1.0／3483049](https://civitai.com/models/3060559?modelVersionId=3483049)。
- 原作者与原文：DetroitWobbly，Near / Far — Subject Zoom Slider，SDXL1.0资源，v1.0／3483049于北京11月22日03:11发布。作者在Juggernaut XL Ragnarok上描述72图提示约束检查，另12图观察明确极近景文字对远离方向的限制，均非本库实测。
- 作者方法：正向强度趋近、更紧取景；负向趋远、扩大上下文。适度-1到+1起步，+2／+3更强但可能身份／构图变化；-2至-3依prompt可趋远，近远并不严格对称。列值是作者条件内建议，不是任意SDXL或Anima通用范围。
- 提示组织价值：若写死必须可见鞋子／道具，模型可能改姿势来保留这些内容，而不是按预期推近；描写修表等动作时，也可能靠近双手与工具而非脸。作者建议需要自由变景别时放宽镜头外细节，向远处走时避免极近景专用措辞。
- 限制：它重新生成感知距离，不是保持同一场景、几何与人物身份的3D相机运动；同seed也可变姿态、衣装或背景。原文“每梯方向一致”仍包含平台期、突变与漂移，不能只提成功概括。
- 读取状态：资源完整描述与版本信息，API查询三条作品均meta:null；其中两条列出本滑块及另一版本ID，不能当仅一个LoRA。请求第一张原图403，未看图、核该图完整正负词或seed。保留[作品直达149779970](https://civitai.com/images/149779970)，未推断其视觉画风或收益。

<a id="n10"></a>

### RMBG3.0视频实践：生成蒙版、透明输出与发丝边缘

**适用方向：图像抠图·边缘精修｜参考RMBG3.0蒙版流程和不同素材的边缘检查。**

**设计思路：蒙版与原图分开｜先估计灰度遮罩，再合成透明输出并检查细边缘。**

- 原作者与原文：AIwood爱屋研究室；BRIA及ComfyUI作者；[原视频BV19TyizJEK9](https://www.bilibili.com/video/BV19TyizJEK9/) · [重打包固定卡](https://huggingface.co/briaai/RMBG-3.0-Comfy/blob/63880aa074782b09e7ae17184960dfd6de70ab85/README.md)。
- 原作者与原文：AIwood爱屋研究室（UID503934057），《重生之我到异世界来抠图-RMBG3.0 comfyui实测》，北京11月22日00:01:07发布，286秒。完整简介给模型与网盘工作流入口；网盘未读取，不凭“有下载链接”称已取得JSON。
- 本库抽读：SDK主媒体200取得852×480、约4.12MB视频，每20秒采样并补末秒共15帧；人工看接触表，另放大查看约90／250秒两帧。视频以灰度蒙版和原图合成透明PNG为主，示例含坐姿人物、透明薄纱／瓶体、同色产品和人物发丝；这些是素材类别，不是全套素材均已评测准确率。
- 已核约90秒示范卡片及控件：4步、CFG1、Euler／simple、denoise1，seed42；这是该流程示例，不套到所有RGB生成或背景编辑模型。视频显示文本条件要求估计matte，并展示蒙版与透明合成，未取字面完整提示／全部有效接线，不补成可复现原配方。
- 看图观察：产品与模特示范中可见从背景分离出的主体；约250秒界面显示遮罩扩展-2及发丝结果，说明边缘仍需检查。480p抽帧不能证明原生毛发／半透明像素正确，未看全部瞬间对比或逐像素检查，未用成图速度作质量依据。
- 模型条件：读取BRIA的Comfy重打包卡（11月18日建立更新，revision `63880aa074782b09e7ae17184960dfd6de70ab85`），只列RMBG3的BF16／INT8-convrot、Qwen3-VL4B文本编码器与Flux2 VAE文件位置；原始briaai/RMBG-3.0卡请求401未取。重打包卡标CC-BY-NC-4.0，不以开放下载推断无条件商用。
- 读取状态：完整简介、单P公开视频、15帧OCR与人工抽读、两帧核字、短重打包卡；zh-CN字幕返回login_required，无配置会话，不称视频没有字幕。本轮未取音轨／ASR、评论或工作流JSON；媒体、OCR和截图只留仓库外，未安装／运行模型。

## 来源覆盖与检索记录

主要入口于北京时间03:57开始，后续原文／画面按需补读；分页范围、接口成功、文字实读、图片和配置分别记录，不宣称全平台穷尽覆盖。

| 平台／吧名 | 实际入口与范围 | 已读结果 | 限制／未完成范围 |
|---|---|---|---|
| stablediffusion吧 | aiotieba4.8.2 CREATE页1／30；全站最新“工作流 提示词”“模型 LoRA”“教程 分享”各页1 | 最新普通帖22日01:04，列表向前至19日12:07，跨昨日水位；问秋月15楼、MOSS画风测试11215414870共18楼文字 | 画风帖首楼及作者多楼无文字，内容主要在图片，未取得示范／配方，未以回复好评补造画风观察。问秋月has_more=true，后页／楼中楼未读 |
| stable diffusion入口核名 | 同工具带空格名称页1／2 | 实际仍返回stable吧2018公告，不是SD教程吧 | 保留名称异常，不把它当stablediffusion无新增／工具失败或已正确重定向 |
| comfyui吧 | CREATE页1／29；读11216845051共5楼 | 最新普通帖22日00:17，向前至17日21:53，跨昨日水位；画风复刻求助仅一般建议，无完整分享配方 | 本轮该范围无精选新增，不代表全吧无内容；未读求助图片。主工具成功，未检查／启用Astron备用 |
| bilibili广泛搜索 | SDK17.4.2 pubdate：ComfyUI教程页1–4各20；生图模型、Anima生图、LoRA画风各页1／20 | ComfyUI页1为21日17:51–22日01:51，页3已到20日21:00，页4回看20日17:40–20:48，已跨21日04:00水位；模型页19日12:25–21日21:15 | Anima页10月28日–21日20:52，LoRA画风页9月13日–11月13日；页内无新命中不代表全站无新内容。大量整合包／营销不按标题作质量推荐 |
| Sena404跟踪 | UID341674866页1／30，总数88，范围10月16日–11月21日 | 新投稿绝区零爱丽丝BV1TXyazAEs1，21日15:12:51，11秒；已读完整简介为“-” | 新角色作品不等于新画师串；系列仍第30期／片内40，核[系列索引](../2026-11-09/notes/Sena404画师串与相关分享.md)与[旧日报](../2026-11-20/README.md#n10)，不重复下载历史媒体。新作品未看图／视频，不称教程已读 |
| bilibili候选与精选 | RMBG视频info／subtitle／精选媒体；另读AIXUT Krea2堆栈BV1e9Wk6zExi、灰色星光Anima工具BV1hKyezGEd4完整简介 | RMBG286秒、4.12MB主地址200，15帧OCR＋接触表和2帧核字；具体范围见N10 | AIXUT738秒、简介仅标题，未取得章节／字幕范围，不盲目下全量。Anima工具自用／群内下载，未当已开源工具；无会话字幕login_required，不登录／提Cookie，本轮无ASR或评论 |
| Reddit | 两社区new.json各50／30；中英文model、finetune、LoRA、workflow、prompt、tutorial、控制等域名与日期搜索 | 最新列表均403；打开dflow作者帖及近期动漫选型讨论，主帖／少量可见回复可读，追作者模型卡 | 检索仍有旧帖／视频内容，逐条核日期。选型讨论意见分歧大，未归纳“唯一最强”；搜索摘录与原页可见回复不当完整评论区读取 |
| Hugging Face | text-to-image最新80、image-to-image最新30；Anima／IL／NoobAI各最新15；按线索读卡 | dflow、AlphaAnything、MOSS i2i固定卡与部分小JSON／图片；RMBG重打包卡、GLM架构段；另读G-star当前卡 | G-star旧仓与近期文件、Pro与Flash不同，不借Flash测速给Pro；未读论文／新旧权重差异，不计当天新训练。IL／Noob列表较旧，Anima含animal误匹配，不把检索条数当全部有效模型；未下载权重 |
| GitHub | comfyui workflow pushed>=2026-11-21最新25；comfyui prompt created>=2026-11-20最新15 | 固定commit读AlphaAnything、Manga Preset、Canvas；另读3D Texturing文档与G-STAR相关段，按来源和版本去重 | 3D贴图工程含Windows／NVIDIA、模型许可和会话限制，未取JSON，不按安装器标题写跨平台成功；未部署、编译、跑作者测试或新建服务 |
| Civitai文章／讨论 | Newest文章30；具体39357、39340、39402 | 训练比较、GLM教程与Canvas正文可读；CAME比较图403，配置zip与所请求GLM训练脚本附件400 | 没有把附件元数据当内容实读，也未改签名／反复下载；GLM生成脚本未请求。预告Totev FP8不计正式模型发布，未读全站评论 |
| Civitai模型／工作流／作品 | Newest模型40、Workflows15；具体3060559、3060621、3059489；NearFar作品API3条 | NearFar资源／版本全文与作品元数据可读，meta均null；Midjourney anime只一行说明；Sampler Compare正文可读 | NearFar第一原图403，作品多版本ID，未补造配方；短模型说明不足以判断训练／风格。采样比较按同prompt／seed扫组合、首轮加载计时另看，缺JSON／对照未单列最优参数；未称完整覆盖带配方作品 |
| 其他作者资料 | WenQiuYue公开Space元数据／README指定段 | revision和更新时刻可读，作为贴吧同源补充合并N07 | 未打开Agent运行界面或调用工具、LLM／生图API；公开README不代表效果／许可已验证 |
| Comfy论坛 | latest.json | 200，实际返回仍含旧主题 | 不据下线公告推断入口已失效；未进入Discord／批量搬运论坛 |
| note.com补充 | ComfyUI最新搜索15 | 403未取正文 | 访问受限，与无命中／无优质新增分开 |

## 后续关注与更正

- **版本和例图**：dflow0.215是0.21权重上的布局转换更新，海报示范明确0.2；MOSS v5颜色框与v4 OCR-caption路径分开，横幅未标逐图版本，不把旧图当新版提升证明。
- **坐标与输入**：dflow原生0–1000、MOSS中心像素及问秋月前端左上原点草稿是不同层，按对应转换器和编译结果理解，不能只拷bbox数值。
- **两个画板**：Canvas2.0是g1ts原项目更新；问秋月是另一套Agent工作台。局部编辑约束、静态页面可访问和实际生成连接分别记录，本轮均未启动／操作生成。
- **训练经验**：CAME文章的等时间不是等步数／曝光量，768和1024两系列不混用；GLM墨线结论只有作者单prompt／seed，附件未取，不升级为通用配方或必然收益。
- **跟踪与缺口**：Sena系列仍投稿30／片内40，新角色作品只读元数据／简介；Civitai原图403／附件400、RMBG原始卡401、Reddit列表403和字幕无会话按实际范围保留。缺件不阻塞已读内容归档，恢复访问后按信息增量补充，不重复计数。
- 本轮没有训练／生图实验待办。已有原文条件、读取冻结版本与许可继续保留；未来实际执行另沿用明确授权与停止点，不把本库资料归档当作已实现或验证。
