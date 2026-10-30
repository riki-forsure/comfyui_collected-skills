#!/usr/bin/env python3
"""Read-only public Tieba access. Dependency: aiotieba==4.8.2."""
import argparse
import asyncio
import html
import json
import re
from datetime import datetime, timezone, timedelta
from importlib.metadata import version
import aiotieba as tb

TZ = timezone(timedelta(hours=8))

def clean(value):
    return html.unescape(re.sub(r"<[^>]+>", " ", str(value or ""))).strip()

def date(value):
    return datetime.fromtimestamp(value, TZ).isoformat() if value else None

def item(obj):
    user = getattr(obj, "user", None)
    author = (getattr(user, "show_name", "") or getattr(user, "nick_name", "")) if user else getattr(obj, "author_show_name", "")
    content = getattr(obj, "text", "") or getattr(obj, "content", "") or getattr(getattr(obj, "contents", None), "text", "")
    tid = getattr(obj, "tid", 0)
    ts = getattr(obj, "create_time", 0)
    return {
        "tid": tid, "url": f"https://tieba.baidu.com/p/{tid}" if tid else None,
        "title": clean(getattr(obj, "title", "")),
        "forum": getattr(obj, "fname", "") or getattr(obj, "forum_name", ""),
        "author": author, "created_at": date(ts), "created_timestamp": ts,
        "floor": getattr(obj, "floor", None), "text": clean(content),
    }

async def run(args):
    timeout = tb.TimeoutConfig(http_connect=5, http_read=15)
    # Retain the execution environment's configured proxy and trust settings.
    async with tb.Client(proxy=True, timeout=timeout) as client:
        if args.mode == "list":
            result = await client.get_threads(args.forum, pn=args.page, rn=args.limit, sort=tb.ThreadSortType.CREATE)
        elif args.mode == "search":
            # PC global search supports newest-first; optional forum filter is local.
            result = await client.search_global(args.query, pn=args.page, rn=args.limit, sort=tb.SearchGlobalType.DESC)
        else:
            result = await client.get_posts(args.tid, pn=args.page, rn=args.limit, with_comments=False)
        if result.err:
            raise RuntimeError(str(result.err))
        rows = [item(obj) for obj in result.objs]
        if args.mode == "search" and args.forum:
            rows = [row for row in rows if row["forum"].casefold() == args.forum.casefold()]
        if args.since:
            start = int(datetime.fromisoformat(args.since).replace(tzinfo=TZ).timestamp())
            rows = [row for row in rows if (row["created_timestamp"] or 0) >= start]
        if args.until:
            end = int((datetime.fromisoformat(args.until).replace(tzinfo=TZ) + timedelta(days=1)).timestamp())
            rows = [row for row in rows if (row["created_timestamp"] or 0) < end]
        payload = {
            "tool": "aiotieba", "version": version("aiotieba"), "guest_only": True,
            "operation": args.mode, "checked_at": datetime.now(TZ).isoformat(),
            "page": args.page, "items": rows, "count": len(rows),
            "has_more": getattr(result, "has_more", getattr(getattr(result, "page", None), "has_more", None)),
            "scope_note": "One page only. Local date/forum filtering does not establish full historical coverage. Text only; images and nested replies are not inspected.",
        }
        if args.mode == "read":
            payload["thread"] = item(result.thread)
        return payload

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["list", "search", "read"])
    parser.add_argument("--forum")
    parser.add_argument("--query")
    parser.add_argument("--tid", type=int)
    parser.add_argument("--page", type=int, default=1)
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--since", help="Beijing date, YYYY-MM-DD; filter current page")
    parser.add_argument("--until", help="Inclusive Beijing date, YYYY-MM-DD; filter current page")
    args = parser.parse_args()
    if args.page < 1 or not 1 <= args.limit <= 30:
        parser.error("page >= 1; limit 1..30")
    if args.mode == "list" and not args.forum:
        parser.error("list requires --forum")
    if args.mode == "search" and not args.query:
        parser.error("search requires --query")
    if args.mode == "read" and not args.tid:
        parser.error("read requires --tid")
    if args.mode == "read" and (args.since or args.until):
        parser.error("date filters apply to thread lists/search; read.thread retains original thread metadata")
    try:
        result = asyncio.run(asyncio.wait_for(run(args), timeout=35))
    except Exception as exc:
        print(json.dumps({"status": "error", "error_type": type(exc).__name__, "message": str(exc)}, ensure_ascii=False))
        raise SystemExit(1)
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
