FileOp = open("testing.txt", "w")
line = input("Write some data: ")
FileOp.write(line)
FileOp.close()

print("Data inside file: ")
FileOp = open("testing.txt", "r")
print(FileOp.read())
