# line = input()
# encrypted_message = ""
#
# for el in line:
#     encrypted_message += chr(ord(el) + 3)
#
# print(encrypted_message)

def encrypted_message(a_line):
    message = ""
    for el in a_line:
        message += chr(ord(el) + 3)
    return message


line = input()
print(encrypted_message(line))




