group_size = int(input())
days = int(input())
money_counter = 0

for day in range(1, days+1):

    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5

    money_counter += 50 - (2 * group_size)

    if day % 3 == 0:
        money_counter -= 3 * group_size
    if day % 5 == 0:
        money_counter += 20 * group_size
        if day % 3 == 0:
            money_counter -= 2 * group_size


money_per_person = int(money_counter/group_size)
print(f"{group_size} companions received {money_per_person} coins each.")





