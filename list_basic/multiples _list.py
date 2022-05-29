factor = int(input())
count = int(input())

final_list = []

for number in range(1, count+1):
    new_factor = factor * number
    final_list.append(new_factor)

print(final_list)

