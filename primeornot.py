num = int (input("Enter a number : "))
i = 2
isprime= True
if num <= 1:
    is_prime = False
else:
    while i < num:
          if num % i == 0:
                isprime = False
        break
    i += 1
if isprime:
    print("prime")
else:
    print("not prime")
