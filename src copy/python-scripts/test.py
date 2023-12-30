from ITSAS import ITSASModel
import sys
from torch.multiprocessing import set_start_method
try:
     set_start_method('spawn')
except RuntimeError:
    pass
import logging
logging.getLogger("pytorch_lightning").setLevel(logging.ERROR)

sys.stderr = open('error_log.txt', 'w')

test = ITSASModel.load('models\my_model.pkl')

df = test.predict(n = int(sys.argv[1]))

# Преобразование TimeSeries в DataFrame для удобства
df = df.pd_dataframe()

# Преобразование DataFrame в JSON
out = df.to_json(orient="records")

print(out)