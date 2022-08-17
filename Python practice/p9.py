marks = {
'Subu' : {'Maths' : 88, 'Eng' : 60, 'SSt' : 95},
'Amol' : {'Maths' : 78, 'Eng' : 68, 'SSt' : 89},
'Raka' : {'Maths' : 56, 'Eng' : 66, 'SSt' : 77}
}
print("========================================")
print("Dictionary:",marks)
print("========================================")
name='Amol'
sub='Eng'
print("Amol's marks in English are:",marks.get(name).get(sub))
print("========================================")
name1='Raka'
marks.get(name1)['Maths']=77
print("Changing Maths marks of Raka:",marks.get(name1))
print("========================================")
d=sorted(marks.items())
print("Sorted Dictionary:",d);
print("========================================")