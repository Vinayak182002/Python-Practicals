#Program to generate random numbers list in the range 10 to 100
#And then deleting some elements by specifying certain condition...

import random
randomList=[]
i=1

#generating list with 20 random numbers between 10 to 100..
while i<=20:
	element=random.randint(10,100)
	randomList.append(element)
	i=i+1
#end of while loop
print("==========================================================================================================")
print("The original List is:",randomList)
print("The length of the list is:",len(randomList))
print("==========================================================================================================")
#deleting the elements between 20 to 50 from the list..
count=0
for num in randomList:
	if num>20 and num<50:
		count+=1
		randomList.remove(num)
	#end of if
#end of for
print("==========================================================================================================")
print("The number of elements deleted is:",count)
print("The list after deleting the elements:",randomList)
print("The length of the list is:",len(randomList))
print("==========================================================================================================")



