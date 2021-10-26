file = open("text","r")
lst = []
while True:
	line = file.readline()
	if not line:
		break
	lst.append(line)
# print(lst)

# function below does the same thing
# print(file.readlines())