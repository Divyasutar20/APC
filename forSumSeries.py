import math
n = int(input("Enter Number of terms:"))
total = 0
for i in range(n + 1):
    total += 1 / math.factorial(i)
    print("Sum of the series:" ,total)