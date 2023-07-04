squares_set = {num**2 for num in range(1, 31)}
divisible_by_3_list = [num for num in range(1, 31) if num % 3 == 0]

new_set = squares_set - set(divisible_by_3_list)

print("Squares Set:", squares_set)
print("Numbers Divisible by 3 List:", divisible_by_3_list)
print("New Set (Squares without Numbers Divisible by 3):", new_set)
