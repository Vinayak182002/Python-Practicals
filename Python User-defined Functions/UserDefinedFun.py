def testPrime(n):
	if n==1:
		return False
	elif n==2:
		return True
	else:
		for x in range(2,n):
			if(n%x==0):
				return False
		return True

num=int(input("Enter number to check whether it is prme or not:"))
if(testPrime(num)):
	print("Entered number is a prime number!")
else:
	print("Entered number is not a prime number!")
