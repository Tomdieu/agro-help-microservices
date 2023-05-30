import express, { Router } from "express";
import {
  createCultureDisease,
  listCultureDisease,
  getCultureDisease,
  updateCultureDisease,
  deleteCultureDisease,
} from "../controllers/culture-disease.controller";

const router = Router();
router.use(express.json());
router.use(express.urlencoded({ extended: true }));
/**
 * CultureDisease
 * @typedef {object} CultureDisease
 * @property {string} id
 * @property {string} disease_name - Culture Disease name
 * @property {string} solution - Culture Disease Solution
 * @property {Culture} cuture - Culture associated to that disease
 *
 */

/**
 * CultureDiseaseCreate
 * @typedef {object} CultureDiseaseCreate
 * @property {string} culture_id - Culture id
 * @property {string} disease_name - Culture Disease name
 * @property {string} solution - Culture Disease solution
 *
 */

/**
 * GET /api/culture-disease/
 * @summary Get all culture disease
 * @returns {array<CultureDisease>} 200 - Success
 * @tags Culture Disease
 *
 */

router.get("/", listCultureDisease);

/**
 * POST /api/culture-disease/
 * @summary Create a culture diseases
 * @param {CultureDiseaseCreate} request.body.required
 * @returns {CultureDisease} 200 - Success
 * @tags Culture Disease
 */
router.post("/", createCultureDisease);

/**
 * GET /api/culture-disease/{id}/
 * @summary Get a culture disease
 * @returns {CultureDisease}
 * @param {int} id.path.required A unique integer value identifying this  culture disease
 * @tags Culture Disease
 *
 */
router.get("/:id/", getCultureDisease);

/**
 * PUT /api/culture-disease/{id}/
 * @summary Update a culture disease
 * @param {int} id.path.required A unique integer value identifying this  culture disease
 * @param {CultureDisease} request.body.required
 * @returns {CultureDisease} 200 - Success
 * @returns {object} 404 - Bad Request
 * @tags Culture Disease
 */
router.put("/:id/", updateCultureDisease);

/**
 * PATCH /api/culture-disease/{id}/
 * @summary Update a culture disease
 * @param {int} id.path.required A unique integer value identifying this  culture disease
 * @param {CultureDisease} request.body.required
 * @returns {CultureDisease} 200 - Success
 * @returns {object} 404 - Bad Request
 * @tags Culture Disease
 */
router.patch("/:id/", updateCultureDisease);

/**
 * DELETE /api/culture-disease/
 * @summary Get all culture disease
 * @param {int} id.path.required A unique integer value identifying this  culture disease
 * @returns {object} 204 - success
 * @returns {object} 404 - Bad Request
 * @tags Culture Disease
 */
router.delete("/:id/", deleteCultureDisease);

let cultureDiseaseRouter = router;

export default cultureDiseaseRouter;
