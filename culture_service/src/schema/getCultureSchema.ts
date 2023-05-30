import { checkSchema } from "express-validator";
import { Culture } from "../models";

export const getCultureSchema = checkSchema({
  id: {
    isInt: true,
    notEmpty: true,
    errorMessage: "Culture Id Require",
    custom: {
      options: async (id: number) => {
        if (id) {
          const culture = await Culture.findOne({ where: { id } });
          if (!culture) {
            return Promise.reject(`Culture with id ${id} not found`);
          }
        }
      },
    },
  },
});
