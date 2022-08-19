def add_towns_dict():
    command = input()
    towns_dict = {}
    while command != "Sail":
        exploding = command.split("||")
        cities = exploding[0]
        population = int(exploding[1])
        gold = int(exploding[2])
        if cities not in towns_dict:
            towns_dict[cities] = [population, gold]
        else:
            towns_dict[cities][0] += population
            towns_dict[cities][1] += gold
        command = input()
    return towns_dict


cities_dict = add_towns_dict()
# print(cities_dict)

line = input()
while line != "End":
    explode = line.split("=>")
    town = explode[1]

    if explode[0] == "Plunder":
        citizens = int(explode[2])
        gold_amount = int(explode[3])

        cities_dict[town][0] -= citizens
        cities_dict[town][1] -= gold_amount
        print (f"{town} plundered! {gold_amount} gold stolen, {citizens} citizens killed.")
        if cities_dict[town][0] <= 0 or cities_dict[town][1] <= 0:
            print(f"{town} has been wiped off the map!")
            del cities_dict[town]

    if explode[0] == "Prosper":
        gold_amount = int(explode[2])
        if gold_amount < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            cities_dict[town][1] += gold_amount
            print(f"{gold_amount} gold added to the city treasury. {town} now has {cities_dict[town][1]} gold.")

    line = input()
print(f"Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:")
for town, additions in cities_dict.items():
    print(f"{town} -> Population: {additions[0]} citizens, Gold: {additions[1]} kg")
