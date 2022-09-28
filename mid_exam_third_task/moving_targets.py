def is_valid(a_index, a_target):
    if 0 <= a_index < len(a_target):
        return True
    return False

def shoot_target(a_targets, a_idx, a_value):
    a_targets[a_idx] -= a_value
    if a_targets[a_idx] <= 0:
        a_targets.pop(a_idx)
    return a_targets

def add_targets(a_targets, a_idx, a_value):
    a_targets.insert(a_idx, a_value)
    return a_targets

def strike_targets(a_targets, a_idx, a_value):
    a_targets = a_targets[0:a_idx - a_value] + a_targets[(a_idx+a_value + 1)::]
    return a_targets


targets = list(map(int, input().split()))
command = input().split()

while command[0] != "End":
    idx = int(command[1])
    value = int(command[2])
    if command[0] == "Shoot":
        if is_valid(idx, targets):
            targets = shoot_target(targets, idx, value)

    elif command[0] == "Add":
        if is_valid(idx, targets):
            targets = add_targets(targets, idx, value)
        else:
            print("Invalid placement!")

    elif command[0] == "Strike":
        if 0 + value < idx + value < len(targets):
            targets = strike_targets(targets, idx, value)
        else:
            print("Strike missed!")

    command = input().split()

print("|".join(list(map(str, targets))))
