import re


pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"


text = input()

numbers_as_list = []
for char in text:
    if char.isdigit():
        numbers_as_list.append(int(char))

result = 1
for el in numbers_as_list:
    multiplier = result * el
    result = multiplier

matches = re.finditer(pattern,text)
cooler = []
counter = 0
for match in matches:
    word = match.group(2)
    coolnes = 0
    for char in word:
        coolnes += ord(char)
    if coolnes > result:
        cooler.append(match.group())
    counter += 1

print(f"Cool threshold: {result}")
print(f"{counter} emojis found in the text. The cool ones are:")
print("\n".join(cooler))


# патърна - започва с две точки или две звездички в група, звездичките да се ескейпнат и двете (::|\*\*)
# една голяма буква, малки букви от 2 нагоре за да станат поне 3 с голямата в група ([A-Z][a-z]{2,})
# завършва с това, което е мачнато в първа група \1


# print(result)
#      print(match.group())
#
# print(counter)
# print(cooler)
#
#



# print(result)
# print(numbers_as_list)
