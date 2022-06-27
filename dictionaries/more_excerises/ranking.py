a_command = input()
contest_dict = {}
users_dict = {}

while a_command != "end of contests":
    contest, password = a_command.split(":")
    contest_dict[contest] = password

    a_command = input()

b_command = input()
while b_command != "end of submissions":
    contest, current_password, username, points = b_command.split("=>")
    points = int(points)
    if contest in contest_dict and contest_dict[contest] == current_password:

        if username not in users_dict:
            users_dict[username] = {}

        if contest not in users_dict[username]:
            users_dict[username][contest] = points
        else:
            if users_dict[username][contest] < points:
                users_dict[username][contest] = points

    b_command = input()

best_player = ""
total_points = 0

for name in users_dict:
    total_sum = sum(users_dict[name].values())
    if total_sum > total_points:
        total_points = total_sum
        best_player = name

print(f"Best candidate is {best_player} with total {total_points} points.")

print("Ranking:")
sorted_users_dict = sorted(users_dict.items(), key = lambda kvpt: kvpt[0])
for key, value in sorted_users_dict:
    print(key)
    sorted_value = sorted(value.items(), key = lambda kvpt: -kvpt[1])
    for val in sorted_value:
        print(f"#  {val[0]} -> {val[1]}")
