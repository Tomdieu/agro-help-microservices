import { sequelize } from "../config/db";
import { Model, DataTypes, Optional } from "sequelize";

interface FertilizerAttributes {
  name: string;
  composition: string;
  description: string;
  type: string;
  id?: number;
}

interface FerilizerCreationAttributes
  extends Optional<FertilizerAttributes, "id"> {}

class Fertilizer
  extends Model<FertilizerAttributes, FerilizerCreationAttributes>
  implements FertilizerAttributes
{
  public name!: string;
  public composition!: string;
  public description!: string;
  public type!: string;
  public id!: number;
}

Fertilizer.init(
  {
    name: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    composition: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    description: {
      type: DataTypes.TEXT,
      allowNull: false,
    },
    type: {
      type: DataTypes.ENUM("organic", "chemical"),
      allowNull: false,
    },
  },
  {
    sequelize,
    createdAt: "created_at",
    updatedAt: "updated_at",
    tableName: "fertilizer",
  }
);

export default Fertilizer;
