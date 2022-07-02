import re

key = input().split()
command = input()
pattern = r"&([a-zA-Z]+)&.+<([0-9A-Za-z]+)>"

strings_list = []
while command != "find":
    change_string = ""
    for i in range(len(command)):
        current_char = ord(command[i])
        change_string += chr(current_char - int(key[i]))
        key.append(key[i])

    strings_list.append(change_string)

    command = input()

print(strings_list)

for el in strings_list:
    matches = re.findall(pattern, el)
    for match in matches:
        if match:
            print(f"Found {match[0]} at {match[1]}")



