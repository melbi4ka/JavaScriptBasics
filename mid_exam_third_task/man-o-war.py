pirate_ship = [int(k) for k in input().split(">")]
warship = [int(s) for s in input().split(">")]
health_capacity = int(input())
command = input().split()
is_sunk = False


while command[0] != "Retire":
    action = command[0]
    if action == "Fire":
        idx = int(command[1])
        damage = int(command[2])
        if 0 <= idx < len(warship):
            warship[idx] -= damage
            if warship[idx] <= 0:
                #is_sunk = True
                print("You won! The enemy ship has sunken.")
                is_sunk = True
                break

    elif action == "Defend":
        start_idx = int(command[1])
        final_idx = int(command[2])
        damage = int(command[3])
        if 0 <= start_idx < len(pirate_ship) and 0 <= final_idx < len(pirate_ship):
            for m in range(start_idx, final_idx + 1):
                pirate_ship[m] -= damage
                if pirate_ship[m] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_sunk = True
                    break

    elif action == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(pirate_ship):
            if pirate_ship[index] + health <= health_capacity:
                pirate_ship[index] += health
            else:
                pirate_ship[index] = health_capacity

    elif action == "Status":
        count = 0
        for n in pirate_ship:
            if n < health_capacity * 0.2:
                count += 1
        print(f"{count} sections need repair.")

    command = input().split()

sum_warship = sum(warship)
sum_pirate = sum(pirate_ship)

if not is_sunk:
    print(f"Pirate ship status: {sum_pirate}\nWarship status: {sum_warship}")
