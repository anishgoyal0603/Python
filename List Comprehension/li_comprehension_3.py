multiplication = []

for i in range(2, 5):
    row = []
    for j in range(1, 6):
        row.append(i * j)
    multiplication.append(row)

print(multiplication)

# li_comprehension