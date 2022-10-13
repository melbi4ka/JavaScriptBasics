import re

some_string = input()

key_list = []

for i in some_string:
    if i.isdigit() or i.isalpha():
        key_list.append(i)
    else:
        key_list.extend(f"\\{i}")

key = "".join(key_list)

command = input()

result_dict = {}
goal_dict = {}

while command != "final":

    command = command
    pattern = fr"{key}([A-Za-z]*){key}"
    matches = re.findall(pattern, command)
    # print(matches)

    teams = []

    for rev_team in matches:
        team = rev_team[::-1].upper()
        teams.append(team)
        if team not in result_dict:
            result_dict[team] = 0

    pattern_for_result = r"(\d+)\:(\d+)"
    results = re.finditer(pattern_for_result, command)

    game_result = 0
    for res in results:
        game_result = res.group()
        # print(res.group())

    for team in range(len(teams)):
        if team == 0:

            if int(game_result[0]) == int(game_result[2]):
                if teams[team] in result_dict:
                    result_dict[teams[team]] += 1
            elif int(game_result[0]) > int(game_result[2]):
                if teams[team] in result_dict:
                    result_dict[teams[team]] += 3
            elif int(game_result[0]) < int(game_result[2]):
                if teams[team] in result_dict:
                    result_dict[teams[team]] += 0
            if teams[team] not in goal_dict:
                goal_dict[teams[team]] = int(game_result[0])
            else:
                goal_dict[teams[team]] += int(game_result[0])

        elif team == 1:
            if int(game_result[0]) == int(game_result[2]):
                if teams[team] in result_dict:
                    result_dict[teams[team]] += 1
            elif int(game_result[0]) < int(game_result[2]):
                if teams[team] in result_dict:
                    result_dict[teams[team]] += 3
            elif int(game_result[0]) > int(game_result[2]):
                if teams[team] in result_dict:
                    result_dict[teams[team]] += 0
            if teams[team] not in goal_dict:
                goal_dict[teams[team]] = int(game_result[2])
            else:
                goal_dict[teams[team]] += int(game_result[2])


    command = input()

sorted_result = sorted(result_dict.items(), key=lambda kvpt: (-kvpt[1], kvpt[0]))
print("League standings:")
n = 0
for team, points in sorted_result:
    n += 1
    print(f"{n}. {team} {points}")


sorted_goals = sorted(goal_dict.items(),key=lambda kvpt: (-kvpt[1], kvpt[0]))
print("Top 3 scored goals:")
m = 0
for team, goals in sorted_goals:
    m += 1
    print(f"- {team} -> {goals}")
    if m == 3:
        break

        
