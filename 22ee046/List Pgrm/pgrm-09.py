years = ["January 2023", "February 2024", "March 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

corrected_years = []
for year in years:
    month, year_value = year.split(" ")
    if year_value != "2023":
        year = month + " 2023"
    corrected_years.append(year)

print("Original List:", years)
print("Corrected List:", corrected_years)
