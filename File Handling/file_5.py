file_object = open("sample.txt","a+")

file_object.write("123")
print(file_object.read()) # prints nothing

file_object.close()

print("new work")
