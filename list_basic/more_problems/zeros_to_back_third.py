numbers = input().split(', ')

for i in numbers:
    if i == '0':
        numbers.append('0')
        numbers.remove('0')
print(list(map(int, numbers)))