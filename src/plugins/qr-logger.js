import qrcode from "qrcode-terminal";

export default async function qrLogger(client) {
  client.on("qr", (qr) => {
    qrcode.generate(qr, { small: true });
  });
}
