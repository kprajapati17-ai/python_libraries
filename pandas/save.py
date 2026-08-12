import pandas as pd
    
data ={
    "name":["kp","jp","rp"],
    "age":[20,30,40],
    "city":["nvs","vapi","patan"]
}
df = pd.DataFrame(data)

print(df)

df.to_csv("demo.csv",index=False)
df.to_excel("demo.xlsx",index=False)
df.to_json("demo.json",index=False)