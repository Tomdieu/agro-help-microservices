import { sequelize } from "../config/db";

import { DataTypes, Model } from "sequelize";

class Soil extends Model {
  public id!: number;
  public type!: string;
  public description!: string;
  public composition!: string;
  public readonly created_at!: Date;
  public readonly updated_at!: Date;
}

Soil.init(
  {
    id: {
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true,
      autoIncrement: false,
    },
    type: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    description: {
      type: DataTypes.TEXT,
      allowNull: false,
    },
    composition: {
      type: DataTypes.STRING,
      allowNull: false,
    },
  },
  {
    sequelize,
    tableName: "soil",
    updatedAt: "updated_at",
    createdAt: "created_at",
  }
);

export default Soil;
