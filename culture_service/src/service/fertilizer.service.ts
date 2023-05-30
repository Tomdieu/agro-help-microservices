import {
  DestroyOptions,
  FindOptions,
  Identifier,
  NonNullFindOptions,
  Optional,
} from "sequelize";
import { Fertilizer } from "../models";

export default class FertilizerService {
  static async getAll(options?: FindOptions<any>) {
    return await Fertilizer.findAll(options);
  }
  static async findOne(options: NonNullFindOptions<any>) {
    return await Fertilizer.findOne(options);
  }
  static async findById(
    id: Identifier,
    options?: Omit<NonNullFindOptions<any>, "where">
  ) {
    return await Fertilizer.findByPk(id, options);
  }
  static async create(data: Optional<any, string>, option?: any) {
    return await Fertilizer.create(data, option);
  }
  static async delete(option: DestroyOptions<any>) {
    return await Fertilizer.destroy(option);
  }
  static async deleteById(id: number) {
    return (await Fertilizer.findOne({ where: { id } })).destroy();
  }
}
