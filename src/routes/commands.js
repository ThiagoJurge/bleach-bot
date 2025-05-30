import supabase from "../utils/supabaseClient.js"

// IDs dos grupos autorizados
const GRUPO_FICHAS = '120363419581121169@g.us'

//Grupo de testes
// const GRUPO_FICHAS = '120363402300515570@g.us'

// Função para verificar se o grupo tem permissão
function grupoAutorizado(command, categoria, chatId) {
    if (categoria === 'geral' && chatId === GRUPO_FICHAS) return false
    if (categoria === "geral") return true
    if (command) return true
    return chatId === GRUPO_FICHAS
}

export default function commandRoute(client) {
    client.on('message', async (msg) => {
        console.log(msg.body, msg.from, msg.author)
        const chatId = msg.from
        if (!msg.body.startsWith('/')) return
        const inputCommand = msg.body.slice(1).toLowerCase()

        // Buscar comandos do Supabase
        const { data: comandos, error } = await supabase.from('comandos').select()
        if (error) {
            console.error('Erro ao carregar comandos do Supabase:', error)
            return
        }

        // Agrupar comandos por categoria
        const categorias = {}
        for (const cmd of comandos) {
            if (!cmd.command) continue
            const categoria = cmd.categoria?.toLowerCase() || 'outros'
            if (!categorias[categoria]) categorias[categoria] = []
            categorias[categoria].push(cmd)
        }

        // Verificar permissões com base em comando e categoria
        const found = comandos.find(cmd => cmd.command.toLowerCase() === inputCommand)
        const categoria = found?.categoria?.toLowerCase()

        if (!grupoAutorizado(inputCommand, categoria, chatId)) {
            return
        }

        // /menu: mostra lista dos comandos, filtrando conforme o grupo
        if (inputCommand === 'menu') {
            let menu = '*_░ി❁⭝ Comandos*\n\n'

            for (const cat in categorias) {
                // Se for o grupo de fichas, pula a categoria "geral"
                if (chatId === GRUPO_FICHAS && cat.toLowerCase() === 'geral') continue

                const listCommands = categorias[cat]
                    .map(c => `- /${c.command}${c.title ? ` - ${c.title}` : ''}`)
                    .join('\n')

                const formattedCat = cat.charAt(0).toUpperCase() + cat.slice(1)
                menu += `▚ׁ̣۬❏̷̸ⷢ♔͎┄  ${formattedCat}\n${listCommands}\n\n`
            }
            try {
                await msg.reply(menu.trim())
            } catch (err) {
                console.error(err)
            }
            return
        }
        // Se for uma categoria, responder com todos os comandos da categoria
        if (categorias[inputCommand]) {
            for (const cmd of categorias[inputCommand]) {
                if (cmd.response && cmd.response.trim()) {
                    try {
                        await msg.reply(cmd.response)
                    } catch (err) {
                        console.error(err)
                    }
                }
            }
            return
        }

        // Se for um comando individual
        try {
            await msg.reply(found.response)
        } catch (err) {
            console.error('Erro ao enviar resposta:', err)

        }
    })
}
