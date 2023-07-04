def is_subset(set_a, set_b):
    for element in set_a:
        if element not in set_b:
            return False
    return True

# Input sets
set_a = {1, 2, 3, 4}
set_b = {1, 2, 3}

# Check if set_a is a subset of set_b
result = is_subset(set_a, set_b)

# Display the result
print(result)
