nums=(20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50)

count_even=0
count_odd=0

for x in nums:
    if num%2==0:
        count_even+=1
    else:
        count_odd+=1

print("odd count:",count_odd)
print("odd count:",count_even)
