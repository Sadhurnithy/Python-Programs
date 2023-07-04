def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example usage
given_list = [1, 2, 3, 4, 2, 1, 5, 6, 3]
new_list = remove_duplicates(given_list)
print("Original List:", given_list)
print("New List without duplicates:", new_list)
