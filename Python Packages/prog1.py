import numpy

x=numpy.array([[1,2],[4,8]])
y=numpy.array([[7,8],[9,10]])

#using add() to add matrices
print("The element wise addition of matrices is:")
print(numpy.add(x,y))
print("===============================================")

#usinf subtract() to subtract matrices
print("The element wise subtraction of matrix is:")
print(numpy.subtract(x,y))
print("===============================================")

#using dot() to multiply matrices
print("The product of matrices is:")
print(numpy.dot(x,y))
print("===============================================")

#using divide() to divide matrices
print("The element wise division of matrix is:")
print(numpy.divide(x,y))
print("===============================================")
