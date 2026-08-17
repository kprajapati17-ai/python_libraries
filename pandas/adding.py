import pandas as pd

data = {
    "name": ["Rahul", "Priya", "Amit", "Neha", "Karan", "Riya", "Vivek", "Anjali", "Rohit", "Pooja"],
    "age": [25, 28, 24, 30, 27, 26, 32, 29, 31, 23],
    "salary": [35000, 45000, 32000, 55000, 42000, 38000, 60000, 48000, 52000, 30000],
    "performancescore": [82, 91, 75, 88, 79, 85, 95, 89, 84, 72]
}

df = pd.DataFrame(data)
print(df)
print("-"*120)

df["bonus"] = df["salary"]*0.1
print(df)
print("-"*120)

df.insert(0,"empid",[11,22,33,44,55,66,77,88,99,100])
print(df)
print("-"*120)