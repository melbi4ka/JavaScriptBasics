message = input()
message_as_list = list(message)
command = input()

while command != "Decode":
    current_command = command.split("|")
    action = current_command[0]
    if action == "Move":
        idx = int(current_command[1])
        for n in range(0, idx):
            move_letter = message_as_list[n]
            message_as_list.append(move_letter)
        del message_as_list[:idx]

    if action == "Insert":
        idx = int(current_command[1])
        value = current_command[2]
        if idx >= 0:
            message_as_list = message_as_list[0:idx] + (list(value)) + message_as_list[idx::]


    if action == "ChangeAll":
        substr = current_command[1]
        replacement = current_command[2]
        for n in range (len(message_as_list)):
            if message_as_list[n] == substr:
                message_as_list[n] = replacement

    command = input()

print(f"The decrypted message is: {''.join(message_as_list)}")
