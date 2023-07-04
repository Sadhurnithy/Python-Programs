def invert_dict(dictionary):
    inverted_dict = {value: key for key, value in dictionary.items()}
    return inverted_dict

# Example usage
dict1 = {'Reg.No': 123, 'Name': 'abc', 'Course': 'CSE'}
inverted_dict = invert_dict(dict1)
print("Original Dictionary:", dict1)
print("Inverted Dictionary:", inverted_dict)
