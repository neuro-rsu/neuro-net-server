from ITSAS import ITSASModel
import sys

test = ITSASModel.load('.\\src\\models\\my_model.pkl')

df = test.predict(n = sys.argv[1])

print(df)