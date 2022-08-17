d1 = {'Pune' : 30, 'Bangalore': 20} 
d2 = {'Chennai' : 70, 'Delhi' : 50} 
d3 = {'Mumbai' : 90, 'Ahmedabad' : 35}

d4 = { }

for d in (d1, d2, d3) :
	d4.update(d)
print("===========================================")
print("Dictionary 1:",d1)
print("===========================================")
print("Dictionary 2:",d2)
print("===========================================")
print("Dictionary 3:",d3)
print("===========================================")
print("Concatenated Disctionary:",d4)
print("===========================================")
d5={**d1,**d2,**d3}
print("Concatenated Dictionary by another way:",d5)
print("===========================================")

