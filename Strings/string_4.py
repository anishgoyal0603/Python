def first_unique(s):
    counts = {}
    # First pass: count frequencies
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    
    # Second pass: check order
    for char in s:
        if counts[char] == 1:
            return char
    return None

print("First unique in 'swiss':", first_unique("swiss"))