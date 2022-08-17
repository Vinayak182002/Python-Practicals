
str1 = input("Enter a String:")
print("=========================================")
print("Entered String: ",str1)
print("=========================================")
all_freq = {}
for i in str1:
	if i in all_freq:
		all_freq[i] += 1
	else:
		all_freq[i] = 1
print("=========================================")
print ("Count of all characters in the string is: ",all_freq)
print("=========================================")