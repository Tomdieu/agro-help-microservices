import { checkSchema } from "express-validator";
import { Op } from "sequelize";
import { Fertilizer } from "../models";

export const updateFertilizerSchema = checkSchema({
  id: {
    notEmpty: true,
    isInt: true,
    errorMessage: "Fertilizer Id Require",
    custom: {
      options: async (id: number) => {
        if (id) {
          const fertilizer = await Fertilizer.findOne({ where: { id } });
          if (!fertilizer) {
            return Promise.reject(`Fertilizer with id ${id} not found`);
          }
        }
      },
    },
  },
  name: {
    notEmpty: true,
    isString: true,
    errorMessage: "Fertilizer name require!",
    custom: {
      options: async (value: string, { req }) => {
        if (value) {
          const { id } = req.query;
          const fertilizer = await Fertilizer.findOne({
            where: { name: value.toLowerCase(), id: { [Op.ne]: id } },
          });
          if (fertilizer) {
            return Promise.reject(`Fertilizer with this name already exists!`);
          }
        }
      },
    },
  },
  composition: {
    notEmpty: true,
    isString: true,
  },
  description: {
    notEmpty: true,
    isString: true,
  },
  type: {
    notEmpty: true,
    isString: true,
  },
});
