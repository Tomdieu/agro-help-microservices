import { Request, Response } from "express";
import { status } from "../status";
import SoilService from "../service/soil.service";
import { Culture } from "../models";

export const listSoil = async (req: Request, res: Response) => {
  res.status(status.HTTP_OK).send(
    await SoilService.getAll({
      include: [{ model: Culture, as: "cultures" }],
    })
  );
};

export const getASoil = async (req: Request, res: Response) => {
  const { id } = req.params;
  const culture = await SoilService.findById(id, {
    include: [{ model: Culture, as: "cultures" }],
    rejectOnEmpty: false,
  });
  if (culture) {
    res.status(status.HTTP_OK).send(culture);
  } else {
    res
      .status(status.HTTP_NOT_FOUND)
      .send({ message: `Soil with id ${id} not found!` });
  }
};
