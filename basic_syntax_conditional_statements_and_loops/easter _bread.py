budget = float(input())
kg_flour_price = float(input())

one_pack_egg = 0.75 * kg_flour_price
one_litter_milk = 1.25 * kg_flour_price
price_per_one_bread = 1 * kg_flour_price + 1 * one_pack_egg + one_litter_milk / 4

bread_counter = 0
colored_eggs = 0

while budget >= price_per_one_bread:
    bread_counter += 1
    colored_eggs += 3
    if bread_counter % 3 == 0:
        colored_eggs -= bread_counter - 2

    budget -= price_per_one_bread


print(f"You made {bread_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")











