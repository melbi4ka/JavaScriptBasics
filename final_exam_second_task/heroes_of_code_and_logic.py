def add_hero_dict():
    num = int(input())
    hero_diction = {}

    for n in range(num):
        a_line = input()
        hero_name, hpoints, mpoints = a_line.split()
        if hero_name not in hero_diction:
            hero_diction[hero_name] = [int(hpoints), int(mpoints)]
            if int(hpoints) > 100:
                hero_diction[hero_name][0] = 100
            elif int(mpoints) > 200:
                hero_diction[hero_name][1] = 200

    return hero_diction


hero_dict = add_hero_dict()


line = input().split(" - ")
while line[0] != "End":
    hero_name = line[1]

    if "CastSpell" in line:
        mp_needed = int(line[2])
        spell_name = line[3]
        if hero_dict[hero_name][1] >= mp_needed:
            diff = hero_dict[hero_name][1] - mp_needed
            hero_dict[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {diff} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif "TakeDamage" in line:
        damage = int(line[2])
        attacker = line[3]
        diff = hero_dict[hero_name][0] - damage
        if hero_dict[hero_name][0] - damage > 0:
            hero_dict[hero_name][0] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {diff} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del hero_dict[hero_name]

    elif "Recharge" in line:
        amount = int(line[2])
        if hero_dict[hero_name][1] + amount > 200:
            diff = 200 - hero_dict[hero_name][1]
            hero_dict[hero_name][1] = 200
            print(f"{hero_name} recharged for {diff} MP!")
        else:
            hero_dict[hero_name][1] += amount
            print(f"{hero_name} recharged for {amount} MP!")

    elif "Heal" in line:
        amount = int(line[2])
        if hero_dict[hero_name][0] + amount > 100:
            diff = 100 - hero_dict[hero_name][0]
            hero_dict[hero_name][0] = 100
            print(f"{hero_name} healed for {diff} HP!")
        else:
            hero_dict[hero_name][0] += amount
            print(f"{hero_name} healed for {amount} HP!")


    line = input().split(" - ")

for name, value in hero_dict.items():
    print(f"{name}")
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")

#print(hero_dict)


