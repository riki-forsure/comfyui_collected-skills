#!/usr/bin/env python3
"""Read selected public Bilibili media and frames; no account writes or services.

Requires requirements-bilibili.txt and FFmpeg. Output/cache must stay outside
the repository. Platform response URLs are used transiently and never logged.
"""
import argparse
import asyncio
from datetime import datetime
from importlib.metadata import version
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request

from bilibili_readonly import BEIJING, video_row


def download(stream, path, referer, max_bytes):
    urls = [stream.get("baseUrl") or stream.get("base_url")]
    urls += (stream.get("backupUrl") or stream.get("backup_url") or [])[:1]
    attempts = []
    for position, url in enumerate(urls):
        if not url or urllib.parse.urlsplit(url).scheme != "https":
            attempts.append({"source": position, "error": "non_https_or_missing"})
            continue
        part = path.with_suffix(path.suffix + ".part")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Referer": referer})
            size, started = 0, time.monotonic()
            with urllib.request.urlopen(req, timeout=20) as response, part.open("wb") as out:
                if int(response.headers.get("Content-Length", 0)) > max_bytes:
                    raise ValueError("stream exceeds size limit")
                while chunk := response.read(256 * 1024):
                    size += len(chunk)
                    if size > max_bytes or time.monotonic() - started > 90:
                        raise ValueError("stream exceeds size/time limit")
                    out.write(chunk)
            part.replace(path)
            attempts.append({"source": position, "status": response.status, "bytes": size})
            return {"ok": True, "file": path.name, "attempts": attempts}
        except urllib.error.HTTPError as exc:
            attempts.append({"source": position, "status": exc.code})
        except Exception as exc:
            attempts.append({"source": position, "error": type(exc).__name__})
        finally:
            part.unlink(missing_ok=True)
    return {"ok": False, "attempts": attempts}


def frames(media, out, interval, ocr, tessdata):
    folder = out / "frames"
    folder.mkdir(exist_ok=True)
    for old in folder.iterdir():
        if re.fullmatch(r"(?:frame\d+|tail)\.(?:png|txt)", old.name):
            old.unlink()
    subprocess.run(["ffmpeg", "-nostdin", "-y", "-hide_banner", "-loglevel", "error",
                    "-i", str(media), "-vf", f"fps=1/{interval}", str(folder / "frame%04d.png")],
                   check=True, capture_output=True, timeout=180)
    subprocess.run(["ffmpeg", "-nostdin", "-y", "-hide_banner", "-loglevel", "error",
                    "-sseof", "-1", "-i", str(media), "-frames:v", "1", str(folder / "tail.png")],
                   check=True, capture_output=True, timeout=30)
    rows = []
    images = sorted(folder.glob("frame*.png"))
    if (folder / "tail.png").exists():
        images.append(folder / "tail.png")
    for number, frame in enumerate(images, 1):
        row = {"file": str(frame.relative_to(out)),
               "sampled_at_seconds_approx": None if frame.stem == "tail" else (number - 0.5) * interval,
               "sample_kind": "last_second" if frame.stem == "tail" else "interval"}
        if ocr:
            command = ["tesseract", str(frame), "stdout", "-l", "chi_sim+eng", "--psm", "6"]
            if tessdata:
                command += ["--tessdata-dir", str(tessdata)]
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
            if proc.returncode:
                row["ocr_status"] = "failed_check_language_data"
            else:
                target = frame.with_suffix(".txt")
                target.write_text(proc.stdout, encoding="utf-8")
                row.update(ocr_file=str(target.relative_to(out)), ocr_status="machine_text_unverified")
        rows.append(row)
    return rows


async def media_info(args):
    from bilibili_api import Credential, request_settings, video
    proxy = urllib.request.getproxies().get("https") or urllib.request.getproxies().get("http", "")
    request_settings.set_proxy(proxy)
    request_settings.set_trust_env(True)
    request_settings.set_verify_ssl(True)
    request_settings.set_timeout(15)
    request_settings.set_wbi_retry_times(1)
    obj = video.Video(bvid=args.bvid, credential=Credential(sessdata=os.environ.get("BILIBILI_SESSDATA") or None))
    info = await obj.get_info()
    pages = info.get("pages", [])
    if not 1 <= args.part <= len(pages):
        raise ValueError("part outside page list")
    page = pages[args.part - 1]
    if page.get("duration", 0) > args.max_duration:
        return info, page, None
    return info, page, await obj.get_download_url(page_index=args.part - 1)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--bvid", required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--part", type=int, default=1)
    p.add_argument("--short-side", "--height", dest="height", type=int, default=480,
                   help="Maximum short side, also supports portrait video")
    p.add_argument("--max-duration", type=int, default=600)
    p.add_argument("--max-mib", type=int, default=40, help="Per-stream limit")
    p.add_argument("--interval", type=float, default=6)
    p.add_argument("--audio", action="store_true", help="Also save lowest-bitrate audio for optional ASR")
    p.add_argument("--ocr", action="store_true")
    p.add_argument("--tessdata", type=Path)
    a = p.parse_args()
    if not re.fullmatch(r"BV[0-9A-Za-z]{10}", a.bvid):
        p.error("invalid BV id")
    if min(a.part, a.height, a.max_duration, a.max_mib) < 1 or a.interval < 1:
        p.error("positive limits and interval >= 1 required")
    repo = Path(__file__).resolve().parents[1]
    a.out = a.out.resolve()
    if a.out == repo or repo in a.out.parents:
        p.error("media/cache output must be outside the repository")
    if not shutil.which("ffmpeg"):
        p.error("FFmpeg is required")
    a.out.mkdir(parents=True, exist_ok=True)
    result = {"tool": "bilibili-api-python+FFmpeg", "sdk_version": version("bilibili-api-python"),
              "checked_at": datetime.now(BEIJING).isoformat(), "bvid": a.bvid, "part": a.part,
              "scope": "Selected-part media and sampled frames only; OCR needs visual verification. No platform subtitles or comments read."}
    try:
        info, page, data = asyncio.run(asyncio.wait_for(media_info(a), timeout=60))
        result.update(video=video_row(info, detail=True), selected_duration=page.get("duration"))
        if data is None:
            result.update(ok=False, status="duration_limit")
        else:
            dash = data.get("dash") or {}
            candidates = [x for x in dash.get("video", [])
                          if 0 < min(x.get("width", 0), x.get("height", 0)) <= a.height]
            if not candidates:
                raise ValueError("no DASH video within short-side limit")
            chosen = max(candidates, key=lambda x: (min(x.get("width", 0), x.get("height", 0)),
                                                    -x.get("bandwidth", 0)))
            result["resolution"] = [chosen.get("width"), chosen.get("height")]
            target = a.out / "video.m4s"
            result["video_download"] = download(chosen, target, result["video"]["url"], a.max_mib * 1024**2)
            if a.audio:
                audio = dash.get("audio") or []
                result["audio_download"] = (download(min(audio, key=lambda x: x.get("bandwidth", 0)),
                    a.out / "audio.m4s", result["video"]["url"], a.max_mib * 1024**2)
                    if audio else {"ok": False, "status": "no_audio_returned"})
            if result["video_download"]["ok"]:
                result["frames"] = frames(target, a.out, a.interval, a.ocr, a.tessdata)
            result["ok"] = result["video_download"]["ok"]
    except Exception as exc:
        result.update(ok=False, error_type=type(exc).__name__)
    (a.out / "manifest.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
