import { Request, Response } from "express";
import { status } from "../status";
import CulturePractiseService from "../service/culture-practise.service";
import { Culture } from "../models";

export const listCulturePractise = async (req: Request, res: Response) => {
  res
    .status(status.HTTP_OK)
    .json(
      await CulturePractiseService.getAll({ include: [{ model: Culture }] })
    );
};
export const createCulturePractise = async (req: Request, res: Response) => {
  const { name, practise, culture_id } = req.body;
  const culturePractise = await CulturePractiseService.create({
    name,
    practise,
    culture_id,
  });
  res.status(status.HTTP_CREATED).json(culturePractise);
};
export const getCulturePractise = async (req: Request, res: Response) => {
  const { id } = req.params;
  res
    .status(status.HTTP_OK)
    .json((await CulturePractiseService.findById(id)) || {});
};
export const updateCulturePractise = async (req: Request, res: Response) => {
  const { id } = req.params;
  const { name, practise } = req.body;
  const culturePractiseToUpdate = await CulturePractiseService.findById(id);
  if (culturePractiseToUpdate) {
    if (name) {
      culturePractiseToUpdate.name = name;
    }
    if (practise) {
      culturePractiseToUpdate.practise = practise;
    }

    res.status(status.HTTP_ACCEPTED).json(await culturePractiseToUpdate.save());
  } else {
    res.status(status.HTTP_NOT_FOUND).send({ message: "Not Found" });
  }
};
export const deleteCulturePractise = async (req: Request, res: Response) => {
  const { id } = req.params;
  await CulturePractiseService.delete({ where: { id } });
  res.status(status.HTTP_NO_CONTENT).send({ message: `Deleted` });
};
