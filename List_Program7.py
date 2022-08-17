#A program to delete duplicate elements from the list..

list=[10,20,30,10,20,50,60,30,90,100]
print("==================================================")
print("The elements in the list are:",list)
print("==================================================")

uniqueList=[]
duplicate=[]
#main logic..
for x in list:
	if x not in duplicate:
		uniqueList.append(x)
		duplicate.append(x)

print("The list after removing duplicate elements:",uniqueList)
print("==================================================")
