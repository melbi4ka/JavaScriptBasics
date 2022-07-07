import re

line = input()

pattern = r"^>>([A-Za-z]+)<<(\d+\.?\d+)!(\d+)$"
# букви в низ, цифри в низ, точка 0 или 1 пъти(може да  я има, може да я няма), цифри в низ, цифри в низ за количество
furniture = []
total_price = 0

while line != "Purchase":
    matches = re.findall(pattern, line)
    if matches:
        furniture.append(matches[0][0])
        total_price += float(matches[0][1]) * float(matches[0][2])

    line = input()

print("Bought furniture:")
if len(furniture) > 0:
    print(*furniture, sep="\n")
print(f"Total money spend: {total_price:.2f}")

# pattern = r"^>>([a-zA-Z]+)<<([0-9]+[\.0-9]*)!([0-9]+)$"
# pattern = r"^>>([A-Za-z]+)<<(\d+[\.\d]*)!(\d+)$"
#  тези патърни не са много точни, тъй като мачват и цена като 0.56.56, което не е валидна цена