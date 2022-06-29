line = input()
encrypted_message = ""

for el in line:
    encrypted_message += chr(ord(el) + 3)

print(encrypted_message)
