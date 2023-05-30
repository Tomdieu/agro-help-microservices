import { sequelize } from "../config/db";
import { Model } from "sequelize";
import Culture from "./Culture";
import Fertilizer from "./Fertilizer";

class CultureFertilizer extends Model {}

CultureFertilizer.init(
  {},
  { sequelize, timestamps: false, tableName: "culture_fertilizer" }
);

Fertilizer.belongsToMany(Culture, {
  through: CultureFertilizer,
  foreignKey: "fertilizer_id",
  as: "cultures",
});
Culture.belongsToMany(Fertilizer, {
  through: CultureFertilizer,
  foreignKey: "culture_id",
  as: "fertilizers",
});

export default CultureFertilizer;
