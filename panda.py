print("Names Column:")
print(df['Name'])
print()



df['Result'] = ['Pass' if m >= 40 else 'Fail' for m in df['Marks']]
print("DataFrame after adding 'Result' column:")
print(df)
print()
print(df.describe())
print()