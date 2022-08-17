import operator

d = {'Vinayak' : 116, 'Omkar' : 112, 'Sahil' : 109, 'Chirag' : 117}
print("============================================================")
print('Original dictionary : ', d)
print("============================================================")

# sorting by key
d1 = sorted(d.items( ))
print('Ascending order by key : ', d1)
d2 = sorted(d.items( ), reverse = True)
print('Descending order by key : ', d2)
print("============================================================")

# sorting by value
d1 = sorted(d.items( ), key = operator.itemgetter(1))
print('Ascending order by value : ', d1)
d2 = sorted(d.items( ), key = operator.itemgetter(1), reverse = True)
print('Descending order by value : ', d2)
print("============================================================")