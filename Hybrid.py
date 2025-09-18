class Student:
    def name1(self):
        print("Name of the Students")
class Excellent(Student):
     def name2(self):
        print("Excellent student name")
class Average(Student):
     def name3(self):
        print("Average student name")
class Performance(Excellent,Average):
    def name4(self):
        print("All student name")
obj1 = Performance()
obj1.name1()
obj1.name2()
obj1.name3()
obj1.name4()