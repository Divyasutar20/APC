# Default Constructor with private variable
class demo:
    _var1 = "Welcome" 
    def __init__(self):
        self.str = "Hi"
    def display(self):
        print(self.str)
        print(self._var1)

class Employee(demo):
    obj = demo()
    obj.display()
