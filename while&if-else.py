#program to reverse a number and check whether it is palindrome or not:

number= int(input("Enter any 5 digit number:"))
num=number
reversed=0

while number > 0:
	digit = number % 10
	reversed = reversed * 10 + digit
	number //= 10

print("The reversed number is:",reversed)

if num==reversed:
	print("The original number and reversed number is same!")
else:
	print("The original number and reversed number is not same!")