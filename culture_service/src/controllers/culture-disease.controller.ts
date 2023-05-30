import { Request, Response } from "express";
import { status } from "../status";
import CultureDiseaseService from "../service/culture-disease.service";
import { Culture } from "../models";

export const listCultureDisease = async (req: Request, res: Response) => {
  res
    .status(status.HTTP_OK)
    .json(
      (await CultureDiseaseService.getAll({ include: [{ model: Culture }] })) ||
        {}
    );
};

export const createCultureDisease = async (req: Request, res: Response) => {
  const { culture_id, disease_name, solution } = req.body;
  const createdCulture = await CultureDiseaseService.create({
    culture_id,
    disease_name,
    solution,
  });
  return res.status(status.HTTP_CREATED).send(createdCulture);
};
export const getCultureDisease = async (req: Request, res: Response) => {
  const { id } = req.params;
  res.status(status.HTTP_OK).send(
    (await CultureDiseaseService.findById(id, {
      include: [{ model: Culture }],
      rejectOnEmpty: false,
    })) || {}
  );
};
export const updateCultureDisease = async (req: Request, res: Response) => {
  const { id } = req.params;
  const { disease_name, solution } = req.body;

  const cultureDiseaseToUpdate = await CultureDiseaseService.findById(id);
  if (cultureDiseaseToUpdate) {
    if (disease_name) {
      cultureDiseaseToUpdate.disease_name = disease_name;
    }
    if (solution) {
      cultureDiseaseToUpdate.solution = solution;
    }
    res.status(status.HTTP_OK).send(await cultureDiseaseToUpdate.save());
  } else {
    res.status(status.HTTP_NOT_FOUND).send({ message: "Not Found" });
  }
};

export const deleteCultureDisease = async (req: Request, res: Response) => {
  const { id } = req.params;
  await CultureDiseaseService.delete({ where: { id } });
  res.status(status.HTTP_NO_CONTENT).send({ message: "Deleted" });
};
