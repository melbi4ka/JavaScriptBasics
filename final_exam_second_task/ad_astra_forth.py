import re

pattern = r"(#|\|)(?P<product>[A-Za-z ]+)\1(?P<date>\d{2}\/\d{2}\/\d{2})\1(?P<callories>\d{1,5})\1"

text = input()

matches = re.finditer(pattern, text)
total_kcal = 0
product_dict = {}
n = 1

for match in matches:
    if match:
        product = match.group("product")
        date = match.group("date")
        callories = match.group("callories")
        total_kcal += int(callories)
        product_dict[n] = {"product": product, "date" : date, "kcal" : callories}
        n += 1

days_per_total_kcal = total_kcal // 2000

print(f"You have food to last you for: {days_per_total_kcal} days!")
if len(product_dict) > 0:
    for value in product_dict.values():
           print(f"Item: {value['product']}, Best before: {value['date']}, Nutrition: {value['kcal']}")
