numbers_str = input().split()
remover = int(input())
numbers = []

for num in numbers_str:
    numbers.append(int(num))

for _ in range(remover):
    numbers.remove(min(numbers))

final_numbers = []
for num in numbers:
    final_numbers.append(str(num))
print(", ".join(final_numbers))
