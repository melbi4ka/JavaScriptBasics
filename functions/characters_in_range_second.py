def string_characters(a, b):
    charact = ""
    for num in range(ord(a)+1, ord(b)):
        charact += chr(num)
    return " ".join(charact)


char_one = input()
char_two = input()
print(string_characters(char_one, char_two))
