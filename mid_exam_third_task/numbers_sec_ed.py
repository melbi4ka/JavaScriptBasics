numbers_int = [int(el) for el in input().split()]

avg = sum(numbers_int) // len(numbers_int)

list_to_be_printed = []

for el in numbers_int:
    if el > avg:
        list_to_be_printed.append(el)
        list_to_be_printed.sort(reverse=True)

if len(list_to_be_printed) == 0:
    print("No")
else:
    print(*list_to_be_printed[:5])
