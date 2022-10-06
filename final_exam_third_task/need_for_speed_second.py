number = int(input())

cars_dict = {}
for num in range(number):
    car, mileage, fuel = input().split("|")
    cars_dict[car] = {}
    cars_dict[car]["Mileage"] = int(mileage)
    cars_dict[car]["Fuel"] = int(fuel)

a_command = input()
while a_command != "Stop":
    command = a_command.split(" : ")
    action = command[0]
    car = command[1]

    if action == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if cars_dict[car]["Fuel"] >= fuel:
            cars_dict[car]["Fuel"] -= fuel
            cars_dict[car]["Mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars_dict[car]["Mileage"] >= 100000:
                print(f"Time to sell the {car}!")
                del cars_dict[car]
        else:
            print("Not enough fuel to make that ride")

    elif action == "Refuel":
        fuel = int(command[2])
        if cars_dict[car]["Fuel"] + fuel > 75:
            fuel = 75 - cars_dict[car]["Fuel"]
            cars_dict[car]["Fuel"] = 75
        else:
            cars_dict[car]["Fuel"] += fuel
        print(f"{car} refueled with {fuel} liters")

    elif action == "Revert":
        kilometers = int(command[2])
        if cars_dict[car]["Mileage"] - kilometers < 10000:
            cars_dict[car]["Mileage"] = 10000
        else:
            cars_dict[car]["Mileage"] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

    a_command = input()

for car,value in cars_dict.items():
    print(f"{car} -> Mileage: {value['Mileage']} kms, Fuel in the tank: {value['Fuel']} lt.")
