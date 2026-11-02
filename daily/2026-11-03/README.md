# 2026-11-03 每日社区发现

本页汇总社区作者的公开分享，感谢原作者的投入。以下为本库概述，保留署名与原文入口，欢迎前往原帖阅读完整内容、示范和更新。

- 北京日期与开始时间：2026-11-03 03:58（UTC时钟换算）。
- 检索类型：每日广泛发现；无具体差距要求，无主动专题。
- 执行状态：进行中，已读内容先归档；继续整理工作流、社区实践与覆盖记录。
- 优先时间窗：自2026-11-02晨间检索快照后的新增与实质更新，必要时近期补录并单列原日期；未将后续保存时间当作检索边界。
- 已归档4项。仅读取与摘要整理，未安装节点、下载大模型、运行生图或自动实验。

## 今日值得阅读

- [Qwen-Image 2.1 Lightning v2 RL：四步生成与编辑](https://huggingface.co/lightx2v/Qwen-Image-2.1-Lightning-v2-RL)：作者在Lightning v2蒸馏基础上进行RL精炼，分享四步文生图、单参考编辑及多参考生成的权重与示例。发布形式是完整transformer，需要原Qwen2.1的处理器、编码器和VAE，并非独立整套管线。
- [MOSS高分辨率LoHa：4MP以上生成的实验分享](https://huggingface.co/comfyanonymous/MOSS_image_MAX_ULTRA_hires_lora_test)：作者分享为MOSS-Image-Base训练的LoHa，目标是改善4MP及以上生成；数据为3.5–10MP动漫与摄影混合，作者也提示动漫占比可能偏高。页面给9MP的旧版本与无LoRA对比入口，适合继续关注高分辨率适配路线。
- [CharaDB：将人物固定项与服装姿态变量分开](https://civitai.com/articles/37854)：作者为批量CG创作整理可视词条与通配符，按发型、眼睛、服装、姿态浏览；强调把固定人物描述保持一致，再改变需要变化的部分。作者用同一基座、seed与基础人物制作示范卡，帮助比较词条表现，而非宣称文本能保证任意模型的角色一致性。

## 分享速查

| 类别 | 分享／资源与版本 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点／可学习经验 | 读取状态 |
|---|---|---|---|---|---|---|
| 后训练／少步蒸馏 | [S01 Qwen-Image 2.1 Lightning v2 RL：四步生成与编辑](#s01) | 少步生成·参考图编辑｜了解Qwen2.1四步RL权重的三类任务用法。 | — | [LightX2V / lightx2v；基座Qwen团队](https://huggingface.co/lightx2v/Qwen-Image-2.1-Lightning-v2-RL) | 作者在Lightning v2蒸馏基础上进行RL精炼，分享四步文生图、单参考编辑及多参考生成的权重与示例。发布形式是完整transformer，需要原Qwen2.1的处理器、编码器和VAE，并非独立整套管线。 | 固定revision模型卡全文及inference_config.json；未看对比图、未读RL实现、未取得权重 |
| 后训练／蒸馏LoRA | [S02 StepX-OPD SD3.5 Medium：区分推理LoRA与训练初始化](#s02) | 少步蒸馏·LoRA加载｜分清SD3.5四步推理文件与训练初始化。 | — | [ShimaRinC（发布账户）；模型卡署名StepFun AI；基座Stability AI](https://huggingface.co/ShimaRinC/StepX-OPD-SD3.5) | 作者发布SD3.5 Medium的StepX-OPD四步权重，说明根目录推理LoRA已合并rank160初始化与rank32学生适配器，总rank192。additive_init目录供训练初始化，不是另一枚应再次叠加的四步推理模型。 | 固定revision模型卡全文；未读论文、训练代码、配置实现或示范图 |
| 后训练／高分辨率LoHa | [S03 MOSS高分辨率LoHa：4MP以上生成的实验分享](#s03) | 高分辨率·MOSS适配器｜关注面向4MP以上生成的训练实验。 | — | [comfyanonymous；基座Comfy-Org/MOSS-Image](https://huggingface.co/comfyanonymous/MOSS_image_MAX_ULTRA_hires_lora_test) | 作者分享为MOSS-Image-Base训练的LoHa，目标是改善4MP及以上生成；数据为3.5–10MP动漫与摄影混合，作者也提示动漫占比可能偏高。页面给9MP的旧版本与无LoRA对比入口，适合继续关注高分辨率适配路线。 | 固定revision模型卡全文及文件目录元数据；未看9MP示范、未下载适配器 |
| 提示词／素材组织 | [S04 CharaDB：将人物固定项与服装姿态变量分开](#s04) | 提示词组织·角色设定·姿态｜固定人物描述，按需替换服装与动作词。 | 设计思路：固定设定与变量分工｜人物外观独立成行，服装、姿态和表情按页变化。 | [takumi1112 / Taki；基座JANKU v4及NoobAI／Illustrious作者见原文](https://civitai.com/articles/37854) | 作者为批量CG创作整理可视词条与通配符，按发型、眼睛、服装、姿态浏览；强调把固定人物描述保持一致，再改变需要变化的部分。作者用同一基座、seed与基础人物制作示范卡，帮助比较词条表现，而非宣称文本能保证任意模型的角色一致性。 | Civitai公开API文章正文全文；未打开应用、未看词条示范、未下载Release或核验数量 |

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

## 来源覆盖与检索记录

| 平台／吧名 | 实际入口、读取范围与结果 |
|---|---|
| 固定来源 | 两贴吧、bilibili、Reddit、Hugging Face、GitHub、Civitai与note.com已实际查询；详细读取范围随本轮整理补全。 |

## 后续关注与更正


[返回总索引](../../每日检索可速查总结.md)
