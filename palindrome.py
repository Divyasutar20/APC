num  = int(input("Enter a number "))
orig = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if orig == rev:
    print("it is palindrome")
else:
    print("it is not palindrome")