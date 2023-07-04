def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = {num for num in range(1, 51) if is_prime(num)}
divisible_by_5 = {num for num in range(1, 51) if num % 5 == 0}

union_set = prime_numbers.union(divisible_by_5)
intersection_set = prime_numbers.intersection(divisible_by_5)
difference_set = prime_numbers.difference(divisible_by_5)
symmetric_difference_set = prime_numbers.symmetric_difference(divisible_by_5)

print("Prime Numbers:", prime_numbers)
print("Numbers Divisible by 5:", divisible_by_5)
print("Union Set:", union_set)
print("Intersection Set:", intersection_set)
print("Difference Set:", difference_set)
print("Symmetric Difference Set:", symmetric_difference_set)
