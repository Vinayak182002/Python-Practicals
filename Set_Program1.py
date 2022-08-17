#CREATE A NEW SET
s={10,2,-3,4,5,88}
print("===================================")
print("The elements in the Set are :",s)
print("===================================")
print("1]Number of items in set :",len(s))
print("2]Maximum element in set :",max(s))
print("3]Minimum element in set :",min(s))
print("4]Sum of items in set :",sum(s))
print("===================================")
s2=sorted(s)
print("Sorted Set :",s2)
print("Original Set:",s)
print("===================================")
msg = '100 present in given set 'if 100 in s else '100 not in set'
print(msg)
print("===================================")
msg = '-3 present in given set 'if -3 in s else '-3 not in set'
print(msg)
print("===================================")

