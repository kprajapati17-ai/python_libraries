import pandas as pd

data = {
    "name": ["Rahul", None, "Amit", "Neha", None, "Riya", "Vivek", "Anjali", "Rohit", "Pooja"],
    "age": [25, None, 24, 30, 27, 26, 32, 29, 31, 23],
    "salary": [35000, None, 32000, 55000, 42000, 38000, 60000, 48000, 52000, 30000],
    "performancescore": [82, None, 75, 88, 79, 85, 95, 89, 84, 72]
}

df = pd.DataFrame(data)

df["name"] = df["name"].fillna("Unknown")
df["age"] = df["age"].fillna(df["age"].median())
df["salary"] = df["salary"].fillna(df["salary"].median())
df["performancescore"] = df["performancescore"].fillna(df["performancescore"].median())

df["age"] = df["age"].astype(int)
df["salary"] = df["salary"].astype(int)
df["performancescore"] = df["performancescore"].astype(int)

df["performance_level"] = pd.cut(
    df["performancescore"],
    bins=[0, 60, 75, 90, 100],
    labels=["Poor", "Average", "Good", "Excellent"]
)

print(df)