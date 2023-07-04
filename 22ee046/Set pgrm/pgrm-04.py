list1 = [10, 45, 34, 20, 11]
list2 = [11, 25, 45, 20]
list3 = [20, 25, 11, 14, 45, 65]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

common_elements = set1.intersection(set2, set3)

print("Common Elements:", common_elements)
