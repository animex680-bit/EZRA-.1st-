/* Nocturne — hand-written WebGL2 + a small motion system.
   No libraries, no CDN, no model files: the wheel is a signed-distance field
   raymarched in the fragment shader, so the whole scene weighs a few kilobytes. */
(() => {
  'use strict';

  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const lerp = (a, b, t) => a + (b - a) * t;
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));

  /* ─────────────────────────── scroll ─────────────────────────── */
  const scroll = { raw: 0, eased: 0 };
  const maxScroll = () => Math.max(1, document.body.scrollHeight - innerHeight);
  const readScroll = () => { scroll.raw = clamp(scrollY / maxScroll(), 0, 1); };
  readScroll();
  scroll.eased = scroll.raw;
  addEventListener('scroll', readScroll, { passive: true });
  addEventListener('resize', readScroll);

  /* ─────────────────────────── pointer ─────────────────────────── */
  const ptr = { x: .5, y: .5, ex: .5, ey: .5, active: false };
  addEventListener('pointermove', e => {
    ptr.x = e.clientX / innerWidth; ptr.y = 1 - e.clientY / innerHeight; ptr.active = true;
  }, { passive: true });

  /* ─────────────────────────── webgl ─────────────────────────── */
  const FRAG = `#version 300 es
precision highp float;
out vec4 fragColor;
uniform vec2 uRes; uniform float uTime; uniform float uScroll; uniform vec2 uMouse; uniform vec2 uOffset;

#define EPS 0.0010
float smin(float a,float b,float k){float h=clamp(.5+.5*(b-a)/k,0.,1.);return mix(b,a,h)-k*h*(1.-h);}
mat2 rot(float a){float c=cos(a),s=sin(a);return mat2(c,-s,s,c);}
float torus(vec3 p, vec2 t){ vec2 q=vec2(length(p.xz)-t.x, p.y); return length(q)-t.y; }
float sph(vec3 p, float r){ return length(p)-r; }

// Three interlocking rings on different axes — an armillary. Chrome on near-black,
// which is the clearest way to show real reflection: a chrome surface is almost
// entirely the room around it, and no CSS gradient can fake that.
float map(vec3 p, out float id){
  float sep = 0.08 + uScroll*0.30;            // the rings draw apart as you read
  float t = uTime*0.22;

  vec3 a = p; a.xz *= rot(t*0.9);  a.yz *= rot(0.42);
  vec3 b = p; b.xy *= rot(-t*0.72); b.yz *= rot(1.22);
  vec3 c = p; c.yz *= rot(t*0.55);  c.xz *= rot(0.95);

  float r1 = torus(a - vec3(0.0,  sep*0.35, 0.0), vec2(0.95, 0.052));
  float r2 = torus(b - vec3(sep*0.30, 0.0, 0.0),  vec2(0.74, 0.044));
  float r3 = torus(c - vec3(0.0, -sep*0.30, 0.0), vec2(0.52, 0.036));

  float core = sph(p, 0.175 + 0.022*sin(uTime*1.1));

  id = 1.0; float d = r1;
  if (r2 < d){ d = r2; id = 2.0; }
  if (r3 < d){ d = r3; id = 3.0; }
  if (core < d){ d = core; id = 4.0; }

  float fl = p.y + 1.30;
  if (fl < d){ d = fl; id = 5.0; }
  return d;
}
float mapD(vec3 p){ float i; return map(p,i); }
vec3 normal(vec3 p){ vec2 e=vec2(EPS,0.);
  return normalize(vec3(mapD(p+e.xyy)-mapD(p-e.xyy),mapD(p+e.yxy)-mapD(p-e.yxy),mapD(p+e.yyx)-mapD(p-e.yyx))); }
float march(vec3 ro,vec3 rd,out float id,int steps){
  float t=0.0; id=0.0;
  for(int i=0;i<140;i++){ if(i>=steps)break;
    float h=map(ro+rd*t,id);
    if(h<EPS*t*0.8+EPS) return t;
    t+=h*0.92; if(t>18.0)break; }
  id=0.0; return -1.0;
}
float shadow(vec3 ro,vec3 rd){ float res=1.0,t=0.04;
  for(int i=0;i<24;i++){ float h=mapD(ro+rd*t); res=min(res,8.0*h/t);
    t+=clamp(h,0.02,0.3); if(res<0.004||t>6.0)break;} return clamp(res,0.,1.); }
float ao(vec3 p, vec3 n){ float o=0.,s=1.;
  for(int i=0;i<5;i++){ float d=0.02+0.06*float(i); o+=(d-mapD(p+n*d))*s; s*=0.74; }
  return clamp(1.0-1.7*o,0.,1.); }

// a cool studio: two white strips and one blue kicker
vec3 env(vec3 rd){
  float h = rd.y*0.5+0.5;
  vec3 c = mix(vec3(0.026,0.028,0.034), vec3(0.10,0.108,0.128), pow(h,1.5));
  c += vec3(1.0,0.99,0.97)*smoothstep(0.30,0.0,abs(rd.y-0.62))*smoothstep(1.0,0.25,abs(rd.x))*2.6;
  c += vec3(1.0,0.98,0.95)*smoothstep(0.20,0.0,abs(rd.x-0.78))*smoothstep(0.9,0.1,abs(rd.y))*1.1;
  c += vec3(0.40,0.60,1.0)*smoothstep(0.30,0.0,abs(rd.x+0.72))*smoothstep(0.9,0.0,abs(rd.y+0.1))*0.95;
  return c;
}

void main(){
  vec2 uv = (gl_FragCoord.xy - 0.5*uRes)/uRes.y + uOffset;

  float yaw = 0.35 + (uMouse.x-0.5)*0.75 + uScroll*0.55;
  float pit = 0.16 + (uMouse.y-0.5)*0.42 - uScroll*0.10;
  float dist = 3.45;
  vec3 ro = vec3(sin(yaw)*cos(pit), sin(pit)+0.16, cos(yaw)*cos(pit))*dist;
  vec3 ta = vec3(0.0, 0.02, 0.0);
  vec3 fw = normalize(ta-ro), rg = normalize(cross(fw,vec3(0,1,0))), up = cross(rg,fw);
  vec3 rd = normalize(uv.x*rg + uv.y*up + 1.85*fw);

  float id; float t = march(ro,rd,id,130);
  vec3 col;
  if (t > 0.0){
    vec3 p = ro+rd*t, n = normal(p);
    vec3 key = normalize(vec3(0.30,0.86,0.40));
    float sh = shadow(p+n*0.02,key), occ = ao(p,n);
    float dif = max(dot(n,key),0.0)*sh;
    vec3 r = reflect(rd,n);
    float fres = pow(1.0-max(dot(-rd,n),0.0),5.0);
    vec3 refl = env(r);

    if (id < 4.5){
      // chrome — almost entirely reflection, with a hint of tint per ring
      vec3 tint = id < 1.5 ? vec3(1.0,0.99,0.98)
                : id < 2.5 ? vec3(0.95,0.97,1.0)
                : id < 3.5 ? vec3(1.0,0.96,0.92)
                           : vec3(0.72,0.84,1.0);
      col = refl*tint*(1.05 + 0.30*dif);
      col = mix(col*0.80, col, clamp(0.45+fres,0.,1.));
      col += vec3(1.0)*pow(max(dot(n,normalize(key-rd)),0.0),220.0)*2.4*sh;
      if (id > 3.5) col += vec3(0.30,0.55,1.0)*0.30;   // the core glows faintly
      col *= occ;
    } else {
      float fade = exp(-length(p.xz)*0.26);
      col = mix(vec3(0.022,0.023,0.028), vec3(0.050,0.052,0.060), fade);
      vec3 rr = reflect(rd,n); float rid;
      float rt = march(p+n*0.02, rr, rid, 46);
      if (rt > 0.0 && rid > 0.5 && rid < 4.5){
        vec3 rp = p+n*0.02+rr*rt;
        col = mix(col, env(reflect(rr, normal(rp)))*0.55, 0.40*fade);
      } else col = mix(col, env(rr)*0.32, 0.26*fade);
      col *= 1.0 - 0.55*exp(-length(p.xz)*0.95);
      // fade the floor into the backdrop so the horizon is not a hard edge
      float hz = smoothstep(6.0, 16.0, length(p.xz));
      col = mix(col, mix(vec3(0.028,0.030,0.038), vec3(0.058,0.064,0.082), 0.5), hz);
    }
  } else {
    // backdrop is a clean gradient only — the softboxes live in the reflections,
    // where they belong. Painting them on the backdrop reads as a seam.
    float h = rd.y*0.5+0.5;
    col = mix(vec3(0.028,0.030,0.038), vec3(0.058,0.064,0.082), pow(h,1.3));
    col += vec3(0.16,0.26,0.52)*smoothstep(0.55,0.0,length(rd.xy-vec2(-0.45,0.05)))*0.22;
  }

  col = max(col,0.0);
  col = col/(1.0+col*0.55);
  col = pow(col, vec3(0.93));
  col *= 1.0 - 0.32*dot(uv,uv);
  float g = fract(sin(dot(gl_FragCoord.xy+uTime,vec2(12.9898,78.233)))*43758.5453);
  col += (g-0.5)*0.013;
  fragColor = vec4(col,1.0);
}
`;
  const VERT = `#version 300 es
in vec2 p; void main(){ gl_Position = vec4(p, 0.0, 1.0); }`;

  const canvas = document.getElementById('gl');
  const fallback = document.getElementById('fallback');
  let gl = null, prog = null, uni = {}, running = false, quality = 1;

  function fail() {
    // A WebGL failure must never leave a blank screen. This is a rule the
    // pipeline learned the hard way: show something, always.
    if (fallback) fallback.classList.add('on');
    if (canvas) canvas.style.display = 'none';
    running = false;
  }

  function compile(type, src) {
    const s = gl.createShader(type);
    gl.shaderSource(s, src); gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) { console.warn(gl.getShaderInfoLog(s)); return null; }
    return s;
  }

  function initGL() {
    try { gl = canvas.getContext('webgl2', { antialias: false, alpha: false, powerPreference: 'high-performance' }); }
    catch (e) { gl = null; }
    if (!gl) { fail(); return false; }

    const vs = compile(gl.VERTEX_SHADER, VERT), fs = compile(gl.FRAGMENT_SHADER, FRAG);
    if (!vs || !fs) { fail(); return false; }
    prog = gl.createProgram();
    gl.attachShader(prog, vs); gl.attachShader(prog, fs); gl.linkProgram(prog);
    if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) { console.warn(gl.getProgramInfoLog(prog)); fail(); return false; }
    gl.useProgram(prog);

    const buf = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
    const loc = gl.getAttribLocation(prog, 'p');
    gl.enableVertexAttribArray(loc);
    gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);

    for (const n of ['uRes', 'uTime', 'uScroll', 'uMouse', 'uOffset']) uni[n] = gl.getUniformLocation(prog, n);

    canvas.addEventListener('webglcontextlost', e => { e.preventDefault(); running = false; fail(); });
    return true;
  }

  function resize() {
    if (!gl) return;
    // Raymarching is fill-rate bound, so render below CSS resolution and let the
    // browser scale up. Small screens get a lower factor still.
    const narrow = innerWidth < 760;
    const cap = narrow ? 1.1 : 1.5;
    const scale = (narrow ? 0.52 : 0.66) * quality;
    const dpr = Math.min(devicePixelRatio || 1, cap);
    const w = Math.max(1, Math.round(innerWidth * dpr * scale));
    const h = Math.max(1, Math.round(innerHeight * dpr * scale));
    if (canvas.width !== w || canvas.height !== h) {
      canvas.width = w; canvas.height = h;
      gl.viewport(0, 0, w, h);
    }
  }

  let t0 = performance.now(), frames = 0, acc = 0, downgraded = false;
  function frame(now) {
    if (!running) return;
    const dt = Math.min(0.05, (now - t0) / 1000); t0 = now;

    scroll.eased = lerp(scroll.eased, scroll.raw, reduced ? 1 : 0.075);
    ptr.ex = lerp(ptr.ex, ptr.x, 0.06);
    ptr.ey = lerp(ptr.ey, ptr.y, 0.06);

    resize();
    gl.uniform2f(uni.uRes, canvas.width, canvas.height);
    gl.uniform1f(uni.uTime, reduced ? 0 : (now - startedAt) / 1000);
    gl.uniform1f(uni.uScroll, scroll.eased);
    gl.uniform2f(uni.uMouse, ptr.ex, ptr.ey);
    // push the subject clear of the headline on wide screens; centre it low on narrow ones
    const wide = innerWidth > 900;
    gl.uniform2f(uni.uOffset, wide ? -0.30 : 0.0, wide ? 0.02 : -0.16);
    gl.drawArrays(gl.TRIANGLES, 0, 3);

    // If the device cannot hold a reasonable frame rate, drop resolution once.
    acc += dt; frames++;
    if (!downgraded && acc > 1.4) {
      if (frames / acc < 26) { quality = 0.72; downgraded = true; }
      acc = 0; frames = 0;
    }

    if (reduced) { running = false; return; }   // one frame is enough
    requestAnimationFrame(frame);
  }

  let startedAt = performance.now();
  function start() { if (running || !gl) return; running = true; t0 = performance.now(); requestAnimationFrame(frame); }
  function stop() { running = false; }

  if (canvas && initGL()) {
    resize();
    addEventListener('resize', resize);
    document.addEventListener('visibilitychange', () => document.hidden ? stop() : start());
    start();
  }

  /* ───────────────────── scroll-built headlines ─────────────────────
     The characters are generated as the line arrives and settle into a clean
     baseline — no residual transform at rest, so the set text stays legible. */
  const assembled = [];
  document.querySelectorAll('[data-assemble]').forEach(el => {
    const text = el.textContent.trim();
    el.textContent = '';
    const frag = document.createDocumentFragment();
    let i = 0;
    // Characters are grouped into words. Without this the line can break
    // between two letters of the same word, which looks broken, not designed.
    text.split(/(\s+)/).forEach(tok => {
      if (!tok) return;
      if (/^\s+$/.test(tok)) { frag.appendChild(document.createTextNode(' ')); return; }
      const word = document.createElement('span');
      word.className = 'word';
      for (const c of tok) {
        const s = document.createElement('span');
        s.className = 'ch'; s.textContent = c;
        s.dataset.seed = String((Math.sin(i * 12.9898) * 43758.5453) % 1);
        word.appendChild(s); i++;
      }
      frag.appendChild(word);
    });
    el.appendChild(frag);
    assembled.push({ el, chars: [...el.querySelectorAll('.ch')] });
  });

  function paintAssembled() {
    for (const a of assembled) {
      const r = a.el.getBoundingClientRect();
      // 0 while below the fold -> 1 once it has risen into comfortable reading position
      const p = clamp((innerHeight * 0.92 - r.top) / (innerHeight * 0.42), 0, 1);
      const n = a.chars.length;
      for (let i = 0; i < n; i++) {
        const ch = a.chars[i];
        const local = clamp(p * (n + 10) - i, 0, 1);
        const e = 1 - Math.pow(1 - local, 3);
        const seed = parseFloat(ch.dataset.seed) || 0;
        const dy = (1 - e) * (16 + seed * 26);
        const dx = (1 - e) * seed * 14;
        const rot = (1 - e) * seed * 9;
        ch.style.opacity = e;
        ch.style.transform = e >= 1 ? '' : `translate3d(${dx.toFixed(2)}px,${dy.toFixed(2)}px,0) rotate(${rot.toFixed(2)}deg)`;
      }
    }
  }
  if (reduced) assembled.forEach(a => a.chars.forEach(c => { c.style.opacity = 1; c.style.transform = ''; }));

  /* ───────────────────── reveals ───────────────────── */
  const io = new IntersectionObserver(es => {
    es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { rootMargin: '0px 0px -12% 0px', threshold: 0.08 });
  document.querySelectorAll('[data-reveal]').forEach(el => io.observe(el));

  /* ───────────────────── count-up ───────────────────── */
  const counters = [...document.querySelectorAll('[data-count]')];
  const cio = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return;
    const el = e.target, target = parseFloat(el.dataset.count);
    cio.unobserve(el);
    if (reduced) { el.textContent = target; return; }
    const dur = 1100, t0 = performance.now();
    const tick = n => {
      const k = clamp((n - t0) / dur, 0, 1);
      el.textContent = Math.round(target * (1 - Math.pow(1 - k, 3)));
      if (k < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }), { threshold: 0.4 });
  counters.forEach(el => cio.observe(el));

  /* ───────────────────── magnetic buttons ─────────────────────
     They react before the cursor reaches them, and the glow follows the pointer. */
  const magnets = [...document.querySelectorAll('.magnetic')].map(el => ({ el, x: 0, y: 0, tx: 0, ty: 0 }));

  /* ───────────────────── drifting, cursor-aware tiles ─────────────────────
     Nothing on the page is ever completely still, and tiles lean away from the
     cursor rather than sitting there inertly. */
  const tiles = [...document.querySelectorAll('.drift')].map((el, i) => ({
    el, i, x: 0, y: 0, tx: 0, ty: 0, ph: i * 1.7
  }));

  let mt = 0;
  function motion(now) {
    const t = now / 1000;
    if (!reduced) {
      for (const m of magnets) {
        const r = m.el.getBoundingClientRect();
        const cx = r.left + r.width / 2, cy = r.top + r.height / 2;
        const dx = (ptr.x * innerWidth) - cx, dy = ((1 - ptr.y) * innerHeight) - cy;
        const d = Math.hypot(dx, dy);
        const reach = Math.max(r.width, r.height) * 1.5;
        const k = d < reach ? (1 - d / reach) : 0;
        m.tx = dx * k * 0.26; m.ty = dy * k * 0.26;
        m.x = lerp(m.x, m.tx, 0.13); m.y = lerp(m.y, m.ty, 0.13);
        m.el.style.transform = (Math.abs(m.x) < 0.05 && Math.abs(m.y) < 0.05) ? '' : `translate3d(${m.x.toFixed(2)}px,${m.y.toFixed(2)}px,0)`;
        m.el.style.setProperty('--mx', (dx * k * 0.5).toFixed(1) + 'px');
        m.el.style.setProperty('--my', (dy * k * 0.5).toFixed(1) + 'px');
      }
      for (const tl of tiles) {
        const r = tl.el.getBoundingClientRect();
        const cx = r.left + r.width / 2, cy = r.top + r.height / 2;
        const dx = (ptr.x * innerWidth) - cx, dy = ((1 - ptr.y) * innerHeight) - cy;
        const d = Math.hypot(dx, dy);
        const reach = r.width * 1.25;
        const k = d < reach ? (1 - d / reach) : 0;
        // perpetual drift, plus an evasive lean away from the pointer
        tl.tx = Math.sin(t * 0.42 + tl.ph) * 5 - dx * k * 0.045;
        tl.ty = Math.cos(t * 0.35 + tl.ph * 1.3) * 6 - dy * k * 0.045;
        tl.x = lerp(tl.x, tl.tx, 0.045); tl.y = lerp(tl.y, tl.ty, 0.045);
        tl.el.style.transform = `translate3d(${tl.x.toFixed(2)}px,${tl.y.toFixed(2)}px,0)`;
      }
    }
    paintAssembled();
    mt = requestAnimationFrame(motion);
  }
  requestAnimationFrame(motion);

  /* ───────────────────── nav hide on the way down ───────────────────── */
  const nav = document.querySelector('.nav');
  let lastY = scrollY;
  addEventListener('scroll', () => {
    const y = scrollY;
    if (nav) nav.classList.toggle('up', y > lastY && y > 260);
    lastY = y;
  }, { passive: true });
})();
