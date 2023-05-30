require("dotenv").config();
import express, { Request, Response } from "express";
import http from "http";
import { sequelize } from "./config/db";
import cors from "cors";
import { log } from "console";
import {setServerConfig} from './config'

import logger from "./config/logger";
import routes from "./routes";
import * as Models from "./models";
import SetupDocs from "./config/docs";
import { connectQueue } from "./consumer";

import ip from 'ip-address';

const ipv6Address = server.address().address;

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
app.use(express.static("media"));
app.use(cors());

const PORT = process.env.PORT || 5000;

app.use(logger);

app.get("/", async (req: Request, res: Response) => {});
app.use("/api", routes);

SetupDocs(app);

connectQueue();

const server = httpServer.listen(PORT, () => {
  // const { address, port } = server.address();
  // config.s;
  console.log(`Server running at http://127.0.0.1:${PORT}`);
});

console.log(server.address().address);
