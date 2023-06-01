import { Sequelize } from "sequelize";
import path from "path";

export const ROOT_DIR = path.dirname(__dirname);

const DATABASE = {
  developement: {
    dialet: "sqlite",
    storage: ROOT_DIR + "/db.sqlite",
  },
  test: {
    dialet: "sqlite",
    storage: ROOT_DIR + "/test.sqlite",
  },
  production: {
    dialet: "sqlite",
    storage: ROOT_DIR + "/prod.sqlite",
  },
};

const env = process.env.NODE_ENV || "development";

const dbConfig = DATABASE[env];

export const sequelize = new Sequelize("sqlite-db", "user", "pass", {
  dialect: "sqlite",
  host: ROOT_DIR + "/db.sqlite",
});
