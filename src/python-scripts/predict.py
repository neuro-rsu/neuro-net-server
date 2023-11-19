from ITSAS import ITSASModel
import sys

test = ITSASModel.load('.\\src\\models\\my_model.pkl')

df = test.predict(n = sys.argv[1])

out = df.to_json(orient="columns")

with open('data.json', 'w') as f:
    f.write(out)

print("Ok!")