budget = float(input())
flour_price_per_kg = float(input())
breads_counter = 0
eggs_counter = 0

while True:
    price_per_bread = flour_price_per_kg + (flour_price_per_kg * 0.75) + (flour_price_per_kg * 1.25 / 4)
    if price_per_bread > budget:
        break
    budget -= price_per_bread
    breads_counter += 1
    eggs_counter += 3
    if breads_counter % 3 == 0:
        eggs_counter -= breads_counter - 2


print(f"You made {breads_counter} loaves of Easter bread! Now you have {eggs_counter} eggs and {budget:.2f}BGN left.")


