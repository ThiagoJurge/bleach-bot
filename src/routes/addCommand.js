import supabase from '../utils/supabaseClient.js';

async function carregarCategorias() {
    const { data, error } = await supabase.from('comandos').select('categoria');

    if (error) {
        console.error('Erro ao carregar categorias:', error);
        return [];
    }

    const categoriasSet = new Set();
    data.forEach(item => {
        if (item.categoria) categoriasSet.add(item.categoria.toLowerCase());
    });

    return Array.from(categoriasSet);
}

function formatarCategorias(categorias = []) {
    return categorias
        .map((cat, i) => `${i + 1}. ${cat.charAt(0).toUpperCase() + cat.slice(1)}`)
        .join('\n');
}

export default async function addCommandRoute(client) {
    // Estado da conversa por chat (map de chatId -> estado)
    const conversas = new Map();

    client.on('message', async (msg) => {
        const chatId = msg.from;

        if (!msg.body.startsWith('/addcommand')) {
            // Se não está em modo addcommand, não processa aqui
            if (!conversas.has(chatId)) return;
        }

        // Cancelar a qualquer momento
        if (msg.body.toLowerCase() === '/cancel') {
            conversas.delete(chatId);
            await msg.reply('🚫 Criação do comando cancelada.');
            return;
        }

        // Se iniciou o comando
        if (msg.body.toLowerCase() === '/addcommand' && !conversas.has(chatId)) {
            conversas.set(chatId, { etapa: 'command' });
            await msg.reply('Vamos criar um novo comando!\n\nDigite o comando (ex: funcionamento):\n\nDigite /cancel para cancelar a qualquer momento.');
            return;
        }

        // Continuar fluxo da conversa
        const estado = conversas.get(chatId);

        if (!estado) return; // nada a fazer

        try {
            switch (estado.etapa) {
                case 'command':
                    {
                        const input = msg.body.trim().toLowerCase();
                        if (!input) {
                            await msg.reply('Comando inválido. Digite novamente o comando (ex: funcionamento):');
                            return;
                        }
                        estado.command = input;
                        estado.etapa = 'title';
                        await msg.reply('Título do comando:');
                    }
                    break;

                case 'title':
                    {
                        const input = msg.body.trim();
                        if (!input) {
                            await msg.reply('Título inválido. Digite novamente o título do comando:');
                            return;
                        }
                        estado.title = input;
                        estado.etapa = 'categoria';

                        // Carregar categorias do banco
                        const categorias = await carregarCategorias();
                        estado.categoriasExistentes = categorias;

                        const textoCategorias = categorias.length
                            ? 'Categorias existentes:\n' + formatarCategorias(categorias) + '\n\nDigite o número da categoria ou digite uma nova categoria:'
                            : 'Nenhuma categoria encontrada. Digite o nome da categoria para o comando:';

                        await msg.reply(textoCategorias);
                    }
                    break;

                case 'categoria':
                    {
                        const input = msg.body.trim();
                        if (!input) {
                            await msg.reply('Categoria inválida. Digite o número da categoria ou o nome da nova categoria:');
                            return;
                        }

                        let categoriaFinal = input;

                        if (estado.categoriasExistentes && estado.categoriasExistentes.length > 0) {
                            const num = parseInt(input, 10);
                            if (!isNaN(num) && num >= 1 && num <= estado.categoriasExistentes.length) {
                                categoriaFinal = estado.categoriasExistentes[num - 1];
                            }
                        }

                        estado.categoria = categoriaFinal.toLowerCase();
                        estado.etapa = 'response';

                        await msg.reply('Digite a resposta do comando:');
                    }
                    break;

                case 'response':
                    {
                        const input = msg.body.trim();
                        if (!input) {
                            await msg.reply('Resposta inválida. Digite a resposta do comando:');
                            return;
                        }
                        estado.response = input;

                        // Inserir no banco
                        const { data, error } = await supabase.from('comandos').insert([
                            {
                                command: estado.command,
                                title: estado.title,
                                categoria: estado.categoria,
                                response: estado.response,
                            },
                        ]);

                        if (error) {
                            console.error('Erro ao inserir comando:', error);
                            await msg.reply('❌ Erro ao criar comando, tente novamente mais tarde.');
                        } else {
                            await msg.reply(`✅ Comando /${estado.command} criado com sucesso!`);
                        }

                        // Finaliza conversa
                        conversas.delete(chatId);
                    }
                    break;

                default:
                    conversas.delete(chatId);
                    await msg.reply('Erro no fluxo de criação do comando. Por favor, tente novamente.');
            }
        } catch (err) {
            console.error('Erro no addCommandRoute:', err);
            conversas.delete(chatId);
            await msg.reply('❌ Ocorreu um erro. Cancelando criação do comando.');
        }
    });
}
