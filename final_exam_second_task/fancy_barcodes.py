import re

pattern = r"@[#]+([A-Z][A-Za-z0-9]{4,}[A-Z])@[#]+"


number = int(input())
for num in range (number):
    text = input()
    match = re.findall(pattern,text)
    group = ""

    if match:
        word = "".join(match)
        if word.isalpha():
            print("Product group: 00")
        else:
            for char in word:
                if char.isdigit():
                    group += char
            print(f"Product group: {group}")
    else:
        print(f"Invalid barcode")
