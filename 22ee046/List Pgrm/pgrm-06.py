def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def contains_prime_numbers(numbers):
    prime_count = 0
    for num in numbers:
        if is_prime(num):
            prime_count += 1
    if prime_count > 0:
        return True, prime_count
    else:
        return False

n = int(input("Enter the number of integers to input: "))
user_numbers = []
for _ in range(n):
    user_input = int(input("Enter a positive integer: "))
    user_numbers.append(user_input)

result, prime_count = contains_prime_numbers(user_numbers)
print(f"The list contains prime numbers: {result}")
print(f"Number of prime numbers: {prime_count}")
