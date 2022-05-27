items = input().split("|")
budget = float(input())

new_price_list = []
profit = 0
sum_new_prices = 0

for element in range(len(items)):
    curent_item = items[element].split("->")
    type_dress = curent_item[0]
    price = float(curent_item[1])
    is_valid = False
    if type_dress == "Clothes" and price <= 50:
        is_valid = True
    if type_dress == "Shoes" and price <= 35:
        is_valid = True
    if type_dress == "Accessories" and price <= 20.5:
        is_valid = True
    if is_valid:
        if budget >= price:
            budget -= price
            sum_new_prices += 1.4 * price
            new_price_as_str = (f"{1.4 * price:.2f}")
            new_price_list.append(new_price_as_str)
            profit += 0.4 * price

for price in range(len(new_price_list)):
    print(new_price_list[price], end=" ")
print()
print(f"Profit: {profit:.2f}")
if budget + sum_new_prices >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")








