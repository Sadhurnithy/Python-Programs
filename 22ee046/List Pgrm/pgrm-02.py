# Step 1: Read a list of 5 numbers from the user
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Step 2: Define a function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Step 3: Generate a new list containing the factorial of each number
factorial_list = []
for num in numbers:
    fact = factorial(num)
    factorial_list.append(fact)

# Step 4: Print the new list containing the factorials
print("Factorial List:", factorial_list)
