import { sequelize } from "../config/db";
import { Model, DataTypes } from "sequelize";

import Soil from "./Soil";
import Culture from "./Culture";

class SoilCulture extends Model {}

SoilCulture.init(
  {},
  {
    sequelize,
    tableName: "soil_culture",
  }
);

Soil.belongsToMany(Culture, {
  through: SoilCulture,
  as: "cultures",
  foreignKey: "culture_id",
});
Culture.belongsToMany(Soil, {
  through: SoilCulture,
  as: "soils",
  foreignKey: "soil_id",
});

export default SoilCulture;
