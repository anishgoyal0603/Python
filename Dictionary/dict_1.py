# info = {                     
#     [1,2,3]:"dhari"          # TypeError: unhashable type: 'list'
# }

dict2 = {
    "dhari":[1,2,3]
}

print(dict2)

# info = {
#     name : "anish", NameError: name 'name' is not defined

# }

info = {
    "name" :"anish1",
    "name " : "anish2" ,
    "cgpa" : 9.3,
    "subjects" : ["math","science"],
    3.14 : "PI"
}

print(info)
print(type(info))
#print(info[name]) # NameError: name 'name' is not defined
#print(info.name) # AttributeError: 'dict' object has no attribute 'name'
#print(info."name") # SyntaxError: invalid syntax
print(info["name"])
print(info["name "])
print(info[3.14])

info["cgpa"] = 9.4
print(info)