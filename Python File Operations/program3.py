f1 = open("testing.txt", "r")
f2 = open("newFile.txt", "a")
for data in f1.read():
    if(data == "h" or data == "H"):
        f2.write("a")
    else:
        f2.write(data)

print("Content successfully transferred to new File!")
