const express = require('express'), router = express.Router(), StartController = require('../controllers/start.controller'), StartService = require('../services/start.service');
router.use(async (req, res, next) => {
    const data = { x: 1, y: 1 };
    if (data) {
        req.start = data;
        next();
    }
    else
        return res
            .status(500)
            .send({ message: 'Error while getting users' });
});
router
    .route('/')
    .get(StartController.getStart);
module.exports = router;
//# sourceMappingURL=start.routes.js.map