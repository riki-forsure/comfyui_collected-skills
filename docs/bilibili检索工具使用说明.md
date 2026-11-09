# bilibili 检索工具：游客态实测与每日使用

## 选择与实际能力

每日优先使用 **bilibili-api-python 17.4.2**，通过本库的[只读脚本](../scripts/bilibili_readonly.py)调用；依赖固定在[requirements-bilibili.txt](../scripts/requirements-bilibili.txt)。感谢工具作者维护公开读取接口。本库仅封装搜索、视频元数据／简介与指定字幕轨读取，不启动 MCP 服务。

2026-11-03 北京时间08:48前后，在当前云环境、没有登录凭据的情况下实测：

| 操作 | 实际结果与边界 |
|---|---|
| 最新视频搜索 | `ComfyUI 教程`，`order=pubdate`，1页20条；取得BV号、作者、真实发布日期、标题与搜索简介 |
| 视频详情 | `BV1zd4A61EVz`、`BV1Af4T6cEvM`成功，取得完整简介、时长与分P／cid；前者在晨间裸HTTP路径返回412 |
| 主脚本 | 最新搜索、详情、游客态字幕状态均已实际调用；搜索短截取3条不意味着页面只有3条 |
| 字幕 | SDK对首个视频返回`CredentialNoSessdataException`；主脚本未配置登录态时明确返回`login_required`，没有取得字幕 |
| bilibili-cli 0.6.2 | 显式沿用环境代理后，游客态搜索成功；默认搜索是综合排序，未提供每日所需的发布时间排序选项 |

选择依据是本轮实际读取能力、可明确按发布时间检索和较少中间层；没有做正式耗时或长期稳定性比较。成功不保证以后所有视频、字幕或运行环境均可读，不能称为“保证绕过412”。

**维护状态需留意：** [Nemo2011/bilibili-api](https://github.com/Nemo2011/bilibili-api)当前已归档并宣布停止维护；PyPI仍有17.4.2可安装。本库保留本次可复查版本与读取结果，不把“仍可安装”当作上游持续维护。SDK包许可为GPL-3.0-or-later，使用与分发依其许可；本库没有复制其实现代码。接口变化时记录失败，不循环安装旧版／分叉或反复尝试。

## 运行方式

复用已有可用Python环境；缺依赖时才在仓库外准备独立环境，例如：

```bash
uv venv /tmp/bilibili-research-venv
uv pip install --python /tmp/bilibili-research-venv/bin/python -r scripts/requirements-bilibili.txt
/tmp/bilibili-research-venv/bin/python scripts/bilibili_readonly.py search --query 'ComfyUI 教程' --page 1 --limit 20 --since 2026-11-02
/tmp/bilibili-research-venv/bin/python scripts/bilibili_readonly.py info --bvid BV1zd4A61EVz
/tmp/bilibili-research-venv/bin/python scripts/bilibili_readonly.py subtitle --bvid BV1zd4A61EVz --part 1 --language zh-CN
```

示例环境路径可替换，不是自动化的固定依赖路径。脚本显式将继承的HTTP(S)代理交给SDK，保留证书验证和CA环境；不改网络路由。每个操作有时间上限，不循环重试。搜索的日期筛选仅作用于当前页，输出原页日期范围供决定是否继续分页。

正常每日先按中英文类别词搜索，再按BV号去重读取有价值候选详情。`--limit`只控制输出数量；判断窗口边界要看未截断的原页日期范围，不能因筛选后空结果就称平台无新增。

## 字幕与读取范围

- 默认游客态，不读取浏览器Cookie、不自动扫码或保存登录信息。
- 只有在已配置环境变量`BILIBILI_SESSDATA`时，字幕操作才使用该现有会话。凭据不放入仓库、命令参数、日志或聊天；当前云环境未配置，本次没有测试登录态字幕。
- 指定分P和准确语言代码；没有返回所选轨时列出可见语言，不能直接断言视频无字幕。AI轨需要显式指定如`ai-zh`，结果另标`platform_ai_subtitle`；未以人工字幕冒充。
- `ok=true`表示操作返回结构化结果；仍要读`status`和`scope`。`login_required`、`track_not_returned`不代表已取得逐字稿。
- 简介、字幕文本、评论、视频画面、公开工作流各自记录。简介中提到资源链接不等于配置文件已读，更不证明视频演示效果；本脚本不会下载音视频或自动ASR。

## 备用与其他工具

[public-clis/bilibili-cli](https://github.com/public-clis/bilibili-cli) 0.6.2仅作交互式备用：它同样依赖bilibili-api-python，并不是独立解决上游限制的另一套接口；正常每日不安装或重复查询。CLI还包含登录、浏览器凭据和账号写操作，本任务仅使用公开搜索／详情，未测试这些功能。直接运行默认CLI搜索未及时返回，最终退出码1且无JSON输出，具体原因未确认；另一有限时调用显式设置继承代理后搜索成功，不能误记成CLI永久不可用。

还查阅了[ShuboLiang/bili-cli](https://github.com/ShuboLiang/bili-cli)的README；未编译或运行，不列作已验证备用。MCP封装和下载器不因名称不同就具有更强读取能力，先看实际字段、版本与依赖。

平台受限时保留失败范围，继续归档其他已读来源；不反复切换工具或安装同类服务。已有用户浏览器会话可在另有需要时通过浏览器正常阅读，读取层级仍需分别记录。

## Codex官方云端：2026-11-09有限试运行

用户明确授权选择并试跑视频内容工具后，在当前托管Linux环境完成了两条视频的有限读取。**深读优先复用bilibili-api-python17.4.2＋FFmpeg，屏幕文字用Tesseract辅助并对照原帧；有讲解时才按需ASR。** 完整结果与版本见[试运行记录](../daily/2026-11-09/notes/b站云端工具试运行.md)。

| 路径 | 本轮实测 |
|---|---|
| yt-dlp2026.10.26 | Sena404视频的元数据与格式解析成功；默认1080p＋音轨下载收到CDN567，未完成媒体下载，不能列为本环境已验证首选下载器。 |
| 既有SDK＋服务返回的一个备用CDN | 取得同视频480p完整视频与音轨，约1.8MB；另一条噪点修复教程的公开音轨主地址成功。不是保证绕过风控，也不推广为所有视频均可匿名读取。 |
| FFmpeg＋Tesseract5.5.0 | 抽样11帧、6张文字卡OCR，并人工核对具体画师标签、LoRA与参数；没有平台字幕也能读取画面上的资料。 |
| faster-whisper1.2.1 CPU int8 | 有讲解教程可返回时间轴草稿；base和small均有技术词误识别。Sena404样本只得到不可靠短音节，未当教程正文。ASR只辅助定位，名字／权重／术语仍回原图或原文。 |

本轮媒体读取由仓库外临时脚本完成，现有 `bilibili_readonly.py` 仍只封装搜索、详情与字幕。未新增常驻BiliNote服务，未接入新的MCP或修改每日定时任务输入；本次明确试运行授权不等于以后每日全量下载／自动ASR。未来如接入媒体深读，须限定精选视频、时长、大小和读取范围，并保留本库原有的署名与证据规则。

网络请求沿用代理、CA与TLS，未自动登录、提取浏览器Cookie或枚举签名地址。失败最多使用同一API响应提供的一个备用地址；媒体／模型缓存与带时效签名的流地址均不入仓库，也不能假定后续官方云任务自动继承本次临时环境。

## 来源与致谢

- [bilibili-api-python 17.4.2发布页](https://pypi.org/project/bilibili-api-python/17.4.2/)与[上游当前状态](https://github.com/Nemo2011/bilibili-api)。
- [bilibili-cli文档](https://github.com/public-clis/bilibili-cli)、[依赖声明](https://github.com/public-clis/bilibili-cli/blob/main/pyproject.toml)。
- 本轮仅检查游客态搜索、两条视频详情及字幕的登录要求，不代表全部接口已测。
