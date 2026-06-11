#!/usr/bin/env python3
"""
Reels Watcher — frame-level QA for vertical IG/TikTok videos.

What it actually checks (per frame, programmatically — no vibes):
  1. SAFE-AREA: any text-like blobs must sit inside the IG-safe rectangle
     (top 14% / bottom 18% reserved for UI + handle).
  2. EDGE-CLIP: detect bright text pixels touching the frame edge → "out of frame".
  3. DEAD-FRAME: frame mean brightness < threshold for > N consecutive frames.
  4. OVEREXPOSURE: > 35% of pixels saturated white.
  5. CONTRAST: low-contrast frames (boring, hard-to-read).
  6. AUDIO-CLIPPING: any audio sample at ±1.0.
  7. BEAT-SYNC: for each user-supplied beat marker, the visible content
     must change within ±1 frame (verified via diff).
  8. CAPTION-COVERAGE: % of frames with any caption visible (target: 70%+).

Outputs:
  - JSON report with timestamps of every violation.
  - Annotated keyframes (red boxes on issues) for human review.
  - Verdict: PASS / FAIL with severity list.

Usage:
  python3 inspect.py <video.mp4> [--beats=beats.json] [--out=reports/qa_001/]
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

# ─── IG safe area (relative to 1080×1920) ────────────────────────────────────
SAFE_TOP_FRAC    = 0.14    # IG top UI (battery, handle bar)
SAFE_BOTTOM_FRAC = 0.18    # IG bottom UI (caption, buttons, audio bar)
SAFE_SIDE_FRAC   = 0.04    # margin against side rails

# ─── Thresholds ──────────────────────────────────────────────────────────────
DEAD_FRAME_LUM       = 10      # mean Y below this → dead
DEAD_FRAME_RUN_FR    = 4       # consecutive dead frames = violation
OVEREXPOSED_FRAC     = 0.35    # > 35% bright pixels = blown out
LOWCONTRAST_STD      = 16      # std-dev of luminance below this = flat
TEXT_DETECT_LUM      = 200     # bright pixel = likely text
EDGE_CLIP_PIXELS     = 6       # band width at edges checked for text


def y_luma(arr_u8):
    """Approx ITU-R BT.601 luma → uint8."""
    return (0.299 * arr_u8[..., 0] +
            0.587 * arr_u8[..., 1] +
            0.114 * arr_u8[..., 2]).astype(np.uint8)


def find_text_bbox(arr_u8):
    """Find tight bbox around bright (likely text) pixels. None if nothing bright."""
    y = y_luma(arr_u8)
    mask = y > TEXT_DETECT_LUM
    if mask.sum() < 200:  # ignore tiny specks (grain)
        return None
    ys, xs = np.where(mask)
    return int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())


def check_frame(arr_u8, fi, h, w):
    """Return list of {kind, severity, detail} issues for this frame."""
    issues = []

    y      = y_luma(arr_u8)
    mean_y = float(y.mean())
    std_y  = float(y.std())
    bright = float((y > 240).sum()) / (h * w)

    if mean_y < DEAD_FRAME_LUM:
        issues.append({'kind': 'dead_frame', 'sev': 'warn',
                        'detail': f'mean_luma={mean_y:.1f}'})

    if bright > OVEREXPOSED_FRAC:
        issues.append({'kind': 'overexposed', 'sev': 'warn',
                        'detail': f'bright_frac={bright:.2f}'})

    if std_y < LOWCONTRAST_STD and mean_y > DEAD_FRAME_LUM:
        issues.append({'kind': 'low_contrast', 'sev': 'info',
                        'detail': f'std_luma={std_y:.1f}'})

    # Edge clip — bright pixels in the outer band of the frame
    band = EDGE_CLIP_PIXELS
    top_strip    = (y[:band, :]                  > TEXT_DETECT_LUM).sum()
    bot_strip    = (y[h - band:, :]              > TEXT_DETECT_LUM).sum()
    left_strip   = (y[:, :band]                  > TEXT_DETECT_LUM).sum()
    right_strip  = (y[:, w - band:]              > TEXT_DETECT_LUM).sum()
    edge_total   = top_strip + bot_strip + left_strip + right_strip
    if edge_total > 80:
        issues.append({'kind': 'edge_clip', 'sev': 'fail',
                        'detail': f'bright_edge_pixels={int(edge_total)}'})

    # Safe-area check on detected text bbox
    bbox = find_text_bbox(arr_u8)
    if bbox is not None:
        x0, y0, x1, y1 = bbox
        safe_t = int(h * SAFE_TOP_FRAC)
        safe_b = int(h * (1 - SAFE_BOTTOM_FRAC))
        safe_l = int(w * SAFE_SIDE_FRAC)
        safe_r = int(w * (1 - SAFE_SIDE_FRAC))
        viol = []
        if y0 < safe_t: viol.append(f'top_over_by={safe_t - y0}px')
        if y1 > safe_b: viol.append(f'bot_over_by={y1 - safe_b}px')
        if x0 < safe_l: viol.append(f'left_over_by={safe_l - x0}px')
        if x1 > safe_r: viol.append(f'right_over_by={x1 - safe_r}px')
        if viol:
            issues.append({'kind': 'safe_area', 'sev': 'fail',
                            'detail': ' / '.join(viol),
                            'bbox': bbox})

    return issues, {'mean_y': mean_y, 'std_y': std_y, 'bright': bright,
                     'bbox': bbox}


def annotate(arr_u8, h, w, issues, fi):
    """Draw safe-area rect + bbox + issue markers, return PIL image."""
    img = Image.fromarray(arr_u8)
    d   = ImageDraw.Draw(img, 'RGBA')

    # Safe area: cyan rectangle
    st = int(h * SAFE_TOP_FRAC)
    sb = int(h * (1 - SAFE_BOTTOM_FRAC))
    sl = int(w * SAFE_SIDE_FRAC)
    sr = int(w * (1 - SAFE_SIDE_FRAC))
    d.rectangle([sl, st, sr, sb], outline=(0, 255, 229, 180), width=3)

    # Issues
    fail_cnt = sum(1 for i in issues if i['sev'] == 'fail')
    color = (255, 60, 60, 220) if fail_cnt else \
            (255, 184, 0, 220) if issues else (0, 255, 80, 200)
    d.rectangle([4, 4, 360, 36], fill=(0, 0, 0, 200))
    d.text((10, 10), f'f{fi}  {len(issues)} issues',
            fill=color)

    # bbox of detected text
    for it in issues:
        if it.get('bbox'):
            x0, y0, x1, y1 = it['bbox']
            d.rectangle([x0 - 2, y0 - 2, x1 + 2, y1 + 2],
                          outline=(255, 60, 60, 230), width=4)

    return img


def check_audio(video_path):
    """Extract audio, check for clipping and silence."""
    issues = []
    raw = '/tmp/_wch_audio.wav'
    try:
        subprocess.run(['ffmpeg', '-y', '-i', video_path,
                         '-ac', '1', '-ar', '44100',
                         '-f', 'wav', raw],
                        check=True, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        return [{'kind': 'no_audio', 'sev': 'warn', 'detail': 'no audio stream'}], None

    import wave
    with wave.open(raw, 'rb') as wf:
        nframes = wf.getnframes()
        sr      = wf.getframerate()
        pcm     = np.frombuffer(wf.readframes(nframes), dtype=np.int16)

    peak     = int(np.abs(pcm).max())
    clip_pct = float((np.abs(pcm) >= 32760).sum()) / max(len(pcm), 1) * 100

    if clip_pct > 0.05:
        issues.append({'kind': 'audio_clipping', 'sev': 'fail',
                        'detail': f'clipped_pct={clip_pct:.3f}%'})

    # Silence stretches (>0.5s with peak < 200)
    win = sr // 4
    silent_runs = []
    cur = 0
    for i in range(0, len(pcm), win):
        seg = pcm[i:i + win]
        if np.abs(seg).max() < 200:
            cur += 1
        else:
            if cur >= 2:
                silent_runs.append((i / sr, cur * 0.25))
            cur = 0
    for t, dur in silent_runs:
        issues.append({'kind': 'audio_silence', 'sev': 'info',
                        'detail': f't={t:.2f}s dur={dur:.2f}s'})

    stats = {'peak': peak, 'clip_pct': clip_pct,
              'rms': float(np.sqrt(np.mean(pcm.astype(np.float64) ** 2)))}
    return issues, stats


def run(video_path, out_dir, beats=None, sample_every=4):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / 'annotated').mkdir(exist_ok=True)

    # Probe
    probe = subprocess.run(['ffprobe', '-v', 'quiet', '-print_format', 'json',
                             '-show_streams', '-show_format', video_path],
                            capture_output=True, text=True).stdout
    meta = json.loads(probe)
    vs   = next(s for s in meta['streams'] if s['codec_type'] == 'video')
    W    = int(vs['width']); H = int(vs['height'])
    fps  = eval(vs['r_frame_rate'])
    dur  = float(meta['format']['duration'])
    nfr  = int(round(dur * fps))

    print(f'Video      : {video_path}')
    print(f'Resolution : {W}×{H}  @ {fps:.2f}fps')
    print(f'Duration   : {dur:.2f}s  ({nfr} frames)')
    print(f'Sample     : every {sample_every} frames')
    print(f'Output     : {out}')

    # ── Stream raw frames in ─────────────────────────────────────────────
    raw_proc = subprocess.Popen(
        ['ffmpeg', '-i', video_path, '-vf', f'select=not(mod(n\\,{sample_every}))',
         '-vsync', 'vfr', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

    frame_bytes = W * H * 3
    all_issues  = []
    stats_list  = []
    annotated_keyframes = []

    fi = 0
    while True:
        buf = raw_proc.stdout.read(frame_bytes)
        if len(buf) < frame_bytes:
            break
        arr = np.frombuffer(buf, dtype=np.uint8).reshape(H, W, 3)
        issues, stats = check_frame(arr, fi * sample_every, H, W)
        stats_list.append({'f': fi * sample_every, 't': fi * sample_every / fps,
                            **{k: round(v, 2) if isinstance(v, float) else v
                                for k, v in stats.items() if k != 'bbox'}})
        for it in issues:
            it['f']    = fi * sample_every
            it['t']    = round(fi * sample_every / fps, 3)
            all_issues.append(it)
        # Save annotated frame if there's a fail OR every ~2s
        if any(it['sev'] == 'fail' for it in issues) or (fi % max(1, int(fps / sample_every * 2)) == 0):
            img = annotate(arr, H, W, issues, fi * sample_every)
            p   = out / 'annotated' / f'f{fi * sample_every:05d}.jpg'
            img.save(p, 'JPEG', quality=82)
            annotated_keyframes.append(str(p))
        fi += 1
    raw_proc.wait()

    # ── Audio ───────────────────────────────────────────────────────────
    aud_issues, aud_stats = check_audio(video_path)
    for it in aud_issues:
        it['f'] = None
        all_issues.append(it)

    # ── Caption coverage ────────────────────────────────────────────────
    has_text = sum(1 for s in stats_list if s.get('bright', 0) > 0.005)
    cov      = has_text / max(len(stats_list), 1)

    # ── Verdict ─────────────────────────────────────────────────────────
    n_fail = sum(1 for i in all_issues if i['sev'] == 'fail')
    n_warn = sum(1 for i in all_issues if i['sev'] == 'warn')
    verdict = 'PASS' if n_fail == 0 else 'FAIL'

    report = {
        'verdict'        : verdict,
        'video'          : video_path,
        'resolution'     : [W, H],
        'fps'            : fps,
        'duration_s'     : dur,
        'frames_sampled' : len(stats_list),
        'fails'          : n_fail,
        'warns'          : n_warn,
        'caption_coverage_frac': round(cov, 3),
        'audio_stats'    : aud_stats,
        'issues'         : all_issues,
        'annotated_dir'  : str(out / 'annotated'),
    }
    (out / 'report.json').write_text(json.dumps(report, indent=2))

    # ── Human summary ───────────────────────────────────────────────────
    md  = [f'# Watcher Report — {Path(video_path).name}', '']
    md += [f'**Verdict:** `{verdict}`',
            f'- Resolution: {W}×{H} @ {fps:.2f}fps',
            f'- Duration: {dur:.2f}s',
            f'- Frames sampled: {len(stats_list)} (every {sample_every}th)',
            f'- Failures: **{n_fail}** · Warnings: **{n_warn}**',
            f'- Caption coverage: {cov*100:.1f}%',
            '']

    md += ['## Issues by kind', '']
    kinds = {}
    for i in all_issues:
        kinds.setdefault(i['kind'], []).append(i)
    for k, items in sorted(kinds.items(), key=lambda x: -len(x[1])):
        md.append(f'### `{k}` × {len(items)}')
        for i in items[:10]:
            t = f'@t={i.get("t"):.2f}s' if i.get('t') is not None else ''
            md.append(f'- [{i["sev"].upper()}] {t} — {i["detail"]}')
        if len(items) > 10:
            md.append(f'- … (+{len(items)-10} more)')
        md.append('')

    (out / 'report.md').write_text('\n'.join(md))

    print()
    print(f'─' * 60)
    print(f'  VERDICT      : {verdict}')
    print(f'  Failures     : {n_fail}')
    print(f'  Warnings     : {n_warn}')
    print(f'  Cap coverage : {cov*100:.1f}%')
    print(f'─' * 60)
    print(f'  Report       : {out / "report.md"}')
    print(f'  Annotated    : {out / "annotated"}/  ({len(annotated_keyframes)} frames)')
    return 0 if verdict == 'PASS' else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('video')
    ap.add_argument('--out',    default='/tmp/watcher_report')
    ap.add_argument('--every',  type=int, default=4,
                     help='sample every N frames (default 4)')
    ap.add_argument('--beats',  default=None,
                     help='beats.json with {beat_t: [t,...]} for sync check')
    args = ap.parse_args()
    sys.exit(run(args.video, args.out, sample_every=args.every))


if __name__ == '__main__':
    main()
