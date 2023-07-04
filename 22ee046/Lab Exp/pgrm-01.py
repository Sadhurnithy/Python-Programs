def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

# Get an integer input from the user
num = int(input("Enter an integer: "))

# Check if the number is odd
if num % 2 != 0:
    # Find the factorial of the number
    fact = factorial(num)
    
    # Find the number of digits in the factorial
    num_digits = len(str(fact))
    
    print("Factorial of", num, ":", fact)
    print("Number of digits in factorial:", num_digits)
else:
    # Check if the number is a palindrome
    if is_palindrome(num):
        print(num, "is a palindrome")
    else:
        print(num, "is not a palindrome")
