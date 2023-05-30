import {
  DestroyOptions,
  FindOptions,
  Identifier,
  NonNullFindOptions,
} from "sequelize/types/model";
import { CulturePractise } from "../models";
import { Optional } from "sequelize";

export default class CulturePractiseService {
  static async getAll(options?: FindOptions<any>) {
    return await CulturePractise.findAll(options);
  }

  static async findOne(options: NonNullFindOptions<any>) {
    return await CulturePractise.findOne(options);
  }

  static async findById(
    id: Identifier,
    options?: Omit<NonNullFindOptions<any>, "where">
  ) {
    return await CulturePractise.findByPk(id, options);
  }

  static async create(data: Optional<any, string>, options?: any) {
    return await CulturePractise.create(data, options);
  }

  static async delete(options: DestroyOptions<any>) {
    return await CulturePractise.destroy(options);
  }

  static async deleteById(id: number) {
    return (await CulturePractise.findOne({ where: { id } })).destroy();
  }
}
