dict1 = {
    "name":"anish",
    "cgpa":9.3
}

print(dict1.keys()) # dict_keys(['name', 'cgpa'])
print(type (dict1.keys())) # <class 'dict_keys'>
#print(dict1.keys([])) # TypeError: dict.keys() takes no arguments (1 given)

#print(dict1.values(1)) # TypeError: dict.values() takes no arguments (1 given)
print(dict1.values()) # dict_values(['anish', 9.3])
print(type (dict1.values())) # <class 'dict_values'>