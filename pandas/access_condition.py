import pandas as pd

data = {
    "name": ["Rahul", "Priya", "Amit", "Neha", "Karan", "Riya", "Vivek", "Anjali", "Rohit", "Pooja"],
    "age": [25, 28, 24, 30, 27, 26, 32, 29, 31, 23],
    "salary": [35000, 45000, 32000, 55000, 42000, 38000, 60000, 48000, 52000, 30000],
    "performancescore": [82, 91, 75, 88, 79, 85, 95, 89, 84, 72]
}

df = pd.DataFrame(data)

# print(df)

# name = df["name"]
# print("single column return series")
# print(name)

# subset = df[["name","age"]]
# print()
# print("subset with name ,age")
# print(subset)

high_salary =df[df["salary"]>50000]
print("salary >50000")
print(high_salary)

#salary>50k and age>26

filterd =df[(df["salary"]>50000) & (df["age"]>26)]
print("salary>50k and age>26")
print(filterd)

filterd_or =df[(df["age"]>30) | (df["performancescore"]>90)]
print("performancescore>90 or age>30")
print(filterd_or)