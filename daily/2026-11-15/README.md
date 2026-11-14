# 2026-11-15 每日社区发现

本页整理社区作者公开的模型、工作流、提示词教程与实践分享，感谢原作者的投入。正文为本库概述与导读，逐条保留作者、原文和读取范围；欢迎回原帖阅读完整内容、许可、示范与后续更新，支持原作者。署名与链接不等于额外转载授权。

- 北京日期与实际时间：2026-11-15，自03:57读取规范，03:58起分平台检索与补读，归档前持续整理。
- 检索类型：无具体差距要求的每日广泛发现；本轮没有另设主动专题。
- 执行状态：已整理11项主题，部分入口受限；未安装节点、下载大模型、启动生成或实验。
- 时间窗：优先自11月14日各平台上次成功读取（约04:00）以来的增量；近期首次收录及历史工具补读保留原始日期，不把建仓、卡片更新时间、原训练或新介绍帖混为一谈。
- 标注口径：适用方向和美术／设计短标注属于本库分类，作者经验、本库实际看图、运行与效果验证分别记录；本轮没有效果验证或用户成图认可。

## 今日值得阅读

- **模型路线**：[Serenity](https://huggingface.co/malcolmrey/moss-serenity)公开身份续训与训练／生成说明；[HaDeS v1.0](https://huggingface.co/DeVilDoNia/HaDeS-MOSS-v1.0-Turbo)提供合并配方和有限比较；[PrismPalette v3](https://civitai.com/models/2750408?modelVersionId=3469753)可看清透人物示范。
- **不同用途**：[16×16图标](https://huggingface.co/Angais/Krea-2-PixelArt-16x16)区分原始生成与像素提取；[Celestial Ink](https://civitai.com/articles/38855)以光感、尺度与墨线分工组织多LoRA。
- **可查阅的方法**：[K2-Editorial](https://www.bilibili.com/video/BV1jTs56wEEt/)讲完整母题与有限替换；[Anima排错帖](https://civitai.com/articles/38844)提醒加载成功与正确映射分开，工具和来源边界见下文。

## 分享速查

| 类别 | 分享／资源与版本 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点／可学习经验 | 读取状态 |
|---|---|---|---|---|---|---|
| 后训练模型 | [MOSS Serenity v7：姓名身份续训与场景提示分开](#n01) | 人物生成·后训练选型｜查阅身份续训、提示格式与全量模型的取舍。 | 设计思路：身份与场景分写｜以姓名触发身份，另写景别、服装与环境。 | malcolmrey／malcolmamal；OpenMOSS；[固定模型卡](https://huggingface.co/malcolmrey/moss-serenity/blob/4db08d3832bc98ae58ddb9d930b50e32a7584f7b/README.md) | 仓库10-19建立；11-14 23:24更新；首次专题收录 | 卡片相关章节、生成文档、训练章节；未看图库 |
| 合并模型更新 | [HaDeS MOSS v1.0 Turbo：QwenLook融入与八步条件](#n02) | 模型选型·少步生成｜区分内置蒸馏与QwenLook合并后的使用条件。 | — | HaDeS／DeVilDoNia；OpenMOSS及上游作者；[固定模型卡](https://huggingface.co/DeVilDoNia/HaDeS-MOSS-v1.0-Turbo/blob/1e11fcfe2aaf10062fe7b5086d6cdce36129ca51/README.md) | 11-14 06:08建仓；18:49更新；接续v0.9.4 | 模型卡全文；作者对比数据；例图未看 |
| Anima合并模型 | [PrismPalette ANIMA v3：脸部轮廓与清透光感](#n03) | 人物插画·画风选型｜参考Anima合并模型的光色与人物表现。 | 美术风格方向：清透日漫·柔亮体积｜两例圆润脸形配大亮眼，细肩轮廓与明净光色突出人物。 | Noginowa；各合并模型与LoRA原作者；[v3版本](https://civitai.com/models/2750408?modelVersionId=3469753) · [模型卡](https://huggingface.co/Noginowa/PrismPalette-ANIMA/blob/c0190d1094ded3f517d730fef156618dcb61d7e5/README.md) | v3：2026-11-14 14:00发布 | 模型卡全文、版本说明、两张示范已看 |
| 用途特化LoRA | [Krea2 PixelArt 16×16：单图标与四宫格的不同配方](#n04) | 游戏素材·像素图标｜区分单图标与四宫格适配器及网格提取。 | 美术风格方向：低分辨率像素·深色轮廓｜已看示范以阶梯轮廓、少量色阶和独立小物造型为主。 | Angais；Krea及原工具作者；[固定模型卡](https://huggingface.co/Angais/Krea-2-PixelArt-16x16/blob/1dff5939eae63cb42b7bdf3a389a602c348c2675/README.md) | 10-16建立；11-14 18:28更新；首次收录 | 模型卡全文、两张图表已看；未生成／提取 |
| 画风组合教程 | [Celestial Ink：光感、尺度与墨线的分工](#n05) | 画风搭配·构图设计｜参考Krea2多LoRA的职责和视觉焦点组织。 | 设计思路：光感·尺度·墨线分工｜以小人物和巨大景物建立尺度，用单一红色焦点引导视线。 | backrnin733；Niji Aesthetic、Pulp Cosmos、monmon、Hollow Void、TextFusion作者；[原教程](https://civitai.com/articles/38855) | 2026-11-15 02:00发布 | 文章正文全文；示范图与JSON未读 |
| 兼容排错教程 | [Anima LoRA“可加载但效果不对”：先核层数映射](#n06) | Anima兼容·LoRA排错｜区分28／40／52层映射与实际效果验证。 | — | Nausamedu；INuBq8、shin131002及前序映射研究者；[经验帖](https://civitai.com/articles/38844) · [统一补丁](https://github.com/INuBq8/ComfyUI-Anima-LoRA-ControlNet-Patch/tree/b25ae637102f2358116fe419a409f0594f61245b) | 经验帖11-14 18:25；工具为历史版本补读 | 经验帖全文、两项目README相关章节；未装补丁 |
| 提示词与场景工具 | [Libretto：预设、场景与已用工作流的关联](#n07) | 提示词组织·场景复用｜用可视预设编排人物、服装和环境条件。 | 设计思路：预设与场景分层｜复用人物服装等组件，保留每次场景与提示快照。 | Higeneko9／higeneko9；[介绍帖](https://civitai.com/articles/38838) · [版本](https://github.com/Higeneko9/Libretto/releases/tag/v0.26.1111.2) | 介绍帖11-14 15:12；版本11-12 12:01 | 文章全文、README使用段与release；未运行 |
| 批量提示节点 | [Batch Builder：提示行、采样seed和通配符分开](#n08) | 批量编排·提示词组织｜对齐逐行提示、种子与通配符的展开结果。 | — | ThedDryz；[固定README](https://github.com/ThedDryz/comfyui-batch-builder/blob/3f222f8567f8f1ceb3af076c04efba571ab09948/README.md) | 11-14 15:48建仓；19:49提交 | README全文；未执行自动排队 |
| B站教程／提示插件 | [K2-Editorial v1.12.0：完整母题与有限替换](#n09) | Krea2提示·主视觉设计｜保留母题整体结构，再替换角色、服装与文字。 | 设计思路：母题整块·有限替换｜统一构图、材质、光位和排版，避免随机片段互相冲突。 | 灵冻不冻／lingdongbudong；素材来源辞雪沐春；[原视频](https://www.bilibili.com/video/BV1jTs56wEEt/) · [固定README](https://github.com/lingdongbudong/Comfyui-K2-Editorial/blob/5a0c3fda62b6c50af153b14a86449393384802a5/README.md) | 视频11-14 20:49；README v1.12.0 | 完整视频简介与项目README；1042秒视频未深读 |
| 特化适配合并 | [H3 Image Character Swap：视频适配迁移到图片的边界](#n10) | 角色替换·参考图编辑｜按场景与角色两路输入组织H3图片替换。 | 设计思路：身份与场景分工｜明确替换对象，分别要求保留角色特征与原场景条件。 | akhaliq；Akatz Labs、MiniMax与上游作者；[固定模型卡](https://huggingface.co/akhaliq/MiniMax-H3-Image-Character-Swap/blob/6325127294249867672d816daaba1e141bcae23f/README.md) | 11-14 17:55建立；11-15 03:58更新 | 模型卡主要使用／评估章节；未看示范或执行 |
| 贴吧实践讨论 | [跨模型画师串：保留候选与原图未知项](#n11) | 画风探索·提示词组织｜阅读社区对跨模型画师串与LoRA候选的讨论。 | 设计思路：特征拆解·候选探索｜从色彩、光效和人物画法拆特征，再区分候选与原配方。 | 安晴Ankii；situhoyi、茅大叔等吧友；[原讨论](https://tieba.baidu.com/p/11196049272) | 2026-11-14 14:50首发；本轮读14楼 | 首楼与可见楼层文字；例图／楼中楼未看 |

## 当日分享

<a id="n01"></a>

### MOSS Serenity v7：姓名身份续训与场景提示分开

**适用方向：人物生成·后训练选型｜查阅身份续训、提示格式与全量模型的取舍。**

**设计思路：身份与场景分写｜以姓名触发身份，另写景别、服装与环境。**

- 原作者与原文：malcolmrey，[MOSS Serenity](https://huggingface.co/malcolmrey/moss-serenity/blob/4db08d3832bc98ae58ddb9d930b50e32a7584f7b/README.md)，固定版本`4db08d3832bc98ae58ddb9d930b50e32a7584f7b`。仓库2026-10-19建立，11月14日23:24更新；当前卡片为v7／250000步，本库首次专题收录，未取得v7权重首次上传时间，不把此次卡片时间当训练完成日。
- 原作者分享：面向按姓名学习人物身份的MOSS-Image Base全量微调路线。训练说明进一步限定为42个joint blocks的Linear权重（4.76B／5.08B参数），文本适配器、norm等冻结，并非全参数都更新；v7由分阶段续训而来。公开batch1、512面积桶、固定lr1e-5、EMA0.999、prior preservation和类别照片正则等个人训练条件，未独立复核训练日志。
- 使用方法：caption形如`photo of <trigger>, a woman/man, ...`，用无空格姓名触发身份，外貌、表情、景别、服装、场景与光线另写；作者指出远景小脸和同类多人物可能身份趋同。此为该模型经验，不推广为所有多主体的规律。
- 公开生成配置分列：完整检查点加Base用DMD适配器1.0时，作者8步／CFG4／Euler/simple／SLG层22、0–0.5；不用DMD时50步／CFG4。另一路是原始Base加SVD提取Serenity LoRA，作者用12步，不将三路设置拼接。编码器Qwen3.5-9B，FLUX.2 VAE。
- 文件差异：最新v7为INT8 ConvRot，卡片中“最新BF16”仍是v5；不同版本不能仅凭精度名视为同权重。r64／128／256提取LoRA保留的是部分微调差量，也不等于完整v7。
- 读取状态：[生成文档](https://huggingface.co/malcolmrey/moss-serenity/blob/4db08d3832bc98ae58ddb9d930b50e32a7584f7b/docs/generating.md)全文；卡片介绍、文件、提示、提取LoRA和训练章节，以及[训练说明](https://huggingface.co/malcolmrey/moss-serenity/blob/4db08d3832bc98ae58ddb9d930b50e32a7584f7b/docs/training.md)设置／数据组织段。未逐项读取完整人物表、图库或权重，未运行训练／生成。本文的设计标注依作者文字。

<a id="n02"></a>

### HaDeS MOSS v1.0 Turbo：QwenLook融入与八步条件

**适用方向：模型选型·少步生成｜区分内置蒸馏与QwenLook合并后的使用条件。**

- 原作者与原文：HaDeS，[HaDeS MOSS v1.0 Turbo](https://huggingface.co/DeVilDoNia/HaDeS-MOSS-v1.0-Turbo/blob/1e11fcfe2aaf10062fe7b5086d6cdce36129ca51/README.md)，固定`1e11fcfe2aaf10062fe7b5086d6cdce36129ca51`，11月14日06:08建仓、18:49更新。接续[11月12日v0.9.4记录](../2026-11-12/README.md#n02)，本次明确配方与评估变化。
- 作者说明：Base加自有Turbo 8-steps v1.0强度1，以及QwenLook Base强度1，已融合进扩散检查点；不额外再叠Turbo。QwenLook为rank32、1000步、1024尺度，作者称由1833张Qwen-Image-Edit2509处理的MOSS场景训练，当前未单独发布。训练适配器与合并整模分别记载，不称整模重新全量训练。
- 该卡参考设置：1344×1792、8步、CFG1、Euler/simple、shift5、SLG关闭，Qwen3.5-9B INT8 ConvRot编码器与`flux2-vae.safetensors`。只含DiT；BF16与INT8 ConvRot为同一版本不同精度导出。作者另提其他CFG／分辨率印象，但明确未作同等测量。
- 对比边界：作者在20条提示、每条一个seed的盲排中偏好v1.0为16／20，不等于普遍成功率。锐度指标变高不自动证明更写实；文中自动评判与作者主观感受不同，均保留为原作者报告。量化配对中也有道具／小细节变化，不能许诺逐像素一致。
- 读取状态：完整模型卡、来源与文件哈希字段；图库和manifest、加载器代码本轮未打开，未下载模型或复跑。沿用原许可入口阅读各上游条件，本文只作摘要导读。

<a id="n03"></a>

### PrismPalette ANIMA v3：脸部轮廓与清透光感

**适用方向：人物插画·画风选型｜参考Anima合并模型的光色与人物表现。**

**美术风格方向：清透日漫·柔亮体积｜两例圆润脸形配大亮眼，细肩轮廓与明净光色突出人物。**

- 原作者与原文：Noginowa，[PrismPalette ANIMA v3](https://civitai.com/models/2750408?modelVersionId=3469753)，11月14日14:00:22发布；[HF固定模型卡](https://huggingface.co/Noginowa/PrismPalette-ANIMA/blob/c0190d1094ded3f517d730fef156618dcb61d7e5/README.md)为`c0190d1094ded3f517d730fef156618dcb61d7e5`。仓库本身7月建立，v3日期来自精确版本，首次收录不混淆两者。
- 原作者分享：v3调整面部轮廓与整体细节，合并PrismPalette v2、Ribeye-Mix v1.0、FiaMix Anima Reboot Cute v1.7，并列Anima Detail Tweaker两项；没有公开本轮可核的完整分块比例，不补造配比。感谢原作者对上游的署名，本库保留其谱系入口。
- 通用推荐：CFG4–5（推荐4.5）、20–40步（推荐32），ER SDE／Beta；想柔和可考虑Euler A／Normal。编码器`qwen_3_06b_base.safetensors`、Qwen Image VAE。正负提示与工作流入口在卡片中；这些是作者建议，不是两张图的已核实值。
- 本库实际看图：[示范01](https://huggingface.co/Noginowa/PrismPalette-ANIMA/resolve/c0190d1094ded3f517d730fef156618dcb61d7e5/images/SampleImage_PrismPaletteANIMA_v3_01.jpeg)与[示范02](https://huggingface.co/Noginowa/PrismPalette-ANIMA/resolve/c0190d1094ded3f517d730fef156618dcb61d7e5/images/SampleImage_PrismPaletteANIMA_v3_02.jpeg)。两例圆润脸颊与收窄下颌、大圆眼和多层虹膜高光、小鼻口、脸红与张口笑；第二例有眨眼。可见细肩、纤细手臂与柔和躯干体量，发束亮边和窗光／林间透光突出主体，背景器物与植物较密。均为局部／半身取景，不推断全身头身与腿部比例；发色、服装和这次表情属于示范内容。
- 读取范围：模型卡全文、Civitai版本时间／变更与两张原示范；未看v2/v3整组对比图、未取图像元数据、未测合并兼容或实际收益。仅按这两例概括表现，不断言全部角色都相同。模型使用遵循所列CircleStone非商用许可与上游条件。

<a id="n04"></a>

### Krea2 PixelArt 16×16：单图标与四宫格的不同配方

**适用方向：游戏素材·像素图标｜区分单图标与四宫格适配器及网格提取。**

**美术风格方向：低分辨率像素·深色轮廓｜已看示范以阶梯轮廓、少量色阶和独立小物造型为主。**

- 原作者与原文：Angais，[Krea 2 PixelArt 16x16](https://huggingface.co/Angais/Krea-2-PixelArt-16x16/blob/1dff5939eae63cb42b7bdf3a389a602c348c2675/README.md)，固定`1dff5939eae63cb42b7bdf3a389a602c348c2675`；仓库10月16日04:43建立，11月14日18:28更新。为近期首次收录，未核两枚权重各自首发时间，不统称当日新训练。
- 作者公开方法：单图标与2×2表格各用一枚LoRA，二选一。单图以`pixel art 16x16 game icon`开头；表格明确左上、右上、左下、右下的对象与单色洋红背景。洋红保留为透明色键，不能同时要求洋红主体。
- 配方须分运行器：Diffusers单图例是Krea2 Turbo、512方图、8步、guidance_scale0，再从32像素块中心取样得到16×16。stable-diffusion.cpp四宫格例另用IQ4_XS、5步、text CFG1、特定噪声日程与作者所列Wan2.1 VAE；不能将此VAE／引导值直接套为ComfyUI默认。
- 四宫格先分成四个256方区，各区按16像素格取中心值，再色键透明；作者提醒轮廓可能相接、颜色有时偏暗。单图训练公开550张合成图放大32倍、rank/alpha32、1000步等；79／80色键成功属于作者样本统计，本库未重算。
- 本库实际看图：[透明小物合集](https://huggingface.co/Angais/Krea-2-PixelArt-16x16/resolve/1dff5939eae63cb42b7bdf3a389a602c348c2675/examples/sprites-transparent.png)与[四宫格原图](https://huggingface.co/Angais/Krea-2-PixelArt-16x16/resolve/1dff5939eae63cb42b7bdf3a389a602c348c2675/examples/sheet-iq4-xs.png)：深色粗轮廓、硬边阶梯、紧凑剪影，少量高光／暗部色块表达物件体积。观察限于图标与这一张原始表格，不涉及人物画法。
- 读取状态：模型卡全文、两张示范与公开代码片段；未运行图像提取或生成。原生输出是512方图，需要后处理才成为精确16像素图标；LoRA许可与作者所列数据许可分开查阅。

<a id="n05"></a>

### Celestial Ink：光感、尺度与墨线的分工

**适用方向：画风搭配·构图设计｜参考Krea2多LoRA的职责和视觉焦点组织。**

**设计思路：光感·尺度·墨线分工｜以小人物和巨大景物建立尺度，用单一红色焦点引导视线。**

- 原作者与原文：backrnin733，[Celestial Ink on Krea 2 Turbo — full ComfyUI recipe](https://civitai.com/articles/38855)，11月15日02:00:33发布。作者明确感谢各LoRA作者，本文是对其组合方法的概述。
- 方法要点：Niji Aesthetic承担光感，Pulp Cosmos承担巨大景物与绘画体量，monmon＋Hollow Void承担细线和半调颗粒；提示先场景／景别，再统一材质句，最后光色与单一绯红物件。小人物与巨大天体／建筑形成尺度，青绿、灰粉和金色中留一处红焦点，是这套设计的取舍，非所有画面必须一处红色。
- 作者原配方依次是Niji Aesthetic v2.0（版本3427089）0.7，Pulp Cosmos v1.0（3407270）0.7，monmon（3305239）0.5，Hollow Void（3219631）0.5，TextFusion v2 Full Rank（3416242）1.0。触发`@Aesthetic2rough`与`m0nm0n.`；各资源直达链接在原文中。
- 公开设置：Krea2 Turbo INT8 ConvRot、作者指定Qwen3-VL-4B修改版编码器、Qwen Image VAE，LoraLoaderModelOnly串联，Euler/simple、8步、CFG1、1024×1536、无负向、无hires fix。本文保留原文条件，不将它与原版编码器的经验拼为同图实值。
- 作者比较固定提示／seed下三组权重，另比是否加TextFusion；前三个数字分组对应前三项权重，Hollow Void与第五项仍另列，不把五枚简写成三枚。文中也承认飞行员位置偏到前景、假签名和场景文字问题；作者提出换seed等个人处理办法，未证明单枚LoRA独立收益。
- 读取状态：正文全文及三条示例提示／seed文字，未取得工作流JSON、成图元数据或实际看示范图。故以设计思路概括，画风细节依作者描述，未做人物体型归纳或本库复跑。

<a id="n06"></a>

### Anima LoRA“可加载但效果不对”：先核层数映射

**适用方向：Anima兼容·LoRA排错｜区分28／40／52层映射与实际效果验证。**

- 原作者与原文：Nausamedu，[ComfyUI — Non functioning LORAs when using ANIMA (fix)](https://civitai.com/articles/38844)，11月14日18:25:33；感谢帖子所致谢的Johnsmithsomehing与Mraclet提供线索。文章的新分享与旧工具本轮补读分开记录。
- 作者经验：LoRA能加载并跑完，却无效果或表现异常，可能涉及Anima扩层版本的块索引错位。文中给手动节点和启动补丁两条路线，不是以“加载成功”证明资源已正确作用。
- 上游核读：[INuBq8统一LoRA／LLLite补丁](https://github.com/INuBq8/ComfyUI-Anima-LoRA-ControlNet-Patch/tree/b25ae637102f2358116fe419a409f0594f61245b)，固定提交`b25ae637102f2358116fe419a409f0594f61245b`（9月9日）；[shin131002手动Remap节点](https://github.com/shin131002/ComfyUI-Anima-Remap/tree/ad6a2c4af587b434f452932a0b1cb67199dcbdc5)，固定`ad6a2c4af587b434f452932a0b1cb67199dcbdc5`（9月29日北京时间）。均不是今天新发布工具。
- 文档说明28／40／52层已知架构间的索引映射。统一补丁保持标准节点、通过日志反馈；手动项目另有LoRA／合并／控制节点。映射表的社区来源和前序工作归于其原作者，本库没有下载真实权重复核tensor相等。
- 实用边界：只覆盖部分低层键的适配器可能被误判来源；未知结构、CLIP侧修正等不在统一补丁范围。扩到新增块的实验工具与运行时映射不同，不能把“填入新层”当效果更好。多套旧补丁／同名节点可能冲突，不能机械同时装。
- 读取状态：文章全文，统一补丁的机制、跳过条件、已知限制／实验区分，以及手动项目介绍与迁移说明。原文“NVIDIA限定”只是帖子推测，本轮未核硬件矩阵，不作平台限制结论；没有安装、加载、核哈希／完整源码或成图验证。

<a id="n07"></a>

### Libretto：预设、场景与已用工作流的关联

**适用方向：提示词组织·场景复用｜用可视预设编排人物、服装和环境条件。**

**设计思路：预设与场景分层｜复用人物服装等组件，保留每次场景与提示快照。**

- 原作者与原文：higeneko9，[Libretto: A Visual Prompt Builder for ComfyUI](https://civitai.com/articles/38838)，11月14日15:12:30发布；所指[v0.26.1111.2](https://github.com/Higeneko9/Libretto/releases/tag/v0.26.1111.2)实际11月12日12:01:23发布。固定README提交`aff5d0d67a80b85b7b67ae6f133005d01738aa89`，不将新介绍帖当软件新版本。
- 方法：把人物、服装、姿态、地点与灯光做可复用预设，再组织成场景；编辑场景节点与修改原预设分开，避免无意改动库。可选随机／权重／顺序集合，预览编译提示，多角色属性归属也属于文本编排。
- 接入边界：Libretto负责提示和设置，仍需单独可用的ComfyUI、模型与工作流。README声明支持KSampler文生图，导入时可展开子图，不支持只有放大或3D的图；更改服务器工作流后要重新导入。角色分段不等于模型层面的区域隔离。
- 可借鉴维护：结果保存所用提示、seed、工作流和环境快照，区分恢复场景与按保存图重新排队；“Regenerate exactly”仍依赖模型、GPU与运行版本相符。v0.26.1111.2修复桌面缩放后的画布平移，不夸大为模型效果升级。
- 读取状态：介绍正文、[固定README](https://github.com/Higeneko9/Libretto/blob/aff5d0d67a80b85b7b67ae6f133005d01738aa89/README.md)的使用、配置快照与许可段，以及release说明；未观看英日演示、看界面图、下载安装包或连接生成服务。软件MIT，模型与其他素材条件另看原作者说明。

<a id="n08"></a>

### Batch Builder：提示行、采样seed和通配符分开

**适用方向：批量编排·提示词组织｜对齐逐行提示、种子与通配符的展开结果。**

- 原作者与原文：ThedDryz，[comfyui-batch-builder](https://github.com/ThedDryz/comfyui-batch-builder/blob/3f222f8567f8f1ceb3af076c04efba571ab09948/README.md)，11月14日15:48建立，固定提交`3f222f8567f8f1ceb3af076c04efba571ab09948`为19:49。
- 作者功能：Character Definition按部件切换文本；Seed List产生种子表；Builder逐行组合固定前后缀、booru标签、自然语言与角色文本，对每行展开若干seed，再排下一行。空行计入行号，长度不齐会补空并报告；不能把行号与忽略空行后的条数混用。
- 接线要点：提示、负向通配符处理与采样器使用Builder输出的同一seed列表；另有hires种子时用Batch输出对齐数量。文本字段为节点本地输入，不接普通STRING连线。宽高是逐行列表，缺值回退／尺寸取整会报告，仍要符合目标模型自己的尺寸条件。
- 随机职责：相同seed通常稳定对应通配符结果；开启Vary wildcards后可在相同采样seed重复项上改变文本选择，用于分开看提示与噪声因素。它使用自有花括号语法，不支持Impact的`__file__`。
- 自动化边界：queue batch count按作者设为1，浏览器扩展在当前任务成功后推进，错误／取消停止；只经API排队不会自动逐行推进。简介的“自动”不等于独立服务器调度器。
- 读取范围：固定README全文；未看全部源码、注册节点、执行测试／排队或自动生图。本条为功能导读，不新增本库自动实验。

<a id="n09"></a>

### K2-Editorial v1.12.0：完整母题与有限替换

**适用方向：Krea2提示·主视觉设计｜保留母题整体结构，再替换角色、服装与文字。**

**设计思路：母题整块·有限替换｜统一构图、材质、光位和排版，避免随机片段互相冲突。**

- 原作者与原文：灵冻不冻，[Krea2白垩光长文提示词自动装配教程](https://www.bilibili.com/video/BV1jTs56wEEt/)，11月14日20:49:21；[Comfyui-K2-Editorial](https://github.com/lingdongbudong/Comfyui-K2-Editorial/blob/5a0c3fda62b6c50af153b14a86449393384802a5/README.md)，固定`5a0c3fda62b6c50af153b14a86449393384802a5`，README标v1.12.0。提交时间18:30，仓库18:36建立，时间分别保存。
- 原作者方法：把25段长文的母题作为整体，保留其构图、材质、光位和版式，只换身份、画幅、服装、单品与画内文字。scene／poster／short三类分支长度与组织不同，不是把395条全部随机拆碎；角色数、词数和母题数描述库规模，不单独证明画质。
- 输出边界：只产生提示词、自检报告、元数据三个STRING，不调用模型或直接生成图。其画幅建议是文本／工作流编排的一部分，不能只改提示词就认定采样latent尺寸已同步；完整接线与实际有效参数仍须看具体图。作者列ComfyUI0.42.x与Python3.10+条件，示例工作流另有XB_ToolBox依赖说明，未由本库运行验证。
- 来源与尊重：README将提示母题素材归于辞雪沐春，角色数据／缩略图来自Anima-Wardrobe-V6；代码AGPL-3.0与上游素材许可不是一回事。作者写口头允许再分发但未指定独立许可，使用原文与角色素材应各自依说明处理，本文不打包再分发素材库。
- 读取状态：SDK完整简介、作者／日期／单P时长，以及项目README全文；视频1042秒，未取得章节／平台字幕，本轮没有盲目全量下载。未看视频画面、网盘配置、母题全集与最终编码文本，也未新装节点或出图；本条按明确的作者文字总结设计方法。

<a id="n10"></a>

### H3 Image Character Swap：视频适配迁移到图片的边界

**适用方向：角色替换·参考图编辑｜按场景与角色两路输入组织H3图片替换。**

**设计思路：身份与场景分工｜明确替换对象，分别要求保留角色特征与原场景条件。**

- 原作者与原文：akhaliq，[MiniMax-H3-Image Character Swap](https://huggingface.co/akhaliq/MiniMax-H3-Image-Character-Swap/blob/6325127294249867672d816daaba1e141bcae23f/README.md)，固定`6325127294249867672d816daaba1e141bcae23f`；11月14日17:55建仓，本次API记录最近修改为15日03:58。上游适配器作者为[Akatz Labs](https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA)，底模来自MiniMax。
- 分享性质：将视频角色替换LoRA v1.5转到H3图片DiT并以强度1融合，也提供单独适配器。40GB整模不是40GB LoRA；不是在本仓库重新训练图片底模。作者说明合并数学／键形状检查与少量实际图例，不能以此替代广泛兼容或身份稳定性评估。
- 提示职责：场景作Picture1，角色参考作Picture2；明确目标人物，并分别写脸、发型、服装与需要保留的背景、光线、其他人。姿态／视线默认跟原场景，极端侧脸可能别扭；它不是把参考原姿态原样贴入画面。
- 作者的Comfy路径：0.45.0+、模板包0.11.104+，Euler/simple、6步、CFG1、denoise1；合并检查点与独立LoRA二选相应接线，不重复叠同一适配。作者同时明确端到端示范主要在Diffusers验证，Comfy文件为对应布局导出，不把数值映射核验冒充ComfyGUI实跑。
- 适用边界：原LoRA为视频训练，模型卡只列8种难例；小脸、遮挡、极端姿态和跨画风身份保持仍需逐图观察。没有原示范可核的本库观察，不采纳“所有场景都保持”的广告式结论。
- 读取范围：固定卡片介绍、FAQ、Comfy／Diffusers使用、合并说明与限制／署名；示范图、测试集、完整工作流和实现未继续读取。未下载权重或生成；许可依MiniMax原协议及适配器条件查阅。

<a id="n11"></a>

### 跨模型画师串：保留候选与原图未知项

**适用方向：画风探索·提示词组织｜阅读社区对跨模型画师串与LoRA候选的讨论。**

**设计思路：特征拆解·候选探索｜从色彩、光效和人物画法拆特征，再区分候选与原配方。**

- 原作者与原文：安晴Ankii，[有人尝试过用开源模型还原novelai v4.5的画风吗](https://tieba.baidu.com/p/11196049272)，stablediffusion吧，11月14日14:50:55。aiotieba读取第1页14个可见楼层（楼层号有跳号），不称完整所有楼中楼。
- 分享内容：楼主描述在NoobAI／Anima下尝试画师标签的困难；吧友讨论同名标签、模型支持与加权写法不能直接互换。situhoyi建议从配色、明暗、发束附色、轮廓线、眼睛和体量等特征分解，11楼给一串候选；茅大叔15／16楼补充多项LoRA名称。
- 本库概述：先保留实际可见的画法特征与不同资源的候选关系，避免把模糊的“像某模型”当配方证据。11楼有`0.2::...::`等原平台语法，未确认其模型／解析器时不改写成Anima可直接运行权重串；候选LoRA只保留原楼层入口，不猜具体Civitai版本。
- 证据边界：楼主对原图底模的推测、吧友对“唯一解”的判断与资源近似建议均为社区意见；本次未看原图、取得元数据、验证候选模型或找到原图作者配方，不认定是NovelAI默认风格或声称已还原。此处写设计探索方法，不给具体风格视觉结论。
- 另读的[Krea2能否用Illustrious LoRA讨论](https://tieba.baidu.com/p/11194949960)有互相矛盾的反馈、未给可核日志与有效键；只记来源覆盖，不据“有变化”断言跨架构权重兼容。提示词本身变化和适配器真正生效必须分开。

## 实际平台覆盖与未精选线索

| 平台／入口 | 本轮实际读取 | 结果／限制 |
|---|---|---|
| stablediffusion吧 | aiotieba4.8.2，CREATE第1页30项；置顶分开后新帖跨过上次窗口；补读3个候选主题 | 画师串讨论入选；跨架构LoRA兼容帖12楼相互矛盾、缺日志；[裙摆蕾丝问题](https://tieba.baidu.com/p/11196857990)仅读首楼，无确认解决方案，不作有效教程。列表不是正文全读。 |
| comfyui吧 | 同工具CREATE第1页29项，剔除2024旧置顶；本轮窗口2条新主题；读[官方／整合包区别](https://tieba.baidu.com/p/11196398536)首楼与一回复 | 已读候选仅为新手问答，未取得具体工作流或新方法；另一新主题为下载推广未精选，不称全吧没有更新。 |
| 吧名与全站补充 | 空格别名`stable diffusion`实测仍转至无关`stable`公告，实际使用stablediffusion；全站最新“工作流 提示词”第1页30项 | 逐帖核吧名、tid和首楼日期，其他吧／推广不冒充两吧覆盖；未启用Astron或检查备用依赖。 |
| bilibili广泛发现 | SDK17.4.2，pubdate；“ComfyUI 教程”3页各20项，页3已到11月14日00:27，跨过上次窗口；“生图 模型”“Anima”“LoRA 画风”各1页20项 | 类别词有限，按BV去重，过滤整合包／无关音乐与重复。完整简介读取K2-Editorial及[余小文AIGC《MOSS+Krea2双采工作流》](https://www.bilibili.com/video/BV1nVsV6MECx/)；后者51秒、简介无可核双阶段设置，保留线索，不把风格宣传拼成配方。 |
| Sena404 | UID341674866最新投稿调用NetworkException；Anima最新搜索仍出现已收录BV1RFWi6HEjd | 水位保持投稿第27期／片内第37期；没有新一期可确认，不能因关键词没命中声称作者无更新。未重复取得旧媒体或启用备用。 |
| B站深读状态 | 当前没有已配置会话；本轮精选长视频1042秒，正文方法转读作者GitHub说明 | 未取得章节／平台字幕／本轮视频画面、OCR或ASR；未盲目全片下载，不复用旧视频读取范围冒充新视频已读。现有FFmpeg／OCR方案按需保留，没有重装或新服务。 |
| Reddit | r/StableDiffusion new50、r/comfyui new30均403；两条日期／类别站内查询，再打开[optimisticalish 11月12日MOSS资讯帖](https://www.reddit.com/r/comfyui/comments/1xu4bgx/a_quick_mossimage_news_roundup_12th_november_2026/) | 资讯正文可读，列出相机焦点工作流、动漫转写实等补查入口；只存导读链接，未逐项跟读或提升为当日新资源。原标题有11月12日，页面只有相对时间，原帖精确时刻未核；评论／图未读。最新列表限制仍保留。 |
| Hugging Face | text-to-image最近修改80项、image-to-image30项；读取Serenity、HaDeS、PrismPalette、PixelArt、H3 Swap等固定卡片与必要文档 | 量化／镜像／课程作业不重复当新模型；Karume Anima只读转换容器、默认模式与使用段，属已有官方模型WebGPU导出，不称新训练。本轮仅Prism两图与Pixel两图实际看过。 |
| GitHub | 工作流／节点更新25项，提示相关新仓库15项；继续追作者说明中的项目 | Batch Builder全文、K2-Editorial全文；Libretto使用与版本、两个Anima映射项目相关章节；其他候选按实际读取筛除，OpalFruit短README只有功能列表，无足够细节。未安装、测试或源码审计。 |
| Civitai社区 | 最新模型40项、文章30项、工作流15项；打开文章、Chiaroscuro与Prism精确版本 | 文章／教程、模型／版本和工作流列表均实际查过；[Chiaroscuro Moss SFT](https://civitai.com/models/3052050)作者写两LoRA合并，但缺可核比例／对照，本轮仅作候选。首次训练感想文章内容偏个人经历，未强行当配置教程。未读全站评论或全部作品配方。 |
| 其他论坛 | ComfyUI Forum最新30主题列表及[论坛下线公告](https://forum.comfy.org/t/4909)正文；note.com近期ComfyUI入口403 | Forum新公告值得来源维护关注：标题写11月18日，正文两处写11月20日且称帖子将下线；日期存在冲突，保留原帖，不据标题替正文下定论。正文建议社区问题转Discord、产品问题转对应GitHub；本轮未加入或访问Discord。note.com是访问受限，不写无优质新增。 |

## 后续关注与维护记录

- 模型侧跟进Serenity完整v7与提取LoRA的差异、HaDeS v1.0及量化的真实条件；卡片实验均为作者报告，不提升为本库测量。
- PrismPalette v3已核精确版本日期；PixelArt和Serenity原仓库较早，保留首次收录口径。工具侧新介绍帖不重置旧release日期。
- 对Anima映射先核具体源／目标架构和既有补丁，再谈兼容；贴吧跨架构“有变化”的讨论不替代有效键和实际分支证据。
- K2-Editorial长视频本轮正文已从作者README获得，简介及时归档；需要时再读指定时间段／配置，不能把完整简介写成已看完整视频。Sena水位保持第27期。
- ComfyUI论坛公告的标题／正文时间不一致，后续直接核原帖变化与可用替代入口；本次没有迁移固定来源或新增服务。
- 本页先保存，随后更新总索引、首页和每日入口。没有安装、模型下载、生成／自动实验、新测试体系或子代理派发；图片、媒体、完整转录与临时签名地址不入库。

[返回总索引](../../每日检索可速查总结.md) · [每日归档说明](../README.md)
