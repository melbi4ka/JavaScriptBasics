pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
maximum_health = int(input())
is_sunken = False

while True:
    command = input().split()
    if command[0] == "Retire":
        break

    if command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if len(warship) > index >= 0:
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                is_sunken = True
                break
        if is_sunken:
            break

    elif command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship) and damage > 0:
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_sunken = True
                    break
            if is_sunken:
                break
        if is_sunken:
            break

    elif command[0] == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(pirate_ship) and health > 0:
            pirate_ship[index] += health
            if pirate_ship[index] > maximum_health:
                pirate_ship[index] = maximum_health

    elif command[0] == "Status":
        counter_for_repair = 0
    low_health = maximum_health * 0.20
    for section in pirate_ship:
        if section < low_health:
            counter_for_repair += 1
    print(f"{counter_for_repair} sections need repair.")

if not is_sunken:
    pirate_ship_sum = sum(pirate_ship)
    warship_sum = sum(warship)

    print(f"Pirate ship status: {pirate_ship_sum}")
    print(f"Warship status: {warship_sum}")