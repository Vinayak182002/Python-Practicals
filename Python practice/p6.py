d = {
'anuj' : {'salary' : 10000, 'age' : 20, 'height' : 6},
'aditya' : {'salary' : 6000, 'age' : 26, 'height' : 5.6},
'rahul' : {'salary' : 7000, 'age' : 26, 'height' : 5.9}
}
lst = [ ]
for v in d.values( ) :
	lst.append(v['salary'])
print("=========================================================")
print("Maximum Salary in the dictionary:",max(lst))
print("Minimum Salary in the dictionary:",min(lst))
print("=========================================================")
