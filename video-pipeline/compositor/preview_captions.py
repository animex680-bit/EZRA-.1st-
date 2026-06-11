#!/usr/bin/env python3
"""
Renders caption-position previews per scene.
Each preview is a static PNG showing every caption that's visible
at the peak frame of that scene, with the IG-safe rectangle drawn.

This is what the user signs off on before rendering the reel.

Also validates every caption's bbox against safe-area programmatically.
Exits non-zero if any violation is found.

Usage:
    python3 preview_captions.py <production_dir>
"""

import argparse
import json
import os
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter


SAFE_TOP_FRAC    = 0.14
SAFE_BOTTOM_FRAC = 0.18
SAFE_SIDE_FRAC   = 0.04


def hex2rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def font_for(font_paths, name, size):
    return ImageFont.truetype(font_paths[name], int(size))


def text_bbox(font, text, x, y, anchor='mm'):
    """Returns (l, t, r, b) at given position with anchor."""
    img = Image.new('L', (10, 10))
    d   = ImageDraw.Draw(img)
    bb  = d.textbbox((x, y), text, font=font, anchor=anchor)
    return bb


def draw_safe_area(d, W, H):
    sl = int(W * SAFE_SIDE_FRAC)
    sr = int(W * (1 - SAFE_SIDE_FRAC))
    st = int(H * SAFE_TOP_FRAC)
    sb = int(H * (1 - SAFE_BOTTOM_FRAC))
    d.rectangle([sl, st, sr, sb], outline=(0, 255, 229, 200), width=3)
    d.text((sl + 8, st + 8), 'IG SAFE AREA',
            fill=(0, 255, 229, 220),
            font=ImageFont.load_default())


def render_text_layer(W, H, cap, font_paths):
    """Render a single caption as RGBA layer. Returns (image, bbox)."""
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    f   = font_for(font_paths, cap['font'], cap['size'])
    cx  = int(W * cap['x_frac'])
    cy  = int(H * cap['y_frac'])
    color = (*hex2rgb(cap['color']), 255)

    # Glow
    if cap.get('glow'):
        gl = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(gl).text((cx, cy), cap['text'], font=f,
                                 fill=(*hex2rgb(cap['glow']['color']),
                                        cap['glow']['alpha']),
                                 anchor=cap.get('anchor', 'mm'))
        gl = gl.filter(ImageFilter.GaussianBlur(cap['glow']['blur']))
        img.alpha_composite(gl)

    # Gradient matte
    if cap.get('matte', {}).get('kind') == 'gradient':
        stops = cap['matte']['stops']
        bb = text_bbox(f, cap['text'], cx, cy, anchor=cap.get('anchor', 'mm'))
        # Build horizontal gradient strip
        strip = Image.new('RGB', (W, 1), (0, 0, 0))
        for x in range(W):
            t = x / W
            for i in range(len(stops) - 1):
                t0, c0 = stops[i]
                t1, c1 = stops[i + 1]
                if t0 <= t <= t1:
                    lt = (t - t0) / max(t1 - t0, 1e-9)
                    lt = lt * lt * (3 - 2 * lt)
                    c0r, c0g, c0b = hex2rgb(c0)
                    c1r, c1g, c1b = hex2rgb(c1)
                    strip.putpixel((x, 0), (
                        int(c0r + (c1r - c0r) * lt),
                        int(c0g + (c1g - c0g) * lt),
                        int(c0b + (c1b - c0b) * lt)))
                    break
        gimg = strip.resize((W, H), Image.NEAREST).convert('RGBA')
        mask = Image.new('L', (W, H), 0)
        ImageDraw.Draw(mask).text((cx, cy), cap['text'], font=f, fill=255,
                                    anchor=cap.get('anchor', 'mm'))
        gimg.putalpha(mask)
        img.alpha_composite(gimg)
    else:
        ImageDraw.Draw(img).text((cx, cy), cap['text'], font=f, fill=color,
                                   anchor=cap.get('anchor', 'mm'))

    bbox = text_bbox(f, cap['text'], cx, cy, anchor=cap.get('anchor', 'mm'))
    return img, bbox


def check_safe_area(W, H, bbox):
    """Returns list of violation strings (empty = OK)."""
    l, t, r, b = bbox
    viol = []
    sl = int(W * SAFE_SIDE_FRAC)
    sr = int(W * (1 - SAFE_SIDE_FRAC))
    st = int(H * SAFE_TOP_FRAC)
    sb = int(H * (1 - SAFE_BOTTOM_FRAC))
    if t < st: viol.append(f'top_over_by={st - t}px')
    if b > sb: viol.append(f'bot_over_by={b - sb}px')
    if l < sl: viol.append(f'left_over_by={sl - l}px')
    if r > sr: viol.append(f'right_over_by={r - sr}px')
    return viol


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('production', help='production folder')
    args = ap.parse_args()
    prod = Path(args.production)

    captions = json.loads((prod / 'captions.json').read_text())
    storyboard_scenes = 8  # 1..8

    W = captions['comp']['w']
    H = captions['comp']['h']
    BAR = 100

    # Resolve font paths relative to repo root
    repo = Path(__file__).resolve().parents[2]
    font_paths = {name: str(repo / rel) for name, rel in
                   captions['font_paths'].items()}
    for name, p in font_paths.items():
        if not os.path.exists(p):
            print(f'ERROR: font "{name}" missing at {p}')
            sys.exit(2)

    out = prod / 'preview_captions'
    out.mkdir(exist_ok=True)

    violations_all = []
    scene_caps = {}
    for cap in captions['captions']:
        scene_caps.setdefault(cap['scene'], []).append(cap)

    # For each scene, render preview frame at midpoint of all its captions
    for scene in sorted(scene_caps):
        caps = scene_caps[scene]
        # Frame to render at: the latest in_frame so all captions are visible
        peak_frame = max(c['in_frame'] for c in caps)

        # Base: dark grey textured "stand-in for footage" so safe area shows clearly
        img = Image.new('RGBA', (W, H), (16, 16, 22, 255))
        # Subtle diagonal texture so it's obvious this is a stand-in
        td = ImageDraw.Draw(img)
        for i in range(0, W + H, 40):
            td.line([(i, 0), (i - H, H)], fill=(28, 28, 36, 255), width=1)

        # Composite each caption visible at peak_frame
        scene_viol = []
        for cap in caps:
            if cap['in_frame'] > peak_frame or cap['out_frame'] <= peak_frame:
                continue
            layer, bbox = render_text_layer(W, H, cap, font_paths)
            img.alpha_composite(layer)
            viol = check_safe_area(W, H, bbox)
            entry = {'caption_id': cap['id'], 'text': cap['text'],
                       'bbox': bbox, 'violations': viol}
            scene_viol.append(entry)
            if viol:
                violations_all.append({'scene': scene, **entry})

        # Letterbox bars
        d = ImageDraw.Draw(img, 'RGBA')
        d.rectangle([0, 0, W, BAR],        fill=(0, 0, 0, 255))
        d.rectangle([0, H - BAR, W, H],    fill=(0, 0, 0, 255))

        # Safe-area overlay
        draw_safe_area(d, W, H)

        # Scene label
        title = f'SCENE {scene}  ·  preview frame f{peak_frame}'
        d.rectangle([0, BAR, 540, BAR + 50], fill=(0, 0, 0, 220))
        d.text((20, BAR + 12), title, fill=(0, 255, 229, 255))

        # Per-caption status
        y_pad = BAR + 56
        for e in scene_viol:
            tag = 'OK' if not e['violations'] else 'FAIL'
            col = (0, 255, 80, 230) if tag == 'OK' else (255, 60, 60, 230)
            d.rectangle([0, y_pad, 720, y_pad + 28], fill=(0, 0, 0, 200))
            d.text((20, y_pad + 6),
                    f"{tag} · {e['caption_id']} · {e['text'][:30]}",
                    fill=col)
            y_pad += 30

        p = out / f'scene_{scene}.jpg'
        img.convert('RGB').save(p, 'JPEG', quality=88)
        print(f'  wrote {p}')

    # Summary
    summary = {
        'comp': captions['comp'],
        'total_captions': len(captions['captions']),
        'scenes': sorted(scene_caps),
        'violations': violations_all,
        'verdict': 'PASS' if not violations_all else 'FAIL'
    }
    (out / 'preview_check.json').write_text(json.dumps(summary, indent=2))

    print()
    print('─' * 60)
    print(f'  Captions     : {len(captions["captions"])}')
    print(f'  Scenes       : {len(scene_caps)}')
    print(f'  Violations   : {len(violations_all)}')
    print(f'  Verdict      : {summary["verdict"]}')
    print('─' * 60)
    print(f'  Previews     : {out}')

    sys.exit(0 if summary['verdict'] == 'PASS' else 1)


if __name__ == '__main__':
    main()
