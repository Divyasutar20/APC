
class Wheel:
     def feature_wheel(self):
        print("It has a circular wheel.")

class Rubber:
    def feature_rubber(self):
        print("It is made of rubber.")

class Tyre(Wheel, Rubber):
    def feature_tyre(self):
        print("tyre is made of rubber and shaped like a wheel.")

t=Tyre()
t.feature_wheel()
t.feature_rubber()
t.feature_tyre()
