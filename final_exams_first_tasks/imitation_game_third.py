message = input()
command = input()

while command != "Decode":
    current_command = command.split("|")
    action = current_command[0]
    if action == "Move":
        idx = int(current_command[1])
        moved = message[0:idx]
        message = message[idx::] + moved

    if action == "Insert":
        idx = int(current_command[1])
        value = current_command[2]
        if idx >= 0:
            message = message[0:idx] + value + message[idx::]

    if action == "ChangeAll":
        substr = current_command[1]
        replacement = current_command[2]
        if substr in message:
            message = message.replace(substr, replacement)

    command = input()

print(f"The decrypted message is: {message}")
