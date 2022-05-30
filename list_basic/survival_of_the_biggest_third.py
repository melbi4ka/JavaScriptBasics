numbers_as_str = input().split()
counter = int(input())

for num in range (len(numbers_as_str)):
    numbers_as_str[num] = int(numbers_as_str[num])

for _ in range(counter):
    min_element = min(numbers_as_str)

    numbers_as_str.remove(min_element)

for num in range (len(numbers_as_str)):
    numbers_as_str[num] = str(numbers_as_str[num])

print(", ".join(numbers_as_str))
