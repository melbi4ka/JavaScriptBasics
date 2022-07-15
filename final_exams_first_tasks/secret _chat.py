
message = input()
a_command = input()

while a_command != "Reveal":
    command = a_command.split(":|:")
    if command[0] == "InsertSpace":
        index = int(command[1])
        if 0 <= index <= len(message):
            message = message[:index] + " " + message[index::]
        print(message)

    elif command[0] == "Reverse":
        substring = command[1]
        if substring in message:
            reverse_substring = "".join(reversed(substring))
            message = message.replace(substring, "", 1)
            message = message + reverse_substring
            print(message)
        else:
            print("error")


    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        if substring in message:
            message = message.replace(substring, replacement)
        print(message)

    a_command = input()

print(f"You have a new text message: {message}")
