# 2026-11-17 每日社区发现

本页为社区公开分享的中文概述与导读，感谢原作者的创作、研究和经验分享。条目保留署名与原文直达链接，请前往原帖阅读完整教程、示范、许可和后续更新，支持原作者；链接及署名不等同额外转载授权。

- 北京日期与实际检索时间：2026-11-17，04:00起读取最新规则，04:01起逐平台检索并补读原文；归档前完成本页记录的阅读范围。
- 检索类型：无具体差距要求的每日广泛发现，本轮无另设主动专题。
- 执行状态：整理12项首次收录（含历史补录与相关不同路线），部分入口受限；未安装节点、下载生图模型、启动生成或实验、增加服务或派发子代理。
- 时间窗：优先接续11月16日各平台上次成功读取（约04:00附近）以来的新增及变化；临近水位的首次收录和历史资料分别保留原始日期。仓库最后修改时间不是训练或首发日期。
- 证据口径：作者说明、社区反馈、本库概述、看图范围和运行验证分别记录；标注帮助查阅，归档不等于成图或收益验证。

## 今日值得阅读

- **后训练与选型**：[Juggernaut专用DMD2](https://huggingface.co/Kandoo/Juggernaut-Moss-DMD2-LoRA-Beta)公开少步训练与取舍，[MOSS相机控制](https://huggingface.co/raspie/RS-CAMERA-CONTROL-MOSS)区分专用LoRA与tokens；Oboro Blink按NOTICE记为合并发布。
- **参考与设计**：[MOSS Charref v2](https://github.com/bag3labo/moss-image-edit-charref-v2)明确参考布局和失效例，[H3三色替换](https://huggingface.co/Alissonerdx/Minimax-H3-ComfyUI/blob/main/docs/character-swap-image-multiple-by-color.md)说明多主体映射；另补录AnyBokeh的焦点／景深编辑。
- **日常创作与实践**：摄影七栏提示、可控随机工作台、颗粒质感经验，以及训练资料管理和量化后端比较，均保留原作者条件与实际读取状态。Sena404 UID最新页可读，仍为已收录第28期，不重复计新增。

## 分享速查

| 类别 | 分享／资源与版本 | 适用方向（短标注） | 美术风格／设计思路 | 原作者与原文 | 分享要点／可学习经验 | 读取状态 |
|---|---|---|---|---|---|---|
| 专用蒸馏LoRA | [Juggernaut MOSS DMD2 Turbo Beta](#n01) | 采样加速·模型选型｜查阅Juggernaut专用少步适配与构图取舍。 | 设计思路：摄影提示分层｜按图像类型、场景、镜头、光色和材质组织自然语言。 | Kandoo／David Turbanisch；RunDiffusion、OpenMOSS及上游作者；[固定模型卡](https://huggingface.co/Kandoo/Juggernaut-Moss-DMD2-LoRA-Beta/blob/faa4cda706a8268a42227d80b707f74f1b58d73e/README.md) | 自行DMD2训练；INT8优先，少步伴随种子多样性下降 | 模型卡全文；未看例图／运行 |
| 相机控制适配器 | [RS-CAMERA-CONTROL-MOSS：42视角与配套tokens](#n02) | 镜头构图·视角控制｜了解MOSS专用机位适配器与配套词向量。 | 设计思路：机位离散控制｜将视角选择映射到已训练方向和对应条件。 | raspie；RS MultiCharacter Sampler、OpenMOSS作者；[固定模型卡](https://huggingface.co/raspie/RS-CAMERA-CONTROL-MOSS/blob/ff44cb77d159d94f1c13aa7e85f1b67882e12e87/README.md) | MOSS-SFT新适配，LoRA和camera tokens须成套 | 模型卡全文；未读节点源码／运行 |
| 模型合并／量化发布 | [Oboro Blink 1.0：Qwen2.1四步合并包](#n03) | 文字生图·合并模型选型｜查阅Qwen2.1四步包的组成与许可条件。 | — | biscet／Egor Prokhorov（Oboro AI）；Qwen、noctaluna、e-n-v-y、ausboss、LightX2V、dx8152；[模型卡](https://huggingface.co/oboro-ai/Oboro-Blink-1.0/blob/9b1aea1eb09db01828f9eb60dff7d2b6dccb74d0/README.md) · [NOTICE](https://huggingface.co/oboro-ai/Oboro-Blink-1.0/blob/9b1aea1eb09db01828f9eb60dff7d2b6dccb74d0/NOTICE) | NOTICE明确无新训练；多适配已合入，勿重复加载 | 模型卡和NOTICE全文；未看图／运行 |
| 历史特化LoRA／摄影编辑 | [AnyBokeh：分阶段估计与景深重渲染](#n04) | 摄影编辑·景深控制｜通过焦点与光圈调整已有照片的虚化层次。 | 设计思路：焦点与虚化分工｜先估计散焦和视差，再按目标光圈重渲染景深。 | Xinyu Hou、Xiaoming Li、Zongsheng Yue、Chen Change Loy；S-Lab／NTU、BFL；[固定模型卡](https://huggingface.co/itsmag11/AnyBokeh/blob/c5597da32fc5f64fdc9e495504a2f6d331fa1ae0/README.md) · [项目代码](https://github.com/itsmag11/AnyBokeh) | FLUX.1-Fill-dev两阶段LoRA；历史首次补录 | HF卡片及GitHub README全文；未看图／运行 |
| 角色参考LoRA／工作流 | [MOSS Charref v2：参考布局与场景提示分开](#n05) | 角色一致性·人物插画｜用单角色参考保身份，文本描述姿态与场景。 | 设计思路：身份与场景分工｜参考图提供外观，提示控制动作，另行选择风格适配。 | bag3labo；OpenMOSS、Comfy-Org及上游作者；[固定README](https://github.com/bag3labo/moss-image-edit-charref-v2/blob/1ab660fd372a9317370240c146e90bf2780a3c17/README.md) | 专用参考布局节点必须；公开失败例和评估边界 | README全文；未看图／读完整JSON／运行 |
| 提示组织节点 | [Krea2 Photo Prompt Builder：七栏提示与分类历史](#n06) | 提示词组织·摄影创作｜分栏复用主体、镜头、光线和后期描述。 | 设计思路：摄影提示分层｜主体外观与姿态分栏，镜头光线质感独立复用。 | magichan-lab；[固定README](https://github.com/magichan-lab/ComfyUI-Photo-Prompt-Builder/blob/22d787ad4ad78d639eee9076a7e488c79d445c7f/README.md) | 输出STRING而非CONDITIONING；分类历史需备份 | README全文；未读源码／运行 |
| 量化与后端实践 | [Krea2 FP8与INT8 ConvRot：4060Ti记录](#n07) | 资源选型·兼容排错｜结合显存余量和后端理解Krea2量化耗时。 | — | nontan_works；原讨论arrssenne及参与者；[原文章](https://civitai.com/articles/38967) | 特定Forge neo测量，FP8显存警告是重要混杂 | 文章全文与作者表格；未看比较图／日志原件 |
| 训练资料管理导读 | [LoRA Dataset Studio V2：从资料整理到挑档](#n08) | LoRA训练·资料管理｜查阅筛图、打标、训练与固定条件挑档流程。 | — | perfectgf；ComfyUI、ai-toolkit与各上游作者；[功能导读](https://civitai.com/articles/39003) · [源码入口](https://github.com/perfectgf/lora-dataset-studio) | 公共版与会员模型支持分开；相似度排名不代替审图 | 文章全文、仓库元数据；README未通读 |
| 贴吧工作台分享 | [Comfy Image Atelier：Anima与Krea2的可控随机](#n09) | 自动化工作流·提示管理｜固定角色条件，按模型组织随机池与历史。 | 设计思路：固定与随机分工｜角色服装可锁定，单独探索姿态、场景与表情。 | 无害的史莱姆pzy／159159pzy-crypto；Anima Tools及社区作者；[原帖](https://tieba.baidu.com/p/11200087842) · [项目](https://github.com/159159pzy-crypto/comfy-Image-Atelier) | 按模型拆标签／自然语言池；保留最终生成条件 | 首楼及可见11楼文字；未看图／运行 |
| 颗粒质感实践 | [胶片颗粒节点：分辨率与颗粒参数的关系](#n10) | 采样精修·摄影质感｜了解放大后添加颗粒时的强度与密度取舍。 | 设计思路：颗粒随尺寸调整｜先确定输出分辨率，再调颗粒强度与分布。 | 鉴纯夏desu；[原帖](https://tieba.baidu.com/p/11202473509) | 有用的调参经验；节点名与截图实值未取得 | 首楼及作者补充共2楼文字；图片未看 |
| 多主体替换适配／流程 | [H3 Image按颜色替换角色v0.1](#n11) | 多主体关系·角色替换｜用三色绑定参考角色，并明确表情与遮挡取舍。 | 设计思路：颜色绑定·表情补写｜按色区分主体，保留映射并逐人说明视线和表情。 | Round_Awareness5490／Alissonerdx；BFSNodes、Comfy-Org及上游作者；[Reddit原帖](https://www.reddit.com/r/comfyui_elite/comments/1xxm4nx/h3_image_lora_v01_swap_up_to_3_characters_in_a/) · [v0.1教程](https://huggingface.co/Alissonerdx/Minimax-H3-ComfyUI/blob/main/docs/character-swap-image-multiple-by-color.md) | 1–3角色三色绑定；主文件为训练适配的分层合并 | 原帖正文、HF教程全文；未看演示／读JSON／运行 |
| B站研发团队问答 | [MOSS研发团队：Base／SFT与后续路线](#n12) | 模型选型·版本跟踪｜区分已发布Base／SFT与Anime、Edit后续计划。 | — | 模思智能；MOSS-Image研发团队与社区提问者；[原视频](https://www.bilibili.com/video/BV1PbsA67EWy/) | 原团队说明及路线入口；未来计划不当已发布功能 | 完整简介、108秒媒体、20张帧与OCR／ASR；关键字幕已核 |

## 当日分享

<a id="n01"></a>

### Juggernaut MOSS DMD2 Turbo Beta

**适用方向：采样加速·模型选型｜查阅Juggernaut专用少步适配与构图取舍。**

**设计思路：摄影提示分层｜按图像类型、场景、镜头、光色和材质组织自然语言。**

- 原作者与原文：Kandoo，[Juggernaut Moss DMD2 LoRA (Turbo Beta)](https://huggingface.co/Kandoo/Juggernaut-Moss-DMD2-LoRA-Beta/blob/faa4cda706a8268a42227d80b707f74f1b58d73e/README.md)。北京11月16日03:33建仓、19:07更新；近期首次收录。接续[11月9日Juggernaut全量微调](../2026-11-09/README.md)，新增的是专门训练的蒸馏LoRA。
- 原作者说明：以Juggernaut Moss V1为教师，DMD2加真实照片GAN loss，单RTX A4500训练rank64 LoRA；本Beta在INT8版上训练。不是将已有加速LoRA换名。训练经过与盲测由作者报告，本库未核训练日志。
- 作者推荐：`juggernaut_moss_v1_int8_convrot.safetensors`配`JuggernautMossDMD2Lora4-8Steps.safetensors`，强度1，6步（复杂场景7）、CFG1、euler_ancestral/simple，约1.5–2.4MP。CFG1时负面提示不起通常的CFG作用，作者建议留空。编码器为MOSS的qwen3.5_9b，VAE推荐flux2-vae_small；没有把该组合写成全MOSS通用配方。
- 参考价值：作者把自然语言分为图像类别、主体动作场景、镜头、光线、色彩、质感和相机；场景里会出现文字的位置直接给定引号内文本。电影颗粒与清晰商业摄影是提示的不同选择，不概括为唯一画风。
- 局限：种子之间更相似，偏居中正面构图；复杂手部、反射仍可能失败，BF16组合作者测得更多错误。A4500约11秒与原版一分钟以上是作者的特定硬件整套方案记录，不作本库测速或普遍收益。
- 读取状态：固定revision模型卡全文与公开文件名／提示示例；未打开工作流JSON、PROMPTS附件、例图或权重。Apache2.0为模型卡声明，仍请查原许可与上游署名。

<a id="n02"></a>

### RS-CAMERA-CONTROL-MOSS：42视角与配套tokens

**适用方向：镜头构图·视角控制｜了解MOSS专用机位适配器与配套词向量。**

**设计思路：机位离散控制｜将视角选择映射到已训练方向和对应条件。**

- 原作者与原文：raspie，[RS-CAMERA-CONTROL-MOSS](https://huggingface.co/raspie/RS-CAMERA-CONTROL-MOSS/blob/ff44cb77d159d94f1c13aa7e85f1b67882e12e87/README.md)，北京11月16日22:12建立、22:15更新。与[11月13日Anima机位适配](../2026-11-13/README.md#n04)是不同基座的资源，不是同文件别名。
- 作者公开：MOSS-Image-SFT上实验性42视角适配，epoch5／step4740，LoRA与共同训练的42个4096维向量成套；训练图和caption未公开。
- 接入条件：使用[RS Camera Control节点](https://github.com/raspie10032/ComfyUI_RS_MultiCharacter_Sampler)，模型通过节点，输出提示送正向编码或RS pipe；节点选择最接近训练视角并注入方向caption和learned token。手动准备也需LoRA及`RS-CAMERA-CONTROL-MOSS-tokens.safetensors`两文件。Anima仍用自己的v2适配器，不能互换。
- 作者验证范围：固定场景16视角，768×1152、Euler ancestral CFG++／SGM Uniform、20步、CFG3、无加速LoRA。7组镜像对通过左右自动检查，其中3组达到更严格角度标准；不等于任意场景42角度都精确受控。
- 读取状态：完整固定模型卡；未看图、核节点实现或重跑。卡片标Apache2.0，训练数据与相机token的内部过程未取得。

<a id="n03"></a>

### Oboro Blink 1.0：Qwen2.1四步合并包

**适用方向：文字生图·合并模型选型｜查阅Qwen2.1四步包的组成与许可条件。**

- 原作者与原文：Oboro AI／Egor Prokhorov，[Oboro Blink 1.0 (v1.0.0)](https://huggingface.co/oboro-ai/Oboro-Blink-1.0/blob/9b1aea1eb09db01828f9eb60dff7d2b6dccb74d0/README.md)，北京11月16日21:38建仓、23:29更新。
- 组成核对：[NOTICE](https://huggingface.co/oboro-ai/Oboro-Blink-1.0/blob/9b1aea1eb09db01828f9eb60dff7d2b6dccb74d0/NOTICE)明确以Noct Q V4为起点，合入Detail Fix v2.0、Consistency、Lightning 4-step、Font，FP32合并运算、INT8 ConvRot存储，再导出GGUF。**此次没有新训练**；各作者的上游贡献分别保留，不列为独立从头训练或新微调成果。
- 作者通用起点：4步、CFG1、Euler/simple、1024方图；文本编码器与VAE仍用标准Qwen Image2.1，未打包。字体提示使用`font`并给精确引号文字。已合入适配器固定强度，不应再加载一遍。
- 用途：把多个已知调整整合为单checkpoint，侧重俄／英文排字，其他语言能力沿用基座；未据此保证任意多语排字准确。图像编辑仍需匹配Qwen2.1参考条件路径，不能把文生图工作流直接说成编辑工作流。
- 读取状态：完整模型卡与NOTICE；未读两套工作流JSON、例图或文件校验清单。Qwen Research License下研究／评估用途，商业使用需另取许可；Font组件Apache2.0不将整个合并包改成Apache许可。

<a id="n04"></a>

### AnyBokeh：分阶段估计与景深重渲染

**适用方向：摄影编辑·景深控制｜通过焦点与光圈调整已有照片的虚化层次。**

**设计思路：焦点与虚化分工｜先估计散焦和视差，再按目标光圈重渲染景深。**

- 原作者与原文：[AnyBokeh](https://huggingface.co/itsmag11/AnyBokeh/blob/c5597da32fc5f64fdc9e495504a2f6d331fa1ae0/README.md)，Xinyu Hou等四位作者；HF仓库北京9月28日00:50建立，11月17日02:13更新。本次是**历史资料首次补录**，未对比旧revision，不声称11月16日才发布或新增训练结果。
- 方法：FLUX.1-Fill-dev两个rank32 LoRA，stage1估计有符号circle-of-confusion及视差，stage2按目标焦点／光圈重渲染。预计算文本embeddings可省推理时文本编码器；不是通用给画面加模糊滤镜。
- 公开用法：输入照片、焦点像素坐标，已知源光圈时传source／target aperture；未知时用bokeh_scale，作者定义为源／目标光圈比。stage1地图可复用给多个目标，而非每次重新估计。
- [GitHub README](https://github.com/itsmag11/AnyBokeh)还公开两阶段训练、stage2先用真值再用stage1预测精调、UnrealBokeh数据入口。作者端到端示例约27GB显存；本库未测试低显存路径或ComfyUI集成，不标作开箱即用ComfyUI工作流。
- 读取状态：固定模型卡、GitHub当前README全文及模型元数据；示范图片、论文正文、训练实现未进一步读。源码S-Lab1.0，权重另受FLUX.1-dev非商用许可约束；没有下载基座或模型。

<a id="n05"></a>

### MOSS Charref v2：参考布局与场景提示分开

**适用方向：角色一致性·人物插画｜用单角色参考保身份，文本描述姿态与场景。**

**设计思路：身份与场景分工｜参考图提供外观，提示控制动作，另行选择风格适配。**

- 原作者与原文：bag3labo，[moss-image-edit-charref-v2](https://github.com/bag3labo/moss-image-edit-charref-v2/blob/1ab660fd372a9317370240c146e90bf2780a3c17/README.md)，北京11月16日11:06建仓，本次读至17日03:05所对应提交。
- 作者说明：MOSS-Image SFT上训练5000步、rank64、lr1e-4、batch4、512px，每5步一次正则；单角色图给头发、脸、衣装和配件，文本给新场景／姿态。参考图训练时放在输出下方，必须配套Reference layout节点；不是任意编辑图路径挂LoRA都相同。
- 公开建议：白底中性单人，手放下；全身参考较能保衣装，头到大腿裁切较保脸眼。图统一到448白方。纯标签描述场景，开头`1girl, solo`或`1boy, solo`，不重复描述由图提供的角色外貌。
- 常规示例：edit格式ai-toolkit、负向空文本但附同参考，LoRA1、50步、CFG3、euler/sgm_uniform、denoise1，SLG层22，约0.6MP；reference guidance2.5是额外分支，作者报告更像但稍牺牲动作遵循。Turbo另为8步CFG1/euler/simple，reference guidance关闭或至多1.5，不能套用2.5。
- 原作者评估：24个未入训练动漫角色、3seed，各72图；CCIP同角色判定普通50%、guided61%，场景姿态85%／78%。自动指标不等同人工观感或普遍成功率。风格叠加只测一个未公开`bag3l_style`与两角色，不能补造该风格配方或推广任意LoRA兼容。
- 局限：肤色、眼睛和配件易丢，参考姿态／画法可能泄漏，可能多手、多道具。Base、多参考、照片、0.6MP以上等未测试。权重文件作者给SHA256 `4e0b874ccc4e5f177fee38fbcc975493f13a962b9c8a791f16448115fd5f9369`，本库未下载核验。
- 读取状态：固定README全文与其中训练／配置表；示例图、三套JSON和节点源码未读，未运行。MIT仅覆盖本发布，不替训练数据授权。

<a id="n06"></a>

### Krea2 Photo Prompt Builder：七栏提示与分类历史

**适用方向：提示词组织·摄影创作｜分栏复用主体、镜头、光线和后期描述。**

**设计思路：摄影提示分层｜主体外观与姿态分栏，镜头光线质感独立复用。**

- 原作者与原文：magichan-lab，[Krea2 Photo Prompt Builder for ComfyUI](https://github.com/magichan-lab/ComfyUI-Photo-Prompt-Builder/blob/22d787ad4ad78d639eee9076a7e488c79d445c7f/README.md)，北京11月16日15:22建立、15:23更新。
- 方法：subject、appearance、pose、environment、composition、lighting、finishing七栏，分别开关；空栏省略，关闭栏仍保存在工作流／历史。参考价值是把人物设定、动作、镜头、用光和质感拆开管理，不是固定某一种画风。
- 节点输出普通STRING接兼容文本编码器，未包含模型／CLIP／采样器，不把有输出端口当任意模型效果验证。节点ID现为`MagichanLab_Krea2PhotoPromptBuilder`，旧ID工作流需改。
- 每栏历史本地JSON，同一ComfyUI安装的所有builder共用；默认每栏100项。自动保存只有Python节点实际执行才发生，缓存命中时可手动保存。Colab重置前需持久化历史，工具不会自动挂载Drive。
- 读取状态：固定README全文；未核后端／JS源码和前端兼容。作者提醒经典LiteGraph控件在未来／Nodes2.0专用前端表现可能不同，保留为版本条件。MIT许可；没有安装节点。

<a id="n07"></a>

### Krea2 FP8与INT8 ConvRot：4060Ti记录

**适用方向：资源选型·兼容排错｜结合显存余量和后端理解Krea2量化耗时。**

- 原作者与原文：nontan_works，[Krea2 FP8 vs INT8 ConvRot: Why Is INT8 Faster on My RTX 4060 Ti?](https://civitai.com/articles/38967)，北京11月16日10:49:37发布，本次首次收录。
- 作者条件：RTX4060Ti16GB、RAM32GB、Forge neo2.32、PyTorch2.14.0+cu130、comfy-kitchen0.2.41，1024×1536、同seed604311911，家族内固定提示／编码器／VAE，无LoRA／高分修复。Stable Yogi V1.0 Civ C89为12步CFG1.5 ER-SDE/Beta，CyberRealistic V4.0为8步CFG1 Euler/simple；两组绝对耗时不直接横排模型。
- 作者记录：CyberRealistic8步后续FP8约36秒、INT8 ConvRot约19.3–20秒；Stable Yogi最后两次FP8约64秒、INT8约55秒。12步CyberRealistic各仅一次，初步值不冒称稳定统计。
- 关键限制：一次FP8日志提示可用显存约1392MB低于安全阈值，可能导致变慢；不同quant layout、后端与显存空间未完全拆开。per-tensor INT8和INT8 ConvRot也不能混作相同实现。日志中的BF16存储标签不足以证明全部以BF16执行，作者未追每层kernel。
- 作者认为示例观感相近，是其主观比较；本库未看比较图，也未核原始控制台日志或跑LoRA负载。参考价值在于按实际格式、后端、工作流与余量选型，不推出INT8在所有Ada卡必然更快。
- 读取状态：文章正文全文、配置及重复耗时表；未取得精确checkpoint文件哈希、原始日志文件或示范PNG，未自行测速。

<a id="n08"></a>

### LoRA Dataset Studio V2：从资料整理到挑档

**适用方向：LoRA训练·资料管理｜查阅筛图、打标、训练与固定条件挑档流程。**

- 原作者与原文：perfectgf，[LoRA Dataset Studio V2: every feature, from one photo to a trained and ranked LoRA](https://civitai.com/articles/39003)，北京11月17日03:55:15发布。是既有项目新版功能导读，不是今天才建立的训练器。
- 文章方法：先按角色／画风／概念区分资料与caption政策；从图池做去重、构图／机位覆盖、保留／拒绝和标注，再接ai-toolkit训练；Test Studio固定提示与seed比较checkpoint／强度，结合投票和脸部相似度挑档。自动分数作为辅助，不能据此替代人物／画风和失败案例审阅。
- 公共版文章列Krea2、FLUX.1／FLUX.2 Klein、Qwen2.1、Z-Image、SDXL和Anima。**MOSS-Image与H3-Image训练／测试列在会员版**，不可把整页所有功能写成免费公共版均可用。外部API和租GPU另有费用。
- 作者硬件边界：无GPU可手工导入／整理／标注；自动caption约8GB、局部生成约16GB，Anima训练约24GB等是作者任务级估计，主要在24GB卡上测得，16GB以下训练未测。视频路线仍beta，多个目标中只完成Wan2.2 14B一条训练，不以列出目标数证明都验证。
- 发布和许可：公共核心／插件为PolyForm Noncommercial1.0.0；作者明确官方资源在[GitHub](https://github.com/perfectgf/lora-dataset-studio)，不要把名称相近的网站当官方。会员与上游模型／数据许可分别适用。图池清理、模型训练与上传只是原文功能，未在本次执行。
- 读取状态：文章全文（含公共／会员范围、硬件与限制）及仓库元数据；文章中插图、演示视频、完整源码／配置和训练产物未读。仅作流程导读，未安装或验证功能。

<a id="n09"></a>

### Comfy Image Atelier：Anima与Krea2的可控随机

**适用方向：自动化工作流·提示管理｜固定角色条件，按模型组织随机池与历史。**

**设计思路：固定与随机分工｜角色服装可锁定，单独探索姿态、场景与表情。**

- 原作者与原文：无害的史莱姆pzy，[更优雅的Anima 与 Krea 2 的本地生图工作台](https://tieba.baidu.com/p/11200087842)，stablediffusion吧，北京11月16日04:03:03首发，本次首次收录；项目[comfy-Image-Atelier](https://github.com/159159pzy-crypto/comfy-Image-Atelier)早于此帖建立，不把发帖日期当软件首版日期。
- 作者分享：Anima标签池、Krea2自然语言池各自保存规则与草稿，随机台探索、单图台精调。角色、服装、姿势、背景、表情五池可关闭／固定／随机，固定角色与画师后只换动作或环境，较容易保留探索思路。
- 管理方法：LoRA独立启停、权重、排序与触发词；角色抽取可绑定LoRA。预设保存模型、LoRA、画师、提示与采样，可带尺寸／修复项；历史记录最终提示、模型和双种子，支持原条件、同词换seed或指定内容重抽。这些是作者声明的功能，不是本库逐项实现核验。
- 条件：Windows原生启动器，背后依赖ComfyUI与Anima Tools生态；提示改写可接OpenAI兼容服务或Ollama，非所有操作都无外部依赖。多阶段修复／模型下载由原项目提供，本轮没有启动任何一个步骤。
- 社区反馈：可见楼层有人问遮罩精修、是否扩展或新项目、与可视化镜头控制搭配；提问不等于已有功能支持，也不把几条“好用”当稳定性测评。
- 读取状态：aiotieba4.8.2读到首楼及可见11楼（楼号有缺），无更多页；楼中楼、图片、完整节点／工作流未读。GitHub元数据与README已取得但正文未进一步通读，原帖概述不冒称源码审查。

<a id="n10"></a>

### 胶片颗粒节点：分辨率与颗粒参数的关系

**适用方向：采样精修·摄影质感｜了解放大后添加颗粒时的强度与密度取舍。**

**设计思路：颗粒随尺寸调整｜先确定输出分辨率，再调颗粒强度与分布。**

- 原作者与原文：鉴纯夏desu，[分享一个节点，可以增加胶片颗粒质感](https://tieba.baidu.com/p/11202473509)，stablediffusion吧，北京11月16日22:52:19；23:06补充，本次首次收录。
- 作者建议：其个人流程在MiniMax H3 Image放大到4K后叠颗粒；较低分辨率时降低`grain_power`与`grain_scale`。原文分别把两者说明为颗粒强度与密度控制，并承认当前参数未必最优。
- 本库整理：参考价值是把输出尺寸与后期纹理一起考虑，避免将高分辨率示例设置直接用于小图。这里不是本库的所有模型通用推荐，也未验证参数变化方向与节点源码定义是否完全一致。
- 读取状态：主帖和作者补充两楼文字，has_more=false；截图、节点准确名称、来源仓库、参数实值和示范PNG未取得。保留实践入口，不拼接其他grain节点参数冒充原图设置。

<a id="n11"></a>

### H3 Image按颜色替换角色v0.1

**适用方向：多主体关系·角色替换｜用三色绑定参考角色，并明确表情与遮挡取舍。**

**设计思路：颜色绑定·表情补写｜按色区分主体，保留映射并逐人说明视线和表情。**

- 原作者与原文：u/Round_Awareness5490，[H3 Image LoRA v0.1…](https://www.reddit.com/r/comfyui_elite/comments/1xxm4nx/h3_image_lora_v01_swap_up_to_3_characters_in_a/)，平台日期2026-11-16；网页只给相对时间，未取精确发帖时区。链接到Alissonerdx的[v0.1完整教程](https://huggingface.co/Alissonerdx/Minimax-H3-ComfyUI/blob/main/docs/character-swap-image-multiple-by-color.md)，本次读取main，教程所标v0.1；未冻结该文档commit。
- 方法：BFS Picker分割并以红／蓝／绿选人，每色对应一个参考；引导图是Picture1，启用的参考按颜色顺序从Picture2接续，不填的颜色省略。支持至多3人，但不能推出任意复杂人群都可靠。
- 文件关系核对：默认`..._fro_v0.1`是两个任务适配器按块合并，0–41取姿态／物件贴合者并按99%平方Frobenius能量做SVD，42–49取较早光色贴合适配并乘1.3。alternative是同训练较早step3200／Fro0.99检查点。**两文件不是两个独立基座模型，也不是单纯不同称呼的同一权重。**
- 公开流程要求ComfyUI0.45.0+、BFSNodes1.121.0+与KJNodes，H3 Image模型／图像VAE／编码器；LoRA1、6步CFG1、euler_ancestral/ddim_uniform，默认4MP。未使用的可选Molmo点节点可以删除，不能把所有可见节点都列成有效分支硬依赖。
- 原作者取舍：主文件更贴源姿态，但光色可能偏移；alternative较保源光照颗粒却替换较弱。全身参考较少猜衣装。表情、视线和头角容易丢，prompt_override保留Picture／颜色映射后逐人补短句；手、衣物随主体整体替换。此为原作者条件与失败记录，未形成普遍成功率。
- 读取状态：Reddit正文和HF教程全文；未看演示视频、参考图片、全部JSON或权重。与[11月15日H3角色替换资料](../2026-11-15/README.md)相关，本条是Alissonerdx另一套训练／分层合并与三色映射路线，首次收录；不是此前akhaliq／Akatz视频适配迁移的版本升级，不把相似标题当同一权重。许可另见原仓库LICENSES，本库未重新授权素材。

<a id="n12"></a>

### MOSS研发团队：Base／SFT与后续路线

**适用方向：模型选型·版本跟踪｜区分已发布Base／SFT与Anime、Edit后续计划。**

- 原作者与原文：模思智能，[MOSS-Image 研发团队便利店问答｜Anime、Edit 和迭代计划](https://www.bilibili.com/video/BV1PbsA67EWy/)，北京11月16日20:35:54发布，108秒。本轮由生图模型最新搜索及[贴吧转载线索](https://tieba.baidu.com/p/11202474316)发现，合并为原视频一个条目。
- 已读内容：简介介绍Base与SFT、长文本和布局控制，并将Anime进展、Edit目标与后续许可列为问答主题。抽样画面可见Base／SFT比较与社区问题卡。本库不从短演示推导基座间通用优劣，也不把未来版本计划当当前已有功能或可下载资源。
- 参考价值：跟踪原研发团队对模型定位和后续用途的说明，避免用转载省流替代原话；下载量和热度不作质量证据。未来发布应回到具体模型卡、版本、许可与原工作流再核。
- 读取状态：SDK完整简介及分P信息；游客会话未配SESSDATA，平台字幕返回login_required。已取得本分P108秒公开音视频，480短边，视频约5.1MiB／音频约0.84MiB，未用备用地址；FFmpeg常规13帧（4秒起间隔8秒）及末秒1帧，OCR草稿已读、联系图已人工看。不是逐帧或全部字幕准确阅读，评论未取；ASR为faster-whisper1.2.1 small／CPU INT8，约107秒音频生成时间轴草稿，模型名及开头数字有明显误识，不当平台字幕或全文准确文本。另在64、70、73、80、96、98秒抽6帧人工核硬字幕：Anime正在开发，希望支持透明通道与多角色参考；Edit在路上；后续许可仍以“不出意外的话”保持Apache2.0表述。上述均为团队计划，未给确定发布日期。本轮合计看20张抽样／定点帧，未逐帧审核。

## 来源覆盖与检索记录

以下为本轮实际抽查范围，不声称全平台穷尽；检查时间均为北京时间11月17日04:01起。

| 平台／吧名 | 实际入口或查询 | 检查与读取范围 | 结果／限制 |
|---|---|---|---|
| stable diffusion／stablediffusion吧 | aiotieba4.8.2，stablediffusion CREATE第1页30条；stable diffusion别名另核2条 | 非置顶新帖从11月16日22:52回到15日17:27，越过上次水位；读工作台11楼、颗粒2楼 | 实际规范吧名stablediffusion；带空格入口返回stable吧2018公告，不能算同吧重定向成功。收录n09、n10；置顶旧帖不作分页边界 |
| comfyui吧 | 同SDK CREATE第1页28条，含2置顶 | 非置顶从17日00:35回到10日22:50；读每日一图帖首楼 | 列表与正文可读；该帖只读到发起说明，没取得图和配方，暂留关注，不称全吧无更新 |
| 贴吧全站补搜 | 最新搜索“工作流 提示词”第1页，实际27条 | 核论坛名、tid与原帖日期 | 有跨吧噪声与旧命中，不代替指定两吧CREATE范围；主工具正常，未启备用 |
| bilibili | SDK17.4.2，pubdate搜索“ComfyUI 教程”第1–3页60条、“生图 模型”“Anima”“LoRA 画风”各第1页20条；BV去重 | ComfyUI第3页到15日20:30，越过水位；读3条完整简介；研发问答补媒体／帧OCR | 工具可用，搜索Anima含同名歌曲／游戏，已区分；平台字幕需已配置会话，本轮未取得。n12收录，两个长教程仍只读简介，未盲目全量下载 |
| Sena404作者跟踪 | UID341674866，第1页30条，总84条 | 页范围10月14日–11月15日；最新BV1wAsE6nE7A为投稿28期 | UID本轮恢复可读，未发现晚于已收录28期的新投稿；[系列索引](../2026-11-09/notes/Sena404画师串与相关分享.md)水位保留投稿28／片内38，未重复读媒体或计新增 |
| Reddit | r/StableDiffusion new50、r/comfyui new30；再用两组限定11月16日网页搜索 | 两个列表403；网页打开H3三色替换及PixlStash原帖，读正文、后者可见作者链接评论 | 部分受限而非全不可读；n11收录，PixlStash保留关注。没有完整最新评论／两版全量覆盖 |
| Hugging Face | text-to-image最新修改80条、image-to-image30条；按类别和新作者筛选 | 5份模型卡全文，Blink另读NOTICE，追AnyBokeh代码 | 收录n01–n04；VegaGen卡片明确无训练权重，未当可用后训练模型。已有Kromoss／MossYume／RoleRef更新未核实质变化，不重复计数 |
| GitHub | comfyui workflow pushed≥11月16日25条、comfyui prompt created≥11月15日15条 | 读取Charref／Photo Builder及AnyBokeh固定或当前README；Atelier／LDS元数据与README取回，未完整通读 | n05、n06与相关来源回链；没有用提交活跃度代替内容质量，也未安装／运行项目 |
| Civitai社区／论坛 | 新文章30条、Newest模型40条、Workflows15条 | 打开3篇文章全文及1个参考页工作流说明；看模型／版本列表元数据，未看画廊作品原图／评论 | n07、n08收录；参考页工作流仅一句说明、缺具体配方，不强凑条目；闲聊型文章未优先。最新列表不是历史所有作品覆盖 |
| ComfyUI论坛／其他论坛 | forum.comfy.org/latest.json；note.com ComfyUI最新15搜索 | 前者30主题列表可读，后者403 | 只检查列表，未新开论坛帖正文；无本轮精选新增结论仅限所查范围。已有教程／日期不因列表靠前就重报 |

## 后续关注与更正

- [Sena404第28期及既有系列](../2026-11-09/notes/Sena404画师串与相关分享.md)保留上次实际收录水位。本轮UID查询成功是访问状态变化，不当作新一期。
- [Anima两行代码训练教程](https://www.bilibili.com/video/BV14eWZ6BEq7/)（最努力の蕉蕉，11月16日07:03，1536秒）已取完整简介但为空；平台字幕login_required，尚未定位关键章节，不从标题补出训练配方。[漫剧风格提示第3期](https://www.bilibili.com/video/BV1XasP6PEfV/)（Ai_随风，18:00，1071秒）已读简介，谈风格确定和模板，但实际模板链接／画面未取；先留具体入口，未列为正文已学完教程。
- [PixlStash角色资料与训练整合](https://www.reddit.com/r/StableDiffusion/comments/1xxv2au/making_consistent_character_creation_easier/)（u/Infamous_Campaign687，平台日期11月16日）已读正文与作者链接评论，值得后续看[2.0更新／升级说明](https://pixlstash.dev/whatsnew.html)。目前仅知整合ComfyUI／ai-toolkit、按相似度组织图池；作者模型比较未独立核验。
- 颗粒节点的准确名字／截图参数、AnyBokeh旧版本差异、Charref其他风格组合仍未取得；只保留与文章用途有关的缺口，不用未知项替代设计思路摘要。
- 本次没有迁移／实验计划，也未做运行收益验证。公开媒体、抽样帧、完整OCR／ASR草稿和API原始响应留在研究缓存，未提交GitHub；正文以中文摘要与来源导读为主。
