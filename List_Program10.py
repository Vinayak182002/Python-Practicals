#Program to convert strings in the list to Uppercae..

list=["Python","Java","Cpp","Android","JavaScript"]
print("========================================================")
print("The original list is:",list)
print("========================================================")

for x in list:
	list[list.index(x)]=x.upper()
print("The list after converting elements to uppercase:",list)
print("========================================================")
