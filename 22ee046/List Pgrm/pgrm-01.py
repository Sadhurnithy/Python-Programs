# Step 1: Read the value of 'n' from the user
n = int(input("Enter the number of integers: "))

# Step 2: Initialize empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Step 3: Read 'n' integers from the user and append them to the respective lists
for i in range(n):
    num = int(input("Enter an integer: "))
    
    # Check if the number is even or odd and append it to the appropriate list
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Step 4: Print the lists of even and odd numbers
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
