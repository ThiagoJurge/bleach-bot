import { writeFile, mkdir } from 'fs/promises';
import { dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));

const files = {
    'src/app.js': `
import { Client } from 'whatsapp-web.js';
import qrcode from 'qrcode-terminal';
import { logger } from './utils/logger.js';

export class App {
  constructor() {
    this.client = new Client();
    this.plugins = [];
  }

  register(plugin) {
    this.plugins.push(plugin);
  }

  async start() {
    for (const plugin of this.plugins) {
      await plugin(this.client);
    }

    this.client.initialize();
  }
}
`.trim(),

    'src/server.js': `
import { App } from './app.js';
import qrLogger from './plugins/qr-logger.js';
import pingRoute from './routes/ping.js';

const app = new App();

app.register(qrLogger);
app.register(pingRoute);

app.start();
`.trim(),

    'src/plugins/qr-logger.js': `
import qrcode from 'qrcode-terminal';

export default async function qrLogger(client) {
  client.on('qr', (qr) => {
    qrcode.generate(qr, { small: true });
  });

  client.on('ready', () => {
    console.log('✅ Client is ready');
  });
}
`.trim(),

    'src/routes/ping.js': `
import { PingController } from '../controllers/ping.controller.js';

export default async function pingRoute(client) {
  const controller = new PingController();

  client.on('message', async (msg) => {
    if (msg.body === '!ping') {
      await controller.handle(msg);
    }
  });
}
`.trim(),

    'src/controllers/ping.controller.js': `
export class PingController {
  async handle(msg) {
    await msg.reply('pong 🏓');
  }
}
`.trim(),

    'src/utils/logger.js': `
export const logger = {
  log: (...args) => console.log('[LOG]', ...args),
  error: (...args) => console.error('[ERROR]', ...args),
};
`.trim(),

    'package.json': `
{
  "name": "wweb-fastify-arch",
  "type": "module",
  "version": "1.0.0",
  "main": "src/server.js",
  "scripts": {
    "start": "node src/server.js"
  },
  "dependencies": {
    "qrcode-terminal": "^0.12.0",
    "whatsapp-web.js": "^1.23.0"
  }
}
`.trim(),

    '.gitignore': `
node_modules
.session
`.trim(),
};

async function createFiles() {
    for (const [filePath, content] of Object.entries(files)) {
        const fullPath = `${__dirname}/${filePath}`;
        const folder = dirname(fullPath);

        await mkdir(folder, { recursive: true });
        await writeFile(fullPath, content + '\n');
        console.log('✅ Created:', filePath);
    }
}

createFiles()
    .then(() => console.log('\n🚀 Projeto criado! Rode:\n\nnpm install\nnpm start\n'))
    .catch((err) => console.error('❌ Erro:', err));
