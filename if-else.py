#Practice program 1 for pr4

quantity=int(input("Enter the quantity you want to purchase:"))
price=float(input("Enter the price per piece:"))
discount=0

if quantity>1000:
	discount=10	
	totalExpense=quantity*price
	totalExpenseDis=totalExpense-(totalExpense*10/100)
	print("Total Expense= Rs.",totalExpense)
	print("Congratulation you have won the dicount!!")
	print("Total Expense after applying discount= Rs.",totalExpenseDis)

else:
	discount=0
	totalExpense=quantity*price
	print("Total Expense= Rs.",totalExpense)