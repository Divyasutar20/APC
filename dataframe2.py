import pandas as pd

data = {
    'Name': ['Divya', 'Ravi', 'Sneha', 'Amit'],
    'Age': [21, 23, 22, 20],
    'Marks': [85, 90, 78, 88],
    'City': ['Pune', 'Mumbai', 'Nashik', 'Nagpur']
}

myvar = pd.DataFrame(data)

print(myvar)
print()

print(myvar['Name'])
print()

print("Students with Marks > 80:")
print(myvar[myvar['Marks'] > 80])
print()

print(myvar.describe())
print()