def remove_even_numbers(input_list):
    odd_list = []
    for item in input_list:
        if item % 2 != 0:
            odd_list.append(item)
    return odd_list

# Example usage
given_list = [5, 6, 2, 8, 9, 12, 66]
new_list = remove_even_numbers(given_list)
print("Original List:", given_list)
print("New List without even numbers:", new_list)
