numbers = list(map(int, input()))
numbers.sort(reverse=True)

print("".join([str(x) for x in numbers]))

