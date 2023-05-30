import { checkSchema } from "express-validator";
import { Fertilizer } from "../models";

export const createFertilizerSchema = checkSchema({
  name: {
    notEmpty: true,
    isString: true,
    errorMessage: "Fertilizer name require!",
    custom: {
      options: async (value: string) => {
        if (value) {
          const fertilizer = await Fertilizer.findOne({
            where: { name: value.toLowerCase() },
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
    errorMessage: "Fertilizer composition require!",
  },
  description: {
    notEmpty: true,
    errorMessage: "Fertilizer description require!",
  },
  type: {
    notEmpty: true,
    errorMessage: "Fertilizer type require!",
  },
});
