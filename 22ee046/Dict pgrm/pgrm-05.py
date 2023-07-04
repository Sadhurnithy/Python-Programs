cricketer = {
    "VinayKumar": {102, 5},
    "Yuzvendra Chahal": {89, 10},
    "Sandeep Sharma": {95, 8},
    "Umesh Yadav": {85, 6},
    "BhuvaneswarKumar": {106, 10},
    "Basil Thampi": {70, 5}
}

# Calculate bowling averages and replace values in the dictionary
for key, value in cricketer.items():
    total_runs, total_wickets = value
    bowling_average = total_runs / total_wickets
    cricketer[key] = {bowling_average}

# Sort the dictionary based on the values (bowling averages)
sorted_cricketer = dict(sorted(cricketer.items(), key=lambda x: x[1]))

# Display the sorted dictionary
print(sorted_cricketer)
