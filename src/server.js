import { App } from './app.js';
import qrLogger from './plugins/qr-logger.js';
import pingRoute from './routes/ping.js';

const app = new App();

app.register(qrLogger);
app.register(pingRoute);

app.start();
