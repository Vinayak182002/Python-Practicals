def count(string):
	ucount=0
	lcount=0
	for i in string:
		if i.islower():
			lcount+=1
		elif i.isupper():
			ucount+=1
	print("String:",string)
	print("The number of lowercase letters in string are:",lcount)
	print("The number of uppercase letters in string are:",ucount)

str=input("Enter the string:")
count(str)