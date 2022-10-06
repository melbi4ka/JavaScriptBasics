message = input()
a_command = input()

while a_command != "Reveal":
    command = a_command.split(":|:")
    action = command[0]

    if action == "InsertSpace":
        index = int(command[1])
        message = message[:index] + " " + message[index:]
        print(message)

    if action == "Reverse":
        substring = command[1]
        if substring in message:
            reverse_substring = substring[::-1]
            message = message.replace(substring, "", 1)
            message = message + reverse_substring
            print(message)
        else:
            print("error")

    if action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        if substring in message:
            message = message.replace(substring, replacement)
            print(message)


    a_command = input()

print(f"You have a new text message: {message}")
