import re

pattern = r"%(?P<name>[A-Z][a-z]+)%[^\|\$\%\.]*?\<(?P<product>\w+)\>[^\|\$\%\.]*?\|(?P<count>\d+)\|[^\|\$\%\.]*?(?P<price>0|[0-9]+[\.0-9]*)\$"

line = input()
income = 0

while line != "end of shift":
    matches = re.finditer(pattern, line)
    for match in matches:
        if match:
            name = match.group("name")
            product = match.group("product")
            count = match.group("count")
            price = match.group("price")
            total_price = float(price) * int(count)
            income += total_price
            print(f"{name}: {product} - {total_price:.2f}")

    line = input()

print(f"Total income: {income:.2f}")
