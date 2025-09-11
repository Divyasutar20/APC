# Default Constructor
class demo:
    var1="hi"
    def __init__ (self):
     self.str="welcome"
    def display(self):
        print(self.str)
        print(self.var1)
obj=demo() 
obj.display

# Parameterized Constructor
class Employee:
    var1 = "hi"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.str = "welcome"
    def display(self):
        print(self.str)
        print(self.var1)
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

obj = Employee("Divya", 21)
obj.display()

# Destructor
class demo:
    def __init__(self):
        print("Demo created")
    def __del__(self):
          print("Destructor called,demo deleted")
obj=demo()
del obj
