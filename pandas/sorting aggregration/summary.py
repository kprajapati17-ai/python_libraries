import pandas as pd

data = {
    "name": ["Rahul", None, "Amit", "Neha", None, "Riya", "Vivek", "Anjali", "Rohit", "Pooja"],
    "age": [25, None, 24, 30, 27, 26, 32, 29, 31, 23],
    "salary": [35000, None, 82000, 55000, 42000, 38000, 60000, 48000, 52000, 30000],
    "performancescore": [82, None, 75, 88, 79, 85, 95, 89, 84, 72]
}

df = pd.DataFrame(data)

print(df)

avg_salary = df["salary"].mean()
print("average salary",avg_salary)

min_salary = df["salary"].min()
print("min salary",min_salary)

max_salary = df["salary"].max()
print("max salary",max_salary)