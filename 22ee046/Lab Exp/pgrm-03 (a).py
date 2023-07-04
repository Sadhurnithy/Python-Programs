def find_element_indices(numbers, element):
    positive_indices = []
    negative_indices = []
    occurrence_count = 0

    for i in range(len(numbers)):
        if numbers[i] == element:
            occurrence_count += 1
            positive_indices.append(i)
            negative_indices.append(i - len(numbers))

    return positive_indices, negative_indices, occurrence_count

# Read a list of numbers from the user
numbers = [int(x) for x in input("Enter the list of numbers: ").split()]

# Read the element to be found from the user
element = int(input("Enter the element to be found: "))

# Find the positive and negative indices and the occurrence count
positive_indices, negative_indices, occurrence_count = find_element_indices(numbers, element)

# Display the result
print("Element", element, "occurs", occurrence_count, "time(s) in the list.")
print("Positive Index:", positive_indices)
print("Negative Index:", negative_indices)
