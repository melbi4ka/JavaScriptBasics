start_list = input().split(" ")

final_list = []
for element in range(len(start_list)):
    current_element = -int(start_list[element])
    final_list.append(current_element)

print(final_list)
