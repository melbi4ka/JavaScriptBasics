targets = [int(s) for s in input().split()]
command = input().split()

while command[0] != "End":
    idx = int(command[1])
    value = int(command[2])
    if command[0] == "Shoot":
        if 0 <= idx < len(targets):
            targets[idx] -= value
            if targets[idx] <= 0:
                targets.pop(idx)
    elif command[0] == "Add":
        if 0 <= idx < len(targets):
            targets.insert(idx, value)
        else:
            print("Invalid placement!")
    elif command[0] == "Strike":
        if 0 + value < idx + value < len(targets):
            targets = targets[0:idx-value] + targets[(idx + value+1)::]
        else:
            print("Strike missed!")

    command = input().split()

print("|".join(str(s) for s in targets))


