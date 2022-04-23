number_of_orders = int(input())
order_price = 0
total_price = 0

for nums in range(1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsule_count = int(input())

    order_price = days * price_per_capsule * capsule_count

    print(f"The price for the coffee is: ${order_price:.2f}")

    total_price += order_price

print(f"Total: ${total_price:.2f}")

