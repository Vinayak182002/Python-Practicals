#Program No.5 on Tuples

t1=('F','I','a','b','b','e','r','g','a','s','t','e','d')
print("===============================================================================")
print("Elements in the tuple are:",t1)
print("===============================================================================")
#directly addding ! to the end of tuple is not possible as tuple is immutable
#so to add it lets create a new tuple
t1=t1+('!',)
print("===============================================================================")
print("New elements in the tuple are:",t1)
print("===============================================================================")
#converting tuple to a string
str=''.join(t1)
print("===============================================================================")
print("Tuple is converted to String: ",str)
print("===============================================================================")
# extracting ('b', 'b') from the tuple
t = t1[3:5]
print("===============================================================================")
print("Extracting elements from tuple: ",t)
print("===============================================================================")
# counting number of 'e' in the tuple
count = t1.count('e')
print("===============================================================================")
print("Count of 'e' in the tuple= ",count)
print("===============================================================================")
# checking whether 'r' exists in the tuple
("===============================================================================")
print("Checking whether 'r' exists in tuple: ",'r' in t1)
("===============================================================================")
#converting tuple to a list
l1=list(t1)
print("===============================================================================")
print("Tuple is converted to List: ",l1)
print("===============================================================================")
# tuples are immutable, so we cannot remove elements from it
# we need to split the tuple, eliminate the unwanted element and then merge the tuples
t1 = t1[:3] + t1[7:]
print("===============================================================================")
print("Tuple after deleting the elements:",t1)
print("===============================================================================")