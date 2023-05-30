import { checkSchema } from "express-validator";
import { Culture, CulturePractise } from "../models";

export const createCulturePractiseSchema = checkSchema({
  culture_id: {
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
  name: {
    notEmpty: true,
    isString: true,
    errorMessage: "Culture Practise name require!",
    custom: {
      options: async (value: string) => {
        if (value) {
          const culturePractise = await CulturePractise.findOne({
            where: { name: value.toLowerCase() },
          });
          if (culturePractise) {
            return Promise.reject(
              `Culture Practise with this name already exists!`
            );
          }
        }
      },
    },
  },
  practise: {
    notEmpty: true,
    errorMessage: "Culture Practise method is require!",
  },
});
