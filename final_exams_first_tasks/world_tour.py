stops = input()
a_command = input()

while a_command != "Travel":
    command = a_command.split(":")
    if command[0] == "Add Stop":
        idx = int(command[1])
        strng = command[2]
        if 0 <= idx < len(stops):
            stops = stops[0:idx] + strng + stops[idx::]
        print(stops)

    if command[0] == "Remove Stop":
        start_idx = int(command[1])
        final_idx = int(command[2])
        if 0 <= start_idx < len(stops) and 0 <= final_idx < len(stops):
            stops = stops[0:start_idx] + stops[final_idx+1::]
        print(stops)

    if command[0] == "Switch":
        old_str = command[1]
        new_str = command[2]
        if old_str in stops:
            stops = stops.replace(old_str, new_str)
        print(stops)


    a_command = input()

print(f"Ready for world tour! Planned stops: {stops}")
