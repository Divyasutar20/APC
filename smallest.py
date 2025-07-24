n = int(input("How many number"))
i = 1
smallest = None

while i <= n:
    num = int(input(f"Enter Number {i}: "))
    if smallest is None or num < smallest:
       smallest = num
    i += 1
print("Smallest number is:" , smallest)