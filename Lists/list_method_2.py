list1 = [7,1,99,32]

#print(list1.insert()) # TypeError: insert expected 2 arguments, got 0
#print(list1.insert(5)) # TypeError: insert expected 2 arguments, got 0
print(list1.insert(5,2)) # adds at last if index is out of bound
print(list1)

print(list1.insert(2,8))
print(list1)