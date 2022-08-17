#implementing queue data structure in python using list

queue=['A','B','C','D']
print("======================================================================")
print("The default elements in the queue are:",queue)
print("======================================================================")

choice=int(input("Press 1 to continue  || Press 0 to end: "))
while choice==1:
	print("1.Push into queue\n2.Pop from queue")
	ch=int(input("Enter your choice:"))
	if(ch==1):
		element=str(input("Enter element to push into queue:"))
		queue.append(element)
		print("The queue after pushing element:",queue)
		print("======================================================================")
	if(ch==2):
		queue.pop(0);
		print("The queue after pop operation:",queue)
		print("======================================================================")
		
	choice=int(input("Press 1 to continue  || Press 0 to end: "))
print("Thank You!!")