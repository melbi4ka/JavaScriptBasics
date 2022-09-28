pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health = int(input())
game_over = False


def is_valid(index, limit):
    return 0 <= index < limit


line = input().split()
while line[0] != 'Retire' and not game_over:
    command = line[0]
    if command == 'Fire':
        index = int(line[1])
        damage = int(line[2])
        if is_valid(index, len(warship)):
            warship[index] -= damage
            if warship[index] <= 0:
                print('You won! The enemy ship has sunken.')
                game_over = True
                break
    elif command == 'Defend':
        index1 = int(line[1])
        index2 = int(line[2])
        damage = int(line[3])
        if is_valid(index1, len(pirate_ship)) and is_valid(index2, len(pirate_ship)):
            for i in range(index1, index2 + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print('You lost! The pirate ship has sunken.')
                    game_over = True
                    break
    elif command == 'Repair':
        index = int(line[1])
        health = int(line[2])
        if is_valid(index, len(pirate_ship)):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health:
                pirate_ship[index] = max_health
    else:
        counter = 0
        for x in pirate_ship:
            if x < max_health * 0.2:
                counter += 1
        print(f'{counter} sections need repair.')

    line = input().split()
if not game_over:
    print(f'Pirate ship status: {sum(pirate_ship)}')
    print(f'Warship status: {sum(warship)}')