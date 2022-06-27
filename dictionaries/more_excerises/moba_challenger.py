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
