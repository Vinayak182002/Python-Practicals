import math
print("========================================================")
print("Function ceil() and fllor()")
print('The Floor and Ceiling value of 19.60 are: ' + str(math.ceil(23.56)) + ', ' + str(math.floor(23.56)))
print("========================================================")

x = 20
y = -15

print("Function fabc()")
print('Absolute value of -47 and 28 are: ' + str(math.fabs(-47)) + ', ' + str(math.fabs(28)))
print("========================================================")

my_list = [12, 4.25, 89, 3.02, -65.23, -7.2, 6.3]
print("List is: ",my_list)
print("========================================================")

print("Function fsum()")
print('Sum of the elements of the list: ' + str(math.fsum(my_list)))
print("========================================================")

print("Function gcd()")
print('The GCD of 80 and 68 : ' + str(math.gcd(80, 68)))
print("========================================================")

print("Function isnan()")
x = float('nan')
if math.isnan(x):
    print("X is not a number")
print("========================================================")

