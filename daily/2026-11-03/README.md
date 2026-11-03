# 2026-11-03 每日社区发现

本页汇总社区作者的公开分享，感谢原作者的投入。以下为本库概述，保留署名与原文入口，欢迎前往原帖阅读完整内容、示范和更新。

- 北京日期与开始时间：2026-11-03 03:58（UTC时钟换算）。
- 检索类型：每日广泛发现；无具体差距要求，无主动专题。
- 执行状态：本轮已归档10项（含10:40起用户指定补充S10）；部分平台接口与图片访问受限，实际范围见下表。
- 优先时间窗：自2026-11-02晨间检索快照后的新增与实质更新，必要时近期补录并单列原日期；未将后续保存时间当作检索边界。
- 已归档10项。仅读取与摘要整理，未安装节点、下载大模型、运行生图或自动实验。

## 今日值得阅读

- [Qwen-Image 2.1 Lightning v2 RL：四步生成与编辑](https://huggingface.co/lightx2v/Qwen-Image-2.1-Lightning-v2-RL)：作者在Lightning v2蒸馏基础上进行RL精炼，分享四步文生图、单参考编辑及多参考生成的权重与示例。发布形式是完整transformer，需要原Qwen2.1的处理器、编码器和VAE，并非独立整套管线。
- [Anima Character Sheet Designer：按视图独立生成角色设定表](https://github.com/ukr8b3g-cmyk/Anima-Character-Sheet-Designer)：作者提供最多13个视图独立生成、再拼成一页的Anima流程，可输入文字，或用本地PixAI／WD标签器提取外观标签。每个视图的基础提示可编辑，部位提示作为补充，最终运行文本可从view_records检查。
- [Anima系14模型比较：把任务遵循与个人审美分开](https://note.com/ai_sketch/n/n86dbfb22c5ca)：作者称以14个Anima系模型生成336张，固定提示、seed和设置，分别比较简单／困难姿态、自然语言任务与画风偏好。文章公开检查项目和失败例，并记录作者与AI对同图审美排名不同；参考价值在比较方法与审美归属，而非将推荐顺序当作客观排名。

## 分享速查

| 类别 | 分享／资源与版本 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点／可学习经验 | 读取状态 |
|---|---|---|---|---|---|---|
| 后训练／少步蒸馏 | [S01 Qwen-Image 2.1 Lightning v2 RL：四步生成与编辑](#s01) | 少步生成·参考图编辑｜了解Qwen2.1四步RL权重的三类任务用法。 | — | [LightX2V / lightx2v；基座Qwen团队](https://huggingface.co/lightx2v/Qwen-Image-2.1-Lightning-v2-RL) | 作者在Lightning v2蒸馏基础上进行RL精炼，分享四步文生图、单参考编辑及多参考生成的权重与示例。发布形式是完整transformer，需要原Qwen2.1的处理器、编码器和VAE，并非独立整套管线。 | 固定revision模型卡全文及inference_config.json；未看对比图、未读RL实现、未取得权重 |
| 后训练／蒸馏LoRA | [S02 StepX-OPD SD3.5 Medium：区分推理LoRA与训练初始化](#s02) | 少步蒸馏·LoRA加载｜分清SD3.5四步推理文件与训练初始化。 | — | [ShimaRinC（发布账户）；模型卡署名StepFun AI；基座Stability AI](https://huggingface.co/ShimaRinC/StepX-OPD-SD3.5) | 作者发布SD3.5 Medium的StepX-OPD四步权重，说明根目录推理LoRA已合并rank160初始化与rank32学生适配器，总rank192。additive_init目录供训练初始化，不是另一枚应再次叠加的四步推理模型。 | 固定revision模型卡全文；未读论文、训练代码、配置实现或示范图 |
| 后训练／高分辨率LoHa | [S03 MOSS高分辨率LoHa：4MP以上生成的实验分享](#s03) | 高分辨率·MOSS适配器｜关注面向4MP以上生成的训练实验。 | — | [comfyanonymous；基座Comfy-Org/MOSS-Image](https://huggingface.co/comfyanonymous/MOSS_image_MAX_ULTRA_hires_lora_test) | 作者分享为MOSS-Image-Base训练的LoHa，目标是改善4MP及以上生成；数据为3.5–10MP动漫与摄影混合，作者也提示动漫占比可能偏高。页面给9MP的旧版本与无LoRA对比入口，适合继续关注高分辨率适配路线。 | 固定revision模型卡全文及文件目录元数据；未看9MP示范、未下载适配器 |
| 提示词／素材组织 | [S04 CharaDB：将人物固定项与服装姿态变量分开](#s04) | 提示词组织·角色设定·姿态｜固定人物描述，按需替换服装与动作词。 | 设计思路：固定设定与变量分工｜人物外观独立成行，服装、姿态和表情按页变化。 | [takumi1112 / Taki；基座JANKU v4及NoobAI／Illustrious作者见原文](https://civitai.com/articles/37854) | 作者为批量CG创作整理可视词条与通配符，按发型、眼睛、服装、姿态浏览；强调把固定人物描述保持一致，再改变需要变化的部分。作者用同一基座、seed与基础人物制作示范卡，帮助比较词条表现，而非宣称文本能保证任意模型的角色一致性。 | Civitai公开API文章正文全文；未打开应用、未看词条示范、未下载Release或核验数量 |
| 角色设定／工作流 | [S05 Anima Character Sheet Designer：按视图独立生成角色设定表](#s05) | 角色设定·多视图·提示词组织｜以外观标签和分视图提示组装设定表。 | 设计思路：外观与视图分工｜固定外观描述，各视图另写方向、景别与部位提示。 | [ukr8b3g-cmyk；PixAI／WD及基座作者见仓库链接](https://github.com/ukr8b3g-cmyk/Anima-Character-Sheet-Designer) | 作者提供最多13个视图独立生成、再拼成一页的Anima流程，可输入文字，或用本地PixAI／WD标签器提取外观标签。每个视图的基础提示可编辑，部位提示作为补充，最终运行文本可从view_records检查。 | README全文及最近3条提交说明；未读工作流JSON、标签器实现或示范图 |
| 区域布局／提示词节点 | [S06 MOSS YXBOX：在同一画布组织人物、文字与物体框](#s06) | 多主体·文字版面·区域提示｜在画布上分配角色、物体和文字位置。 | 设计思路：版面与内容分区｜各框写对象或文字，整体描述另管全图场景。 | [liangci-ai；基于ComfyUI官方Create Bounding Boxes与MOSS-Image Layout Prompt](https://github.com/liangci-ai/MOSS-YXBOX) | 作者把两个官方节点整合成中文布局工作台，支持物体／文字／角色框、参数锁、背景参照与布局导入导出。输出区分可编辑草稿和MOSS编译布局，便于查阅坐标与内容职责；最新提交修正上游空文本清画布等问题。 | README开头约6000字符，另读PNG布局导入说明和第七节输出格式的相关段落；最近3条提交说明；未读全部README与实现 |
| 后训练／具体画风 | [S07 Sabikaze MOSS v1：灰蓝绿干笔动漫风格LoRA](#s07) | 人物插画·风格LoRA｜参考灰蓝绿基调与少量暖色点缀的场景绘制。 | 灰蓝绿·干笔动漫｜按作者描述，以重墨线、平面明暗和衣物背景干笔纹理营造安静氛围。 | [lepetitprince716355](https://civitai.com/models/3033719?modelVersionId=3446890) | 作者用同一组57张自生成素材将Sabikaze路线扩展到MOSS，介绍低饱和灰蓝／灰青主色、单一暖色点缀、重线与干笔质感。使用时明确写出媒介，再以自然句描述人物与真实环境，强调媒介句对这份适配器的作用。 | 模型介绍全文、指定版本元数据及首图的提示／参数／comfy字符串；原图HTTP403，未看任何例图 |
| 工作流／LoRA对照 | [S08 LoRA Strength Grid：零权重与空触发基线的区别](#s08) | LoRA搭配·参数对照｜参考三提示、五权重的网格组织方法。 | 设计思路：风格强度与内容保留｜留一条不请求目标风格的提示，观察作用范围。 | [mr_p_m](https://civitai.com/models/3033699?modelVersionId=3446870) | 作者分享仅使用核心节点的网格流程：三条提示分别配0、0.4、0.7、1、1.3五档强度，每行同seed，再保存整张网格。保留一条不要求LoRA所学内容的提示，用于观察它是否也影响其他题材。 | 模型介绍全文、指定版本说明与配置文件元数据；未下载／打开JSON、未看网格图 |
| 模型选型／社区实践 | [S09 Anima系14模型比较：把任务遵循与个人审美分开](#s09) | 模型选型·提示词组织｜参考同条件比较与任务检查表的写法。 | 设计思路：任务遵循与审美分评｜先检查姿态和空间要求，再按个人偏好选择画风。 | [AIスケッチ / ai_sketch](https://note.com/ai_sketch/n/n86dbfb22c5ca) | 作者称以14个Anima系模型生成336张，固定提示、seed和设置，分别比较简单／困难姿态、自然语言任务与画风偏好。文章公开检查项目和失败例，并记录作者与AI对同图审美排名不同；参考价值在比较方法与审美归属，而非将推荐顺序当作客观排名。 | note公开API文章文字全文约4261日文字符；未看图片表格、视频或附件 |

| 提示词／角色服装 | [S10 Anima Wardrobe V5：自然语言绑定与角色服装预设](#s10) | 自动提示·服装预设·多主体｜用自然语言绑定角色外观、服装与场景关系。 | 设计思路：角色与关系分工｜标签承载外观，绑定句说明谁穿什么及人物关系。 | [灵冻不冻 / lingdongbudong；上游提示词工具作者飞蓬](https://www.bilibili.com/video/BV1Af4T6cEvM/) | 作者将角色、服装和场景词库组织成可复现的本地随机提示词节点，补入自然语言关系描述及角色服装预设。版本记录说明双人时按角色分别绑定衣着／外观，并让共享随机字段让位，避免同一属性重复描述。 | 视频完整简介与元数据；仓库README全文、手册与版本历史相关段落、独立提示词JSON；未看视频／图片、未取得字幕 |

## 当日分享

<a id="s01"></a>

### S01 Qwen-Image 2.1 Lightning v2 RL：四步生成与编辑

**适用方向：** 少步生成·参考图编辑｜了解Qwen2.1四步RL权重的三类任务用法。

- 原文标题：Qwen-Image-2.1-Lightning-v2-RL。
- 原作者／平台与原文：LightX2V / lightx2v；基座Qwen团队；[原文](https://huggingface.co/lightx2v/Qwen-Image-2.1-Lightning-v2-RL)。
- 发布／更新与精确版本：2026-11-02 21:43:01 +08:00（仓库lastModified，非首发日）；revision f3551c760933f7adf45b57a7571215eca6efffd0；完整transformer权重，非LoRA。
- 收录类型与内容形式：首次收录；本库概述，非原文转载或本库实测。
- 原作者分享要点（本库概述）：作者在Lightning v2蒸馏基础上进行RL精炼，分享四步文生图、单参考编辑及多参考生成的权重与示例。发布形式是完整transformer，需要原Qwen2.1的处理器、编码器和VAE，并非独立整套管线。
- 公开资料与适用条件：模型卡示例1024²、CFG1；FP32存储的权重可按BF16加载。已读inference_config.json给出sigmas=[1.0,0.95418,0.89508,0.704534]、use_kv_cache=true、shift1、use_dynamic_shifting=false。sigmas已经移位，不能再次动态移位；配置需示例代码显式读取，仅设置num_inference_steps=4不等价。其他尺寸要求边长为32倍数。Qwen Research非商业使用条件适用，见原许可。
- 实际读取范围：固定revision模型卡全文及inference_config.json；未看对比图、未读RL实现、未取得权重。
- 本库整理备注与信息范围：模型卡中的40步基座对照是作者选取的定性示范；本库未复跑或认定四步普遍等质。原文提醒小字、解剖、计数与参考保持仍需检查；ComfyUI接入未在本库验证。
- 相关原始资料：https://huggingface.co/lightx2v/Qwen-Image-2.1-Lightning-v2-RL/blob/f3551c760933f7adf45b57a7571215eca6efffd0/README.md
- 相关原始资料：https://huggingface.co/lightx2v/Qwen-Image-2.1-Lightning-v2-RL/blob/f3551c760933f7adf45b57a7571215eca6efffd0/inference_config.json

<a id="s02"></a>

### S02 StepX-OPD SD3.5 Medium：区分推理LoRA与训练初始化

**适用方向：** 少步蒸馏·LoRA加载｜分清SD3.5四步推理文件与训练初始化。

- 原文标题：StepX-OPD (SD3.5-Medium)。
- 原作者／平台与原文：ShimaRinC（发布账户）；模型卡署名StepFun AI；基座Stability AI；[原文](https://huggingface.co/ShimaRinC/StepX-OPD-SD3.5)。
- 发布／更新与精确版本：2026-11-02 22:27:33 +08:00（仓库lastModified，非首发日）；revision 2253ec4af90a6065b63b62b1889b5c366572146e；推理pytorch_lora_weights.safetensors。
- 收录类型与内容形式：首次收录；本库概述，非原文转载或本库实测。
- 原作者分享要点（本库概述）：作者发布SD3.5 Medium的StepX-OPD四步权重，说明根目录推理LoRA已合并rank160初始化与rank32学生适配器，总rank192。additive_init目录供训练初始化，不是另一枚应再次叠加的四步推理模型。
- 公开资料与适用条件：基座stabilityai/stable-diffusion-3.5-medium；示例512²、4步、guidance_scale1、seed0，显式sigmas=np.linspace(1.0,1.0/4,4)，即[1.0,0.75,0.5,0.25]。省略该时间表会回到不同的基座默认网格。训练初始化rank160／alpha64、23目标模块的说明按模型卡记录，未读取权重。模型适用Stability AI Community许可；训练代码Apache-2.0另计。
- 实际读取范围：固定revision模型卡全文；未读论文、训练代码、配置实现或示范图。
- 本库整理备注与信息范围：本库保存的是作者文件职责与推理示例，不把rank相加推成任意LoRA都可这样融合。未测试ComfyUI兼容性、其他尺寸或四步效果。
- 相关原始资料：https://huggingface.co/ShimaRinC/StepX-OPD-SD3.5/blob/2253ec4af90a6065b63b62b1889b5c366572146e/README.md
- 相关原始资料：https://github.com/WinterCCC/StepX-OPD

<a id="s03"></a>

### S03 MOSS高分辨率LoHa：4MP以上生成的实验分享

**适用方向：** 高分辨率·MOSS适配器｜关注面向4MP以上生成的训练实验。

- 原文标题：MOSS_image_MAX_ULTRA_hires_lora_test。
- 原作者／平台与原文：comfyanonymous；基座Comfy-Org/MOSS-Image；[原文](https://huggingface.co/comfyanonymous/MOSS_image_MAX_ULTRA_hires_lora_test)。
- 发布／更新与精确版本：2026-11-03 03:28:57 +08:00（仓库lastModified，非首发日）；revision 6ec944cad2cfab4b8211d226a150c6027711bdd8；目录v0.1–v0.7，正文示范仅列v0.1–v0.3。
- 收录类型与内容形式：首次收录；本库概述，非原文转载或本库实测。
- 原作者分享要点（本库概述）：作者分享为MOSS-Image-Base训练的LoHa，目标是改善4MP及以上生成；数据为3.5–10MP动漫与摄影混合，作者也提示动漫占比可能偏高。页面给9MP的旧版本与无LoRA对比入口，适合继续关注高分辨率适配路线。
- 公开资料与适用条件：已读取目录确认存在moss_hires_lora_test_v0.1至v0.7.safetensors；当前模型卡没有给出最新v0.7的专属示范、权重强度、触发词、完整提示或采样配置，均未取得。资源名含lora，正文明确称LoHa，按作者实际类型记录。
- 实际读取范围：固定revision模型卡全文及文件目录元数据；未看9MP示范、未下载适配器。
- 本库整理备注与信息范围：目录出现v0.7不等于它的效果优于已列示范版本。作者训练目标不等于本库确认收益；混合训练题材不是具体画风总结依据。具体加载依赖及许可需回作者资料核对。
- 相关原始资料：https://huggingface.co/comfyanonymous/MOSS_image_MAX_ULTRA_hires_lora_test/blob/6ec944cad2cfab4b8211d226a150c6027711bdd8/README.md

<a id="s04"></a>

### S04 CharaDB：将人物固定项与服装姿态变量分开

**适用方向：** 提示词组织·角色设定·姿态｜固定人物描述，按需替换服装与动作词。

**设计思路：** 固定设定与变量分工｜人物外观独立成行，服装、姿态和表情按页变化。

- 原文标题：CharaDB: 1,027 free anime prompt materials (hair, outfits, poses + wildcards)。
- 原作者／平台与原文：takumi1112 / Taki；基座JANKU v4及NoobAI／Illustrious作者见原文；[原文](https://civitai.com/articles/37854)。
- 发布／更新与精确版本：2026-11-02 11:40:20.821 +08:00（文章发表）；文章37854；公开版GitHub Release v1.0，未下载资源包。
- 收录类型与内容形式：首次收录；本库概述，非原文转载或本库实测。
- 原作者分享要点（本库概述）：作者为批量CG创作整理可视词条与通配符，按发型、眼睛、服装、姿态浏览；强调把固定人物描述保持一致，再改变需要变化的部分。作者用同一基座、seed与基础人物制作示范卡，帮助比较词条表现，而非宣称文本能保证任意模型的角色一致性。
- 公开资料与适用条件：作者列公开版1027图、440服装、281姿态，并给姿态线稿入口及各类wildcard文件。模板职责依次为模型质量行、固定外观行、表情／服装／姿态变量和场景镜头。作者称标签／提示／应用可商用，图片不可转载转售，也不可放入出售作品；基座许可另适用。本库仅链接，未搬运素材。
- 实际读取范围：Civitai公开API文章正文全文；未打开应用、未看词条示范、未下载Release或核验数量。
- 本库整理备注与信息范围：同seed／同基座是作者制卡条件，不证明跨角色或跨模型稳定。Illustrious、NoobAI、Anima等预设的字面提示未取得，不能通用套用示例质量词；使用条件以原作者和基座许可为准。
- 相关原始资料：https://github.com/taki-ttt/charadb/releases/tag/v1.0
- 相关原始资料：https://charadb-2fi.pages.dev/

<a id="s05"></a>

### S05 Anima Character Sheet Designer：按视图独立生成角色设定表

**适用方向：** 角色设定·多视图·提示词组织｜以外观标签和分视图提示组装设定表。

**设计思路：** 外观与视图分工｜固定外观描述，各视图另写方向、景别与部位提示。

- 原文标题：Anima Character Sheet Designer — v1.0。
- 原作者／平台与原文：ukr8b3g-cmyk；PixAI／WD及基座作者见仓库链接；[原文](https://github.com/ukr8b3g-cmyk/Anima-Character-Sheet-Designer)。
- 发布／更新与精确版本：2026-11-03 01:25:52 +08:00（最新提交）；v1.0；提交56a8aa61095e7166bb4b6fcf700d07fdd8900dd8；README快照。
- 收录类型与内容形式：首次收录；本库概述，非原文转载或本库实测。
- 原作者分享要点（本库概述）：作者提供最多13个视图独立生成、再拼成一页的Anima流程，可输入文字，或用本地PixAI／WD标签器提取外观标签。每个视图的基础提示可编辑，部位提示作为补充，最终运行文本可从view_records检查。
- 公开资料与适用条件：模板为WAI-ANIMA v1.0 base1.0（Civitai版本2983680）与Anima Turbo LoRA v0.2（2979642）；作者模板LoRA0.7、10步、CFG1.5、Euler/simple。作者本地环境ComfyUI0.43.0／frontend1.57.4，依赖Save WEBP Meta；标签器二选一，ONNX CPU/GPU包也按实际环境选择，未自动安装。
- 实际读取范围：README全文及最近3条提交说明；未读工作流JSON、标签器实现或示范图。
- 本库整理备注与信息范围：图像输入实际是图像→标签→新文生图，不是视觉参考编辑，也没有旧Ref Adapter路径；脸、衣服、左右朝向及不可见部分可能变化。画布上的人台仅作预览，不送进Anima。页面测试数量和单次44.3秒是作者记录，不等于本库实测或稳定性证明。
- 相关原始资料：https://github.com/ukr8b3g-cmyk/Anima-Character-Sheet-Designer/commit/56a8aa61095e7166bb4b6fcf700d07fdd8900dd8
- 相关原始资料：https://github.com/ukr8b3g-cmyk/Anima-Character-Sheet-Designer/blob/56a8aa61095e7166bb4b6fcf700d07fdd8900dd8/examples/Anima-Character-Sheet-Designer-Text-or-Image.json

<a id="s06"></a>

### S06 MOSS YXBOX：在同一画布组织人物、文字与物体框

**适用方向：** 多主体·文字版面·区域提示｜在画布上分配角色、物体和文字位置。

**设计思路：** 版面与内容分区｜各框写对象或文字，整体描述另管全图场景。

- 原文标题：MOSS YXBOX 控图排版。
- 原作者／平台与原文：liangci-ai；基于ComfyUI官方Create Bounding Boxes与MOSS-Image Layout Prompt；[原文](https://github.com/liangci-ai/MOSS-YXBOX)。
- 发布／更新与精确版本：2026-11-03 03:07:41 +08:00（最新提交）；main提交d2230b5e545afeb8344dcb7fc2fe3d44b53b3f66；最近里程碑v1.0.5，后续修复按提交区分。
- 收录类型与内容形式：首次收录；本库概述，非原文转载或本库实测。
- 原作者分享要点（本库概述）：作者把两个官方节点整合成中文布局工作台，支持物体／文字／角色框、参数锁、背景参照与布局导入导出。输出区分可编辑草稿和MOSS编译布局，便于查阅坐标与内容职责；最新提交修正上游空文本清画布等问题。
- 公开资料与适用条件：需要自带MOSS-Image节点的ComfyUI。作者文档的编译布局为abs_centralized＋yxyx，以中心为原点；草稿为abs＋xyxy，以左上为原点，不能混用。背景图及隐藏框不写入items；无框时输出整体描述。前置／布局／后置文本按实际非空项组合。main可包含里程碑后的修复，不能仅按旧UI截图版本判断。
- 实际读取范围：README开头约6000字符，另读PNG布局导入说明和第七节输出格式的相关段落；最近3条提交说明；未读全部README与实现。
- 本库整理备注与信息范围：背景参照画布不等于图像作为生成器视觉条件。作者称与官方输出一致，本库未做字节比对或接入验证。导入参与分支识别是作者功能说明，未核实现；模型权重和采样设置未由这份节点文档确定。
- 相关原始资料：https://github.com/liangci-ai/MOSS-YXBOX/commit/d2230b5e545afeb8344dcb7fc2fe3d44b53b3f66

<a id="s07"></a>

### S07 Sabikaze MOSS v1：灰蓝绿干笔动漫风格LoRA

**适用方向：** 人物插画·风格LoRA｜参考灰蓝绿基调与少量暖色点缀的场景绘制。

**美术风格方向：** 灰蓝绿·干笔动漫｜按作者描述，以重墨线、平面明暗和衣物背景干笔纹理营造安静氛围。

- 原文标题：[MOSS Image] Sabikaze - grey-teal dry-brush anime style。
- 原作者／平台与原文：lepetitprince716355；[原文](https://civitai.com/models/3033719?modelVersionId=3446890)。
- 发布／更新与精确版本：2026-11-03 03:23:46.019 +08:00（版本发表）；模型3033719／版本3446890 v1；moss_sabikaze_v1.safetensors。
- 收录类型与内容形式：首次收录；本库概述，非原文转载或本库实测。
- 原作者分享要点（本库概述）：作者用同一组57张自生成素材将Sabikaze路线扩展到MOSS，介绍低饱和灰蓝／灰青主色、单一暖色点缀、重线与干笔质感。使用时明确写出媒介，再以自然句描述人物与真实环境，强调媒介句对这份适配器的作用。
- 公开资料与适用条件：作者通用测试：MOSS-SFT INT8 ConvRot、Qwen3.5-9B、25步／CFG2.5／er_sde/simple／shift5、832×1248、LoraLoaderModelOnly强度1。触发前缀@z3-sabikaze.；作者称不写触发也会作用。首图元数据另列seed2026110312、qwen3.5_9b_w4a8_gptq.safetensors、flux2-vae_small.safetensors、denoise1，以及正负提示和节点参数字符串；这些是该图公开记录，不用通用建议补成实值。训练记录rank32／2000步／ai-toolkit。
- 实际读取范围：模型介绍全文、指定版本元数据及首图的提示／参数／comfy字符串；原图HTTP403，未看任何例图。
- 本库整理备注与信息范围：风格概括仅按作者文字；不推断人物体型、五官或模型稳定倾向。作者提醒商铺／墙面可能出现虚构招牌文字，即使提示禁止文字。首图comfy字符串含workflow: undefined，不能把取得字符串当作可直接导入的合法JSON或已还原工作流。资源许可标记要求署名，具体使用范围见版本页。
- 相关原始资料：https://civitai.com/images/147713031

<a id="s08"></a>

### S08 LoRA Strength Grid：零权重与空触发基线的区别

**适用方向：** LoRA搭配·参数对照｜参考三提示、五权重的网格组织方法。

**设计思路：** 风格强度与内容保留｜留一条不请求目标风格的提示，观察作用范围。

- 原文标题：LoRA Strength Grid (core nodes only)。
- 原作者／平台与原文：mr_p_m；[原文](https://civitai.com/models/3033699?modelVersionId=3446870)。
- 发布／更新与精确版本：2026-11-03 03:10:44.751 +08:00（版本发表）；模型3033699／版本3446870 v1.0；loraStrengthGridCore_v10.json，约68.95KB。
- 收录类型与内容形式：首次收录；本库概述，非原文转载或本库实测。
- 原作者分享要点（本库概述）：作者分享仅使用核心节点的网格流程：三条提示分别配0、0.4、0.7、1、1.3五档强度，每行同seed，再保存整张网格。保留一条不要求LoRA所学内容的提示，用于观察它是否也影响其他题材。
- 公开资料与适用条件：作者测试环境ComfyUI0.27.1、SDXL系检查点；832×1216、28步、Euler ancestral、CFG5，模型与CLIP等强度，共15次采样。作者明确这些设置面向Illustrious系，其他基座需另核；0强度仍保留触发词，干净基线须另将触发留空。
- 实际读取范围：模型介绍全文、指定版本说明与配置文件元数据；未下载／打开JSON、未看网格图。
- 本库整理备注与信息范围：本库只汇总作者对照设计，未执行网格或新增自动实验。未读JSON，不能确认全部节点连线、隐藏设置或版本兼容。约7分钟是作者RTX4060 8GB个例，不作本库耗时保证。

<a id="s09"></a>

### S09 Anima系14模型比较：把任务遵循与个人审美分开

**适用方向：** 模型选型·提示词组织｜参考同条件比较与任务检查表的写法。

**设计思路：** 任务遵循与审美分评｜先检查姿态和空间要求，再按个人偏好选择画风。

- 原文标题：【Anima系モデルの選び方】14本・336枚を総当たりして分かった「推し3本」と「個性派3本」。
- 原作者／平台与原文：AIスケッチ / ai_sketch；[原文](https://note.com/ai_sketch/n/n86dbfb22c5ca)。
- 发布／更新与精确版本：2026-11-02 13:33:49 +08:00（原文14:33:49 +09:00）；该篇公开文章；Anima_Compare_note.json附件未读取，14个模型的精确版本未逐枚核实。
- 收录类型与内容形式：首次收录；本库概述，非原文转载或本库实测。
- 原作者分享要点（本库概述）：作者称以14个Anima系模型生成336张，固定提示、seed和设置，分别比较简单／困难姿态、自然语言任务与画风偏好。文章公开检查项目和失败例，并记录作者与AI对同图审美排名不同；参考价值在比较方法与审美归属，而非将推荐顺序当作客观排名。
- 公开资料与适用条件：作者称统一2B版、无LoRA，编码器qwen_3_06b_base.safetensors、VAE qwen_image_vae.safetensors，流程30步／CFG4／er_sde/simple。正文给出拳头透视提示及窗边写生自然语言范例；约定画面左右按观看者，右手按人物自身。RTX4070Ti SUPER约20秒是作者环境报告。
- 实际读取范围：note公开API文章文字全文约4261日文字符；未看图片表格、视频或附件。
- 本库整理备注与信息范围：图片中的14模型清单／版本与336张结果未由本库逐项核验。作者偏好的hikari、nyaIris、cotton等属于个人评价；计数、身体朝向和颜色仍有失败记录。“补充正面朝向”建议作者也标明未试，不改写成已验证方法。所有模型统一设置有助此轮比较，但不等于各模型最优配置。

<a id="s10"></a>

### S10 Anima Wardrobe V5：自然语言绑定与角色服装预设

**适用方向：** 自动提示·服装预设·多主体｜用自然语言绑定角色外观、服装与场景关系。

**设计思路：** 角色与关系分工｜标签承载外观，绑定句说明谁穿什么及人物关系。

- 原文标题：大的来了ComfyUI插件Comfyui-Anima-Wardrobe-V5版本提示词增加自然语言（画面感提升巨大）1103更新完成。
- 原作者／平台与原文：灵冻不冻；[bilibili视频](https://www.bilibili.com/video/BV1Af4T6cEvM/)；[作者公开仓库](https://github.com/lingdongbudong/Comfyui-Anima-Wardrobe-V5)。用户提供的[短链接](https://b23.tv/KlqBwXx)已核对重定向至同一BV号，归档使用清洁直达链接。
- 发布／更新与精确版本：视频2026-11-03 07:30:00 +08:00，65分30秒；本次10:40起补读。仓库v5.0.8，固定提交 `6c18fd26cbdeaa32aac45a8e09675f06f8894f8a`（2026-11-03 02:11:51 +08:00），不是对视频中每一处操作的逐帧核对。
- 收录类型与内容形式：用户指定补充；将08:48的简介线索补读为正式条目，原视频与仓库合并一项。本段是本库概述，感谢作者公开分享。
- 原作者分享要点（本库概述）：作者将角色、服装和场景词库组织成可复现的本地随机提示词节点，补入自然语言关系描述及角色服装预设。版本记录说明双人时按角色分别绑定衣着／外观，并让共享随机字段让位，避免同一属性重复描述。
- 自然语言与提示词组织：按已读文档，工具运行时不调用大模型，而是本地词库／规则组合。v5.0.7记录了双人服装预设的修复：每人分别写“谁穿什么／谁有什么”的绑定句，并清空冲突的共享服装字段；v5.0.8又记录移除自拍手机描述，同时排除随机道具、动作和机位来源。这里可学习的是检查所有描述来源、避免重复和互相干扰；效果记录属于原作者，不是本库实验。
- 公开接口与参数：四个节点分别承担随机正文、分级、拼接、检查修复；随机节点输出 `text/report/level/cn_summary`。作者说明固定seed与设置可复现文本，`-1`用于重抽；段／字段／选项三层权重，0关闭、1常态、3必现的规则仍受分级和互斥控制。本库未运行核验。
- 公开工作流读取：已读[独立提示词输出JSON](https://github.com/lingdongbudong/Comfyui-Anima-Wardrobe-V5/blob/6c18fd26cbdeaa32aac45a8e09675f06f8894f8a/workflows/Anima-V5_%E7%8B%AC%E7%AB%8B%E6%8F%90%E7%A4%BA%E8%AF%8D%E8%BE%93%E5%87%BA.json)。6个节点含2个Note；`AnimaV5RandomPrompt`的text同时接审查与正文保存，审查report接另一保存节点，没有采样／模型加载分支。两个保存节点来自Comfyroll；JSON保留作者Windows保存目录，实际接入前需核对。README介绍接入作者出图流程的全局正文端口1004，但本次未取得该完整出图流程，不推广此编号为其他工作流的固定接法。
- 适用条件与数据范围：作者要求Python3.10+及支持WEB_DIRECTORY的ComfyUI，运行时纯标准库与原生JS；不等于配套保存节点也无额外依赖。角色库／预设数量是作者数据说明，本库未逐项审核；角色、服装与最终生图表现并不因预设存在而获保证。默认sfw，词库另含成人分级内容；本条仅整理提示词组织与工作流设计，不摘录具体成人词条。
- 署名与使用条件：插件作者灵冻不冻；上游 `ANIMA提示词生成器.html` 作者飞蓬。仓库声明GPL-3.0；作者称上游已授权开源但未说明其具体许可证，原始HTML未随仓库提供，本库未独立核实授权文件。模型、人物与其他素材的权利另计，本次未搬运词库、图片或配置文件。
- 实际读取范围：视频完整简介与元数据；仓库README全文、手册与版本历史相关段落、独立提示词JSON；未看视频／图片、未取得字幕。USAGE仅相关段落，CHANGELOG重点v5.0.7／v5.0.8，不冒称读完全部历史或审查实现。
- 本库整理备注：视频标题中的“画面感提升巨大”保留为原标题，不当作效果已验证。尚未安装、加载、生成文本、复跑生图或确认身份／服装保持；本条设计摘要适用于查阅作者方法，不是某种具体画风的视觉结论。
- 固定版本资料：[README](https://github.com/lingdongbudong/Comfyui-Anima-Wardrobe-V5/blob/6c18fd26cbdeaa32aac45a8e09675f06f8894f8a/README.md) · [使用手册](https://github.com/lingdongbudong/Comfyui-Anima-Wardrobe-V5/blob/6c18fd26cbdeaa32aac45a8e09675f06f8894f8a/docs/USAGE.md) · [版本历史](https://github.com/lingdongbudong/Comfyui-Anima-Wardrobe-V5/blob/6c18fd26cbdeaa32aac45a8e09675f06f8894f8a/docs/CHANGELOG.md)。

## 来源覆盖与检索记录

| 平台／吧名 | 实际入口、读取范围与结果 |
|---|---|
| stablediffusion吧 | 03:59:19，aiotieba4.8.2／仓库只读脚本CREATE最新列表1页30条，实际吧名stablediffusion；除置顶外已到11月1日，跨过上轮晨间窗口。读取11160517561首楼训练反馈，内容见后续补充。沿用上轮核对的无空格入口；本轮未重新请求带空格入口，未假称新的网页重定向验证。 |
| comfyui吧 | 03:59:19，同工具CREATE列表1页28条，实际吧名comfyui；剔除旧置顶后已到10月29日。读取11160149511第1–2楼，是UltimateSDUpscaleFLSLLLite获取求助，未读到可用资源与教程，不写成解决方案。未启动Astron备用。 |
| 贴吧补充搜索 | 全站最新“工作流 教程 分享”1页29条、“LoRA 提示词”1页30条；按实际吧名与原帖日期筛选，结果夹有旧帖和其他吧，未冒称近期全覆盖。两吧本轮各一页列表，不声称已读完所有历史或全部回复。 |
| bilibili | 03:59前后，“ComfyUI 教程”按pubdate公开API返回20条，code0；已读标题、UP主、pubdate与相关两条的搜索简介。“生图 模型”查询HTTP412；Qwen2.1动作迁移、批量换装两条view API均412，网页打开也失败，正文／字幕／视频／配方未取得。近期候选仅留线索，不依据标题宣称效果。 |
| Reddit | r/StableDiffusion最新50条与r/comfyui最新30条JSON请求均403；两轮含日期的英文workflow／LoRA／prompt及MOSS／Anima补查，仅返回旧帖或无关结果。未取得可靠本轮增量，不推断平台无更新；搜索摘要不记为已读原帖。 |
| Hugging Face | 按lastModified检索text-to-image 40条，完整读取4份模型卡（S01–S03及SD1.4旧书插画LoRA）；另读S01固定配置与S03文件目录。明确区分完整权重、LoRA／LoHa、量化打包和镜像。未下载权重、未看HF示范。列表最新40条不代表覆盖所有新模型。 |
| GitHub | 近期ComfyUI workflow仓库搜索15条、最近新建prompt相关仓库10条。S05 README全文＋3条提交说明；S06 README部分章节＋3条提交说明；另读VRM Pose Studio开头约1500字符。未安装或读这些项目的实现；已知ZuperWorkflow仅出现新push而未核实变化，本轮不重复计条目。 |
| Civitai社区／论坛 | 最新文章25条、模型／版本30条。CharaDB及TKtagger文章全文；V67文章仅导论与前段；S07／S08模型介绍与指定版本全文，S07首图公开提示、参数及节点字符串。原图403；未读评论讨论、未取得S08配置正文，不将模型列表等同于逐项深入。 |
| 其他作者论坛：note.com | 站内搜索403；RSS成功读取25条标题与日期，进一步读取Anima比较及HairDeck体验两篇全文。S09入正文，HairDeck作为邻近3D用途补充；note网页打开失败，但原文API可读，分别记录。 |

## 后续关注与更正

- 贴吧训练反馈：[白泽千岁《孩子们，MOSS可能真的要大力出奇迹》](https://tieba.baidu.com/p/11160517561)，首楼2026-11-02 21:39:57。本库读首楼文字：作者为人物瞳孔与背部发条特征增加数据至近400张、训练至4000步后自述改善。数据量和步数一起改变，基座版本／对照图／精确参数未取得，不能归因于单个变量或推广成MOSS训练下限。保留作者个案，不据短帖宣称通用训练结论。
- bilibili近期待补：[余小文AIGC《QwenImage2.1人物动作迁移》](https://www.bilibili.com/video/BV1zd4A61EVz/)，2026-11-02 23:30:25；[AI工作流《人物批量换装工作流》](https://www.bilibili.com/video/BV1RHx46AELU/)，2026-11-02 18:30:00。仅取得搜索标题／作者／日期及简介；详情受限，未把“完美复刻”“理论9999套”等标题措辞当结论。后续需要的是原视频步骤与实际公开配置。
- 邻近3D用途：[混合順《ComfyUIでHairDeckを試してみた》](https://note.com/kongo_jun/n/n616292ee1c1c)，2026-11-02 23:10:34北京时间；原作者分享从人物图生成带绑定头发的ComfyUI流程，提供VRM／GLB附件。读文章全文约988日文字符，未看图或附件；38秒／8GB为其RTX4090环境个例。作者认为输入还原度仍有提升空间。本库未安装、下载模型或把3D头发流程当生图画风。
- 移动打标工具线索：[Quocraft_AI《TKtagger - Android Tagging & Captioning App》](https://civitai.com/articles/37826)，2026-11-02 03:25:10北京时间，早于上轮晨间窗口，属于近期补录线索。文章全文仅介绍Android本地ONNX、无需服务器与多语言界面，指向[Quocraft1436/TKtaggerDroid](https://github.com/Quocraft1436/TKtaggerDroid)；未读仓库、未核具体模型和打标效果，不单凭功能清单推荐。
- 风格系列补来源：[angelomaiota的V67系列文章](https://civitai.com/articles/37871)，2026-11-02 20:26:02北京时间。读导论及前段的摄影与绘画材质、东方人物方向说明，未读完全部组件、未看图。与[既有V67记录](../2026-10-30/notes/history/civitai.md#cv-17)同作者同系列，补充作者的组件组织思路；不把宣传中的museum-quality或8K词当质量证明，不据此假定所有版本可叠加。
- 另读[Sergio2291的SD1.4旧书插画LoRA模型卡](https://huggingface.co/Sergio2291/sd14-lora-oldbookillustrations/blob/ce6f10ad3567443fdf145bee9fa28c0c7f98d322/README.md)全文：基座SD1.4、UNet rank6、训练数据gigant/oldbookillustrations，示范图未看。读取信息较少，作为不同家族与用途的补充线索；不根据“旧书”名称猜具体笔触或人物画法。
- 高分辨率适配器的最新文件与README示范版本不一致（S03）；Anima设定表的图像→标签与直接参考编辑不同（S05）；零LoRA权重仍含触发词（S08）。这些条件随原作者版本更新再核对，本次不新增实验任务。
- 本日先保存4项，再补齐5项、平台覆盖和已读线索。全部为资料阅读／本库概述；没有成图、加载、复跑或用户收益验证记录。

## 08:48起补查：bilibili开源读取工具

本节记录08:48起工具补查，保留晨间的原始412记录，不表示重跑全部平台；当时精选9项。10:40起按用户指定补读V5仓库并新增S10，当前共10项。

- 已用bilibili-api-python17.4.2游客态取得最新排序搜索1页20条；另经本库只读脚本取得搜索、详情与字幕状态输出。使用继承的环境代理，未自动登录或提取浏览器Cookie。
- [余小文AIGC《QwenImage2.1人物动作迁移》](https://www.bilibili.com/video/BV1zd4A61EVz/)（2026-11-02 23:30:25）已补到完整简介、43秒时长及cid。原先“只读搜索简介”的范围仅适用于晨间；新范围仍不含视频画面、字幕、实际工作流与效果核验。简介中的“完美复刻”等为作者措辞，不作为本库结论。
- 工具调用新取得的简介线索：[灵冻不冻《大的来了ComfyUI插件Comfyui-Anima-Wardrobe-V5版本提示词增加自然语言（画面感提升巨大）1103更新完成》](https://www.bilibili.com/video/BV1Af4T6cEvM/)，2026-11-03 07:30:00。适用方向：自动提示·角色服装预设｜按作者简介，加入自然语言扩写和角色服装预设；设计思路：设定与描述组织｜将角色服装预设与自然语言描述组合。简介指向[作者V5仓库](https://github.com/lingdongbudong/Comfyui-Anima-Wardrobe-V5)，08:48时尚未读取其正文、视频或配置，因此当时只作线索。10:40起已补读仓库文档与独立提示词JSON，转为[S10正式条目](#s10)；视频画面和字幕仍未取得。
- 对首个视频的字幕调用返回缺少SESSDATA；本库脚本游客态返回login_required。本次没有取得字幕、没有把AI总结或弹幕冒作逐字稿。
- 主工具为固定SDK版本＋只读脚本；CLI仅备用，具体版本、实测与上游归档状态见[bilibili工具说明](../../docs/bilibili检索工具使用说明.md)。

## 10:40起用户指定补充

用户提供V5视频短链接后，核对BV号、作者及版本，并补读作者仓库；新增S10，三个浏览入口使用一致适用方向／设计思路。晨间及08:48的访问结果按原时段保留，未将本次补查写成全平台重新检索。

[返回总索引](../../每日检索可速查总结.md)
