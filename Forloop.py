# for i in range(5):
#     for j in range(5):
#         print("*", end="")
#     print()
# print()
# for i in range(5):
#     print("*"*5)
#
# for i in range(5):
#     print("*"*i)
#
# print()
# for i  in range(5):
#     for j in range(i+1):
#         print("*",end="")
#
#     print("\r")

for i in range(10):
    for j in range(10):
        if i == 0 or i ==9:
            print("*",end=" ")
        elif j==0 or j==9:
            print('*',end=" ")
        else:
            print(end="  ")
    print()

print()

n = int(input("Enter a number:"))
mid = n//2
low = mid
high = mid
for i in range(n):
    for j in range(n):
        if i==0 and j==mid:
            print("*",end=" ")
        if (j == low and i!=0)or(j == high and i!=0):
            print("*",end=" ")
        elif low==0 and high==n-1:
            print("*",end=" ")
        else:
            print(end="  ")
    print("\r")
    low=low-1
    high=high+1

for i in range(n):
    for j in range(n):
        if ((i+j) == mid) or((j-i)==mid) or ((i+j)==(((n-1)/2) + n-1) )or ((i-j)==mid):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
