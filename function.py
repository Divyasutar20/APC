#creating an array
numbers = [1,2,3,4,5]

#length of array
print("Length of array:",len(numbers))

#accessng elements
print("first element:",numbers[0])

#Adding an element
numbers.append(6)
print("Array after adding the element:",numbers)

#removing an eloement
numbers.remove(3)
print("Array after removing the element:",numbers)

#slicing an array
print("Sliced array:",numbers[1:4])

#iterating through a arrray
for number in numbers:
    print("Element:",number)
    
#finding the index of an element
index_of_4=numbers.index(4)
print("Index of element 4:",index_of_4)

#sorting of the array
numbers.sort()
print("Sorted arrray:",numbers)

#reversing the array
numbers.reverse()
print("Reversed array:",numbers)

#copying the array
numbers_copy = numbers.copy()
print("Copird he array:", numbers_copy)

#checking for the presence of elements
if 2 in numbers :
    print ("Element 2 is present in the arrray")
else:
    print("Element 2 is not present in the array")

#clearing the array
numbers.clear()
print("Array after clearing:",numbers)
