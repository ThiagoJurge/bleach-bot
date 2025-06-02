import Whatsapp from 'whatsapp-web.js'
import qrcode from 'qrcode-terminal';
import { logger } from './utils/logger.js';
const { Client, LocalAuth } = Whatsapp


export class App {
  constructor() {
    this.client = new Client({
      authStrategy: new LocalAuth(),
      headless: true,
      args: ['--no-sandbox'],
      executablePath: process.env.PUPPETEER_EXECUTABLE_PATH,
        });
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
