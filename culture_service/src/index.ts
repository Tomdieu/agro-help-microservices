require("dotenv").config();
import express, { Request, Response } from "express";
import http from "http";
import { sequelize } from "./config/db";
import cors from "cors";
import { log } from "console";
import { MEDIA_ROOT, setServerConfig, setServerProtocole } from "./config";

import logger from "./config/logger";
import routes from "./routes";
import * as Models from "./models";
import SetupDocs from "./config/docs";
import { connectQueue } from "./consumer";
import { AddressInfo } from "./types";
import { IP6to4 } from "./utils/ipv6to4";

(async () => {
  sequelize
    .sync({ logging: false })
    .then(() => {
      (async () => {})();

      console.log("db ready".bold);
    })
    .catch((err) => {
      log(err);
    });
})();

const app = express();
const httpServer = http.createServer(app);
app.set("trust proxy", true);

app.use("/media", express.static(MEDIA_ROOT));
app.use(cors());

const PORT = process.env.PORT || 5000;

app.use(logger);
app.use(function (req, res, next) {
  const protocole = req.protocol;
  setServerProtocole(protocole);
  return next();
});

app.get("/", async (req: Request, res: Response) => {});
app.use("/api", routes);

SetupDocs(app);

connectQueue();

const server = httpServer.listen(PORT, () => {
  console.log(`Server running at http://127.0.0.1:${PORT}`);
});

const stringData = JSON.stringify(server.address());
const jsonData: AddressInfo = JSON.parse(stringData);

setServerConfig(IP6to4(jsonData.address), jsonData.port);

console.log(`App running at ${IP6to4(jsonData.address)}:${jsonData.port}`);

export default server;
