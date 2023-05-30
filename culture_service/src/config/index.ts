import path from "path";
import { Request } from "express";
const PARENT_PATH = path.dirname(__dirname);

const MEDIA_ROOT = PARENT_PATH + "/media/";

import multer from "multer";

var storage = multer.diskStorage({
  destination: function (req: Request, file, cb) {
    cb(null, MEDIA_ROOT);
  },
  filename: function (req: Request, file, cb) {
    cb(
      null,
      file.fieldname + "-" + Date.now() + path.extname(file.originalname)
    );
  },
});

let serverAddress: string = null;
let serverPort: number = null;
let serverProtocol: string = null;

function setServerConfig(address: string, port: number) {
  serverAddress = address;
  serverPort = port;
}

function setServerProtocole(protocole: string) {
  serverProtocol = protocole;
}

function getServerProtocole() {
  return serverProtocol;
}

function getServerAddress() {
  return serverAddress;
}

function getServerPort() {
  return serverPort;
}

export {
  PARENT_PATH,
  MEDIA_ROOT,
  storage,
  setServerConfig,
  getServerAddress,
  getServerPort,
  setServerProtocole,
  getServerProtocole,
};
