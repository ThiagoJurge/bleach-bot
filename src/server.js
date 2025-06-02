import { App } from './app.js';
import boasVindas from './plugins/boas-vindas.js';
import clientInit from './plugins/client-init.js';
import qrLogger from './plugins/qr-logger.js';
import addCommandRoute from './routes/addCommand.js';
import commandsRoute from './routes/commands.js';
import pingRoute from './routes/ping.js';

const app = new App();

app.register(clientInit);
app.register(qrLogger);
app.register(boasVindas);
app.register(pingRoute);
app.register(commandsRoute)
app.register(addCommandRoute)

app.start();
