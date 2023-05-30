import { checkSchema } from "express-validator";
import { Fertilizer } from "../models";

export const getFertilizerSchema = checkSchema({
  id: {
    isInt: true,
    notEmpty: true,
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
});
