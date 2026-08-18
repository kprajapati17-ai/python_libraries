import pandas as pd

data ={
    "time":[1,2,3,4,5],
    "value":[1,None,5,None,10]    

}

df = pd.DataFrame(data)

print(df)

print("after interpolation")

df["value"]=df["value"].interpolate(method="linear")

print(df)