import { useRef, useMemo } from 'react';
import { useFrame } from '@react-three/fiber';
import * as THREE from 'three';
import Vista from './Vista.jsx';

/*
  The signature moment: an aluminium stacking door whose panels slide open as
  `progress` (0..1, driven by scroll) rises, dissolving the wall to reveal the
  vista behind. Glass uses a custom fresnel + tint shader so edges glow with
  raking light — the thing a template can't do, and literally the product.
*/

// --- custom glass material: fresnel rim + view tint, lightweight (mobile-safe) ---
function useGlassMaterial(tint = '#bfe3ea') {
  return useMemo(() => {
    const mat = new THREE.ShaderMaterial({
      transparent: true,
      depthWrite: false,
      side: THREE.DoubleSide,
      uniforms: {
        uTint: { value: new THREE.Color(tint) },
        uRim: { value: new THREE.Color('#f4e3c4') }, // warm light catching the edge
        uOpacity: { value: 0.16 },
        uTime: { value: 0 },
      },
      vertexShader: /* glsl */ `
        varying vec3 vNormalW;
        varying vec3 vViewDir;
        void main() {
          vec4 wp = modelMatrix * vec4(position, 1.0);
          vNormalW = normalize(mat3(modelMatrix) * normal);
          vViewDir = normalize(cameraPosition - wp.xyz);
          gl_Position = projectionMatrix * viewMatrix * wp;
        }
      `,
      fragmentShader: /* glsl */ `
        uniform vec3 uTint;
        uniform vec3 uRim;
        uniform float uOpacity;
        uniform float uTime;
        varying vec3 vNormalW;
        varying vec3 vViewDir;
        void main() {
          float f = 1.0 - max(dot(normalize(vNormalW), normalize(vViewDir)), 0.0);
          float fres = pow(f, 3.0);
          // subtle moving sheen so the glass feels alive
          float sheen = 0.04 * sin(vViewDir.x * 6.0 + uTime * 0.6);
          vec3 col = mix(uTint, uRim, fres) + sheen;
          float alpha = clamp(uOpacity + fres * 0.7, 0.0, 0.9);
          gl_FragColor = vec4(col, alpha);
        }
      `,
    });
    return mat;
  }, [tint]);
}

// a single door leaf: aluminium frame (4 bars) + a glass pane
function Leaf({ width = 1.6, height = 4.2, frame = 0.09, glassMat, depth = 0.06 }) {
  const aluMat = useMemo(
    () =>
      new THREE.MeshStandardMaterial({
        color: '#c8ccce',
        metalness: 0.95,
        roughness: 0.35,
        envMapIntensity: 1.1,
      }),
    []
  );
  const hw = width / 2;
  const hh = height / 2;
  return (
    <group>
      {/* glass pane */}
      <mesh material={glassMat}>
        <planeGeometry args={[width - frame, height - frame]} />
      </mesh>
      {/* frame bars */}
      <mesh material={aluMat} position={[0, hh - frame / 2, 0]}>
        <boxGeometry args={[width, frame, depth]} />
      </mesh>
      <mesh material={aluMat} position={[0, -hh + frame / 2, 0]}>
        <boxGeometry args={[width, frame, depth]} />
      </mesh>
      <mesh material={aluMat} position={[-hw + frame / 2, 0, 0]}>
        <boxGeometry args={[frame, height, depth]} />
      </mesh>
      <mesh material={aluMat} position={[hw - frame / 2, 0, 0]}>
        <boxGeometry args={[frame, height, depth]} />
      </mesh>
    </group>
  );
}

export default function GlassDoor({ progressRef }) {
  const group = useRef();
  const left1 = useRef();
  const left2 = useRef();
  const right1 = useRef();
  const right2 = useRef();
  const rays = useRef();
  const glassMat = useGlassMaterial();

  const leafW = 1.7;
  const eased = useRef(0);

  useFrame((state, dt) => {
    const target = progressRef.current ?? 0;
    // smooth the scroll-driven progress so motion glides (no linear snapping)
    eased.current += (target - eased.current) * Math.min(1, dt * 4);
    const p = eased.current;
    glassMat.uniforms.uTime.value = state.clock.elapsedTime;

    // panels stack outward: closed, two leaves meet each side at center; opening
    // slides them outward, with the outer leaf travelling further (stacking feel).
    const open = p; // 0 closed -> 1 fully stacked
    const base = leafW / 2;
    if (left1.current) left1.current.position.x = -base - open * leafW * 1.6;
    if (left2.current) left2.current.position.x = -(base + leafW) - open * leafW * 1.0;
    if (right1.current) right1.current.position.x = base + open * leafW * 1.6;
    if (right2.current) right2.current.position.x = base + leafW + open * leafW * 1.0;

    // gentle parallax from pointer for life
    const mx = (state.pointer.x || 0) * 0.15;
    const my = (state.pointer.y || 0) * 0.1;
    if (group.current) {
      group.current.rotation.y += (mx - group.current.rotation.y) * 0.05;
      group.current.rotation.x += (-my - group.current.rotation.x) * 0.05;
    }

    // god-rays brighten as the door opens (light floods in)
    if (rays.current && rays.current.material.uniforms) {
      rays.current.material.uniforms.uIntensity.value = 0.05 + open * 0.5;
      rays.current.material.uniforms.uTime.value = state.clock.elapsedTime;
    }
  });

  // volumetric light cone (cheap additive plane stack behind the opening)
  const rayMat = useMemo(
    () =>
      new THREE.ShaderMaterial({
        transparent: true,
        depthWrite: false,
        blending: THREE.AdditiveBlending,
        uniforms: { uTime: { value: 0 }, uColor: { value: new THREE.Color('#f6e6c4') }, uIntensity: { value: 0.05 } },
        vertexShader: /* glsl */ `
          varying vec2 vUv;
          void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }
        `,
        fragmentShader: /* glsl */ `
          varying vec2 vUv; uniform float uTime; uniform vec3 uColor; uniform float uIntensity;
          void main(){
            // soft vertical shafts, fading at edges
            float shaft = smoothstep(0.0, 0.5, vUv.y) * (1.0 - smoothstep(0.5, 1.0, vUv.y));
            float x = abs(vUv.x - 0.5);
            float beam = smoothstep(0.5, 0.0, x);
            float flick = 0.92 + 0.08 * sin(uTime * 0.8 + vUv.x * 10.0);
            float a = shaft * beam * flick * uIntensity;
            gl_FragColor = vec4(uColor, a);
          }
        `,
      }),
    []
  );

  return (
    <group ref={group} position={[0, 0, 0]}>
      {/* procedural Cape Town vista (Table Mountain + Lion's Head), warms as door opens */}
      <Vista revealRef={progressRef} />

      {/* god-rays through the opening */}
      <mesh ref={rays} position={[0, 0, -1.4]} scale={[5.5, 6, 1]} material={rayMat}>
        <planeGeometry args={[1, 1]} />
      </mesh>

      {/* aluminium head + sill track */}
      <mesh position={[0, 2.25, 0.1]}>
        <boxGeometry args={[8.4, 0.18, 0.34]} />
        <meshStandardMaterial color="#b9bdbf" metalness={0.95} roughness={0.3} />
      </mesh>
      <mesh position={[0, -2.25, 0.1]}>
        <boxGeometry args={[8.4, 0.18, 0.34]} />
        <meshStandardMaterial color="#9fa3a5" metalness={0.95} roughness={0.4} />
      </mesh>

      {/* four stacking leaves */}
      <group ref={left2}><Leaf width={leafW} glassMat={glassMat} /></group>
      <group ref={left1}><Leaf width={leafW} glassMat={glassMat} /></group>
      <group ref={right1}><Leaf width={leafW} glassMat={glassMat} /></group>
      <group ref={right2}><Leaf width={leafW} glassMat={glassMat} /></group>
    </group>
  );
}
