"Methods"

a = {1, 2, 4, 5}
b = {5, 6, 7, 8}

union = a | b  # {1, 2, 4, 5, 6, 7, 8}
intersection = a & b  # {5}
subset = a < b  # False
diff = b - a  # {8, 6, 7}
symmetric_difference = a ^ b   # {1, 2, 4, 6, 7, 8}


"Set Comprehensions"

nums = [1, 2, 3, 4, 5, 5, 5, 6, 6, 6, 7, 8, 7, 7, 9, 9, 9, 9, 5, 6, 4, 3, 4, 4, 4, 5]
unique = {i for i in nums}

print(unique)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

