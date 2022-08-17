#Program to add two 3*4 matrices..

matrix1=[[1,2,3,4],
		  [5,6,7,8],
		  [9,10,11,12]]

matrix2=[[13,14,15,16],
		  [17,18,19,20],
		  [21,22,23,24]]

answer=[[0,0,0,0],
		  [0,0,0,0],
		  [0,0,0,0]]
print("=============================================================================")
print("First Matrix is:",matrix1)
print("Second Matrix is:",matrix2)
print("=============================================================================")

#Adding two matrices..
for i in range(len(matrix1)):
	for j in range(len(matrix1[0])):
		answer[i][j]=matrix1[i][j]+matrix2[i][j]
	#end of inner for loop
#end of outer for loop
print("The addition of Matrices is:",answer)
print("=============================================================================")
