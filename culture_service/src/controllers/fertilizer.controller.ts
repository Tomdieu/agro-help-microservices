import { Request, Response } from "express";
import { status } from "../status";
import FertilizerService from "../service/fertilizer.service";
import { Culture, CultureFertilizer, Fertilizer } from "../models";
import CultureService from "../service/culture.service";

export const listFertilizer = async (req: Request, res: Response) => {
  res.status(status.HTTP_OK).send(
    await FertilizerService.getAll({
      include: [{ model: Culture, as: "cultures" }],
    })
  );
};
export const createFertilizer = async (req: Request, res: Response) => {
  const { name, composition, description, type } = req.body;
  const createdFertilizer = await FertilizerService.create({
    name,
    composition,
    description,
    type,
  });
  res.status(status.HTTP_CREATED).json(createdFertilizer);
};
export const getFertilizer = async (req: Request, res: Response) => {
  const { id } = req.params;
  const fertlizer = await FertilizerService.findById(id, {
    include: [
      {
        model: Culture,
        as: "cultures",
      },
    ],
    rejectOnEmpty: false,
  });
  if (fertlizer) {
    res.status(status.HTTP_OK).send(fertlizer);
  } else {
    res.status(status.HTTP_NOT_FOUND).send({ message: "Not Found" });
  }
};
export const updateFertilizer = async (req: Request, res: Response) => {
  const { id } = req.params;
  const { name, composition, description, type } = req.body;
  const fertlizer = await FertilizerService.findById(id);

  if (fertlizer) {
    if (name) {
      fertlizer.name = name;
    }
    if (composition) {
      fertlizer.composition = composition;
    }
    if (description) {
      fertlizer.description = description;
    }
    if (type) {
      fertlizer.type = type;
    }
    res.status(status.HTTP_OK).send(await fertlizer.save());
  } else {
    res
      .status(status.HTTP_NOT_FOUND)
      .send({ message: `Fertilizer ${id} not found!` });
  }
};
export const deleteFertilizer = async (req: Request, res: Response) => {
  const { id } = req.params;
  const fertlizer = await FertilizerService.findById(id);
  if (fertlizer) {
    await fertlizer.destroy();
    res.status(status.HTTP_NO_CONTENT).send({ message: "Deleted" });
  } else {
    res
      .status(status.HTTP_NOT_FOUND)
      .send({ message: `Fertilizer ${id} not found!` });
  }
};

export const addCultureToFertlizer = async (req: Request, res: Response) => {
  const { id, cultureId } = req.params;
  const fertlizer = await FertilizerService.findById(id);
  const culture = await CultureService.findById(cultureId);

  if (culture && fertlizer) {
    const data = {
      fertilizer_id: fertlizer.id,
      culture_id: culture.id,
    };

    await CultureFertilizer.create(data);

    var fertilizer = await Fertilizer.findByPk(id, {
      include: [
        {
          model: Culture,
          as: "cultures",
          attributes: { exclude: ["CultureFertilizer"] },
          duplicating: false,
        },
      ],
    });

    res.status(status.HTTP_CREATED).send(fertilizer);
  } else {
    res.status(status.HTTP_OK).send({
      message: "Not Found",
    });
  }
};
