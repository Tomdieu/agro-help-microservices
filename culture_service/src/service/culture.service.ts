import {
  DestroyOptions,
  FindOptions,
  Identifier,
  NonNullFindOptions,
  Optional,
} from "sequelize";
import Culture from "../models/Culture";

class CultureService {
  static async getAll(options?: FindOptions<any>) {
    return await Culture.findAll(options);
  }
  static async findById(
    id: Identifier,
    options?: Omit<NonNullFindOptions<any>, "where">
  ) {
    return await Culture.findByPk(id, options);
  }

  static async create(data: Optional<any, string>, options?: any) {
    return await Culture.create(data, options);
  }

  static async delete(options: DestroyOptions<any>) {
    return await Culture.destroy(options);
  }
  static async deleteById(id: number) {
    return (await Culture.findByPk(id)).destroy();
  }
}

export default CultureService;
