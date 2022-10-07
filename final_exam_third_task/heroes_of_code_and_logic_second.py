number = int(input())
heroes_dict = {}

for _ in range(number):
    name, hp, mp = input().split()
    hp,mp = int(hp),int(mp)
    if name not in heroes_dict:
        heroes_dict[name] = {"HP": hp, "MP": mp}
        if heroes_dict[name]["HP"] > 100:
            heroes_dict[name]["HP"] = 100
        if heroes_dict[name]["MP"] > 200:
            heroes_dict[name]["MP"] = 200


a_command = input()
while a_command != "End":
    command = a_command.split(" - ")
    action = command[0]
    hero_name = command[1]

    if action == "Heal":
        amount = int(command[2])
        if heroes_dict[hero_name]["HP"] + amount > 100:
            diff = 100 - heroes_dict[hero_name]["HP"]
            heroes_dict[hero_name]["HP"] = 100
        else:
            diff = amount
            heroes_dict[hero_name]["HP"] += amount
        print(f"{hero_name} healed for {diff} HP!")

    elif action == "Recharge":
        amount = int(command[2])
        if heroes_dict[hero_name]["MP"] + amount > 200:
            diff = 200 - heroes_dict[hero_name]["MP"]
            heroes_dict[hero_name]["MP"] = 200
        else:
            heroes_dict[hero_name]["MP"] += amount
            diff = amount

        print(f"{hero_name} recharged for {diff} MP!")

    elif action == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        diff = heroes_dict[hero_name]["HP"] - damage
        heroes_dict[hero_name]["HP"] -= damage
        if diff > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {diff} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes_dict[hero_name]

    elif action == "CastSpell":
        mp_needed = int(command[2])
        spell_name = command[3]
        if heroes_dict[hero_name]["MP"] >= mp_needed:
            diff = heroes_dict[hero_name]["MP"] - mp_needed
            heroes_dict[hero_name]["MP"] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {diff} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    a_command = input()

for key, value in heroes_dict.items():
    print(f"{key}")
    print(f"  HP: {value['HP']}")
    print(f"  MP: {value['MP']}")







