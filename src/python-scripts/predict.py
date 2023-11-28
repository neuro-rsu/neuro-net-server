from ITSAS import ITSASModel
import sys

sys.stderr = open('error_log.txt', 'w')

test = ITSASModel.load('src\python-scripts\models\my_model.pkl')

df = test.predict(n = int(sys.argv[1]))

# Преобразование TimeSeries в DataFrame
df = df.pd_dataframe()

# Преобразование DataFrame в JSON
out = df.to_json()

sys.stdout = open('out_log.txt', 'w')

print(out)