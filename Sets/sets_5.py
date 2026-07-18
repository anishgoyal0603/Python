original = {1, 2, 3, 4, 5}

# Assignment: both names point to the same set object
ref = original
ref.add(99)
print("--- Assignment (=) ---")
print("original:", original)
print("ref:", ref)

# Reset
original = {1, 2, 3, 4, 5}

# Shallow copy: independent object
copied = original.copy()
copied.add(42)
print("\n--- Shallow copy (.copy()) ---")
print("original:", original)
print("copied:", copied)