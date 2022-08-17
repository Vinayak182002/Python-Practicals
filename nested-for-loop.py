#program to print all unique combinations of 1, 2 and 3

for i in range(1,4):

	for j in range(1,4):

		for k in range(1,4):

			if i==j or j==k or k==i:
				continue

			else:
				print(i,j,k)
