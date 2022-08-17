#implementing stack data structure in python using list

stack=[10,20,30,40]
print("======================================================================")
print("The default elements in the stack are:",stack)
print("======================================================================")

choice=int(input("Press 1 to continue  || Press 0 to end: "))
while choice==1:
	print("1.Push into stack\n2.Pop from stack")
	ch=int(input("Enter your choice:"))
	if(ch==1):
		element=int(input("Enter element to push into stack:"))
		stack.append(element)
		print("The stack after pushing the element:",stack)
		print("======================================================================")
	if(ch==2):
		stack.pop();
		print("The stack after pop operation:",stack)
		print("======================================================================")
		
	choice=int(input("Press 1 to continue  || Press 0 to end: "))
print("Thank You!!")