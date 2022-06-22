command = input()

resource_dict = {}

while command != "stop":
    key = command
    command_two = int(input())

    if key not in resource_dict:
        resource_dict[key] = 0
    resource_dict[key] += command_two

    command = input()

for key, value in resource_dict.items():
    print(f"{key} -> {value}")

    
