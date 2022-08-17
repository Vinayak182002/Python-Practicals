#program to implement all the Arithmetic Operators, Logical Operators and Bitwise Operators..
#Practical 3
#Arithmetic Operators:
print("\nArithmetic Operators:")
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print("\nNumbers are A="+str(a)+" B="+str(b))
print("Performing Arithmetic Operations:")
add=a+b;
print("\tAddition is:",add)

sub=a-b;
print("\tSubtraction is:",sub)

mul=a*b;
print("\tMultiplication is:",mul)

div=a/b;
print("\tDivision is:",div)

exp=a**b
print("\tExponential is:",exp)

mod=a%b
print("\tModulus is:",mod)

fdiv=a//b
print("\tFloor division is:",fdiv)
print("==================================================")

#Logical Operators:
print("\nLogical Opeartors")
x=int(input("\nEnter number 1 for performing logical operations:"))
y=int(input("Enter number 2 for performing logical operations:"))
z=int(input("Enter number 3 for performing logical operations:"))

print("Entered Number 1 is:",x)
print("Entered Number 2 is:",y)
print("Entered Number 3 is:",z)
if x>y and x>z:
	print("\nNumber 1 is grater number from all the numbers!")
elif y>x and y>z:
	print("\nNumber 2 is greater number from all the numbers!")
else:
	print("\nNumber 3 is greater number from all the numbers!")

l=int(input("\nEnter first number for OR operation:"))
m=int(input("Enter second number for OR operation:"))

print("Number 1:",l)
print("Number 2:",m)

if l>0 or m>0:
	print("Either number 1 or number 2 is greater than 0")
else:
	print("No number is greater than 0")

print("==================================================")


#Bitwise Opeartors
print("\nBitwise Opeartors:")
p=10
q=4

print("\nNumber 1:",p)
print("Number 2:",q)
print("\nBitwise AND result p & q is:",p&q)
print("Bitwise OR result p | q is:",p|q)
print("Bitwise NOT result ~p is:",~p)
print("Bitwise XOR result p ^ q is:",p^q)
print("Bitwise RIGHT SHIFT result p>>2 is:",p>>2)
print("Bitwise LEFT SHIFT result p<<2 is:",p<<2)


print("==================================================")








