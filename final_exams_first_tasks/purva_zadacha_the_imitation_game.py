text = input()

a_command = input()

while a_command != "Decode":
    command = a_command.split("|")
    action = command[0]

    if action == "ChangeAll":
        substring = command[1]
        replacement = command[2]

        if substring in text:
            text = text.replace(substring,replacement)
            # print(text)

    elif action == "Insert":
        index = int(command[1])
        value = command[2]

        if 0 <= index < len(text):
            text = text[: index] + value + text[index: ]
        else:
            text = text + value
            # print(text)

    elif action == "Move":
        num_letters = int(command[1])

        if num_letters < len(text):
            text = text[num_letters : ]  + text [: num_letters]

        else:
            diff = len(text) - num_letters
            text = text[diff : ]  + text [: diff]
            # print(text)


    a_command = input()

print(f"The decrypted message is: {text}")






