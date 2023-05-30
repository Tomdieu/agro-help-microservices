import { sequelize } from "../config/db";
import { Model, DataTypes } from "sequelize";
import Culture from "./Culture";

class CulturePractise extends Model {
  name: string;
  practise: string;
}

CulturePractise.init(
  {
    name: {
      type: DataTypes.STRING,
      validate: {
        is: {
          args: ["^[a-z]+$", "i"],
          msg: "Only characters are allowed!",
        },
      },
    },
    practise: {
      type: DataTypes.TEXT,
      allowNull: false,
    },
  },
  {
    sequelize,
    createdAt: "created_at",
    updatedAt: "updated_at",
    tableName: "culture_practise",
  }
);

Culture.hasMany(CulturePractise, { foreignKey: "culture_id" });
CulturePractise.belongsTo(Culture, { foreignKey: "culture_id" });

export default CulturePractise;
