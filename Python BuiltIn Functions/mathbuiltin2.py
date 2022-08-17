import math

print("============================================")
print("Function isint()")
x = float('inf')
y = 45
if math.isinf(x):
    print('X is Infinity')
print("============================================")

print("Function isfinite()")    
print("x is not a finite number: ",math.isfinite(x))
print("y is a finite number: ", math.isfinite(y))
print("============================================")

print("Function pow()")
print('The value of 5^8: ' + str(math.pow(5, 8)))
print("============================================")

print("Function sqrt()")
print('Square root of 400: ' + str(math.sqrt(400)))
print("============================================")

print("Function exp()")
print('The value of 5^e: ' + str(math.exp(5)))
print("============================================")

print("Function log()")
print('The value of Log(625), base 5: ' + str(math.log(625, 5)))
print("============================================")
