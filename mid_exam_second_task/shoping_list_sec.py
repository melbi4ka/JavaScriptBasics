grocery = input().split("!")
a_command = input()

while a_command != "Go Shopping!":
    command = a_command.split(" ")
    item = command[1]
    if command[0] == "Urgent":
        if item not in grocery:
            grocery.insert(0, item)

    elif command[0] == "Unnecessary":
        if item in grocery:
            grocery.remove(item)

    elif command[0] == "Correct":
        new_item = command[2]
        #if old_item in grocery:
        for i in range(len(grocery)):
            if grocery[i] == item:
                grocery[i] = new_item

    elif command[0] == "Rearrange":
        if item in grocery:
            grocery.remove(item)
            grocery.append(item)

    a_command = input()


print(", ".join(grocery))
