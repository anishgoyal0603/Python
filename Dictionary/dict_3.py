dict1 = {
    "name":"anish",
    "cgpa":9.3
}

# print(dict1.get()) # TypeError: get expected at least 1 argument, got 0
print(dict1.get("cg"))
print(dict1.get('cgpa'))
print(dict1.get('cgpa',1))
#print(dict1.get('cgpa',5,2)) # TypeError: get expected at most 2 arguments, got 3
