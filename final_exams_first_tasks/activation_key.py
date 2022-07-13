raw_key = input()
a_command = input()

while a_command != "Generate":
    command = a_command.split(">>>")
    if command[0] == "Contains":
        substring = command[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")

    if command[0] == "Flip":
        start_index = int(command[2])
        final_index = int(command[3])
        if command[1] == "Upper":
            upper_subs = raw_key[start_index:final_index].upper()
            raw_key = raw_key[0:start_index] + upper_subs + raw_key[final_index::]
            print(raw_key)
        elif command[1] == "Lower":
            lower_subs = raw_key[start_index:final_index].lower()
            raw_key = raw_key[:start_index] + lower_subs + raw_key[final_index::]
            print(raw_key)

    if command[0] == "Slice":
        start_idx = int(command[1])
        final_idx = int(command[2])
        raw_key= raw_key[0:start_idx] + raw_key[final_idx::]
        print(raw_key)

    a_command = input()

print(f"Your activation key is: {raw_key}")
