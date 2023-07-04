string = input("Enter a string: ")

ascii_list = []
for char in string:
    ascii_value = ord(char)  # Convert character to ASCII value
    ascii_list.append(ascii_value)

print("ASCII values of characters in the string:", ascii_list)
