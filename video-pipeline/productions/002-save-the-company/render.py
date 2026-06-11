#!/usr/bin/env python3
"""
0x100x Style Kinetic Typography
Production #002 — Save The Company | 32s | 24fps | 1080x1920

Drop: f336 (14.0s) — scene 6 ($250,000 A YEAR signature)
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import subprocess, math, os, wave
from pathlib import Path

# Paths
_DIR  = Path(__file__).parent
FONT_PATH = str(_DIR.parents[1] / "03-assets/fonts/BebasNeue.ttf")

W, H    = 1080, 1920
FPS     = 24
DUR     = 32
FRAMES  = FPS * DUR
BAR_H   = 100
CX      = W // 2

BG   = (6,   6,   8)
WHT  = (255, 255, 255)
GOLD = (255, 184,   0)
CGLD = (212, 175,  55)
BLUE = (  0, 194, 255)
GREY = (170, 170, 170)
GR2  = (204, 204, 204)
PURP = (139,   0, 255)
CYAN = (  0, 255, 229)
ORNG = (255, 107,   0)

GRAD = [(0.0, PURP), (0.35, BLUE), (0.65, CYAN), (1.0, ORNG)]

BEAT = 0.5

_FC = {}
def fnt(sz):
    if sz not in _FC:
        _FC[sz] = ImageFont.truetype(FONT_PATH, max(8, sz))
    return _FC[sz]

def tsz(text, sz):
    bb = fnt(sz).getbbox(text)
    return bb[2] - bb[0], bb[3] - bb[1]

def eo(t, p=3.0):
    t = max(0.0, min(1.0, float(t)))
    return 1.0 - (1.0 - t) ** p

def eio(t):
    t = max(0.0, min(1.0, float(t)))
    return t * t * (3 - 2 * t)

_rng = np.random.default_rng(42)
_GRAIN = [_rng.normal(0, 9, (H, W)).astype(np.float32) for _ in range(12)]

def add_grain(arr, fi, s=0.80):
    g = _GRAIN[fi % 12][:, :, None]
    return np.clip(arr.astype(np.float32) + g * s, 0, 255).astype(np.uint8)

def hgrad_row(stops, offset=0.0):
    t = (np.linspace(0, 1, W) + offset) % 1.0
    r, g, b = np.zeros(W, np.float32), np.zeros(W, np.float32), np.zeros(W, np.float32)
    for i in range(len(stops) - 1):
        t0, c0 = stops[i]
        t1, c1 = stops[i + 1]
        m  = (t >= t0) & (t <= t1)
        lt = np.where(m, ((t - t0) / max(t1 - t0, 1e-9)).clip(0, 1), 0.0)
        lt = lt * lt * (3 - 2 * lt)
        r  += np.where(m, c0[0] + (c1[0] - c0[0]) * lt, 0.0)
        g  += np.where(m, c0[1] + (c1[1] - c0[1]) * lt, 0.0)
        b  += np.where(m, c0[2] + (c1[2] - c0[2]) * lt, 0.0)
    return np.stack([r, g, b], axis=1).clip(0, 255).astype(np.uint8)

def grad_img(stops, offset=0.0):
    row = hgrad_row(stops, offset)
    return np.broadcast_to(row[None, :, :], (H, W, 3)).copy()

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

def color_grade(arr):
    f = arr.astype(np.float32)
    f = np.clip(f - 6, 0, 255)
    shad = np.clip(1.0 - f[:, :, 0] / 80.0, 0, 1)
    f[:, :, 2] += shad * 14
    f[:, :, 1] += shad * 6
    f = np.clip(f * 1.06 - 2, 0, 255)
    return f.astype(np.uint8)

def add_bars(arr):
    arr[:BAR_H]      = 0
    arr[H - BAR_H:]  = 0
    return arr

def shake(arr, fi, intensity=7):
    r2 = np.random.default_rng(fi * 17 + 3)
    dx = int(r2.uniform(-intensity, intensity))
    dy = int(r2.uniform(-intensity * 0.6, intensity * 0.6))
    return np.roll(np.roll(arr, dy, axis=0), dx, axis=1)

def grad_text_layer(text, sz, cx, cy, stops, offset=0.0, scale=1.0):
    asiz = max(8, int(sz * scale))
    f    = fnt(asiz)
    mask = Image.new('L', (W, H), 0)
    ImageDraw.Draw(mask).text((cx, cy), text, font=f, fill=255, anchor='mm')
    gi   = Image.fromarray(grad_img(stops, offset)).convert('RGBA')
    gi.putalpha(mask)
    return gi

def scale_punch(arr, text, sz, color, cx, cy, prog,
                glow_col=None, grad=False, grad_stops=None, grad_off=0.0,
                peak=1.18):
    if prog <= 0:
        return arr
    p = eo(min(1.0, prog), p=2.2)
    if p < 0.58:
        scale = peak - (peak - 0.92) * (p / 0.58)
    elif p < 0.80:
        ov    = (p - 0.58) / 0.22
        scale = 0.92 + 0.11 * math.sin(ov * math.pi)
    else:
        scale = 1.0
    ss   = max(8, int(sz * scale))
    f    = fnt(ss)
    base = Image.fromarray(arr).convert('RGBA')
    if glow_col:
        gl = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(gl).text((cx, cy), text, font=f,
                                fill=(*glow_col, 180), anchor='mm')
        gl = gl.filter(ImageFilter.GaussianBlur(14))
        base.alpha_composite(gl)
    if grad and grad_stops:
        txt = grad_text_layer(text, sz, cx, cy, grad_stops, grad_off, scale)
    else:
        txt = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(txt).text((cx, cy), text, font=f,
                                  fill=(*color, 255), anchor='mm')
    base.alpha_composite(txt)
    return np.array(base.convert('RGB'))

def clip_reveal(arr, text, sz, color, cx, cy, prog,
                glow_col=None, grad=False, grad_stops=None, grad_off=0.0):
    p    = eo(min(1.0, prog * 1.15), p=2.5)
    f    = fnt(sz)
    _tw, th = tsz(text, sz)
    shift = int((1.0 - p) * (th + 22))
    ty    = cy + shift
    ct = max(0,     cy - th // 2 - 5)
    cb = min(H - 1, cy + th // 2 + 5)
    base = Image.fromarray(arr).convert('RGBA')
    if glow_col:
        gl = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(gl).text((cx, cy), text, font=f,
                                 fill=(*glow_col, 170), anchor='mm')
        gl = gl.filter(ImageFilter.GaussianBlur(18))
        gla = np.array(gl); gla[:ct] = 0; gla[cb:] = 0
        base.alpha_composite(Image.fromarray(gla))
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
    ta = np.array(txt); ta[:ct] = 0; ta[cb:] = 0
    base.alpha_composite(Image.fromarray(ta))
    return np.array(base.convert('RGB'))

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
    # Sit inside IG safe area (14% top, 18% bot, 4% sides)
    top = int(H * 0.14) + 12
    bot = int(H * 0.82) - 12
    lft = int(W * 0.04) + 12
    rgt = int(W * 0.96) - 12
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
    img = Image.fromarray(arr).convert('RGBA')
    d   = ImageDraw.Draw(img)
    sl  = int(W * 0.04) + 12
    sr  = int(W * 0.96) - 12
    span = sr - sl
    for i in range(3):
        delay = i * 0.10
        p = eo(max(0.0, min(1.0, (prog - delay) / 0.55)))
        if p <= 0:
            continue
        y    = y0 + (i - 1) * 72
        x_end = sl + int(span * p)
        c    = (*col, int(255 * opacity * (1.0 - p * 0.35)))
        d.line([(sl, y), (x_end, y)], fill=c, width=1)
    return np.array(img.convert('RGB'))

# Captions are timed in frames per captions.json
# Scene table (start_frame, scene_no):
SCENES = [
    (0,   1),   # HOOK         f0-48
    (48,  2),   # BUILD 1      f48-96
    (96,  3),   # BUILD 2      f96-168 (word swap)
    (168, 4),   # BUILD 3      f168-240 (word swap)
    (240, 5),   # PRE-PEAK     f240-336
    (336, 6),   # PEAK         f336-528 (drop)
    (528, 7),   # RESOLUTION   f528-672
    (672, 8),   # CTA          f672-768
]

def scene_at(fi):
    cur = SCENES[0]
    for s in SCENES:
        if fi >= s[0]:
            cur = s
    return cur

def render_frame(fi):
    sf, sn = scene_at(fi)
    sfp = fi - sf

    # Background
    if sn == 6:
        # Drop scene: purple radial glow ramping up
        g = min(1.0, sfp / 32.0) * 0.70
        arr = make_bg(glow=g, glow_col=PURP)
    elif sn == 7:
        arr = make_bg(glow=0.22, glow_col=CGLD)
    elif sn == 8:
        arr = np.full((H, W, 3), (4, 4, 6), dtype=np.uint8)
    else:
        arr = make_bg(glow=0.0)

    # ─── SCENE 1: HOOK f0-48 ───────────────────────────
    if sn == 1:
        arr = scale_punch(arr, "EVERY DEAD COMPANY", 134, WHT, CX,
                          int(H * 0.42), sfp / 5)
        arr = draw_divider(arr, CX, int(H * 0.49), sfp / 8)
        if sfp >= 24:
            arr = clip_reveal(arr, "HAD A DEAD WEBSITE.", 108, GOLD, CX,
                              int(H * 0.555), (sfp - 24) / 8)

    # ─── SCENE 2: BUILD 1 f48-96 ───────────────────────
    elif sn == 2:
        arr = scale_punch(arr, "BUSINESSES NEED YOU.", 124, WHT, CX,
                          int(H * 0.44), sfp / 5)
        if sfp >= 12:
            arr = clip_reveal(arr, "THEY DON'T KNOW IT YET.", 78, GR2, CX,
                              int(H * 0.56), (sfp - 12) / 8)

    # ─── SCENE 3: BUILD 2 word swap f96-168 ────────────
    elif sn == 3:
        cy3 = int(H * 0.50)
        if sfp < 12:
            arr = scale_punch(arr, "BAD WEBSITE.", 138, GOLD, CX, cy3,
                              sfp / 5)
        elif sfp < 24:
            arr = scale_punch(arr, "NO LEADS.", 138, WHT, CX, cy3,
                              (sfp - 12) / 4)
        else:
            arr = scale_punch(arr, "NO COMPANY.", 138, GOLD, CX, cy3,
                              (sfp - 24) / 4)
            if sfp >= 32:
                arr = draw_corners(arr, (sfp - 32) / 8)

    # ─── SCENE 4: BUILD 3 word swap f168-240 ───────────
    elif sn == 4:
        cy4 = int(H * 0.50)
        if sfp < 12:
            arr = scale_punch(arr, "NO WEBSITE.", 130, WHT, CX, cy4,
                              sfp / 5)
        elif sfp < 24:
            arr = scale_punch(arr, "NO LEADS.", 130, WHT, CX, cy4,
                              (sfp - 12) / 4)
        else:
            arr = scale_punch(arr, "NO REVENUE.", 130, CGLD, CX, cy4,
                              (sfp - 24) / 4)

    # ─── SCENE 5: PRE-PEAK f240-336 ────────────────────
    elif sn == 5:
        arr = clip_reveal(arr, "ONE WEBSITE", 148, WHT, CX,
                          int(H * 0.43), sfp / 8)
        if sfp >= 12:
            arr = clip_reveal(arr, "FIXES IT ALL.", 92, WHT, CX,
                              int(H * 0.555), (sfp - 12) / 8)
        # Ramp into the drop: darken last second
        if sfp >= 72:
            ramp = min(1.0, (sfp - 72) / 24.0)
            arr  = np.clip(arr.astype(np.float32) * (1.0 - ramp * 0.40),
                           0, 255).astype(np.uint8)

    # ─── SCENE 6: PEAK / DROP f336-528 ─────────────────
    elif sn == 6:
        # Camera shake first 8 frames
        if sfp < 8:
            arr = shake(arr, fi, intensity=max(1, int(8 * (1 - sfp / 8))))

        # Sweep lines
        arr = draw_sweeps(arr, min(1.0, sfp / 12.0), int(H * 0.28))

        # "$5,000 PER BUILD." — punch + blue glow
        arr = scale_punch(arr, "$5,000 PER BUILD.", 130, WHT, CX,
                          int(H * 0.37), sfp / 5, glow_col=BLUE)

        # "ONE CLIENT A WEEK." — clip reveal
        if sfp >= 12:
            arr = clip_reveal(arr, "ONE CLIENT A WEEK.", 76, GR2, CX,
                              int(H * 0.52), (sfp - 12) / 8)

        # "$250,000 A YEAR." — SIGNATURE moment: gradient + gold glow
        if sfp >= 24:
            go  = ((sfp / FPS) * 0.28) % 1.0
            arr = scale_punch(arr, "$250,000 A YEAR.", 130, GOLD, CX,
                              int(H * 0.66), (sfp - 24) / 6,
                              glow_col=GOLD, grad=True,
                              grad_stops=GRAD, grad_off=go)

    # ─── SCENE 7: RESOLUTION f528-672 ──────────────────
    elif sn == 7:
        arr = clip_reveal(arr, "BUILD WEBSITES.", 132, WHT, CX,
                          int(H * 0.44), sfp / 10)
        if sfp >= 24:
            arr = clip_reveal(arr, "SAVE COMPANIES.", 132, CGLD, CX,
                              int(H * 0.555), (sfp - 24) / 10)

    # ─── SCENE 8: CTA f672-768 ─────────────────────────
    else:
        if sfp >= 2:
            arr = clip_reveal(arr, "FOLLOW. START NOW.", 76, GOLD, CX,
                              int(H * 0.48), (sfp - 2) / 10)
        if sfp >= 6:
            arr = fade_in(arr, "@animex680", 56, WHT, CX,
                          int(H * 0.78), (sfp - 6) / 14)

    arr = color_grade(arr)
    arr = add_grain(arr, fi)
    arr = add_bars(arr)
    return arr


# ─── Audio ───────────────────────────────────────────────────────────────────
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

    # Atmospheric pad
    for f_, v_ in [(55, 0.055), (82, 0.038), (110, 0.024), (165, 0.014)]:
        pad(f_, 0, 32, v_)

    # HOOK slam (0.0s)
    impact(0.0, 0.90)
    sub_boom(0.0, 1.10, freq=34, d=0.70)

    # BUILD beats 2.0s–14.0s (24 beats)
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

    # Impact on text entrances (per captions.json)
    for ti, vi in [(1.0,  0.55),   # HAD A DEAD WEBSITE
                   (2.0,  0.62),   # BUSINESSES
                   (2.5,  0.45),   # THEY DON'T KNOW
                   (4.0,  0.65),   # BAD WEBSITE
                   (4.5,  0.55),   # NO LEADS
                   (5.0,  0.62),   # NO COMPANY
                   (7.0,  0.65),   # NO WEBSITE
                   (7.5,  0.50),   # NO LEADS
                   (8.0,  0.62),   # NO REVENUE
                   (10.0, 0.58),   # ONE WEBSITE
                   (10.5, 0.42)]:  # FIXES IT ALL
        impact(ti, vi)

    # RISER into the drop (11.0s → 14.0s)
    riser(11.0, 14.0, 0.48)
    for ti, vi in [(13.15, 0.28), (13.55, 0.50), (13.82, 0.75)]:
        impact(ti, vi)

    # THE DROP (14.0s) — peak
    kick(14.0, 1.00)
    sub_boom(14.0, 1.45, freq=33, d=1.0)
    snare(14.0, 0.65)
    impact(14.0, 1.00)

    # PEAK beats 14.0s–22.0s (16 beats)
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

    impact(14.5, 0.55)             # ONE CLIENT A WEEK
    impact(15.0, 0.85)             # $250,000 A YEAR — signature impact
    sub_boom(15.0, 0.78, freq=40, d=0.42)

    # RESOLUTION 22.0s–28.0s (12 beats)
    for i in range(12):
        t   = 22.0 + i * BEAT
        bib = i % 4
        kick(t, 0.50)
        if bib in (1, 3):
            snare(t, 0.22)
        hat(t, 0.09)
        hat(t + BEAT * 0.5, 0.07)

    impact(22.0, 0.60)
    impact(23.0, 0.48)

    # CTA — vinyl crackle
    crackle = _ar.standard_normal(int(4 * sr)) * 0.018
    s28 = int(28 * sr)
    out[s28:s28 + len(crackle)] += crackle[:n - s28]

    mx = np.max(np.abs(out))
    if mx > 0:
        out = out / mx * 0.88
    return (out * 32767).astype(np.int16)


if __name__ == "__main__":
    OUT = str(_DIR / "002_SaveTheCompany_REELS.mp4")
    VID = "/tmp/_vid002_raw.mp4"
    AUD = "/tmp/_beat002.wav"

    print(f"Font     : {FONT_PATH}  exists={os.path.exists(FONT_PATH)}")
    print(f"Output   : {OUT}")
    print(f"Frames   : {FRAMES}  ({DUR}s @ {FPS}fps  {W}x{H})")

    print("\n[1/3] Rendering frames...")
    proc = subprocess.Popen([
        "ffmpeg", "-y",
        "-f", "rawvideo", "-vcodec", "rawvideo",
        "-s", f"{W}x{H}", "-pix_fmt", "rgb24", "-r", str(FPS),
        "-i", "pipe:0",
        "-vcodec", "libx264", "-pix_fmt", "yuv420p",
        "-crf", "20", "-preset", "fast",
        VID
    ], stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)

    for fi in range(FRAMES):
        if fi % (FPS * 4) == 0:
            print(f"  {fi // FPS:>3}s / {DUR}s ...")
        proc.stdin.write(render_frame(fi).tobytes())

    proc.stdin.close()
    proc.wait()
    print("  Frames done.")

    print("\n[2/3] Generating audio...")
    pcm = gen_audio(DUR + 0.2)
    with wave.open(AUD, "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(44100)
        wf.writeframes(pcm.tobytes())
    print("  Audio done.")

    print("\n[3/3] Muxing...")
    subprocess.run([
        "ffmpeg", "-y",
        "-i", VID, "-i", AUD,
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-shortest", "-movflags", "+faststart",
        OUT
    ], check=True, stderr=subprocess.DEVNULL)

    size_mb = os.path.getsize(OUT) / 1024 / 1024
    print(f"\nDone! {OUT}  ({size_mb:.1f} MB)\n")
