def is_obtained_from_first_string(first_str, second_str):
    first_str_set = set(first_str)
    second_str_set = set(second_str)

    # Check if all characters in the second string are present in the first string
    return second_str_set.issubset(first_str_set)

# Get the two strings from the user
first_str = input("Enter the first string: ")
second_str = input("Enter the second string: ")

# Check if the second string can be obtained from the first string
if is_obtained_from_first_string(first_str, second_str):
    print("YES")
else:
    print("NO")
