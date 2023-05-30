import { checkSchema } from "express-validator";
import { Op } from "sequelize";
import { Request } from "express";
import { CultureDiseaseAdvice } from "../models";

export const updateCultureDiseaseAdviceSchema = checkSchema({
  id: {
    notEmpty: true,
    isInt: true,
    errorMessage: "Culture Practise Id Require",
    custom: {
      options: async (id: number) => {
        if (id) {
          const cultureDiseaseAdvice = await CultureDiseaseAdvice.findOne({
            where: { id },
          });
          if (!cultureDiseaseAdvice) {
            return Promise.reject(`Culture Practise with id ${id} not found`);
          }
        }
      },
    },
  },
  disease_name: {
    custom: {
      options: async (value: string, { req }) => {
        if (value) {
          const { id } = req.query;
          const cultureDiseaseAdvice = await CultureDiseaseAdvice.findOne({
            where: {
              disease_name: value.toLowerCase(),
              culture_id: { [Op.ne]: id },
            },
          });
          if (cultureDiseaseAdvice) {
            return Promise.reject(
              `Culture Disease with this name already exists!`
            );
          }
        }
      },
    },
  },
  solution: {},
});
