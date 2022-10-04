number = int(input())

plant_dict = {}

for num in range(number):
    line = input().split("<->")
    plant = line[0]
    rarity = line[1]
    plant_dict[plant] = [rarity]

a_command = input()
while a_command != "Exhibition":
    command = a_command.split(": ")

    if command[0] == "Rate":
        plant, rating = command[1].split(" - ")
        if plant not in plant_dict:
            print("error")
        else:
            plant_dict[plant] += [rating]


    elif command[0] == "Update":
        plant, new_rarity = command[1].split(" - ")
        if plant not in plant_dict:
            print("error")
        else:
            plant_dict[plant][0] = new_rarity


    elif command[0] == "Reset":
        plant = command[1]
        if plant not in plant_dict:
            print("error")
        else:
            plant_dict[plant] = [plant_dict[plant][0]]

    a_command = input()

print(f"Plants for the exhibition:")
for key, value in plant_dict.items():
    if len(value) == 1:
        average_rating = 0
    else:
        average_rating = sum(map(int,value[1:])) / len(value[1:])


    print(f"- {key}; Rarity: {value[0]}; Rating: {average_rating:.2f}")



# print(plant_dict)


