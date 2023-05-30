import { checkSchema } from "express-validator";
import { CulturePractise } from "../models";

export const getCulturePractiseSchema = checkSchema({
  id: {
    isInt: true,
    notEmpty: true,
    errorMessage: "CulturePractise Id Require",
    custom: {
      options: async (id: number) => {
        if (id) {
          const culturePractise = await CulturePractise.findOne({
            where: { id },
          });
          if (!culturePractise) {
            return Promise.reject(`CulturePractise with id ${id} not found`);
          }
        }
      },
    },
  },
});
