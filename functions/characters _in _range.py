def string_characters(a, b):
    list_char = []
    for num in range(ord(a)+1, ord(b)):
        charact = chr(num)
        list_char.append(charact)
    return " ".join(list_char)


char_one = input()
char_two = input()
print(string_characters(char_one, char_two))

