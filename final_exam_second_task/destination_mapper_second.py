import re

pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
text = input()
matches = re.finditer(pattern, text)
cities_list = []

for match in matches:
    if match:
        cities_list.append(match.group(2))

travel_points = sum([len(el) for el in cities_list])

print(f"Destinations: {', '.join(cities_list)}")
print(f"Travel Points: {travel_points}")
