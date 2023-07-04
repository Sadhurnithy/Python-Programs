def reverse_tuple(t):
    # Convert the tuple to a list, reverse it, and convert back to a tuple
    reversed_tuple = tuple(reversed(t))
    return reversed_tuple

# Input tuple
t = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

# Reverse the tuple
result = reverse_tuple(t)

# Display the result
print(result)
