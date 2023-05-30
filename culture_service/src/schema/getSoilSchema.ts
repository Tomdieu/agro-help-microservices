import { checkSchema } from "express-validator";
import { Soil } from "../models";

export const getSoilSchema = checkSchema({
  id: {
    isInt: true,
    notEmpty: true,
    errorMessage: "Soil Id Require",
    custom: {
      options: async (id: number) => {
        if (id) {
          const soil = await Soil.findOne({ where: { id } });
          if (!soil) {
            return Promise.reject(`Soil with id ${id} not found`);
          }
        }
      },
    },
  },
});
