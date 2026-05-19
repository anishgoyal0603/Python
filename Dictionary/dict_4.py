dict_1 = {
    "name" : "anish",
    "cgpa" : 9.17,
    "subjects" : ["Advanced Java","unix OS"],
     3.14 : "PI"
}

dict_1.update() # works , nothing is updated in dictionary
# dict_1.update(1) # TypeError: 'int' object is not iterable
#dict_1.update([2]) # TypeError: cannot convert dictionary update sequence element #0 to a sequence
dict_1.update({"surname" : "goyal","Advanced Java":"nitin nagar sir"})
print(dict_1)