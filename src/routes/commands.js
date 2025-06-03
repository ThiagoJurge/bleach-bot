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
    const body = msg.body.trim();

    // Somente processa mensagens que começam com "/" ou "#"
    if (!body.startsWith("/") && !body.startsWith("#")) return;

    // Buscar todos os comandos no Supabase
    const { data: comandos, error } = await supabase.from("comandos").select();
    if (error) {
      console.error("Erro ao carregar comandos:", error);
      return;
    }

    // --- 1) Monta a estrutura de categorias para gerar códigos ##########

    // Categorias agrupadas (igual ao gerarMenu)
    const categorias = {};
    for (const cmd of comandos) {
      if (!cmd.command) continue;
      const catLower = (cmd.categoria?.toLowerCase() || "outros");
      if (!categorias[catLower]) categorias[catLower] = [];
      categorias[catLower].push(cmd);
    }

    // Mapa de #CÓDIGOS para o nome do comando real
    const codigosMap = {}; // ex: { "#H001": "resurreccion", ... }
    for (const cat in categorias) {
      const lista = categorias[cat];
      const inicial = cat.charAt(0).toUpperCase();
      lista.forEach((cmd, idx) => {
        // índice + 1 e zero padding de 3 dígitos
        const numero = String(idx + 1).padStart(3, "0");
        const codigo = `#${inicial}${numero}`; 
        // armazena o *command* (sem barra) para lookup
        codigosMap[codigo] = cmd.command.toLowerCase();
      });
    }

    // ---------------------------------------------------------------------

    // 2) Se começou com "#" => interpretar código curto
    if (body.startsWith("#")) {
      const codigoDigitado = body.toUpperCase(); // ex: "#H002"
      const cmdPraExecutar = codigosMap[codigoDigitado];

      if (cmdPraExecutar) {
        // Encontrou o comando associado
        const found = comandos.find(
          (c) => c.command?.toLowerCase() === cmdPraExecutar
        );
        const categoria = found?.categoria?.toLowerCase();

        if (!grupoAutorizado(cmdPraExecutar, categoria, chatId)) return;
        if (found?.response?.trim()) {
          try {
            await msg.reply(found.response);
          } catch (err) {
            console.error("Erro ao enviar resposta via código curto:", err);
          }
        }
      }

      return;
    }

    // 3) Mensagem começa com "/": parseia o comando normal
    const inputCommand = body.slice(1).toLowerCase(); // sem a "/"

    // Localiza o comando digitado (se for comando individual)
    const found = comandos.find(
      (cmd) => cmd.command?.toLowerCase() === inputCommand
    );
    const categoria = found?.categoria?.toLowerCase();

    if (!grupoAutorizado(inputCommand, categoria, chatId)) return;

    // 4) Se for "/menu": gera e envia o menu
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

    // 5) Se for "/<categoria>": devolve todas as respostas daquela categoria
    const categoriasUnicas = [
      ...new Set(comandos.map((c) => c.categoria?.toLowerCase() || "outros")),
    ];

    if (categoriasUnicas.includes(inputCommand)) {
      const comandosDaCategoria = comandos.filter(
        (c) => (c.categoria?.toLowerCase() || "outros") === inputCommand
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

    // 6) Se for "/<comando individual>": envia a resposta daquele comando
    if (found?.response?.trim()) {
      try {
        await msg.reply(found.response);
      } catch (err) {
        console.error("Erro ao enviar resposta:", err);
      }
    }
  });
}
