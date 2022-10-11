import re

message = input()


while message != "Over!":
    is_valid = False
    m = int(input())
    valid_word = ""
    verification_code = ""
    pattern = r"^\d+([A-Za-z]+)([^A-Za-z]*?)$"

    matches = re.finditer(pattern, message)

    for match in matches:
        if match:
            word = match.group(1)
            if len(word) == m:
                valid_word = word
                is_valid = True

    for char in message:
        if char.isdigit():
            index = int(char)
            if 0 <= index < len(valid_word):
                verification_code += valid_word[index]
            else:
                verification_code += " "

    if is_valid:
        print(f"{valid_word} == {verification_code}")

    message = input()
