#Program to find position of occurence of number in the list..
import random

list=[]
i=1
while i<20:
	element=random.randint(0,100)
	list.append(element)
	i+=1
print("==========================================================================")
print("The elements in the list are:",list)
print("==========================================================================")
num=int(input("Enter the number to find the position of occurence:"))
print("==========================================================================")
print("The position of ",num," in the list is:")
for x in list:
	if x==num:
		print(list.index(x))
print("==========================================================================")
