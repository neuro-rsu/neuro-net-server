import type { Express, Router, Request, Response, NextFunction} from 'express'

import express from 'express'

// import neuralDataService from './neural-data.service.mjs'

import neuralDataController from './neural-data.controller.mjs'

const router: Router = express.Router()

// router.use(async (req: Request, res: Response, next: NextFunction) => {
//   neuralDataService.checkMethod(req)
//       .then (() => next())
//       .catch(next)
// })

router
  .route('/')
  //.get(loginController.getLogin)
  .post(neuralDataController.getNeuralData)
//.put(LoginController.updateLogin)
//.delete(LoginController.deleteLogin)

router.use(function(err: any, req: Request, res: Response, next: NextFunction) {
  res.status(err.status || 500)
  .send(err);
});

export default router