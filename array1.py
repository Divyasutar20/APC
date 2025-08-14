import array as arr
a=arr.array('i',[1,2,3,4,5])
print("the new created array is:",end= "")
for i in range(0,5):
    print(a[i],end="")
    b=arr.array('d',[2.5,3.2,3.3])
    a.insert(1,4)
    print("\nAfter insertion: ",end=" ")
    for i in(a):
        print(i,end="")
    a.append(6)
    print("\nAfter append: ",end="")
    for i in(b):
        print(i,end="")
    a.remove(4)
    print("\nAfter remove: ",end="")
    for i in(a):
        print(i,end="")
    a.pop(2)
    print("\nAfter pop: ",end="")
    for i in(a):
        print(i,end="")
    a.count(1)
    print("\nCount of 1: ",a.count(1))
    a.reverse()
    print("\nAfter reverse: ",end="")
    for i in(a):
        print(i,end="")
    a.index(6)
    print("\nIndex of 6: ",a.index(6))
    


 