import sys

start_list = input().split()
start_number = int(input())
new_list = []

for num in start_list:
    new_list.append(int(num))

for numbers in range(start_number):
    removed_element = sys.maxsize

    for element in new_list:
        if element < removed_element:
            removed_element = element

    new_list.remove(removed_element)

result = []
for num in new_list:
    result.append(str(num))
print(", ".join(result))
