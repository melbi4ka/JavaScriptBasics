a_line = input()
towns_dict = {}

while a_line != "Sail":
    town, population,gold = a_line.split("||")
    if town not in towns_dict:
        towns_dict[town] = {"population": int(population), "gold": int(gold)}
    else:
        towns_dict[town]["population"] += int(population)
        towns_dict[town]["gold"] += int(gold)

    a_line = input()


a_command = input()
while a_command != "End":
    command = a_command.split("=>")
    action = command[0]

    if action == "Plunder":
        town, people, gold = command[1:]
        people = int(people)
        gold = int(gold)

        towns_dict[town]["population"] -= people
        towns_dict[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if towns_dict[town]["population"] <= 0 or towns_dict[town]["gold"] <= 0:
            print(f"{town} has been wiped off the map!")
            del towns_dict[town]

    elif action == "Prosper":
        town,gold = command[1:]
        gold = int(gold)

        if gold <= 0:
            print(f"Gold added cannot be a negative number!")
        else:
            towns_dict[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {towns_dict[town]['gold']} gold.")

    a_command = input()
if len(towns_dict) > 0:
    print(f"Ahoy, Captain! There are {len(towns_dict)} wealthy settlements to go to:")
    for key, value in towns_dict.items():
        print(f"{key} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")

else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")

