#pack and unpack
#packing multiples of 10
tuple1=(10,20,30,40,50,60,70,80,90,100)
print("=======================================================")
print("The first 10 mutiples of 10 are:",tuple1);
print("=======================================================")
#unpacking tuple into 10 different variables
a,b,c,d,e,f,g,h,i,j = tuple1
print("=======================================================")
print("A:",a," B:",b," C:",c," D:",d," E:",e," F:",f," G:",g," H:",h," I:",i," J:",j);
print("=======================================================")
#unpacking first and last in variables and other in disposable variables
x,_,_,_,_,_,_,_,_,y=tuple1
print("=======================================================")
print("First element:",x,"\nLast element:",y,"\nValue of disposable variable:",_)
print("=======================================================")
#unpacking first and last in variables and other in single disposable variables
i,*_,j=tuple1
print("=======================================================")
print("First element:",i,"\nLast element:",j,"\nValue of disposable variable:",_)
print("=======================================================")
