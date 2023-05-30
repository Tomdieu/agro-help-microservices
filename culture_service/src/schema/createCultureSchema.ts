import { checkSchema } from "express-validator";
import { Culture } from "../models";

export const createCultureSchema = checkSchema({
  culture_name: {
    isString: true,
    errorMessage: "culture name require!",
    custom: {
      options: async (value: string) => {
        if (value) {
          const culture = await Culture.findOne({
            where: { name: value.toLowerCase() },
          });
          if (culture) {
            return Promise.reject(`culture with this name already exists!`);
          }
        }
      },
    },
  },
});
