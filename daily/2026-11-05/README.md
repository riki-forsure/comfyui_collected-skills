# 2026-11-05 每日社区发现

感谢社区作者公开分享模型、教程与实践经验。本页为本库摘要整理，保留作者署名和原文入口，欢迎回原帖阅读完整内容与更新。

- 北京日期与开始时间：2026-11-05 03:57起。
- 检索类型：每日广泛发现，无具体差距要求。
- 执行状态：进行中，已归档首批3项；继续整理其余已读资料和平台覆盖。
- 时间窗：优先自11月4日各平台成功快照之后至本轮查询时点的新增与实质变化；旧版本首次收录保留原始日期，当前提交不自动称为首发。
- 本次仅阅读与汇总，未安装节点、下载大模型、运行生图或实验，未派发子代理。

## 今日值得阅读

- [Krea2 Turbo三步LoRA](https://huggingface.co/lvladikov/Krea2-Turbo-Distill-3step-LoRA)：公开文件格式与采样条件，并区分去噪时间和完整流程时间。
- [cocoamixMOSS](https://civitai.com/models/3035448?modelVersionId=3451079)：可查普通／Turbo／量化版本及作者的眼睛、配色提示，混合与训练明细仍有缺口。
- [Illustrious三人构图词](https://civitai.com/articles/37976)：人数之外考虑角色间距、前后景与互动关系。

## 分享速查

| 类别 | 分享／资源与版本 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点／可学习经验 | 读取状态 |
|---|---|---|---|---|---|---|
| 后训练／少步蒸馏LoRA | [N01 Krea2 Turbo三步LoRA：区分采样提速与完整流程耗时](#n01) | 少步生成·Krea2适配器｜查阅三步蒸馏的文件格式、采样条件与取舍。 | — | [lvladikov；基座Krea团队](https://huggingface.co/lvladikov/Krea2-Turbo-Distill-3step-LoRA) | 作者从既有四步适配器继续训练三步LoRA，提供Diffusers与ComfyUI键名两种文件；两者属于同一适配器，三步提速不包括编码和解码。 | 固定revision发布说明、Files与ComfyUI等前约10000字符；检查点说明全文；未读训练后半、工作流JSON或示范图。 |
| 混合检查点／MOSS画风 | [N02 cocoamixMOSS：区分普通、Turbo与量化版本](#n02) | 人物插画·模型选型·MOSS｜区分普通与Turbo配方，查看眼睛和配色写法。 | 美术风格方向：细线萌系·柔和渐层｜本例圆脸大眼、眨眼笑，发束高光与白色褶饰突出。 | [ccooccoo](https://civitai.com/models/3035448?modelVersionId=3451079) | 作者以MOSS、自训模型与少步适配器做混合发布，提供普通与Turbo路线，并说明瞳孔和鲜艳配色的提示；量化另为文件版本。 | 模型说明与前三个版本元数据；实际看147939778一张例图，未取得该图参数或训练配方。 |
| 提示词／多人构图经验 | [N03 Illustrious三人构图：人数词与群体姿态词的区别](#n03) | 多主体关系·构图·Illustrious｜比较群体姿态词对三人前景与间距的影响。 | 设计思路：人数与站位关系｜人数词之外补充并排、靠头或排队等空间关系。 | [shyamalan](https://civitai.com/articles/37976) | 作者在Illustrious中按每词8次生成记录三人前景的出现次数、间距和互动倾向，展示群体姿态词并非同义替换。 | 文章正文全文；未看例图、未取得精确检查点和完整提示／seed。 |

## 当日分享

<a id="n01"></a>

### N01 Krea2 Turbo三步LoRA：区分采样提速与完整流程耗时

**适用方向：** 少步生成·Krea2适配器｜查阅三步蒸馏的文件格式、采样条件与取舍。


- 原作者与原文：[lvladikov《Krea 2 Turbo — 3-Step Distillation LoRA》](https://huggingface.co/lvladikov/Krea2-Turbo-Distill-3step-LoRA)。首次收录；当前revision `885b61599dd1c152f293ad0bc52426a8a8ac4a42`，提交2026-11-05 03:32:47 +08:00，非首发时间证明。
- 作者分享要点：在Krea2 Turbo上做三步蒸馏，从已发布四步LoRA权重开始；rank64、228模块。作者报告22条测试提示上的细节指标与采样时间，称训练仍在继续。细节统计高于教师不等于整体画质更好，结果也不等于保持教师原图构图。
- 公开配置：ComfyUI使用 `krea2_turbo_3step_rank_64_lora_comfyui.safetensors`，作者设置3步、CFG1、Euler/simple、LoRA1.0；Diffusers文件仅键名不同，不能同时加载两枚当作额外增强。卡片将Diffusers guidance_scale0与ComfyUI CFG1对应，不能把0照搬到ComfyUI。
- [检查点说明](https://huggingface.co/lvladikov/Krea2-Turbo-Distill-3step-LoRA/blob/885b61599dd1c152f293ad0bc52426a8a8ac4a42/krea2_turbo_3step_rank_64_lora_checkpoint_info.md)全文已读：当前两文件对应chk00066000；历史chk00042000等另在_archive，不由不带编号的文件名判断版本。
- 条件与边界：作者的2.6倍提速仅指去噪，不含文本编码／VAE解码；训练目标为Turbo。Raw段为作者额外尝试，不当作受支持的通用兼容模式。文件列有Krea2社区许可与NOTICE，使用回原页核对。
- 读取范围：固定revision前约10000字符，涵盖发布说明、文件、Diffusers／ComfyUI用法及Raw试验入口；未读后半完整训练过程、下载权重、看样图或复跑。

<a id="n02"></a>

### N02 cocoamixMOSS：区分普通、Turbo与量化版本

**适用方向：** 人物插画·模型选型·MOSS｜区分普通与Turbo配方，查看眼睛和配色写法。

**美术风格方向：细线萌系·柔和渐层｜本例圆脸大眼、眨眼笑，发束高光与白色褶饰突出。**

- 原作者与原文：[ccooccoo《cocoamixMOSS (moss image)》BF16_turbo_v1.0 / 3451079](https://civitai.com/models/3035448?modelVersionId=3451079)，2026-11-05 03:21:47.601 +08:00。另有BF16_normal_v1.0 / 3449076（11月4日05:07:23.110）与int8_turbo_v1.0 / 3451120（11月5日03:12:12.297）。
- 作者说明：发布形式为混合检查点，成分概述为MOSS、自训模型，Turbo另含8-steps-dmd2-lora；没有公开精确混合比例与自训明细。不将它写成已证实的纯全参数微调，也不把int8版另计独立新训练。
- 作者通用用法：Turbo约10步，CFG1–4，可参考er_sde/simple、Euler/normal等；普通版50步、CFG4、er_sde/simple。旧文档的13步／0.65 LoRA组合另列为历史写法，不与当前Turbo默认混成同一配方。
- 作者文字称常规画法不出现瞳孔，给出 `eyes has dark_circle shaped pupils`；鲜明配色给 `vivid dark color`。这是其用法提示，不代表本库已验证效果或例图使用了这些词。
- 本库实际看图：[147939778](https://civitai.com/images/147939778)一例，近距离俯视的猫耳女仆举起猫爪与包装盒；圆润脸、大虹膜、眨眼与张口笑，头发分束高光、柔和肤色及衣服硬边阴影并存。猫耳、猫爪和女仆服属于本例设定，俯视比例不推为模型固定体型；未取得该图提示／seed等元数据。
- 读取范围：模型介绍全文、前三版本说明／文件元数据及一张公开示例；未取得混合比例或训练数据，未下载权重。作者明确禁止商用并要求再分发／合并发布等先获许可；本库仅摘要与原链接，不转载模型或示例图。

<a id="n03"></a>

### N03 Illustrious三人构图：人数词与群体姿态词的区别

**适用方向：** 多主体关系·构图·Illustrious｜比较群体姿态词对三人前景与间距的影响。

**设计思路：人数与站位关系｜人数词之外补充并排、靠头或排队等空间关系。**

- 原作者与原文：[shyamalan《Tags for composing 3 characters》](https://civitai.com/articles/37976)，发布2026-11-04 09:53:53.418 +08:00，更新10:08:47.833；本次新增分享首次收录。
- 作者分享要点：单写3girls等人数词的该组记录为1/8；side-by-side、lineup、heads together等为8/8。作者同时记录人物间距、重叠和互动气氛；group photo与group picture在该组仅2/8。这里是作者小样本观察，不是全模型成功率排名。
- 可学习经验：并排／列队偏向前景并列，queue可把人物分散到不同景深，heads together让头部靠近；词语会同时改变关系和构图。triplets虽常出现三人，也可能使外貌相似，不能只以人数正确评价身份区分。
- 适用条件：原文仅说明用Illustrious，未给精确后训练版本、完整正负提示、种子、分辨率或参数控制，无法确认各词之外是否完全一致。不直接外推到Anima、MOSS或任意多主体数量。
- 实际读取范围：公开API文章正文全文；未看示例图／评论、未生成。本文为作者经验，本库整理用途与语义取舍，欢迎回原文查看完整词表。


## 来源覆盖与检索记录

本轮已分别执行两贴吧CREATE列表与全站补充搜索、bilibili最新排序搜索、HF更新／创建两组模型列表、GitHub近期项目检索、Civitai文章／模型近期列表；其他作者资料读取note的ComfyUI／Anima RSS。Reddit两社区最新JSON请求403，定向搜索主要返回旧帖；具体边界继续整理，不把其他平台内容替代Reddit最新覆盖。

## 后续关注与更正

首批已读内容先保存，其余资料继续增量整理；访问、正文读取、配置取得和效果验证分别记录。

[返回总索引](../../每日检索可速查总结.md)
