# Step 1: Initialize an empty list
numbers = []

# Step 2: Read integers from the user and append them to the list
while True:
    num = int(input("Enter an integer (enter 0 to stop): "))
    if num == 0:
        break
    numbers.append(num)

# Step 3: Sort the list in ascending order
numbers.sort()

# Step 4: Print the sorted list
print("Sorted List:", numbers)
