list1=list(input("1233Enter list1: "))
print("List1: ",list1)

#append=Adds an element at the end of the list
list2=list(input("Enter list2: "))
print("List2: ",list2)
list1.append(list2)
print("List after append: ",list1)

#The count() method returns the number of elements with the specified value
element=input("Enter element to find occurenace: ")
print("Elements of list1: ",list1.count(element))

#Reverses the order of the list
list1.reverse()
print("Reverse list: ",list1)

#Removes the element at the specified position
list1.pop(2)
print("List1 after pop operation: ",list1)


#The remove() method removes the first occurrence of the element with the specified value.
list1.remove(ele)
print("List after removing element: ",list1)

