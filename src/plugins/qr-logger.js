import express from 'express';
import qrcode from 'qrcode';

export default async function qrLogger(client) {
  const app = express();
  let qrImageData = '';

  client.on('qr', async (qr) => {
    qrImageData = await qrcode.toDataURL(qr);
    console.log('🖼️ QR code disponível em http://localhost:3000');
  });

  app.get('/', (req, res) => {
    if (!qrImageData) {
      return res.send('QR code não gerado ainda. Aguarde...');
    }

    res.send(`
      <h2>Escaneie o QR code com o WhatsApp:</h2>
      <img src="${qrImageData}" />
    `);
  });

  app.listen(3000, () => {
    console.log('🌐 Servidor de QR rodando em http://localhost:3000');
  });

  client.on('ready', () => {
    console.log('✅ Client is ready');
  });
}
