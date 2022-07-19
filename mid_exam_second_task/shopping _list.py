grocery = input().split("!")
command = input().split()

while command[0] != "Go" and command[1] != "Shopping!":
    #command = input().split(" ")
    if command[0] == "Urgent":
        item = command[1]
        if item not in grocery:
            grocery.insert(0, item)

    elif command[0] == "Unnecessary":
        item = command[1]
        if item in grocery:
            grocery.remove(item)

    elif command[0] == "Correct":
        old_item = command[1]
        new_item = command[2]
        #if old_item in grocery:
        for i in range(len(grocery)):
            if grocery[i] == old_item:
                grocery[i] = new_item

    elif command[0] == "Rearrange":
        item = command[1]
        if item in grocery:
            grocery.remove(item)
            grocery.append(item)


    command = input().split()


print(", ".join(grocery))




