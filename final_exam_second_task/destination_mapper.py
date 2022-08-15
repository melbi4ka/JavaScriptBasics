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

# патърна - започва с равно или наклонена черта, която е ексейпната в група (=|\/)
# една главна буква и комбинация от малки и главни поне два пъти за да станат поне 3 символа в група ([A-Z][A-Za-z]{2,})
# завършва с това, което е мачнато в първа група \1
