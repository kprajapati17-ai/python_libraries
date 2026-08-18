import pandas as pd

customer_data1 = {
    "customer_id": [101, 102, 103, 104, 105],
    "name": ["Rahul", "Priya", "Amit", "Neha", "Karan"],
    "city": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Navsari"]
}

customer_data2 = {
    "customer_id": [106, 107, 108, 109],
    "name": ["kp", "Pk", "Ap", "Np"],
    "city": ["amc", "Smc", "bmc", "nvs"]
}
df1 = pd.DataFrame(customer_data1)
df2 = pd.DataFrame(customer_data2)

conte = pd.concat([df1,df2],axis=0,ignore_index=True)

print(conte)