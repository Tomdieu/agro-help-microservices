import express, { Router } from "express";
import {
  createCulturePractise,
  deleteCulturePractise,
  getCulturePractise,
  listCulturePractise,
  updateCulturePractise,
} from "../controllers/culture-practise.controller";
import {
  createCulturePractiseSchema,
  getCulturePractiseSchema,
  updateCulturePractiseSchema,
  validate,
} from "../schema";

const router = Router();
router.use(express.json());
router.use(express.urlencoded({ extended: true }));

/**
 * Culture Practise
 * @typedef {object} CulturePractise
 * @property {integer} id - Culture practise id
 * @property {string} name - The Culture Practise name
 * @property {string} practise - The Culture Practise steps
 * @property {Culture} culture - Culture associated to the practise
 */

/**
 * Culture Practise
 * @typedef {object} CulturePractiseCreate
 * @property {integer} culture_id.required - The culture id
 * @property {string} name.required - The Culture Practise name
 * @property {string} practise.required - The Culture Practise steps
 */

/**
 * GET /api/culture-practise/
 * @tags Culture Practise
 * @returns {array<CulturePractise>} 200 - success
 * @summary List all the culture practise
 */
router.get("/", listCulturePractise);
/**
 * POST /api/culture-practise/
 * @tags Culture Practise
 * @summary Create a culture practise
 * @param {CulturePractiseCreate} request.body.required
 * @returns {CulturePractise} 200 - Success response
 * @returns {object} 400 -  Bad Request response
 */
router.post("/", validate(createCulturePractiseSchema), createCulturePractise);
/**
 * GET /api/culture-practise/{id}/
 * @tags Culture Practise
 * @summary Get a culture Practise
 * @param {int} id.path.required A unique integer value identifying this  Culture Practise
 * @returns {CulturePractise} 200 - Success response
 * @returns {object} 400 -  Bad Request response
 */
router.get("/:id/", validate(getCulturePractiseSchema), getCulturePractise);
/**
 * PUT /api/culture-practise/{id}/
 * @tags Culture Practise
 * @summary update a culture practise
 * @param {int} id.path.required A unique integer value identifying this  Culture Practise
 * @param {CulturePractiseCreate} request.body.required
 * @returns {CulturePractise} 200 - Success response
 * @returns {object} 400 -  Bad Request response
 */
router.put(
  "/:id/",
  validate(updateCulturePractiseSchema),
  updateCulturePractise
);
/**
 * PATCH /api/culture-practise/{id}/
 * @tags Culture Practise
 * @summary update a culture practise
 * @param {int} id.path.required A unique integer value identifying this  Culture Practise
 * @param {CulturePractiseCreate} request.body.required
 * @returns {CulturePractise} 200 - Success response
 * @returns {object} 400 -  Bad Request response
 */
router.patch(
  "/:id/",
  validate(updateCulturePractiseSchema),
  updateCulturePractise
);
/**
 * DELETE /api/culture-practise/{id}/
 * @tags Culture Practise
 * @summary Delete a culture practise
 * @param {int} id.path.required A unique integer value identifying this  Culture Practise
 * @returns {CulturePractise} 200 - Success response
 * @returns {object} 400 -  Bad Request response
 */
router.delete(
  "/:id/",
  validate(getCulturePractiseSchema),
  deleteCulturePractise
);

let culturePractiseRouter = router;

export default culturePractiseRouter;
