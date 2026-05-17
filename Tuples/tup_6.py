tup = (1,2,2,3,2,4)

#print(tup.count()) # TypeError: tuple.count() takes exactly one argument (0 given)
print(tup.count([7,2,7])) # valid  searches for exact list [7,2,7] in tuple
print(tup.count(4))
print(tup.count(2))
print(tup.count(2,4)) # TypeError: tuple.count() takes exactly one argument (2 given)

