import supabase from "../utils/supabaseClient.js"

let comandos = [] // cache em memória
let categorias = {} // cache agrupado por categoria

// Carregar comandos do Supabase e organizar
async function carregarComandos() {
    const { data, error } = await supabase.from('comandos').select()

    if (error) {
        console.error('Erro ao carregar comandos do Supabase:', error)
        return
    }

    comandos = data || []

    // Agrupar por categoria
    categorias = {}
    for (const cmd of comandos) {
        if (!cmd.command) continue

        const categoria = cmd.categoria?.toLowerCase() || 'outros'
        if (!categorias[categoria]) categorias[categoria] = []

        categorias[categoria].push(cmd)
    }

    console.log(`✅ ${comandos.length} comandos carregados do Supabase.`)
}

await carregarComandos()

// Opcional: recarregar cache a cada 10 min
setInterval(carregarComandos, 10 * 60 * 1000)

export default async function commandRoute(client) {
    client.on('message', async (msg) => {
        if (!msg.body.startsWith('/')) return

        const inputCommand = msg.body.slice(1).toLowerCase()

        // /menu: mostra lista dos comandos agrupados por categoria (só títulos)
        if (inputCommand === 'menu') {
            let menu = '*_░ി❁⭝ Comandos*\n\n'
            for (const cat in categorias) {
                const formattedCat = cat.charAt(0).toUpperCase() + cat.slice(1)
                const listCommands = categorias[cat]
                    .map(c => `- /${c.command}${c.title ? ` - ${c.title}` : ''}`)
                    .join('\n')
                menu += `▚ׁ̣۬❏̷̸ⷢ♔͎┄  ${formattedCat}\n${listCommands}\n\n`
            }
            await msg.reply(menu.trim())
            return
        }

        // Se for uma categoria, enviar cada response separadamente
        if (categorias[inputCommand]) {
            for (const cmd of categorias[inputCommand]) {
                if (cmd.response && cmd.response.trim()) {
                    await msg.reply(cmd.response)
                }
            }
            return
        }

        // Se for um comando individual
        const found = comandos.find(cmd => cmd.command.toLowerCase() === inputCommand)
        if (found && found.response) {
            await msg.reply(found.response)
        }
    })
}
