// ecosystem.config.js
module.exports = {
    apps: [
      {
        name: 'bleach-bot',
        script: './src/server.js',
        env: {
          NODE_ENV: 'production',
          // Ajuste seu PATH aqui pra incluir o Node e o Chromium corretos no WSL
          PATH: '/home/tjurge/.nvm/versions/node/v22.16.0/bin:/usr/bin:' + process.env.PATH,
          PUPPETEER_EXECUTABLE_PATH: '/usr/bin/chromium-browser',
        },
        // Para garantir que o pm2 mantenha o app vivo
        autorestart: true,
        watch: false,
        max_restarts: 10,
      },
    ],
  };
  