# 2026-11-21 每日社区发现

感谢社区模型、工具、教程及素材作者的公开分享。本页是中文概述与原文导读，欢迎回作者原帖阅读完整方法、示范和更新并支持原作者；署名和链接不等于转载授权，第三方成果不作为本库原创。

- 北京日期：2026-11-21。03:59起读取最新仓库规范，04:00起逐平台检查，发现及补读至约04:07；13:35继续整理归档并重新核对最新仓库内容与SHA。中断时段未检索，不把保存时间当平台覆盖截止时间。
- 检索类型：无具体差距要求的每日广泛发现；本轮没有主动目标专题。
- 时间窗：接续[11月20日日报](../2026-11-20/README.md)约03:57起的成功读取水位，优先新增／实质变化；近期首次补录保留原始发布日期，同源版本合并。
- 执行状态：精选10项，包含MOSS蒸馏更新、HomeIMG续训、Anima风格分支、提示与参考组织、工作流、训练选材和图像编辑经验；部分列表、图片、附件和字幕受限，具体范围如下。
- 标注归属：适用方向、美术风格／设计思路为本库整理；作者描述、社区反馈、本库看图和运行验证分开。技术资料无须美术概括时留“—”。
- 执行边界：仅研究与汇总；复用现有SDK、FFmpeg、Tesseract和缓存，未安装节点、下载生图模型、启动训练／生图／自动实验、增加服务、测试体系或派发子代理。阅读及归档不等于生成器实现、收益验证或用户认可。

## 今日值得阅读

- **模型与后训练**：[MOSS四步30K](https://huggingface.co/lvladikov/MOSS-SFT-Distill-4step-LoRA)更新了同名文件和加载补偿，[HomeIMG](https://huggingface.co/cpral/HomeIMG-1.2B-PL-EN-epoch49.2-DanceOPD5000)推进到累计5000次蒸馏更新；[AniFrame](https://civitai.com/models/3048873?modelVersionId=3481576)另开Dreamy分支，分别记录条件。
- **提示与参考组织**：[同一编码器扩写／编码](https://github.com/Magirad/ComfyUI-SingleEncoderEnhancer)、[按Skill规则分配多图职责](https://github.com/chengbeyond/ComfyUI-Qwen-Skill-Prompt)、[按JSON分类风格片段](https://github.com/Sky-Wright/ComfyUI-Style-Matrix)，各有不同输入与输出边界。
- **社区经验**：[角色选材](https://civitai.com/articles/39168)避免固定妆容／光线缠入身份；[贴吧](https://tieba.baidu.com/p/11213080261)保留画风分辨率与一致性的分歧；[街景重绘视频](https://www.bilibili.com/video/BV1mdsh6aE5C/)抽读强度、锁seed和蒙版的分工。

## 分享速查

| 类别 | 分享／资源与版本 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点／可学习经验 | 读取状态 |
|---|---|---|---|---|---|---|
| SFT蒸馏更新 | [MOSS四步30K：同名文件换检查点，补偿与负向实验另记](#n01) | 采样加速·版本选型｜核对SFT四步更新、加载补偿和实验负向的条件。 | 设计思路：色调与纹理分评｜分别观察暗部、重边和细纹，不以训练量直接判优。 | lvladikov／Reddit u/TimeTruth2490；OpenMOSS及相关作者；[30K固定模型卡](https://huggingface.co/lvladikov/MOSS-SFT-Distill-4step-LoRA/blob/8d211b763fa020facf0f4aa32d6effca965bf37d/README.md) · [作者更新帖](https://www.reddit.com/r/StableDiffusion/comments/1y147ho/mossimage_sft_update_checkpoint_30k_final_4step/) | chk00030000；同一LoRA两种加载文件；CFG2是训练范围外实验 | 主卡全文、详细卡相关段、检查点说明、1张对照；未运行 |
| 小模型续训 | [HomeIMG DanceOPD5000：双语小模型继续蒸馏与混合分辨率](#n02) | 后训练研究·双语模型｜跟踪小模型续训阶段、采样配置和语言条件。 | — | cpral／adamo1139；Poziomka、BFL与数据作者；[固定英文模型卡](https://huggingface.co/cpral/HomeIMG-1.2B-PL-EN-epoch49.2-DanceOPD5000/blob/f254c4cf7745c857441ff15349d31e134d66239f/README_en.md) | 2048→3652→5000累计蒸馏更新；不是5000步推理或FLUX文件改名 | 英波两卡、元数据、1张8格示范预览；未比较旧版同图 |
| Anima风格LoRA | [AniFrame Dreamy：摄影日常感与梦幻分支分版本阅读](#n03) | 人物插画·画风LoRA｜查阅Anima日常镜头感及独立梦幻分支的定位。 | 美术风格方向：日常摄影·朦胧梦幻｜按作者描述，以生活镜头感和柔和光线组织动漫画面。 | table_oH；致谢Zoropaton与Anima作者；[v1-Dreamy／3481576](https://civitai.com/models/3048873?modelVersionId=3481576) · [主支v1.1／3474823](https://civitai.com/models/3048873?modelVersionId=3474823) | Dreamy独立更新；@anifr与推荐参数来自资源总说明 | 资源全文、三个版本与作品元数据；例图403未观察 |
| 提示与编码节点 | [Single Encoder Enhancer：同一编码器扩写并编码参考图指令](#n04) | 提示词组织·多图编辑｜阅读Qwen2.1编码器扩写、编码与图像条件的分工。 | 设计思路：参考职责·保留项｜结构化说明各图作用及允许编辑与需要保留的内容。 | Magirad；ComfyUI、Qwen及相关作者；[固定README](https://github.com/Magirad/ComfyUI-SingleEncoderEnhancer/blob/c56d298ab4628d5741763c56669963cc7ddb74dc/README.md) | prose／JSON模式不同；接图不接VAE只指导扩写 | README全文；未核源码、兼容实现或性能 |
| 多参考提示工具 | [Qwen Skill Prompt：用文字规则分配身份、服装与姿势参考](#n05) | 提示词组织·参考分工｜用本地写作规则和有序参考图组织自然语言提示。 | 设计思路：按图取信息｜分别说明身份、衣装与姿势职责，减少参考信息混写。 | chengbeyond；llama.cpp、ComfyUI与Qwen作者；[固定README](https://github.com/chengbeyond/ComfyUI-Qwen-Skill-Prompt/blob/d1cd53edd59813c8844667d5498de36d8bd37478/README.md) | 最多10图；只输出提示文字，不等于图像条件或生图完成 | README功能、节点、运行和限制段；未读源码／执行 |
| 风格片段管理 | [Style Matrix：分类保存可编辑的正负提示片段](#n06) | 提示词组织·风格管理｜将正负提示按JSON分类保存，便于查找与再编辑。 | 设计思路：风格片段复用｜将命名、分类和文字编辑集中，具体模型配方另行保存。 | Sky-Wright；ComfyUI与相关作者；[固定README](https://github.com/Sky-Wright/ComfyUI-Style-Matrix/blob/06c14239a1ea3ab472616f57f57ad968b8afb2c2/README.md) | 输出三路STRING；可管理文字，不自动加载风格LoRA | README全文；未读代码／操作界面 |
| MOSS工作流 | [Mikoshii MOSS v1.0：模型混合、反推与放大按开关组织](#n07) | 工作流选型·图像精修｜查阅MOSS日用流程中的混合、反推和放大模块。 | — | Mikoshii；lonecatone23、MOSS与相关节点作者；[v1.0／3481536](https://civitai.com/models/3059544?modelVersionId=3481536) | MOSS专用；轻量标题不等于少显存；工作流附件403 | 资源全文、版本和附件元数据；未取得JSON |
| 角色训练经验 | [角色LoRA数据选择：身份与固定妆容、光线分开](#n08) | 人物一致性·训练素材｜阅读角色数据中妆容、光线和视角重复的取舍。 | — | archiprompts／ARCHIPROMPT及示范素材作者；[原文章39168](https://civitai.com/articles/39168) | 从作者失败经验学习数据重复；付费工具不是文章方法的必要条件 | 文章正文全文及日期；未看配图／训练配置 |
| 贴吧画风训练讨论 | [画风训练分辨率：微观笔触与素材一致性一起看](#n09) | 画风训练·素材处理｜阅读分辨率、裁切与素材一致性的社区分歧。 | 设计思路：保留笔触信息｜围绕线条、渐变和纹理讨论采样尺寸与裁切取舍。 | colourfulbird；肉鸡魔人、貓師傅及参与讨论吧友；[原讨论11213080261](https://tieba.baidu.com/p/11213080261) | 首楼偏向高分辨率；回复强调一致性、模型与有意识裁切 | 首楼与11条可见回复文字；未看对照图／楼中楼 |
| B站图生图教程 | [托曼A街景雨夜：重绘强度、锁种子与局部蒙版](#n10) | 图像编辑·局部重绘｜用街景示范理解重绘强度、种子和蒙版的分工。 | 设计思路：场景保留·限定改动｜先比原图线索，再限定允许改动区域并合回。 | 托曼A；街景原作者Bernard Spragg. NZ；SDEdit论文作者；[原视频BV1mdsh6aE5C](https://www.bilibili.com/video/BV1mdsh6aE5C/) | 同图同提示同seed比较强度；低强度／蒙版不等于必然局部成功 | 完整简介、424秒480p媒体、15帧OCR与人工抽读；无字幕／ASR |

## 当日分享

<a id="n01"></a>

### MOSS四步30K：同名文件换检查点，补偿与负向实验另记

**适用方向：采样加速·版本选型｜核对SFT四步更新、加载补偿和实验负向的条件。**

**设计思路：色调与纹理分评｜分别观察暗部、重边和细纹，不以训练量直接判优。**

- 原作者与原文：lvladikov／Reddit u/TimeTruth2490；OpenMOSS及相关作者；[30K固定模型卡](https://huggingface.co/lvladikov/MOSS-SFT-Distill-4step-LoRA/blob/8d211b763fa020facf0f4aa32d6effca965bf37d/README.md) · [作者更新帖](https://www.reddit.com/r/StableDiffusion/comments/1y147ho/mossimage_sft_update_checkpoint_30k_final_4step/)。
- 原作者分享：lvladikov把MOSS-Image SFT四步eDMD＋LADD蒸馏推进到`chk00030000`，文件名沿用旧版。接续[11月20日15K记录](../2026-11-20/README.md#n01)，不把同名文件当未更新，也不覆盖旧版本条件。当前固定revision `8d211b763fa020facf0f4aa32d6effca965bf37d`，北京11月21日00:06更新；卡片写检查点产于11月20日，30K口径是累计训练样本。
- 两种文件仍是同一适配器：作者说down/up张量相同，plain用于精确旁路加载，`_comfyui`用于标准LoRA加载器，强度均为1。30K的ComfyUI alpha因子由旧1.18改为1.12（精确alpha71.68／rank64），不是再把加载器强度乘1.12。其校准针对BF16 SFT，不外推到Base、INT8或其他加载器。
- 作者公布的整文件SHA-256：plain为`51fb026b562e127542857fb9c7ec561e35c7e1d41a971b8abc0a17e79da5c60e`；ComfyUI为`b5b998f65b181169bd2fe6d0ee384a42bebffc1f2aa760b08323aea44497ad11`。来源为同revision的[检查点说明](https://huggingface.co/lvladikov/MOSS-SFT-Distill-4step-LoRA/blob/8d211b763fa020facf0f4aa32d6effca965bf37d/moss_sft_4step_rank_64_lora_checkpoint_info.md)，未下载权重自行计算；HF revision与文件SHA-256分开保存。
- 训练点仍为Euler、ManualSigmas `1.0, 0.91, 0.717, 0.024, 0.0`、4步、CFG1／BasicGuider；不以simple四步替代。CFG1路径不使用负向。新增CFG2负向图属于训练条件外实验，作者描述可影响未锁定的颜色，不保证移除核心对象，CFG4容易过饱和；每步两次模型调用，四步变8次调用，不能套用CFG1的测速。
- 作者报告暗场色调、重边更接近教师，文字题仍14／15；这些是其有限题组指标，不构成所有题材均优于15K的结论。15K仍在archive，可回原文看两版取舍。主卡还明确默认文生图尺寸2848×1600高于训练最大1824×1024／1024×1824，卡片示范用BF16编码器，配套JSON默认用w4a8编码器。
- 本库看图：只看当前revision的[portrait_compare三栏](https://huggingface.co/lvladikov/MOSS-SFT-Distill-4step-LoRA/blob/8d211b763fa020facf0f4aa32d6effca965bf37d/assets/portrait_compare.jpg)缩放预览，右栏有明显雀斑、卷发边缘与窗侧光，中栏肤面更平滑；三栏脸部和构图有变化。未做15K与30K同图新对照，不将这张教师／两适配器对照当版本胜负证明。
- 读取状态：Reddit主帖、HF主卡全文；详细卡只读加载、精度、测速、强度及CFG实验相关段，另读检查点说明，未逐项读十套JSON、训练日志或全例图。Reddit原页显示相对时间，搜索索引标11月20日，未独立核精确发布时间。Apache-2.0社区适配器，非OpenMOSS官方产品；未下载模型／复跑。

<a id="n02"></a>

### HomeIMG DanceOPD5000：双语小模型继续蒸馏与混合分辨率

**适用方向：后训练研究·双语模型｜跟踪小模型续训阶段、采样配置和语言条件。**

- 原作者与原文：cpral／adamo1139；Poziomka、BFL与数据作者；[固定英文模型卡](https://huggingface.co/cpral/HomeIMG-1.2B-PL-EN-epoch49.2-DanceOPD5000/blob/f254c4cf7745c857441ff15349d31e134d66239f/README_en.md)。
- 原作者分享：cpral继续训练波兰语／英语HomeIMG，1.24B DiT去噪器另配72.1M可训练文本refiner及冻结Poziomka编码器。新仓北京11月21日01:23建立、01:33更新，revision `f254c4cf7745c857441ff15349d31e134d66239f`；接续[11月18日epoch49.2／DanceOPD2048](../2026-11-18/README.md#n02)。
- 阶段关系：本次从DanceOPD3652再续1348次更新；原2048加后段2952，合计5000。导出局部计数2952的EMA权重。3652只作为作者说明的中间阶段，不补称本库此前已报道。
- 方法变化：最初2048只训练1024尺寸、均匀轨迹取样；后2952按Beta(1,2)抽20步Euler轨迹，偏向高噪声前半段。教师是W8A8的FLUX.2 klein base 4B、CFG5，提供目标速度；这不等于发布的HomeIMG就是FLUX.2权重／LoRA，也不把教师CFG当学生推荐值。
- 新阶段恢复256／512／1024混合分辨率，batch取样权重1／1／8，对应time shift1.5／3／6；作者意图恢复低分辨率摄影表现。公开1024用法仍是50步、CFG3、shift6，不因名含distillation改写成四步模型。训练表中的global batch不是日常生图batch建议。
- 本库看图：固定revision的英文8格示范缩放预览含雪林狐狸、霓虹城市、草莓静物、水彩灯塔、读书机器人、宇航员骑马、OPEN灯牌与放风筝场景，展示用途多样；没有看Test22原生局部或同seed旧版并排，不判断普遍提升。卡片作者另指出滑雪题未实现第一人称、部分题种子间构图变化有限，属于作者观察。
- 读取状态：英波两份主卡全文、API日期和revision、英文8格预览；未读训练源码、日志或运行自定义pipeline。去噪器／refiner／代码Apache-2.0，捆绑Poziomka为openmdw-1.1，组件条件各自保留。

<a id="n03"></a>

### AniFrame Dreamy：摄影日常感与梦幻分支分版本阅读

**适用方向：人物插画·画风LoRA｜查阅Anima日常镜头感及独立梦幻分支的定位。**

**美术风格方向：日常摄影·朦胧梦幻｜按作者描述，以生活镜头感和柔和光线组织动漫画面。**

- 原作者与原文：table_oH；致谢Zoropaton与Anima作者；[v1-Dreamy／3481576](https://civitai.com/models/3048873?modelVersionId=3481576) · [主支v1.1／3474823](https://civitai.com/models/3048873?modelVersionId=3474823)。
- 原作者分享：table_oH的AniFrame面向照片质感的动漫日常随拍、抓拍和生活镜头感。`v1-Dreamy`／3481576于北京11月21日03:50发布，文件`ANIFR_Dreamy.safetensors`；作者明确它比主支更柔软、朦胧、偏梦核，会独立更新。主支v1.1／3474823发布于11月16日17:45，不能把主支旧图当新分支示范。
- 作者推荐：基于Anima，触发`@anifr`，LoRA0.8–1、CFG4.5、30步，`er_sde + simple`或`er_sde + beta`，用光词包括`photo_background`、`cinematic lighting`、`dramatic lighting`、`soft daylight`。这些来自资源总说明，不是本轮取得的某张Dreamy作品完整设置；精确基座权重／seed／逐图负词未知。
- 本库概述：适合查阅如何用镜头感、光线和日常场景组织动漫风格；Dreamy与主支的区别按作者文字归纳，未把模型名当人体、五官或笔触特征依据。
- 证据与缺口：资源描述和版本表可读；Dreamy三张、主支两张作品API元数据可取，但`meta:null`，不能补造配方。抽取其中各两张公开原图均403，未实际看图，未给体型／脸型的视觉归纳。[Dreamy作品149674490](https://civitai.com/images/149674490)保留直达入口，供回原作查看。
- 条件：API资源级商业权限仅列RentCivit，衍生与换许可条件分列；不把它改称MIT／Apache或默认无条件商用。未下载／运行／证明与某个Anima衍生checkpoint完全兼容。

<a id="n04"></a>

### Single Encoder Enhancer：同一编码器扩写并编码参考图指令

**适用方向：提示词组织·多图编辑｜阅读Qwen2.1编码器扩写、编码与图像条件的分工。**

**设计思路：参考职责·保留项｜结构化说明各图作用及允许编辑与需要保留的内容。**

- 原作者与原文：Magirad；ComfyUI、Qwen及相关作者；[固定README](https://github.com/Magirad/ComfyUI-SingleEncoderEnhancer/blob/c56d298ab4628d5741763c56669963cc7ddb74dc/README.md)。
- 原作者分享：Magirad将“文字扩写”和“条件编码”交给同一可生成文字的CLIP，设计起点是Qwen-Image-2.1的Qwen3-VL编码器。仓北京11月20日11:27建立，固定commit `c56d298ab4628d5741763c56669963cc7ddb74dc`于15:38提交；作者要求ComfyUI≥0.45，测试版本0.45.3，无额外Python包。
- 方法：normal原样编码；enhance先扩写成自然语言再编码；json直接编码结构化JSON。编辑字段区分edit_instruction、reference_roles、target_description、preserve；文生图另有主体、背景、构图、光线、风格、文字。不是所有模型都应统一改用JSON，也不以长词数证明画面更好。
- 参考图条件：静态图最多16个输入口，batch还可展开；`<image1>`等按图指定职责。接VAE才加入参考latent；不接VAE时图片只指导扩写，不直接形成该图像编辑条件。图片多会增加视觉tokens与内存压力，不把16口当低显存保证。
- 兼容边界：若编码器不能生成文字则回退normal，可用refiner CLIP负责写作、主CLIP仍负责编码。作者指出Qwen3-VL／Gemma的GGUF CLIP可能缺视觉投影；不因文件能载入就宣称看到了图片。bf16 fast encode会改变conditioning，作者所谓缓存／减少视觉重复计算和耗时均未由本库测量。
- 可读输出：prepared_prompt是编码的文字，raw_output还可能含未编码的思考；两者不可混作最终提示。负向关闭时输出零条件只在CFG1有同结果条件，未外推其他CFG。
- 读取状态：固定README全文，含模式、输入、输出、缓存、限制和作者测试说明；未执行该测试、审源码、安装节点或成图。GPL-3.0；本库只提供中文导读和原文链接。

<a id="n05"></a>

### Qwen Skill Prompt：用文字规则分配身份、服装与姿势参考

**适用方向：提示词组织·参考分工｜用本地写作规则和有序参考图组织自然语言提示。**

**设计思路：按图取信息｜分别说明身份、衣装与姿势职责，减少参考信息混写。**

- 原作者与原文：chengbeyond；llama.cpp、ComfyUI与Qwen作者；[固定README](https://github.com/chengbeyond/ComfyUI-Qwen-Skill-Prompt/blob/d1cd53edd59813c8844667d5498de36d8bd37478/README.md)。
- 原作者分享：chengbeyond的三节点链路选择本地GGUF模型、选择SKILL.md写作规则、按最多10张有序参考图生成提示字符串。仓北京11月20日20:15建立，固定commit `d1cd53edd59813c8844667d5498de36d8bd37478`于20:20提交，尚无正式版本；作者在ComfyUI0.45.4开发验证。
- 可学习的方法是逐图限定信息：人物图取身份、服装图取剪裁面料、姿势图取动作朝向，再明确各维度保留／排除项。reference_roles第N行对应第N张展开图片，批次合计超过10张报错；不把多图接入当身份／衣装／姿势自动无干扰分离的效果证明。
- Skill在这里是文字写作规范，auto先路由选择一份、固定选择则直接读；references默认不加入，启用后可能挤占上下文。其功能不是执行Skill脚本或检索外网；输出仍是STRING，还需下游编码与具体模型支持，不能当已经加入参考latent。
- 作者运行约定：准备时卸载ComfyUI缓存模型，临时启动私有llama-server，生成结束即释放；后续图像模型须重新加载，连续请求会重复付出加载时间。本库只阅读，不启动此进程或新增服务。
- 条件：图片需要与主GGUF配套的mmproj；默认最长边768、上下文16384，图多或references长需另核容量。自动运行时安装器仅Windows x64，其他系统须自行提供兼容llama-server；任意.gguf后缀不证明架构／量化／聊天模板兼容。
- 读取状态：固定README的功能、环境、节点、多图、Skill、运行及限制段；未审实现或导入示例。README列作者的测试结果不记作本库通过。MIT代码，模型与运行时各依自身许可；没有复制其Skill内容或第三方参考图。

<a id="n06"></a>

### Style Matrix：分类保存可编辑的正负提示片段

**适用方向：提示词组织·风格管理｜将正负提示按JSON分类保存，便于查找与再编辑。**

**设计思路：风格片段复用｜将命名、分类和文字编辑集中，具体模型配方另行保存。**

- 原作者与原文：Sky-Wright；ComfyUI与相关作者；[固定README](https://github.com/Sky-Wright/ComfyUI-Style-Matrix/blob/06c14239a1ea3ab472616f57f57ad968b8afb2c2/README.md)。
- 原作者分享：Sky-Wright提供节点内浏览、分类、编辑和保存风格JSON的方法；仓北京11月20日13:50建立，固定commit `06c14239a1ea3ab472616f57f57ad968b8afb2c2`于14:01提交。
- 作者方法：子目录成为分类，按名称或时间排序；选中后把正向与负向载入可编辑框，可另存或删除。配置路径、extra_model_paths.yaml及模型styles目录是文档列出的发现位置，真实环境路径需另核。
- 输出positive_text、negative_text、style_name_text三路字符串，接到转为输入口的文本编码节点。它组织风格文字，不包含自动匹配底模、加载LoRA或复原某图完整参数的能力；JSON风格条目仍应注明来源及适用模型。
- 本库概述：适合已有较多光线／媒介／上色片段的人查找和迭代。正负词跨模型搬运仍需具体条件，不能因字符串能接任何CLIP节点就认定各种模型画风一致。
- 读取状态：固定README全文；未看运行界面、读保存实现或进行使用验证。MIT代码，本次未复制作者样式库或安装。

<a id="n07"></a>

### Mikoshii MOSS v1.0：模型混合、反推与放大按开关组织

**适用方向：工作流选型·图像精修｜查阅MOSS日用流程中的混合、反推和放大模块。**

- 原作者与原文：Mikoshii；lonecatone23、MOSS与相关节点作者；[v1.0／3481536](https://civitai.com/models/3059544?modelVersionId=3481536)。
- 原作者分享：Mikoshii将MOSS文生图／图生图、两模型实时混合及另存、LC Vision图片反推、LoRA、SeedVR2放大与对照查看放在一个可开关工作流。v1.0／3481536于北京11月21日02:57发布，附件约85.7KiB，首次收录。
- 任务分工：手写或图片反推提示、单模型或两模型混合、是否图生图／放大分别选择；文档说无需每次重接线，并在图内提供英中日下载指南。本库未取得图内指南和有效分支，不把资源介绍当JSON实读。
- 适用范围：仅MOSS-Image及其衍生，作者明确不直接用于SDXL／Flux／Krea／Z-Image。两份BF16模型更适合其混合路径；文档称ComfyUI0.46.x下压缩fp8／int8只能放Model1，Model2不可放压缩模型。本条保留作者版本条件，未核核心实现。
- 参数归属：说明中turbo预设8步、CFG1；未明确该预设的精确LoRA文件，不套用到N01的专用四步LoRA。资源写最低ComfyUI0.42.0，同时另述0.46.x压缩模型条件，不能把最低版本当所有功能均已测的版本。
- 硬件取舍：作者用4090／24GB，LC Vision和SeedVR2可能占用较多显存，建议低显存降低像素面积或关闭放大。标题“Ultra Lightweight”不证明所有配置轻量，也不把1MP建议当任意显卡可运行保证。
- 读取状态：资源完整描述、版本／依赖与附件元数据；请求该附件403，未取JSON、例图或同图参数。未绕过、重试其他下载工具或运行工作流；原许可／使用条件以版本页为准。

<a id="n08"></a>

### 角色LoRA数据选择：身份与固定妆容、光线分开

**适用方向：人物一致性·训练素材｜阅读角色数据中妆容、光线和视角重复的取舍。**

- 原作者与原文：archiprompts／ARCHIPROMPT及示范素材作者；[原文章39168](https://civitai.com/articles/39168)。
- 原作者与原文：archiprompts，Pretty Images Don't Train Consistent Characters.，北京11月20日05:47发布／更新。文章分享自己用约40张精致渲染训练后，固定浓妆与强侧光随身份一起出现、换场景时脸部漂移的经历。
- 作者方法：核心集先用较中性的妆容、柔光和清楚可见的面部；有意变化景别、正侧面、表情、衣装和位置，避免只收同一好看角度。重点是控制与身份无关的重复条件，而不是要求整份数据完全同质。
- 可学习性：训练素材的“好看”与是否提供可分离的身份信息是两回事。本文是个人经验，未给精确基座、训练器、caption、rank和同条件对照；“多少项没达标就一定漂移”不作为本库阈值，也不把柔光解释成所有画风训练唯一正确光线。
- 商业披露：后半介绍作者自制Persona付费规划工具及48镜头清单，属于作者产品推广；阅读前半经验不需要购买，本库未访问或验证付费产品。未转载其完整计划、配图或销售文案。
- 读取状态：Civitai API返回的正文全文与发布时间，图片未看，评论未读；未训练／复跑验证。此条收录的是选材经验，非经过本库测试的训练配方。

<a id="n09"></a>

### 画风训练分辨率：微观笔触与素材一致性一起看

**适用方向：画风训练·素材处理｜阅读分辨率、裁切与素材一致性的社区分歧。**

**设计思路：保留笔触信息｜围绕线条、渐变和纹理讨论采样尺寸与裁切取舍。**

- 原作者与原文：colourfulbird；肉鸡魔人、貓師傅及参与讨论吧友；[原讨论11213080261](https://tieba.baidu.com/p/11213080261)。
- 原作者与原文：colourfulbird，stablediffusion吧《训练画风像不像很大程度取决于训练时的分辨率》，北京11月20日12:17:41首发。用aiotieba4.8.2核到真实吧名、首楼时间和首楼正文，读到12条可见楼层。
- 楼主经验：以同一画面区域在6K、1536、1024下的笔触和颜色过渡损失为线索，认为自己的画风训练更适合1536；人物／姿势轮廓与细笔触的信息需求不同。这里的6K／1536是原图或训练尺寸讨论，不是N01的训练样本计数，也不是N02累计训练更新。
- 社区分歧：肉鸡魔人认为素材时期／画法一致性更关键，并称Krea2的512训练也可用；貓師傅主张按任务有意识裁切细节。另有Anima裁切与分桶的具体提问，但本轮未取得楼主对该问题的明确可执行答复。
- 本库概述：值得学习的是先确认原图有多少真实笔触、裁切保留什么信息，再讨论训练尺寸；不能将楼主“1024是斩杀线”等个人强断言写成所有模型定律，也不能把超分补图宣称为恢复原作者丢失的笔触。素材使用仍须依原作许可。
- 读取状态：首楼和11条回复文本，共12条，页内has_more=false不代表楼中楼／图片已读。示范图、精确底模、训练配置、数据集与可复核日志未取得；未视觉比较或训练验证。

<a id="n10"></a>

### 托曼A街景雨夜：重绘强度、锁种子与局部蒙版

**适用方向：图像编辑·局部重绘｜用街景示范理解重绘强度、种子和蒙版的分工。**

**设计思路：场景保留·限定改动｜先比原图线索，再限定允许改动区域并合回。**

- 原作者与原文：托曼A；街景原作者Bernard Spragg. NZ；SDEdit论文作者；[原视频BV1mdsh6aE5C](https://www.bilibili.com/video/BV1mdsh6aE5C/)。
- 原作者与原文：托曼A（UID691410286），《只想把照片改成雨夜，AI 怎么连房子都重画了？》，北京11月19日18:08:56发布，424秒。是本轮发现的近期首次补录，标真实日期，不称11月21日新发布。
- 作者分享：以同一香港街景、同一句提示和同种子，比较不同重绘强度，并在第一步观察原图线索剩余；最后针对巴士蒙版重绘与合回。原街景署名Bernard Spragg. NZ，简介写CC0 1.0，并提SDEdit论文；原素材许可仍请回作者说明核查。
- 本库看图：SDK取得单P公开视频，852×480、约7.55MB；每30秒抽样并补末秒共15帧，已看整张接触表并核读文字。约45秒的四格比较标0.27／0.55／0.89：低强度保留更多车和店铺轮廓，中间雨夜效果更强同时改动车辆，高强度明显另造街道。此为作者这组示范，未据三张图概括所有模型阈值。
- 方法说明：约135–225秒卡片解释编码／加噪／按提示去噪及强度所管的起始噪声；约285秒强调原图、提示、seed固定后只改强度；约345秒用蒙版圈定允许修改区域、再合回原街景。约375秒还展示局部变暗／偏色的失败，不把圈蒙版等同于模型一定理解换车任务。
- 公开配置边界：画面标ComfyUI＋Stable Diffusion1.5示范，非Anima／MOSS专属结论。已核三档强度数字，但未取得精确checkpoint、字面完整正负提示、全部节点／采样器／步数等，不拼接成可复现配方。
- 读取状态：完整简介、媒体、15帧OCR与人工抽样观察；非逐帧观看。平台zh-CN字幕请求返回login_required（未配置会话），不据此称视频无字幕；本轮画面文字已足够导读，未下载音轨或生成ASR，评论未读。媒体、截图、OCR原文仅留仓库外，未转载完整教程或提交原媒体。

## 来源覆盖与检索记录

下列检查主要完成于北京时间04:00–04:07；13:35后为整理与保存。关键词、分页和返回数量只代表实际入口，不代表穷尽全平台；未检查的页面不补称覆盖。

| 平台／吧名 | 实际入口和范围 | 结果与读取 | 限制／未完成范围 |
|---|---|---|---|
| stablediffusion吧 | aiotieba4.8.2 CREATE页1／30；全站最新“工作流 提示词”27、“模型 LoRA”30、“教程 分享”21条 | 普通列表最新21日00:12，向前到18日08:09，跨上次水位；深读画风训练12楼、构图提问14楼 | 构图帖多为参考摄影／设计的建议，未给示范配方，未单独扩写成教程。所有读取仅文字，无楼中楼／图片 |
| stable diffusion入口核名 | 同工具带空格名称页1／2 | 实际返回stable吧2018公告，并非stablediffusion吧 | 不把旧帖当SD社区停更或工具失败，也不称已证实两名称正确重定向；有效SD覆盖使用上行真实吧名 |
| comfyui吧 | aiotieba CREATE页1／30 | 最新普通帖20日18:12，向前到17日07:02，跨上次水位；读SKU配件提问11213581687首楼 | 未有可执行解决分享，列为本页范围内无精选新增，不推断全吧无更新。主工具成功，未启用／检查Astron备用 |
| bilibili广泛发现 | SDK17.4.2 pubdate“ComfyUI 教程”页1–5各20；“生图模型”“Anima 生图”“LoRA 画风”各页1／20 | ComfyUI页1范围20日17:54–21日02:24，页4已跨20日03:57水位，页5回看19日17:34–20:13；模型页18日16:26–20日21:20 | 另两词页分别10月28日–11月19日、9月13日–11月13日，页内无新命中不代表全站无新增。整合包／广告不凭标题当教程推荐 |
| Sena404作者跟踪 | UID341674866最新页1／30，总数87；核仓库系列水位 | 最新仍第30期BV1DSsh6iEJv，11月19日18:27；[旧记录](../2026-11-20/README.md#n10)与[系列索引](../2026-11-09/notes/Sena404画师串与相关分享.md)已收录 | 无新期，不重下历史媒体，不重复新增；投稿30／片内40继续分别记录 |
| bilibili精选与候选 | 托曼A雨夜视频info／subtitle／必要媒体；另读BV1Aay4zGEJM完整简介 | 雨夜424秒视频主地址200，15帧OCR＋人工看图；zh-CN字幕login_required。Qwen2.1“最强4K”视频简介为空 | 空简介候选只获标题／元数据，本轮未深读，不按标题认定无偏移／最强。无会话不自动登录；本轮没有音轨、ASR和评论读取 |
| Reddit | 两社区new.json各50／30；中英文model／LoRA／workflow／prompt／tutorial等域名日期检索 | 最新列表403；打开30K作者原帖和H3多参考编辑讨论，原帖文字可读，MOSS追到作者HF固定卡 | 原帖主帖、搜索摘录与评论取得范围不同：本轮MOSS原页只取主帖，不把搜索返回的纹理偏好／INT8试用评论当完整评论区实读。H3答复提两路接图／无蒙版，未核官方模板，不作为通用结论 |
| Hugging Face | text-to-image最新80、image-to-image最新30；Anima／Illustrious／NoobAI各最新15 | 固定revision读MOSS30K、HomeIMG5000；另读Trout、Meru、Reflora卡，前两精选见上；MOSS和HomeIMG各看1张示范 | Trout公开承认训练预算差距大，本轮不因参数小或指标多就推荐成品质量；Reflora仅短卡不足以判断画风。IL／Noob仅列表检查，未凭修改日新增报告；未下载权重 |
| GitHub | comfyui workflow pushed>=2026-11-20最新25；comfyui prompt created>=2026-11-19最新15；追作者仓 | 固定commit读Style Matrix、Single Encoder Enhancer及Qwen Skill Prompt，按原链接与历史档案去重 | README功能与作者测试说明不记作本库已审实现／兼容／通过；未安装、编译、运行节点 |
| Civitai文章／讨论 | Newest文章30；具体39168、39238、39310、39321 | 正文可读；角色训练经验精选。另读彩玻璃材质短文、IL裤脚盖靴提问及生成经验导读 | 彩玻璃文偏材料史且无生成配置；裤靴帖本轮无可读答复，未拼成提示解法；经验文含产品推广，未访问付费内容。未读社区评论 |
| Civitai模型／版本／工作流／作品 | Newest模型40、Workflows15；AniFrame3048873、Mikoshii3059544具体版本；Dreamy作品3条、主支2条元数据 | 资源与版本正文可读；新Dreamy与主支分开。工作流附件元数据约85.7KiB；作品meta均null | JSON附件403；各分支抽取的2张原图均403，未看图。标有hasMeta不等于取得配方；未补造同图seed／完整提示，未称作品配方面向已完整覆盖 |
| Comfy社区论坛 | latest.json | 200，取到的列表仍含旧主题；保留入口实际可读状态 | 未据日期公告推断今天已不可读，不重复收录此前公告；未进入Discord或批量搬运 |
| note.com补充 | ComfyUI最新搜索15 | 403，未取得正文 | 访问受限，与无命中／无优质新增分开，不推断作者停更 |

## 后续关注与更正

- **版本变更**：MOSS同名文件现为30K，补偿1.12只属此版；[15K历史条件](../2026-11-20/README.md#n01)保留，不回写成原先就是30K。当前文件SHA-256为作者发布值，非本库实算；更高CFG负向试验不与训练点、测速混用。
- **模型身份**：HomeIMG5000是2048／3652后的继续蒸馏，不把5000写成推理步数；AniFrame Dreamy是独立分支，不能套主支作品、逐图参数或商业许可推断。
- **Sena水位**：仍投稿30／片内40；本轮新作者的阅读与Sena跟踪分别记录。未执行的中断时段不补称已覆盖。
- **读取缺口**：Mikoshii附件和AniFrame原图403、Reddit最新列表403、B站会话字幕未取；已读正文先保存。后续若这些资料可读，按原链接和实质信息增量更新本页，不因访问恢复自动计作新分享。
- **学习边界**：角色数据文章和画风分辨率帖子均是经验分享，保留不同模型／任务条件及分歧；街景教程只核本例抽样与公开强度，不下发本地生图或训练计划。原文许可、署名或链接需更正时保留旧条件并注明更正依据。
