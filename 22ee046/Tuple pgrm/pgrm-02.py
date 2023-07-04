def extract_positive_numbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    return tuple(positive_numbers)

# Example usage
number_list = [-20, -4, -7, 6, 4, 8, 3, -6]
positive_tuple = extract_positive_numbers(number_list)
print("Original List:", number_list)
print("Tuple of Positive Numbers:", positive_tuple)
