digit_word = {
    1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
    6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
}

# Read the integer from the user
num = int(input("Enter an integer: "))

# Convert each digit to its corresponding word
result = []
while num > 0:
    digit = num % 10
    word = digit_word.get(digit)
    result.insert(0, word)
    num //= 10

# Display the number in words
print(" ".join(result))
