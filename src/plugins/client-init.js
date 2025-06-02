export default function clientInit(client) {
  // Quando o cliente estiver pronto
  client.on("ready", () => {
    console.log("✅ Cliente do WhatsApp pronto!");
  });

  // Autenticado com sucesso
  client.on("authenticated", () => {
    console.log("🔐 Cliente autenticado com sucesso.");
  });

  // Erro de autenticação
  client.on("auth_failure", (msg) => {
    console.error("❌ Falha na autenticação:", msg);
  });

  // Desconectado
  client.on("disconnected", (reason) => {
    console.warn("🔌 Cliente desconectado. Motivo:", reason);
  });

  // Mensagem recebida (opcional)
  client.on("message", async (message) => {
    const chat = await message.getChat();
    const contact = await message.getContact();

    const senderNumber = contact.number; // Número sem @c.us
    const senderName = contact.pushname || contact.name || "Desconhecido";
    const isGroup = chat.isGroup;

    let chatName = isGroup ? chat.name : senderName;

    console.log(
      `📨 ${chatName} - ${senderName} (${senderNumber}): 💬 ${message.body}`
    );
  });
}
