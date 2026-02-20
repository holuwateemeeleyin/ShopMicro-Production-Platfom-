import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],

  server: {
    allowedHosts: true, // This tells Vite to accept any host (e.g., AWS URLs)
    host: true,         // Ensures it listens on all network interfaces
    port: 5173,
  },
})