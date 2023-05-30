import { checkSchema } from "express-validator";
import { Culture, CultureDiseaseAdvice } from "../models";

export const createCultureDiseaseAdviceSchema = checkSchema({
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
  disease_name: {
    notEmpty: true,
    isString: true,
    errorMessage: "disease name require!",
    custom: {
      options: async (value: string) => {
        if (value) {
          const cultureDiseaseAdvice = await CultureDiseaseAdvice.findOne({
            where: { name: value.toLowerCase() },
          });
          if (cultureDiseaseAdvice) {
            return Promise.reject(
              `disease name with this name already exists!`
            );
          }
        }
      },
    },
  },
  solution: {
    notEmpty: true,
    errorMessage: "Solution require!",
  },
});
