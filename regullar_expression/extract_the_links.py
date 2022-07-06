import re

# pattern = r"(?P<subdomain>www\.)(?P<domain>[A-Za-z0-9]+\-?[\-A-Za-z0-9]+)(?P<extension>\.[\.a-z]+)+"
pattern = r"(?P<subdomain>www\.)(?P<domain>[A-Za-z0-9]+[\-A-Za-z0-9]*)(?P<extension>\.[\.a-z]+)+"

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
