def add_car_dict():
    num = int(input())
    car_diction = {}

    for n in range(num):
        a_line = input()
        car, mileage, fuel = a_line.split("|")
        car_diction[car] = [int(mileage), int(fuel)]

    return car_diction


car_dict = add_car_dict()


command = input()
while command != "Stop":
    explode = command.split(" : ")
    if "Drive" in command:
        car = explode[1]
        distance = int(explode[2])
        fuel = int(explode[3])
        if car_dict[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            car_dict[car][1] -= fuel
            car_dict[car][0] += distance
        if car_dict[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            del car_dict[car]

    elif "Refuel" in command:
        car = explode[1]
        fuel = int(explode[2])
        if car_dict[car][1] + fuel >= 75:
            diff = 75 - car_dict[car][1]
            car_dict[car][1] = 75 # първо трябва да изпечатам диффа и после да сетна стойността, защото иначе бърка печата.
            print(f"{car} refueled with {diff} liters")
        else:
            car_dict[car][1] += fuel
            print(f"{car} refueled with {fuel} liters")

    elif "Revert" in command:
        car = explode[1]
        kilometers = int(explode[2])
        if car_dict[car][0] - kilometers <= 10000:
            car_dict[car][0] = 10000
        else:
            car_dict[car][0] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

sorted_car_dict = dict(sorted(car_dict.items(), key=lambda x: (-x[1][0], x[0])))
for car, car_adds in sorted_car_dict.items():
    print(f"{car} -> Mileage: {car_adds[0]} kms, Fuel in the tank: {car_adds[1]} lt.")

#print(sorted_dict)



