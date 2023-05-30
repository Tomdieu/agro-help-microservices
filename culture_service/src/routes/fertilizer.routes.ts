import express, { Router } from "express";
import {
  listFertilizer,
  createFertilizer,
  getFertilizer,
  updateFertilizer,
  deleteFertilizer,
  addCultureToFertlizer,
} from "../controllers/fertilizer.controller";

const router = Router();

router.use(express.json());
router.use(express.urlencoded({ extended: true }));

/**
 * Fertilizer
 * @typedef {object} Fertilizer
 * @property {number} id
 * @property {string} name - fertilizer name
 * @property {string} composition - fertilizer composition
 * @property {string} description - fertilizer description
 * @property {string} type - fertilizer type
 * @property {string} cultures - cultues for that fertilizer
 */

/**
 * Fertilizer
 * @typedef {object} FertilizerWNC
 * @property {number} id
 * @property {string} name - fertilizer name
 * @property {string} composition - fertilizer composition
 * @property {string} description - fertilizer description
 * @property {string} type - fertilizer type
 */

/**
 * Fertilizer
 * @typedef {object} FertilizerCreate
 * @property {string} name - fertilizer name
 * @property {string} composition - fertilizer composition
 * @property {string} description - fertilizer description
 * @property {string} type - fertilizer type
 */

/**
 * GET /api/fertilizer/
 * @summary list all the fertilizer
 * @returns {array<Fertilizer>} 200 - success
 * @tags Fertilizer
 */
router.get("/", listFertilizer);

/**
 * POST /api/fertilizer/
 * @param {FertilizerCreate} request.body.required
 * @returns {Fertilizer} 201 - Created
 * @tags Fertilizer
 * @summary create a fertilizer
 */
router.post("/", createFertilizer);

/**
 * GET /api/fertilizer/{id}/
 * @summary Get a fertilizer
 * @param {number} id.path.required A unique integer value identifying this  Fertilizer
 * @tags Fertilizer
 * @returns {Fertilizer} 200 - Success
 * @returns {object} 404 - Not Found
 */
router.get("/:id/", getFertilizer);

/**
 * PATCH /api/fertilizer/{id}/
 * @param {number} id.path.required A unique integer value identifying this  Fertilizer
 * @param {FertilizerCreate} request.body.required
 * @returns {Fertilizer} 200 - Success
 * @returns {object} 404 - Not Found
 * @tags Fertilizer
 * @summary Update a fertilizer
 */
router.patch("/:id/", updateFertilizer);
/**
 * PUT /api/fertilizer/{id}/
 * @param {number} id.path.required A unique integer value identifying this  Fertilizer
 * @param {FertilizerCreate} request.body.required
 * @returns {Fertilizer} 200 - Success
 * @returns {object} 404 - Not Found
 * @tags Fertilizer
 * @summary Update a fertilizer
 */
router.put("/:id/", updateFertilizer);

/**
 * DELETE /api/fertilizer/{id}/
 * @param {number} id.path.required A unique integer value identifying this  Fertilizer
 * @returns {object} 204 - No Content
 * @returns {object} 404 - Not Found
 * @tags Fertilizer
 * @summary Update a fertilizer
 */
router.delete("/:id/", deleteFertilizer);

/**
 * POST /api/fertilizer/{id}/add-culture/{cultureId}/
 * @summary Add a culture to fertilizer
 * @param {number} id.path.required A unique integer value identifying this  Fertilizer
 * @param {number} cultureId.path.required A unique integer value identifying a Culture
 * @tags Fertilizer
 * @returns {Fertilizer} 200 - Success
 * @returns {object} 404 - Not Found
 */

router.post("/:id/add-culture/:cultureId/", addCultureToFertlizer);

let fertilizerRouter = router;

export default fertilizerRouter;
