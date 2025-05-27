import commands from '../../commands.json' assert { type: 'json' };

export default async function menuRoute(client) {
    client.on('message', async (msg) => {
        if (!msg.body.startsWith('/')) return;

        const inputCommand = msg.body.slice(1).toLowerCase();

        if (inputCommand === 'menu') {
            // Gera o menu com todos os comandos do JSON
            const menu = commands.map(cmd => {
                const title = cmd.title ? ` - ${cmd.title}` : '';
                return `/${cmd.command}${title}`;
            }).join('\n');

            await msg.reply(`📜 Comandos disponíveis:\n\n${menu}`);
            return;
        }

        const found = commands.find(cmd => cmd.command.toLowerCase() === inputCommand);

        if (found && found.response) {
            await msg.reply(found.response);
        }
    });
}
