# bilibili每日检索：SDK＋FFmpeg＋OCR

2026-11-09用户明确要求将已验证方案用于每日B站检索。默认采用 **bilibili-api-python17.4.2＋FFmpeg＋Tesseract OCR**，有讲解且确需补读时用faster-whisper生成时间轴草稿。感谢各工具维护者与社区作者；当前工具不启动常驻服务、不写入账号。

## 每日执行顺序

1. 用[基础只读脚本](../scripts/bilibili_readonly.py)按pubdate广泛搜索，结合作者投稿列表、上次成功时间和页边界分页，按BV去重后读完整简介。
2. 平台字幕用已配置会话和指定轨读取。未配置／未返回时记录真实状态，不能推断视频没有字幕；AI字幕与人工字幕分开。
3. 对关键内容在画面中、值得收录的视频，用[媒体深读脚本](../scripts/bilibili_deep_readonly.py)取得必要分P的公开视频，FFmpeg抽样与末秒补帧，Tesseract中英文OCR后对照原帧核字。名字、数字、括号、反斜杠与权重必须人工核对。
4. 有讲解且需要时，用[可选ASR脚本](../scripts/bilibili_asr.py)读取已取得的音轨。先生成时间轴草稿，再核对技术词和数字；音乐／短音节不能改写成教程正文。不是每个视频都下载音轨或跑ASR。
5. 及时保存已经读到的作者要点、原视频／时间点、字面配置与缺口；简介、字幕、ASR、画面、OCR、配置各自记范围。公开资料不等于已复跑或确认效果。

Sena404为固定跟进作者：**UID341674866**，先看最新投稿而非只靠关键词搜索。[第一至二十四期与相关分享](../daily/2026-11-09/notes/Sena404画师串与相关分享.md)是历史基础；2026-11-10已补[投稿第25期](../daily/2026-11-10/README.md#n08)，之后读取最新索引并按投稿时间／BV增量跟进。内部卡片第35期与投稿第25期的差异已记录，不能据此补称中间期数已收录。作者跟踪不替代其他作者和用途的广泛发现。

## 依赖与复用

| 阶段 | 需要什么 | 本轮已验证 |
|---|---|---|
| 搜索、作者投稿、简介、字幕、媒体API | [requirements-bilibili.txt](../scripts/requirements-bilibili.txt) | SDK17.4.2 |
| 解码／抽帧 | 系统可用的ffmpeg、ffprobe | 7.1.5 |
| OCR | tesseract及chi_sim、eng语言数据 | Tesseract5.5.0＋官方tessdata_fast中文 |
| 可选ASR | 单独环境的[requirements-bilibili-asr.txt](../scripts/requirements-bilibili-asr.txt)、FFmpeg和转写模型缓存 | faster-whisper1.2.1、CPU int8 base／small；均需校词 |

先复用可用Python、系统工具、语言数据与模型缓存；缺少才准备，不因日期变化重装／重下，不依赖本次临时环境路径。SDK与ASR可用独立进程／环境，避免把可选的大型依赖混入日常发现入口。

在当前执行环境中检查FFmpeg与Tesseract；缺少时按该环境的包安装规则准备相应工具及中文语言包。已有Tesseract但缺中文数据时，也可从[官方tessdata_fast](https://github.com/tesseract-ocr/tessdata_fast)将chi_sim.traineddata和eng.traineddata缓存到仓库外，用 `--tessdata` 指定。不要反复切换第三方安装源。

示例环境路径均可替换：

```bash
uv venv /tmp/bilibili-research-venv
uv pip install --python /tmp/bilibili-research-venv/bin/python -r scripts/requirements-bilibili.txt
ffmpeg -version
tesseract --list-langs
```

## 搜索与作者增量

```bash
python scripts/bilibili_readonly.py search --query 'ComfyUI 教程' --page 1 --limit 20 --since 2026-11-08
python scripts/bilibili_readonly.py uploader --uid 341674866 --page 1 --limit 30
python scripts/bilibili_readonly.py uploader --uid 341674866 --query '画师' --page 1 --limit 30
python scripts/bilibili_readonly.py info --bvid BV1LR4b6VEVw
python scripts/bilibili_readonly.py subtitle --bvid BV1LR4b6VEVw --part 1 --language zh-CN
```

实际用已准备SDK环境的Python。search原页20条，uploader原页30条；日期筛选只作用当前页。读取page.count、原页日期范围并判断分页，不能把截取后的空结果当平台无新增。作者接口成功也不表示所有投稿正文／画面已读；关键词筛选不能代替无关键词的最新投稿检查。

## 精选视频的媒体与OCR

```bash
python scripts/bilibili_deep_readonly.py --bvid BV1LR4b6VEVw --out /tmp/bili-read/BV1LR4b6VEVw --ocr --tessdata /tmp/bilibili-tessdata
```

- 默认分P1、短边不超过480像素（含竖屏）、单分P不超过600秒、每条流40MiB、90秒下载上限、每6秒抽样并补末秒帧。需要时显式指定 `--part`、`--short-side`、`--interval`、`--max-duration`、`--max-mib`；长视频先读章节／字幕、选必要分P。脚本不实现任意长视频的按时间段网络截取，超限会记录duration_limit，不悄悄全量下载。
- 只有需要转写时加 `--audio`，取得最低码率音轨；只读画师标签的短片通常不需要。仅主视频成功不代表音轨或OCR也成功，查看manifest各项状态。
- SDK响应给出的主媒体地址失败，最多使用其中一个备用地址。不猜域名、重写签名、枚举地址或循环重试。签名链接只在请求时使用，不保存进manifest或公开笔记。
- 输出在仓库外：媒体、frames、OCR文本和manifest.json。重复执行同一输出目录会更新该脚本生成的帧与OCR文件；为不同BV／分P使用独立目录，避免混杂。
- OCR结果标machine_text_unverified。抽样帧时间是近似采样点，末帧另标last_second；关键卡片仍应点回原视频核对。采样可能漏掉瞬间页面，必要时针对同一已下载素材加密抽样，不能声称逐帧读完。
- 若平台只返回脚本未支持的流类型，记录真实限制，不反复切换下载器。API返回成功、媒体完整取得、画面已读与配方完整是不同状态。

## 可选ASR

```bash
uv venv /tmp/bilibili-asr-venv
uv pip install --python /tmp/bilibili-asr-venv/bin/python -r scripts/requirements-bilibili-asr.txt
/tmp/bilibili-asr-venv/bin/python scripts/bilibili_asr.py --input /tmp/bili-read/BV1LR4b6VEVw/audio.m4s --out /tmp/bili-asr/BV1LR4b6VEVw --cache /tmp/bili-asr-models --model base
```

首次按需准备小型转写模型，此后复用缓存；small只在有必要时选择，本轮对照并未消除专业词错误。脚本先经FFmpeg解码16kHz单声道PCM，再交给faster-whisper，避开本轮PyAV19直接读容器的兼容问题；不新增后台服务。执行方另按任务预算限时，失败保留已取得部分。

输出asr.json为local_asr_unverified，包含时间段、模型与语言等读取状态，不自动送入公开日报。ASR不能可靠还原屏幕中的画师串、特殊语法和模型名；优先原画面／作者配置，必要时回听，未知就保留缺口。

## 登录态、网络与归档

- 默认游客态，只有环境已配置BILIBILI_SESSDATA才复用该会话；不自动扫码、提取浏览器Cookie或索要聊天里的凭据。私密会话只在任务执行环境配置，不入仓库／命令参数／日志。
- SDK显式沿用继承代理与环境信任，保持CA与TLS校验；HTTP媒体请求同样沿用，不改网络路由。浏览器登录不会自动把会话传给云任务。
- 媒体、截图、完整转录、模型／语言缓存、会话和临时签名地址不自动提交GitHub；归档中文摘要、作者与原文、必要字面配置、时间点和读取缺口。引用与素材使用仍按原作者说明和许可。
- 当前环境成功不保证下一次官方云任务继承已安装依赖和缓存；按仓库说明检测与准备。平台限制、无命中、无优质新增分开记录。

## 选择依据与历史实测

- 11月3日：SDK游客态最新搜索与两视频完整简介成功；字幕因无会话未取得。bilibili-cli0.6.2显式沿用代理后搜索可用，但默认综合排序，不是每日主工具。
- 11月9日[有限试运行](../daily/2026-11-09/notes/b站云端工具试运行.md)：yt-dlp2026.10.26解析成功、默认媒体下载567；SDK响应的备用CDN取得Sena404完整480p视频／音轨，FFmpeg＋OCR读出标签与参数。有讲解的另一视频可得ASR草稿，但base／small均有术语错字。
- 随后用户明确授权每日采用本方案。本次用可复用脚本完成Sena404系列读取，竖屏按短边选择、末秒补帧；详细覆盖见系列笔记。此前“仅临时试运行、未改每日任务”的文字是当时状态，不再作为当前禁止精选媒体深读的规则。
- SDK上游已归档停维，固定版本仅代表可复查的已测版本，不是稳定性保证；接口变化据实记录。bilibili-cli、yt-dlp留档备用，正常每日不重复查询／启动；BiliNote等常驻服务未接入。

## 来源与致谢

- [bilibili-api-python](https://github.com/Nemo2011/bilibili-api)及[17.4.2](https://pypi.org/project/bilibili-api-python/17.4.2/)。
- [FFmpeg](https://ffmpeg.org/)、[Tesseract](https://github.com/tesseract-ocr/tesseract)、[tessdata_fast](https://github.com/tesseract-ocr/tessdata_fast)。
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper)、[yt-dlp](https://github.com/yt-dlp/yt-dlp)、[bilibili-cli](https://github.com/public-clis/bilibili-cli)。各组件分别遵循上游许可，本库未复制其实现。
