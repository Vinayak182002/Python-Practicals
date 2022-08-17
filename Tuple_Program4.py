#accessing tuples in the list

list1=[(1906116,"Vinayak",20),(1906112,"Omkar",19),(1906131,"Prathamesh",19),(1906109,"Sahil",20)]
nameList=[]
for x in list1:
	nameList=nameList+[x[1]]
print("==============================================================================")
print("The students all information:",list1)
print("The names of the students are:",nameList)
print("==============================================================================")
