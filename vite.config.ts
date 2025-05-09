import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		port: 5173,
		proxy: {
			"/api/my": {
				target: process.env.OPSDEV_HOST,
				changeOrigin: true
			}
		}
	}
});
