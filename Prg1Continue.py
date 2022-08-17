#program to print 1 to 15 numbers but skip the number which is divisible by 3


for i in range(1,16):
	
	if (i % 3 == 0):
		continue;
	else:
		print("The number is :",i)
