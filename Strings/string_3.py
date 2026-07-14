def is_rotation(s1, s2):
    # Rotations must be the same length
    if len(s1) != len(s2):
        return False
    
    # Double the first string
    combined = s1 + s1
    
    # Check if s2 is inside the doubled version
    return s2 in combined

s1 = "waterbottle"
s2 = "erbottlewat"
print(f"Is '{s2}' a rotation of '{s1}'? {is_rotation(s1, s2)}")