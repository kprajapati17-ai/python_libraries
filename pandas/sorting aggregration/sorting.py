import pandas as pd

data = {
    "name": ["Rahul", None, "Amit", "Neha", None, "Riya", "Vivek", "Anjali", "Rohit", "Pooja"],
    "age": [25, None, 24, 30, 27, 26, 32, 29, 31, 23],
    "salary": [35000, None, 32000, 55000, 42000, 38000, 60000, 48000, 52000, 30000],
    "performancescore": [82, None, 75, 88, 79, 85, 95, 89, 84, 72]
}

df = pd.DataFrame(data)

print(df)

df.sort_values(by="age",ascending=False,inplace=True)

print(df)