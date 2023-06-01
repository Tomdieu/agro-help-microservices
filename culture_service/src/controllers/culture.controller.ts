import { MEDIA_ROOT } from "../config";
import { Culture, Fertilizer } from "../models";
import Soil from "../models/Soil";
import serializeCulture from "../serializers/culture.serializer";
import CulturePractiseService from "../service/culture-practise.service";
import CultureService from "../service/culture.service";
import { status } from "../status";
import { Request, Response } from "express";
import fs from "fs";

/**
 * This controller is use to list all the cultures
 * @param req
 * @param res
 */
export const listCulture = async (req: Request, res: Response) => {
  const cultures = await CultureService.getAll({
    include: [{ model: Soil, as: "soils" }],
  });
  res.status(200).send(serializeCulture(cultures));
};

/**
 *This controller is to get a culture by it's id
 * @param req
 * @param res
 */
export const getCulture = async (req: Request, res: Response) => {
  const { id } = req.params;
  const culture = await CultureService.findById(id, {
    include: [{ model: Soil, as: "soils" }],
    rejectOnEmpty: false,
  });
  if (culture) {
    res.status(status.HTTP_OK).send(culture);
  } else {
    res
      .status(status.HTTP_BAD_REQUEST)
      .send({ message: `culture with id ${id} not found` });
  }
};

/**
 * This controller is use to create a culture
 * @param req
 * @param res
 */
export const createCulture = async (req: Request, res: Response) => {
  const { culture_name, description, category } = req.body;
  const image = req.file?.filename || "";
  const culture = await CultureService.create({
    name: culture_name.toLowerCase(),
    image,
    category,
    description,
  });
  res.status(status.HTTP_CREATED).send(culture);
};

/**
 * This controller is to update a culture
 * @param req
 * @param res
 */
export const updateCulture = async (req: Request, res: Response) => {
  const { id } = req.params;
  const { name } = req.body;
  const image = req.file?.filename || "";
  const cultureToUpdate = await CultureService.findById(id);
  if (cultureToUpdate) {
    if (name) {
      const filePath = `${MEDIA_ROOT}/${cultureToUpdate.image}`;

      cultureToUpdate.name = name;
      // Check if the file exists
      if (fs.existsSync(filePath)) {
        // Delete the file
        fs.unlinkSync(filePath);
      }
    }
    if (image) {
      cultureToUpdate.image = image;
    }

    const culture = await cultureToUpdate.save();
    res.status(status.HTTP_OK).send(culture);
  } else {
    res.status(status.HTTP_NOT_FOUND).send({ message: "Culture not found" });
  }
};

/**
 * This controller is use to delete a culture from it's id
 *
 * @param req
 * @param res
 */
export const deleteCulture = async (req: Request, res: Response) => {
  const { id } = req.params;
  const culture = await CultureService.findById(id, {
    include: [{ model: Soil, as: "soils" }],
    rejectOnEmpty: false,
  });
  if (!culture) {
    res.status(status.HTTP_NOT_FOUND).send({ message: "Culture not found" });
  }
  await CultureService.delete({ where: { id } });
  res.status(status.HTTP_NO_CONTENT).send({ message: `Deleted` });
};

export const getPractiseCulture = async (req: Request, res: Response) => {
  const { id } = req.params;
  const culture = await CulturePractiseService.findOne({
    include: [
      {
        model: Culture,
        where: {
          id,
        },
      },
    ],
    rejectOnEmpty: false,
  });
  if (culture) {
    res.status(status.HTTP_OK).send(culture);
  } else {
    res
      .status(status.HTTP_BAD_REQUEST)
      .send({ message: `culture with id ${id} not found` });
  }
};

export const getDiseaseCulture = async (req: Request, res: Response) => {
  const { id } = req.params;
  const culture = await CulturePractiseService.findOne({
    include: [
      {
        model: Culture,
        where: {
          id,
        },
      },
    ],
    rejectOnEmpty: false,
  });
  if (culture) {
    res.status(status.HTTP_OK).json(culture);
  } else {
    res
      .status(status.HTTP_BAD_REQUEST)
      .send({ message: `culture with id ${id} not found` });
  }
};

export const getFertilizer = async (req: Request, res: Response) => {
  const { id } = req.params;
  const cultures = await CultureService.findById(id, {
    include: [{ model: Fertilizer, as: "fertilizers" }],
    rejectOnEmpty: false,
  });

  if (cultures) {
    res.status(status.HTTP_OK).send(cultures);
  } else {
    res.status(status.HTTP_NOT_FOUND).send({ message: "Not Found" });
  }
};
