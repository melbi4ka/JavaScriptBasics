text = input()
a_command = input()

while a_command != "Generate":
    command = a_command.split(">>>")
    action = command[0]

    if action == "Contains":
        substring = command[1]
        if substring in text:
            print(f"{text} contains {substring}")
        else:
            print("Substring not found!")

    elif action == "Flip":
        sub_action = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        if sub_action == "Upper":
            add_text = text[start_index : end_index].upper()
        elif sub_action == "Lower":
            add_text = text[start_index : end_index].lower()

        text = text[:start_index] + add_text + text[end_index : ]
        print(text)

    elif action == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        text = text[:start_index] + text[end_index :]
        print(text)

    a_command = input()

print(f"Your activation key is: {text}")


