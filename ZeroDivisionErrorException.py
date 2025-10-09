class ZeroDivisionError(Exception):
    pass

try:
    n = int(input("Enter a Number: "))
    res = 100 / n
  
except ZeroDivisionError:
    print("You Cannot Divide by Zero")
else:
    print("The Result is:",res)
finally:
    print("Execution Completed")