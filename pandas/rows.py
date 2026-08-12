import pandas as pd

df = pd.read_json("sample_Data.json")

print("1st 10 rows")
print(df.head(10))

print("\nlast 10 rows")
print(df.tail(10))