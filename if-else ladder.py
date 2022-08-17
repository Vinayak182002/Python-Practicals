#Practice program 3 for pr4

percentage=int(input("Enter the value of percentage:"))

if (percentage>=60):
	print("You have scored: ",percentage,"%")
	print("First Division!!")

elif (percentage<=59 and percentage>=50):
	print("You have scored: ",percentage,"%")
	print("Second Division!!")

elif (percentage<=49 and percentage>=40):
	print("You have scored: ",percentage,"%")
	print("Third Division!!")

else:
	print("You have scored: ",percentage,"%")
	print("Fail!!")
