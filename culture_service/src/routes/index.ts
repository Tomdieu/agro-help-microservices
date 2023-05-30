import { Router } from "express";
import cultureRouter from "./culture.routes";
import soilRouter from "./soil.routes";
import culturePractiseRouter from "./culture-practise.routes";
import cultureDiseaseRouter from "./culture-disease.routes";
import fertilizerRouter from "./fertilizer.routes";

const router = Router();

router.use("/culture", cultureRouter);
router.use("/soil", soilRouter);
router.use("/culture-practise", culturePractiseRouter);
router.use("/culture-disease", cultureDiseaseRouter);
router.use("/fertilizer", fertilizerRouter);

export default router;
