names={'Amit','Akshay','Bheem','Aditya','Bhakti','Bhavesh'}
print("=====================================================")
print("Original set is:",names)
print("=====================================================")
set_A=set()
set_B=set()
set_C=set()
for i in names:
    if i.startswith('A' or 'a'):
        set_A.add(i)
    elif i.startswith('B' or 'b'):
        set_B.add(i)
print("=====================================================")
print("Set contains names started with 'A' :",set_A)
print("Set contains names started with 'B' :",set_B)
print("=====================================================")