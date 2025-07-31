l=[10,20,30,40,"python","prgramming"]
l.append(70)
print("70 is appended:",l)
l1=[10,20,30,40,"python","prgramming"]
l1.insert(1,15)
print("15 is inserted:",l1)
l2=[10,20,30,40,"python","prgramming"]
b=l2.index('python')
print("index :",b)
l3=[10,10,30,40,"python","prgramming"]
a=l3.count(10)
print("count:",a)
l4=[10,20,30,40,"python","prgramming"]
l4.clear()
l5=[10,20,30,40,"python","prgramming"]
l5.remove(10)
print("10 is removed:",l5)
l6=[10,20,30,40,"python","prgramming"]
l6.copy()
print("list copy:",l6)
l7=[10,20,30,40,"python","prgramming"]
l7.pop(1)
print("popped:",l7)
l8=[10,20,30,40,"python","prgramming"]
l8.reverse()
print("reversed:",l8)
l9=[10,20,30,40,"python","prgramming"]
l9.extend('python')
print("extend:",l9)