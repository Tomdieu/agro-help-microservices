import {
  DestroyOptions,
  FindOptions,
  Identifier,
  NonNullFindOptions,
} from "sequelize/types/model";
import { CultureDiseaseAdvice } from "../models";
import { Optional } from "sequelize";

export default class CultureDiseaseService {
  static async getAll(options?: FindOptions<any>) {
    return await CultureDiseaseAdvice.findAll(options);
  }

  static async findById(
    id: Identifier,
    options?: Omit<NonNullFindOptions<any>, "where">
  ) {
    return await CultureDiseaseAdvice.findByPk(id, options);
  }

  static async create(data: Optional<any, string>, options?: any) {
    return await CultureDiseaseAdvice.create(data, options);
  }

  static async delete(options: DestroyOptions<any>) {
    return await CultureDiseaseAdvice.destroy(options);
  }

  static async deleteById(id: number) {
    return (await CultureDiseaseAdvice.findOne({ where: { id } })).destroy();
  }
}
