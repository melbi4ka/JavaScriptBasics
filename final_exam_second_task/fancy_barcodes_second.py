import re

pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"

number = int(input())
for _ in range(number):
    text = input()
    match = re.search(pattern, text)
    if match:
        barcode = match.group(1)
        barcode_group = ""
        for char in barcode:
            if char.isdigit():
                barcode_group += char
        if barcode_group == "":
            barcode_group = "00"
        print(f"Product group: {barcode_group}")

    else:
        print("Invalid barcode")
