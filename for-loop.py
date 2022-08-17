#program to find number of alphabets and number of digits in the string:

digits = ['0','1','2','3','4','5','6','7','8','9']

string = str(input("Enter any string:"))

tot_digits=0
tot_alphabets=0

for i in string:
	if i in digits:
		tot_digits+=1
	else:
		tot_alphabets+=1

print("The number of alphabets in the entered string are:",tot_alphabets)
print("The number of digits in the entered string are:",tot_digits)