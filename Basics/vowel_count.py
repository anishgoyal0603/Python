word = "artificial inteligence"

# count the number of vowels => 5

count = 0
for ch in word:
    if ch == 'i' or ch == "o" or ch == "a" or ch == "e" or ch == "u":
        count += 1

print(f"ans = {count}")        