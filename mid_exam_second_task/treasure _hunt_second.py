initial_tresure = input().split("|")
command = input().split()
sum_items = 0


while command[0] != "Yohoho!":
    #command = input().split(" ")
    if command[0] == "Loot":
        for i in range(1, len(command)):
            item = command[i]
            if item not in initial_tresure:
                initial_tresure.insert(0, item)

    elif command[0] == "Drop":
        idx = int(command[1])
        if 0 <= idx < len(initial_tresure):
            new = initial_tresure.pop(idx)
            initial_tresure.append(new)

    elif command[0] == "Steal":
        num = int(command[1])
        if num >= len(initial_tresure):
            removed = initial_tresure
            print(', '.join(removed))
            print('Failed treasure hunt.')
            initial_tresure.clear()
            break 
        else:
            removed = initial_tresure[-num:]
            del initial_tresure[-num:]
            print(', '.join(removed))

    command = input().split()

if len(initial_tresure) > 0:
    for i in range(len(initial_tresure)):
        sum_items += len(initial_tresure[i])

    avg = sum_items/len(initial_tresure)
    print(f'Average treasure gain: {avg:.2f} pirate credits.')




#    command = input()
#print(initial_tresure)












