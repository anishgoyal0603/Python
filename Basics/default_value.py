# def sum(a=1,b): # error
#     return a + b

#print(sum(1,2)) # error as function must be defined first then called

def sum(a,b=1):
    return a + b

print(sum(1,2))
print(sum(5))