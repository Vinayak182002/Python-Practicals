import keyword
import math
import operator

s="if"
s1="vinayak"
print("============================================")
print(s," is a keyword?",keyword.iskeyword(s))
print(s1," is a keyword?",keyword.iskeyword(s1))
print("============================================")
n1=5.3
print("n1=",n1)
print("Ceiling value of n1 is: ",math.ceil(n1))
print("============================================")
a=4
b=6
print("a=",a,"b=",b)
print("The addition of two number is:",operator.add(a,b))
print("============================================")
