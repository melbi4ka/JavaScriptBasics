import re

# pattern = r"(?P<subdomain>www\.)(?P<domain>[A-Za-z0-9]+\-?[\-A-Za-z0-9]+)(?P<extension>\.[\.a-z]+)+"
pattern = r"(?P<subdomain>www\.)(?P<domain>[A-Za-z0-9]+[\-A-Za-z0-9]*)(?P<extension>\.[\.a-z]+)+"
# група субдомейн - обхваща www и точката
# група домейн - букви от a-z малки и големи и числа в низ един или няколко пъти
# и след това букви от a-z, малки и големи числа и тире в низ нула или няколко пъти
# група ехтеншън - започва с точка, малки букви от a-z и точка в низ един или няколо пъти
# и цялата група един или няколко пъти - обхваща всички точки след домейна
# pattern = r"(?P<subdomain>www\.)(?P<domain>[A-Za-z0-9]+\-?[\-A-Za-z0-9]+)(?P<extension>\.[\.a-z]+)+"
# друг работещ патърн

line = input()
while line:
    matches = re.finditer(pattern, line)
    if matches:
        for match in matches:
            subdomain = match.group("subdomain")
            domain = match.group("domain")
            extension = match.group("extension")
            print(f"{subdomain}{domain}{extension}")

    line = input()


