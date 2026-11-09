#!/usr/bin/env python3
"""Optional local ASR draft for previously obtained media; no Bilibili login.

FFmpeg decodes PCM before inference, avoiding the PyAV container-open path.
Use a separate environment with requirements-bilibili-asr.txt when needed.
"""
import argparse
from datetime import datetime, timezone
from importlib.metadata import version
import json
from pathlib import Path
import subprocess
import tempfile
import time


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--cache", type=Path, required=True)
    p.add_argument("--model", choices=["base", "small"], default="base")
    p.add_argument("--max-duration", type=float, default=600)
    a = p.parse_args()
    repo = Path(__file__).resolve().parents[1]
    for folder in (a.out, a.cache):
        if folder.resolve() == repo or repo in folder.resolve().parents:
            p.error("ASR output/cache must be outside the repository")
    a.out.mkdir(parents=True, exist_ok=True)
    result = {"source": "local_asr_unverified", "model": a.model, "device": "cpu",
              "compute_type": "int8", "checked_at": datetime.now(timezone.utc).isoformat(),
              "scope": "Machine transcription draft, not platform subtitles or verified literal text. Check terms and numbers against original sources."}
    started = time.monotonic()
    try:
        probe = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                "-of", "json", str(a.input)], capture_output=True, text=True,
                               check=True, timeout=30)
        duration = float(json.loads(probe.stdout)["format"]["duration"])
        if not 0 < duration <= a.max_duration:
            raise ValueError("duration outside limit")
        import numpy as np
        from faster_whisper import WhisperModel
        result["faster_whisper_version"] = version("faster-whisper")
        with tempfile.TemporaryDirectory(dir=a.out) as temp:
            pcm = Path(temp) / "audio.f32"
            subprocess.run(["ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "error", "-i", str(a.input),
                            "-ar", "16000", "-ac", "1", "-f", "f32le", str(pcm)],
                           capture_output=True, check=True, timeout=90)
            model = WhisperModel(a.model, device="cpu", compute_type="int8", cpu_threads=2,
                                 download_root=str(a.cache))
            segments, info = model.transcribe(np.fromfile(pcm, dtype=np.float32), vad_filter=True, beam_size=3)
            rows = [{"start": s.start, "end": s.end, "text": s.text,
                     "no_speech_prob": s.no_speech_prob} for s in segments]
        result.update(ok=True, language=info.language, language_probability=info.language_probability,
                      duration=info.duration, duration_after_vad=info.duration_after_vad, segments=rows)
    except Exception as exc:
        result.update(ok=False, error_type=type(exc).__name__)
    result["elapsed_seconds"] = round(time.monotonic() - started, 2)
    (a.out / "asr.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "segments"}, ensure_ascii=False, indent=2))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
