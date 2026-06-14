squares = []

for i in range(6):
    squares.append(i*i)

print(squares)

sq = [i * i for i in range(6)]
print(sq)

sq1 = [i*i for i in range(6) if i%2==0]
print(sq1)