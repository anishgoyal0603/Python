#file_object = open("data.txt","R") # ValueError: invalid mode: 'R'
#file_object = open("data.txt","r") # FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'

file_object = open("SAMple.txt","r") # works
data = file_object.read()
print(type(data))
print(data)

file_object.close()