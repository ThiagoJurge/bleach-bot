import qrcode from 'qrcode-terminal';

export default async function qrLogger(client) {
  client.on('qr', (qr) => {
    qrcode.generate(qr, { small: true });
  });

  client.on('ready', async () => {
    console.log('✅ Client is ready');
  });

  client.on('group_join', async (notification) => {
    const GRUPO_FICHAS = '120363419581121169@g.us';

    const group = await notification.getChat();
    const number = notification.id?.participant;

    if (group.id._serialized === GRUPO_FICHAS) {
      try {
        // Envia mensagem de boas-vindas
        await group.sendMessage(
          `Opa! Seja bem-vindo (a) ao Bleach After Dead!\nVou te mandar o menu de sistemas pra dar uma olhadinha.\nCaso tenha alguma dúvida, pode consultar a administração.`
        );

        // Gera o menu
        let menu = '*_░ി❁⭝ Comandos*\n\n';

        for (const cat in categorias) {
          // Pula a categoria "geral" se for o grupo de fichas
          if (group.id._serialized === GRUPO_FICHAS && cat.toLowerCase() === 'geral') continue;

          const listCommands = categorias[cat]
            .map(c => `- /${c.command}${c.title ? ` - ${c.title}` : ''}`)
            .join('\n');

          const formattedCat = cat.charAt(0).toUpperCase() + cat.slice(1);
          menu += `▚ׁ̣۬❏̷̸ⷢ♔͎┄  ${formattedCat}\n${listCommands}\n\n`;
        }

        await group.sendMessage(menu.trim()); // Manda o menu no grupo mesmo
      } catch (error) {
        console.log(`❌ Erro ao enviar mensagem de boas-vindas para ${number}: ${error.message}`);
      }
    }
  });
}
