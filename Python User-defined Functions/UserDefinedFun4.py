def greater(n1,n2):
	if n1>n2:
		return n1
	else:
		return n2

x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
greaterNumber=greater(x,y)
print("The greater number is:",greaterNumber)