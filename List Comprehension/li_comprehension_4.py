# Classify numbers as even or odd
numbers = [1, 2, 3, 4, 5, 6]
classifications = ['even' if num % 2 == 0 else 'odd' for num in numbers]
print(classifications)  # Output: ['odd', 'even', 'odd', 'even', 'odd', 'even']
 
# Replace negative numbers with zero
values = [5, -3, 8, -1, 12, -7]
non_negative = [num if num >= 0 else 0 for num in values]
print(non_negative)  # Output: [5, 0, 8, 0, 12, 0]