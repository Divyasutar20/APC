import pandas as pd
df=pd.read_csv("d:\\hello.csv")
ser=pd.series(df['Name'])
print(ser)
ser=pd.DataFrame(df['Name'],'Team','Number')
print(ser)