#!/usr/bin/env python3
"""
0x100x Style Kinetic Typography Video
Production #001 — Building Websites  |  32s  |  24fps  |  1080x1920
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont
import subprocess, math, sys, os, wave

# ── Constants ─────────────────────────────────────────────────────────────────
W, H   = 1080, 1920
FPS    = 24
DUR    = 32
FRAMES = FPS * DUR
BAR_H  = 110                      # letterbox bar height

# ── Colors ────────────────────────────────────────────────────────────────────
BG   = (10,  10,  10)
WHT  = (255, 255, 255)
GOLD = (255, 184,   0)
CGLD = (212, 175,  55)
BLUE = (  0, 194, 255)
GREY = (180, 180, 180)
PURP = (139,   0, 255)
CYAN = (  0, 255, 229)
ORNG = (255, 107,   0)

# ── Beat grid (120 BPM, 0.5s per beat) ───────────────────────────────────────
BEAT = 0.5
def b(n):      return (n - 1) * BEAT   # beat n → seconds
CX = W // 2

# ── Font ──────────────────────────────────────────────────────────────────────
_FONT_PATH = next(
    (p for p in [
        '/tmp/BebasNeue.ttf',
        '/usr/share/fonts/truetype/freefont/FreeSansBold.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
    ] if os.path.exists(p)),
    None
)
_FONT_CACHE = {}
def font(size):
    if size not in _FONT_CACHE:
        try:   _FONT_CACHE[size] = ImageFont.truetype(_FONT_PATH, size)
        except: _FONT_CACHE[size] = ImageFont.load_default()
    return _FONT_CACHE[size]

def tsize(text, size):
    d = ImageDraw.Draw(Image.new('RGB', (4, 4)))
    bb = d.textbbox((0, 0), text, font=font(size))
    return bb[2] - bb[0], bb[3] - bb[1]

# ── Easing ────────────────────────────────────────────────────────────────────
def ease_out(t):
    t = max(0.0, min(1.0, t))
    return 1.0 - (1.0 - t) ** 3

def ease_io(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3.0 - 2.0 * t)

# ── Pre-computed grain (8 tiles, 1080×1920×3) ────────────────────────────────
rng   = np.random.default_rng(42)
GRAIN = [rng.normal(0, 9, (H, W, 3)).astype(np.float32) for _ in range(8)]

# ── Pre-computed diagonal gradient coords ────────────────────────────────────
_Y, _X = np.mgrid[:H, :W]
_DIAG  = (_X / W * 0.5 + _Y / H * 0.5).astype(np.float32)  # 0..1

# ── Background ────────────────────────────────────────────────────────────────
def make_bg(t, gradient=False, gi=1.0):
    arr = np.zeros((H, W, 3), dtype=np.float32)
    arr[:] = BG

    # Subtle radial vignette
    cx, cy = W / 2.0, H / 2.0
    dist  = np.sqrt(((_X - cx) / cx) ** 2 + ((_Y - cy) / cy) ** 2)
    vign  = np.clip(1.0 - dist * 0.22, 0.65, 1.0)
    arr  *= vign[:, :, np.newaxis]

    if gradient:
        offset = (t * 0.38) % 1.0
        pos = (_DIAG + offset) % 1.0

        r = np.where(pos < 0.35,
                139 + (0   - 139) * (pos / 0.35),
            np.where(pos < 0.65,
                0.0,
                0   + (255 -   0) * ((pos - 0.65) / 0.35)))

        g = np.where(pos < 0.35,
                0   + (194 -   0) * (pos / 0.35),
            np.where(pos < 0.65,
                194 + (255 - 194) * ((pos - 0.35) / 0.30),
                255 + (107 - 255) * ((pos - 0.65) / 0.35)))

        bch = np.where(pos < 0.35,
                255.0,
            np.where(pos < 0.65,
                255 + (229 - 255) * ((pos - 0.35) / 0.30),
                229 + (  0 - 229) * ((pos - 0.65) / 0.35)))

        grad = np.stack([r, g, bch], axis=-1)
        arr  = np.clip(arr + grad * (gi * 0.28), 0, 255)

    return arr.astype(np.uint8)

# ── Text animations ───────────────────────────────────────────────────────────
def clip_reveal(arr, text, sz, color, cx, cy, prog):
    """Slide text up from behind a hidden mask strip."""
    p    = ease_out(prog)
    f    = font(sz)
    tw, th = tsize(text, sz)
    tx   = cx - tw // 2
    ty_n = cy - th // 2        # natural resting y

    # Shift text down at prog=0; at prog=1 it sits at ty_n
    y_shift = int((1.0 - p) * (th + 14))
    ty = ty_n + y_shift

    tmp = Image.new('RGB', (W, H))
    ImageDraw.Draw(tmp).text((tx, ty), text, font=f, fill=color)
    src = np.array(tmp)

    # Clip window = [ty_n-2 .. ty_n+th+2]
    r0 = max(0, ty_n - 2)
    r1 = min(H, ty_n + th + 2)
    result = arr.copy()
    if r1 > r0:
        region = src[r0:r1]
        mask   = np.any(region > 18, axis=-1)
        result[r0:r1][mask] = region[mask]
    return result

def scale_punch(arr, text, sz, color, cx, cy, prog, style='fill'):
    """Scale in from 130% → 100% with a small overshoot."""
    p = ease_out(prog)
    if p < 0.82:
        scale = 1.30 - 0.30 * (p / 0.82)
    else:
        ov    = (p - 0.82) / 0.18
        scale = 1.0 - 0.028 * math.sin(ov * math.pi)

    ss   = max(8, int(sz * scale))
    f    = font(ss)
    tw, th = tsize(text, ss)
    tx   = cx - tw // 2
    ty   = cy - th // 2

    img  = Image.fromarray(arr)
    d    = ImageDraw.Draw(img)

    if style == 'gradient':
        # Cycle through PURP→BLUE→CYAN→GOLD per word
        grad_colors = [PURP, BLUE, CYAN, GOLD]
        words  = text.split()
        xc = tx
        for i, w in enumerate(words):
            wf   = font(ss)
            bb   = d.textbbox((0, 0), w + ' ', font=wf)
            ww   = bb[2] - bb[0]
            c    = grad_colors[i % len(grad_colors)]
            d.text((xc, ty), w, font=wf, fill=c)
            xc  += ww
    else:
        d.text((tx, ty), text, font=f, fill=color)

    return np.array(img)

def fade_in(arr, text, sz, color, cx, cy, prog):
    p   = ease_io(prog)
    a   = int(255 * p)
    f   = font(sz)
    tw, th = tsize(text, sz)
    tx  = cx - tw // 2
    ty  = cy - th // 2

    base    = Image.fromarray(arr).convert('RGBA')
    overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(overlay).text((tx, ty), text, font=f, fill=(*color, a))
    return np.array(Image.alpha_composite(base, overlay).convert('RGB'))

# ── Shape accent line ─────────────────────────────────────────────────────────
def accent_line(arr, y, prog):
    p  = ease_out(prog)
    lw = int(W * p)
    if lw <= 0 or not (0 <= y < H):
        return arr
    x0 = (W - lw) // 2
    x1 = x0 + lw
    result = arr.copy()
    alpha  = 0.40
    result[y, x0:x1] = np.clip(
        result[y, x0:x1].astype(np.float32) * (1 - alpha) + np.array([255, 255, 255]) * alpha,
        0, 255
    ).astype(np.uint8)
    return result

# ── Effects ───────────────────────────────────────────────────────────────────
def add_grain(arr, fi):
    return np.clip(arr.astype(np.float32) + GRAIN[fi % 8] * 0.85, 0, 255).astype(np.uint8)

def add_bars(arr):
    arr[:BAR_H]      = 0
    arr[H - BAR_H:]  = 0
    return arr

# ── Scene / animation data ────────────────────────────────────────────────────
# Tuple: (scene_start, scene_end, gradient, g_intensity, [elements])
# Element: (text, size, color, cx, cy_frac, anim, in_t, dur, out_t [, style])

SCENES = [

    # ── HOOK (0–2 s) ──────────────────────────────────────────────────────
    (b(1), b(5), True, 0.88, [
        ('MOST PEOPLE',       153, WHT,  CX, 0.44, 'reveal', b(1),      0.33, b(5)     ),
        ('SCROLL PAST THIS.', 90,  GOLD, CX, 0.56, 'reveal', b(2),      0.33, b(5)     ),
    ]),

    # ── BUILD 1 (2–4 s) ───────────────────────────────────────────────────
    (b(5), b(9), False, 0, [
        ('WHILE THEY SCROLL', 122, WHT,  CX, 0.43, 'punch',  b(5),      0.22, b(9)     ),
        ('YOU BUILD.',        146, BLUE, CX, 0.59, 'reveal', b(6),      0.30, b(9)     ),
    ]),

    # ── BUILD 2 (4–7 s) ───────────────────────────────────────────────────
    (b(9), b(15), False, 0, [
        ('EVERY WEBSITE',       126, WHT,  CX, 0.40, 'reveal', b(9),    0.30, b(15)    ),
        ('IS A MONEY MACHINE.', 78,  GOLD, CX, 0.53, 'punch',  b(10),   0.26, b(15)    ),
    ]),

    # ── BUILD 3: word swap (7–10 s) ────────────────────────────────────────
    (b(15), b(21), False, 0, [
        ('NO DEGREE.', 118, WHT,  CX, 0.50, 'punch', b(15), 0.20, b(17)              ),
        ('NO BOSS.',   118, WHT,  CX, 0.50, 'punch', b(17), 0.20, b(19)              ),
        ('NO OFFICE.', 118, CGLD, CX, 0.50, 'punch', b(19), 0.20, b(21)              ),
    ]),

    # ── PRE-PEAK (10–14 s) ────────────────────────────────────────────────
    (b(21), b(29), False, 0, [
        ('JUST A LAPTOP',         140, WHT, CX, 0.43, 'reveal', b(21),  0.30, b(29)   ),
        ('AND THE RIGHT SKILLS.',  74, WHT, CX, 0.56, 'reveal', b(22),  0.30, b(29)   ),
    ]),

    # ── PEAK / DROP (14–22 s) ─────────────────────────────────────────────
    (b(29), b(45), True, 1.40, [
        ('$3,000 A MONTH', 142, WHT,  CX, 0.35, 'punch',  b(29),       0.17, b(45)   ),
        ('STARTS WITH',     72, GREY, CX, 0.50, 'reveal', b(30),       0.26, b(45)   ),
        ('ONE CLIENT.',    150, GOLD, CX, 0.64, 'punch',  b(31),       0.17, b(45), 'gradient'),
    ]),

    # ── RESOLUTION (22–28 s) ─────────────────────────────────────────────
    (b(45), b(57), False, 0, [
        ('BUILD WEBSITES.', 130, WHT,  CX, 0.42, 'reveal', b(45),      0.36, b(57)   ),
        ('BUILD WEALTH.',   130, CGLD, CX, 0.56, 'reveal', b(46),      0.36, b(57)   ),
    ]),

    # ── CTA (28–32 s) ────────────────────────────────────────────────────
    (b(57), b(65), False, 0, [
        ('FOLLOW FOR MORE.', 74, GOLD, CX, 0.50, 'fade', b(57) + 0.10, 0.44, b(65)   ),
    ]),
]

# ── Frame renderer ────────────────────────────────────────────────────────────
def render_frame(fi):
    t = fi / FPS

    # Find scene
    scene = None
    for sc in SCENES:
        if sc[0] <= t < sc[1]:
            scene = sc
            break

    if scene is None:
        arr = np.zeros((H, W, 3), dtype=np.uint8)
    else:
        s0, s1, grad, gi, elems = scene
        arr = make_bg(t, gradient=grad, gi=gi)

        for elem in elems:
            text, sz, color, cx, cy_f, anim, in_t, dur = elem[:8]
            out_t = elem[8] if len(elem) > 8 else s1
            style = elem[9] if len(elem) > 9 else 'fill'
            cy    = int(H * cy_f)

            if t < in_t or t > out_t:
                continue

            prog = (t - in_t) / dur if dur > 0 else 1.0

            if   anim == 'reveal': arr = clip_reveal(arr, text, sz, color, cx, cy, prog)
            elif anim == 'punch':  arr = scale_punch(arr, text, sz, color, cx, cy, prog, style)
            elif anim == 'fade':   arr = fade_in(    arr, text, sz, color, cx, cy, prog)

    # Accent lines
    if 0.05 <= t < 2.0:
        arr = accent_line(arr, int(H * 0.496), (t - 0.05) / 0.38)
    elif 14.0 <= t < 22.0:
        for i, yf in enumerate([0.298, 0.312, 0.326]):
            arr = accent_line(arr, int(H * yf), (t - 14.0 - i * 0.07) / 0.28)

    arr = add_grain(arr, fi)
    arr = add_bars(arr)
    return arr

# ── Audio: dark trap beat (120 BPM) ──────────────────────────────────────────
def gen_audio(dur, sr=44100):
    n   = int(dur * sr)
    out = np.zeros(n, dtype=np.float32)

    def kick(t, v=0.82):
        L  = int(0.20 * sr)
        tt = np.linspace(0, 0.20, L)
        env = np.exp(-tt / 0.07)
        f0  = 60.0 * np.exp(-tt * 20)
        sig = np.sin(2 * np.pi * f0 * tt) * env
        i0  = int(t * sr);  i1 = min(i0 + L, n)
        out[i0:i1] += sig[:i1-i0] * v

    def sub(t, v=0.55, f0=42):
        L  = int(0.55 * sr)
        tt = np.linspace(0, 0.55, L)
        env = np.exp(-tt / 0.38)
        sig = np.sin(2 * np.pi * f0 * tt) * env
        i0  = int(t * sr);  i1 = min(i0 + L, n)
        out[i0:i1] += sig[:i1-i0] * v

    def hat(t, v=0.16):
        L  = int(0.045 * sr)
        tt = np.linspace(0, 0.045, L)
        rr = np.random.default_rng(int(t * 500)).normal(0, 1, L)
        sig = rr * np.exp(-tt / 0.014)
        i0  = int(t * sr);  i1 = min(i0 + L, n)
        out[i0:i1] += sig[:i1-i0] * v

    def clap(t, v=0.32):
        L  = int(0.07 * sr)
        tt = np.linspace(0, 0.07, L)
        rr = np.random.default_rng(int(t * 777 + 3)).normal(0, 1, L)
        sig = rr * np.exp(-tt / 0.028)
        i0  = int(t * sr);  i1 = min(i0 + L, n)
        out[i0:i1] += sig[:i1-i0] * v

    beats = int(dur / BEAT) + 2
    for i in range(beats):
        tb  = i * BEAT
        bib = i % 4
        if tb > dur:
            break

        if bib in (0, 2):        kick(tb)
        if bib == 2:             clap(tb)
        hat(tb)
        hat(tb + BEAT * 0.5)
        if 14.0 <= tb < 22.0:
            hat(tb + BEAT * 0.25)
            hat(tb + BEAT * 0.75)
        if bib == 0 and tb >= 2.0:
            sub(tb, v=0.38)

    # Big hit at the drop
    sub(14.0, v=0.92, f0=36)
    sub(14.0 + BEAT,      v=0.52, f0=42)
    sub(14.0 + BEAT * 2,  v=0.42, f0=42)

    # Atmospheric pad
    tt = np.linspace(0, dur, n)
    pad  = np.sin(2 * np.pi * 55  * tt) * 0.038
    pad += np.sin(2 * np.pi * 82  * tt) * 0.026
    pad += np.sin(2 * np.pi * 110 * tt) * 0.018
    pad *= np.clip(tt / 2.5, 0, 1)    # fade in
    out += pad

    mx = np.max(np.abs(out))
    if mx > 0:
        out = out / mx * 0.88
    return (out * 32767).astype(np.int16)

# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    OUT  = sys.argv[1] if len(sys.argv) > 1 else '/tmp/001_BuildingWebsites_v01.mp4'
    VID  = '/tmp/_vid_raw.mp4'
    AUD  = '/tmp/_beat.wav'

    print(f"Font     : {_FONT_PATH}")
    print(f"Output   : {OUT}")
    print(f"Frames   : {FRAMES}  ({DUR}s @ {FPS}fps  {W}×{H})")

    # ── Video pass ──────────────────────────────────────────────────────────
    print("\n[1/3] Rendering frames…")
    proc = subprocess.Popen([
        'ffmpeg', '-y',
        '-f', 'rawvideo', '-vcodec', 'rawvideo',
        '-s', f'{W}x{H}', '-pix_fmt', 'rgb24', '-r', str(FPS),
        '-i', 'pipe:0',
        '-vcodec', 'libx264', '-pix_fmt', 'yuv420p',
        '-crf', '17', '-preset', 'fast',
        VID
    ], stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)

    for fi in range(FRAMES):
        if fi % (FPS * 5) == 0:
            print(f"  {fi // FPS:>3}s / {DUR}s  …")
        proc.stdin.write(render_frame(fi).tobytes())

    proc.stdin.close()
    proc.wait()
    print("  Frames done.")

    # ── Audio pass ──────────────────────────────────────────────────────────
    print("\n[2/3] Generating beat…")
    pcm = gen_audio(DUR + 0.5)
    with wave.open(AUD, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(44100)
        wf.writeframes(pcm.tobytes())
    print("  Audio done.")

    # ── Mux ─────────────────────────────────────────────────────────────────
    print("\n[3/3] Muxing…")
    subprocess.run([
        'ffmpeg', '-y',
        '-i', VID, '-i', AUD,
        '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
        '-shortest', '-movflags', '+faststart',
        OUT
    ], check=True, stderr=subprocess.DEVNULL)

    size_mb = os.path.getsize(OUT) / 1024 / 1024
    print(f"\n✓  Done!  {OUT}  ({size_mb:.1f} MB)\n")
