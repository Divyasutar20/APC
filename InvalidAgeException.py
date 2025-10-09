class InvalidAgeException(Exception):
      pass
    
try:
    input_num = int(input("Enter Number: "))
    number = 18
    if input_num < number:
         raise InvalidAgeException
    else:
        print("Eligible to vote")

except InvalidAgeException:
        print("Exception Occured:Invalid Age")    