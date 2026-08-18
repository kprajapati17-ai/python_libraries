import pandas as pd

data = {
    "name": ["Rahul", "Amit", "Neha", "Riya", "Vivek", "Anjali", "Rohit", "Pooja"],
    "age": [25, 27, 30, 25, 27, 32,30, 25],
    "salary": [35000, 82000, 55000, 42000, 38000, 60000, 52000, 30000],
    "performancescore": [75, 88, 79, 85, 95, 89, 84, 72]
}

df = pd.DataFrame(data)

group = df.groupby("age")["salary"].sum()

print(group)


group2 = df.groupby(["age","name","performancescore"])["salary"].sum()

print(group2)