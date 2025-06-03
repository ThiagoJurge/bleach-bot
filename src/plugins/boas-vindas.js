import gerarMenu from "../utils/menu.js";
import supabase from "../utils/supabaseClient.js";

export default function boasVindas(client) {
  client.on("group_join", async (notification) => {
    const GRUPO_FICHAS = "120363419581121169@g.us";
    const group = await notification.getChat();
    const number = notification.id?.participant;

    if (group.id._serialized === GRUPO_FICHAS) {
      try {
        const privateChat = await client.getChatById(number);

        // Envia mensagem de boas-vindas no privado
        await privateChat.sendMessage(
          `Opa! Seja bem-vindo (a) ao Bleach After Dead!\nVou te mandar o menu de sistemas pra dar uma olhadinha.\nCaso tenha alguma dúvida, pode consultar a administração.\nObs.: Os comandos abaixo você só vai conseguir utilizar no grupo de fichas.`
        );

        // Buscar comandos do Supabase
        const { data: comandos, error } = await supabase
          .from("comandos")
          .select();
        if (error) {
          console.error("Erro ao carregar comandos do Supabase:", error);
          return;
        }

        // Gera e envia o menu
        const menu = await gerarMenu(group.id._serialized, comandos, {
          excluirCategorias: ["geral"],
        });
        await privateChat.sendMessage(menu);
      } catch (error) {
        console.log(
          `❌ Erro ao enviar mensagem de boas-vindas para ${number}: ${error.message}`
        );
      }
    }
  });
}
