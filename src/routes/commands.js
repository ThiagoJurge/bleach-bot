import gerarMenu from "../utils/menu.js";
import supabase from "../utils/supabaseClient.js";

const GRUPO_FICHAS = "120363419581121169@g.us";

// Permissões por grupo
function grupoAutorizado(command, categoria, chatId) {
  if (categoria === "geral" && chatId === GRUPO_FICHAS) return false;
  if (categoria === "geral") return true;
  if (command) return true;
  return chatId === GRUPO_FICHAS;
}

export default function commandRoute(client) {
  client.on("message", async (msg) => {
    const chatId = msg.from;
    if (!msg.body.startsWith("/")) return;

    const inputCommand = msg.body.slice(1).toLowerCase();

    // Buscar comandos
    const { data: comandos, error } = await supabase.from("comandos").select();
    if (error) {
      console.error("Erro ao carregar comandos:", error);
      return;
    }

    // Localiza o comando digitado
    const found = comandos.find(cmd => cmd.command?.toLowerCase() === inputCommand);
    const categoria = found?.categoria?.toLowerCase();

    if (!grupoAutorizado(inputCommand, categoria, chatId)) return;

    // /menu: mostra comandos filtrando categorias conforme o grupo
    if (inputCommand === "menu") {
      try {
        const menu = await gerarMenu(chatId, comandos, {
          excluirCategorias: chatId === GRUPO_FICHAS ? ["geral"] : [],
        });
        await msg.reply(menu);
      } catch (err) {
        console.error("Erro ao gerar/enviar menu:", err);
      }
      return;
    }

    // /<categoria>: retorna todos os comandos da categoria
    const categoriasUnicas = [
      ...new Set(comandos.map(c => c.categoria?.toLowerCase() || "outros"))
    ];

    if (categoriasUnicas.includes(inputCommand)) {
      const comandosDaCategoria = comandos.filter(
        c => (c.categoria?.toLowerCase() || "outros") === inputCommand
      );
      for (const cmd of comandosDaCategoria) {
        if (cmd.response?.trim()) {
          try {
            await msg.reply(cmd.response);
          } catch (err) {
            console.error(err);
          }
        }
      }
      return;
    }

    // /<comando individual>
    if (found?.response?.trim()) {
      try {
        await msg.reply(found.response);
      } catch (err) {
        console.error("Erro ao enviar resposta:", err);
      }
    }
  });
}
