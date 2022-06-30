def encrypted_message(a_line):
    message = ""
    for el in a_line:
        message += chr(ord(el) + 3)
    return message

line = input()
print(encrypted_message(line))
