import { checkSchema } from "express-validator";
import { Op } from "sequelize";
import { Request } from "express";
import { CulturePractise } from "../models";

export const updateCulturePractiseSchema = checkSchema({
  id: {
    notEmpty: true,
    isInt: true,
    errorMessage: "Culture Practise Id Require",
    custom: {
      options: async (id: number) => {
        if (id) {
          const culturePractise = await CulturePractise.findOne({
            where: { id },
          });
          if (!culturePractise) {
            return Promise.reject(`Culture Practise with id ${id} not found`);
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
      options: async (value: string, { req }) => {
        if (value) {
          const { id } = req.query;
          const culturePractise = await CulturePractise.findOne({
            where: { name: value.toLowerCase(), culture_id: { [Op.ne]: id } },
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
  practise: {},
});
