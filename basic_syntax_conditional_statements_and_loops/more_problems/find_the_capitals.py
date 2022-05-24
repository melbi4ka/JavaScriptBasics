str_word = input()
upper_list = []


for index, char in enumerate(str_word):
    if char.isupper():
        upper_list.append(index)

print(upper_list)
