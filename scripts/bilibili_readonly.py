#!/usr/bin/env python3
"""Bounded, read-only Bilibili discovery using bilibili-api-python.

Uses inherited proxy/CA settings. No browser-cookie extraction, QR login,
video/audio download, ASR, or account mutations.
"""
import argparse
import asyncio
from datetime import datetime, timedelta, timezone
import html
from importlib.metadata import version
import json
import os
import re
import sys
import urllib.parse
import urllib.request

BEIJING = timezone(timedelta(hours=8))


def date_text(timestamp):
    return datetime.fromtimestamp(timestamp, BEIJING).isoformat() if timestamp else None


def video_row(data, detail=False):
    bvid = data.get("bvid", "")
    row = {
        "bvid": bvid,
        "url": f"https://www.bilibili.com/video/{bvid}/",
        "title": html.unescape(re.sub(r"<[^>]*>", "", data.get("title", ""))),
        "author": (data.get("owner") or {}).get("name") if detail else data.get("author"),
        "author_uid": (data.get("owner") or {}).get("mid") if detail else data.get("mid"),
        "published_at": date_text(data.get("pubdate")),
        "description": data.get("desc" if detail else "description", ""),
    }
    if detail:
        row.update(duration_seconds=data.get("duration"), pages=[
            {k: page.get(k) for k in ("page", "cid", "part", "duration")}
            for page in data.get("pages", [])
        ])
    return row


async def read(args):
    from bilibili_api import Credential, request_settings, search, user, video

    # aiohttp-backed SDK calls need an explicit proxy in this executor.
    proxy = urllib.request.getproxies().get("https") or urllib.request.getproxies().get("http", "")
    request_settings.set_proxy(proxy)
    request_settings.set_trust_env(True)
    request_settings.set_verify_ssl(True)
    request_settings.set_timeout(15)
    request_settings.set_wbi_retry_times(1)
    if args.mode == "search":
        data = await search.search_by_type(
            args.query, search.SearchObjectType.VIDEO,
            order_type=search.OrderVideo.PUBDATE, page=args.page, page_size=20,
        )
        rows = [video_row(row) for row in data.get("result", [])]
        # Filter this page only; keep page boundaries visible for incremental research.
        page_dates = [row["published_at"] for row in rows if row["published_at"]]
        if args.since:
            rows = [row for row in rows if row["published_at"] and row["published_at"] >= args.since]
        return {"auth_mode": "guest", "query": args.query, "page": args.page,
                "order": "pubdate", "page_date_range": [min(page_dates), max(page_dates)] if page_dates else [],
                "items": rows[:args.limit], "count": len(rows[:args.limit]),
                "scope": "One search page; search descriptions only. Date filtering does not establish complete coverage."}
    cred = Credential(sessdata=os.environ.get("BILIBILI_SESSDATA") or None)
    if args.mode == "uploader":
        data = await user.User(args.uid, credential=cred).get_videos(
            pn=args.page, ps=30, keyword=args.query or "", order=user.VideoOrder.PUBDATE,
        )
        rows = [video_row(dict(row, pubdate=row.get("created")))
                for row in data.get("list", {}).get("vlist", [])]
        dates = [row["published_at"] for row in rows if row["published_at"]]
        if args.since:
            rows = [row for row in rows if row["published_at"] and row["published_at"] >= args.since]
        return {"auth_mode": "provided_session" if cred.sessdata else "guest",
                "uid": args.uid, "query": args.query or "", "page": data.get("page"),
                "page_date_range": [min(dates), max(dates)] if dates else [],
                "items": rows[:args.limit], "count": len(rows[:args.limit]),
                "scope": "One uploader page, optionally keyword-filtered; metadata only. Check page count before claiming series coverage."}
    if args.mode == "subtitle" and not cred.sessdata:
        return {"auth_mode": "guest", "status": "login_required", "segments": [],
                "scope": "No subtitle obtained. BILIBILI_SESSDATA is not configured; no login or cookie extraction attempted."}
    obj = video.Video(bvid=args.bvid, credential=cred)
    info = await obj.get_info()
    row = video_row(info, detail=True)
    if args.mode == "info":
        return {"auth_mode": "provided_session" if cred.sessdata else "guest", "video": row,
                "scope": "Video metadata, full description and page list only; no subtitle, comments or frames read."}
    pages = info.get("pages", [])
    if not 1 <= args.part <= len(pages):
        raise ValueError("Requested part is outside the video's page list")
    tracks = (await obj.get_subtitle(cid=pages[args.part - 1]["cid"]) or {}).get("subtitles", [])
    selected = next((track for track in tracks if track.get("lan") == args.language), None)
    if selected is None:
        return {"auth_mode": "provided_session", "video": row, "status": "track_not_returned",
                "available_languages": [track.get("lan") for track in tracks], "segments": [],
                "scope": "Subtitle track list only; absent track does not prove the video has no subtitles."}
    url = urllib.parse.urljoin("https://www.bilibili.com/", selected["subtitle_url"])
    if urllib.parse.urlparse(url).scheme != "https":
        raise ValueError("Subtitle endpoint did not return an HTTPS URL")

    def fetch_subtitle():
        # No session credential is forwarded to the subtitle CDN.
        with urllib.request.urlopen(url, timeout=15) as response:
            return json.load(response)

    body = await asyncio.to_thread(fetch_subtitle)
    return {"auth_mode": "provided_session", "video": row, "part": args.part,
            "language": selected.get("lan"), "language_name": selected.get("lan_doc"),
            "source": "platform_ai_subtitle" if selected.get("lan", "").startswith("ai-") else "platform_subtitle",
            "segments": body.get("body", []), "scope": "Selected subtitle track only; no video frames or audio read."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["search", "uploader", "info", "subtitle"])
    parser.add_argument("--query")
    parser.add_argument("--bvid")
    parser.add_argument("--uid", type=int)
    parser.add_argument("--page", type=int, default=1)
    parser.add_argument("--limit", type=int, choices=range(1, 31), default=20)
    parser.add_argument("--since", help="Beijing ISO date; local filtering of this page only")
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--language", default="zh-CN", help="Exact returned language code; AI tracks must be selected explicitly")
    args = parser.parse_args()
    if args.page < 1 or args.part < 1:
        parser.error("page and part must be positive")
    if args.mode == "search" and not args.query:
        parser.error("search requires --query")
    if args.mode == "uploader" and (args.uid or 0) < 1:
        parser.error("uploader requires a positive --uid")
    if args.mode in ("info", "subtitle") and not re.fullmatch(r"BV[0-9A-Za-z]{10}", args.bvid or ""):
        parser.error("info/subtitle require a valid --bvid")
    if args.since:
        try:
            datetime.strptime(args.since, "%Y-%m-%d")
        except ValueError:
            parser.error("since must be YYYY-MM-DD")
    result = {"tool": "bilibili-api-python", "checked_at": datetime.now(BEIJING).isoformat(), "operation": args.mode}
    try:
        result["version"] = version("bilibili-api-python")
        result.update(asyncio.run(asyncio.wait_for(read(args), timeout=45)))
        result["ok"] = True
    except Exception as exc:
        # Exception payloads may contain request URLs/headers; never dump credentials.
        result.update(ok=False, error_type=type(exc).__name__,
                      scope="Operation failed; do not count as source coverage or a no-match result.")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
