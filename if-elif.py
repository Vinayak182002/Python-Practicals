#Practice program 2 for pr4

salary=int(input("Enter the employee salary:"))
hra=0
da=0

if salary<1500:
	hra=salary*10/100
	da=salary*90/100
elif salary>=1500:
	hra=500
	da=salary*90/100

grossSalary=salary+hra+da
print("\n\tHRA of employee salary is: Rs.",hra)
print("\tDA of employee salary is: Rs.",da)
print("\tGross Salary of an employee is: Rs.",grossSalary)