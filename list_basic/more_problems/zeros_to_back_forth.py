my_list = input().split(", ")

for element in my_list:
    if element == "0":
        my_list.remove(element)
        my_list.append(element[-1])

# new_list = []
# for num in my_list:
#     new_list.append(int(num))

print(list(map(int, my_list)))


