file_object = open("SAMple.txt","r") # works
data = file_object.readline()
print(type(data))
print(data)

data = file_object.readline()
print(data)

data = file_object.readlines()
print(data)

file_object.close()