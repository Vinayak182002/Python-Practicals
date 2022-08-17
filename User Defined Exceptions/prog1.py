a=int(input("Enter any number: "))
b=int(input("Enter another number: "))
try:
    d=a/b
    print(d)
except ZeroDivisionError as obj:
    print(obj)
except NameError as obj1:
    print(obj1) 