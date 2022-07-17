quantity_food_kg = float(input()) * 1000
quantity_hay_kg = float(input()) * 1000
quantity_cover_kg = float(input()) * 1000
guinea_weight_kg = float(input()) * 1000
is_enough = True

for days in range(1, 31):
    quantity_food_kg -= 300
    if days % 2 == 0:
        quantity_hay_kg -= 0.05 * quantity_food_kg
    if days % 3 == 0:
        quantity_cover_kg -= (1/3) * guinea_weight_kg

    if quantity_food_kg == 0 or quantity_hay_kg == 0 or quantity_cover_kg == 0:
        break


if quantity_food_kg > 0 and quantity_cover_kg > 0 and quantity_hay_kg > 0:
    quantity_food_kg /= 1000
    quantity_hay_kg /= 1000
    quantity_cover_kg /= 1000
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food_kg:.2f}, "
          f"Hay: {quantity_hay_kg:.2f}, Cover: {quantity_cover_kg:.2f}.")
else:
    print("Merry must go to the pet store!")
