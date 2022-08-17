#program to find absolute value of a entered number

num = int(input("Enter any number:"))
number=num

if num > 0:
	print("The absolute value of a number is:",num)
else:
	num=(-1)*num
	print("The absolute value of a number is:",num)

print("The absolute value of a number found using abs() method is:",abs(number))