line = input()
orders_dict = {}

while line != "buy":
    explode = line.split()
    product = explode[0]
    price = float(explode[1])
    quantity = int(explode[2])
    if product not in orders_dict:
        orders_dict[product] = []
        orders_dict[product].append(price)
        orders_dict[product].append(quantity)
    else:
        orders_dict[product][0] = price
        orders_dict[product][1] += quantity

    line = input()

for key, values in orders_dict.items():
    result = values[0] * values[1]
    print(f"{key} -> {result:.2f}")

#print(orders_dict)




