#!/usr/bin/env python3
"""
0x100x Style Kinetic Typography
Production #001 — Building Websites | 32s | 24fps | 1080×1920
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import subprocess, math, sys, os, wave
from pathlib import Path

# ─── Output paths ────────────────────────────────────────────────────────────
_DIR  = Path(__file__).parent
FONT_PATH = str(_DIR.parents[1] / "03-assets/fonts/BebasNeue.ttf")
if not os.path.exists(FONT_PATH):
    FONT_PATH = "/tmp/BebasNeue.ttf"

# ─── Frame settings ──────────────────────────────────────────────────────────
W, H    = 1080, 1920
FPS     = 24
DUR     = 32
FRAMES  = FPS * DUR
BAR_H   = 100
CX      = W // 2

# ─── Colors ─────────────────────────────────────────────────────────────────
BG   = (6,   6,   8)
WHT  = (255, 255, 255)
GOLD = (255, 184,   0)
CGLD = (212, 175,  55)
BLUE = (  0, 194, 255)
GREY = (170, 170, 170)
PURP = (139,   0, 255)
CYAN = (  0, 255, 229)
ORNG = (255, 107,   0)

# Signature gradient stops: purple → blue → cyan → orange
GRAD = [(0.0, PURP), (0.35, BLUE), (0.65, CYAN), (1.0, ORNG)]

# ─── Beat grid (120 BPM) ─────────────────────────────────────────────────────
BEAT = 0.5
def b(n): return (n - 1) * BEAT

# ─── Font cache ──────────────────────────────────────────────────────────────
_FC = {}
def fnt(sz):
    if sz not in _FC:
        _FC[sz] = ImageFont.truetype(FONT_PATH, max(8, sz))
    return _FC[sz]

def tsz(text, sz):
    bb = fnt(sz).getbbox(text)
    return bb[2] - bb[0], bb[3] - bb[1]

# ─── Easing ──────────────────────────────────────────────────────────────────
def eo(t, p=3.0):
    t = max(0.0, min(1.0, float(t)))
    return 1.0 - (1.0 - t) ** p

def eio(t):
    t = max(0.0, min(1.0, float(t)))
    return t * t * (3 - 2 * t)

# ─── Grain ───────────────────────────────────────────────────────────────────
_rng = np.random.default_rng(42)
_GRAIN = [_rng.normal(0, 9, (H, W)).astype(np.float32) for _ in range(12)]

def add_grain(arr, fi, s=0.80):
    g = _GRAIN[fi % 12][:, :, None]
    return np.clip(arr.astype(np.float32) + g * s, 0, 255).astype(np.uint8)

# ─── Gradient row ────────────────────────────────────────────────────────────
def hgrad_row(stops, offset=0.0):
    """Returns (W, 3) uint8 gradient row."""
    t = (np.linspace(0, 1, W) + offset) % 1.0
    r = g = b = np.zeros(W, np.float32)
    r, g, b = np.zeros(W, np.float32), np.zeros(W, np.float32), np.zeros(W, np.float32)
    for i in range(len(stops) - 1):
        t0, c0 = stops[i]
        t1, c1 = stops[i + 1]
        m  = (t >= t0) & (t <= t1)
        lt = np.where(m, ((t - t0) / max(t1 - t0, 1e-9)).clip(0, 1), 0.0)
        lt = lt * lt * (3 - 2 * lt)  # smoothstep
        r  += np.where(m, c0[0] + (c1[0] - c0[0]) * lt, 0.0)
        g  += np.where(m, c0[1] + (c1[1] - c0[1]) * lt, 0.0)
        b  += np.where(m, c0[2] + (c1[2] - c0[2]) * lt, 0.0)
    return np.stack([r, g, b], axis=1).clip(0, 255).astype(np.uint8)

def grad_img(stops, offset=0.0):
    """Returns full-frame (H, W, 3) gradient image."""
    row = hgrad_row(stops, offset)
    return np.broadcast_to(row[None, :, :], (H, W, 3)).copy()

# ─── Vignette and background ─────────────────────────────────────────────────
_vy, _vx = np.mgrid[:H, :W]
_RDIST   = np.sqrt(((_vx - W / 2) / W * 2.0) ** 2 + ((_vy - H / 2) / H * 2.0) ** 2).astype(np.float32)

def make_bg(glow=0.0, glow_col=PURP):
    arr = np.full((H, W, 3), BG, dtype=np.float32)
    vig = np.clip(1.0 - _RDIST * 0.28, 0.45, 1.0)
    arr *= vig[:, :, None]
    if glow > 0:
        gd = np.clip(1.0 - _RDIST * 2.8, 0, 1)
        for ch, cv in enumerate(glow_col):
            arr[:, :, ch] += gd * cv * glow * 0.55
    return np.clip(arr, 0, 255).astype(np.uint8)

# ─── Color grade ─────────────────────────────────────────────────────────────
def color_grade(arr):
    f = arr.astype(np.float32)
    f = np.clip(f - 6, 0, 255)                          # crush blacks
    shad = np.clip(1.0 - f[:, :, 0] / 80.0, 0, 1)      # teal in shadows
    f[:, :, 2] += shad * 14
    f[:, :, 1] += shad * 6
    f = np.clip(f * 1.06 - 2, 0, 255)                   # contrast
    return f.astype(np.uint8)

def add_bars(arr):
    arr[:BAR_H]      = 0
    arr[H - BAR_H:]  = 0
    return arr

# ─── Camera shake ────────────────────────────────────────────────────────────
def shake(arr, fi, intensity=7):
    r2 = np.random.default_rng(fi * 17 + 3)
    dx = int(r2.uniform(-intensity, intensity))
    dy = int(r2.uniform(-intensity * 0.6, intensity * 0.6))
    return np.roll(np.roll(arr, dy, axis=0), dx, axis=1)

# ─── Gradient text layer ─────────────────────────────────────────────────────
def grad_text_layer(text, sz, cx, cy, stops, offset=0.0, scale=1.0):
    """RGBA PIL image: gradient fill through text shape."""
    asiz = max(8, int(sz * scale))
    f    = fnt(asiz)
    mask = Image.new('L', (W, H), 0)
    ImageDraw.Draw(mask).text((cx, cy), text, font=f, fill=255, anchor='mm')
    gi   = Image.fromarray(grad_img(stops, offset)).convert('RGBA')
    gi.putalpha(mask)
    return gi

# ─── Scale punch animation ───────────────────────────────────────────────────
def scale_punch(arr, text, sz, color, cx, cy, prog,
                glow_col=None, grad=False, grad_stops=None, grad_off=0.0):
    if prog <= 0:
        return arr
    p = eo(min(1.0, prog), p=2.2)

    # Scale curve: 130% → 95% overshoot → 100%
    if p < 0.58:
        scale = 1.30 - 0.38 * (p / 0.58)
    elif p < 0.80:
        ov    = (p - 0.58) / 0.22
        scale = 0.92 + 0.11 * math.sin(ov * math.pi)
    else:
        scale = 1.0

    ss   = max(8, int(sz * scale))
    f    = fnt(ss)
    base = Image.fromarray(arr).convert('RGBA')

    # Glow (soft blurred text behind)
    if glow_col:
        gl = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(gl).text((cx, cy), text, font=f,
                                fill=(*glow_col, 210), anchor='mm')
        gl = gl.filter(ImageFilter.GaussianBlur(26))
        base.alpha_composite(gl)

    # Text layer: gradient or plain
    if grad and grad_stops:
        txt = grad_text_layer(text, sz, cx, cy, grad_stops, grad_off, scale)
    else:
        txt = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(txt).text((cx, cy), text, font=f,
                                  fill=(*color, 255), anchor='mm')

    base.alpha_composite(txt)
    return np.array(base.convert('RGB'))

# ─── Clip reveal animation ───────────────────────────────────────────────────
def clip_reveal(arr, text, sz, color, cx, cy, prog,
                glow_col=None, grad=False, grad_stops=None, grad_off=0.0):
    p    = eo(min(1.0, prog * 1.15), p=2.5)
    f    = fnt(sz)
    _tw, th = tsz(text, sz)
    shift = int((1.0 - p) * (th + 22))
    ty    = cy + shift

    # Clip bounds at natural position
    ct = max(0,     cy - th // 2 - 5)
    cb = min(H - 1, cy + th // 2 + 5)

    base = Image.fromarray(arr).convert('RGBA')

    # Glow at natural position (not shifted)
    if glow_col:
        gl = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(gl).text((cx, cy), text, font=f,
                                 fill=(*glow_col, 170), anchor='mm')
        gl = gl.filter(ImageFilter.GaussianBlur(18))
        gla = np.array(gl); gla[:ct] = 0; gla[cb:] = 0
        base.alpha_composite(Image.fromarray(gla))

    # Text layer at shifted position
    if grad and grad_stops:
        mask = Image.new('L', (W, H), 0)
        ImageDraw.Draw(mask).text((cx, ty), text, font=f, fill=255, anchor='mm')
        gi   = Image.fromarray(grad_img(grad_stops, grad_off)).convert('RGBA')
        gi.putalpha(mask)
        txt  = gi
    else:
        txt = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(txt).text((cx, ty), text, font=f,
                                  fill=(*color, 255), anchor='mm')

    # Apply clip: zero alpha outside [ct, cb]
    ta = np.array(txt); ta[:ct] = 0; ta[cb:] = 0
    base.alpha_composite(Image.fromarray(ta))
    return np.array(base.convert('RGB'))

# ─── Fade in ─────────────────────────────────────────────────────────────────
def fade_in(arr, text, sz, color, cx, cy, prog):
    p = eio(min(1.0, prog))
    if p <= 0:
        return arr
    tmp = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(tmp).text((cx, cy), text, font=fnt(sz),
                              fill=(*color, int(255 * p)), anchor='mm')
    base = Image.fromarray(arr).convert('RGBA')
    base.alpha_composite(tmp)
    return np.array(base.convert('RGB'))

# ─── Shape graphics ──────────────────────────────────────────────────────────
def draw_divider(arr, cx, cy, prog, col=WHT, opacity=0.55):
    p  = eo(min(1.0, prog * 2.0))
    hw = int(W * 0.38 * p)
    if hw < 1:
        return arr
    img = Image.fromarray(arr).convert('RGBA')
    ImageDraw.Draw(img).line([(cx - hw, cy), (cx + hw, cy)],
                              fill=(*col, int(255 * opacity)), width=1)
    return np.array(img.convert('RGB'))

def draw_corners(arr, prog, col=WHT, opacity=0.72):
    p   = eo(min(1.0, prog * 2.0))
    arm = int(80 * p)
    if arm < 2:
        return arr
    mg  = 105
    top = BAR_H + mg
    bot = H - BAR_H - mg
    lft = mg
    rgt = W - mg
    img = Image.fromarray(arr).convert('RGBA')
    d   = ImageDraw.Draw(img)
    c   = (*col, int(255 * opacity))
    lw  = 2
    for (x, y, sx, sy) in [(lft, top, 1, 1), (rgt, top, -1, 1),
                             (lft, bot, 1, -1), (rgt, bot, -1, -1)]:
        d.line([(x, y), (x + sx * arm, y)], fill=c, width=lw)
        d.line([(x, y), (x, y + sy * arm)], fill=c, width=lw)
    return np.array(img.convert('RGB'))

def draw_sweeps(arr, prog, y0, col=WHT, opacity=0.30):
    """3 thin horizontal lines sweep left→right with stagger."""
    img = Image.fromarray(arr).convert('RGBA')
    d   = ImageDraw.Draw(img)
    for i in range(3):
        delay = i * 0.10
        p = eo(max(0.0, min(1.0, (prog - delay) / 0.55)))
        if p <= 0:
            continue
        y    = y0 + (i - 1) * 72
        lw_p = int(W * p)
        c    = (*col, int(255 * opacity * (1.0 - p * 0.35)))
        d.line([(0, y), (lw_p, y)], fill=c, width=1)
    return np.array(img.convert('RGB'))

# ─── Main frame renderer ──────────────────────────────────────────────────────
def render_frame(fi):
    t  = fi / FPS

    if   t < 2.0:  sn, s0 = 1, 0.0
    elif t < 4.0:  sn, s0 = 2, 2.0
    elif t < 7.0:  sn, s0 = 3, 4.0
    elif t < 10.0: sn, s0 = 4, 7.0
    elif t < 14.0: sn, s0 = 5, 10.0
    elif t < 22.0: sn, s0 = 6, 14.0
    elif t < 28.0: sn, s0 = 7, 22.0
    else:          sn, s0 = 8, 28.0
    ts = t - s0

    # ── Background ──
    if   sn == 6: arr = make_bg(glow=min(1.0, ts / 1.8) * 0.70, glow_col=PURP)
    elif sn == 7: arr = make_bg(glow=0.22, glow_col=CGLD)
    else:         arr = make_bg(glow=0.0)

    # ─────────────────────────────────────────────────────────────────────────
    # SCENE 1 — HOOK (0–2 s)
    # ─────────────────────────────────────────────────────────────────────────
    if sn == 1:
        arr = scale_punch(arr, "MOST PEOPLE", 165, WHT, CX, int(H * 0.44),
                          ts / (5 / FPS))
        arr = draw_divider(arr, CX, int(H * 0.505), ts / (6 / FPS))
        if ts > 0.33:
            arr = clip_reveal(arr, "SCROLL PAST THIS.", 96, GOLD, CX,
                              int(H * 0.575), (ts - 0.33) / (8 / FPS))

    # ─────────────────────────────────────────────────────────────────────────
    # SCENE 2 — BUILD 1 (2–4 s)
    # ─────────────────────────────────────────────────────────────────────────
    elif sn == 2:
        arr = scale_punch(arr, "WHILE THEY SCROLL", 132, WHT, CX,
                          int(H * 0.44), ts / (5 / FPS))
        if ts > BEAT:
            arr = clip_reveal(arr, "YOU BUILD.", 158, BLUE, CX,
                              int(H * 0.60), (ts - BEAT) / (8 / FPS))

    # ─────────────────────────────────────────────────────────────────────────
    # SCENE 3 — BUILD 2 (4–7 s)
    # ─────────────────────────────────────────────────────────────────────────
    elif sn == 3:
        arr = clip_reveal(arr, "EVERY WEBSITE", 132, WHT, CX,
                          int(H * 0.42), ts / (8 / FPS))
        if ts > BEAT:
            arr = clip_reveal(arr, "IS A MONEY MACHINE.", 84, GOLD, CX,
                              int(H * 0.56), (ts - BEAT) / (10 / FPS))
        if ts > BEAT * 2:
            arr = draw_corners(arr, (ts - BEAT * 2) / (8 / FPS))

    # ─────────────────────────────────────────────────────────────────────────
    # SCENE 4 — BUILD 3: word swap (7–10 s)
    # ─────────────────────────────────────────────────────────────────────────
    elif sn == 4:
        cy4 = int(H * 0.50)
        if ts < BEAT:
            arr = scale_punch(arr, "NO DEGREE.", 125, WHT, CX, cy4,
                              ts / (5 / FPS))
        elif ts < BEAT * 2:
            arr = scale_punch(arr, "NO BOSS.", 125, WHT, CX, cy4,
                              (ts - BEAT) / (5 / FPS))
        else:
            arr = scale_punch(arr, "NO OFFICE.", 125, CGLD, CX, cy4,
                              (ts - BEAT * 2) / (5 / FPS))

    # ─────────────────────────────────────────────────────────────────────────
    # SCENE 5 — PRE-PEAK (10–14 s)
    # ─────────────────────────────────────────────────────────────────────────
    elif sn == 5:
        arr = clip_reveal(arr, "JUST A LAPTOP", 148, WHT, CX,
                          int(H * 0.44), ts / (8 / FPS))
        if ts > BEAT:
            arr = clip_reveal(arr, "AND THE RIGHT SKILLS.", 82, WHT, CX,
                              int(H * 0.585), (ts - BEAT) / (8 / FPS))
        # Ramp: darken+desaturate into the drop
        if ts > 2.5:
            ramp = min(1.0, (ts - 2.5) / 1.5)
            arr  = np.clip(arr.astype(np.float32) * (1.0 - ramp * 0.40),
                           0, 255).astype(np.uint8)

    # ─────────────────────────────────────────────────────────────────────────
    # SCENE 6 — PEAK / DROP (14–22 s)   ← THE KEY SCENE
    # ─────────────────────────────────────────────────────────────────────────
    elif sn == 6:
        # Camera snap — first 10 frames
        if ts < 10 / FPS:
            arr = shake(arr, fi, intensity=max(1, int(8 * (1 - ts * FPS / 10))))

        # Sweep lines
        arr = draw_sweeps(arr, min(1.0, ts / 0.50), int(H * 0.30))

        # "$3,000 A MONTH" — scale punch + electric-blue glow
        arr = scale_punch(arr, "$3,000 A MONTH", 188, WHT, CX,
                          int(H * 0.375), ts / (5 / FPS), glow_col=BLUE)

        # "STARTS WITH" — clip reveal 8 frames in
        if ts > 8 / FPS:
            arr = clip_reveal(arr, "STARTS WITH", 74, GREY, CX,
                              int(H * 0.535), (ts - 8 / FPS) / (8 / FPS))

        # "ONE CLIENT." — GRADIENT TEXT scale punch on the next beat
        if ts > BEAT:
            go  = (ts * 0.28) % 1.0
            arr = scale_punch(arr, "ONE CLIENT.", 164, GOLD, CX,
                              int(H * 0.685), (ts - BEAT) / (6 / FPS),
                              glow_col=GOLD, grad=True,
                              grad_stops=GRAD, grad_off=go)

    # ─────────────────────────────────────────────────────────────────────────
    # SCENE 7 — RESOLUTION (22–28 s)
    # ─────────────────────────────────────────────────────────────────────────
    elif sn == 7:
        arr = clip_reveal(arr, "BUILD WEBSITES.", 140, WHT, CX,
                          int(H * 0.44), ts / (8 / FPS))
        if ts > BEAT * 1.5:
            arr = clip_reveal(arr, "BUILD WEALTH.", 140, CGLD, CX,
                              int(H * 0.575), (ts - BEAT * 1.5) / (8 / FPS))

    # ─────────────────────────────────────────────────────────────────────────
    # SCENE 8 — CTA (28–32 s)
    # ─────────────────────────────────────────────────────────────────────────
    else:
        arr = np.full((H, W, 3), (4, 4, 6), dtype=np.uint8)
        if ts > 2 / FPS:
            dt = ts - 2 / FPS
            arr = clip_reveal(arr, "FOLLOW FOR MORE.", 78, GOLD, CX,
                              int(H * 0.50), dt / (10 / FPS))
            arr = fade_in(arr, "@animex680", 54, WHT, CX,
                          int(H * 0.88), dt / (14 / FPS))

    # ── Post-processing ──
    arr = color_grade(arr)
    arr = add_grain(arr, fi)
    arr = add_bars(arr)
    return arr


# ─── Audio synthesis ─────────────────────────────────────────────────────────
def gen_audio(dur=DUR, sr=44100):
    n   = int((dur + 0.2) * sr)
    out = np.zeros(n, np.float32)
    _ar = np.random.default_rng(7)

    def place(sig, t):
        i0 = int(t * sr)
        le = min(len(sig), n - i0)
        if le > 0:
            out[i0:i0 + le] += sig[:le]

    def kick(t, v=0.80):
        L  = int(0.22 * sr)
        tt = np.linspace(0, 0.22, L)
        f0 = 65 * np.exp(-tt * 22)
        place(np.sin(2 * np.pi * f0 * tt) * np.exp(-tt / 0.08) * v, t)

    def sub_boom(t, v=0.70, freq=38, d=0.55):
        L  = int(d * sr)
        tt = np.linspace(0, d, L)
        place(np.sin(2 * np.pi * freq * tt) * np.exp(-tt / 0.35) * v, t)

    def snare(t, v=0.32):
        L  = int(0.09 * sr)
        tt = np.linspace(0, 0.09, L)
        place(_ar.standard_normal(L) * np.exp(-tt / 0.03) * v, t)

    def hat(t, v=0.13, opn=False):
        d  = 0.06 if opn else 0.022
        L  = int(d * sr)
        tt = np.linspace(0, d, L)
        n_ = _ar.standard_normal(L)
        hp = np.diff(n_, prepend=n_[0]) * 0.5 + n_ * 0.5
        place(hp * np.exp(-tt / (0.024 if opn else 0.008)) * v, t)

    def impact(t, v=0.55):
        L  = int(0.14 * sr)
        tt = np.linspace(0, 0.14, L)
        place((_ar.standard_normal(L) * 0.4 + np.sin(2 * np.pi * 55 * tt))
              * np.exp(-tt / 0.04) * v, t)

    def riser(t0, t1, v=0.30):
        L    = int((t1 - t0) * sr)
        tt   = np.arange(L) / sr
        env  = (tt / (t1 - t0)) ** 1.8 * v
        place(_ar.standard_normal(L) * env * 0.55, t0)

    def pad(freq, t0, tdur, v=0.06):
        L  = int(tdur * sr)
        tt = np.linspace(0, tdur, L)
        env = np.minimum(tt / 0.15, 1.0) * np.minimum((tdur - tt) / 0.4, 1.0)
        sig = (np.sin(2 * np.pi * freq * tt) +
               np.sin(2 * np.pi * freq * 2 * tt) * 0.22 +
               np.sin(2 * np.pi * freq * 3 * tt) * 0.10) * env * v
        place(sig, t0)

    # Dark atmospheric pad (throughout)
    for f_, v_ in [(55, 0.055), (82, 0.038), (110, 0.024), (165, 0.014)]:
        pad(f_, 0, 32, v_)

    # HOOK — opening slam
    impact(0.0, 0.90)
    sub_boom(0.0, 1.10, freq=34, d=0.70)

    # BUILD section beats (2–14 s, 24 beats)
    for i in range(24):
        t   = 2.0 + i * BEAT
        bib = i % 4
        kick(t, 0.65)
        if bib in (1, 3):
            snare(t, 0.28)
        hat(t, 0.12)
        hat(t + BEAT * 0.5, 0.09)
        if bib == 0:
            sub_boom(t, 0.30, d=0.24)

    # Impact on each text entrance
    for ti, vi in [(2.0, 0.65), (2.5, 0.48), (4.0, 0.60), (4.5, 0.42),
                   (7.0, 0.65), (7.5, 0.55), (8.0, 0.44),
                   (10.0, 0.58), (10.5, 0.40)]:
        impact(ti, vi)

    # RISER into the drop
    riser(11.0, 14.0, 0.48)
    for ti, vi in [(13.15, 0.28), (13.55, 0.50), (13.82, 0.75)]:
        impact(ti, vi)

    # THE DROP (14 s) — loudest moment
    kick(14.0, 1.00)
    sub_boom(14.0, 1.45, freq=33, d=1.0)
    snare(14.0, 0.65)
    impact(14.0, 1.00)

    # PEAK beats (14–22 s, 16 beats)
    for i in range(16):
        t   = 14.0 + i * BEAT
        bib = i % 4
        kick(t, 0.78)
        if bib in (1, 3):
            snare(t, 0.36)
        hat(t, 0.15)
        hat(t + BEAT * 0.5, 0.10)
        hat(t + BEAT * 0.25, 0.07, opn=True)
        if bib == 0:
            sub_boom(t, 0.36, d=0.22)

    impact(14.0 + 8 / FPS, 0.52)   # STARTS WITH
    impact(14.5, 0.85)               # ONE CLIENT.
    sub_boom(14.5, 0.72, freq=40, d=0.38)

    # RESOLUTION (22–28 s)
    for i in range(12):
        t   = 22.0 + i * BEAT
        bib = i % 4
        kick(t, 0.50)
        if bib in (1, 3):
            snare(t, 0.22)
        hat(t, 0.09)
        hat(t + BEAT * 0.5, 0.07)

    impact(22.0, 0.60)
    impact(22.75, 0.48)

    # CTA — vinyl crackle texture
    crackle = _ar.standard_normal(int(4 * sr)) * 0.018
    s28 = int(28 * sr)
    out[s28:s28 + len(crackle)] += crackle[:n - s28]

    # Master limit
    mx = np.max(np.abs(out))
    if mx > 0:
        out = out / mx * 0.88
    return (out * 32767).astype(np.int16)


# ─── Entry point ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    OUT = str(_DIR / "001_BuildingWebsites_REELS.mp4")
    VID = "/tmp/_vid_raw.mp4"
    AUD = "/tmp/_beat.wav"

    print(f"Font     : {FONT_PATH}  exists={os.path.exists(FONT_PATH)}")
    print(f"Output   : {OUT}")
    print(f"Frames   : {FRAMES}  ({DUR}s @ {FPS}fps  {W}×{H})")

    # ── Video pass ──────────────────────────────────────────────────────────
    print("\n[1/3] Rendering frames…")
    proc = subprocess.Popen([
        "ffmpeg", "-y",
        "-f", "rawvideo", "-vcodec", "rawvideo",
        "-s", f"{W}x{H}", "-pix_fmt", "rgb24", "-r", str(FPS),
        "-i", "pipe:0",
        "-vcodec", "libx264", "-pix_fmt", "yuv420p",
        "-crf", "17", "-preset", "fast",
        VID
    ], stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)

    for fi in range(FRAMES):
        if fi % (FPS * 5) == 0:
            print(f"  {fi // FPS:>3}s / {DUR}s …")
        proc.stdin.write(render_frame(fi).tobytes())

    proc.stdin.close()
    proc.wait()
    print("  Frames done.")

    # ── Audio pass ──────────────────────────────────────────────────────────
    print("\n[2/3] Generating audio…")
    pcm = gen_audio(DUR + 0.2)
    with wave.open(AUD, "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(44100)
        wf.writeframes(pcm.tobytes())
    print("  Audio done.")

    # ── Mux ─────────────────────────────────────────────────────────────────
    print("\n[3/3] Muxing…")
    subprocess.run([
        "ffmpeg", "-y",
        "-i", VID, "-i", AUD,
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-shortest", "-movflags", "+faststart",
        OUT
    ], check=True, stderr=subprocess.DEVNULL)

    size_mb = os.path.getsize(OUT) / 1024 / 1024
    print(f"\n✓  Done!  {OUT}  ({size_mb:.1f} MB)\n")
