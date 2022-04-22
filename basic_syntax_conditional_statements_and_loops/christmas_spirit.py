allowed_quantity = int(input())
days_to_christmas = int(input())


ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

costs = 0
christmas_spirit = 0
for current_day in range (1, days_to_christmas + 1):
    if current_day % 11 == 0:
        allowed_quantity += 2
    if current_day % 2 == 0:
        costs += ornament_set * allowed_quantity
        christmas_spirit += 5
    if current_day % 3 == 0:
        costs += (tree_skirt + tree_garlands) * allowed_quantity
        christmas_spirit += 13
    if current_day % 5 == 0:
        costs += tree_lights * allowed_quantity
        christmas_spirit += 17
        if current_day % 3 == 0:
            christmas_spirit += 30
    if current_day % 10 == 0:
        christmas_spirit -= 20
        costs += tree_skirt + tree_garlands + tree_lights

if days_to_christmas % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {costs}")
print(f"Total spirit: {christmas_spirit}")

