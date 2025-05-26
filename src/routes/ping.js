import { PingController } from '../controllers/ping.controller.js';

export default async function pingRoute(client) {
  const controller = new PingController();

  client.on('message', async (msg) => {
    if (msg.body === '!ping') {
      await controller.handle(msg);
    }
  });
}
