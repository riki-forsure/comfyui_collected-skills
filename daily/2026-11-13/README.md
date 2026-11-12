# 2026-11-13 每日社区发现

感谢社区作者分享模型、工作流、教程和实践经验。本页为本库中文概述与学习备注，保留原作者、原文与版本入口，欢迎回原帖阅读完整资料和后续更新。第三方成果归原作者；署名链接不作为额外转载授权。

- 北京日期与实际检索时间：2026-11-13，04:02起读取仓库和近期入口，约04:08完成本轮主要来源阅读，随后整理并核对归档。
- 类型：无具体差距要求的每日广泛发现；没有额外主动专题，不以某个目标画风替代平台覆盖。
- 状态：归档10项主题，包含后训练／蒸馏适配、合并方法、提示与训练经验、工作流和社区实践。部分来源受限，实际范围见覆盖表。
- 时间窗：优先自11月12日03:57–04:04各平台上次成功快照之后的新增和实质变化，至本轮各来源读取时间。Emanata为本轮首次发现的修复资源归档，底层模型不作当日新训练；旧记录按链接回溯。
- 本轮仅研究与汇总，复用SDK＋FFmpeg＋OCR和缓存ASR补读一条183秒视频；未安装生图节点、下载大模型、调用生成API、开启服务或执行自动实验。读取、作者声明、实际看图与效果验证分别记录。

## 今日值得阅读

- [H3-Image波普LoRA](https://huggingface.co/syntaxdiffusion/tanaami-style-h3-image-lora)与[MOSS十二步适配](https://huggingface.co/anyMODE/moss-image-12step-turbo-lora)：分别看风格触发、题材选择和导出缩放条件。
- [Solarum标注经验](https://civitai.com/articles/38638)与[抽象画训练经验](https://civitai.com/articles/38640)：按学习目标理解标注职责，也关注训练题材能否迁移。
- [双角色分绘合成](https://civitai.com/models/3043456?modelVersionId=3459584)和[生成器3.0](https://www.bilibili.com/video/BV1J1Wd6pEta/)：前者讨论位置／身份取舍，后者补网页生图与标签界面更新。

## 分享速查

| 类别 | 分享／资源与版本 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点／可学习经验 | 读取状态 |
|---|---|---|---|---|---|---|
| 风格LoRA／后训练 | [N01 Tanaami-style H3-Image LoRA：高密度波普与题材提示](#n01) | 风格插画·提示词组织｜在H3-Image中结合风格触发与具体图案母题。 | 美术风格方向：迷幻波普·高饱和拼贴｜已看两组示范呈现粗轮廓、彩带和密集装饰。 | [syntaxdiffusion](https://huggingface.co/syntaxdiffusion/tanaami-style-h3-image-lora) | 17图、rank16风格适配；0.5／0.75／1.0对照体现题材和强度的共同作用。 | 固定模型卡全文、老虎与渔夫两组四栏图；未读训练实现、核权重或运行。 |
| 蒸馏适配／少步采样 | [N02 MOSS十二步蒸馏LoRA：缩放导出与加载器条件](#n02) | 少步生成·兼容排错｜按MOSS-SFT和导出缩放方式选择十二步适配。 | — | [anyMODE；OpenMOSS及所引方法作者](https://huggingface.co/anyMODE/moss-image-12step-turbo-lora) | weightsx2、alpha元数据版和PEFT版属于导出用途差异，不能反复叠加缩放。 | 固定模型卡全文与文件列表元数据；未读训练代码、示范图或加载实现。 |
| 合并模型／Illustrious谱系 | [N03 AniCross IL Blend与MBW：三路平均和分块合并分开](#n03) | 模型选型·画风组合｜区分Illustrious三路加权和分块合并的取舍。 | 设计思路：谱系组合·分块取舍｜以不同合并方式探索线条、厚涂和角色倾向。 | [dabasir；WAI、NoobAI与Nova上游作者](https://civitai.com/models/3048912?modelVersionId=3466897) | 两资源是不同合并方法，不是一份模型的别名或只改变总强度。 | 两个完整资源说明与v1.0元数据；未看例图、读取合并脚本或核权重。 |
| 机位LoRA／实验适配 | [N04 RS Camera Control：42训练视点与有限测试范围](#n04) | Anima2B·机位控制｜查阅相机LoRA与构图提示共同工作的条件。 | 设计思路：机位预设·提示配合｜选择邻近训练视点，并与相同构图提示分开比较。 | [raspie／raspie10032；CircleStone Labs](https://huggingface.co/raspie/RS-CAMERA-CONTROL) | 42个训练视点不等于42个已验证机位；两向测试在不加LoRA时也匹配。 | 固定模型卡全文与节点仓库入口；未读节点实现、看测试图或核权重。 |
| LoRA训练／数据设计经验 | [N05 Solarum两篇训练经验：标注职责与题材覆盖一起看](#n05) | LoRA训练·数据标注｜按学习目标区分风格共有项与变化内容。 | 设计思路：风格与内容分工｜调整标注职责，同时补齐风格可迁移的题材。 | [signalofsolarum](https://civitai.com/articles/38638) | 精简共有风格词和补充“风格中的具体主体”分别解决不同目标，不能归纳为越短越好。 | 两篇文章正文全文与发布元数据；未看对照图、读取数据集／训练日志或复跑。 |
| 多主体／合成工作流 | [N06 Krea2双角色：分开生成、抠图合成后低强度统一](#n06) | 多主体关系·角色合成｜分别生成角色后定位合成，再统一光线与边缘。 | 设计思路：角色分绘·整体统一｜先保留各自属性和位置，再控制整体重绘变化。 | [Azimondious](https://civitai.com/models/3043456?modelVersionId=3459584) | 实际测试为分开站立的通用成年人，未测角色LoRA或拥抱等交叠关系。 | 完整资源说明与v1.0元数据；未读附件JSON、看对照图或运行。 |
| 提示编排／CSV节点 | [N07 Sequential CSV Wildcard：行号驱动的顺序提示](#n07) | 提示词组织·批量编排｜按CSV行号顺序展开选项并记录使用位置。 | — | [Rightey](https://github.com/Rightey/ComfyUI-SequentialCSVWildcard) | seed在本节点是行索引；多个通配组共用索引，不是所有选项笛卡尔积。 | 固定README全文及创建／提交元数据；源码树接口401，未读实现或运行。 |
| B站教程／实质版本更新 | [N08 柒月FIGO生成器3.0：网页生图入口与标签界面更新](#n08) | 提示词工具·生成衔接｜将选词结果送入网页生图入口并管理LoRA。 | 设计思路：选词与生成衔接｜从已选列表进入生成面板，保留标签与参数检查。 | [柒月FIGO](https://www.bilibili.com/video/BV1J1Wd6pEta/) | 3.0补网页内生图演示、浅色界面和滚动修复；不再把2.0未实现状态套给本版。 | 完整简介、183秒P1、16张抽样／末帧、OCR与ASR草稿；未取得ZIP实现、平台字幕或评论。 |
| 贴吧分享／实践经验 | [N09 贴吧社区实践：画风探索、白模姿态与移动操作](#n09) | 画风组合·姿态参考·移动操作｜阅读作者的LoRA组合探索与单手交互思路。 | 设计思路：组合探索·白模参考｜分享少量LoRA搭配、三维参考和移动操作经验。 | [雨泪滴泽](https://tieba.baidu.com/p/11190301988) | 作者主动分享个人画风和前端思路，但完整配方／项目文件未取得，不由文字猜图。 | 首楼／主题元数据与第1页25条可见楼层文字；未看图片、楼中楼或附件。 |
| 修复资源归档／上游追溯 | [N10 Emanata漫画修复索引：去网点、压缩伪影与放大分工](#n10) | 漫画修复·资源选型｜区分去网点、JPEG伪影与不同倍率放大模型。 | — | [MadameMinty；OpenComic AI、waifu2x、Real-ESRGAN等原作者](https://huggingface.co/MadameMinty/Emanata) | 既有修复模型的按用途归档，逐文件来源和许可清楚，不计作新的后训练模型。 | 固定README及两份OpenComic SOURCE.md全文；未核权重哈希、看修复图或运行。 |

## 当日分享

<a id="n01"></a>

### N01 Tanaami-style H3-Image LoRA：高密度波普与题材提示

**适用方向：风格插画·提示词组织｜在H3-Image中结合风格触发与具体图案母题。**

**美术风格方向：迷幻波普·高饱和拼贴｜已看两组示范呈现粗轮廓、彩带和密集装饰。**

- 原作者与原文：[Tanaami-style LoRA for MiniMax H3 Image](https://huggingface.co/syntaxdiffusion/tanaami-style-h3-image-lora)，syntaxdiffusion；[固定模型卡](https://huggingface.co/syntaxdiffusion/tanaami-style-h3-image-lora/blob/3804b381526a3e537c7961942ba4861a831b2d39/README.md)。北京时间11月13日02:03创建／更新，首次收录。
- 作者说明：AI Toolkit的minimax_h3_image架构，17张约4MP图、rank16、2000步、batch1、AdamW8bit、学习率1e-4，并用ostris的训练assistant LoRA。训练助手的作用与推理风格文件分别记，不据文件名推断需要一起用于出图。
- 作者用法为Model Only加载器接在H3 Image模型与采样之间，约4MP、6步、CFG1、Euler／simple；提示以`T4N4AM1 style illustration.`开头，强度0.75–1.0。作者说在眼、牙、彩带、火焰、条纹、密集拼贴等母题下风格更强，普通主体更偏大胆彩色插画；这是这份LoRA的用法，不推广成所有H3提示规则。
- 本库实际看[老虎四栏图](https://huggingface.co/syntaxdiffusion/tanaami-style-h3-image-lora/blob/3804b381526a3e537c7961942ba4861a831b2d39/samples/strip_tiger.jpg)和[渔夫四栏图](https://huggingface.co/syntaxdiffusion/tanaami-style-h3-image-lora/blob/3804b381526a3e537c7961942ba4861a831b2d39/samples/strip_fisherman.jpg)：作者标为base／0.5／0.75／1.0、同提示同seed。老虎组随强度提高，背景更满、眼形和多色带更密；渔夫组从白底写实感向有轮廓、纹理与装饰背景的插画变化。高强度不是对所有题材都更贴合母题的证明。
- 人物观察仅有渔夫近脸一组：本例保留突出鼻梁、眼睑与额头皱褶，胡须、帽纹以密集线条刻画，神情克制。年长面貌属于该主体，不概括成风格固定年龄、全身体型或原画师全作品特征。其余两组未看，完整提示／运行元数据未取得。
- 实际读取范围：固定模型卡全文、两组原始对照条图；未核权重、读训练日志或运行。权重遵循原模型Community License；“Tanaami-style”是资源作者命名，不代表原画师参与或背书。

<a id="n02"></a>

### N02 MOSS十二步蒸馏LoRA：缩放导出与加载器条件

**适用方向：少步生成·兼容排错｜按MOSS-SFT和导出缩放方式选择十二步适配。**

- 原作者与原文：[MOSS-Image-SFT 12-Step Turbo Distillation LoRA](https://huggingface.co/anyMODE/moss-image-12step-turbo-lora)，anyMODE；[固定卡](https://huggingface.co/anyMODE/moss-image-12step-turbo-lora/blob/5045cdb8366d6993282a716613227d79108e8274/README.md)。11月12日20:24创建、20:25更新，首次收录，与既有HaDeS及其他少步资源分开。
- 作者介绍在线teacher–student轨迹匹配，将24步CFG3的目标蒸馏到12步CFG1，rank64，并称用CFG-Zero*投影和Differential Guidance改善对比／细纹理。模型卡base_model和推荐明确指MOSS-Image-SFT，训练段又概称5.2B base teacher；精确teacher revision未取得，不凭“base”一词替其改成已核官方Base checkpoint。
- 三个导出分别是`12_step_turbo_moss_1024_distill_v8_r64_weightsx2.safetensors`（作者推荐，张量已乘2，强度1）、标准r64版（alpha128，作者说忽略alpha的加载器才用2）、原始PEFT续训格式。它们不是三轮独立训练；也不能对weightsx2再机械乘2。具体加载器是否读取alpha，本库未读实现。
- 作者推荐SFT BF16／int8 ConvRot、12步、Euler（或文中flow）、simple、CFG1、LoRA1.0（weightsx2）。这些是卡片推荐，不是某张图的完整实值，更不能套用到MOSS Base或所有量化加载器后称已兼容。
- “无质量退化”“保留解剖与微纹理”等为作者措辞；原卡未给本轮已读的完整配对图／评估日志，本库不确认这些效果，也不把少步直接等同同质量提速。
- 实际读取范围：固定模型卡全文和版本／文件元数据；未看图、读训练与推理实现、下载核权重或运行。

<a id="n03"></a>

### N03 AniCross IL Blend与MBW：三路平均和分块合并分开

**适用方向：模型选型·画风组合｜区分Illustrious三路加权和分块合并的取舍。**

**设计思路：谱系组合·分块取舍｜以不同合并方式探索线条、厚涂和角色倾向。**

- 原作者与原文：[AniCross Blend IL](https://civitai.com/models/3048912?modelVersionId=3466897)，v1.0／3466897，11月13日03:38发布；[AniCross MBW IL](https://civitai.com/models/3048881?modelVersionId=3466856)，v1.0／3466856，03:10发布。dabasir，首次合并导读，精确资源仍分别记录。
- Blend作者配方仅合UNet：0.50 WAI_Illustrious_ILXL_Real v1.0＋0.30 NoobAI-XL EPS Four-Mix（CyberFix）＋0.20 Nova Anime XL IL v19.0，VAE与文本编码器继承WAI。MBW则WAI向NoobAI总体0.40，作者列base0.30／in0.45／mid0.55／out0.50的分块系数；未读脚本，不能自行将两层系数相乘写成真实逐块有效值。
- 作者将系列称为机制批次：Diff、Dual、MBW、Blend用于探索不同组合，而非alpha从小到大的同一路线。本轮只深入Blend与MBW，不把系列另外两项算作已读或已验证。
- 设计定位按作者描述：结合高细节动漫渲染、厚涂倾向与角色知识。本文以合并思路概括，未看图，不凭模型／画师名推断脸型、身材或具体上色效果。原文也提醒NoobAI可能牵引角色倾向，分块版可能改变手部与文字。
- 两页通用推荐Euler a、24–28步、CFG5.0–5.5、832×1216，Danbooru式标签；Hires建议也属于作者经验。未取得逐图正负提示、有效采样或合并权重比对；合并资源不当作已证实的新一轮训练。上游许可请逐项核对，原文称有衍生／生成服务许可、未获销售checkpoint授权，本库未独立审核所有父资源条款。
- 实际读取范围：两份完整说明、版本日期与父资源链接；未看例图、读合并脚本／逐图元数据、核权重或运行。

<a id="n04"></a>

### N04 RS Camera Control：42训练视点与有限测试范围

**适用方向：Anima2B·机位控制｜查阅相机LoRA与构图提示共同工作的条件。**

**设计思路：机位预设·提示配合｜选择邻近训练视点，并与相同构图提示分开比较。**

- 原作者与原文：[RS-CAMERA-CONTROL](https://huggingface.co/raspie/RS-CAMERA-CONTROL)，raspie；[固定模型卡](https://huggingface.co/raspie/RS-CAMERA-CONTROL/blob/d91f7186804ce14e41b9dc5d0244dea66205de30/README.md)。11月12日23:27创建、23:30更新，首次收录。
- 作者在Anima Base v1.0上用42个相机视点的合成角色渲染训练实验LoRA，原渲染与caption私有。通过[RS MultiCharacter Sampler](https://github.com/raspie10032/ComfyUI_RS_MultiCharacter_Sampler)的RS Camera Control节点输入Anima2B MODEL，输出MODEL与building pipe；节点选择邻近训练机位并套相应构图提示。
- 作者用法强度1；强度0可以保留相同构图提示作比较。卡片验证仅涉及Aesthetic v1.1、RS-CVN5、Progressive、832×1216、Euler A CFG++、15步、CFG3，温室场景单seed的左右侧脸；作者明确写加／不加LoRA都匹配。不能由此认定增益来自LoRA、完整相机球已验证或支持其他block数的Anima分支。
- 多角色采样器的名称与该相机LoRA的能力分开，不补称角色隔离、任意视角、透视结构或身份一致性均成立。作者节点首次使用会获取权重，手动位置为loras/anima；本轮未执行节点，不触发自动下载。
- 实际读取范围：固定卡全文、创建／更新时间及节点项目入口；未取得私有训练集、测试图、节点实现或运行记录。许可按CircleStone Non-Commercial及作者署名要求使用。

<a id="n05"></a>

### N05 Solarum两篇训练经验：标注职责与题材覆盖一起看

**适用方向：LoRA训练·数据标注｜按学习目标区分风格共有项与变化内容。**

**设计思路：风格与内容分工｜调整标注职责，同时补齐风格可迁移的题材。**

- 原作者与原文：[My Captions Taught My LoRA Nothing（Undercity Fix）](https://civitai.com/articles/38638)，11月12日04:19发布；[I Trained a LoRA on My Own Automatic Drawings](https://civitai.com/articles/38640)，04:49发布。signalofsolarum的Building Solarum第6／7篇，首次合并收录，两文均以Juggernaut XL v9路线研究其自有世界设定。
- 第6篇：作者从12种地下场景各20次候选中筛74张，起初完整caption写铜管、冰、蒸汽等共有外观；随后称保持图集／设置／seed，仅改为trigger加房间类别等变化内容，触发词才更容易带出共有地下城观感。作者“文字已解释一切、trigger只学剩余”的讲法是其教学解释，不当作已读训练实现证明的普遍机制。
- 第7篇给出另一面：7张自己的铅笔／淡水彩自动绘画经裁切和旋转形成111张，标注只有trigger＋abstract时会画抽象，却难把新主体画进这种风格。作者先用低强度img2img从原笔触长出19种主体，仍缺室内等题材；再补40种并筛60张主体可辨的图，未见题材的测试才更像所需画法。
- 可学习的取舍是**先定想被trigger承载的共有特征，再标清变化内容，并用训练集外题材找覆盖缺口**。第6篇的短标注与第7篇仅abstract失败不矛盾；不能推出所有风格／角色LoRA都删细节或只写短词。旋转增强也只在作者这种无固定上下的抽象画前提下使用。
- 作者仍承认第7篇结果比手绘更整洁、偏墨线／版画；第6篇的蒸汽、钢梁、发光菌仍弱，强度高于0.9偏热。两文示例和AI助手协作均按作者叙述，本库没有看对照或核验控制变量；不据文字宣称收益已证实。
- 原资源：[Undercity XL](https://civitai.red/models/3040999)、[Lattice-sight Grey XL](https://civitai.red/models/3043053)，本轮只定位，不复制训练集或自动执行文中的多轮流程。实际读取范围：两文正文全文和日期；未看示例图、读数据／日志或运行。

<a id="n06"></a>

### N06 Krea2双角色：分开生成、抠图合成后低强度统一

**适用方向：多主体关系·角色合成｜分别生成角色后定位合成，再统一光线与边缘。**

**设计思路：角色分绘·整体统一｜先保留各自属性和位置，再控制整体重绘变化。**

- 原作者与原文：[Krea 2 Two Characters Without Merging](https://civitai.com/models/3043456?modelVersionId=3459584)，Azimondious，v1.0／3459584于11月12日23:00发布；首次收录。与既有区域LoRA方案分别记录，不因都做双人就视为同一工作流。
- 作者方案：A／B各在灰背景单独生成896×1152全身图，另出1152×896无人场景；BRIA RMBG抠出角色，mask收1px并柔化，两角色缩0.62后按坐标贴入，最后用包含两人完整描述与光向的提示做denoise0.4整图统一。输出合成前后便于查看身份变化。
- 作者测试RedCraft3.0 Krea2 INT8 ConvRot，Qwen3-VL 4B、Qwen Image VAE，8步CFG1、er_sde／simple、分块VAE512／64。需ComfyUI-BRIA_AI-RMBG和RMBG1.4；后者原作者有非商业条件，其他资源许可也分别回原文查。
- 原文很有价值的限定：作者在普通单提示图里没有观察到这些测试对的属性串人，因此不声称本方案解决了已被对照证明的普遍问题；其明确观察包括单人生成更容易保留腰长发，以及贴图的位置／尺度控制。四组通用成年人不代表具名角色或任意画师组合。
- 整体重绘会改脸；0.3较贴近cutout，0.5时脸与胡须重画更明显。只测两人分开站立，拥抱、牵手或交叠身体不在此图支持范围；角色LoRA未测，不能据分绘机制就声称完全避免LoRA污染。UI JSON为脚本生成并查节点定义，非浏览器保存的实跑文件。
- 实际读取范围：完整说明、版本及作者测试范围；未看示范图、读JSON、核BRIA权重或运行，原文推荐参数不补成某张图实值。

<a id="n07"></a>

### N07 Sequential CSV Wildcard：行号驱动的顺序提示

**适用方向：提示词组织·批量编排｜按CSV行号顺序展开选项并记录使用位置。**

- 原作者与原文：[ComfyUI-SequentialCSVWildcard](https://github.com/Rightey/ComfyUI-SequentialCSVWildcard)，Rightey；固定README提交`35393401034c1cb57266c5f88ed016ce142c0e1e`。仓库11月12日19:54创建、20:03提交，首次收录。
- 作者节点位于prompt/csv，从指定CSV列逐行取提示，seed作为行号，生成后increment可逐行推进；另设column（从0起）、has_header、wrap和前后缀。输出prompt、used_index、total_rows帮助追踪所用行。
- 本节点seed属于文本选择状态，不等同采样噪声seed。`{a|b|c}`按同一index模选项数顺序选取；多个组选项共用行索引，文档不承诺枚举全部组合，不能当完整笛卡尔积测试器。wrap关且索引越界会报错，而非自动补一条随机提示。
- 作者称无需额外Python包并给Manager安装入口；本轮没有核Registry状态或执行安装。固定README可读，但随后源码树接口返回401，所以不将README规则写成已审计的实现行为，也未为补读循环换接口。
- 实际读取范围：固定README全文及创建／提交信息；未读实现、看样图或运行队列。与[11月11日SweepKit](../2026-11-11/README.md#n09)不同，此条主要负责顺序文本，不把它当已授权自动实验入口。

<a id="n08"></a>

### N08 柒月FIGO生成器3.0：网页生图入口与标签界面更新

**适用方向：提示词工具·生成衔接｜将选词结果送入网页生图入口并管理LoRA。**

**设计思路：选词与生成衔接｜从已选列表进入生成面板，保留标签与参数检查。**

- 原作者与原文：[v3.0 内置生图与tag大更！【Anima提示词生成器】](https://www.bilibili.com/video/BV1J1Wd6pEta/)，柒月FIGO，11月13日01:17:33发布，P1为183秒。完整简介给[作者3.0 ZIP分享入口](https://pan.quark.cn/s/de2a0055f067)，本轮仅记录入口，未获取压缩包实现。属于[11月9日笔记V08的2.0](../2026-11-09/notes/Anima截图视频与评论汇总.md#v08)后续实质更新。
- 视频说明新增浅色UI；通过配套文件启动HTML界面与ComfyUI代理连接，在网页里AI选词→替换已选→生图面板，选择LoRA并提交。约1:15–1:40演示选词结果和LoRA面板，约2:15起网页面板出现生成结果。当前视频确有内置生图演示，不沿用2.0时的未实现说明。
- 本库看图：16张约12秒间隔并含末帧的抽样覆盖文件启动、浅色界面、选词、生成面板与返回图。约2:03可见评分／年代／媒介等标签分组；3.0标题与讲解称tag大更，但未取得完整词表或逐条核对新增数，不将旧版词数／角色数直接移作3.0实值。
- 作者还说明修复保存／测试等弹窗文字穿出，以及提示过多顶掉“替换已选”按钮的问题，在二级界面增加滚动。ASR把HTML、ComfyUI、LoRA等词识别错，更新摘要据抽样画面字幕与界面交叉确认，不转写未核术语。
- 作者称网页与其ComfyUI端效果相同；本库未读代理代码、API请求、完整模型版本／采样与有效提示，不证明任意后端等价或所有已有工作流均兼容。视频出现的样图只是功能演示，不据此推断固定画风配方。
- 实际读取范围：完整简介、P1公开媒体、16帧及OCR、faster-whisper base的183秒时间轴草稿；无平台字幕、评论、ZIP源码或完整逐图配置。媒体、截图和完整转录不提交仓库，未运行生成器、代理或生图。

<a id="n09"></a>

### N09 贴吧社区实践：画风探索、白模姿态与移动操作

**适用方向：画风组合·姿态参考·移动操作｜阅读作者的LoRA组合探索与单手交互思路。**

**设计思路：组合探索·白模参考｜分享少量LoRA搭配、三维参考和移动操作经验。**

- 原作者与原文：[个人ai使用分享](https://tieba.baidu.com/p/11190301988)，stablediffusion吧，雨泪滴泽，11月12日17:03发布；本轮aiotieba读到第1页25条可见楼层，不代表完整楼中楼／图片已读。首次收录社区经验，感谢作者愿意交流与开放分享。
- 作者第2／4楼分别称研究一个LoRA的真实画风、三个LoRA的3D画风；第10楼给[okitatsuki资源入口](https://civitai.red/models/2702998/okitatsuki)，第14楼提到标签`@poriuretan`。这些出处分别保存，不能把一个链接、不同楼层标签与未读图片拼成完整同图配方；本轮未深读模型页。
- 第7楼称自己主要用Anima，试过深度控制而更偏好白模，并提到VRoid可做模型；同时承认内置姿势库有骨骼混乱。这是作者项目与任务中的经验，没有对照图、有效分支或控制权重，不推广成深度控制普遍不如白模。
- 第5／6／20楼介绍面向单手操作的前端、提示库／反推功能及Tailscale跨设备访问思路。作者也说明部分资料整理来自其他网站，归属应继续回原来源；本库不将该资料库或第三方作者图称作楼主原创。没有取得前端代码、包或配置，本轮只摘要交互思路，不安装VPN或开放端口。
- 实际读取范围：主题、楼主日期、25楼文字；图片、含图提示、楼中楼和项目附件未读，因此没有具体视觉画风判断。原帖承载真实社区分享价值，配置缺口分别记录，不补私人画师串／LoRA权重。

<a id="n10"></a>

### N10 Emanata漫画修复索引：去网点、压缩伪影与放大分工

**适用方向：漫画修复·资源选型｜区分去网点、JPEG伪影与不同倍率放大模型。**

- 原作者与原文：[Emanata models](https://huggingface.co/MadameMinty/Emanata)，MadameMinty；[固定README](https://huggingface.co/MadameMinty/Emanata/blob/fdc7f69cbfa9e9b134970ce675259d114e1cb31b/README.md)。仓库11月12日04:41创建、06:25更新，首次收录其资源组织方式；其中模型来自已有上游，不把归档日期改成新训练首发。
- 按任务区分：OpenComic AI去JPEG伪影和descreen是1x修复；同系列2x／3x／4x、waifu2x不同降噪等级、Real-ESRGAN AnimeVideo倍率则承担不同放大／清理用途。去网点不自动等于去除AI纹理噪点，漫画原生笔触、网点保留与压缩损伤也需按任务判断，本库未看输出对照。
- 深读[Artifact Removal Fast v2来源](https://huggingface.co/MadameMinty/Emanata/blob/fdc7f69cbfa9e9b134970ce675259d114e1cb31b/opencomic-ai-artifact-removal-compact-v2/SOURCE.md)与[Descreen Hard Fast v3来源](https://huggingface.co/MadameMinty/Emanata/blob/fdc7f69cbfa9e9b134970ce675259d114e1cb31b/opencomic-ai-descreen-hard-fast-v3-256/SOURCE.md)：两者追溯到Oleguer Llopart Mora／OpenComic AI，固定上游commit `334cc9806f22110633989fe2e8f341872dfa5477`，列param／bin整文件SHA-256和字节数，声明未改文件。本库只读清单，没有下载逐文件计算，不能称字节一致已由本库确认。
- 仓库没有统一给所有权重加许可：OpenComic条目列CC BY4.0，其他目录分别有MIT、BSD、LGPL等来源条件；代码转换与原权重也不同。请按具体目录原文使用与署名，不把“能公开下载”写成全库任意授权。
- 实际读取范围：固定README全文、上述两份SOURCE.md全文；未读全部目录许可证／转换实现、核权重或运行。以修复资源索引收录，不安装阅读器或推理服务。

## 来源覆盖与检索记录

时间均为北京时间。本表只记录本轮取得的内容；列表、摘要、正文、评论、配置与图像观察分别计范围。

| 平台／吧名 | 实际入口或查询 | 检查时间与读取范围 | 结果／限制 |
|---|---|---|---|
| stable diffusion／stablediffusion吧 | aiotieba4.8.2，CREATE最新第1页30项；[个人ai使用分享](https://tieba.baidu.com/p/11190301988)、[k2tubro的一些分享](https://tieba.baidu.com/p/11189813236) | 04:03列表核吧名，置顶单列，非置顶从11月13日01:55回过上轮晨间水位；约04:04分别读25条／5条可见楼层 | N09收录第一帖。第二帖作者称jvn与极光旧梦融合、另有纯版图，但完整资源／混合权重与图片未取得；关于纹理的回复是社区反馈，不当模型通病结论。 |
| comfyui吧 | CREATE第1页28项；[Windows更新后打不开讨论](https://tieba.baidu.com/p/11189424600) | 04:03核吧名，两个2024置顶与新帖分开，非置顶日期跨上轮水位；约04:04读首楼 | 只有求助，未取得解决回复，不当修复教程；与访问失败、无关键词命中分开。 |
| 贴吧别名／全站补充 | “stable diffusion”第1页1项；全站最新“工作流 提示词”第1页 | 04:03–04:04；别名仍返回stable吧旧公告，实际采用stablediffusion；全站按tid与实际吧名筛选 | 返回无关论坛不计生图吧覆盖，补充搜索不冒称两个吧全量正文。未启用／检查备用Astron，无循环重试。 |
| bilibili广泛发现 | SDK17.4.2按pubdate搜“ComfyUI 教程”1–4页80条返回项；“生图 模型”“Anima”“LoRA 画风”各第1页20项 | 04:03–04:06，ComfyUI页从11月13日00:51回到11月11日23:24，跨过上轮水位；按BV去重、过滤无关音乐与重复推广；N08完整简介／媒体深读 | 取得183秒P1、16帧、OCR及ASR草稿；未取得平台字幕／评论和作者ZIP实现，不把API成功称全文准确阅读。 |
| Sena404固定作者 | UID341674866最新投稿第1页30项，平台计82项 | 04:03此次接口成功；返回页从11月11日18:31至10月13日，最新仍是已存[第26期](https://www.bilibili.com/video/BV1hgWm65EEC/) | 最新页可读且跨已收录水位，本轮未见该页新增，不声称82条正文／画面全部已读；无需重复下载第26期。水位保持26，本日不沿用前两轮NetworkException状态。 |
| Reddit | r/StableDiffusion new.json50、r/comfyui new.json30；日期＋model／LoRA／workflow／tutorial等补搜 | 约04:03两个最新列表403；打开[游戏美术迭代经验](https://www.reddit.com/r/aigamedev/comments/1xu4329/my_process_for_mostly_autonomous_art_improvement/)及[MOSS Turbo疑问](https://www.reddit.com/r/StableDiffusion/comments/1xtagta/does_official_moss_image_turbo_exist/)可见正文与少量回复 | 原帖部分可读。前者文字介绍参考图、候选、人选和反馈；后者是求助与社区建议，未证明官方Turbo存在／不存在。未看图片、取得实现／完整评论，日期搜索与打开页相对时间分开；不把旧帖改成本轮确定新品。 |
| Hugging Face | text-to-image按lastModified最新80、image-to-image最新30；追风格、蒸馏、机位与修复线索 | 04:03起，N01／N02／N04／N10固定卡；两组风格对照图、两份修复SOURCE记录 | 区分训练LoRA、导出格式、转换／镜像和既有模型归档；部分卡片有强效果措辞，按作者声明记录，未下载权重或验证推理。 |
| GitHub | comfyui workflow pushed:>=2026-11-12按updated25；comfyui prompt created:>=2026-11-11按updated15；原文跟进 | 04:03起，N07固定README与元数据；另读Magik Prompt Preview说明，原图预览／提示排序功能未运行 | SequentialCSV README可读，随后源码树401，因此只据文档总结，不称实现审计。其他工具只列候选读取范围，不把编译／语法声明当前端兼容或运行验证。 |
| Civitai社区／文章／模型／工作流 | 最新模型40、文章30、Workflows15；打开文章38638／38640及版本3466897／3466856／3459584 | 04:03起，N03／N05／N06完整说明与版本日期 | 保留原作者、上游模型与限制。训练／合并／整组对照分别写，不以推荐参数补成每图实值；未深读带配方作品、全部版本评论或附件JSON。 |
| 其他有效论坛与作者资料 | forum.comfy.org/latest.json前30话题；note.com ComfyUI最新检索；按原文追作者资料 | 约04:03列表筛选，旧PhotoDeblur等已存，未见本轮已读的实质新增正文；未重复展开旧主题 | forum列表可读但不等同正文全部已读；note403。作者模型卡、原始仓库与SOURCE文件按条目分别记范围，不用其他来源冒称已读受限平台。 |

本环境没有配置可用B站会话，平台字幕未取得；ASR为本库工具生成的未完全核字草稿，术语／数字优先看画面。音视频、截图、完整转录、凭据和签名媒体地址不入库。没有自动登录、提取Cookie、启用备用CLI、反复安装或切换工具。

## 后续关注与维护

- H3风格LoRA的同图提示／参数与MOSS蒸馏的teacher revision、导出缩放和加载器行为：需读相应原始实现或数据后补，不能由命名／加载成功推断全兼容或收益。
- AniCross其余机制、父资源条件、RS相机LoRA的多题材／seed和全视点表现均不由本轮少量文字推断；再次收录要说明实质变化并回链本日。
- 训练文章的标注策略按学习目标和样本覆盖理解；双人合成的重绘量、身份保持及交叠动作分开。原文没有的私人配方和控制参数保持未取得。
- 生成器3.0已有新功能演示，保留2.0当时状态与本次更新的关联；精确API请求、ZIP实现和新增词表尚缺，不补称任意后端均可用。
- Sena最新页本轮成功，最新仍为第26期；未来继续按UID／BV／投稿时间跟进。Reddit／note及部分源码接口限制保留，不推断全网无新增。
- 本轮均未执行生图、原样复跑或获得用户效果认可；社区实践、资料读取和本库视觉观察分别归属。后续实际执行沿用明确授权与停止点，不由归档触发实验。

归档记录：2026-11-13首次整理10项主题，先保存本文，再更新总索引与阅读入口。原作者说明、读取范围及版本条件以各条为准。
