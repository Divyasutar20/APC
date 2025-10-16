import pandas as pd
data={ "Calories":[420,380,390],
       "Duration":[50,40,45]}
myvar=pd.DataFrame(data)
print(myvar)
print(myvar.loc[0])
print(myvar.iloc[0])
print(myvar.loc[0,"Duration"])
print(myvar.iloc[0,0])
print(myvar.loc[:,["Duration","Calories"]])
print(myvar.iloc[:,[0,1]])
print(myvar.loc[0:1,"Duration"])
print(myvar.iloc[0:2,0])
print(myvar.loc[0:1])
print(myvar.iloc[0:2])
print(myvar.loc[myvar["Duration"]>40])
print()