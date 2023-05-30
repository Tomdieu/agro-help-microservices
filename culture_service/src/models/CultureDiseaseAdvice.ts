import { sequelize } from "../config/db";
import { DataTypes, Model } from "sequelize";
import Culture from "./Culture";

class CultureDiseaseAdvice extends Model {
  disease_name: string;
  solution: string;
}

CultureDiseaseAdvice.init(
  {
    disease_name: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    solution: {
      type: DataTypes.TEXT,
      allowNull: false,
    },
  },
  {
    sequelize,
    tableName: "culture_disease_advice",
    createdAt: "created_at",
    updatedAt: "updated_at",
  }
);

Culture.hasMany(CultureDiseaseAdvice, { foreignKey: "culture_id" });
CultureDiseaseAdvice.belongsTo(Culture, { foreignKey: "culture_id" });

export default CultureDiseaseAdvice;
