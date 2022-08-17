FileOp = open("testing.txt", "a")
AppendLine = input("Enter content to append in the existing file: ")
FileOp.write(AppendLine)
FileOp.close()

print("Content inside the file: ")
FileOp = open("testing.txt", "r")
print(FileOp.read())


