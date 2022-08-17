#program to perform list operations...

names=['Anil','Amol','Aditya','Avi','Alka']

print("The items in the list are:")
print(names)
print("======================================================")
#insert method for adding element in the list
names.insert(2,'Anuj')
print("\nThe items in the list after inserting an element:")
print(names)
print("======================================================")
#sort method for sorting the list
names.sort()
print("\nThe list after sorting:")
print(names)
print("======================================================")
#reverse method for reversing the list
names.reverse()
print("\nThe reversed sorted list:")
print(names)
print("======================================================")