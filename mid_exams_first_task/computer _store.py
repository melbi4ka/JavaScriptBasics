comand = input()
price_sum = 0

while comand != "special" and comand != "regular":
    # когато е различно от двете заедно е true, когато едното е вярно, а другото не е false и не влиза в цикъла
    current_comand = float(comand)

    if current_comand < 0:
        print("Invalid price!")
    else:
          price_sum += current_comand

    comand = input()


taxes = 0.2 * price_sum
total_price = price_sum + taxes
discount_total_price = 0.9 * total_price

if total_price == 0:
    print("Invalid order!")
else:
    if comand == "special":
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {price_sum:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {discount_total_price:.2f}$")
    else:
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {price_sum:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {total_price:.2f}$")









