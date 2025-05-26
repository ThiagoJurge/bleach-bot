export class PingController {
  async handle(msg) {
    await msg.reply('pong 🏓');
  }
}
