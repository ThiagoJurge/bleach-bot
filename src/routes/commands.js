import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

// Necessário no ESM para resolver __dirname
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const commandsPath = path.join(__dirname, '../../commands.json');
const commands = JSON.parse(fs.readFileSync(commandsPath, 'utf-8'));

export default async function commandRoute(client) {
    client.on('message', async (msg) => {
        if (!msg.body.startsWith('/')) return;

        const inputCommand = msg.body.slice(1).toLowerCase();

        // Agrupar comandos por categoria (guardando os objetos dos comandos)
        const categorias = {};
        for (const cmd of commands) {
            if (!cmd.command) continue;

            const categoria = cmd.categoria?.toLowerCase() || 'outros';
            if (!categorias[categoria]) categorias[categoria] = [];

            categorias[categoria].push(cmd);
        }

        // /menu: mostra lista dos comandos agrupados por categoria (só títulos)
        if (inputCommand === 'menu') {
            let menu = '*_░ി❁⭝ Comandos*\n\n';
            for (const cat in categorias) {
                const formattedCat = cat.charAt(0).toUpperCase() + cat.slice(1);
                const listCommands = categorias[cat]
                    .map(c => `- /${c.command}${c.title ? ` - ${c.title}` : ''}`)
                    .join('\n');
                menu += `▚ׁ̣۬❏̷̸ⷢ♔͎┄  ${formattedCat}\n${listCommands}\n\n`;
            }
            await msg.reply(menu.trim());
            return;
        }

        // Se for uma categoria, enviar cada response separadamente, sem cabeçalho
        if (categorias[inputCommand]) {
            const formattedCat = inputCommand.charAt(0).toUpperCase() + inputCommand.slice(1);

            for (const cmd of categorias[inputCommand]) {
                if (cmd.response && cmd.response.trim()) {
                    await msg.reply(cmd.response);
                }
            }
            return;
        }

        // Se for um comando individual
        const found = commands.find(cmd => cmd.command.toLowerCase() === inputCommand);
        if (found && found.response) {
            await msg.reply(found.response);
        }
    });
}
