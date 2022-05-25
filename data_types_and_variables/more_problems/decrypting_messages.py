key = int(input())
number = int(input())
encrypted_message = ""

for num in range(number):
    letter = input()
    char = chr(ord(letter) + key)
    encrypted_message += char

print(encrypted_message)
