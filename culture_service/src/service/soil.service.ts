import {
  DestroyOptions,
  FindOptions,
  Identifier,
  NonNullFindOptions,
  Optional,
} from "sequelize";
import { Soil } from "../models";

export default class SoilService {
  static async getAll(options?: FindOptions<any>) {
    return await Soil.findAll(options);
  }

  static async findById(
    id: Identifier,
    options?: Omit<NonNullFindOptions<any>, "where">
  ) {
    return await Soil.findByPk(id, options);
  }

  static async create(data: Optional<any, string>, options: any) {
    return await Soil.create(data, options);
  }

  static async delete(options: DestroyOptions<any>) {
    return await Soil.destroy(options);
  }

  static async deleteById(id: number) {
    return (await Soil.findOne({ where: { id } })).destroy();
  }
}
