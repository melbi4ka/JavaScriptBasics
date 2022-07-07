import re

line = input()

pattern = r"^>>([A-Za-z]+)<<(\d+\.?\d+)!(\d+)$"

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
