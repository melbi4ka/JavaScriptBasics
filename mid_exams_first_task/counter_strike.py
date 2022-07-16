initial_energy = int(input())
command = input()
count_battle = 0


while command != "End of battle":
    current_command = int(command)
    if current_command > initial_energy:
        print(f"Not enough energy! Game ends with {count_battle} won battles and {initial_energy} energy")
        break
    else:
        initial_energy -= current_command
        count_battle += 1
    if count_battle % 3 == 0:
        initial_energy += count_battle

    command = input()

if command == "End of battle":
    print(f"Won battles: {count_battle}. Energy left: {initial_energy}")
