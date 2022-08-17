import random
random_nos=set()
for i in range(10):
    random_nos.add(random.randint(15,45))
print("=============================================")
print("Random 10 numbers : ",random_nos)
print("==============================================")
count =0
temp =set()
for i in random_nos:
    if i < 30:
        count += 1
    if i <=35:
        temp.add(i)
random_nos=temp
print("Total Numbers less than 30 are :",count)
print("==============================================")
print("Set after deleting elements greater than 35 :",temp)
print("==============================================")

