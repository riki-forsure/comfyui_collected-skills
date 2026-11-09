# B站视频内容工具：Codex云端试运行（2026-11-09）

本记录是用户明确要求“判断哪个最适合并进行试运行”后的有限验证，时间为北京时间10:51起。未新增常驻服务，未改变每日04:00调度或自动扩展全部视频的媒体处理范围。感谢工具维护者与视频作者，本库记录实际读取结果，原内容仍请回作者视频。

## 选择结论

当前官方托管Codex环境下，优先复用 **bilibili-api-python 17.4.2＋FFmpeg**：SDK取得视频信息、公开DASH流与服务返回的备用地址，FFmpeg解码和抽帧；屏幕文字再用Tesseract辅助、人工对照。ASR用faster-whisper作为可选讲解草稿来源。

不将BiliNote桌面／常驻服务或VideoToNo的本机MCP推荐等同于本环境已接入。yt-dlp适合按次运行，也成功解析本次视频，但默认媒体地址下载失败，故本样本未优于已有SDK路径。这是当前两个样本的实测选择，不是所有平台／运行环境的性能排名。

## 实际环境与工具

| 项目 | 本轮范围 |
|---|---|
| 环境 | OpenAI托管Codex，Linux／Python3.12.14，无NVIDIA GPU工具；继承代理与CA，保持TLS校验。环境状态显示网络策略已生效、没有配置B站会话。 |
| 既有SDK | bilibili-api-python17.4.2，复用既有独立环境，不自动登录、读取浏览器Cookie或保存新会话。 |
| 下载候选 | yt-dlp2026.10.26，本次在仓库外隔离环境安装并运行。 |
| 媒体 | FFmpeg／ffprobe7.1.5，使用既有程序。 |
| OCR | Tesseract5.5.0；已有eng，另在仓库外取得官方tessdata_fast的chi_sim，未覆盖系统数据。 |
| ASR | faster-whisper1.2.1／CTranslate2 4.8.5，CPU int8；base与small各一次主试／对照，VAD启用。模型与依赖缓存留在仓库外。 |
| 归档 | 只保存本库摘要、命令要点与证据范围；未把音视频、截图、完整转录、签名CDN地址或模型权重推入GitHub。 |

## 样本A：Sena404《anima画师串第二十二期》

原视频：[BV1UQ4u6kENU](https://www.bilibili.com/video/BV1UQ4u6kENU/)，2026-11-03 18:18:32 +08:00发布，详情标66秒。素材实际视频约65秒、音轨65.016秒，内部卡片日期2026-11-02，与投稿日期分别保留。

1. yt-dlp成功读取标题、格式与流信息，游客态未返回字幕／自动字幕；不据此断言视频根本没有字幕。
2. 选择1080p视频＋最低码率音频下载时，CDN返回HTTP567。重试次数设0，未靠循环请求继续。
3. 现有SDK取得公开480p视频与音轨：视频主地址也返回567，使用**同一响应提供的一个备用地址**成功；音频主地址成功。没有改造签名、关闭证书或手工猜CDN地址。
4. 成功保存852×480 H.264视频1,259,510字节，AAC音轨540,210字节；合计1,799,720字节。FFmpeg无重编码合并并由ffprobe确认流与时长。
5. 每6秒取一帧，共11帧；另做场景变化抽帧补查。六张文字卡片用chi_sim＋eng做OCR，并人工对照其中画师串、资源和参数页。抽样看图不等于逐帧看完整片。
6. 已能从画面取得画师标签、两枚LoRA及强度、底模、编码器／VAE显示名、尺寸、步数、CFG、采样器与调度器，见[当日N11](../README.md#n11)。
7. base ASR只返回一小段低参考价值日文音节，VAD后时长约2.624秒；不当作教程口播、不据此认定作者说过这句话或全片没有人声。这个样本的有效资料来自画面。

## 样本B：hihihihi202《GPT二次元图噪点修复方法skill》

原视频：[BV1EC4B6rEMs](https://www.bilibili.com/video/BV1EC4B6rEMs/)，2026-11-06 23:49:57 +08:00发布；内容概述见[当日N10](../README.md#n10)。

- SDK公开音轨主地址成功，1,246,878字节，约158.443秒。这里只读取了音频，没有把该视频画面补称已看。
- FFmpeg解码成16kHz单声道PCM，供faster-whisper离线转写；两模型均返回中文、带时间段的草稿，VAD后约150.624秒。
- base约11.5秒（已缓存模型，含加载）；small首次约68.9秒，其中加载／模型准备约36.8秒。不同缓存状态不构成严格速度基准，也不将此成本推广到所有云任务。
- 草稿可定位：约42–65秒谈缩小到60%再超分；65–90秒谈梯度平滑和0.001；90秒附近谈残纹与渐变损失的调节。已与此前读取的作者GitHub方法说明交叉核对。
- **专业术语仍需核对**：两模型均将噪点、超分、L0梯度最小化等词误写，small也未消除这些错误。转写草稿不能直接粘贴成作者字面原文；数字、名字、画师串和模型版本优先回原图／原文确认。此次没有人工逐字听校，不能报告全文准确率。

## 遇到的问题与解决范围

首次faster-whisper直接打开m4s时，PyAV19报 `open() got an unexpected keyword argument 'metadata_errors'`。没有循环换装依赖；改由既有FFmpeg解码PCM，再把float32数组交给转写接口，两个样本均完成。这验证的是PCM输入路径，不表示上述版本直接读所有容器都兼容。

## 可复用的操作顺序

1. 复用本库[只读脚本](../../../scripts/bilibili_readonly.py)读取BV信息、分P／cid与实际字幕状态。
2. 在有媒体深读授权时，通过SDK的 `Video.get_download_url(page_index=0)` 取得响应；只选必要分P、分辨率和音轨。HTTP失败最多补读该响应给出的一个备用地址，保留状态，不枚举／循环换工具。
3. 按有限时、有限大小下载；沿用环境代理和TLS，设置视频原页Referer；签名链接仅用于本次请求，不入公开笔记。
4. 用FFmpeg抽样关键帧。OCR只是辅助，名字、括号、反斜杠、权重与小字必须对照原画面。
5. 有讲解时才视需要转写；先找时间段，再核对正文／画面。音乐、无讲解、低质量音频和术语误识别均单独记录。
6. 归档作者与原视频、发布时间、字面配置、读取范围和缺口。输出摘要不冒充完整视频理解，不将测试资源加载当生图效果验证。

示例（已下载、获准处理的本地文件；不自动触发网络下载）：

```bash
ffprobe -v error -show_entries stream=width,height,codec_name,duration -of json sample.mp4
ffmpeg -i sample.mp4 -vf fps=1/6 frame%02d.png
ffmpeg -i sample.mp4 -ar 16000 -ac 1 -f f32le audio.f32
tesseract frame.png stdout -l chi_sim+eng --psm 6
```

媒体与模型缓存本轮已在工作区实际使用，但未验证下一次官方任务会自动继承；未来复用须按可用环境检测，不能依赖本次临时路径。这里没有新建运行服务、全量下载任务或测试框架。

## 工具来源

- [bilibili-api-python](https://github.com/Nemo2011/bilibili-api)：本库固定17.4.2及其实际可读范围。
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)：格式解析与按次下载候选。
- [FFmpeg](https://ffmpeg.org/)：解码、合并、抽帧。
- [Tesseract](https://github.com/tesseract-ocr/tesseract)、[tessdata_fast](https://github.com/tesseract-ocr/tessdata_fast)：OCR与中文数据。
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper)：CPU转写；所用base缓存revision `ebe41f70d5b6dfa9166e2c581c45c9c0cfc57b66`，small另按本轮实际缓存使用，不据名称推定不同模型结果相同。

[返回当日日报](../README.md)
