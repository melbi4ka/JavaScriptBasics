first_words = input().split(", ")
second_word = input().split(", ")

new_words = []
for el in first_words:
    for elm in second_word:
        if el in elm and el not in new_words:
            new_words.append(el)

print(new_words)


