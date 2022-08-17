#Practice program 2 to perform operations on list..
#list of odd numbers:
odd=[1,3,5,7,13,15]
print("The list of odd numbers:",odd)
print("===============================================================")
#list of even numbers:
even=[2,4,6,8,10,12,14,16,18,20]
print("The list of even numbers:",even)
print("===============================================================")
#extend method for adding elements of list to the end of current list
odd.extend(even)
print("The combined list is:",odd)
print("===============================================================")
prime=[11,17,29]
#using + operator to apend the list in the beginning
odd=prime+odd
print("The new Combined list will be:",odd)
print("===============================================================")
#count method to get number of items in the list
print("The number of elements present in the list are:",len(odd))
print("===============================================================")
#replacing last 3 values
odd[16]=100
odd[17]=200
odd[18]=300
print("The new list after replacing last three values:",odd)
print("===============================================================")
#deleting all the elements in the list
odd.clear()
print("The list after deleting all the elements:",odd)
print("===============================================================")