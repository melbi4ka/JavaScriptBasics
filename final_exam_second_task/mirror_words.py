import re

pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
text = input()

matches = re.finditer(pattern, text)
mirror_list = []
end_list = []

for match in matches:
    mirror_list.append(match.group(2))
    mirror_list.append(match.group(3))

for el in range(0, len(mirror_list), 2):
    first_word = mirror_list[el]
    second_word = mirror_list[el+1]
    if first_word == second_word[::-1]:
        mirrors = f"{first_word} <=> {second_word}"
        end_list.append(mirrors)


if len(mirror_list) == 0 and len(end_list) == 0:
    print(f"No word pairs found!")
    print(f"No mirror words!")
else:
    print(f"{len(mirror_list)//2} word pairs found!")
    if len(end_list) == 0:
        print(f"No mirror words!")
    else:
        print(f"The mirror words are:")
        print(", ".join(end_list))

# патърна - (@|#) започва или с кльомба или с хаштаг първа група
# комбинация от главни и малки букви от 3 нагоре ([A-Za-z]{3,})
# завършва с това, което е мачнато в първа група
# продължава с това, което е мачнато в първа група
# комбинация от главни и малки букви от 3 нагоре ([A-Za-z]{3,})
# завършва с това, което е мачнато в първа група






