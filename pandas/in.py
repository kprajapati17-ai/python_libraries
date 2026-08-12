import pandas as pd

df = pd.read_json("sample_Data.json")
data ={
    "name":["kp","jp","rp"],
    "age":[20,30,40],
    "city":["nvs","vapi","patan"]
}
df2 = pd.DataFrame(data)
print("display info of data")
print(df.info())
print(df2.info())