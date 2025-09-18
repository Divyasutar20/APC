class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Vehicle: {self.brand} {self.model}")

class Bike(Vehicle):
    def type(self):
        print(f"{self.brand} {self.model} is a Bike.")


class Car(Vehicle):
    def type(self):
        print(f"{self.brand} {self.model} is a Car.")

class Bus(Vehicle):
    def type(self):
        print(f"{self.brand} {self.model} is a Bus.")
class Truck(Vehicle):
    def type(self):
        print(f"{self.brand} {self.model} is a Truck.")


        b1=Bike("Honda","Activa")
        c1=Car("Tata","Nano")
        b2=Bus("Konduskar","AC Bus")
        t1=Truck("Ashoka","Good Carrier")

        b1.display_info()
        c1.displsy_info()
        b2.display_info()
        t1.display_info()
        
