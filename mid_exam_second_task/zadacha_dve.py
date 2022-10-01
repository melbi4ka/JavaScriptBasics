vehicle = input().split(">>")
agency_taxes = 0

for n in range(len(vehicle)):
    car_atributes = vehicle[n].split()
    car = car_atributes[0]
    years = int(car_atributes[1])
    km = int(car_atributes[2])
    if car == "family":
        if km > 3000:
            taxes = (km//3000) * 12 + (50 - (years * 5))
        else:
            taxes = 50 - (years * 5)

        print(f"A {car} car will pay {taxes:.2f} euros in taxes.")


    elif car == "heavyDuty":
        if km > 9000:
            taxes = (km // 9000) * 14 + (80 - (years * 8))
        else:
            taxes = 50 - (years * 8)

        print(f"A {car} car will pay {taxes:.2f} euros in taxes.")

    elif car == "sports":
        if km > 2000:
            taxes = (km // 2000) * 18 + (100 - (years * 9))
        else:
            taxes = 50 -(years * 9)

        print(f"A {car} car will pay {taxes:.2f} euros in taxes.")

    else:
        taxes = 0
        print ("Invalid car type.")

    agency_taxes += taxes


print(f"The National Revenue Agency will collect {agency_taxes:.2f} euros in taxes.")

# 70/100 не е нужна проверката дали са пробягали километрите







