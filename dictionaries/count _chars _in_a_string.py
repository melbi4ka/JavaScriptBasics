a_words = input().split()
words = "".join(a_words)


word_dict = {}

for char in words:
    if char not in word_dict:
        word_dict[char] = 0
    word_dict[char] += 1

for key, value in word_dict.items():
    print(f"{key} -> {value}")

