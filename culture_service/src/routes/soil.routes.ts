import { Router } from "express";
import { listSoil, getASoil } from "../controllers/soil.controller";

const router = Router();

/**
 * Soil
 * @typedef {object} Soil
 * @property {string} type -  The soil type
 * @property {string} description - The soil description
 * @property {array<string>} composition - The Soil compositions
 * @property {array<Culture>} cultures - The Culture associated to a soil
 *
 */

/**
 * GET /api/soil/
 * @tags Soil
 * @return {array<Soil>} 200 - Success response application/json
 * @return {object} 400 - Bad request response
 * @summary List all the soils
 */

router.get("/", listSoil);

/**
 * GET /api/soil/{id}/
 * @tags Soil
 * @param {int} id.path.required
 * @return {Soil} 200 - Success
 * @returns {object} 404 - Not Found
 * @summary Get a soil
 */
router.get("/:id/", getASoil);

let soilRouter = router;
export default soilRouter;
