number = int(input())

car_dict = {}

for n in range(number):
    line = input().split()
    command = line[0]
    username = line[1]
    if command == "register":
        plate = line[2]
        if username not in car_dict:
            car_dict[username] = plate
            print(f"{username} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")
    elif command == "unregister":
        if username not in car_dict:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del car_dict[username]

for key, value in car_dict.items():
    print(f"{key} => {value}")



