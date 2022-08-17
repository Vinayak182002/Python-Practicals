#program to print all prime numbers between 1 to 300:

list = []

for i in range(1,300):
	if i==0 or i==1:
		continue
	else:
		for j in range(2, int(i/2)+1):
			if i % j == 0:
				break
		else:
			list.append(i)

print("The prime numbers between 1 to 300 are:")
for j in list:
	print(j,end='  ')
