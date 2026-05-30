import { useRef, useMemo } from 'react';
import { useFrame } from '@react-three/fiber';
import * as THREE from 'three';

/*
  Procedural Cape Town vista — no external assets (sandbox blocks photo hosts,
  and this stays original + instant-loading). Renders, back to front:
  sunset sky gradient + sun glow, atmospheric haze bands, Table Mountain (flat
  top) with Lion's Head to its right, and a foreground shore. Parallaxes gently
  with pointer and warms as the door opens (uReveal).
*/
export default function Vista({ revealRef }) {
  const mat = useRef();

  const material = useMemo(
    () =>
      new THREE.ShaderMaterial({
        depthWrite: false,
        uniforms: {
          uTime: { value: 0 },
          uReveal: { value: 0 }, // 0..1 door-open, warms/brightens the scene
          uMouse: { value: new THREE.Vector2(0, 0) },
          uAspect: { value: 1.75 },
        },
        vertexShader: /* glsl */ `
          varying vec2 vUv;
          void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }
        `,
        fragmentShader: /* glsl */ `
          precision highp float;
          varying vec2 vUv;
          uniform float uTime, uReveal, uAspect;
          uniform vec2 uMouse;

          // cheap hash + value noise for haze/texture
          float hash(vec2 p){ return fract(sin(dot(p, vec2(41.3, 289.1))) * 43758.5453); }
          float noise(vec2 p){
            vec2 i = floor(p), f = fract(p);
            vec2 u = f*f*(3.0-2.0*f);
            return mix(mix(hash(i+vec2(0,0)), hash(i+vec2(1,0)), u.x),
                       mix(hash(i+vec2(0,1)), hash(i+vec2(1,1)), u.x), u.y);
          }

          // a mountain silhouette given a height profile h(x); returns 1 below ridge
          float below(vec2 uv, float ridge){ return smoothstep(0.004, 0.0, uv.y - ridge); }

          void main(){
            vec2 uv = vUv;
            // pointer parallax (subtle, far layer moves least)
            vec2 p = uv + uMouse * 0.012;
            float x = (p.x - 0.5) * uAspect; // centered, aspect-correct

            // ---------- SKY ----------
            vec3 top = vec3(0.45, 0.52, 0.68);      // cool upper sky
            vec3 mid = vec3(0.96, 0.74, 0.48);      // warm band
            vec3 hor = vec3(1.0, 0.86, 0.62);       // bright horizon
            vec3 sky = mix(top, mid, smoothstep(0.95, 0.45, p.y));
            sky = mix(sky, hor, smoothstep(0.5, 0.28, p.y));
            // sun glow low-right
            vec2 sun = vec2(0.62, 0.40);
            float d = distance(vec2(p.x, p.y), sun);
            sky += vec3(1.0, 0.8, 0.5) * smoothstep(0.5, 0.0, d) * 0.7;
            sky += vec3(1.0, 0.9, 0.7) * smoothstep(0.06, 0.0, d);   // sun disc

            vec3 col = sky;

            // ---------- TABLE MOUNTAIN (flat top), centered-left ----------
            // flat plateau with steep sides; Devil's Peak step on the right
            float tmTop = 0.46;
            float plateau = smoothstep(0.55, 0.40, abs(x + 0.35)) * 0.0; // unused base
            float tm = tmTop
              + 0.10 * smoothstep(0.9, 0.2, x + 1.15)   // left slope up
              - 0.10 * smoothstep(0.2, 0.9, x + 0.05)   // right slope down (toward saddle)
              + 0.015 * noise(vec2(x*6.0, 1.0));        // rocky texture
            // clamp into a believable flat top
            tm = clamp(tm, tmTop - 0.02, tmTop + 0.12);
            float mTM = below(p, tm) * step(-1.7, x) * step(x, 0.35);

            // Devil's Peak (pointed) to the right of the table
            float dp = 0.30 + 0.22 * exp(-pow((x - 0.62)*3.0, 2.0)) + 0.01*noise(vec2(x*8.0,3.0));
            float mDP = below(p, dp) * step(0.2, x) * step(x, 1.05);

            // Lion's Head (sharp cone) far left
            float lh = 0.26 + 0.30 * exp(-pow((x + 1.35)*4.0, 2.0));
            float mLH = below(p, lh) * step(x, -0.9);

            float mountain = clamp(mTM + mDP + mLH, 0.0, 1.0);

            // mountain shading: cool shadow side, warm sun side
            vec3 mShadow = vec3(0.18, 0.20, 0.28);
            vec3 mLit = vec3(0.40, 0.33, 0.34);
            float lit = smoothstep(-1.0, 1.0, x);     // right side catches sun
            vec3 mountainCol = mix(mShadow, mLit, lit);
            mountainCol += vec3(0.25,0.15,0.10) * smoothstep(0.4,0.0,d) * lit; // rim warmth
            col = mix(col, mountainCol, mountain);

            // ---------- ATMOSPHERIC HAZE at the mountain base ----------
            float haze = smoothstep(0.30, 0.42, p.y) * smoothstep(0.5, 0.34, p.y);
            haze *= 0.5 + 0.5*noise(vec2(x*3.0 + uTime*0.02, p.y*8.0));
            col = mix(col, vec3(0.95,0.85,0.78), haze * 0.5 * mountain);

            // ---------- FOREGROUND (shore / water) ----------
            float water = smoothstep(0.30, 0.26, p.y);
            vec3 waterCol = vec3(0.20, 0.26, 0.30);
            // shimmering reflection of the warm sky
            float shimmer = noise(vec2(p.x*40.0, p.y*120.0 - uTime*0.6));
            waterCol += vec3(0.5,0.4,0.3) * shimmer * 0.12 * smoothstep(0.30,0.0,p.y);
            waterCol = mix(waterCol, hor*vec3(0.7,0.6,0.55), smoothstep(0.30,0.27,p.y)); // bright waterline
            col = mix(col, waterCol, water);

            // ---------- GRADE: warm + brighten as the door opens ----------
            col *= mix(0.78, 1.12, uReveal);
            col = mix(col, col * vec3(1.06, 1.0, 0.92), uReveal); // warmer when open
            // gentle vignette
            float vig = smoothstep(1.25, 0.4, distance(uv, vec2(0.5)));
            col *= mix(0.82, 1.0, vig);
            // subtle film grain
            col += (noise(uv*vec2(900.0,540.0) + uTime) - 0.5) * 0.02;

            gl_FragColor = vec4(col, 1.0);
          }
        `,
      }),
    []
  );

  useFrame((state) => {
    const u = material.uniforms;
    u.uTime.value = state.clock.elapsedTime;
    u.uReveal.value += ((revealRef.current ?? 0) - u.uReveal.value) * 0.08;
    u.uMouse.value.set(state.pointer.x || 0, state.pointer.y || 0);
    u.uAspect.value = state.viewport.aspect || 1.75;
  });

  return (
    <mesh ref={mat} position={[0, 0, -3]} scale={[16, 9, 1]} material={material}>
      <planeGeometry args={[1, 1]} />
    </mesh>
  );
}
