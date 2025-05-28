import readline from 'readline'
import commandRoute from './src/routes/commands.js'
import addCommandRoute from './src/routes/addCommand.js'

// Mock de client com .on('message')
const mockClient = {
    on(event, handler) {
        if (event === 'message') {
            // Interface de linha de comando
            const rl = readline.createInterface({
                input: process.stdin,
                output: process.stdout
            })

            console.log('🤖 Bot de testes iniciado. Digite um comando (ex: /menu, /funcionamento):\n')

            rl.on('line', async (input) => {
                const trimmed = input.trim()
                if (!trimmed) return

                const msg = {
                    body: trimmed,
                    reply: async (resposta) => {
                        console.log('\n📩 RESPOSTA DO BOT:\n' + resposta + '\n')
                    }
                }

                try {
                    await handler(msg)
                } catch (err) {
                    console.error('Erro ao processar comando:', err)
                }
            })
        }
    }
}

// Inicializa a função do bot com o mock
await addCommandRoute(mockClient)
