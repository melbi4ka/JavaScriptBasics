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

# патърна - @[#]+ започва с кльомба и има хаштаг повече от веднъж
# група ([A-Z][A-Za-z0-9]{4,}[A-Z]) - започва с главна буква, после има главни, малки и цифри от 4 бр. нагоре, завършва с главна буква
# за да станат символите от 6 нагоре
#  @[#]+ завършва с кльомба и има хаштаг повече от веднъж




