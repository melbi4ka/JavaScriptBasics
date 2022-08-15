import re

pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
text = input()

result = re.finditer(pattern, text)
destinations_list = []
travel_points = 0

for res in result:
    if res:
        destinations_list.append(res.group(2))
        travel_points += len(res.group(2))

print(f"Destinations: {', '.join(destinations_list)}")
print(f"Travel Points: {travel_points}")
