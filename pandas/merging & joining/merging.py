import pandas as pd

customer_data = {
    "customer_id": [101, 102, 103, 104, 105],
    "name": ["Rahul", "Priya", "Amit", "Neha", "Karan"],
    "city": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Navsari"]
}

customer_df = pd.DataFrame(customer_data)

print(customer_df)

order_data = {
    "order_id": [1001, 1002, 1003, 1004, 1005, 1006],
    "customer_id": [101, 102, 101, 103, 105, 102],
    "product": ["Laptop", "Mobile", "Mouse", "Keyboard", "Monitor", "Headphone"],
    "amount": [55000, 25000, 800, 1500, 12000, 3000]
}

order_df = pd.DataFrame(order_data)

print(order_df)

mer = pd.merge(customer_df,order_df,on="customer_id",how="")
print(mer)