def check_subsequence(string1, string2):
    i = 0
    j = 0

    while i < len(string1) and j < len(string2):
        if string1[i] == string2[j]:
            j += 1
        i += 1

    return j == len(string2)

# Example usage
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if check_subsequence(string1, string2):
    print("YES")
else:
    print("NO")
