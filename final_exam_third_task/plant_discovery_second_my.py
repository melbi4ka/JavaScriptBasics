number = int(input())
plant_dict = {}

for n in range(number):
    line = input().split("<->")
    plant = line[0]
    rarity = int(line[1])
    plant_dict[plant] = [rarity]

command = input()
while command != "Exhibition":
    explode = command.split(": ")
    if explode[0] == "Rate":
        new_explode = explode[1].split(" - ")
        plants = new_explode[0]
        rating = int(new_explode[1])
        if plants in plant_dict:
            plant_dict[plants].append(rating)
        else:
            print("error")

    elif explode[0] == "Update":
        new_explode = explode[1].split(" - ")
        plants = new_explode[0]
        new_rarity = int(new_explode[1])
        if plants in plant_dict:
            plant_dict[plants][0] = new_rarity
        else:
            print("error")

    elif explode[0] == "Reset":
        plants = explode[1]
        if plants in plant_dict:
            del plant_dict[plants][1:]
            #plant_dict[plants].append(0)
            # трябва само да изтривам рейтинга, без да добавям нулев. нулевия го добавям в цикъла, защото два пъти мога да имам ресет
        else:
            print("error")

    command = input()

for key, value in plant_dict.items():
    item_to_amend = value[1:]
    remaining_part = value[0]
    if len(item_to_amend) > 1:
        total = sum(item_to_amend)
        new_num = total / len(item_to_amend)
        value.clear()
        value.append(remaining_part)
        value.append(new_num)
    if len(value) == 1:
        value.append(0)


sorted_plants = dict(sorted(plant_dict.items(), key=lambda x: (-x[1][0], -x[1][1])))
print(f"Plants for the exhibition:")
for key, value in sorted_plants.items():
    print(f"- {key}; Rarity: {value[0]:}; Rating: {value[1]:.2f}")
