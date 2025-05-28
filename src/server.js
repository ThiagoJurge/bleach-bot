import { App } from './app.js';
import qrLogger from './plugins/qr-logger.js';
import addCommandRoute from './routes/addCommand.js';
import commandsRoute from './routes/commands.js';
import pingRoute from './routes/ping.js';

const app = new App();

app.register(qrLogger);
app.register(pingRoute);
app.register(commandsRoute)
app.register(addCommandRoute)

app.start();
