# def fire_warship (a_warship, a_idx, a_damage):
#     a_warship[a_idx] -= a_damage
#     if a_warship[a_idx] <= 0:
#         print("You won! The enemy ship has sunken.")
#
#     return a_warship

# def defend_pirateship(a_pirateship, a_start, a_final, a_damge):
#     for m in range (a_pirateship[a_start], a_pirateship[a_start] + 1):
#         m -= damage
#         if m <= 0:
#             break
#     print("You lost! The pirate ship has sunken.")
#     return a_pirateship

# def repair_pirateship(a_piratsh, a_index, a_health):
#     if a_piratsh[a_index] + a_health <= 70:
#         a_piratsh[a_index] += a_health
#     else:
#         a_piratsh[a_index] += 70 - a_piratsh[a_index]
#     return a_piratsh

def status_pirate (a_pirate):
    count = 0
    for n in a_pirate:
        if n < 70 * 0.8:
            count += 1
    return f"{count} sections need repair."


pirate_ship = [int(k) for k in input().split(">")]
warship = [int(s) for s in input().split(">")]
health_capacity = int(input())
command = input().split()

while command[0] != "Retire":
    action = command[0]
    if action == "Fire":
        idx = int(command[1])
        damage = int(command[2])
        if 0<= idx <= len(warship):
            warship = fire_warship(warship, idx, damage)

    elif action == "Defend":
        start_idx = int(command[1])
        final_idx = int(command[2])
        damage = int(command[3])
        if 0 <= start_idx <= len(pirate_ship) and 0 <= final_idx <= len(pirate_ship):
            pirate_ship = defend_pirateship(pirate_ship, start_idx, final_idx, damage)

    elif action == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index <= len(warship):
            pirate_ship = repair_pirateship(pirate_ship, index, health)

    elif action == "Status":
       print(status_pirate(pirate_ship))

    command = input().split()

print(pirate_ship)
print(warship)

# for n in pirate_ship:
#     for m in warship:
#         if m <= 0:
#             break
#         else:
#             sum_warship = sum(warship)
#         break
#
#     if n <= 0:
#         break
#     else:
#         sum_pirate = sum(pirate_ship)
#         print (f"Pirate ship status: {sum} \n Warship status: {sum_warship}")
#







