n = int(input("How many number"))
i = 1
largest = None

while i <= n:
    num = int(input(f"Enter Number {i}: "))
    if largest is None or num > largest:
        largest = num
    i += 1
print("Largest number is:" , largest)