items = input().split(", ")
new_command = input()

while new_command != "Craft!":
    command = new_command.split(" - ")
    item = command[1]

    if command[0] == "Collect":
        if item not in items:
            items.append(item)

    if command[0] == "Drop":
        if item in items:
            items.remove(item)

    if command[0] == "Combine Items":
        new_items = item.split(":")
        old_item = new_items[0]
        new_item = new_items[1]
        if old_item in items:
            items.insert(items.index(old_item)+1, new_item)

    if command[0] == "Renew":
        if item in items:
            items.append(item)
            items.remove(item)

    new_command = input()

print(", ".join(items))
