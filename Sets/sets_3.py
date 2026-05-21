set1 = {5,3,8}

# print(set1.add()) # TypeError: set.add() takes exactly one argument (0 given)
print(set1.add(2)) # None
print(set1)
#print(set1.remove()) # TypeError: set.remove() takes exactly one argument (0 given)
print(set1.remove(5)) # None
#print(set1.remove(4)) # KeyError: 4

print(set1.clear()) # None
print(set1)