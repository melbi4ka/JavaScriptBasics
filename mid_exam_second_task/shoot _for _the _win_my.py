targets = list(map(int, input().split()))
command = input()
shot_target = 0

while command != "End":
    index = int(command)
    if index in range(len(targets)):
        current_target = targets[index]
        targets[index] = -1
        for n in range(len(targets)):
            if targets[n] != -1:
                if targets[n] > current_target:
                    targets[n] -= current_target
                else:
                    targets[n] += current_target
        #current_target = -1
        shot_target += 1
    command = input()


print(f"Shot targets: {shot_target} -> {' '. join(map(str, targets))}")

















#print(int_targets)

