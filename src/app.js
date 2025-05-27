import Whatsapp from 'whatsapp-web.js'
import qrcode from 'qrcode-terminal';
import { logger } from './utils/logger.js';
const { Client, LocalAuth } = Whatsapp


export class App {
  constructor() {
    this.client = new Client({
      authStrategy: new LocalAuth(),  // <- Aqui
      puppeteer: {
        headless: true,
        args: ['--no-sandbox'], // necessário em ambientes restritos como Docker ou algumas VMs
      }
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
