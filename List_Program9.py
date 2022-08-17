#Program to seperate positive and negative numbers from the list

list=[10,20,-50,30,-2,-30,50,100,-35]
positive=[]
negative=[]
print("==========================================================")
print("The elements in the list are:",list)
print("==========================================================")
for x in list:
	if x>0:
		positive.append(x)
	else:
		negative.append(x)
print("==========================================================")
print("The positive elements list is:",positive)
print("==========================================================")
print("The negative elements list is:",negative)
print("==========================================================")
