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

# започва с %
# наименувана група - първа главна буква и после малки букви 1 или няколко пъти (?P<name>[A-Z][a-z]+)
# завършва с %
# мачва всякакви чарактъри без |$%. които са ескейпнати [^\|\$\%\.] нон грийди *?
# започва с ескейпнато \<
# наименована група - всякакви чарактъри и долна черта в сикуънс (?P<product>\w+)
# завършва с ескейпнат \>
# мачва всякакви чарактъри без |$%. които са ескейпнати [^\|\$\%\.] нон грийди *?
# започва с ескейпнат \|
# наименована група - цифри в сикуънс (?P<count>\d+)
# завършва с ескейпнат \|
# мачва всякакви чарактъри без |$%. които са ескейпнати [^\|\$\%\.] нон грийди *?
# наименована група - 0 или цифри в сикуънс от 0-9, ескейпната точка и цифри от нула до 9 - 0 или няколко пъти (?P<price>0|[0-9]+[\.0-9]*)
# завършва с ескейпнат долар - \$
