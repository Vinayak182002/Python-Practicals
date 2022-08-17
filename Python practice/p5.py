d1 = {'Anil' : 45, 'Amol' : 32}
print("Dictionary 1:",d1)
print("Dictionary 1 result:-->")
if bool(d1) :
	print('Dictionary is not empty')
else: 
	print('Dictionary is empty')

d2 = { }
print("Dictionary 2:",d2)
print("Dictionary 2 result:-->")
if not bool(d2) :
	print('Dictionary is empty')
else:
	print('Dictionary is not empty')