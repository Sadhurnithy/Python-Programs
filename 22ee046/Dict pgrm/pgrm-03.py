def calculate_factors(num, range_start, range_end):
    factors = set()
    for i in range(range_start, range_end + 1):
        if num % i == 0:
            factors.add(i)
    return factors

def generate_factors_dict(range_start, range_end):
    factors_dict = {}
    for num in range(range_start, range_end + 1):
        factors = calculate_factors(num, range_start, range_end)
        factors_dict[num] = factors
    return factors_dict

# Example usage
range_start = 1
range_end = 9
factors_dict = generate_factors_dict(range_start, range_end)

print("Factors Dictionary:", factors_dict)
