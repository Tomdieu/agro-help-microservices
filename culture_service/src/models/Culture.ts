import { sequelize } from "../config/db";
import { Model, DataTypes, Optional } from "sequelize";

import { sendData } from "../producer";
import {
  MEDIA_ROOT,
  getServerAddress,
  getServerPort,
  getServerProtocole,
} from "../config";
import fs from "fs";

interface CultureAttributes {
  id?: number;
  name: string;
  image: string;
}

interface CultureCreationAttributes extends Optional<CultureAttributes, "id"> {}

class Culture
  extends Model<CultureAttributes, CultureCreationAttributes>
  implements CultureAttributes
{
  public id!: number;
  public name!: string;
  public image!: string;

  public readonly created_at!: Date;
  public readonly updated_at!: Date;

  public get imageUrl(): string {
    const mediaFolder = "media";
    const address = getServerAddress();
    const port = getServerPort();
    const protocole = getServerProtocole();
    const url = `${protocole}://${address}:${port}/${mediaFolder}`;
    return this.image.split(".").length > 1 ? `${url}/${this.image}` : null;
  }
}

Culture.init(
  {
    name: {
      type: DataTypes.STRING,
      allowNull: false,
      unique: true,
    },
    image: {
      type: DataTypes.STRING,
      allowNull: true,
    },
  },
  {
    sequelize,
    tableName: "culture",
    createdAt: "created_at",
    updatedAt: "updated_at",
  }
);

// Culture.addHook("beforeCreate",(culture)=>{
//   culture.name = culture.name.toLowerCase()

// })

Culture.addHook("afterCreate", (culture) => {
  const message = {
    type: "culture_created",
    data: culture.toJSON(),
  };

  sendData(["soil", "parcel"], message);
});

Culture.addHook("afterUpdate", (culture) => {
  const message = {
    type: "culture_updated",
    data: culture.toJSON(),
  };

  sendData(["soil", "parcel"], message);
});

Culture.addHook("afterDestroy", (culture: Culture) => {
  const message = {
    type: "culture_deleted",
    data: { id: culture.id },
  };

  const filePath = `${MEDIA_ROOT}/${culture.image}`;
  // Check if the file exists
  if (fs.existsSync(filePath)) {
    // Delete the file
    fs.unlinkSync(filePath);
  }

  sendData(["soil", "parcel"], message);
});

export default Culture;
