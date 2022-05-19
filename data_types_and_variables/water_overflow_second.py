number = int(input())
free_space = 255
sum_litters = 0

for nums in range(number):
    litters = int(input())

    if free_space - litters < 0:
        print("Insufficient capacity!")
        continue

    free_space -= litters
    sum_litters += litters

print(sum_litters)
