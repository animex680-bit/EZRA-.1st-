import { useEffect, useRef, useState, Suspense } from 'react';
import { Canvas } from '@react-three/fiber';
import { Environment, AdaptiveDpr } from '@react-three/drei';
import Lenis from 'lenis';
import GlassDoor from './GlassDoor.jsx';

function Loader({ pct, hide }) {
  return (
    <div className={`loader ${hide ? 'hide' : ''}`}>
      <div className="mk">Aluminium Windows Cape Town</div>
      <div className="track"><span style={{ width: `${pct}%` }} /></div>
      <div className="sub">Framing Light</div>
    </div>
  );
}

export default function App() {
  const progressRef = useRef(0); // door-open scrub 0..1
  const [pct, setPct] = useState(0);
  const [ready, setReady] = useState(false);
  const reduce = useRef(
    typeof window !== 'undefined' &&
      window.matchMedia &&
      window.matchMedia('(prefers-reduced-motion: reduce)').matches
  );

  // smooth scroll + map scroll over the reveal-spacer to door progress
  useEffect(() => {
    const revealEl = document.getElementById('reveal');
    if (reduce.current) {
      // reduced motion: open the door immediately, no smooth scroll
      progressRef.current = 1;
      return;
    }
    const lenis = new Lenis({ lerp: 0.1, smoothWheel: true });
    let raf;
    const loop = (t) => {
      lenis.raf(t);
      // compute progress from the reveal section's position
      if (revealEl) {
        const r = revealEl.getBoundingClientRect();
        const total = r.height - window.innerHeight;
        const p = Math.max(0, Math.min(1, -r.top / Math.max(1, total)));
        progressRef.current = p;
      }
      raf = requestAnimationFrame(loop);
    };
    raf = requestAnimationFrame(loop);
    return () => {
      cancelAnimationFrame(raf);
      lenis.destroy();
    };
  }, []);

  // fake-but-honest asset progress tied to a short warmup, then reveal
  useEffect(() => {
    let p = 0;
    const id = setInterval(() => {
      p = Math.min(100, p + 8 + Math.random() * 14);
      setPct(Math.round(p));
      if (p >= 100) {
        clearInterval(id);
        setTimeout(() => setReady(true), 500);
      }
    }, 120);
    return () => clearInterval(id);
  }, []);

  return (
    <>
      <Loader pct={pct} hide={ready} />

      <div className="scene-wrap">
        <Canvas
          dpr={[1, 2]}
          gl={{ antialias: true, powerPreference: 'high-performance', alpha: false }}
          camera={{ position: [0, 0, 8.5], fov: 42 }}
        >
          <color attach="background" args={['#0e0f10']} />
          <ambientLight intensity={0.35} />
          <directionalLight position={[4, 6, 5]} intensity={1.6} color="#fff3df" />
          <directionalLight position={[-5, 2, 3]} intensity={0.5} color="#cfe6ff" />
          <Suspense fallback={null}>
            <Environment preset="sunset" />
            <GlassDoor progressRef={progressRef} />
          </Suspense>
          <AdaptiveDpr pixelated />
        </Canvas>
      </div>

      <div className="chrome">
        <div className="brand">
          AWCT
          <small>Cape Town</small>
        </div>
        <nav className="nav">
          <a href="#range">Range</a>
          <a href="#made">Made Here</a>
          <a href="#quote">Get a Quote</a>
        </nav>
      </div>

      <main className="content">
        {/* HERO */}
        <section className="hero">
          <div className="pad">
            <h1>We frame the light.</h1>
            <p className="sub">
              Aluminium windows &amp; doors that dissolve the wall between your home and the
              Cape. Designed, manufactured and installed — in-house, made to your exact spec.
            </p>
          </div>
        </section>

        {/* REVEAL — drives the door opening via scroll over this tall spacer */}
        <section id="reveal" className="reveal-spacer">
          <div style={{ position: 'sticky', top: 0, height: '100svh', display: 'flex', alignItems: 'center' }}>
            <div className="pad">
              <div className="eyebrow">Scroll — open the wall</div>
              <h2 style={{ fontFamily: 'var(--d)', fontWeight: 800, fontSize: 'clamp(28px,4vw,56px)', letterSpacing: '-.025em', maxWidth: '16ch', lineHeight: 1.0 }}>
                A stacking door doesn’t divide a room. It removes one.
              </h2>
            </div>
          </div>
        </section>

        {/* RANGE */}
        <section id="range" className="beat">
          <div className="pad">
            <div className="eyebrow">The Range</div>
            <h2>Every opening, engineered.</h2>
            <p>From frameless sliding walls to side-hung casements — each profile thermally
              broken, climate-proof, and finished to architectural tolerance.</p>
            <div className="range-grid">
              {[
                ['Folding / Stacking', 'Up to 6 leaves'],
                ['Sliding Doors', 'Frameless options'],
                ['Casement Windows', 'Side & top hung'],
                ['Shopfronts', 'Commercial spec'],
              ].map(([n, m]) => (
                <div className="pcard" key={n}>
                  <div className="n">{n}</div>
                  <div className="m">{m}</div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* MADE HERE */}
        <section id="made" className="beat">
          <div className="pad">
            <div className="eyebrow">Made Here</div>
            <h2>Our factory. Your tolerances.</h2>
            <p>In-house production at Racing Park means we control the line from extrusion to
              installation — faster turnaround, tighter tolerances, one point of accountability.</p>
            <div className="stats">
              <div className="stat"><div className="big">In-house</div><div className="lbl">Manufacturing &amp; install</div></div>
              <div className="stat"><div className="big">±1mm</div><div className="lbl">Architectural tolerance</div></div>
              <div className="stat"><div className="big">Western Cape</div><div className="lbl">Climate-rated systems</div></div>
            </div>
          </div>
        </section>

        {/* CTA */}
        <section id="quote" className="cta">
          <div className="pad">
            <h2>Let’s open up your space.</h2>
            <div className="row">
              <a className="btn solid" href="tel:+27673687537">Call +27 67 368 7537</a>
              <a className="btn ghost" href="mailto:admin@tganorth.co.za">Request a quote</a>
            </div>
          </div>
        </section>

        <footer>
          <div className="pad">
            <div>Aluminium Windows Cape Town · Racing Park, 25 Benetton Rd, Killarney Ave</div>
            <div>admin@tganorth.co.za · +27 67 368 7537</div>
          </div>
        </footer>
      </main>

      <div className="scrollcue"><span>Scroll</span><span className="bar" /></div>
      <div className="concept-flag">Unsolicited concept · not affiliated</div>
    </>
  );
}
