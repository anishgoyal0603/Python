nums = [1,2,3,10,4]

for val in nums:
    print(val)

idx = 0
x = 10
for val in nums:
    if val == x:
        print(f"{x} found at idx = {idx}")
        print(idx)
        break
    idx += 1    