rooms = input().split("|")
health = 100
bitcoins = 0
counter_room = 0

for room in rooms:
    new_room = room.split()
    action = new_room[0]
    number = int(new_room[1])
    counter_room += 1
    if action == "potion":
        if number + health < 100:
            print(f"You healed for {number} hp.")
            health += number
        else:
            diff = abs(100 - health)
            health += diff
            print(f"You healed for {diff} hp.")
        print(f"Current health: {health} hp.")
    elif action == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        if health - number <= 0:

            print(f"You died! Killed by {action}.")
            print(f"Best room: {counter_room}")
            health -= number
            break
        else:
            health -= number
            print(f"You slayed {action}.")


if health > 0:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")











