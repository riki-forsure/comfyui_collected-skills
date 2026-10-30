# 检索覆盖、公开接口与限制

> 后续补查（2026-10-30 14:40）：aiotieba／Astron游客态专用接口已取得两个吧的原帖，新增6条摘要，并完成MCP stdio实际调用。下文保留初轮02:26前普通网页／HTTP入口受限的历史记录。最新方法及范围见[贴吧工具补查](../tieba-tools.md)。

- 本轮范围：2026-06-30 00:00北京时间至2026-10-30 02:26:31 +08:00。
- 六个gpt-6.1-terra子代理执行来源检索与补核，根代理合并归档。
- 投稿时间、原帖created_utc、资源版本发布与实质提交分别记录；提交作者时间不等于服务器首次公开时间。
- HF-16由仓库创建与含权重的固定快照夹定窗口内资源存在，首次公开的确切时刻未知。
- 当前模型卡、简介和文章可能在发布后继续更新，不能把当前文本全部归于初始版本。

本轮平台读取于北京时间02:19—02:26完成，09:12汇总归档；未声称在02:26以后再次检索新增内容。

## 访问与读取范围

- 当前会话已读取Browser技能并检索工具，但无可调用本地浏览器连接，未接入用户电脑登录态、未取得凭据。
- 公开HTTP/API补查取得B站、Reddit和Civitai资料；贴吧吧页、移动入口、作者主页及普通curl仍403。
- B站17条核公开作者/投稿时间/当前简介，未看视频、字幕、画面或评论。
- Reddit13条以原帖created_utc核日期；另5条有正文线索但原始日期仍待核。
- Civitai模型/版本元数据与15篇文章正文有公开接口依据；文章附件和评论未核。
- 两张Civitai公开示范有单例观察（CV-13、CV-14）；其他画风多为作者说明、例图未核。
- 未下载大模型、安装节点、生图或实际复跑；没有本库效果验收。

## 按来源实际记录

### 百度贴吧（指定两吧）

| 实际查询／入口 | 检查时间 | 状态 | 阅读范围与备注 |
|---|---|---|---|
| [stable diffusion/stablediffusion吧 六月底、七月、八月、九月、十月 × 模型、工作流、画师串、LoRA](https://tieba.baidu.com/f?kw=stablediffusion) | 2026-10-30 02:19:14 +08:00 | 受限 | 公开搜索结果与主页索引摘要；打开贴吧页面返回 HTTP 403；吧页 403；公开搜索主要索引作者主页，旧帖多；未取得合格原帖 |
| [comfyui吧 七月、八月、九月、十月 × 工作流、节点、教程、分享](https://tieba.baidu.com/f?kw=comfyui) | 2026-10-30 02:19:14 +08:00 | 受限 | 公开搜索结果与主页索引摘要；打开贴吧页面返回 HTTP 403；吧页 403；搜索获得一条 CLIP 报错求助的主页摘要，未取得具体帖子链接或解答，不列为有效分享 |
| 精确标题追查 NovelAI v5、Krea 2 训练及人物 LoRA（原帖链接未取得） | 2026-10-30 02:19:14 +08:00 | 受限 | 公开搜索结果与主页索引摘要；打开贴吧页面返回 HTTP 403；只返回作者主页索引，无具体主题链接；N问一不知两条吧归属未证实 |
| site:tieba.baidu.com/p/ "stablediffusion吧" "2026-07" 模型 分享（原帖链接未取得） | 2026-10-30 02:21:44 +08:00 | 未找到合格原帖 | 搜索结果摘要；引擎返回作者主页、旧帖或无关结果；未取得符合条件的具体主题链接。 |
| site:tieba.baidu.com/p/ "stablediffusion吧" "2026-08" 画师串 LoRA（原帖链接未取得） | 2026-10-30 02:21:44 +08:00 | 未找到合格原帖 | 搜索结果摘要；引擎返回作者主页、旧帖或无关结果；未取得符合条件的具体主题链接。 |
| site:tieba.baidu.com/p/ "stablediffusion吧" "2026-09" 工作流 教程（原帖链接未取得） | 2026-10-30 02:21:44 +08:00 | 未找到合格原帖 | 搜索结果摘要；引擎返回作者主页、旧帖或无关结果；未取得符合条件的具体主题链接。 |
| site:tieba.baidu.com/p/ "stablediffusion吧" "2026-10" 模型 分享（原帖链接未取得） | 2026-10-30 02:21:44 +08:00 | 未找到合格原帖 | 搜索结果摘要；引擎返回作者主页、旧帖或无关结果；未取得符合条件的具体主题链接。 |
| site:tieba.baidu.com/p/ "comfyui吧" "2026-07" 工作流 教程（原帖链接未取得） | 2026-10-30 02:21:44 +08:00 | 未找到合格原帖 | 搜索结果摘要；引擎返回作者主页、旧帖或无关结果；未取得符合条件的具体主题链接。 |
| site:tieba.baidu.com/p/ "comfyui吧" "2026-08" 模型 节点（原帖链接未取得） | 2026-10-30 02:21:44 +08:00 | 未找到合格原帖 | 搜索结果摘要；引擎返回作者主页、旧帖或无关结果；未取得符合条件的具体主题链接。 |
| site:tieba.baidu.com/p/ "comfyui吧" "2026-09" 工作流 分享（原帖链接未取得） | 2026-10-30 02:21:44 +08:00 | 未找到合格原帖 | 搜索结果摘要；引擎返回作者主页、旧帖或无关结果；未取得符合条件的具体主题链接。 |
| site:tieba.baidu.com/p/ "comfyui吧" "2026-10" 教程 节点（原帖链接未取得） | 2026-10-30 02:21:44 +08:00 | 未找到合格原帖 | 搜索结果摘要；引擎返回作者主页、旧帖或无关结果；未取得符合条件的具体主题链接。 |
| [Python 标准库 urllib 公开 HTTP GET，普通 Mozilla 用户代理](https://tieba.baidu.com/f?kw=stablediffusion) | 2026-10-30 02:24:38 +08:00 | HTTP 403 | HTTP 状态；未取得正文；未经登录且未处理凭据。 |
| [Python 标准库 urllib 公开 HTTP GET，普通 Mozilla 用户代理](https://tieba.baidu.com/f?kw=comfyui) | 2026-10-30 02:24:38 +08:00 | HTTP 403 | HTTP 状态；未取得正文；未经登录且未处理凭据。 |
| [Python 标准库 urllib 公开 HTTP GET，普通 Mozilla 用户代理](https://wapp.baidu.com/f?kw=stablediffusion) | 2026-10-30 02:24:38 +08:00 | HTTP 403 | HTTP 状态；未取得正文；未经登录且未处理凭据。 |
| [Python 标准库 urllib 公开 HTTP GET，普通 Mozilla 用户代理](https://tieba.baidu.com/mo/q---/m?kw=stablediffusion) | 2026-10-30 02:24:38 +08:00 | HTTP 403 | HTTP 状态；未取得正文；未经登录且未处理凭据。 |
| [Python 标准库 urllib 公开 HTTP GET，普通 Mozilla 用户代理](https://tieba.baidu.com/p/7768044181) | 2026-10-30 02:24:38 +08:00 | HTTP 403 | HTTP 状态；未取得正文；未经登录且未处理凭据。主题号仅为主页摘要里视频链接的 ptid 测试，不证明相关候选或主题内容。 |
| [curl -L --max-time 12 常规公开 GET](https://tieba.baidu.com/f?kw=stablediffusion) | 2026-10-30 02:26:31 +08:00 | HTTP 403 | HTTP 状态及响应大小，未取得主题正文；无登录态、未处理凭据；curl 退出码 0 仅表明 HTTP 请求完成。 |
| [curl -L --max-time 12 常规公开 GET](https://tieba.baidu.com/f?kw=comfyui) | 2026-10-30 02:26:31 +08:00 | HTTP 403 | HTTP 状态及响应大小，未取得主题正文；无登录态、未处理凭据；curl 退出码 0 仅表明 HTTP 请求完成。 |
| [curl -L --max-time 12 常规公开 GET](https://wapp.baidu.com/f?kw=stablediffusion) | 2026-10-30 02:26:31 +08:00 | HTTP 403 | HTTP 状态及响应大小，未取得主题正文；无登录态、未处理凭据；curl 退出码 0 仅表明 HTTP 请求完成。 |
| [curl -L --max-time 12 常规公开 GET](https://tieba.baidu.com/mo/q---/m?kw=stablediffusion) | 2026-10-30 02:26:31 +08:00 | HTTP 403 | HTTP 状态及响应大小，未取得主题正文；无登录态、未处理凭据；curl 退出码 0 仅表明 HTTP 请求完成。 |
| [curl -L --max-time 12 常规公开 GET](https://tieba.baidu.com/home/main?fr=pb&id=tb.1.2a1c6f63.M57GAqD9H3reRZWJLusaUg%3Ft%3D1529435815) | 2026-10-30 02:26:31 +08:00 | HTTP 403 | HTTP 状态及响应大小，未取得主题正文；无登录态、未处理凭据；curl 退出码 0 仅表明 HTTP 请求完成。 |
| [curl -L --max-time 12 常规公开 GET](https://tieba.baidu.com/home/main/?fr=hottopic&ie=utf-8&un=N%E9%97%AE%E4%B8%80%E4%B8%8D%E7%9F%A5) | 2026-10-30 02:26:31 +08:00 | HTTP 403 | HTTP 状态及响应大小，未取得主题正文；无登录态、未处理凭据；curl 退出码 0 仅表明 HTTP 请求完成。 |

- 排除或限制：[搜索摘要里的 ComfyUI 节点缺失条目实际为 2025-06-23，超出窗口。](https://tieba.baidu.com/home/main?fr=home&id=tb.1.d25b3ea6.9F8ao37X9B1_XfikDRhi4A&un=%E7%A5%81%E7%BF%A0%E6%B3%99)
### bilibili

| 实际查询／入口 | 检查时间 | 状态 | 阅读范围与备注 |
|---|---|---|---|
| [视频元数据 BV1VKe46XEsP](https://api.bilibili.com/x/web-interface/view?bvid=BV1VKe46XEsP) | 2026-10-30T02:20:51+08:00 | HTTP 412; HTTP Error 412: Precondition Failed | 接口未取得有效内容；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1s1HL6VE8Q](https://api.bilibili.com/x/web-interface/view?bvid=BV1s1HL6VE8Q) | 2026-10-30T02:20:51+08:00 | HTTP 412; HTTP Error 412: Precondition Failed | 接口未取得有效内容；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV11SNq6wEvP](https://api.bilibili.com/x/web-interface/view?bvid=BV11SNq6wEvP) | 2026-10-30T02:20:51+08:00 | HTTP 412; HTTP Error 412: Precondition Failed | 接口未取得有效内容；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV18UNT6HErn](https://api.bilibili.com/x/web-interface/view?bvid=BV18UNT6HErn) | 2026-10-30T02:20:51+08:00 | HTTP 412; HTTP Error 412: Precondition Failed | 接口未取得有效内容；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1n9MM6mE29](https://api.bilibili.com/x/web-interface/view?bvid=BV1n9MM6mE29) | 2026-10-30T02:20:51+08:00 | HTTP 412; HTTP Error 412: Precondition Failed | 接口未取得有效内容；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV11Eb26mEo9](https://api.bilibili.com/x/web-interface/view?bvid=BV11Eb26mEo9) | 2026-10-30T02:20:51+08:00 | HTTP 412; HTTP Error 412: Precondition Failed | 接口未取得有效内容；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1H3gp68E3R](https://api.bilibili.com/x/web-interface/view?bvid=BV1H3gp68E3R) | 2026-10-30T02:20:51+08:00 | HTTP 412; HTTP Error 412: Precondition Failed | 接口未取得有效内容；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1hF4X6MEqt](https://api.bilibili.com/x/web-interface/view?bvid=BV1hF4X6MEqt) | 2026-10-30T02:20:51+08:00 | HTTP 412; HTTP Error 412: Precondition Failed | 接口未取得有效内容；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1kReD6TEVb](https://api.bilibili.com/x/web-interface/view?bvid=BV1kReD6TEVb) | 2026-10-30T02:20:51+08:00 | HTTP 412; HTTP Error 412: Precondition Failed | 接口未取得有效内容；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1nSY76BEuu](https://api.bilibili.com/x/web-interface/view?bvid=BV1nSY76BEuu) | 2026-10-30T02:20:51+08:00 | HTTP 412; HTTP Error 412: Precondition Failed | 接口未取得有效内容；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1oZap6CE8m](https://api.bilibili.com/x/web-interface/view?bvid=BV1oZap6CE8m) | 2026-10-30T02:20:51+08:00 | HTTP 412; HTTP Error 412: Precondition Failed | 接口未取得有效内容；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1fKpB6wEx4](https://api.bilibili.com/x/web-interface/view?bvid=BV1fKpB6wEx4) | 2026-10-30T02:20:51+08:00 | HTTP 412; HTTP Error 412: Precondition Failed | 接口未取得有效内容；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV18Xp86ZEH1](https://api.bilibili.com/x/web-interface/view?bvid=BV18Xp86ZEH1) | 2026-10-30T02:20:51+08:00 | HTTP 412; HTTP Error 412: Precondition Failed | 接口未取得有效内容；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1gGHv6BE38](https://api.bilibili.com/x/web-interface/view?bvid=BV1gGHv6BE38) | 2026-10-30T02:20:51+08:00 | HTTP 412; HTTP Error 412: Precondition Failed | 接口未取得有效内容；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1YDeB6HEg8](https://api.bilibili.com/x/web-interface/view?bvid=BV1YDeB6HEg8) | 2026-10-30T02:20:51+08:00 | HTTP 412; HTTP Error 412: Precondition Failed | 接口未取得有效内容；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1pKN96iEso](https://api.bilibili.com/x/web-interface/view?bvid=BV1pKN96iEso) | 2026-10-30T02:20:51+08:00 | HTTP 412; HTTP Error 412: Precondition Failed | 接口未取得有效内容；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV14Cuj6nE5T](https://api.bilibili.com/x/web-interface/view?bvid=BV14Cuj6nE5T) | 2026-10-30T02:20:51+08:00 | HTTP 412; HTTP Error 412: Precondition Failed | 接口未取得有效内容；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1VKe46XEsP](https://api.bilibili.com/x/web-interface/view?bvid=BV1VKe46XEsP) | 2026-10-30T02:21:01+08:00 | HTTP 200; code 0 | 公开元数据标题、投稿人、pubdate、简介；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1s1HL6VE8Q](https://api.bilibili.com/x/web-interface/view?bvid=BV1s1HL6VE8Q) | 2026-10-30T02:21:01+08:00 | HTTP 200; code 0 | 公开元数据标题、投稿人、pubdate、简介；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV11SNq6wEvP](https://api.bilibili.com/x/web-interface/view?bvid=BV11SNq6wEvP) | 2026-10-30T02:21:01+08:00 | HTTP 200; code 0 | 公开元数据标题、投稿人、pubdate、简介；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV18UNT6HErn](https://api.bilibili.com/x/web-interface/view?bvid=BV18UNT6HErn) | 2026-10-30T02:21:01+08:00 | HTTP 200; code 0 | 公开元数据标题、投稿人、pubdate、简介；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1n9MM6mE29](https://api.bilibili.com/x/web-interface/view?bvid=BV1n9MM6mE29) | 2026-10-30T02:21:01+08:00 | HTTP 200; code 0 | 公开元数据标题、投稿人、pubdate、简介；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV11Eb26mEo9](https://api.bilibili.com/x/web-interface/view?bvid=BV11Eb26mEo9) | 2026-10-30T02:21:01+08:00 | HTTP 200; code 0 | 公开元数据标题、投稿人、pubdate、简介；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1H3gp68E3R](https://api.bilibili.com/x/web-interface/view?bvid=BV1H3gp68E3R) | 2026-10-30T02:21:01+08:00 | HTTP 200; code 0 | 公开元数据标题、投稿人、pubdate、简介；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1hF4X6MEqt](https://api.bilibili.com/x/web-interface/view?bvid=BV1hF4X6MEqt) | 2026-10-30T02:21:01+08:00 | HTTP 200; code 0 | 公开元数据标题、投稿人、pubdate、简介；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1kReD6TEVb](https://api.bilibili.com/x/web-interface/view?bvid=BV1kReD6TEVb) | 2026-10-30T02:21:01+08:00 | HTTP 200; code 0 | 公开元数据标题、投稿人、pubdate、简介；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1nSY76BEuu](https://api.bilibili.com/x/web-interface/view?bvid=BV1nSY76BEuu) | 2026-10-30T02:21:01+08:00 | HTTP 200; code 0 | 公开元数据标题、投稿人、pubdate、简介；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1oZap6CE8m](https://api.bilibili.com/x/web-interface/view?bvid=BV1oZap6CE8m) | 2026-10-30T02:21:01+08:00 | HTTP 200; code 0 | 公开元数据标题、投稿人、pubdate、简介；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1fKpB6wEx4](https://api.bilibili.com/x/web-interface/view?bvid=BV1fKpB6wEx4) | 2026-10-30T02:21:01+08:00 | HTTP 200; code 0 | 公开元数据标题、投稿人、pubdate、简介；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV18Xp86ZEH1](https://api.bilibili.com/x/web-interface/view?bvid=BV18Xp86ZEH1) | 2026-10-30T02:21:01+08:00 | HTTP 200; code 0 | 公开元数据标题、投稿人、pubdate、简介；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1gGHv6BE38](https://api.bilibili.com/x/web-interface/view?bvid=BV1gGHv6BE38) | 2026-10-30T02:21:01+08:00 | HTTP 200; code 0 | 公开元数据标题、投稿人、pubdate、简介；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1YDeB6HEg8](https://api.bilibili.com/x/web-interface/view?bvid=BV1YDeB6HEg8) | 2026-10-30T02:21:01+08:00 | HTTP 200; code 0 | 公开元数据标题、投稿人、pubdate、简介；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV1pKN96iEso](https://api.bilibili.com/x/web-interface/view?bvid=BV1pKN96iEso) | 2026-10-30T02:21:01+08:00 | HTTP 200; code 0 | 公开元数据标题、投稿人、pubdate、简介；未观看视频、字幕、画面或评论。 |
| [视频元数据 BV14Cuj6nE5T](https://api.bilibili.com/x/web-interface/view?bvid=BV14Cuj6nE5T) | 2026-10-30T02:21:01+08:00 | HTTP 200; code 0 | 公开元数据标题、投稿人、pubdate、简介；未观看视频、字幕、画面或评论。 |
| [site:bilibili.com/video/ ComfyUI 2026年10月 工作流 生图](https://www.google.com/search?q=site%3Abilibili.com/video/%20ComfyUI%202026%E5%B9%B410%E6%9C%88%20%E5%B7%A5%E4%BD%9C%E6%B5%81%20%E7%94%9F%E5%9B%BE) | 2026-10-30T02:21:46+08:00 | 搜索引擎查询；部分命中 | 标题与摘要；命中视频另经元数据API核对；搜索接口实际执行该查询；链接为可重查的查询入口。 |
| [site:bilibili.com/video/ ComfyUI 2026年9月 绘画 教程](https://www.google.com/search?q=site%3Abilibili.com/video/%20ComfyUI%202026%E5%B9%B49%E6%9C%88%20%E7%BB%98%E7%94%BB%20%E6%95%99%E7%A8%8B) | 2026-10-30T02:21:46+08:00 | 搜索引擎查询；部分命中 | 标题与摘要；命中视频另经元数据API核对；搜索接口实际执行该查询；链接为可重查的查询入口。 |
| [site:bilibili.com/video/ Anima Illustrious 2026年8月 绘画](https://www.google.com/search?q=site%3Abilibili.com/video/%20Anima%20Illustrious%202026%E5%B9%B48%E6%9C%88%20%E7%BB%98%E7%94%BB) | 2026-10-30T02:21:46+08:00 | 搜索引擎查询；部分命中 | 标题与摘要；命中视频另经元数据API核对；搜索接口实际执行该查询；链接为可重查的查询入口。 |
| [site:bilibili.com/video/ NoobAI 2026年7月 工作流](https://www.google.com/search?q=site%3Abilibili.com/video/%20NoobAI%202026%E5%B9%B47%E6%9C%88%20%E5%B7%A5%E4%BD%9C%E6%B5%81) | 2026-10-30T02:21:46+08:00 | 搜索引擎查询；部分命中 | 标题与摘要；命中视频另经元数据API核对；搜索接口实际执行该查询；链接为可重查的查询入口。 |
| [site:bilibili.com/video/ "Anima" "2026-10" 工作流](https://www.google.com/search?q=site%3Abilibili.com/video/%20%22Anima%22%20%222026-10%22%20%E5%B7%A5%E4%BD%9C%E6%B5%81) | 2026-10-30T02:21:46+08:00 | 搜索引擎查询；部分命中 | 标题与摘要；命中视频另经元数据API核对；搜索接口实际执行该查询；链接为可重查的查询入口。 |
| [site:bilibili.com/video/ "Anima" "2026-09" 提示词](https://www.google.com/search?q=site%3Abilibili.com/video/%20%22Anima%22%20%222026-09%22%20%E6%8F%90%E7%A4%BA%E8%AF%8D) | 2026-10-30T02:21:46+08:00 | 搜索引擎查询；部分命中 | 标题与摘要；命中视频另经元数据API核对；搜索接口实际执行该查询；链接为可重查的查询入口。 |
| [site:bilibili.com/video/ "Anima" "2026-08" 绘画](https://www.google.com/search?q=site%3Abilibili.com/video/%20%22Anima%22%20%222026-08%22%20%E7%BB%98%E7%94%BB) | 2026-10-30T02:21:46+08:00 | 搜索引擎查询；部分命中 | 标题与摘要；命中视频另经元数据API核对；搜索接口实际执行该查询；链接为可重查的查询入口。 |
| [site:bilibili.com/video/ "Anima" "2026-07" comfyui](https://www.google.com/search?q=site%3Abilibili.com/video/%20%22Anima%22%20%222026-07%22%20comfyui) | 2026-10-30T02:21:46+08:00 | 搜索引擎查询；部分命中 | 标题与摘要；命中视频另经元数据API核对；搜索接口实际执行该查询；链接为可重查的查询入口。 |
| [site:bilibili.com/video/ "2026-10" ComfyUI 生图 工作流](https://www.google.com/search?q=site%3Abilibili.com/video/%20%222026-10%22%20ComfyUI%20%E7%94%9F%E5%9B%BE%20%E5%B7%A5%E4%BD%9C%E6%B5%81) | 2026-10-30T02:21:46+08:00 | 搜索引擎查询；部分命中 | 标题与摘要；命中视频另经元数据API核对；搜索接口实际执行该查询；链接为可重查的查询入口。 |
| [site:bilibili.com/video/ "2026-09" ComfyUI 人物 工作流](https://www.google.com/search?q=site%3Abilibili.com/video/%20%222026-09%22%20ComfyUI%20%E4%BA%BA%E7%89%A9%20%E5%B7%A5%E4%BD%9C%E6%B5%81) | 2026-10-30T02:21:46+08:00 | 搜索引擎查询；部分命中 | 标题与摘要；命中视频另经元数据API核对；搜索接口实际执行该查询；链接为可重查的查询入口。 |
| [site:bilibili.com/video/ "2026-08" ComfyUI 提示词 绘画](https://www.google.com/search?q=site%3Abilibili.com/video/%20%222026-08%22%20ComfyUI%20%E6%8F%90%E7%A4%BA%E8%AF%8D%20%E7%BB%98%E7%94%BB) | 2026-10-30T02:21:46+08:00 | 搜索引擎查询；部分命中 | 标题与摘要；命中视频另经元数据API核对；搜索接口实际执行该查询；链接为可重查的查询入口。 |
| [site:bilibili.com/video/ "2026-07" ComfyUI 图像 控制](https://www.google.com/search?q=site%3Abilibili.com/video/%20%222026-07%22%20ComfyUI%20%E5%9B%BE%E5%83%8F%20%E6%8E%A7%E5%88%B6) | 2026-10-30T02:21:46+08:00 | 搜索引擎查询；部分命中 | 标题与摘要；命中视频另经元数据API核对；搜索接口实际执行该查询；链接为可重查的查询入口。 |
| [site:bilibili.com/video/ "2026-10" AI绘画 LoRA 教程](https://www.google.com/search?q=site%3Abilibili.com/video/%20%222026-10%22%20AI%E7%BB%98%E7%94%BB%20LoRA%20%E6%95%99%E7%A8%8B) | 2026-10-30T02:21:46+08:00 | 搜索引擎查询；部分命中 | 标题与摘要；命中视频另经元数据API核对；搜索接口实际执行该查询；链接为可重查的查询入口。 |
| [site:bilibili.com/video/ "2026-09" 光辉 模型 绘画](https://www.google.com/search?q=site%3Abilibili.com/video/%20%222026-09%22%20%E5%85%89%E8%BE%89%20%E6%A8%A1%E5%9E%8B%20%E7%BB%98%E7%94%BB) | 2026-10-30T02:21:46+08:00 | 搜索引擎查询；部分命中 | 标题与摘要；命中视频另经元数据API核对；搜索接口实际执行该查询；链接为可重查的查询入口。 |
| [site:bilibili.com/video/ "2026-08" NoobAI 绘画](https://www.google.com/search?q=site%3Abilibili.com/video/%20%222026-08%22%20NoobAI%20%E7%BB%98%E7%94%BB) | 2026-10-30T02:21:46+08:00 | 搜索引擎查询；部分命中 | 标题与摘要；命中视频另经元数据API核对；搜索接口实际执行该查询；链接为可重查的查询入口。 |
| [site:bilibili.com/video/ "2026-07" Illustrious 绘画](https://www.google.com/search?q=site%3Abilibili.com/video/%20%222026-07%22%20Illustrious%20%E7%BB%98%E7%94%BB) | 2026-10-30T02:21:46+08:00 | 搜索引擎查询；部分命中 | 标题与摘要；命中视频另经元数据API核对；搜索接口实际执行该查询；链接为可重查的查询入口。 |

### Reddit

| 实际查询／入口 | 检查时间 | 状态 | 阅读范围与备注 |
|---|---|---|---|
| [site:reddit.com/r/StableDiffusion/ 2026 July workflow lora tutorial](https://www.reddit.com/) | 2026-10-29T18:20:22.770121+00:00 | 搜索并筛选 | 搜索结果；部分结果另打开具体 Reddit 正文；搜索服务日期与原帖绝对时间尚待独立核实 |
| [site:reddit.com/r/comfyui/ July 2026 workflow tutorial](https://www.reddit.com/) | 2026-10-29T18:20:22.770121+00:00 | 搜索并筛选 | 搜索结果；部分结果另打开具体 Reddit 正文；搜索服务日期与原帖绝对时间尚待独立核实 |
| [site:reddit.com/r/StableDiffusion/ August 2026 prompt workflow](https://www.reddit.com/) | 2026-10-29T18:20:22.770121+00:00 | 搜索并筛选 | 搜索结果；部分结果另打开具体 Reddit 正文；搜索服务日期与原帖绝对时间尚待独立核实 |
| [site:reddit.com/r/comfyui/ August 2026 lora workflow](https://www.reddit.com/) | 2026-10-29T18:20:22.770121+00:00 | 搜索并筛选 | 搜索结果；部分结果另打开具体 Reddit 正文；搜索服务日期与原帖绝对时间尚待独立核实 |
| [site:reddit.com/r/StableDiffusion/ September 2026 workflow lora](https://www.reddit.com/) | 2026-10-29T18:20:22.770121+00:00 | 搜索并筛选 | 搜索结果；部分结果另打开具体 Reddit 正文；搜索服务日期与原帖绝对时间尚待独立核实 |
| [site:reddit.com/r/comfyui/ September 2026 tutorial workflow](https://www.reddit.com/) | 2026-10-29T18:20:22.770121+00:00 | 搜索并筛选 | 搜索结果；部分结果另打开具体 Reddit 正文；搜索服务日期与原帖绝对时间尚待独立核实 |
| [site:reddit.com/r/StableDiffusion/ October 2026 prompt tutorial](https://www.reddit.com/) | 2026-10-29T18:20:22.770121+00:00 | 搜索并筛选 | 搜索结果；部分结果另打开具体 Reddit 正文；搜索服务日期与原帖绝对时间尚待独立核实 |
| [site:reddit.com/r/comfyui/ October 2026 workflow](https://www.reddit.com/) | 2026-10-29T18:20:22.770121+00:00 | 搜索并筛选 | 搜索结果；部分结果另打开具体 Reddit 正文；搜索服务日期与原帖绝对时间尚待独立核实 |
| [site:reddit.com/r/StableDiffusion/ June 30 2026 tutorial lora](https://www.reddit.com/) | 2026-10-29T18:20:22.770121+00:00 | 搜索并筛选 | 搜索结果；部分结果另打开具体 Reddit 正文；搜索服务日期与原帖绝对时间尚待独立核实 |
| [site:reddit.com/r/StableDiffusion/ 2026 artist style mixing characters composition](https://www.reddit.com/) | 2026-10-29T18:20:22.770121+00:00 | 搜索并筛选 | 搜索结果；部分结果另打开具体 Reddit 正文；搜索服务日期与原帖绝对时间尚待独立核实 |
| [site:reddit.com/r/comfyui/ 2026 faces expressions prompt detail](https://www.reddit.com/) | 2026-10-29T18:20:22.770121+00:00 | 搜索并筛选 | 搜索结果；部分结果另打开具体 Reddit 正文；搜索服务日期与原帖绝对时间尚待独立核实 |
| [site:reddit.com/r/StableDiffusion/ 2026 training lora finetune guide](https://www.reddit.com/) | 2026-10-29T18:20:22.770121+00:00 | 搜索并筛选 | 搜索结果；部分结果另打开具体 Reddit 正文；搜索服务日期与原帖绝对时间尚待独立核实 |
| [site:reddit.com/r/StableDiffusion/comments/ "July" "2026" "workflow" prompt Krea](https://www.reddit.com/) | 2026-10-29T18:22:07.184230+00:00 | 已搜索并筛选 | 搜索结果；命中另打开正文和部分评论；日期用公开 JSON created_utc 核对；无法读取时保留搜索日期候选 |
| [site:reddit.com/r/StableDiffusion/comments/ "July" "2026" "LoRA" training dataset](https://www.reddit.com/) | 2026-10-29T18:22:07.184230+00:00 | 已搜索并筛选 | 搜索结果；命中另打开正文和部分评论；日期用公开 JSON created_utc 核对；无法读取时保留搜索日期候选 |
| [site:reddit.com/r/comfyui/comments/ "August" "2026" "image" "workflow"](https://www.reddit.com/) | 2026-10-29T18:22:07.184230+00:00 | 已搜索并筛选 | 搜索结果；命中另打开正文和部分评论；日期用公开 JSON created_utc 核对；无法读取时保留搜索日期候选 |
| [site:reddit.com/r/StableDiffusion/comments/ "August" "2026" "workflow" image](https://www.reddit.com/) | 2026-10-29T18:22:07.184230+00:00 | 已搜索并筛选 | 搜索结果；命中另打开正文和部分评论；日期用公开 JSON created_utc 核对；无法读取时保留搜索日期候选 |
| [site:reddit.com/r/StableDiffusion/comments/ "September" "2026" "workflow" prompt](https://www.reddit.com/) | 2026-10-29T18:22:07.184230+00:00 | 已搜索并筛选 | 搜索结果；命中另打开正文和部分评论；日期用公开 JSON created_utc 核对；无法读取时保留搜索日期候选 |
| [site:reddit.com/r/comfyui/comments/ "September" "2026" "workflow" image editing](https://www.reddit.com/) | 2026-10-29T18:22:07.184230+00:00 | 已搜索并筛选 | 搜索结果；命中另打开正文和部分评论；日期用公开 JSON created_utc 核对；无法读取时保留搜索日期候选 |
| [site:reddit.com/r/StableDiffusion/comments/ "September" "2026" "training" lora](https://www.reddit.com/) | 2026-10-29T18:22:07.184230+00:00 | 已搜索并筛选 | 搜索结果；命中另打开正文和部分评论；日期用公开 JSON created_utc 核对；无法读取时保留搜索日期候选 |
| [site:reddit.com/r/comfyui/comments/ "September" "2026" "character" workflow](https://www.reddit.com/) | 2026-10-29T18:22:07.184230+00:00 | 已搜索并筛选 | 搜索结果；命中另打开正文和部分评论；日期用公开 JSON created_utc 核对；无法读取时保留搜索日期候选 |
| [site:reddit.com/r/StableDiffusion/comments/ "June 30 2026" image workflow](https://www.reddit.com/) | 2026-10-29T18:22:07.184230+00:00 | 已搜索并筛选 | 搜索结果；命中另打开正文和部分评论；日期用公开 JSON created_utc 核对；无法读取时保留搜索日期候选 |
| [site:reddit.com/r/comfyui/comments/ "June 30 2026" workflow image](https://www.reddit.com/) | 2026-10-29T18:22:07.184230+00:00 | 已搜索并筛选 | 搜索结果；命中另打开正文和部分评论；日期用公开 JSON created_utc 核对；无法读取时保留搜索日期候选 |
| [site:reddit.com/r/StableDiffusion/comments/ "October" "2026" "prompt" image](https://www.reddit.com/) | 2026-10-29T18:22:07.184230+00:00 | 已搜索并筛选 | 搜索结果；命中另打开正文和部分评论；日期用公开 JSON created_utc 核对；无法读取时保留搜索日期候选 |
| [site:reddit.com/r/comfyui/comments/ "October" "2026" "portrait" workflow](https://www.reddit.com/) | 2026-10-29T18:22:07.184230+00:00 | 已搜索并筛选 | 搜索结果；命中另打开正文和部分评论；日期用公开 JSON created_utc 核对；无法读取时保留搜索日期候选 |
| [Reddit 公开帖子 JSON .json?limit=0 和 old.reddit.com](https://www.reddit.com/r/StableDiffusion/comments/1ulonm8/.json?limit=0) | 2026-10-29T18:22:07.184230+00:00 | 部分成功 | 公开 Reddit JSON 原帖 created_utc 字段；old 页面工具不可访问；直接网络 curl 被拦；部分 JSON 因超长截断或输出定位问题无法核原帖时间，不以评论时间代替。 |

- 排除或限制：[搜索结果原帖日期 2026-06-24，早于窗口](https://www.reddit.com/r/comfyui/comments/1uedjfi/comfyui_v0260/)
### Hugging Face

| 实际查询／入口 | 检查时间 | 状态 | 阅读范围与备注 |
|---|---|---|---|
| [HF API 模型搜索 anima，按 likes 排序前100](https://huggingface.co/models?search=anima) | 2026-10-29T18:20:43.833424+00:00 | 已检查 | API结果与选中模型卡、提交历史；按热度前100并非全量；个别模型卡无读取权限。 |
| [HF API 模型搜索 anisee，按 likes 排序前100](https://huggingface.co/models?search=anisee) | 2026-10-29T18:20:43.833424+00:00 | 已检查 | API结果与选中模型卡、提交历史；按热度前100并非全量；个别模型卡无读取权限。 |
| [HF API 模型搜索 illustrious，按 likes 排序前100](https://huggingface.co/models?search=illustrious) | 2026-10-29T18:20:43.833424+00:00 | 已检查 | API结果与选中模型卡、提交历史；按热度前100并非全量；个别模型卡无读取权限。 |
| [HF API 模型搜索 noobai，按 likes 排序前100](https://huggingface.co/models?search=noobai) | 2026-10-29T18:20:43.833424+00:00 | 已检查 | API结果与选中模型卡、提交历史；按热度前100并非全量；个别模型卡无读取权限。 |
| [HF API 模型搜索 flux，按 likes 排序前100](https://huggingface.co/models?search=flux) | 2026-10-29T18:20:43.833424+00:00 | 已检查 | API结果与选中模型卡、提交历史；按热度前100并非全量；个别模型卡无读取权限。 |
| [HF API 模型搜索 qwen-image，按 likes 排序前100](https://huggingface.co/models?search=qwen-image) | 2026-10-29T18:20:43.833424+00:00 | 已检查 | API结果与选中模型卡、提交历史；按热度前100并非全量；个别模型卡无读取权限。 |
| [HF API 模型搜索 image lora，按 likes 排序前100](https://huggingface.co/models?search=image lora) | 2026-10-29T18:20:43.833424+00:00 | 已检查 | API结果与选中模型卡、提交历史；按热度前100并非全量；个别模型卡无读取权限。 |

- 排除或限制：[复制仓库；原始作者 SeeSee21，原始V1早于窗口，V2实质更新已另收。](https://huggingface.co/qwrdfsdc/AniSee)
- 排除或限制：[模型卡和提交历史401，放弃将仓库创建视为发布。](https://huggingface.co/black-forest-labs/flux-3-image-klein-base)
### GitHub

| 实际查询／入口 | 检查时间 | 状态 | 阅读范围与备注 |
|---|---|---|---|
| [comfyui artist mixer created:2026-06-29..2026-10-30](https://api.github.com/search/repositories?q=comfyui+artist+mixer+created:2026-06-29..2026-10-30) | 2026-10-29T18:21:11+00:00 | 已检索 | 仓库搜索结果；候选进一步读取 commits API 和历史 README；仓库创建日期仅用于发现，不等于工作流发布日期。 |
| [comfyui regional prompt created:2026-06-29..2026-10-30](https://api.github.com/search/repositories?q=comfyui+regional+prompt+created:2026-06-29..2026-10-30) | 2026-10-29T18:21:11+00:00 | 已检索 | 仓库搜索结果；候选进一步读取 commits API 和历史 README；仓库创建日期仅用于发现，不等于工作流发布日期。 |
| [comfyui style workflow created:2026-06-29..2026-10-30](https://api.github.com/search/repositories?q=comfyui+style+workflow+created:2026-06-29..2026-10-30) | 2026-10-29T18:21:11+00:00 | 已检索 | 仓库搜索结果；候选进一步读取 commits API 和历史 README；仓库创建日期仅用于发现，不等于工作流发布日期。 |
| [comfyui controlnet created:2026-06-29..2026-10-30](https://api.github.com/search/repositories?q=comfyui+controlnet+created:2026-06-29..2026-10-30) | 2026-10-29T18:21:11+00:00 | 已检索 | 仓库搜索结果；候选进一步读取 commits API 和历史 README；仓库创建日期仅用于发现，不等于工作流发布日期。 |
| [comfyui prompt nodes created:2026-06-29..2026-10-30](https://api.github.com/search/repositories?q=comfyui+prompt+nodes+created:2026-06-29..2026-10-30) | 2026-10-29T18:21:11+00:00 | 已检索 | 仓库搜索结果；候选进一步读取 commits API 和历史 README；仓库创建日期仅用于发现，不等于工作流发布日期。 |
| [comfyui detailer workflow created:2026-06-29..2026-10-30](https://api.github.com/search/repositories?q=comfyui+detailer+workflow+created:2026-06-29..2026-10-30) | 2026-10-29T18:21:11+00:00 | 已检索 | 仓库搜索结果；候选进一步读取 commits API 和历史 README；仓库创建日期仅用于发现，不等于工作流发布日期。 |

- 排除或限制：[仓库创建于 5 月，不能直接作为窗口内新仓库；上列仅计实质更新。](https://github.com/An1X3R/Anima-Artist-Mixer)
- 排除或限制：[重复镜像／fork 内容与 Rinne414 Forge 相同，未重复计数。](https://github.com/peter119lee/Anima-Artist-Mixer-Forge)
### Civitai 模型与版本

| 实际查询／入口 | 检查时间 | 状态 | 阅读范围与备注 |
|---|---|---|---|
| [site:civitai.com/articles，July/August/September/October 2026 workflow、LoRA、prompt](https://civitai.com/articles) | 2026-10-30T02:20:19+08:00 | 搜索无结果；入口打开失败 | 搜索摘要及网页打开尝试；不能据此断言没有文章；未取得文章正文。 |
| [site:civitai.com/models Anima、Illustrious；site:civitai.com/articles 工作流、提示词](https://civitai.com/) | 2026-10-30T02:20:19+08:00 | 搜索无结果 | 搜索结果；搜索服务返回空结果。 |
| [公开 API 模型搜索：anima style、illustrious style、workflow、portrait、composition、watercolor、expression、artist mix、noobai、flux](https://civitai.com/api/v1/models?limit=5&sort=Newest) | 2026-10-30T02:20:19+08:00 | 成功 | 搜索返回及指定模型 API 模型卡、版本发布日期和正文；未看图；每个词最多取 40 条，按下载量排序；非全站穷举。API 返回的版本元数据以 UTC 标记。 |
| [具体模型网页打开 2742675、2748901](https://civitai.com/models/2742675?modelVersionId=3428980) | 2026-10-30T02:20:19+08:00 | 网页打开报错 | 页面打开尝试；仅使用无需登录的公开 API，不绕过访问限制。 |

### Civitai 社区文章

| 实际查询／入口 | 检查时间 | 状态 | 阅读范围与备注 |
|---|---|---|---|
| [公开 articles API 按发布时间分页 11 页，标题关键词筛选；逐条读取 18 篇正文](https://civitai.com/api/v1/articles?limit=100) | 2026-10-30T02:25:00+08:00 | 成功 | 列表 1100 条至 2026-06-25；18 篇 API 正文文字；实际筛选15条；未查看附件、例图和评论，不代表全站穷举。 |

### 其他作者技术分享

| 实际查询／入口 | 检查时间 | 状态 | 阅读范围与备注 |
|---|---|---|---|
| site:note.com "ComfyUI" "2026年7月" ワークフロー（原帖链接未取得） | 2026-10-30 02:21:44 +08:00 | 已检索 | 搜索结果及原文可见文字段落；例图、附件、视频和评论未核。 |
| site:note.com "ComfyUI" "2026年8月" LoRA（原帖链接未取得） | 2026-10-30 02:21:44 +08:00 | 已检索 | 搜索结果及原文可见文字段落；例图、附件、视频和评论未核。 |
| site:note.com "ComfyUI" "2026年9月" 画像 生成（原帖链接未取得） | 2026-10-30 02:21:44 +08:00 | 已检索 | 搜索结果及原文可见文字段落；例图、附件、视频和评论未核。 |
| site:note.com "ComfyUI" "2026年10月" ワークフロー（原帖链接未取得） | 2026-10-30 02:21:44 +08:00 | 已检索 | 搜索结果及原文可见文字段落；例图、附件、视频和评论未核。 |
| site:stable-diffusion-art.com 2026 ComfyUI tutorial image（原帖链接未取得） | 2026-10-30 02:21:44 +08:00 | 已检索 | 搜索结果及原文可见文字段落；例图、附件、视频和评论未核。 |
| site:note.com "Anima" 画風 2026 8（原帖链接未取得） | 2026-10-30 02:21:44 +08:00 | 已检索 | 搜索结果及原文可见文字段落；例图、附件、视频和评论未核。 |
