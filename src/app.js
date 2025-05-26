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
