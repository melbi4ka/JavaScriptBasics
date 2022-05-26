events = input().split("|")
energy = 100
coins = 100
is_closed = False

for numbers in range(len(events)):
    current_event = events[numbers].split("-")
    action = current_event[0]
    value = int(current_event[1])
    if action == "rest":
        if energy + value > 100:
            print("You gained 0 energy.")
        else:
            energy += value
            print(f"You gained {value} energy.")
        print(f"Current energy: {energy}.")
    elif action == "order":
        if energy - 30 >= 0:
            print(f"You earned {value} coins.")
            coins += value
            energy -= 30
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins - value > 0:
            coins -= value
            print(f"You bought {action}.")
        else:
            is_closed = True
            print(f"Closed! Cannot afford {action}.")
            break

if not is_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
