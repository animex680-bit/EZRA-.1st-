import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// Deployed under GitHub Pages subpath /EZRA-.1st-/alucape/
export default defineConfig({
  base: '/EZRA-.1st-/alucape/',
  plugins: [react()],
  build: {
    outDir: 'dist',
    assetsInlineLimit: 0,
  },
});
