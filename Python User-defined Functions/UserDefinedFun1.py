def calFact(n):
	return 1 if (n==1 or n==0) else n * calFact(n-1);
		
num=int(input("Enter a number to calculate its factorial:"))
fact=calFact(num)
print("The factorial of number is:",fact)