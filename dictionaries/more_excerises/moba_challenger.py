a_command = input()
players_dict = {}

while a_command != "Season end":
    if "->" in a_command:
        player, position, skill = a_command.split(" -> ")
        skill = int(skill)

        if player not in players_dict:
            players_dict[player] = {position : skill}
        elif player in players_dict:
            if position not in players_dict[player]:
                players_dict[player][position] = skill
            elif position in players_dict[player]:
                if players_dict[player][position] < skill:
                    players_dict[player][position] = skill



    elif "vs" in a_command:
        player_one, player_two = a_command.split(" vs ")

    a_command = input()


print(players_dict.items())
players = players_dict

for n in players_dict.values():
    print(sum(n.values()))



# for key, val in players_dict.items():
#     print(key)
#     print(val.items())
#     # sorted_val = sorted(val.items(), key = lambda kvpt: sum(kvpt[1]))
#     # print(sorted_val)
#     # print(sum(val.values()))







# for key, value in players_dict.items():
#     sum = 0
#     for val in value.values():
#         sum += val
#     print(f"{key}: {sum} skill")
#     for n in value:
#         print(f"- {n} <::> {value[n]}")
#
# print(players_dict.items())
# sorted_players = sorted(players_dict.items(), key = lambda kvpt: kvpt[1])
# print(sorted_players)


# {'Peter': {'Adc': 400, 'all': ...}, 'George': {'Jungle': 300, 'all': ...}, 'Simon': {'Mid': 200, 'Support': 250, 'all': .. }}
