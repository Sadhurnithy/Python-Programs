n = int(input("Enter the number of words: "))

word_list = []
for i in range(n):
    word = input("Enter a word: ")
    word_list.append(word)

word_lengths = []
for word in word_list:
    length = len(word)
    word_lengths.append(length)

longest_word = max(word_list, key=len)

print("Length of each word:")
for i in range(len(word_list)):
    print(f"{word_list[i]}: {word_lengths[i]}")

print("Longest word:", longest_word)
