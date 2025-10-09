from abc import ABC ,abstractmethod
class Car(ABC):
    def mileage(self):
        pass
class Tesla(Car):
    def mileage(self):
        print("The Mileage is 30 kmph")
class Suzuki(Car):
    def mileage (self):
        print("The Mileage is 25 kmph")

t=Tesla()
t.mileage()
s=Suzuki()
s.mileage()        