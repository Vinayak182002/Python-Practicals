#counting number of boys and girls

list=[("Vinayak",),"Pooja","Suvarna",("Omkar",),("Prathamesh",)]
nBoys=0
nGirls=0
for x in list:
	if isinstance(x,tuple):
		nBoys+=1
	else:
		nGirls+=1
print("=========================================")
print("List is:",list)
print("Number of Boys:",nBoys)
print("Number of Girls:",nGirls)
print("=========================================")
