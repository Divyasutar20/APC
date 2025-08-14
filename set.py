Months = set(["Jan", "Feb", "March", "April", "May", "June"])
print(Months)

Months.pop()
print(Months)

Months.add("July")
print(Months)

Months.update(["Oct"])
print(Months)

Months.discard("Jan")
print(Months)

Months.remove("June") 
print(Months)

Months_copy = Months.copy()
print(Months_copy)

Months.clear()
print(Months)


#operation on two set
N1={1,2,3,4,5,6,100,98}
N2={100,99,98,4,97,96,95}
print(N1 | N2)
print(N1.union(N2))
print(N1.intersection(N2))
print(N1.difference(N2))
print(N1.symmetric_difference(N2))
print(N1.issubset(N2))
print(N1.isdisjoint(N2))
print(N1.issuperset(N2))