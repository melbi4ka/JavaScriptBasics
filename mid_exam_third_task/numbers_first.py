numbers = [int(s) for s in input().split()]


sum_numbers = sum(numbers)
average_numbers = sum_numbers // len(numbers)
above_average = []
for num in numbers:
    if num > average_numbers:
        above_average.append(num)
        above_average.sort(reverse=True)

if len(above_average) == 0:
    print("No")
else:
    print(*above_average[:5])



    # print(*[n for n in above_average if n > 5][:5])
