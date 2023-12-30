import sys
from ITSAS import ITSASModel
import logging

# logging.getLogger("lightning")
# logging.disable()
# logging.getLogger("pytorch_lightning")
# logging.disable()

sys.stderr = open('error_log.txt', 'w')

test = ITSASModel.load('src\python-scripts\models\my_model.pkl')

df = test.predict(n = int(sys.argv[1]))

# # Преобразование TimeSeries в DataFrame
df = df.pd_dataframe()

# # Преобразование DataFrame в JSON
out = df.to_json()

# sys.stdout = open('out_log.txt', 'w')

# from darts.logging import get_logger, raise_if_not

# logging.getLogger(__name__).setLevel(logging.INFO)
# logger = get_logger(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
logger.addHandler(handler)
logger.info(out)