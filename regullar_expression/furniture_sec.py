import re

line = input()

pattern = r"^>>([A-Za-z]+)<<(\d+\.?\d+)!(\d+)$"

furniture_list = []
total_price = 0

while line != "Purchase":
    matches = re.search(pattern, line)
    if matches:
        furniture, price, quantity = matches.groups()
        furniture_list.append(furniture)
        total_price += float(price) * float(quantity)

    line = input()

print("Bought furniture:")
if len(furniture_list) > 0:
    print(*furniture_list, sep="\n")
print(f"Total money spend: {total_price:.2f}")

# букви в низ, цифри в низ, точка 0 или 1 пъти(може да  я има, може да я няма), цифри в низ, цифри в низ за количество
