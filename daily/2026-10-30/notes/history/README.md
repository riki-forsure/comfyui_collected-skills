# 近四个月历史分享集中补录

感谢社区作者分享模型、工具、教程与实践经验。本库保留原文链接与署名，摘要与学习备注另行标明；欢迎前往原帖阅读和支持作者。

- 原始分享／版本时间窗：2026-06-30 00:00至2026-10-30 02:26:31 +08:00（北京时间）。
- 本次归档：2026-10-30；六个gpt-6.1-terra子代理执行。
- 结果：122条日期有原始依据的资料／版本，11条待核线索。
- 同一资源不同实质版本与配套教程可分别记录；多源记录不当作独立效果验证。

## 优先阅读入口

以下为本库按公开资料参考价值选择的入口，作者效果说明与本库实际读取范围分别记录。

| 编号／原分享 | 原文／版本日期 | 适用方向（短标注） | 美术风格／设计思路 | 原作者 | 详情与读取范围 |
|---|---|---|---|---|---|
| [CVA-08 Facial Expression Tags Dictionary for Illust…](https://civitai.com/articles/34888) | 2026-09-12 | Illustrious·人物表情·提示词｜表情标签词典按情绪、眼眉口、符号等分类；作者标记效果不确定词条，强调与… | 设计思路：表情设计｜按情绪和眼眉口组织表情提示词。 | Nonichill | [公开 API 文章正文文字；未读取附件及文章例图](civitai_articles.md#cva-08) |
| [CV-02 Anima Text to Image ［ControlNet (3D Pose, Re…](https://civitai.com/models/2742675?modelVersionId=3428980) | 2026-10-25 | Anima·区域控制·工作流｜v1.3 增加 LoRA 高低噪声分段、split condition… | — | Marui_Melons | [公开 API 模型卡正文及指定版本元数据；未读取图片与工作…](civitai.md#cv-02) |
| [HF-07 AniSee V2 Base/Aesthetic/Turbo](https://huggingface.co/SeeSee21/AniSee) | 2026-09-06 | 动漫插画·Anima·后训练｜旧仓库新发布V2三款权重；作者说明为单个 LoKr 合并，区别于 V1… | 动漫插画｜按作者描述，侧重更干净的动漫表现。 | SeeSee21 | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-07) |
| [GH-01 Anima Artist Mixer：post-adapter 混合与锚点](https://github.com/An1X3R/Anima-Artist-Mixer/commit/8e6c780cb1fd2cb3532efaa623ad5ae510b5a2d5) | 2026-07-27 | 画师混合·Anima｜26.8.1 已加入 post-LLMAdapter 多画师混合；26… | 设计思路：画师混合｜通过多画师条件混合与锚点控制组织风格组合。 | An1X3R | [仓库历史 README 及提交列表；部分条目参考当前 RE…](github.md#gh-01) |
| [OF-03 Anima 风格提示词固定种子对照](https://note.com/ai_0049/n/n74ccab5370e0) | 2026-07-12 | 画风提示·对照实验｜作者固定种子和简单构图测试 108 个风格提示词并讨论限制。 | 设计思路：多风格对照｜固定种子与构图比较 108 个风格提示词。 | おーら | [原文可见文字段落；未读取图片、附件、视频与评论](other_forums.md#of-03) |
| [BV1VKe46XEsP 【ComfyUI】Anima提示词扩写 TIPO v2.1｜使用详解&本地安装教程](https://www.bilibili.com/video/BV1VKe46XEsP/) | 2026-09-19 | Anima提示词·自动化｜API简介给出TIPO示例工作流、模型发布页与节点。 | — | Zove-try | [B站公开API：标题、UP主、pubdate和视频简介；未…](bilibili.md#bv1vke46xesp) |
| [HF-15 Qwen-Image-2.1-Outfit-Swap-Consistency-LoRA …](https://huggingface.co/ausboss/Qwen-Image-2.1-Outfit-Swap-Consistency-LoRA) | 2026-10-04 | 换装·一致性｜对参考换装进行局部一致性训练，减少原图主体和背景漂移。 | — | ausboss | [模型卡正文、公开提交历史（选段）](huggingface.md#hf-15) |
| [CVA-11 Where Anima style LoRAs keep their realism: …](https://civitai.com/articles/36233) | 2026-10-07 | Anima·风格 LoRA·层权重｜作者对单个混合来源 LoRA 做分块实验，报告写实倾向与风格损失的权衡… | 设计思路：写实与风格平衡｜比较 LoRA 分块权重对写实倾向与风格保留的影响。 | ducktopuss | [公开 API 文章正文文字；未读取附件及文章例图](civitai_articles.md#cva-11) |
| [CV-13 Anima style: Habeli](https://civitai.com/models/2949844?modelVersionId=3340766) | 2026-09-20 | Anima·线稿与上色·LoRA｜作者介绍平色与赛璐璐风格 LoRA，并给出基座、建议设置及示例所用模型。 | 平色·赛璐璐｜本例大眼、简化鼻口、粗轮廓与块面阴影 | Habeli | [公开 API 模型卡及指定版本元数据；查看一张公开例图](civitai.md#cv-13) |
| [CV-14 Krea 2 Geometric Composition Style Slider Kr…](https://civitai.com/models/2927993?modelVersionId=3313473) | 2026-09-10 | Krea 2·构图·风格滑块｜概念验证滑块在写实摄影与几何构成两个方向调节，作者提示可能不稳定。 | 摄影→几何构成｜本例由柔焦转硬边块面、五官简化 | baizuobusi | [公开 API 模型卡及指定版本元数据；查看一张公开例图](civitai.md#cv-14) |
| [R15 A simple character-sheet workflow in ComfyUI…](https://www.reddit.com/user/Sea-Advantage-4063/comments/1wexhhp/a_simple_charactersheet_workflow_in_comfyui_using/) | 2026-09-13 | 人物参考·多视图·LoRA数据｜用全身与面部裁切组合参考并拼接多角度。 | 设计思路：角色多视图｜组合全身与面部参考，再提取正侧背角色图。 | Sea-Advantage-4063 | [正文及提示词](reddit.md#r15) |
| [OF-13 Anima 与 Illustrious 漫画分镜工作流](https://note.com/nobinlog/n/n7b306e23e9a1) | 2026-10-09 | 漫画分镜·自动化工作流｜分享三格和四格文字生图分格工作流，10 月 12 日修正模型对应和节点… | — | nobin | [原文可见文字段落；未读取图片、附件、视频与评论](other_forums.md#of-13) |

## 全部分册

| 来源分册 | 日期有原始依据的条目 | 待核线索 |
|---|---|---|
| [百度贴吧（指定两吧）](tieba.md) | 0 | 3 |
| [bilibili](bilibili.md) | 17 | 0 |
| [Reddit](reddit.md) | 13 | 5 |
| [Hugging Face](huggingface.md) | 23 | 1 |
| [GitHub](github.md) | 17 | 2 |
| [Civitai 模型与版本](civitai.md) | 21 | 0 |
| [Civitai 社区文章](civitai_articles.md) | 15 | 0 |
| [其他作者技术分享](other_forums.md) | 16 | 0 |

## 月份分布

| 原文／版本月份 | 数量 |
|---|---|
| 2026-06 | 2 |
| 2026-07 | 33 |
| 2026-08 | 16 |
| 2026-09 | 36 |
| 2026-10 | 35 |

六月仅覆盖6月30日。带时区日期转北京时间，来源未标时区的日期保留原写法。

## 阅读边界

[覆盖与限制](coverage.md)记录公开接口、查询、原始时间口径及无法访问的来源。视频简介不等于观看完整教程，模型卡不等于工作流实跑；单例风格观察不推广为稳定特点。

[当天汇总](../../README.md) · [结构化记录](records.json) · [全库索引](../../../../每日检索可速查总结.md)
