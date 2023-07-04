def count_vowels(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count

# Example usage
input_string = "Hello, World!"
vowel_count = count_vowels(input_string)
print("Input String:", input_string)
print("Number of Vowels:", vowel_count)
