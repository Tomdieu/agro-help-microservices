import { checkSchema } from "express-validator";
import { Op } from "sequelize";
import { Request } from "express";
import { Culture } from "../models";

export const updateCultureSchema = checkSchema({
  id: {
    notEmpty: true,
    isInt: true,
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
    errorMessage: "culture name require!",
    custom: {
      options: async (value: string, { req }) => {
        if (value) {
          const { id } = req.query;
          const culture = await Culture.findOne({
            where: { name: value.toLowerCase(), id: { [Op.ne]: id } },
          });
          if (culture) {
            return Promise.reject(`culture with this name already exists!`);
          }
        }
      },
    },
  },
});
