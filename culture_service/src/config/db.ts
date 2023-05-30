import { Sequelize } from "sequelize";
import path from "path";

export const ROOT_DIR = path.dirname(__dirname);

export const sequelize = new Sequelize("sqlite-db", "user", "pass", {
  dialect: "sqlite",
  host: ROOT_DIR + "/db.sqlite",
});
